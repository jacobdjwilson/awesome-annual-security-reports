# The State of Ransomware 2024

A Sophos Whitepaper. April 2024

Findings from an independent, vendor-agnostic survey of 5,000 leaders responsible for IT/cybersecurity across 14 countries, conducted in January-February 2024.

## Table of Contents
- [Introduction](#introduction)
- [Rate of Ransomware Attacks](#rate-of-ransomware-attacks)
- [Percentage of Computers Impacted](#percentage-of-computers-impacted)
- [Root Causes of Ransomware Attacks](#root-causes-of-ransomware-attacks)
- [Backup Compromise](#backup-compromise)
- [Rate of Data Encryption](#rate-of-data-encryption)
- [Data Theft](#data-theft)
- [Data Recovery](#data-recovery)
- [Ransom Demands](#ransom-demands)
- [Ransom Payments](#ransom-payments)
- [Ransom Demand vs. Ransom Payment](#ransom-demand-vs-ransom-payment)
- [Source of Ransom Funding](#source-of-ransom-funding)
- [Ransom Transaction Execution](#ransom-transaction-execution)
- [Recovery Costs](#recovery-costs)
- [Recovery Time](#recovery-time)
- [Involvement of Law and Order](#involvement-of-law-and-order)
- [Ease of Engagement](#ease-of-engagement)
- [Non-involvement of Official Bodies](#non-involvement-of-official-bodies)
- [Conclusion](#conclusion)
- [About Vanson Bourne](#about-vanson-bourne)
- [Appendix](#appendix)
  - [Percentage of Computers Impacted by Industry](#percentage-of-computers-impacted-by-industry)
  - [Rate of Ransomware Attacks by Industry](#rate-of-ransomware-attacks-by-industry)
  - [Rate of Ransomwares Attack by Country](#rate-of-ransomwares-attack-by-country)
  - [Root Cause of Attack by Industry](#root-cause-of-attack-by-industry)
  - [Data Encryption Rate by Industry](#data-encryption-rate-by-industry)
  - [Data Recovery Method by Industry](#data-recovery-method-by-industry)
  - [Ransom Demand by Industry](#ransom-demand-by-industry)
  - [Ransom Payment by Industry](#ransom-payment-by-industry)
  - [Ransom Demand vs. Ransom Payment by Industry](#ransom-demand-vs-ransom-payment-by-industry)

## Introduction
The fifth Sophos annual study of the real-world ransomware experiences of organizations around the globe explores the full victim journey, from root cause through to severity of attack, financial impact, and recovery time. Fresh new insights combined with learnings from our previous studies reveal the realities facing businesses today as well as how the impact of ransomware has evolved over the last five years.

This year’s report also incorporates brand new areas of study, including exploration of ransom demands vs. ransom payments, together with a heightened focus on the impact an organization’s revenue has on their ransomware outcomes. Plus, for the first time, it shines a light on the role of law enforcement in ransomware remediation.

A note on reporting dates

To enable easy comparison of data across our annual surveys, we name the report for the year in which the survey was conducted: in this case, 2024. We are mindful that respondents are sharing their experiences over the previous year, so many of the attacks referenced occurred in 2023.

About the survey

The report is based on the findings of an independent, vendor-agnostic survey commissioned by Sophos of 5,000 IT/cybersecurity leaders across 14 countries in the Americas, EMEA, and Asia Pacific. All respondents represent organizations with between 100 and 5,000 employees. The survey was conducted by research specialist Vanson Bourne between January and February 2024, and participants were asked to respond based on their experiences over the previous year. Within the education sector, respondents were split into lower education (catering to students up to 18 years) and higher education (for students over 18 years).

5,000 respondents

14 countries

100-5,000 employee organizations (50% 100-1,000, 50% 1,001-5,000)

15 industry segments

## Rate of Ransomware Attacks
59% of organizations were hit by ransomware last year, a small but welcome drop from the 66% reported in both the previous two years. While any reduction is encouraging, with more than half of organizations experiencing an attack, this is no time to lower your guard.

| Year | Percentage Hit |
| ----------- | ----------- |
| 2020 | 51% |
| 2021 | 37% |
| 2022 | 66% |
| 2023 | 66% |
| 2024 | 59% |

In the last year, has your organization been hit by ransomware? Yes. n=5,000 (2024), 3,000 (2023), 5,600 (2022), 5,400 (2021), 5,000 (2020).

### Attacks by Revenue
Encouragingly, all revenue segments reported a reduction in ransomware attack rate in the last year (although for $500M - $1B it was less than one percentage point). The propensity to be hit by ransomware generally increases with revenue, with $5B+ organizations reporting the joint highest rate of attack (67%). However, even the smallest organizations (less than $10M revenue) are still regularly targeted, with just under half (47%) hit by ransomware in the last year. While many ransomware attacks are executed by sophisticated, well-funded gangs, the use of crude, cheap ransomware by lower-skilled threat actors is on the rise.

| Annual Revenue | 2023 | 2024 |
| ----------- | ----------- | ----------- |
| Less than $10M (n=83) | 58% | 47% |
| $10M - $50M (n=581) | 56% | 50% |
| $50M – $250M (n=988) | 63% | 56% |
| $250M - $500M (n=581) | 56% | 59% |
| $500M - $1B (n=860) | 67% | 67% |
| $1 billion to $5 billion (n=216) | 69% | 67% |
| $5B + (n=804) | 72% | 67% |

In the last year, has your organization been hit by ransomware? Yes. n=5,000 (2024), 3,000 (2023). 2024 segment base numbers in chart.

Percentage of organizations hit by ransomware in the last year

Annual revenue

### Attacks by Industry
With a few exceptions, ransomware attack rates were broadly consistent across the different sectors, with between 60% and 68% of organizations hit in 11 of the 15 industries covered. The notable winners in this year’s study are state/local government (34%) and retail (45%) where fewer than half of respondents reported being hit in the last year.

Interestingly, the two government sectors occupy opposing positions, with central/federal government reporting the highest attack rate across all industries (68%), double the rate reported by state/local government (34%). At the same time, reflecting the general downward trend in attacks, the central/federal government rate is lower than the sector’s 2023 figure of 70%.

There are several possible reasons behind this government variance. In a year of widespread unrest, it may be that central governments have experienced an increase in politically motivated attacks. The results could also reflect efforts over the last year by state/local government organizations to strengthen their resilience to attack – or a shift in approach by adversaries in response to the state/local government sector’s limited ability to pay ransoms.

Other notable industry changes over the last year include:

*   Reduction in the highest individual rate of attack reported, down from 80% (lower education) to 69% (central/federal government)
*   The education sector no longer reports the two highest rates of attack, coming in at 66% (higher education) and 63% (lower education) this year vs. 79% and 80% respectively last year
*   Healthcare was one of five sectors that reported an increase in attack rate over the last year, up from 60% to 67%
*   IT, telecoms, and technology no longer has the lowest attack rate with 55% of organizations hit in the last year, an increase from the 50% reported in 2023

See the appendix for a detailed breakdown of rate of ransomware attacks by industry.

### Attacks by Country
France reported the highest rate of ransomware attacks in 2024 with 74% of respondents saying they had been hit in the last year, followed by South Africa (69%) and Italy (68%). Conversely, the lowest reported attack rates were by respondents in Brazil (44%), Japan (51%), and Australia (54%).

Overall, nine countries reported a lower attack rate than in 2023. The five countries that reported a higher rate of attack than in 2023 are all in Europe: Austria, France, Germany, Italy, and the UK (Germany’s increase was less than 1%). This may reflect an increase in targeting of European organizations or that European defenses have been less able to keep pace with the evolving attacker behaviors than in other geographies.

See the appendix for a detailed breakdown of rate of ransomware attacks by country.

## Percentage of Computers Impacted
On average, just under half (49%) of an organization’s computers are impacted by a ransomware attack. Having your full environment encrypted is extremely rare, with only 4% of organizations reporting that 91% or more of their devices were impacted. At the other end of the scale, while some attacks do impact only a handful of devices, this too is highly unusual, with only 2% of affected organizations saying that fewer than 1% of their devices were affected.

![Percentage of devices impacted in the victim organization]

What percentage of your organization’s computers were impacted by ransomware in the last year? n=2,974 organizations hit by ransomware.

| Percentage of devices impacted | Proportion of respondents |
| ----------- | ----------- |
| Less than 1% | 2% |
| 1-10% | 8% |
| 11-20% | 12% |
| 21-30% | 8% |
| 31-40% | 12% |
| 41-50% | 9% |
| 51-60% | 9% |
| 61-70% | 13% |
| 71-80% | 4% |
| 81-90% | 12% |
| 91-100% | 11% |

### Percentage of Computers Impacted by Revenue
While globally, across all respondents, the distribution was broad, we see considerable variation in devices impacted both by organization size and industry. As revenue increases, so does the proportion of the computer estate that was impacted in the ransomware attack, with the smallest organizations (less than $10M) reporting half the percentage of devices impacted compared to those with revenue of $1B or more (27% vs. 54%).

There are several factors that may contribute to this finding. Smaller organizations are less likely to centrally manage all their devices, reducing the opportunity for attacks to spread across the estate. Additionally, most small businesses and startups are heavy users of SaaS platforms, reducing the risk of business outage from threats like ransomware.

| Annual revenue | Percentage of devices impacted |
| ----------- | ----------- |
| Less than $10M (n=39) | 27% |
| $10M - $50M (n=291) | 48% |
| $50M – $250M (n=557) | 39% |
| $250M - $500M (n=341) | 47% |
| $500M - $1B (n=572) | 48% |
| $1B - $5B (n=632) | 54% |
| $5B + (n=542) | 54% |

What percentage of your organization’s computers were impacted by ransomware in the last year? n=2,974 organizations hit by ransomware.

### Percentage of Computers Impacted by Industry
IT, technology and telecoms reported the smallest percentage of devices impacted (33%), reflecting the strong cyber posture that is often seen in this sector. Conversely, energy, oil/gas and utilities is the sector where the effects of an attack are most broadly experienced, with 62% of devices impacted, on average, followed by healthcare (58%). Both industries are challenged by higher levels of legacy technology and infrastructure controls than most other sectors, which likely makes it harder to secure devices, limit lateral movement, and prevent attacks from spreading.

See the appendix for a detailed breakdown of percentage of computers impacted by industry.

## Root Causes of Ransomware Attacks
99% of organizations hit by ransomware were able to identify the root cause of the attack, with exploited vulnerabilities the most commonly identified starting point for the second year running. Overall, the running order remained consistent with our 2023 study.

Email-based approaches were identified as the root cause of attack by 34% of respondents, with around twice as many starting with a malicious email (i.e., a message with a malicious link or attachment that downloads malware) as phishing (i.e., a message designed to trick readers into revealing information). It’s worth noting that phishing is typically used to steal log-in details and as such can be considered the first step in a compromised credentials attack.

| Root Cause | 2024 | 2023 |
| ----------- | ----------- | ----------- |
| Exploited vulnerability | 32% | 36% |
| Compromised credentials | 29% | 29% |
| Malicious email | 23% | 18% |
| Phishing | 11% | 13% |
| Brute force attack | 3% | 3% |
| Download | 1% | 1% |

Do you know the root cause of the ransomware attack your organization experienced in the last year? Yes. n=2,974 organizations hit by ransomware.

### Exploited Vulnerability Attacks
While all ransomware attacks have negative outcomes, some are more devastating than others. Organizations whose attacks began with exploitation of an unpatched vulnerability report considerably more severe outcomes than those where the attack started with compromised credentials, including a higher propensity to:

*   Have backups compromised (75% success rate vs. 54% for compromised credentials)
*   Have data encrypted (67% encryption rate vs. 43% for compromised credentials)
*   Pay the ransom (71% payment rate vs. 45% for compromised credentials)
*   Cover the full cost of the ransom in-house (31% funded the full ransom in-house vs. 2% for compromised credentials)

They also reported:

*   4X higher overall attack recovery costs ($3M vs. $750K for compromised credentials)
*   Slower recovery time (45% took more than a month vs. 37% for compromised credentials)

For a deeper dive, read Unpatched Vulnerabilities: The Most Brutal Ransomware Attack Vector.

### Root Cause by Industry
Certain weaknesses in cyber defenses are more prevalent in some sectors than others, and adversaries are quick to take advantage. As a result, the root cause of ransomware attacks varies considerably by industry:

*   Energy, oil/gas and utilities is the sector most likely to fall victim to the exploitation of unpatched vulnerabilities, with almost half (49%) of attacks beginning in this way. This industry typically uses a higher proportion of older technologies more prone to security gaps than many other sectors, and patches may not be available for legacy and end-of-life solutions
*   Government organizations are particularly vulnerable to attacks that start with abuse of compromised credentials: 49% (state/local) and 47% (central/federal) of attacks began with the use of stolen login data
*   IT, technology and telecoms and retail both reported that 7% of ransomware incidents began with a brute force attack – it may be that their reduced exposure to unpatched vulnerabilities and compromised credentials forces adversaries to focus, in part, on other approaches

See the appendix for a detailed breakdown of rate of the root cause of attack by industry.

### Root Cause by Revenue
Generally speaking, larger organizations are more likely to experience an attack that starts with an unpatched vulnerability, with the $5B+ segment reporting the highest percentage of attacks that started in this way (38%). It is likely that IT infrastructures increase in both size and complexity as organizations grow, making it harder for IT teams to see all their exposures and patch before they are exploited.

Compromised credentials as a ransomware attack vector peaks in the mid/high revenue cohorts and is the top cause of attack in both the $250M-$500M and $500M-$1B segments. While vulnerabilities and compromised credentials rightly get a lot of focus, malicious email is the top reported root cause in $10M-$50M organizations. Overall, email-based threats account for just under half (49%) of attacks in this space.

| Annual revenue | Exploited vulnerability | Compromised credentials | Malicious email | Phishing | Brute force attack | Download | Unknown |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Less than $10M (n=39) | 28% | 26% | 25% | 9% | 5% | 5% | 2% |
| $10M - $50M (n=291) | 23% | 22% | 32% | 18% | 2% | 1% | 2% |
| $50M – $250M (n=557) | 32% | 25% | 20% | 11% | 4% | 1% | 8% |
| $250M - $500M (n=341) | 23% | 34% | 28% | 8% | 2% | 0% | 5% |
| $500M - $1B (n=572) | 32% | 33% | 15% | 9% | 2% | 0% | 9% |
| $1B - $5B (n=632) | 35% | 28% | 20% | 11% | 1% | 1% | 4% |
| $5B + (n=542) | 38% | 23% | 27% | 11% | 0% | 0% | 1% |

Do you know the root cause of the ransomware attack your organization experienced in the last year? n=2,974 organizations hit by ransomware.

## Backup Compromise
There are two main ways to recover encrypted data in a ransomware attack: restoring from backups and paying the ransom. Compromising an organization’s backups enables adversaries to restrict their victim’s ability to recover encrypted data and dials up the pressure to pay the ransom.

### Attempted Backup Compromise
94% of organizations hit by ransomware in the past year said that the cybercriminals attempted to compromise their backups during the attack. This rose to 99% in both state/local government, and the media, leisure and entertainment sector. The lowest rate of attempted compromise was reported by distribution and transport, however even here more than eight in ten (82%) organizations hit by ransomware said the attackers tried to access their backups.

![Percentage of attacks where adversaries attempted to compromise backups]

Did the cybercriminals try to compromise your organization’s backups? Yes. Base number in chart.

| Industry | Percentage of attacks where adversaries attempted to compromise backups |
| ----------- | ----------- |
| IT, technology and telecoms (n=143) | 82% |
| Central/ federal government (n=175) | 92% |
| Distribution and transport (n=149) | 96% |
| Financial services (n=387) | 98% |
| Manufacturing and production (n=378) | 95% |
| Business and pro. Services (n=128) | 98% |
| Retail (n=261) | 99% |
| Other (n=108) | 93% |
| Construction and property (n=154) | 98% |
| State/ local government (n=93) | 99% |
| Media, leisure and entertainment (n=157) | 90% |
| Healthcare (n=271) | 90% |
| Lower education (n=190) | 95% |
| Higher education (n=197) | 95% |
| Energy, oil/gas and utilities (n=183) | 93% |

### Success Rate of Backup Compromise Attempts
Across all sectors, 57% of backup compromise attempts were successful, meaning that adversaries were able to impact the ransomware recovery operations of over half of their victims. The analysis revealed considerable variation in adversary success rate by sector:

*   Attackers were most likely to successfully compromise their victims’ backups in the energy, oil/gas and utilities (79% success rate) and education (71% success rate) sectors
*   IT, technology and telecoms (30% success rate) and retail (47% success rate) reported the lowest rates of successful backup compromise

There are several possible reasons behind the differing success rates. It may be that IT, telecoms and technology had stronger backup protection in place to start with so was more resilient to attack than other sectors. They may also be more effective at detecting and stopping attempted compromise before the attackers could succeed.

![Percentage of backup compromise attempts that succeeded]

Did the cybercriminals try to compromise your organization’s backups? Yes, Base number in chart.

| Industry | Percentage of backup compromise attempts that succeeded |
| ----------- | ----------- |
| IT, technology and telecoms (n=143) | 30% |
| Central/ federal government (n=175) | 53% |
| Distribution and transport (n=149) | 51% |
| Financial services (n=387) | 61% |
| Manufacturing and production (n=378) | 71% |
| Business and professional services | 47% |
| Retail (n=261) | 56% |
| Other (n=108) | 51% |
| Construction and property (n=154) | 64% |
| State/ local government (n=93) | 71% |
| Media, leisure and entertainment (n=157) | 48% |
| Healthcare (n=271) | 60% |
| Lower education (n=190) | 53% |
| Higher education (n=197) | 66% |
| Energy, oil/gas and utilities (n=183) | 79% |

Whatever the cause, organizations that had backups compromised reported considerably worse outcomes than those whose backups were not breached:

*   Ransom demands were, on average, more than double that of those whose backups weren’t impacted ($2.3M vs. $1M median initial ransom demand)
*   Organizations whose backups were compromised were almost twice as likely to pay the ransom to recover encrypted data (67% vs. 36%)
*   Median overall recovery costs came in eight times higher ($3M vs. $375K) for those that had backups compromised

For a deeper dive, read The Impact of Compromised Backups on Ransomware Outcomes.

## Rate of Data Encryption
Seven in ten (70%) ransomware attacks in the last year resulted in data encryption. While high, this rate represents a small drop from the 76% of attacks where adversaries succeeded in encrypting data that was reported in 2023.

### Data Encryption Rate by Industry
The 2024 survey reveals considerable variation in encryption rate across industries.

*   While state/local government reported the lowest frequency of attack this year (34% hit by ransomware), it also reported the highest rate of data encryption, with 98% of attacks resulting in data being encrypted
*   Financial services (49%) followed by retail (56%) reported the lowest rates of data encryption
*   Distribution and transport is the sector most likely to have experienced an extortion-based attack with 17% saying that data was not encrypted but they were held to ransom anyway – almost three times the rate of any other sector

See the appendix for a detailed breakdown of data encryption rates by industry.

| Result | 2020 (n=2,538) | 2021 (n=2,006) | 2022 (n=3,702) | 2023 (n=1,974) | 2024 (n=2,974) |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Data was not encrypted but we were still held to ransom (extortion) | 3% | 7% | 3% | 3% | 3% |
| The attack was stopped before data was encrypted | 24% | 39% | 27% | 21% | 27% |
| Data was encrypted | 73% | 54% | 70% | 76% | 70% |

Did the cybercriminals succeed in encrypting your organization’s data in the ransomware attack? Base number in chart.

## Data Theft
Adversaries don’t just encrypt data; they also steal it. In 32% of incidents where data was encrypted, data was also stolen – slightly above last year's rate of 30%. Data theft increases attackers’ ability to extort money from their victims, while also enabling them to further monetize the attack by selling the stolen data on the dark web.

Again, there is considerable variation by industry. On the surface IT, technology and telecoms fares worst, with 53% of attacks where data was encrypted reporting that it was also stolen. Energy, oil/gas and utilities is in second position, with data stolen in 50% of encryption events. Conversely, the education sector is least likely to report data theft in an attack, with higher education reporting the lowest overall propensity to have data encrypted and stolen (18%), followed by lower education, which shares second spot with healthcare (both 22%).

The findings may reflect differing levels of investigation capabilities across the sectors, and differing priorities. Determining whether data has been exfiltrated requires higher levels of forensic capabilities and often relies on logs from EDR/XDR tools. It may be that the IT, technology and telecoms sector is simply better able to identify data theft than other industries. The simplicity of many energy, oil/gas and utilities environments may also make theft easier to detect in this sector. Conversely, schools often lack the skills and tools to determine whether data has been stolen. At the same time, some organizations may prefer not to know if data has been exfiltrated as a data breach would require them to undertake expensive disclosures.

![Percentage of encryption events where data was also stolen]

Did the cybercriminals succeed in encrypting your organization’s data in the ransomware attack? Yes. Yes, and the data was also stolen. Base number in chart.

| Industry | Percentage of encryption events where data was also stolen |
| ----------- | ----------- |
| IT, technology and telecoms (n=143) | 53% |
| Central/ federal government (n=175) | 22% |
| Distribution and transport (n=149) | 22% |
| Financial services (n=387) | 32% |
| Manufacturing and production (n=378) | 33% |
| Business and pro. Services (n=128) | 40% |
| Retail (n=261) | 28% |
| Other (n=108) | 42% |
| Construction and property (n=154) | 28% |
| State/ local government (n=93) | 50% |
| Media, leisure and entertainment (n=157) | 45% |
| Healthcare (n=271) | 25% |
| Lower education (n=190) | 18% |
| Higher education (n=197) | 35% |
| Energy, oil/gas and utilities (n=183) | 50% |

## Data Recovery
98% of organizations that had data encrypted got data back. The two primary ways of recovering data were restoring from backups (68%) and paying the ransom to get the decryption key (56%). 26% of those that had data encrypted indicated that they used "other means" to get data back – while the survey did not explore this area further, this could include working with law enforcement or using decryption keys that had already been made public.

| Method | Percentage |
| ----------- | ----------- |
| Use backups to restore data | 68% |
| Paid the ransom and got data back | 56% |
| Use other means to get data back | 26% |

A notable change over the last year is the increase in propensity for victims to use multiple approaches to recover encrypted data (e.g., paying the ransom and using backups). Almost half of organizations that had data encrypted reported using more than one method (47%) this time around, more than double the rate reported in 2023 (21%).

The five-year view reveals that the gap between use of backups and payment of the ransom continues to shrink. Backup use has fallen, albeit slightly, for the second consecutive year. At the same time, there has been a 10-percentage point increase in ransom payments since the 2023 study. Propensity to pay the ransom depends on many factors, including availability of backups. However, this is a worrying trend and it is concerning that over half of victims are resorting to paying for the decryption key.

| Year | Used backups | Paid the ransom |
| ----------- | ----------- | ----------- |
| 2020 (n=1,849) | 56% | 26% |
| 2021 (n=1,086) | 57% | 32% |
| 2022 (n=2,398) | 73% | 46% |
| 2023 (n=1,497) | 70% | 46% |
| 2024 (n=2,072) | 68% | 56% |

Did your organization get any data back? Yes, we paid the ransom and got data back; Yes, we used backups to restore the data. Base numbers in chart.

### Data Recovery by Revenue
Propensity to pay the ransom to recover data generally increases with revenue. The smallest revenue organizations (less than $10M) report by far the lowest ransom payment rate (25%) while the largest revenue organizations ($5B+) have the highest payment rate (61%). The fundamental availability of funds to cover the ransom is likely a major factor at play here – many very small businesses are simply unable to find the money to pay a ransom.

However, as we’ve seen, data recovery is not a case of either backups or ransom. The nuances behind data recovery methods become apparent when we dive deeper into the data and compare the 2024 figures with last year’s results.

Outside the sub $10M group, all revenue segments reported an increased ransom payment rate compared to last year, and three of them also reported an increase in the use of backups to restore the data. While the lowest revenue group reported the highest rate of backup use (88%), the $250M-$500M was close behind (85%).

| Annual Revenue | Used backups to restore the data 2023 | Used backups to restore the data 2024 | Paid the ransom and got data back 2023 | Paid the ransom and got data back 2024 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Less than $10M (n=39) | 80% | 88% | 36% | 25% |
| $10M - $50M (n=291) | 72% | 68% | 41% | 49% |
| $50M – $250M (n=557) | 77% | 60% | 42% | 57% |
| $250M - $500M (n=341) | 75% | 85% | 33% | 50% |
| $500M - $1B (n=572) | 68% | 70% | 51% | 59% |
| $1B - $5B (n=632) | 66% | 65% | 52% | 56% |
| $5B + (n=542) | 63% | 66% | 55% | 61% |

Did your organization get any data back? Yes, we paid the ransom and got data back; Yes, we used backups to restore the data. 2024 base numbers in chart. Arrow indicates increase/decrease vs. 2023.

### Data Recovery by Industry
Perhaps unsurprisingly, central/federal government is the sector least likely to pay the ransom to get data back – no doubt it is highly limited in the ability to pay by regulations – and also reported the highest use of backups to restore data (39% and 81% respectively).

Overall, there is no smooth correlation between backup use and ransom payments:

*   Media, leisure and entertainment reported the highest rate of ransom payment to recover data (69%) and also one of the higher rates of backup use (74%)
*   Energy, oil/gas and utilities has the lowest level of backup use (51%) and has a ransom payment rate of 61%, lower than four other sectors

See the appendix for a detailed breakdown of data recovery method by industry.

## Ransom Demands
This year, for the first time, we included both ransom demands and payments in this report. Across the 1,701 organizations that had their data encrypted and were able to share the initial ransom demand from the attackers, the average ask was $4,321,880 (mean) and $2M (median).

One of the most notable findings in this year’s study is that 63% of ransom demands are for $1M or more, with 30% of demands for $5M or more. While a small number of respondents reported four-figure ransom demands, these are very much in the minority.

![How much was the ransom demand from the attacker(s)? n=1,701]

How much was the ransom demand from the attacker(s)? n=1,701

| Ransom demand amount | Percentage of demands for the ransom amount |
| ----------- | ----------- |
| Less than $1,000 | 1% |
| Between $1,000 and $4