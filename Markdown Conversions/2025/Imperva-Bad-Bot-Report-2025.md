# 2025 Imperva Bad Bot Report

## About the Imperva Bad Bot Report

The 12th Annual Imperva Bad Bot Report explores the rapidly changing landscape of automated internet traffic, examining the increasing sophistication of bad bots and their impact on businesses. Based on invaluable insights from our Threat Research and Security Analyst Services (SAS) teams, this report highlights the latest tactics, techniques, and procedures (TTPs) of malicious bots.

Our analysis draws from data collected from across the Imperva global network in 2024, including the blocking of 13 trillion bad bot requests across thousands of domains and industries. This dataset provides key insights into bot activity to help organizations understand and address the growing risks of automated attacks.

This year’s report focuses on the growing role of Artificial Intelligence (AI) in bot attacks, significantly increasing their volume, accessibility, and ability to evade detection. Bad bots are increasingly targeting businesses through tactics like data scraping, account hijacking, and inventory manipulation for financial gain. As AI evolves, organizations must adopt advanced mitigation strategies to protect against fraud, financial losses, and security risks.

These attacks can degrade customer service, inflate prices, and limit access to products, ultimately eroding trust and loyalty. The report also provides actionable recommendations for organizations to defend against this growing threat.

Sponsored by

## Executive Summary

### The Role of AI in Bot Attacks

The rise in the number of accessible AI tools has significantly lowered the barrier for entry for cyber attackers enabling them to create and deploy malicious bots at scale. With generative AI simplifying bot development, automated threats are evolving rapidly - becoming more sophisticated, evasive, and widespread, fueling the growth of both simple and advanced bad bots. Attackers now use AI not only to generate bots but also to analyze failed attempts and refine their techniques to bypass detection with greater efficiency.

The resulting emergence of more sophisticated, evasive bad bots puts businesses at greater risk than ever before. As automated traffic volumes increase, security teams must adapt their approach to application security, facing increasing pressure to counter an evolving threat landscape in which bots are gaining the upper hand.

### Automated Traffic Surpasses Human Traffic

For the first time in a decade, automated traffic surpassed human activity, accounting for 51% of all web traffic in 2024. This was largely driven by the rapid adoption of AI and large language models (LLMs), which have made bot creation more accessible and scalable.

At the same time, bad bot activity has risen for the sixth consecutive year, with malicious bots now making up 37% of all internet traffic, a sharp increase from 32% in 2023.

![Chart showing global internet traffic profile in 2024 with percentages for Human, Bad Bot, and Good Bot.](Image description)

### GLOBAL INTERNET TR AFFIC PROFILE IN 2024

- Human: 14%
- Bad Bot: 49%
- Good Bot: 37%

The chart below illustrates the steady rise of bad bots as a percentage of total web bot traffic over the years. In 2015, bad bots accounted for just 19% of all bot traffic. Growth spiked in 2019, largely influenced by unprecedented online usage during the COVID-19 pandemic, a trend that has continued, with bad bot traffic reaching 37% in 2024.

![Line chart showing global internet traffic for the past 10 years, with lines for Human, Bad Bot, and Good Bot.](Image description)

### GLOBAL INTERNET TR AFFIC FOR THE PAST 10 YEARS

- **2015**: Human 54%, Bad Bot 19%, Good Bot 27%
- **2016**: Human 61%, Bad Bot 20%, Good Bot 19%
- **2017**: Human 58%, Bad Bot 18%, Good Bot 24%
- **2018**: Human 62%, Bad Bot 15%, Good Bot 23%
- **2019**: Human 63%, Bad Bot 13%, Good Bot 24%
- **2020**: Human 59%, Bad Bot 15%, Good Bot 26%
- **2021**: Human 58%, Bad Bot 15%, Good Bot 27%
- **2022**: Human 53%, Bad Bot 17%, Good Bot 30%
- **2023**: Human 50%, Bad Bot 18%, Good Bot 32%
- **2024**: Human 49%, Bad Bot 37%, Good Bot 14%

The sharp rise in bot traffic is alarming, and with the emergence of AI raises questions about how we can stem the flow of bot traffic to protect businesses and maintain fair markets.

### Bot Attack Sophistication Trends

In 2024, advanced and moderate bot attacks accounted for 55% of all bot attacks. Attackers increasingly employ sophisticated techniques to emulate human traffic and carry out malicious activities, making these attacks harder to detect and mitigate.

However, there has been a significant shift in the dynamics of bot attack sophistication. Simple, high-volume bot attacks have grown substantially, now comprising 45% of all bot attacks—up from 40% in 2023. This rise can be attributed to the increasing accessibility of AI-powered automation tools, which allow attackers with less technical expertise to launch bot attacks easily.

![Pie chart showing bot sophistication in 2024 with percentages for Simple, Moderate, and Advanced.](Image description)

### BOT SOPHISTICATION IN 2024

- Simple: 45%
- Moderate: 11%
- Advanced: 44%

### OWASP Automated Threats Account for Almost a Third of All Attacks

In the past year, 31% of all attacks recorded and mitigated by Imperva were automated threats, as defined by the OWASP. The OWASP 21 Automated Threats are a set of automated cyberattacks that leverage bots and scripts to exploit web application vulnerabilities at scale, bypass security controls, and disrupt businesses across various industries, and represent some of the most common and critical vulnerabilities facing web applications. Their widespread nature and the ease with which attackers exploit them make them a primary concern for any organization’s security strategy.

A deeper look into the attack types reveals that 25% of mitigated attacks were sophisticated bad bots specifically targeting and abusing business logic.

### Why Modern APIs Must Defend Against Bad Bots

In 2024, the Imperva Threat Research team observed a significant surge in API-directed attacks, with 44% of advanced bot traffic targeting APIs. This report includes a section dedicated to API Security, which looks into how bad bots targeting API business logic are a major threat to businesses and how protecting APIs is not just a security measure but safeguarding the foundation of your digital ecosystems.

### Residential Proxies Remain a Preferred Evasion Tactic

By leveraging residential proxies, bad bots can mimic legitimate traffic from a residential address, making detection more challenging. In fact, 21% of all bot attacks using internet service providers (ISPs), were conducted through residential proxies - a key evasive tactic commonly employed by advanced attackers.

### Account Takeover Attacks

The number of Account Takeover (ATO) attacks has increased significantly, rising by 40% since last year and by 54% since 2022. This surge is likely driven by cybercriminals using AI and machine learning to automate credential stuffing and brute-force attacks, making them more sophisticated and harder to detect.

![Bar chart showing the growth of ATO attacks from 2022 to 2024.](Image description)

### GROWTH OF ATO AT TACKS 2022 TO 2024

- +54%

- **2022**: [Value]
- **2023**: [Value]
- **2024**: [Value]

> “
> 25% of mitigated attacks were sophisticated bad bots specifically targeting and abusing business logic.
> ”

## Contents

- About the Imperva Bad Bot Report: 2
- Executive Summary: 3
- Key Findings in Numbers: 7
- Bot Attacks Exploit API Business Logic: 9
- The Emergence of AI-Powered Attacks: 13
- Bot Evasion Tactics: 15
- Browser Impersonation by Bad Bots: 17
- Account Takeover Attacks: 18
- Bad Bots: A Global Problem: 22
- Industry Overview: 25
  - Most Targeted Industry: 25
  - Why Bad Bots Are a Retail Nightmare: 29
- Spotlight on the Airline Industry: 30
- Case Study – Marketing Fraud: 32
  - How Bad Bots Disrupted a Global Marketing Campaign: 32
- Recommendations: 33
- Appendix: 39

## Key Findings

- **51%**: Amount of automated internet traffic.
- **37%**: Amount of internet traffic made up of bad bots.
- **14%**: Amount of internet traffic made up of good bots.
- **55%**: Proportion of advanced or moderate bot attacks in 2024.
- **45%**: Proportion of simple bot attacks in 2024.
- **44%**: Percentage of advanced bot attacks targeting APIs.
- **25%**: Percentage of bot attacks targeting business logic.
- **19%**: Percentage of account takeover attacks targeting APIs.

- **46%**: Percentage of bot attacks using Chrome to appear as legitimate traffic.
- **14%**: Percentage of all logins that were account takeover attempts.
- **31%**: Percentage of attacks that were OWASP Automated Threats.
- **2 Million**: Daily average number of AI-enabled attacks.
- **13 Trillion**: Number of bot requests blocked by Imperva in 2024.
- **40%**: Percentage growth of account takeover attacks in 2024.
- **27%**: Percentage of bot attacks targeting the travel industry in 2024.

## Bot Attacks Exploit API Business Logic

Businesses are increasingly relying on APIs, driven by the rapid expansion of digital transformation, AI-powered automation, and the growing demand for seamless integration across platforms. APIs are the backbone of modern applications, enabling businesses to connect services, streamline operations, and deliver personalized customer experiences at scale. They power everything from payment processing and supply chain management to AI-driven analytics and third-party integrations, making them essential for agility, innovation, and competitive advantage. As organizations continue to adopt cloud-based services and microservices architectures, APIs provide the critical infrastructure needed to enhance efficiency, accelerate product development, and unlock new revenue streams.

The power behind each API is its business logic —the rules and processes that dictate how it functions interacts with data and facilitates critical business operations. APIs enable automation, real-time decision-making, and seamless integrations, making them indispensable to modern businesses. However, their very functionality also makes them a prime target for bad bots, which manipulate API logic to commit fraud, scrape data, and bypass security controls.

Bad bots are no longer just overwhelming API endpoints—they are evolving to exploit the business logic that underpins these systems. Attackers deploy bots to target vulnerabilities in API workflows, automating payment fraud, account hijacking, and data exfiltration. Because API business logic is unique to each organization, traditional security measures relying on known attack signatures often fail. This allows bots to mimic legitimate user behavior and evade detection. Attackers aren’t merely testing vulnerabilities—they’re automating large-scale fraud that drains revenue, erodes customer trust, and imposes steep financial losses, regulatory penalties, and reputational damage.

The following analysis from the Imperva Threat Research team highlights how bad bots target APIs, the top industries at risk, the techniques and tactics used, and emerging attack vectors shaping the threat landscape.

### API vs. Web Applications

In 2024, the Imperva Threat Research team observed a significant surge in API-directed attacks, with 44% of advanced bot traffic targeting APIs—compared to just 10% targeting web applications. This highlights a deliberate shift by attackers toward API endpoints that handle sensitive and high-value data.

### Top Targeted Industries for Bot Attacks on APIs

Financial services, telecom, healthcare and retail are among the top ten most targeted industries for bot attacks on APIs. These sectors depend on APIs for critical operations and sensitive transactions, making them prime targets for sophisticated bot attacks.

![Pie chart showing top targeted industries for API attacks with percentages.](Image description)

### TOP TARGETED INDUSTRIES FOR API AT TACKS

- Financial Services: 24%
- Business: 7%
- Telecom & ISPs: 6%
- Healthcare: 6%
- Lifestyle: 4%
- Education: 3%
- Retail: 3%
- Computing & IT: 3%
- Society: 2%
- Travel: 2%
- Other: 40%

### API Attack Techniques & Tactics

Our analysis of 2024 API bot attacks reveal a multifaceted threat landscape, where adversaries employ a range of tactics to exploit API vulnerabilities:

![Pie chart showing percentage of API attacks by attack type.](Image description)

### PERCENTAGE OF API AT TACKS BY AT TACK T YPE

- Scraping: 31%
- Payment Fraud: 26%
- ATO: 12%
- Scalping: 11%
- User Details Harvesting: 6%
- File Upload & RCE: 4%
- Gift Card Fraud: 4%
- Session Hijacking: 2%
- Carding: 1%
- Coupon Guessing: 1%
- Administrative Interface Access: 1%
- Sensitive Data Access: 1%

### Data Scraping (~31% of API Attacks)

Bots extract vast amounts of data by exploiting APIs that expose sensitive or proprietary information. This method is favored because it enables attackers to automate the collection of valuable datasets, such as user details, product information, and internal metrics, with minimal resistance. The high volume of data scraping not only facilitates further criminal activities but could also provide competitive intelligence.

### Payment Fraud (~26% of API Attacks)

Targeting financial transaction endpoints, attackers manipulate payment processes to commit fraud. Representing roughly 26% of attacks, this technique involves exploiting vulnerabilities in checkout systems to trigger unauthorized transactions or abuse promotional mechanisms. The immediate financial impact, combined with the erosion of customer trust, makes payment fraud a highly attractive target for bad bots.

### Account Takeover (~12% of API Attacks)

Comprising around 12% of the attack landscape, account takeover attacks (ATO) leverage stolen or brute-forced credentials to gain unauthorized access to user accounts. Once in control, attackers can access sensitive personal and transactional data, often leading to broader security breaches and further exploitation.

### Scalping (~11% of API Attacks)

Scalping attacks, accounting for approximately 11%, involve bots rapidly purchasing or reserving large volumes of high-demand items or services. This tactic not only disrupts fair consumer access but also undermines market dynamics by allowing attackers to resell these items at inflated prices.

In addition to these primary techniques, our report also highlights other methods such as Gift-Card Fraud (~4), Remote Code Execution (~4%), and Session Hijacking (~2%). The common denominator across all these tactics is the exploitation of inherent API vulnerabilities, ranging from misconfigurations and insufficient rate limiting to weak authentication protocols.

### Endpoint-Specific Bot Attacks

The chart below indicates that bad bots strategically target API endpoints that handle high-value and sensitive operations. Here’s a detailed analysis of the observed trends and the probable reasons behind these attack vectors:

![Pie chart showing percentage of API attacks by endpoint.](Image description)

### PERCENTAGE OF API AT TACKS BY ENDPOINT

- Data Access: 37%
- Checkout: 32%
- Authentication: 16%
- Product: 11%
- Admin: 4%

#### Data Access Endpoints (~37% of API Attacks)

These endpoints are responsible for retrieving sensitive or proprietary information, making them a goldmine for attackers. The high attack rate of approximately 37% suggests that adversaries are heavily invested in scraping and exfiltrating data. Such data can fuel further criminal activities or serve as competitive intelligence. The attractiveness of data access endpoints stems from the sheer volume and sensitivity of the information they control, often with less stringent security measures compared to transactional endpoints. To counter this, security professionals should enhance monitoring, enforce strict access controls, and deploy anomaly detection systems to flag unusual data retrieval patterns.

#### Checkout Endpoints (~32% of API Attacks)

Critical for processing financial transactions, checkout endpoints face around 32% of all API attacks. These endpoints are a prime target because any disruption here directly impacts revenue and customer trust. Attackers exploit vulnerabilities to manipulate payment processes, commit fraud, or abuse business logic, leading to unauthorized financial activities. The significant focus on checkout processes underscores the need for robust transaction security, including real-time monitoring, layered authentication, and proactive fraud detection measures.

#### Authentication Endpoints (~16% of API Attacks)

Authentication endpoints, which facilitate identity verification and access control, account for 16% of API bot attacks. These endpoints are targeted to bypass multi-factor authentication, abuse token-based authentication, and manipulate session handling. Given that they serve as the first line of defense in securing user access, any compromise here can lead to account takeovers and broader breaches. Strengthening these endpoints with robust, dynamic authentication protocols and regular audits is crucial to mitigate the risk of unauthorized access.

Overall, the focus on data access, checkout, and authentication endpoints reflects a calculated strategy by attackers to exploit the most critical and vulnerable areas of API infrastructure.

### New Exploitation Methods

Beyond traditional tactics, bad bots are now exploiting API vulnerabilities via misconfigured third-party integrations and parameter tampering. These emerging methods enable attackers to bypass established security measures more effectively.

## The Emergence of AI-Powered Attacks

In 2024, we witnessed the growing use of AI-enabled tools in cyber attacks. Notably Imperva blocked an average of 2 million AI-powered cyber-attacks every day.

AI tools such as ChatGPT, ByteSpider Bot, ClaudeBot, Google Gemini, Perplexity AI, Cohere AI, Apple Bot and more are revolutionizing how users interact with their favorite brands, how students learn and how employees perform tasks and create content more quickly than ever before. However, these tools are also being used as a new attack vector.

In an analysis of AI tools, the Imperva Threat Research team found that most of the widely used AI-powered tools currently in circulation are being used for cyber-attacks. The distribution of bot attacks across the AI tools analyzed varied significantly. As shown in the chart below, ByteSpider Bot was responsible for 54% of all AI-enabled attacks followed by AppleBot at 26%. ClaudeBot accounted for 13%, while ChatGPT User Bot contributed 6% of the attacks.

![Pie chart showing bot attacks by AI tool with percentages.](Image description)

### BOT AT TACKS BY AI TOOL

- ByteSpider Bot: 54%
- Apple Bot: 26%
- ClaudeBot: 13%
- ChatGPT-User: 6%
- ImagesiftBot: 1%

ByteSpider’s dominance in AI-enabled attacks can largely be attributed to its widespread recognition as a legitimate web crawler, making it an ideal candidate for spoofing. Cybercriminals frequently disguise their malicious bots as web crawlers to evade detection and bypass security measures that whitelist known web crawlers. In contrast, AppleBot (26%) and ClaudeBot (13%) are used less frequently, likely due to stricter security controls or less favorable spoofing potential.

Fluctuations in attack volume throughout the year suggest that attackers are still in an experimental phase, refining their tactics to maximize the effectiveness of these emerging tools. As adversaries continue to adapt, we anticipate this attack vector will expand in the coming years, fueling a rise in automated threats.

![Line chart showing AI-enabled bot attacks in 2024 by month.](Image description)

### AI-ENABLED BOT AT TACKS IN 2024

- **January 2024**: ~50 Million
- **February 2024**: ~100 Million
- **March 2024**: ~150 Million
- **April 2024**: ~200 Million
- **May 2024**: ~250 Million
- **June 2024**: ~300 Million
- **July 2024**: ~350 Million
- **August 2024**: ~300 Million
- **September 2024**: ~250 Million
- **October 2024**: ~200 Million
- **November 2024**: ~150 Million
- **December 2024**: ~100 Million

AI is enabling attackers to execute a wide range of cyber threats, including DDoS attacks, custom rules exploitation, and API violations. While API violations can involve automated bot activity, they also include broader abuse scenarios, such as unauthorized access attempts and exploitation of misconfigurations. However, bot-driven attacks, in particular, are becoming more sophisticated and harder to detect. In 2024, bad bots accounted for over 16% of all AI-enabled attacks. When combined with business logic attacks—which use automation for stealthy, low-and-slow reconnaissance—this number rises to 41%. This trend highlights how attackers are leveraging AI to refine their techniques, particularly in identifying and exploiting API vulnerabilities to extract sensitive data. As AI capabilities advance, defending against Business Logic Abuse will become even more challenging.

![Pie chart showing % AI-powered attacks by type.](Image description)

### % AI-POWERED AT TACKS BY T YPE

- Custom Rules: 3%
- Business Logic: 2%
- Bad Bot: 6%
- API Violations: 16%
- DDoS: 25%
- Other: 48%

## Bot Evasion Tactics

As bots become more sophisticated and mimic human behavior, security teams face increasing challenges in differentiating between automated threats and real users. Additionally, with growing concerns around data privacy, bot operators increasingly use VPNs and obfuscation techniques to blend into legitimate human traffic and avoid being flagged as automated threats.

Based on insights from Imperva’s dedicated bot-focused Security Analysts and the Imperva Threat Research team, the following list highlights the latest evasion tactics and techniques employed by bot attackers in 2024:

### Fake browser identity and attributes

Many simple bad bots fake their browser identity to appear as a legitimate browser (e.g., Chrome, Firefox). This is a simple but effective way to evade basic security measures. More advanced bots will also fake other browser attributes, such as headers and JavaScript execution to avoid detection by more advanced bot mitigation tools.

### Residential Proxies

Attackers use residential IP addresses to evade detection and blend in with normal traffic. Residential proxies allow attackers to route malicious traffic through real user devices, making it harder to detect and block them based on IP reputation alone. While the use of residential ISPs for bot attacks decreased slightly from 26% of all bot attacks where traffic was routed via an ISP in 2023 to 21% in 2024, it remains a favored tactic due to its effectiveness in mimicking legitimate users.

### Privacy Tools

Services like iCloud Private Relay mask user identities, increasing the challenge of distinguishing between legitimate human traffic and automated bot activity.

### API Abuse

Attackers exploit exposed or unprotected APIs to extract data, automate attacks, and bypass front-end security controls.

### App Cracking

Bots target outdated mobile applications that do not enforce mandatory updates, making them vulnerable to reverse engineering, credential stuffing, and unauthorized modifications.

### Consistent Token Generation

Bots generate consistent tokens, reducing the chances of triggering anti-bot protections during postback processes.

### Polymorphic Bots

Self-learning bots dynamically change attributes to evade detection.

### Bots-As-A-Service (BaaS)

A growing ecosystem of commercialized bot services is driving an unprecedented surge in automated threats across industries.

### Bypassing CAPTCHA

AI-driven bots solve CAPTCHA challenges with high accuracy, rendering many traditional defenses ineffective.

### Property-cycling

AI enables rapid switching of IP addresses, user agents, or browser parameters, to evade detection.

### Headless Browsers

Tools like Puppeteer, Playwright, Selenium are enhanced by AI to evade detection and allow attackers to interact with websites just like a human user would execute JavaScript, handle CAPTCHA challenges and navigate pages dynamically.

### AI-Assisted Scripting

AI-generated bot scripts increase attack volumes and automation efficiency.

### Content Scraping and Anti-detect browsers

Content scraping services such as Browser.ai enable large-scale data extraction, while anti-detection browsers like Multilogin, GoLogin, and AdsPower help evade security measures.

## Browser Impersonation by Bad Bots

In their quest to continue undetected, bad bots disguise themselves as popular web or mobile browsers typically used by humans. This is accomplished through browser automation tools. While this was once considered an advanced method of evasion, it has since become a standard approach for many bad bots. Over the years, the browsers favored by these bots have shifted in line with changing human user preferences and evolving strategies to stay under the radar. For instance, Internet Explorer, once widely used by both legitimate users and bad bots, has largely fallen out of favor in recent years.

Chrome remains the top browser that attackers impersonate, as it has done for the last ten years, accounting for 46% of all bad bot attacks in 2024. The percentage of attacks where bots declare themselves as Chrome increased from 40% to 46% in 2024.

Attackers often choose to impersonate Chrome for several legitimate reasons:

*   **Widespread Usage**: Chrome is the most popular browser globally, used by a significant majority of internet users. By mimicking Chrome, attackers increase the likelihood that their bot traffic will blend in with legitimate user activity, reducing the chances of detection by security systems.
*   **Common Whitelisting**: Many websites and security systems whitelist traffic from well-known browsers like Chrome, assuming it is legitimate. Since Chrome is widely trusted, bad bots can bypass basic bot mitigation systems that may not scrutinize requests from recognized browsers.
*   **Advanced Capabilities**: Chrome supports a wide range of modern web technologies (such as JavaScript and HTML5), which many websites rely on. By impersonating Chrome, attackers can exploit these features to navigate more complex sites, interact with dynamic content, and carry out more sophisticated attacks, like credential stuffing or scraping, without raising suspicion.

Mobile Safari is the second most mimicked browser, accounting for 17% of attacks. Being the default browser on Apple devices, including iPhones and iPads, which have a significant global user base, by mimicking Mobile Safari, attackers can target a large segment of mobile web traffic.

For many of the same reasons Mobile Chrome is the third most popular choice for attackers, remaining close to Mobile Safari at a steady 14% year-over-year.

![Pie chart showing top browsers impersonated by bad bots in 2024.](Image description)

### TOP BROWSERS IMPERSONATED BY BAD BOTS IN 2024

- Chrome: 46%
- Microsoft Edge: 17%
- Firefox: 14%
- Mobile Safari: 5%
- Android Browser: 4%
- Mobile Chrome: 3%
- Safari: 2%
- Samsung Browser: 2%
- Other: 7%

## Account Takeover Attacks

Account Takeover (ATO) attacks use malicious bots to gain unauthorized access and take over online user accounts through credential stuffing and credential cracking. These attacks lead to digital identity theft and financial losses for targeted organizations.

ATO attacks are among the most significant cybersecurity challenges facing digital businesses today. A successful attack can result in financial loss, theft of sensitive customer data, misuse of personal information, and reputational damage.

The chart below shows the month-by-month growth of ATO attacks over the past two years. As the chart shows, ATO attacks grew significantly from June onwards with the greatest percentage growth in the months of September, October and November when ATO attacks increased by 79% each month compared to the same period the previous year.

![Line chart showing monthly account takeover attacks in 2023 vs 2024.](Image description)

### MONTHLY ACCOUNT TAKEOVER AT TACKS 2023 vs 2024

- **January**: 2023 [Value], 2024 [Value]
- **February**: 2023 [Value], 2024 [Value]
- **March**: 2023 [Value], 2024 [Value]
- **April**: 2023 [Value], 2024 [Value]
- **May**: 2023 [Value], 2024 [Value]
- **June**: 2023 [Value], 2024 [Value]
- **July**: 2023 [Value], 2024 [Value]
- **August**: 2023 [Value], 2024 [Value]
- **September**: 2023 [Value], 2024 [Value]
- **October**: 2023 [Value], 2024 [Value]
- **November**: 2023 [Value], 2024 [Value]
- **December**: 2023 [Value], 2024 [Value]

Below are some possible reasons why ATO attacks increased so significantly from June onwards last year:

### Seasonal E-commerce and Sales Events

With major shopping events (like Black Friday and holiday sales) starting to peak in the second half of the year, attackers target high-value accounts during these times, contributing to the sharp rise in ATO attempts.

### Increased Data Breaches

The rise in compromised credentials from high-profile data breaches has provided attackers with larger databases of stolen login information, making it easier to execute ATO attacks. According to the Identity Theft Resource Center (ITRC), over 1.7 billion data breach notices were issued across the United States in 2024, marking a 312% increase from the 419 million notices sent in 2023.

### More Sophisticated Attack Techniques

Attackers are using more advanced tools, such as bots and AI-driven automation, to bypass traditional security measures like CAPTCHA and MFA, leading to a surge in successful ATOs.

### Most targeted industries by Account Takeover Attacks

The chart on the right shows the top five most targeted industries for Account Takeover attacks in 2024 accounting for 78% of all attacks.

![Pie chart showing five industries accounting for 78% of ATO attacks.](Image description)

### FIVE INDUSTRIES ACCOUNT FOR 78% OF ATO AT TACKS

- Financial Services: 22%
- Telecom & ISPs: 18%
- Computing & IT: 17%
- Business: 11%
- Food & Beverage: 10%

The top targeted industry was Financial Services accounting for 22% of all ATO attacks, followed by Telecom and ISPs with 18%, and Computing & IT with 17%.

The Financial Services industry has always been a prime target for account takeover attacks because of the high value of accounts and the sensitive nature of the data to be obtained. Banks, credit card companies and fintech platforms hold a vast amount of Personally Identifiable information (PII), including credit card and bank account details which can be sold for a profit on the dark web. The proliferation of APIs in the industry has expanded the attack surface for cyber criminals who target API vulnerabilities such as weak authentication and authorization methods, to conduct account takeover and data theft.

The Telecom industry is also a top target for account takeover but motivation that extends beyond financial gain. While access to sensitive PII and customer data can bring financial reward for attackers, the Telecom industry controls critical internet infrastructure and by compromising an internet services provider or ISP’s accounts or systems, attackers can intercept our reroute traffic (man-in-the-middle attacks), deploy malware or disrupt services in the case of nation state actors, who often target Telecom organizations for espionage and surveillance in times of geopolitical conflict.

### Consequences of Account Takeover

A successful account takeover attack that results in a data breach can lead to regulatory penalties, legal costs, compensation claims, reputational damage and long-term financial losses. The severity depends on the nature of the breach, the regulatory environment, and the company’s response time. Here are some examples of regulatory penalties:

| REGULATION                               | PENALTIES                                                              | ADDITIONAL CONSEQUENCES                                                              |
| :--------------------------------------- | :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| GDPR (General Data Protection Regulation) | Fines up to €20 million or 4% of global annual turnover for failure to protect personal data | Additional penalties for failure to notify authorities within 72 hours               |
| CCPA (California Consumer Privacy Act)   | Fines up to $2,500 per violation or $7,500 for intentional violations    | Consumer lawsuits for personal data exposure, including class-action lawsuits        |
| HIPAA (Health Insurance Portability and Accountability Act) | Fines ranging from $100 to $50,000 per violation, with a maximum annual penalty of $1.5 million | Severe penalties for exposing Protected Health Information (PHI)                     |

## Bad Bots: A Global Problem

### More Than Half of All Bot Attacks Targeted the United States

The United States remained the top targeted country for bot attacks accounting for 53% of all attacks in 2024. Brazil and the United Kingdom were joint second with 6% of all attacks targeting them, respectively.

The United States boasts the world’s largest online economy, with millions of consumer transactions occurring daily. As home to a significant share of global wealth, leading financial institutions, and tech giants, it presents a highly attractive target for cyber attackers seeking lucrative opportunities.

### Almost One-Third of All Bot Attacks in EMEA Targeted UK Sites

In 2024, the United Kingdom was the most targeted country in the Europe, Middle East, and Africa (EMEA) region, accounting for 31% of all bot attacks. Much like the United States, the UK serves as the region’s leading financial hub, with a high concentration of wealth, major banks, and fintech companies operating in London. This makes it a prime target for cybercriminals looking to exploit financial transactions, conduct account takeovers, and deploy fraud-related bot attacks.

Additionally, geopolitical factors continue to shape the cybersecurity landscape. Notably, Russia and Ukraine both ranked among the top ten most targeted countries in EMEA, highlighting the ongoing cyber threats influenced by regional conflicts. Cyberattacks on these nations often include state-sponsored operations, hacktivism, and financially motivated threats, further underscoring the complex and evolving nature of cyber risks across the region.

![Bar chart showing top 5 most targeted countries worldwide.](Image description)

### Top 5 most targeted countries worldwide

- United States: 53%
- Brazil: 6%
- United Kingdom: 6%
- Canada: 5%
- France: 3%

![Bar chart showing top 5 most targeted countries in EMEA.](Image description)

### 5 most targeted countries EMEA

- United Kingdom: 31%
- France: 17%
- Netherlands: 11%
- United Arab Emirates: 11%
- Russia: 7%

### Top Targeted Countries APAC

In 2024, bot attacks in the Asia-Pacific (APAC) region were heavily concentrated in Hong Kong and Indonesia, with each country accounting for 24% of all bot attacks. Together, they made up nearly half of the region’s total bot activity.

Hong Kong’s status as a global financial hub and a gateway to China makes it a prime target for cybercriminals seeking to exploit banking, fintech, and e-commerce platforms. Meanwhile, Indonesia’s large and rapidly growing digital economy, combined with relatively weaker cybersecurity infrastructure, has made it particularly vulnerable to bot-driven fraud and credential stuffing attacks.

Australia followed closely in third place, accounting for 18% of all bot attacks. As one of APAC’s most developed economies with a strong financial sector, e-commerce market, and critical infrastructure, Australia remains a frequent target for cybercriminals using bots to launch credential attacks, and automated fraud schemes.

The concentration of attacks in these countries underscores the evolving cyber threat landscape in APAC, where economic growth, digital expansion, and geopolitical factors continue to shape cybersecurity risks.

![Bar chart showing top 5 most targeted countries in Asia Pacific.](Image description)

### 5 most targeted countries Asia Pacific

- Hong Kong: 24%
- Indonesia: 24%
- Australia: 18%
- Singapore: 11%
- India: 9%

### Top Targeted Countries Americas

In 2024, the United States remained the dominant target for bot attacks in the Americas, accounting for a staggering 76% of all incidents. However, outside the U.S., Brazil (9%) and Canada (7%) were the most targeted countries in the region.

Brazil’s high ranking could be due to its rapidly growing digital economy, widespread mobile banking adoption, and high levels of online fraud. Cybercriminals often exploit vulnerabilities in Brazil’s financial and e-commerce sectors, using bots for credential stuffing and payment fraud. Additionally, Brazil’s large population and high internet penetration make it a lucrative target for bot-driven cybercrime.

Canada, ranking third, is a frequent target due to its strong banking sector, e-commerce growth, and