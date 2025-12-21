# 2025 Advanced Persistent Bots Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Impact of Mitigation](#impact-of-mitigation)
- [Bot Sophistication](#bot-sophistication)
- [Going With The Flow](#going-with-the-flow)
- [Bot Breakdown](#bot-breakdown)
- [Top Targeted Industries](#top-targeted-industries)
- [Industry Trends](#industry-trends)
- [Industry Sophistication](#industry-sophistication)
- [Industry Seasonality](#industry-seasonality)
- [Web Automation Industry Seasonality](#web-automation-industry-seasonality)
- [Mobile API Automation Industry Seasonality](#mobile-api-automation-industry-seasonality)
- [Top Focused Flows](#top-focused-flows)
- [Sophistication by Flow](#sophistication-by-flow)
- [Automation Prevalence by Flow and Industry](#automation-prevalence-by-flow-and-industry)
- [Bot Behavior Post-Mitigation](#bot-behavior-post-mitigation)
- [The Identity Threat](#the-identity-threat)
- [Credential Stuffing and Account Takeover](#credential-stuffing-and-account-takeover)
- [The Rise of Residential Proxies](#the-rise-of-residential-proxies)
- [Hiding in Plain Sight](#hiding-in-plain-sight)
- [Reselling Proxy Networks](#reselling-proxy-networks)
- [PROXYLIB](#proxylib)
- [Conclusions](#conclusions)
- [Flow Attack Prevalence and Trends](#flow-attack-prevalence-and-trends)
- [Industry Attack Prevalence, Trends and Seasonality](#industry-attack-prevalence-trends-and-seasonality)
- [Sophistication](#sophistication)
- [Impact of Mitigation](#impact-of-mitigation-1)
- [Recommendations](#recommendations)
- [Further Reading](#further-reading)
- [Appendix 1: Industry Definitions](#appendix-1-industry-definitions)
- [Appendix 2: Flow Definitions](#appendix-2-flow-definitions)

---

## Executive Summary

In today’s digital landscape, bots dominate the internet, with some estimates suggesting they account for over 50% of all website and mobile API activity. Beneficial bots support search engines, fulfill genuine business needs, and automate repetitive tasks. While some are outright malicious and enable fraud, many other bots operate somewhere in the middle—in the murky grey area between illegal and immoral. They ignore website terms of use, prevent customers from purchasing goods and services, and can even weaken security. Existing research often examines uncontrolled bot traffic across the entire internet, but this report takes a different approach and, instead, focuses on how automated traffic changes after bot mitigation is put in place.

We provide a detailed analysis of bot types, their objectives, and industry-specific impacts. A key focus is on advanced and persistent bots—those that adapt as security measures evolve. Malicious actors, including nation-states and cybercriminals, frequently modify tactics to bypass defenses, increasing attack sophistication or moving to softer targets.

This report analyzes over 200 billion web and API transactions from F5’s Bot Defense customers from November 2023 to September 2024. Because these organizations have long-standing bot protection, the data highlights the most persistent and advanced bot and automation activity. We define ‘automation’ as any malicious non-human traffic targeting protected applications and ‘transactions’ as HTTP requests to and from a client device. Our analysis divides traffic by application type. ‘Web’ refers to traditional websites, and ‘mobile’ (or ‘mobile API’) are Android and iOS mobile applications which make use of an API call to load data onto the device. Collectively, we refer to ‘web’ and ‘mobile API’ as ‘platforms’.

Looking at all HTTP requests across all sectors and platforms, we found an average of 10.2% (21.22 Billion) were bots and other forms of automation.

![Figure 1: Average automated traffic across all industries after bot mitigation was enabled.](Figure 1: Average automated traffic across all industries after bot mitigation was enabled.)

Not all bot traffic was entirely malicious. Of all the HTTP transactions, 2.0% (4.06 Billion) came from known financial aggregators (commonly used by money management apps). A total of 3.5% of transactions (7.18 Billion) were from bots we categorize as “flagged automation” (comprised of allowed automation from external sources as well as automation on applications that customers have in monitoring mode). Finally, 4.8% transactions (9.98 Billion) were unwanted bots that were mitigated by F5.

While 4.8% sounds like a modest number it is important to remember that this figure represents an average across all bot types across all industries. As we explain in more detail later, these are bots which have persisted long after mitigation has been put in place. The average quantity of bots affecting sites and APIs without mitigation is often far higher. As previously reported on in our 2023 Identity Theft Report, the average quantity of bots attacking login pages alone averages 20% across all industries, with some sectors seeing upwards of 80% of all login traffic originating from bots. See [Impact of Mitigation](#impact-of-mitigation) for further analysis of the effects of bot mitigation.

When examining bot traffic broken out by sector, we found that the Hospitality industry experienced the highest levels of unauthorized bot traffic against web platforms, with almost 45% of all transactions coming from automated activity, primarily driven by web scraping. When focusing on mobile API endpoints, the Entertainment industry was worst hit, with 23% of all traffic originating from unauthorized bots.

Most industries saw a decline in automation targeting their web and mobile API endpoints when compared to the 2024 Bad Bots Review. Unauthorized bot traffic decreased in 15 of 26 of industry-platform combinations. The largest web platform declines were in Telecoms (-18.5%), Healthcare (-10%), and Airlines (-9.2%). Mobile API decreases were seen in Entertainment (-11.5%) and Fashion Retail (-8.3%). This trend aligns with the expectation that persistent bot mitigation deters threat actors. Initially, bot operators attempt to bypass controls, but when unsuccessful, they often abandon automated attacks, leading to a year-over-year decline. While many industries saw declines in automated attacks, eCommerce, Hospitality, and Quick Service Retail (QSR) experienced increases. Hospitality (+18.3%) and QSR (+11.2%) saw the largest web automation spikes, while mobile API automation rose in QSR (+3.4%) and eCommerce (+2.8%). These increases were driven by determined bot operators whose businesses depended on the ability to automate their activities. None of the increased bot traffic was able to reach the origin servers. An increase in automation attempts is not necessarily indicative of a failure of controls, but rather of an increase in attacker motivation and or sophistication. If, for example, bot operators create a new attack tool or a new fraud scheme for a given industry that they want to leverage, they will try it on target enterprises, resulting in an increase in automation reaching the bot defenses.

Bot sophistication varied between the web and mobile API platforms. Web sites saw just over 24% of automated traffic originating from advanced bots, while only 13.5% of all mobile API transactions came from similarly capable attackers. The reverse was true for intermediate bots. Web sites saw 21.5% of automated traffic coming from these automated clients, while intermediate bots represented 40.0% of activity to mobile APIs (Figure 2).

![Figure 2: Breakdown of unauthorized bot traffic by level of sophistication.](Figure 2: Breakdown of unauthorized bot traffic by level of sophistication.)

The sophistication of bots also varies widely across industries. Advanced bots were most prevalent in General Retail, Airlines, and Banking (web platforms), and Telecommunications and Entertainment (mobile APIs).

Effects of enabling bot mitigation varied between platforms. Mobile APIs saw a significant drop in unauthorized automation, with flows seeing a median of 6.11% in monitoring mode, and a median of 0.90% with mitigation enabled. Web traffic saw an unexpected increase in bot activity, though further analysis showed that bot operators increased their automation efforts since their business depended on unauthorized activity such as price scraping. Web flows had a median of 7.04% of all traffic originating from bots while in monitoring only mode, and a median of 7.94% after mitigation. No unauthorized bots were able to connect to origin servers post mitigation.

Credential stuffing, an common cyber attack enabled through the use of malicious bots, continues to be a significant challenge for all industries. With bot-mitigation in place, the attempted level of malicious login attempts across all industries was 10.6% for web traffic, and 5.2% for mobile API transactions. Per-industry, this reached as high as 33.5% of all login traffic targeting the Technology industry on the web, and around 24% against mobile API endpoints in the eCommerce and Entertainment industries. Telecom ranked first for the highest share of advanced credential stuffing bots across all industries and platforms. A full half of all login traffic targeting mobile APIs within the Telecom sector originated from advanced automation sources.

Residential IP proxies have become a must-have for bot operators. By routing their traffic through the networks of home broadband and cellular users, bots are able to benefit from clean and trusted IP addresses, bypassing simple bot defenses that rely heavily on IP reputation checks. The problem is so widespread that recent research claims that virtually every single cellular IP address passes some bot traffic.

![Figure 3: Overview of a residential proxy network architecture.](Figure 3: Overview of a residential proxy network architecture.)

Bots and automation continue to pose a significant challenge across industries, with web scrapers being the most prevalent threat. Over half of all web content requests came from scrapers, and nearly a quarter of web searches were automated. This surge in scraping activity is likely linked to AI agents from companies like OpenAI, Anthropic, and Perplexity. Reseller bots also remained a major concern, automating more than one in five "add to cart" transactions. While overall bot automation levels have declined compared to previous years—likely due to improved mitigation efforts—persistent scraping and advanced automation attempts continue.

The impact of bots varies by industry, with hospitality, e-commerce, and entertainment being the hardest hit. Interestingly, web-based attacks tend to be of lower sophistication, while mobile API attacks often exhibit intermediate sophistication. Effective mitigation significantly reduces bot-driven transactions, but some persistent attackers continue their efforts, particularly in scraping and account creation. This ongoing cat-and-mouse game underscores the need for businesses to maintain robust anti-bot defenses, as even small lapses can be exploited by automated threats that adapt and retry, potentially leading to increased attack volumes despite mitigation efforts.

## Introduction

In today’s online world, bots flood the web. If some reports are to be believed they make up 50% or more of all internet traffic. Not all bots are bad, of course. We rely on bots to crawl and index the web for search engines, such as Google and Bing. We improve efficiency by creating scripts to automate repetitive tasks, such as data backups. Entire businesses are even built based on the use of bots (think price comparison sites and financial aggregators). But for each good bot there are many questionable ones, and a growing number of entirely malicious ones.

Much research already exists which examines the web’s traffic at large, comparing the number of human users to bots and how things differ from one industry to another. This report is different in a few crucial ways.

One such way is the level of detail into which we go when examining the different types of bots and their uses. Automation affects all industries to varying levels, and the types of bots (the objective of the bot operators) can be dramatically different. In the full and unabridged version of this report available at f5.com/labs we provide exhaustive analysis of the various types of bots, their prevalence in each industry, explain the motivation of the bot operators, and even provide guidance and recommendations for countering each of them.

Additionally, we focus on advanced and persistent bots. Threat actors, whether they be nation state or organized crime, often change their behavior once security controls and other mitigation strategies are put in place. Our research shows this is certainly true of bots and their operators. Once bot defenses are activated bot operators often move to softer targets or increase the sophistication of their tactics, tools, and procedures. This report analyses over 200 billion web and API transactions for users of F5’s Bot Defense solution. Most of these users have had this solution in place for many years which means the data we have on bot attacks is heavily skewed towards those operators who are advanced and persistent in their use of bots. The attacks and methods we observe in our data, therefore, showcases the sustained and advanced bots that organizations might encounter even after enabling bot mitigations.

Readers interested in seeing the quantity of bot traffic (such as credential stuffing attacks) against organizations without bot defenses are encouraged to review our 2023 Identity Threat Report. This publication showcases the drastic difference in bot traffic before and after enabling bot controls.

This report analyses bot traffic targeting a wide range of global industries during 2024 (specifically, 12th November 2023 to 18th September 2024). Henceforth, the term ‘automation’ shall refer to any malicious synthetic or non-human traffic reaching a protected application.[^1]

Due to the change in focus of this report compared with the 2024 Bad Bots Review, the list of flows included in the research has been adjusted. This means that while some flows remain the same, others have been broken down into more granular flows so we can better analyze the intent of the automation. An example is the Shop flow as found in previous reports. This has now been split into Shop, Add to Cart and Checkout. This is to allow us to differentiate between bots simply reviewing shopping pages (Shop), those trying to acquire goods at scale (Add to Cart) and carding bots trying out multiple stolen credit cards (Checkout). Details of the changes in the flow definitions can be found in the appendix.

[back to top](#table-of-contents)

## Impact of Mitigation

In our 2023 Identity Threat Report we examined the impact that bot mitigation had on the quantity and proportion of credential stuffing attacks. We analyzed bot traffic targeting web and mobile APIs and compared figures before and after bot mitigation was enabled for each protected endpoint. As might be expected, we found a significant drop in the proportion of unauthorized automation, as show in Figure 4. This drop off was present across both web and mobile API endpoints, but was more pronounced in mobile API traffic. Pre-mitigation, mobile API automation levels were higher than web. Once mitigation was enabled, mobile API automation levels dropped below those for web. This, despite web also seeing a significant decrease in automation levels post mitigation.

![Figure 4: Average rate of malicious automation against authentication endpoints over time, broken out by platform.](Figure 4: Average rate of malicious automation against authentication endpoints over time, broken out by platform.)

While mobile endpoints see higher level of automation rates pre-mitigation, web endpoints tend to stay higher post-mitigation.

In this report, we have expanded upon this previous analysis, and look beyond just credential stuffing attacks to examine the effects of bot mitigation on all flows. We continue to split traffic by web and mobile API since our research shows different tools, motivation, and persistence for the different platforms. For this analysis, we only included flows that had substantial quantities of data for enterprises in monitoring-only and in mitigation mode. For these reasons some flows were excluded and the list here may differ from the full list of flows.

More details can be found in the Bot Behavior Post-Mitigation section.

[back to top](#table-of-contents)

## Bot Sophistication

The capabilities (sophistication) of bots are indicative of the level of technical expertise, motivation, and resources that a bot operator can bring to bear in the execution of their automated activities. There is usually a positive correlation between the level of sophistication of an attack and the cost associated with carrying out that attack. Threat actors will generally do the minimum amount required to get a successful result. Hence attacks that start off unsophisticated can quickly retool into more sophisticated attacks depending on the level of technical expertise, motivation and resources the attacker has.

Attack sophistication can be categorized in one of two ways: the capabilities of the tools, or by the techniques used to operate the bots (for example, by cleverly distributing the timing of requests sent by the bots). For the purposes of this report sophistication is limited to the capabilities of the automation tools.

We categorize bots by three levels of sophistication (Table 1).

| Level         | Description