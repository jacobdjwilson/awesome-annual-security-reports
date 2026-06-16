# 2026 Annual Security Report

## Table of Contents
- [Foreword](#foreword)
- [2025 Industry News in Review](#2025-industry-news-in-review)
- [Trends and Analysis: Data in Motion](#trends-and-analysis-data-in-motion)
- [Comparing to Previous Years](#comparing-to-previous-years)
- [How Often is the Average Person Encountering a Threat?](#how-often-is-the-average-person-encountering-a-threat)
- [AI on Our Network](#ai-on-our-network)
- [Threats by Region](#threats-by-region)
- [TLD Analysis](#tld-analysis)
- [MSP Spotlight: The Categories MSPs Do—and Don’t—Block For Their Customers](#msp-spotlight-the-categories-msps-doand-dontblock-for-their-customers)
- [Major Internet Outages](#major-internet-outages)
- [Spotlight on Current Events](#spotlight-on-current-events)
- [Final Reflections on the Year's Threat Data](#final-reflections-on-the-years-threat-data)

---

## Foreword
Year after year, this report reinforces why DNSFilter exists: To stop real threats, in real time, at the DNS layer, before damage is done. The internet continues to grow in scale and complexity, and so do the attacks that target it.

Our job is simple: Today, DNSFilter processes more than 200 billion DNS queries every day and blocks roughly 7% of that traffic—including hundreds of millions of threats daily. Each blocked request represents a phishing attempt that never reached a victim or malware that was never executed. These aren’t abstract metrics; they’re tangible attacks stopped before they could cause harm.

Threat activity on our network grew more than 30% over the past year, both in volume and sophistication. That trajectory isn’t slowing down. We continue to stay ahead by investing deeply in innovation and expanding what DNS-layer security can do. In 2025, we strengthened that strategy with the acquisition of Zorus, adding endpoint-based filtering through DNS PreCheck and faster incident response through CyberSight.

Many security vendors rely on reactive approaches and static threat lists. That’s not enough. DNSFilter focuses on identifying and blocking threats earlier, with greater context and precision. With continued platform advancements—including URL filtering, geolocation-based IP filtering, and Zero Trust Device Isolation. We’re raising the bar for what customers should expect from a security partner.

As we expand DNSFilter’s capabilities further in 2026, our purpose remains unchanged: Protect people and organizations from real-world harm. That mission drives every decision we make, and it’s why this work matters.

CO-FOUNDER & CEO, DNSFILTER

---

## 2025 Industry News in Review
Ultimately, DNS is at the center of every exploit, a tool used by adversaries to gain access or trick targets. While industry trends can vary from year to year, malware-based attacks continue to permeate the cybersecurity landscape. Ransomware is an ongoing threat to critical infrastructures everywhere, such as healthcare and supply chains. The overall cost of a data breach as reported in 2025 is now well above $4 million[^1].

Aside from malware and ransomware, AI threats continue to grow in sophistication and complexity. With the automation capabilities of AI, this has allowed threat actors to operate more quickly and launch new exploits with little effort, including deepfakes, phishing campaigns, and AI-powered malware. Alarmingly, AI has also been successfully leveraged in brute force and credential stuffing attacks.

Law enforcement worked actively this past year to continue to combat cybercrime groups on the dark web. In 2025 we saw another seizure of the BreachForums domain by law enforcement only to be resurrected by a threat group called ShinyHunter[^2]. This past year, law enforcement was able to seize and takedown the forum once again. However, for every win for the industry, there is another trade off. While BreachForums was successfully taken down, this led to the “hydra” effect with the growth of a phishing-as-a-service (PhaaS) platform named Tycoon 2FA.

Beyond attacks, it’s important to address some of the DNS outages seen in the past year. While these outages are not commonly a result of threats or targeted attacks, their impacts can create waves of technological and network disruptions. In the past year we saw two notable outages from Cloudflare and AWS. Cloudflare’s outage in July was brief but showed the impact of how public DNS resolvers can be affected by routing/configuration issues[^3]. While AWS’s outage in October saw a bigger impact overall, it brought attention to how critical it is to cloud infrastructures[^4].

Although the cybersecurity industry continues to see an increase in the volume and sophistication of attacks, resiliency is key. One of the biggest shifts we’ve seen is how AI is increasingly becoming non-negotiable for organizations of all types, including Managed Service Providers (MSPs)[^5]. AI is being used in countless ways to make workflows more efficient, and organizations will need to be leveraging AI automation to keep up with demand. This will also require more organizations to develop a security culture that is foundational on authenticity and ethics to further emphasize resiliency rooted in proactiveness over reactivity.

It is also notable that as threats using AI increase, so are the ways in which it can be leveraged to better protect against real-world attacks. Dedication to more innovations in detection capabilities, threat intelligence, and ongoing law enforcement engagement continues to drive the fight against cybercrime adversaries.

---

## Trends and Analysis: Data in Motion

### The Big Picture
Trends evolve, but passive DNS data is a continuous measuring stick that we can hold up to the new threat landscape. It offers us the opportunity to have a clearer lens to analyze the progressive threats our network has seen over the past 12 months.

The percentage of threats uncovered on our network has continued to increase annually. The identified threats on our network grew by 30% between October 2024 and September 2025. Many of the threats distributed have remained consistent over time, with malware remaining the highest month-over-month blocked requests. It shows that organizations everywhere continue to be plagued by malware distribution.

Our network processes roughly 200 billion daily DNS queries. During the timeframe reviewed in this report (October 2024 - September 2025), we processed over 52 trillion queries.

![Figure 1. Percent of Threats out of Total Queries by Category]

Over this timeframe, January 2025 saw the largest amount of threat queries on our network when looking at both raw query count and by percent, with 1.02% of all requests in January categorized as malicious. By comparison, the average over this timespan was .66% of monthly requests are malicious.

![Figure 2. Percent of Threat Domains out of Total Domains]

When looking at the total number of unique domains trafficked by month, December 2024 saw the highest number of unique threat domains. In December 2024, 4.95% of all unique domains trafficked on our network were malicious. Following behind, October 2024 was the second highest month of unique threat domains at 4.22%. This peak season likely aligns with the highest US retail shopping period, spanning from October through December annually.

Focusing specifically on unique threat domains in 2025, the months of May and July recorded the highest volume of traffic to malicious domains on our network. During each of these months, malicious domains accounted for 4% of all unique domains observed on our network. This spike is likely correlated with the summer travel season for our users, which typically sees an increase in travel-related scams. Overall, the annual average for unique threat domains across the year was 3.78%.

Looking only at blocked queries, we found between October 2024 and September 2025 that an average of 2.44% of all blocked requests are malicious.

![Figure 3. Threat Traffic by Category]
![Figure 4. Domain count by category]

By far, the new domains category leverages the most unique domains, leveraging more than six times as many domains as the next category (malware). The phishing category uses the third-highest number of domains, but new domains as a category still uses over 7.5 times more domains than phishing.

New domains make up over 65% of all unique threat domains on the DNSFilter network. While malware queries are more active, it means that there are fewer malware domains active on our network—which is consistent with a small number of malware groups responsible for a large portion of all ransomware. These malware domains are likely attempting to “phone home” continuously at a fast rate.

The nature of new domains is that they commonly will have lower traffic overall. They can be used both legitimately and maliciously. However, they are frequently used only once or for a short period of time and then discarded, leading to a higher overall volume. This is because new domains are often testing grounds for new threats.

Another threat we see that we often don’t discuss is CSAM (child sexual abuse material) content. On the DNSFilter network, CSAM is always less than 0.00% of daily network traffic. However, despite the low query counts, we still see attempted (and always blocked) traffic to these domains on a daily basis. DNSFilter automatically blocks CSAM content and generates detailed reports on related activity. We expanded our CSAM blocklist by hundreds of thousands of domains in 2025 and saw a 5% increase in Non-Photographic Imagery (NPI) and AI-generated imagery since January 2025. In 2025, DNSFilter blocked 44% more CSAM content than the previous year.

---

## Comparing to Previous Years
![Figure 5. Percent of Threats out of Total Queries by Category - 2025 Report]

Comparing the data to the previous period from our last report, threats have continued to increase slightly year over year. While January 2025 was the highest period for the amount of threats overall across 2024 and 2025, the summer months of 2024 had the most malicious traffic in our previous report. This mirrors the seasonal traffic we saw again this year, indicating a strong correlation between summer months and increased threat activity.

Due to a steady increase in the percentage of threats, DNSFilter processed and blocked significantly more threat queries in 2025 than in prior years. Overall, the average daily volume of threat queries grew 21.81% between this year and the last. Within the timeframe of this report, at least .6% of all queries were malicious every single month, whereas in our last report there were multiple months that were under .4%.

---

## How Often is the Average Person Encountering a Threat?
Last year, we reported that the average person encounters 29 threats per day. But threats have increased, and internet usage has changed. Now, the average user is likely to encounter 66 threats per day.

This number is based on the average of 10,000 DNS requests a day which is up from the average of 5,000 in our previous report. If we kept the average daily query count from the 2025 report of 5,000 requests, the number of threats encountered would still be up nearly 14% year to year. The number of threats an average user online encounters has effectively more than doubled.

---

## AI on Our Network
Since DNSFilter released its GenAI category, we have seen the evolution of GenAI technology adoption. The implementation of AI has continued to increase over time for both malicious and legitimate use. Between October 2024 and September 2025, our network processed more than 6 billion AI-related queries.

![Figure 6. AI Traffic Volume by Month]

While GenAI traffic has increased substantially on our network, the number of GenAI domains trafficked has remained much more consistent. Our research team observed several trends surrounding the adoption of AI:
- DNSFilter processes a monthly average of 330 million AI queries and counting since January 2024.
- Organizations are more likely to block specific sites as opposed to our GenAI category specifically.
- Threat actors are using fewer “general” GenAI terms for malicious site names. Between April 2024 - April 2025, there was a 92% decrease in malicious or impersonation of GenAI sites. However, there was a rise in malicious domains that used the keyword “openai” specifically.

---

## Threats by Region
![Figure 7. Percent of Threat Requests by Region]

The top five countries that have the highest percentage of malicious requests on our network are:

| Rank | Country | Percentage of Blocked Threats |
| :--- | :--- | :--- |
| 1 | Croatia | 2.70% |
| 2 | Denmark | 2.49% |
| 3 | Germany | 1.23% |
| 4 | Egypt | 1.09% |
| 5 | Singapore | 0.79% |

Many of these countries are more developed economically and have stronger cybersecurity infrastructures. They also host a large number of data centers and Content Delivery Networks (CDNs) that could be leveraged by threat actors to host malicious domains.

The top five countries that saw the lowest volume of threats were:

| Rank | Country | Percentage of Blocked Threats |
| :--- | :--- | :--- |
| 1 | Ireland | 0.20% |
| 2 | Czech Republic | 0.19% |
| 3 | Ukraine | 0.18% |
| 4 | Portugal | 0.18% |
| 5 | Peru | 0.15% |

---

## TLD Analysis
Given that .com is generally the most popular TLD used on the web, it’s also the most popular for threat actors to utilize.

| Rank | Most Trafficked TLD | Most Blocked TLD |
| :--- | :--- | :--- |
| 1 | .com | .com |
| 2 | .google | .google |
| 3 | .net | .net |
| 4 | .google.com | .apple |
| 5 | .apple | .google.com |

When we look at which individual TLDs have the highest amount of traffic blocked overall, we see a very different top five:

| Rank | TLD | % Blocked |
| :--- | :--- | :--- |
| 1 | .pw | Approximately 100% of Traffic |
| 2 | .eu | 96% of Traffic |
| 3 | .me | 95% of Traffic |
| 4 | .de | 94% of Traffic |
| 5 | .biz | 93% of Traffic |

![Figure 8: Percent blocked by TLD]

---

## MSP Spotlight: The Categories MSPs Do—and Don’t—Block For Their Customers
Managed service providers (MSPs) hold a unique position within our industry. They often become both the IT and security experts with access to multiple organizations and their infrastructures.

Regardless of the type of organization, there is a consistent list of the top content categories that our users block on their network: 1. Botnet, 2. Phishing, 3. Malware, 4. Cryptomining, 5. Adult Content.

When comparing both MSPs and non-MSPs, most MSPs are more security conscious with a higher number of categories blocked overall. However, non-MSPs are more often to restrict web traffic for their users, likely due to internal security and risk management policies.

---

## Major Internet Outages
In the past year we saw multiple outages from vendors such as Cloudflare and AWS. Cloudflare experienced several outages in July, October, November, and December 2025. Our data shows there was a spike in malicious domain traffic with the keyword “cloudflare” after the October 2025 outage.

![Figure 9: Domain requests and blocks by day]
![Figure 10: Total Requests]

---

## Spotlight on Current Events

### Expansion of Tycoon 2FA Phishing Group
In April, our research team discovered that the phishing as a service (PhaaS) group Tycoon 2FA has had significant operational changes including the platform's coordinated expansion surge in Spanish (.es) domains. Our analysis revealed evidence that Tycoon 2FA may employ target-specific subdomain generation.

### Lumma Stealer Exploiting CAPTCHA
In August, we reported on a discovery by an MSP customer of a false CAPTCHA prompt delivering fileless malware. This discovery introduced us to infostealer malware as a service (MaaS) program called Lumma Stealer.

![Figure 11: The actual fake CAPTCHA]

### Sporting Events and Gambling Scams
Leading up to Super Bowl LIX, we saw a 15% increase in illegal streaming and torrenting traffic. There was also an increase in malicious domains with “football” in the domain name.

![Figure 12: Betting scam site traffic requests by day]

### Tax Scams
In 2025, some of the most common scams surrounding tax season involved bad actors increasing the use of tax terminology to trick individuals and evolving their tactics such as targeting fuel credits on taxes.

![Figure 13: Tax scam site traffic requests by day]

### Travel Site Scams
Between January and March, terms such as “vacation,” “travel,” and “holiday” were most regularly used to entrap unsuspecting users.

![Figure 14: Travel scam site traffic requests by day]

### Back to School Scams
Targeted textbook scams aimed at students along with school impersonation sites were the most prevalent tactics used in these types of scams.

### Shopping Scams
When we pulled data from malicious domains that contained the keyword “shop”, we saw a significant increase of 891% in early October 2025.

![Figure 15: Shopping site traffic requests by day]

### Hiring-related Scams
Over the timeframe of April to October 2025, 8,724 domains containing the word “jobs” were found to be malicious. 88% of malicious domains containing hiring-related keywords were newly registered or newly observed.

### Open Enrollment Scams
Our data showed there was a sustained spike in threat domains related to the keyword “insurance” throughout November and December of 2025.

---

## Final Reflections on the Year's Threat Data
As seen over the years of releasing this report, the threat landscape and the domains used in attacks continues to change, all while expanding in reach and depth. Threats over the last year have increased over 30% compared to the previous report. AI has made every threat actor more dangerous, giving them tools to create new domains and assets to attack more quickly.

The average user encounters 66 malicious queries per day, creating a significant risk to end users everywhere and businesses as a whole. Our report emphasizes the need for proactive security measures that take into account not only blatant malicious activity but also the periodic trends seen throughout the year.

[^1]: https://www.ibm.com/reports/data-breach
[^2]: https://www.bleepingcomputer.com/news/security/fbi-takes-down-breachforums-portal-used-for-salesforce-extortion/
[^3]: https://blog.cloudflare.com/cloudflare-1-1-1-1-incident-on-july-14-2025/
[^4]: https://aws.amazon.com/message/101925/
[^5]: https://www.dnsfilter.com/blog/2026-cybersecurity-predictions