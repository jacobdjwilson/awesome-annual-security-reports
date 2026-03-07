# Annual Security Report 2026

## Table of Contents
- [Foreword](#foreword)
- [2025 Industry News in Review](#2025-industry-news-in-review)
- [Trends and Analysis: Data in Motion](#trends-and-analysis-data-in-motion)
  - [The Big Picture](#the-big-picture)
  - [Comparing to Previous Years](#comparing-to-previous-years)
  - [How Often is the Average Person Encountering a Threat?](#how-often-is-the-average-person-encountering-a-threat)
- [AI on Our Network](#ai-on-our-network)
- [Threats by Region](#threats-by-region)
- [TLD Analysis](#tld-analysis)
- [MSP Spotlight: The Categories MSPs Do—and Don’t—Block For Their Customers](#msp-spotlight-the-categories-msps-doand-dontblock-for-their-customers)
- [Outage Impacts Related to DNS Traffic](#outage-impacts-related-to-dns-traffic)
- [Spotlight on Current Events](#spotlight-on-current-events)
  - [Expansion of Tycoon 2FA Phishing Group](#expansion-of-tycoon-2fa-phishing-group)
  - [Lumma Stealer Exploiting CAPTCHA](#lumma-stealer-exploiting-captcha)
  - [Sporting Events and Gambling Scams](#sporting-events-and-gambling-scams)
  - [Tax Scams](#tax-scams)
  - [Travel Site Scams](#travel-site-scams)
  - [Back to School Scams](#back-to-school-scams)
  - [Shopping Scams](#shopping-scams)
  - [Hiring-related Scams](#hiring-related-scams)
  - [Open Enrollment Scams](#open-enrollment-scams)
- [Final Reflections on the Year's Threat Data](#final-reflections-on-the-years-threat-data)

---

## Foreword

Year after year, this report reinforces why DNSFilter exists: To stop real threats, in real time, at the DNS layer, before damage is done. The internet continues to grow in scale and complexity, and so do the attacks that target it.

Today, DNSFilter processes more than 200 billion DNS queries every day and blocks roughly 7% of that traffic—including hundreds of millions of threats daily. Each blocked request represents a phishing attempt that never reached a victim or malware that was never executed. These aren’t abstract metrics; they’re tangible attacks stopped before they could cause harm.

Threat activity on our network grew more than 30% over the past year, both in volume and sophistication. That trajectory isn’t slowing down. We continue to stay ahead by investing deeply in innovation and expanding what DNS-layer security can do. In 2025, we strengthened that strategy with the acquisition of Zorus, adding endpoint-based filtering through DNS PreCheck and faster incident response through CyberSight.

## 2025 Industry News in Review

Ultimately, DNS is at the center of every exploit, a tool used by adversaries to gain access or trick targets. While industry trends can vary from year to year, malware-based attacks continue to permeate the cybersecurity landscape. Ransomware is an ongoing threat to critical infrastructures everywhere, such as healthcare and supply chains. The overall cost of a data breach as reported in 2025 is now well above $4 million.[^2]

Aside from malware and ransomware, AI threats continue to grow in sophistication and complexity. With the automation capabilities of AI, this has allowed threat actors to operate more quickly and launch new exploits with little effort, including deepfakes, phishing campaigns, and AI-powered malware.

Law enforcement worked actively this past year to continue to combat cybercrime groups on the dark web. In 2025 we saw another seizure of the BreachForums domain by law enforcement only to be resurrected by a threat group called ShinyHunter.[^1] This past year, law enforcement was able to seize and takedown the forum once again. However, for every win for the industry, there is another trade off. While BreachForums was successfully taken down, this led to the “hydra” effect with the growth of a phishing-as-a-service (PhaaS) platform named Tycoon 2FA.

Beyond attacks, it’s important to address some of the DNS outages seen in the past year. In the past year we saw two notable outages from Cloudflare and AWS.[^3][^4]

## Trends and Analysis: Data in Motion

### The Big Picture

The percentage of threats uncovered on our network has continued to increase annually. The identified threats on our network grew by 30% between October 2024 and September 2025. 

![Figure 1. Percent of Threats out of Total Queries by Category]

Over this timeframe, January 2025 saw the largest amount of threat queries on our network when looking at both raw query count and by percent, with 1.02% of all requests in January categorized as malicious. By comparison, the average over this timespan was .66% of monthly requests are malicious.

### Comparing to Previous Years

![Figure 5. Percent of Threats out of Total Queries by Category - 2025 Report]

Due to a steady increase in the percentage of threats, DNSFilter processed and blocked significantly more threat queries in 2025 than in prior years. Overall, the average daily volume of threat queries grew 21.81% between this year and the last.

### How Often is the Average Person Encountering a Threat?

Last year, we reported that the average person encounters 29 threats per day. But threats have increased, and internet usage has changed. Now, the average user is likely to encounter 66 threats per day.

## AI on Our Network

Since DNSFilter released its GenAI category, we have seen the evolution of GenAI technology adoption. Between October 2024 and September 2025, our network processed more than 6 billion AI-related queries.

![Figure 6. AI Traffic Volume by Month]

## Threats by Region

The top five countries that have the highest percentage of malicious requests on our network are:

| Country | Percentage of Blocked Threats |
| :--- | :--- |
| 1. Croatia | 2.70% |
| 2. Denmark | 2.49% |
| 3. Germany | 1.23% |
| 4. Egypt | 1.09% |
| 5. Singapore | 0.79% |

## TLD Analysis

![Figure 8: Percent blocked by TLD]

When we examine the percentage of threat requests that belong to ccTLDs, these are the top five most-malicious discovered in the past year:

1. French and Southern Atlantic Lands (.tf): 87% of Traffic
2. Palau (.pw): 79% of Traffic
3. Sint Maarten (.sx): 75% of Traffic
4. Aland (.ax): 49% of Traffic
5. Faroe Island (.fo): 46% of Traffic

## MSP Spotlight: The Categories MSPs Do—and Don’t—Block For Their Customers

When comparing both MSPs and non-MSPs, most MSPs are more security conscious with a higher number of categories blocked overall. 

| Category | MSPs | Non-MSPs |
| :--- | :--- | :--- |
| Blogs & Personal Sites | 6% | 9% |
| Media Sharing | 5% | 9% |
| Streaming Media | 4% | 8% |
| Shopping | 3% | 6% |
| Generative AI Tools | 2% | 8% |

## Outage Impacts Related to DNS Traffic

![Figure 9: Domain requests and blocks by day]
![Figure 10: Total Requests]

## Spotlight on Current Events

### Expansion of Tycoon 2FA Phishing Group

In April, our research team discovered that the phishing as a service (PhaaS) group Tycoon 2FA has had significant operational changes including the platform's coordinated expansion surge in Spanish (.es) domains.

### Lumma Stealer Exploiting CAPTCHA

In August of this year we reported on how one of DNSFilter’s MSP customers discovered what first appeared to be an ordinary CAPTCHA prompt, but was discovered to be a false prompt delivering fileless malware. This discovery introduced us to infostealer malware as a service (MaaS) program called Lumma Stealer.[^8]

![Figure 11: The actual fake CAPTCHA.]

### Sporting Events and Gambling Scams

During this timeframe we saw a 15% increase in illegal streaming and torrenting traffic related to fake streaming sites. Additionally, we saw an increase in malicious domains with “football” in the domain name along with domains related to the NFL.

### Tax Scams

![Figure 13: Tax scam site traffic requests by day]

### Travel Site Scams

![Figure 14: Travel scam site traffic requests by day]

### Back to School Scams

The largest spikes in blocked requests were in October 2024 and September of 2025. September 30, 2025 had the largest spike in blocked requests in a single day throughout the year.

### Shopping Scams

![Figure 15: Shopping site traffic requests by day]

### Hiring-related Scams

Over the timeframe of April to October 2025, our data found that 8,724 domains containing the word “jobs” have been found to be malicious.

### Open Enrollment Scams

A significant spike of 1610% over the average within the past year timeframe was noted on November 18, 2025 for threat domains related to “unitedhealth”.

## Final Reflections on the Year's Threat Data

As seen over the years of releasing this report, the threat landscape and the domains used in attacks continues to change, all while expanding in reach and depth. Threats over the last year have increased over 30% compared to the previous report. AI has made every threat actor more dangerous, giving them tools to create new domains and assets to attack more quickly.

---

[^1]: https://www.bleepingcomputer.com/news/security/fbi-takes-down-breachforums-portal-used-for-salesforce-extortion/
[^2]: https://www.ibm.com/reports/data-breach
[^3]: https://blog.cloudflare.com/cloudflare-1-1-1-1-incident-on-july-14-2025/
[^4]: https://aws.amazon.com/message/101925/
[^5]: https://www.dnsfilter.com/blog/2026-cybersecurity-predictions
[^6]: https://cyberpress.org/denmark-warning-cyber-attack/
[^7]: https://www.middleeasteye.net/news/how-ramses-telecom-centre-fire-exposed-egypts-digital-vulnerability
[^8]: https://www.microsoft.com/en-us/security/blog/2025/05/21/lumma-stealer-breaking-down-the-delivery-techniques-and-capabilities-of-a-prolific-infostealer/