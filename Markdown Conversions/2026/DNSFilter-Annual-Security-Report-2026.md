2026
Annual Security Report

Table of Contents
01
02
03
The Big Picture 03
Comparing to Previous Years 07
How Often is the Average Person Encountering a Threat? 07
AI on Our Network 08
Threats by Region 09
TLD Analysis 11
MSP Spotlight: The Categories MSPs Do—and Don’t—Block For Their Customers 13
Major Internet Outages 14
Spotlight on Current Events 15
Tycoon 2FA 15
Lumma Stealer 16
Sporting Events and Gambling Scams 16
Tax and Travel Scams 17
Back to School and Shopping Scams 18
Hiring and Open Enrollment Scams 19
20

Foreword
Year after year, this report reinforces why DNSFilter exists: To stop real threats,
in real time, at the DNS layer, before damage is done. The internet continues to
grow in scale and complexity, and so do the attacks that target it.
Our job is simple:
Today, DNSFilter processes more than 200 billion DNS queries every day and blocks roughly 7% of
that traffic—including hundreds of millions of threats daily. Each blocked request represents a
phishing attempt that never reached a victim or malware that was never executed. These aren’t
abstract metrics; they’re tangible attacks stopped before they could cause harm.
Threat activity on our network grew more than 30% over the past year, both in volume and
sophistication. That trajectory isn’t slowing down. We continue to stay ahead by investing deeply in
innovation and expanding what DNS-layer security can do. In 2025, we strengthened that strategy
with the acquisition of Zorus, adding endpoint-based filtering through DNS PreCheck and faster
incident response through CyberSight.
Many security vendors rely on reactive approaches and static threat lists. That’s not enough.
DNSFilter focuses on identifying and blocking threats earlier, with greater context and precision.
With continued platform advancements—including URL filtering, geolocation-based IP filtering, and
Zero Trust Device Isolation. We’re raising the bar for what customers should expect from a security
partner.
As we expand DNSFilter’s capabilities further in 2026, our purpose remains unchanged: Protect
people and organizations from real-world harm. That mission drives every decision we make, and it’s
why this work matters.
CO-FOUNDER & CEO, DNSFILTER
DNSFILTER ANNUAL SECURITY REPORT 01

2025 Industry News in Review
Ultimately, DNS is at the center of every exploit, a tool used by adversaries to gain access or trick targets.
While industry trends can vary from year to year, malware-based attacks continue to permeate the
cybersecurity landscape. Ransomware is an ongoing threat to critical infrastructures everywhere, such as
healthcare and supply chains. The overall cost of a data breach as reported in 2025 is now well above $4
million1.
Aside from malware and ransomware, AI threats continue to grow in sophistication and complexity. With
the automation capabilities of AI, this has allowed threat actors to operate more quickly and launch new
exploits with little effort, including deepfakes, phishing campaigns, and AI-powered malware. Alarmingly, AI
has also been successfully leveraged in brute force and credential stuffing attacks.
Law enforcement worked actively this past year to continue to combat cybercrime groups on the dark web.
In 2025 we saw another seizure of the BreachForums domain by law enforcement only to be resurrected by
a threat group called ShinyHunter.2 This past year, law enforcement was able to seize and takedown the
forum once again. However, for every win for the industry, there is another trade off. While BreachForums
was successfully taken down, this led to the “hydra” effect with the growth of a phishing-as-a-service
(PhaaS) platform named Tycoon 2FA.
Beyond attacks, it’s important to address some of the DNS outages seen in the past year. While these
outages are not commonly a result of threats or targeted attacks, their impacts can create waves of
technological and network disruptions. In the past year we saw two notable outages from Cloudflare and
AWS. Cloudflare’s outage in July was brief but showed the impact of how public DNS resolvers can be
affected by routing/configuration issues.3 While AWS’s outage in October saw a bigger impact overall, it
brought attention to how critical it is to cloud infrastructures.4
Although the cybersecurity industry continues to see an increase in the volume and sophistication of
attacks, resiliency is key. One of the biggest shifts we’ve seen is how AI is increasingly becoming non-
negotiable for organizations of all types, including Managed Service Providers (MSPs).5 AI is being used in
countless ways to make workflows more efficient, and organizations will need to be leveraging AI
automation to keep up with demand. This will also require more organizations to develop a security culture
that is foundational on authenticity and ethics to further emphasize resiliency rooted in proactiveness over
reactivity.
It is also notable that as threats using AI increase, so are the ways in which it can be leveraged to better
protect against real-world attacks. Dedication to more innovations in detection capabilities, threat
intelligence, and ongoing law enforcement engagement continues to drive the fight against cybercrime
adversaries.
1 https://www.ibm.com/reports/data-breach
2https://www.bleepingcomputer.com/news/security/fbi-takes-down-breachforums-portal-used-for-salesforce-extortion/
3https://blog.cloudflare.com/cloudflare-1-1-1-1-incident-on-july-14-2025/
4https://aws.amazon.com/message/101925/
5 https://www.dnsfilter.com/blog/2026-cybersecurity-predictions
DNSFILTER ANNUAL SECURITY REPORT 02

Trends and Analysis: Data in Motion
The Big Picture
Trends evolve, but passive DNS data is a continuous measuring stick that we can hold up to the new
threat landscape. It offers us the opportunity to have a clearer lens to analyze the progressive threats
our network has seen over the past 12 months.
The percentage of threats uncovered on our network has continued to increase annually. The identified
threats on our network grew by 30% between October 2024 and September 2025. Many of the threats
distributed have remained consistent over time, with malware remaining the highest month-over-
month blocked requests. It shows that organizations everywhere continue to be plagued by malware
distribution.
Our network processes roughly 200 billion daily DNS queries. During the timeframe reviewed in this
report (October 2024 - September 2025), we processed over 52 trillion queries.
Botnet Cryptomining Proxy & Filter Avoidance Translation Sites New Domains Phishing & Deceptive Malware
1.0%
0.8%
0.6%
0.4%
0.2%
0.0%
October 2024 November 2024 December 2024 January 2025 February 2025 March 2025 April 2025 May 2025 June 2025 July 2025 August 2025 September 2025
Figure 1. Percent of Threats out of Total Queries by Category
Over this timeframe, January 2025 saw the largest amount of threat queries on our network when looking at
both raw query count and by percent, with 1.02% of all requests in January categorized as malicious. By
comparison, the average over this timespan was .66% of monthly requests are malicious.
DNSFILTER ANNUAL SECURITY REPORT 03

However, domains give us a slightly different story.
5.0010%0
4.008%0
3.006%0
2.004%0
1.002%0
0.00%0
October 2024 November 2024 December 2024 January 2025 February 2025 March 2025 April 2025 May 2025 June 2025 July 2025 August 2025 September 2025
Figure 2. Percent of Threat Domains out of Total Domains
When looking at the total number of unique domains trafficked by month, December 2024 saw the
highest number of unique threat domains. In December 2024, 4.95% of all unique domains trafficked on
our network were malicious. Following behind, October 2024 was the second highest month of unique
threat domains at 4.22%. This peak season likely aligns with the highest US retail shopping period,
spanning from October through December annually.
Focusing specifically on unique threat domains in 2025, the months of May and July recorded the
highest volume of traffic to malicious domains on our network. During each of these months, malicious
domains accounted for 4% of all unique domains observed on our network. This spike is likely correlated
with the summer travel season for our users, which typically sees an increase in travel-related scams.
Overall, the annual average for unique threat domains across the year was 3.78%.
Looking only at blocked queries, we found between October 2024 and September 2025 that an average
of 2.44% of all blocked requests are malicious.
DNSFILTER ANNUAL SECURITY REPORT 04

When we examine the breakdown of threats among themselves (removing proxy and filter avoidance),
we see that New Domains had the highest distribution of threats over this timespan, followed by
Malware and Phishing.
Translation Sites
Botnet
3.4%
1.3%
Phishing & Deceptive
Malware & Malicious
26.4%
28.2%
New Domains
40.6%
Figure 3. Threat Traffic by Category
When we examine the domains, we see a slightly more exaggerated picture:
Phishing & Deceptive
9.6%
Malware & Malicious
11.2%
New Domains
79%
Figure 4. Domain count by category
DNSFILTER ANNUAL SECURITY REPORT 05

By far, the new domains category leverages the most unique domains, leveraging more than six times as
many domains as the next category (malware). The phishing category uses the third-highest number of
domains, but new domains as a category still uses over 7.5 times more domains than phishing.
New domains make up over 65% of all unique threat domains on the DNSFilter network. While malware
queries are more active, it means that there are fewer malware domains active on our network—which is
consistent with a small number of malware groups responsible for a large portion of all ransomware. These
malware domains are likely attempting to “phone home” continuously at a fast rate. This is activity we have
observed on our network over the last 12 months.
The nature of new domains is that they commonly will have lower traffic overall. They can be used both
legitimately and maliciously. However, they are frequently used only once or for a short period of time and
then discarded, leading to a higher overall volume. This is because new domains are often testing grounds for
new threats. They are usually taken down quickly or recycled into a new set of unique URLs. Unsurprisingly,
this category has the highest domain count. However, the number of new domains is accelerating annually
and is growing faster than other categories.
Another threat we see that we often don’t discuss is CSAM (child sexual abuse material) content. On the
DNSFilter network, CSAM is always less than 0.00% of daily network traffic. However, despite the low query
counts, we still see attempted (and always blocked) traffic to these domains on a daily basis.
DNSFilter automatically blocks CSAM content and generates detailed reports on related activity. We
expanded our CSAM blocklist by hundreds of thousands of domains in 2025 and saw a 5% increase in Non-
Photographic Imagery (NPI) and AI-generated imagery since January 2025. In 2025, DNSFilter blocked 44%
more CSAM content than the previous year. Our independent reporting and research has resulted in a 60%
increase in reports to international law enforcement.
DNSFILTER ANNUAL SECURITY REPORT 06

Comparing to Previous Years
New Domains Phishing Malware Botnet Cryptomining Proxy & Filter Avoidance Translation Sites
0.010%
0.008%
0.006%
0.004%
0.002%
0.000%
Oct 2023 Nov 2023 Dec 2023 Jan 2024 Feb 2024 Mar 2024 Apr 2024 May 2024 Jun 2024 Jul 2024 Aug 2024 Sep 2024
Figure 5. Percent of Threats out of Total Queries by Category - 2025 Report
Co%mparing the data to the previous period from our last report, threats have continued to increase
slightly year over year. While January 2025 was the highest period for the amount of threats overall across
2024 and 2025, the summer months of 2024 had the most malicious traffic in our previous report. This
mirrors the seasonal traffic we saw again this year, indicating a strong correlation between summer
months and increased threat activity.
Due to a steady increase in the percentage of threats, DNSFilter processed and blocked significantly more
threat queries in 2025 than in prior years. Overall, the average daily volume of threat queries grew 21.81%
between this year and the last. Within the timeframe of this report, at least .6% of all queries were
malicious every single month, whereas in our last report there were multiple months that were under .4%.
We expect to see this remain steady over the next year.
How Often is the Average Person Encountering a Threat?
LLast year, we reported that the average person encounters 29 threats per day. But threats have increased,
and internet usage has changed. Now, the average user is likely to encounter 66 threats per day.
This number is based on the average of 10,000 DNS requests a day which is up from the average of 5,000 in
our previous report. If we kept the average daily query count from the 2025 report of 5,000 requests, the
number of threats encountered would still be up nearly 14% year to year. The number of threats an average
user online encounters has effectively more than doubled.
The quantity of threat actor activity has increased over the last year, while their methods of deception are
becoming more sophisticated and can fall into a variety of categories.
DNSFILTER ANNUAL SECURITY REPORT 07

AI on Our Network
Since DNSFilter released its GenAI category, we have seen the evolution of GenAI technology adoption.
The implementation of AI has continued to increase over time for both malicious and legitimate use.
Between October 2024 and September 2025, our network processed more than 6 billion AI-related
queries. Between November 2024 and September 2025, GenAI traffic has steadily increased month-over-
month, culminating in September 2025 with the largest spike of all: 102.13% increase over the time
period’s average.
1200000000
1000000000
800000000
600000000
400000000
200000000
0
October
2024
Nove
mber
2024
Dece
mber
2024
January
2025
February
2025
March
2025
April
2025
May
2025
June
2025
July
2025
Au
gust
2025
Septe
mber
2025
Figure 6. AI Traffic Volume by Month
While GenAI traffic has increased substantially on our network, the number of GenAI domains trafficked
has remained much more consistent, with a large increase in September 2025 which likely impacted the
increase in queries. However, domains trafficked do not always equate to more traffic. For instance, May
2025 represented more GenAI domains than August 2025 but May’s traffic was 57% lower than August.
Our research team observed several trends surrounding the adoption of AI:
DNSFilter processes a monthly average of 330 million AI queries and counting since January 2024.
Organizations are more likely to block specific sites as opposed to our GenAI category specifically. This
is likely due to companies adopting AI but wanting to restrict certain tools.
Threat actors are using fewer “general” GenAI terms for malicious site names. Instead, they are getting
much more specific. Between April 2024 - April 2025, there was a 92% decrease in malicious or
impersonation of GenAI sites. However, there was a rise in malicious domains that used the keyword
“openai” specifically.
Similar to threats, AI domains make up roughly .01% of all the traffic on our network. By comparison, social
networking is .78% of all queries on our network. Our largest categories, such as Business and IT,
represent over 5% of our network traffic.
As AI use increases, organizations have growing concerns over Shadow AI, a subset of Shadow IT that is
concerning because of the risk in leaking proprietary or confidential information. Having clear GenAI
policies, visibility into tool usage, and the ability to block these tools when necessary for IT governance is
imperative.
DNSFILTER ANNUAL SECURITY REPORT 08

Threats by Region
In reviewing the threats on our network based on regional data, we examine what locations and which
servers on our network processed the request. The data in the following map shows what percentage
of requests routed through each region is categorized as malicious.
AASSIIAA
Figure 7.  Percent of Threat Requests by Region
The top five countries that have the highest percentage of malicious requests on our network are:
Country Percentage of Blocked Threats
| 1.  | Croatia   | 2.70% |
| --- | --------- | ----- |
| 2.  | Denmark   | 2.49% |
| 3.  | Germany   | 1.23% |
| 4.  | Egypt     | 1.09% |
| 5.  | Singapore | 0.79% |
When looking at this data, it poses the question of why these countries? In our previous report, Germany
was in the top spot for threat requests on our network. However, this year Croatia has taken its place with
noticeably more threat requests.
Many of these countries listed above are more developed economically and have stronger cybersecurity
infrastructures. They also host a large number of data centers and Content Delivery Networks (CDNs) that
could be leveraged by threat actors to host malicious domains. This has made countries like Denmark a
target for nation-state attacks to telecommunications infrastructures.6
6https://cyberpress.org/denmark-warning-cyber-attack/
DNSFILTER ANNUAL SECURITY REPORT 09

In the example of Egypt, it is likely a matter of a large population creating more traffic while the
infrastructure is still growing to support it. This has made the country a vulnerable target for DDoS
attacks and other infrastructure disruptions. A structural fire to a large telecommunications provider in
July 2025 led to a temporary outage of internet and mobile phone services7. Emergency disruptions
such as this can often create the opportunity for threat actors to exploit it to their advantage.
When we look more specifically at the queries trafficked throughout US servers, only 0.68% of all
requests were malicious. This number is 44.7% higher than it was for the US in our previous report. The
highest month of threat traffic for the US was January, which aligns with overall malicious traffic on our
network.
Exploring the regions that experience a lower number of threats passing through our servers allows us
to see the comparisons across all countries.
Peru was the country with the fewest number of threats passing through our servers. The country saw
only 0.16% of threat request volume. The top five countries that saw the lowest volume of threats were:
Country Percentage of Blocked Threats
1. Ireland 0.20%
2. Czech Republic 0.19%
3. Ukraine 0.18%
4. Portugal 0.18%
5. Peru 0.15%
When looking at this data, a few of these countries have smaller populations than the ones at the top,
which can result in lower overall traffic, including threat traffic. Countries with less dense infrastructure
or less favorable conditions for anonymous hosting tend to see fewer malicious domains established
within their borders. This makes them less attractive for certain types of threat campaigns.
It’s important to consider that this is a snapshot of only DNSFilter network usage. Some of these
countries may have fewer high-risk online users which can indicate lower and safer traffic in these
regions.
7https://www.middleeasteye.net/news/how-ramses-telecom-centre-fire-exposed-egypts-digital-vulnerability
DNSFILTER ANNUAL SECURITY REPORT 10

TLD Analysis
Examining the top level domains (TLDs) that are most-trafficked and most-blocked on our network
every year gives us insight into the popularity of certain TLDs. These trends often expand beyond our
own network and show us which TLDs are leveraged by the most threat actors within that time frame.
Given that .com is generally the most popular TLD used on the web, it’s also the most popular for threat
actors to utilize. Most often .com is seen as a familiar domain, which can create a false sense of safety to
those who are targeted in an attack. For this reason it consistently remains a popular TLD for use in
attacks.
Let’s analyze the top trafficked TLDs and the most blocked TLDs by raw query volume:
|     | Most Trafficked TLD | Most Blocked TLD |             |
| --- | ------------------- | ---------------- | ----------- |
| 1.  | .com                |                  | .com        |
| 2.  | .google             |                  | .google     |
| 3.  | .net                |                  | .net        |
| 4.  | .google.com         |                  | .apple      |
| 5.  | .apple              |                  | .google.com |
This shows us that some of the most common TLDs known are often the most trafficked and blocked
by our networks. When threat actors are looking to target users, the familiarity of these domains often
is what they leverage most in their attacks.
When we look at which individual TLDs have the highest amount of traffic blocked overall, we see a
very different top five:
|     | TLD  |                               | % Blocked      |
| --- | ---- | ----------------------------- | -------------- |
| 1.  | .pw  | Approximately 100% of Traffic |                |
| 2.  | .eu  |                               | 96% of Traffic |
| 3.  | .me  |                               | 95% of Traffic |
| 4.  | .de  |                               | 94% of Traffic |
| 5.  | .biz |                               | 93% of Traffic |
This list shows us lesser common TLDs that can have a higher rate of malicious activity per domain
registered despite their unfamiliarity. Additionally, uncommon TLDs are often cheaper and easier to
register in bulk. This makes them more attractive to threat actors that aim to utilize them in targeted
campaigns with greater ease.
DNSFILTER ANNUAL SECURITY REPORT 11

This data below shows us the overall percentage of all the TLDs blocked on our network from October
2024 to September 2025:
100%
80%
60%
40%
20%
0%
.pw .eu .me .de .biz .app .ru .xyz .one .info .co .google.com .top .io .net .com .delivery .cc .org .pro .apple .google .us .club .dk
Figure 8: Percent blocked by TLD
To better understand the overall impact that malicious TLDs can have, let’s now analyze country code
top level domains (ccTLDs). ccTLDs are commonly used in threats given that these domains are low
cost or even free to obtain. In the overall threat actor ecosystem, the use of low cost or free options
allows them to leverage them for their own gain. When we examine the percentage of threat requests
that belong to ccTLDs, these are the top five most-malicious discovered in the past year:
ccTLD % Malicious
1. French and Southern
.tf 87% of Traffic
Atlantic Lands
2. Palau .pw 79% of Traffic
3. Sint Maarten .sx 75% of Traffic
4. Aland .ax 49% of Traffic
5. Faroe Island .fo 46% of Traffic
As trends with domains evolve and shift over time, this list has changed in previous publications of this
report. This shows us that domain registrars aim to continue combating malicious traffic by shutting
down domains with abuse as the volume continues to increase.
In our previous report, Sint Maarten (.sx) was the highest ccTLD with 43% of traffic. However, for this report
that amount has not only increased to 75% of traffic, but it fell into the third spot being overshadowed by
the French and Southern Atlantic Lands (.tf) at 87% and Palau (.pw) at 79%.
This is the lifecycle of a threat domain. It demonstrates to us that malicious actors will take measures and
shift their domains to utilize different ccTLDs in order to keep their threat ecosystem afloat. Visibility into
which threats (via which ccTLDs) are most prominent on your network allows you to block threats
appropriately and in a timely manner. It’s important to note also that your own network might look
different from the DNSFilter ecosystem as a whole.
DNSFILTER ANNUAL SECURITY REPORT 12

The Categories MSPs
Do—and Don’t—Block For Their Customers
Managed service providers (MSPs) hold a unique position within our industry. They often become both the IT and
security experts with access to multiple organizations and their infrastructures. This commonly puts them in the
line of fire as a prime target for cybercriminals. They find themselves needing to protect their infrastructure while
simultaneously protecting their customers' networks and data as well.
Due to this unique positioning, MSPs approach cybersecurity measures differently than those who self-manage
their own IT and security infrastructures. This can be seen based on the content categories they block within their
policies.
Regardless of the type of organization, there is a consistent list of the top content
categories that our users block on their network. This list includes:
1. Botnet 2. Phishing 3. Malware 4. Cryptomining 5. Adult Content
What differentiates MSPs from organizations that self-manage their IT and security lies in how often these
categories are added to their DNSFilter block policies.
When comparing both MSPs and non-MSPs, most MSPs are more security conscious with a higher number of
categories blocked overall. While they are more security focused, they also are an external provider that allows
their users to traffic the web at their discretion. Non-MSPs are still security focused but are more often to restrict
web traffic for their users. This is likely due to their internal security and risk management policies that limit user
web traffic to minimize threats.
Let’s next review the policy comparisons between MSPs and non-MSPs. When we look at the policies surrounding
cryptomining, 92% of all MSP policies block this category as a high-risk threat. Conversely, non-MSP organizations
block cryptomining in 89% of policies. Cryptomining is a simple but lesser known threat. It operates by computers
mining for cryptocurrency, but the real threat is resource hijacking where someone’s device is overtaken to mine
for cryptocurrency on behalf of a malicious actor, resulting in poor performance and high electric bills.
Another observed difference between MSPs and non-MSPs, social media only appears in 8% of MSP policies
compared to 13% of non-MSPs. Although social media sites are not typically viewed as threats, non-MSPs may be
more concerned with social media interfering with work related projects over ensuring user safety while browsing.
This does not minimize the potential security threat that social media can play in social engineering scams.
There are several other notable comparisons that show the difference between what MSPs are likely to block as
opposed to other organizations that self-manage their policies. Here are some of the comparisons:
MSPs Non-MSPs
Blogs & Personal Sites 6% 9%
Media Sharing 5% 9%
Streaming Media 4% 8%
Shopping 3% 6%
Generative AI Tools 2% 8%
This list shows us that MSPs are less likely to leverage content categories in filtering policies than non-MSPs.
It is likely due in part to the factor that non-MSPs prefer to have a better control of user internet access to
minimize their risk.
DNSFILTER ANNUAL SECURITY REPORT 13

Outage Impacts Related to DNS Traffic
Despite advancements in technology, internet and website outages are unfortunately not just a
possibility, but an occurrence we have all experienced. In our previous report, we reported on the
CrowdStrike outage and the aftermath of scams that followed. While these IT-related outages are not
commonly a result of direct security threats or targeted attacks, their impacts can create waves of
technological and network disruptions.
In the past year we saw multiple outages from vendors such as Cloudflare and AWS. Cloudflare
experienced several outages in July, October, November, and December 2025. Although these outages
were temporary with quick resolution, our researchers saw an uptick in malicious domains related to
these events following them. Our data shows there was a spike in malicious domain traffic with the
keyword “cloudflare” after the October 2025 outage:
14,000,000
12,000,000
10,000,000
8,000,000
6,000,000
4,000,000
2,000,000
0
October 1, 2025 Oct 06, 2025 Oct 13, 2025 Oct 20, 2025 Oct 27, 2025 Nov 03, 2025 Nov 10, 2025 Nov 17, 2025 Nov 24, 2025 Dec 01, 2025
Figure 9: Domain requests and blocks by day
At the same time, overall traffic (regardless of threat category) increased tremendously after the
October and November outages:
500,000,000
400,000,000
300,000,000
200,000,000
100,000,000
0
Oct 01, 2025 Oct 06, 2025 Oct 13, 2025 Oct 20, 2025 Oct 27, 2025 Nov 03, 2025 Nov 10, 2025 Nov 17, 2025 Nov 24, 2025 Dec 01, 2025 Dec 06, 2025 Dec 13, 2025 Dec 20, 2025 Dec 27, 2025
Figure 10: Total Requests
System outages often drive individual users to seek resolutions, creating opportunities for scammers.
When large-scale disruptions occur, effective security requires real-time blocking of emerging threats
and visibility into user behavior, which can then be used to enhance internal security training.
DNSFILTER ANNUAL SECURITY REPORT 14

Spotlight on Current Events
The various challenges encountered in 2025 provided valuable opportunities to identify several distinct
8
trends across our network.
Expansion of Tycoon 2FA Phishing Group
In April, our research team discovered that the phishing as a service (PhaaS) group Tycoon 2FA has had
significant operational changes including the platform's coordinated expansion surge in Spanish (.es)
domains. We also found evidence suggesting the threat group was increasing their highly targeted
subdomain usage patterns. This is an expansion of their platform which has been active since August
2023.
Our analysis of DNS query patterns across our 11,343 unique FQDN (fully qualified domain name) dataset
revealed evidence that Tycoon 2FA may employ target-specific subdomain generation that includes:
99.6% of subdomains received fewer than 10 total DNS queries
94.3% received fewer than 5 queries
Median query count: 2 queries per subdomain
Reviewing this usage pattern suggests most subdomains are created for specific campaigns or individual
targets rather than for broad phishing distribution. It shows us the platform's massive subdomain
generation rates with their expansion efforts while maintaining operational security through
compartmentalization.
DNSFILTER ANNUAL SECURITY REPORT 15

Lumma Stealer Exploiting CAPTCHA
In August of this year we reported on how one of
DNSFilter’s MSP customers discovered what first
appeared to be an ordinary CAPTCHA prompt, but
was discovered to be a false prompt delivering
fileless malware. This discovery introduced us to
infostealer malware as a service (MaaS) program
called Lumma Stealer.8 Threat actors were using fake
CAPTCHA prompts to inject fileless malware
designed to steal information from various browsers
and applications.
Our researchers were able to discover: Figure 11: The actual fake CAPTCHA.
This particular fake CAPTCHA was interacted with 23 times on the DNSFilter network over a three-day
period.
17% of people who encountered the fake CAPTCHA completed the steps on the screen to copy and
paste it, resulting in an attempted malware payload delivery.
The fake CAPTCHA was first observed on a Greek banking site. Two other domains were associated
with the malicious CAPTCHA: a brand-new Cloudflare Pages site (human-verify-7u[.]pages[.]dev) that
loads with an error message after clicking “I’m not a robot,” and recaptcha-manual[.]shop, which loads
outside of the browser after following the prompted commands.
Lumma Stealer showed us firsthand that not all threats are always obvious. As security measures
continue to enhance, so will the tactics that threat actors use to exploit information.
Sporting Events and Gambling Scams
Phishing scams continue to be prevalent across the industry. Earlier in the year we uncovered an increase
in the number of DNS queries to domains with gambling keywords in the domain names, both malicious
and legitimate, leading up to Super Bowl LIX.
During this timeframe we saw a 15% increase in illegal streaming and torrenting traffic related to fake
streaming sites. Additionally, we saw an increase in malicious domains with “football” in the domain
name along with domains related to the NFL. There was also an increase in the amount of traffic to fake
betting and gambling sites that coincided with both the Superbowl and the NBA playoffs.
50,000
40,000
30,000
20,000
10,000
0
October 2024 November 2024 December 2024 January 2025 February 2025 March 2025 April 2025 May 2025 June 2025 July 2025 August 2025 September 2025
Figure 12: Betting scam site traffic requests by day
Some of the most notable spikes in traffic aligned with the NBA playoffs in April as well. The highest spike
during the NFL playoffs was a 713% increase. Compared to the average over the October 2024 through
September 2025 time period, this is a 1467.94% spike overall. This shows us that threat actors will
capitalize on sporting events and betting as an avenue to scam individuals.
8https://www.microsoft.com/en-us/security/blog/2025/05/21/lumma-stealer-breaking-down-the-delivery-techniques-and-capabilities-of-a-prolific-infostealer/
DNSFILTER ANNUAL SECURITY REPORT 16

Tax Scams
Every year, tax season can be an opportunity for threat actors to exploit it for their own gain. Data we
discovered revealed a significant surge in tax-related scams in the lead-up to the tax filing deadline.
However, our data also showed us that it is a scam that remains consistent throughout the year
beyond the initial filing deadline in April.
In 2025, some of the most common scams surrounding tax season involved bad actors increasing the
use of tax terminology to trick individuals and evolving their tactics such as targeting fuel credits on
taxes.
October 12000
October 10000
October 8000
October 6000
October 4000
October 2000
October 0
October 2024 November 2024 December 2024 January 2025 February 2025 March 2025 April 2025 May 2025 June 2025 July 2025 August 2025 September 2025
Figure 13: Tax scam site traffic requests by day
The peak activity we observed for most requests and blocks per day under the keyword “tax” and “W2”
was in October 2024. This increase was in the lead up to the 2025 tax season with noticeable spikes
surrounding March - April 2025 within the core timeframe of tax season.
However, we also saw that there were minor increases in malicious requests and blocks at the end of
July/early August 2025 and end of September 2025. More specifically, September 8, 2025 saw a brief
spike in blocked traffic. This was the highest daily spike since tax season with 211% increase over the
average.
Travel Site Scams
Threat actors are consistently looking for opportunities to capitalize on phishing scams, including using
fake travel sites maliciously. Our research team found that between January and March, terms such as
“vacation,” “travel,” and “holiday” were most regularly used to entrap unsuspecting users looking for
vacation deals, tips, and offers.
20000
15000
10000
5000
0
October 2024 November 2024 December 2024 January 2025 February 2025 March 2025 April 2025 May 2025 June 2025 July 2025 August 2025 September 2025
Figure 14: Travel scam site traffic requests by day
Additionally, it was found that the end of February and September 2025 saw the two largest spikes in
malicious domains blocked. The most notable date, February 26, 2025, had the largest increase at 2311%
over the average request in this time period. These trends continued to remain steady throughout the
year and even slightly increased through the end of September 2025 with a 458% increase over average in
this time period.
DNSFILTER ANNUAL SECURITY REPORT 17

Back to School Scams
The back to school season has become another trend that threat actors will utilize to exploit for their
own gain. Data that our team had uncovered over the past year revealed various threat types targeting
students and staff as they return to class. Our research team found that targeted textbook scams
17
aimed at students along with school impersonation sites were the most prevalent tactics used in these
types of scams.
The largest spikes in blocked requests were in October 2024 and September of 2025. December 2024
also saw another moderate increase in blocked domains, while the rest of the year remained steady.
September 30, 2025 had the largest spike in blocked requests in a single day throughout the year.
Notably this has been a scam that we have seen grow over time and data suggests that this is seasonal
surrounding the back to school season.
Shopping Scams
Retail shopping scams are one of the most common scams cybercriminals use. When we pulled data
from malicious domains that contained the keyword “shop”, we saw a significant increase of 891% in
early October 2025. During the development of this report, we also saw an additional spike showing
sustained traffic throughout October and November of 2025. Although this range is outside of our
traditional timeframe scope of this report, it was important to include it in order to show how this
signals to us that threat actors are deploying retail-focused phishing campaigns well in advance of the
traditional holiday shopping season.
1000
18
800
600
400
200
0
October
2024
Nove
mber
2024
Dece
mber
2024
January
2025
February
2025
March
2025
April
2025
May
2025
June
2025
July
2025
August
2025
Septe
mber
2025
October
2025
Nove
mber
2025
Figure 15: Shopping site traffic requests by day
One of the reasons behind the retail shift that has been seen with cyber monday preparations starting
within the summer months in the US in recent years. This has likely given threat actors a larger window
of time for scam opportunities. Our team saw activity targeting the keyword “cybermonday” domains
as early as August 17, 2025. This shows the demonstration of year-round, sophisticated planning behind
seasonally based scams.
DNSFILTER ANNUAL SECURITY REPORT 18

Hiring-related Scams
Hiring-related scams have emerged as a significant and growing trend observed on our network over
the past year. New data from our networks has shown an alarming trend in domain activity related to
domains that include terms like “careers,” “hiring,” “jobs,” and “talent.” These keywords have seen a
17
significant increase since the start of 2025. Below is some of the data our researchers uncovered.
Over the timeframe of April to October 2025, our data found that:
8,724 domains containing the word “jobs” have been found to be malicious.
1,161 domains containing the word “careers” have been found to be malicious.
88% of malicious domains containing hiring-related keywords were newly registered or newly
observed.
86% of all domains using the word “jobs” that were determined to be malicious were either newly
registered or newly observed.
Researchers also discovered that a number of suspicious domain practices are being used to lure
victims into clicking malicious links, including excessive hyphens or long-winded URLs, or spoofed or
fake domains with the goal to resemble legitimate job portals. This activity coincides with the increase
in the number of job seekers in this year's unstable job market. It shows us that cybercriminals will use
uncertain economic and job market conditions to their advantage when possible.
Open Enrollment Scams
From healthcare organizations to insurance companies, the healthcare industry is often highly
targeted for attack from cybercriminals. During the development of this report, our researchers found a
noticeable increase of malicious domains used towards keywords such as “insurance” along with
largely known healthcare insurers such as “unitedhealth”, “aetna”, and “bluecross” at the start of
healthcare’s open enrollment season.
Our data showed there was a sustained spike in threat domains related to the keyword “insurance”
throughout November and December of 2025. A more significant spike of 1610% over the average
within the past year timeframe was noted on November 18, 2025 for threat domains related to
“unitedhealth”. Aetna, United, and Blue Cross Blue Shield were all insurance company names
leveraged in attacks to fool users with their malicious domains. It is also likely that threat actors have
been leveraging the legislative changes to healthcare insurance in the US and have contributed to the
increase of malicious domains related to healthcare.
DNSFILTER ANNUAL SECURITY REPORT 19

Final Reflections on the
Year's Threat Data
As seen over the years of releasing this report, the threat landscape and the domains used in attacks
continues to change, all while expanding in reach and depth. Threats over the last year have increased over
30% compared to the previous report. AI has made every threat actor more dangerous, giving them tools to
create new domains and assets to attack more quickly. DNS itself provides a window into the malicious
activity that can occur across the internet, as domains are used in nearly every type of attack.
The average user encounters 66 malicious queries per day, creating a significant risk to end users
everywhere and businesses as a whole. As threats appear in more places, using a wide array of domains and
threat types, the ability to steer clear of attacks is much more difficult.
Our report emphasizes the need for proactive security measures that take into account not only blatant
malicious activity but also the periodic trends seen throughout the year, often surfacing under the umbrella
of “new domains.” This focus is critical, as new domains alone make up over 65% of all unique threat
domains on the DNSFilter network, leveraging them more than six times as often as the next category,
Malware.
Security needs to become part of all organizational culture, not just a department within the company.
Leveraging the insights gleaned from DNS data, coupled with advanced AI-powered security solutions, is
paramount in effectively mitigating these evolving threats and safeguarding our digital future.
Book Your DNSFilter Demo Today
DNSFILTER ANNUAL SECURITY REPORT 20

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-02", "model": "gemini-3.5-flash-lite"} -->
