Zscaler ThreatLabz 2024 AI Security Report
The AI revolution has arrived. Discover key trends, risks, and best practices in enterprise AI adoption, with insights into AI-driven threats and key strategies to defend against them.
©2024 Zscaler, Inc. All rights reserved.
©2024 Zscaler, Inc. All rights reserved.

## Contents

03 Executive Summary

04 Key Findings

05 Key GenAI and ML Usage Trends

05 AI transactions continue to accelerate

06 Enterprises are blocking more AI transactions than ever

07 Industry AI breakdown

09 Healthcare and AI

10 Finance

11 Government

12 Manufacturing

13 Education and AI

14 ChatGPT usage trends

15 AI usage by country

Regional breakdown: EMEA

Regional breakdown: APAC

18 Enterprise AI Risk and Real-World Threat Scenarios

18 Enabling AI in the enterprise: top 3 risks

20 AI-driven threat scenarios

AI impersonation: deepfakes, misinformation, and more

21 AI-generated phishing campaigns

From query to crime: creating a phishing login page using ChatGPT

22 Dark chatbots: uncovering WormGPT and FraudGPT on the dark web

23 AI-driven malware and ransomware across the attack chain

24 AI worm attacks and “viral” AI jailbreaking

25 AI and US elections

26 All Eyes on AI Regulations

26 United States

27 European Union

28 AI Threat Predictions

31 Case Study: How to Securely Enable ChatGPT in the Enterprise

31 5 Steps to integrate and secure generative AI tools

33 How Zscaler Delivers AI + Zero Trust and Secures Generative AI

33 The key to AI-driven cybersecurity: high-quality data at scale

34 Leveraging AI across the attack chain

18 Enabling the enterprise AI transition: the control is in your hands

35 Summary of Zscaler’s AI-infused offerings

36 Enabling the enterprise AI transition: the control is in your hands

37 Appendix

37 ThreatLabz research methodology

37 About Zscaler ThreatLabz

02

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

### Executive Summary

AI is more than a pioneering innovation—it’s now business as usual. As generative AI tools like ChatGPT transform business in large and small ways, AI is being woven deep into the fabric of enterprise life. However, questions about how to securely adopt these AI tools while defending against AI-driven threats are not settled.

Enterprises are rapidly adopting AI and ML tools across departments like engineering, IT marketing, finance, customer success, and more. Yet, they must balance the numerous risks that come with AI tools to reap their fullest rewards. Indeed, to unlock the transformative potential of AI, enterprises must enable secure controls to protect their data, prevent the leakage of sensitive information, mitigate ‘Shadow AI’ sprawl, and ensure the quality of AI data.

These AI risks to enterprises are bidirectional: outside enterprise walls, AI has become a driving force for cyberthreats. Indeed, AI tools are allowing cybercriminals and nation state-sponsored threat actors to launch sophisticated attacks, more quickly, and at greater scale. Despite this, AI holds promise as a key piece of the cyber defense puzzle as enterprises grapple with a dynamic threat landscape.

Throughout, you’ll find insights into top-of-mind AI topics including business risk, AI-driven threat scenarios and adversary tactics, regulatory considerations, and predictions for the AI landscape in 2024 and beyond.

Just as critically, this report offers best practices on two fronts: how enterprises can securely embrace generative AI transformation while protecting critical data, and how AI-powered tools are working to deliver layered, zero trust security to face the new landscape of AI-driven threats.

Drawing on more than 18 billion transactions from April 2023 to January 2024 across the Zscaler Zero Trust Exchange™, ThreatLabz analyzed how enterprises are using AI and ML tools today. These insights reveal key trends across business sectors and geographies in how enterprises are adapting to the shifting AI landscape and securing their AI tools.

The ThreatLabz 2024 AI Security Report offers key insights into these critical AI challenges and opportunities.

03

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

### Key Findings

*   AI/ML tool usage skyrocketed by 594.82%, rising from 521 million AI/ML-driven transactions in April 2023 to 3.1 billion monthly by January 2024.
*   Enterprises are blocking 18.5% of all AI/ML transactions—a 577% increase in blocked transactions over nine months—reflecting growing concerns around AI data security and companies’ reluctance to establish AI policies.
*   The most widely used AI applications by transaction volume are ChatGPT, Drift, OpenAI*, Writer, and LivePerson. The top three blocked applications by transaction volume are ChatGPT, OpenAI, and Fraud.net.
*   The top 5 countries generating the most AI and ML transactions are the US, India, the UK, Australia, and Japan.
*   Manufacturing generates the most AI traffic with 20.9% of all AI/ML transactions in the Zscaler cloud, followed by Finance and Insurance (19.9%) and Services (16.8%).
*   Enterprises are sending significant volumes of data to AI tools, with a total of 569 TB exchanged between AI/ML applications between September 2023 and January 2024.
*   ChatGPT usage continues to soar, with 634.1% growth, even though it is also the most-blocked AI application by enterprises, based on Zscaler cloud insights.
*   AI is empowering threat actors in unprecedented ways, including for AI-driven phishing campaigns, deepfakes and social engineering attacks, polymorphic ransomware, enterprise attack surface discovery, automated exploit generation, and more.

NOTE: The Zscaler Zero Trust Exchange tracks ChatGPT transactions independently from other OpenAI transactions at large.

04

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

## Key GenAI and ML Usage Trends

The enterprise AI revolution is far from its peak. Enterprise AI transactions have surged by nearly 600% and show no signs of slowing. Still, blocked transactions to AI apps have also risen — by 577%.

![AI and ML Transaction Trends graph](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 1 AI transactions from April 2023 to January 2024

### AI transactions continue to accelerate

From April 2023 to January 2024, enterprise AI and ML transactions grew by nearly 600%, rising to more than 3 billion monthly transactions across the Zero Trust Exchange in January. This underscores the fact that, despite a rising number of security incidents and data risks associated with enterprise AI adoption, its transformative potential is too great to ignore. Note that while AI transactions saw a brief lull over the December holidays, transactions continued at an even greater pace at the start of 2024.

Even as AI applications proliferate, however, the majority of AI transactions are being driven by a relatively small set of market-leading AI tools. Overall, ChatGPT accounts for more than half of all AI and ML transactions, while the OpenAI application itself comes in third place, with 7.82% of all transactions. Meanwhile, Drift, the popular AI-powered chatbot, generated nearly one-fifth of enterprise AI traffic (the LivePerson and BoldChat Enterprise chatbots also breached the top apps in spots 5 and 6). Meanwhile, Writer remains a favored generative AI tool in the creation of written enterprise content, such as marketing materials. Finally, Otter, an AI transcription tool often used in video calls, drives a significant portion of AI traffic.

![Top AI applications by transaction volume chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 2 Top AI applications by transaction volume

![Top AI/ML apps by the percentage of total data transferred chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 3 Top AI/ML apps by the percentage of total data transferred

Meanwhile, the volumes of data that enterprises send and receive from AI tools adds nuance to these trends. Hugging Face, the open-source AI developer platform often described as “the GitHub of AI,” accounts for nearly 60% of enterprise data transferred by AI tools. Since Hugging Face allows users to host and train AI models, it makes sense that it captures significant data volumes from enterprise users.

While ChatGPT and OpenAI make expected appearances on this list, two notable additions are Veed—an AI video editor often used to add subtitles, imagery, and other text to videos—and Fotor, a tool used to generate AI images, among other uses. Since videos and images entail large file sizes compared to other kinds of requests, it’s not surprising to see these two applications represented.

### Enterprises are blocking more AI transactions than ever

Even as enterprise AI adoption continues to surge, organizations are increasingly blocking AI and ML transactions because of data and security concerns. Today, enterprises block 18.5% of all AI transactions, a 577% increase from April to January, for a total of more than 2.6 billion blocked transactions.

![Number of AI/ML transactions blocked over time graph](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 4 Number of AI/ML transactions blocked over time

Some of the most popular AI tools are also the most blocked. Indeed, ChatGPT holds the distinction of being both the most-used and most-blocked AI application. This indicates that despite—or even because of—the popularity of these tools, enterprises are working actively to secure their use against data loss and privacy concerns. Another notable trend is that bing.com, which has an AI-enabled Copilot functionality, is blocked from April to January. In fact, bing.com accounts for 25.02% of all blocked AI and ML domain transactions.

**TOP MOST-BLOCKED AI TOOLS**
01 ChatGPT
02 OpenAI
03 Fraud.net
04 Forethought
05 Hugging Face
06 ChatBot
07 Aivo
08 Neeva
09 infeedo.ai
10 Jasper

**TOP BLOCKED AI DOMAINS**
01 Bing.com
02 Divo.ai
03 Drift.com
04 Quillbot.com
05 Compose.ai
06 Openai.com
07 Qortex.ai
08 Sider.ai
09 Tabnine.com
10 securiti.ai

FIGURE 5 Top blocked AI applications and domains by volume of transactions

### Industry AI breakdown

Enterprise industry verticals show notable differences in their overall adoption of AI tools as well as the proportion of AI transactions they block. Manufacturing is the clear leader, driving more than 20% of AI and ML transactions across the Zero Trust Exchange. Still, the finance and insurance, technology, and services sectors follow closely behind. Together, these four industries have pulled ahead of others as the most aggressive AI adopters.

![Share of AI Transactions by Industry Vertical chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 6 Industries driving the largest proportions of AI transactions

![AI/ML transaction trends among the highest-volume industries graph](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 7 AI/ML transaction trends among the highest-volume industries, April 2023–January 2024

#### Securing AI/ML transactions

**Percent of Blocked AI Transactions by Vertical**

| Vertical                | % of AI transactions blocked |
| :---------------------- | :--------------------------- |
| Finance & Insurance     | 37.16                        |
| Manufacturing           | 15.65                        |
| Services                | 13.17                        |
| Technology              | 19.36                        |
| Healthcare              | 17.23                        |
| Retail & Wholesale      | 10.52                        |
| Others                  | 8.93                         |
| Energy, Oil & Gas       | 14.24                        |
| Government              | 6.75                         |
| Transportation          | 7.90                         |
| Education               | 2.98                         |
| Communication           | 4.29                         |
| Construction            | 4.12                         |
| Basic Materials, Chemicals & Mining | 2.92                         |
| Entertainment           | 1.33                         |
| Food, Beverage & Tobacco| 3.66                         |
| Hotels, Restaurants & Leisure | 3.16                         |
| Religious Organizations | 6.06                         |
| Agriculture & Forestry  | 0.18                         |
| **Average across all verticals** | **18.53**                    |

FIGURE 8 Top industry verticals by percentage of AI transactions blocked

Paired with the sharp rise in AI transactions, industry sectors are blocking more AI transactions. Here, certain industries diverge from their overall adoption trends, reflecting differing priorities and levels of maturity in terms of securing AI tools. The finance and insurance sector, for instance, blocks the largest proportion of AI transactions: 37.2% vs. the global average of 18.5%. This is likely due in large part to the industry’s strict regulatory and compliance environment, combined with the highly sensitive financial and personal user data these organizations process.

Meanwhile, manufacturing blocks 15.7% of AI transactions, despite its outsized role in driving overall AI transactions. The technology sector, one of the earliest and most eager adopters of AI, has taken something of a middle path, blocking an above-average 19.4% of AI transactions as it works to scale AI adoption. Surprisingly, the healthcare industry blocks a below-average 17.2% of AI transactions, despite these organizations processing a vast wealth of health data and personally identifiable information (PII). This trend likely reflects a lagging effort among healthcare organizations to protect sensitive data involved in AI tools, as security teams play catch-up to AI innovation. Overall AI transactions in healthcare remain comparatively low.

#### Healthcare and AI

Ranking as the sixth biggest AI/ML user, the healthcare industry blocks 17.23% of all AI/ML transactions.

**Vital signs of progress in AI healthcare**

While the healthcare industry is typically cautious when putting innovations like AI into practice, as seen by its current 5% contribution to AI/ML traffic in the Zscaler cloud, it’s only a matter of time before AI has a greater impact on healthcare operations, patient care, and medical research and innovation.¹ Indeed, AI promises to help not only save time, but also save lives. Already, AI-powered technologies are enhancing diagnostics and patient care. By analyzing medical images with remarkable accuracy, AI helps radiologists detect abnormalities more quickly and facilitates faster treatment decisions.²

The potential benefits are vast. AI algorithms can use patient data to personalize treatment plans and accelerate drug discovery by efficiently analyzing biological data. Administrative tasks can be automated with generative AI as well, alleviating burdens on short-staffed healthcare teams.

These advancements underscore AI’s capacity to transform health provision and healthcare delivery.

**Key Healthcare Risks:**
Healthcare organizations should acknowledge the potential risks and challenges associated with AI, including concerns about data privacy and security, especially for personal identifiable information (PII), as well as ensuring that AI algorithms and their outputs are highly reliable and unbiased when aiding in the administration of patient care.

1. Statista, Future Use Cases for AI in Healthcare, September 2023.
2. The Hill, AI already plays a vital role in medical imaging and is effectively regulated, February 23, 2024.

**THE TOP AI APPS IN HEALTHCARE ARE:**
01 ChatGPT
02 Drift
03 OpenAI
04 Writer
05 Intercom
06 Zineone
07 Securiti
08 Pypestream
09 Hybrid
10 VEED

09

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

#### Finance & AI

In second place for total AI/ML usage, the finance industry blocks 37.16% of all AI/ML traffic.

**Financial institutions bank on AI**

Financial services companies have been leading early adopters in the AI era, with the sector accounting for nearly a quarter of AI/ML traffic in the Zscaler cloud. What’s more, McKinsey projects a potential annual revenue of US$200 billion to $340 billion from generative AI initiatives in banking, largely driven by increased productivity.³ AI quite literally represents a wealth of opportunity for banks and financial services.

While AI-powered chatbots and virtual assistants are nothing new to finance (Bank of America’s “Erica” was launched in 2018), generative AI enhancements are elevating these customer service tools to new levels of personalization. Other AI capabilities like predictive modeling and data analysis are poised to deliver massive productivity advantages to financial operations—transforming fraud detection, risk assessments, and more.

**Key Finance & Insurance Risks:**
Integrating AI into financial services and products also raises security and regulatory concerns about data privacy, biases, and accuracy. The significant 37% of blocked AI/ML traffic reported by ThreatLabz reflects that perspective. Addressing these concerns will require astute oversight and planning to maintain trust and integrity in banking, financial services, and insurance.

3. McKinsey, Capturing the full value of generative AI in banking, December 5, 2023.

**THE TOP AI APPS IN FINANCE ARE:**
01 ChatGPT
02 Drift
03 OpenAI
04 BoldChat Enterprise
05 LivePerson
06 Writer
07 Hugging Face
08 Otter Ai
09 Securiti
10 Intercom

010

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

#### Government and AI

Although it falls in the top 10 of AI/ML usage, the government sector blocks just 6.75% of AI/ML transactions.

**Global governments navigate AI practices and policies**

Two critical AI discussions have emerged in government: one on implementing AI technologies and another on establishing governance to manage them securely. The advantages of AI adoption by government and public sector entities are substantial, particularly where chatbots and virtual assistants can give citizens faster access to essential information and services across sectors like public transportation and education. AI-driven data analysis can help address societal challenges through data-driven decision-making processes, leading to more efficient policy development and resource allocation.

Notable progress is already underway. For example, the US Department of Justice appointed its inaugural Chief AI Officer, confirming a commitment to using AI systems. ThreatLabz data indicates that government customers are increasingly using AI/ML platforms like ChatGPT and Drift.

**Key Government Risks:**
Despite these trends, key concerns about AI-related risks and data privacy underscore the continued need for regulatory frameworks and governance across federal organizations. In general, policymakers worldwide have taken significant steps toward AI regulation in the past year, signaling a collective effort to drive responsible development and deployment of AI/ML technologies.

**THE TOP AI APPLICATIONS* IN GOVERNMENT ARE:**
01 ChatGPT
02 Drift
03 OpenAI
04 Zineone
*AI applications with at least 1M transactions

011

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

#### Manufacturing and AI

Unsurprisingly, the highest influx of AI/ML traffic (18.2%) in our research comes from manufacturing customers. AI adoption in manufacturing stands as a cornerstone of Industry 4.0, a.k.a. the Fourth Industrial Revolution—an era marked by the convergence of digital technologies and industrial processes.

From preemptively detecting equipment failures by analyzing vast amounts of data from machinery and sensors to optimizing supply chain management, inventory, and logistics operations, AI is proving instrumental to manufacturers. Additionally, AI-driven robotics and automation systems can significantly enhance manufacturing efficiency. They can execute tasks at far greater speed and accuracy than humans—all while reducing costs and errors.

**Manufacturing builds on AI momentum**

As the top AI/ML vertical, the manufacturing vertical blocks 15.65% of all AI/ML applications.

**TOP APPLICATIONS ARE:**
01 ChatGPT
02 Drift
03 OpenAI
04 Writer
05 Securiti
06 Google Search
07 Zineone
08 Pypestream
09 Hugging Face
10 Fotor

**Key Manufacturing AI Risks:**
As for the 16% of blocked traffic from AI/ML applications by manufacturing customers, some manufacturers are approaching generative AI/ML with caution. This may arise from concerns regarding the security of manufacturing organizations’ data as well as the need to selectively vet and approve a smaller set of AI applications while blocking applications that incur greater risk.

012

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

#### Education and AI

Coming in 11th in overall AI/ML usage, the education vertical blocks 2.98% of all AI/ML traffic.

**Education embraces AI as a learning tool**

While the education sector is not a top producer of AI traffic, it blocks a comparatively low percentage (2.98%) of AI and ML transactions: approximately 9 million, from a total of more than 309 million transactions. It’s clear that, despite popular narratives that education institutions typically block AI applications like ChatGPT among students, the sector has mostly embraced AI applications as learning tools.

Notably, five of the most popular AI apps in education (ChatGPT, Character.AI, Pixlr, and OpenAI) are explicitly or frequently focused on creative outputs for writing and image generation—while Forethought, meanwhile, can be used as an instructional chatbot aid.

Adding nuance to this narrative, it may also be that many educators block tools like ChatGPT as a matter of classroom policy, but that educational institutions have lagged behind other sectors in implementing technology solutions like DNS filtering that allow organizations to block AI and ML tools in more specific ways.

**Key Education AI Risks:**
In education, data privacy concerns will likely grow as the sector continues to embrace AI tools, specifically surrounding protections afforded to students’ personal data. In all likelihood, the education sector will increasingly adopt technological means to block selective AI applications, while providing greater data protection measures for personal data.

**TOP APPLICATIONS ARE:**
01 ChatGPT
02 Character.AI
03 Pixlr
04 Forethought
05 Deepai
06 Drift
07 OpenAI

013

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

### ChatGPT usage trends

ChatGPT adoption has soared. Since April 2023, global ChatGPT transactions grew by more than 634%, an appreciably faster rate than the overall 595% increase in AI transactions. From these findings and the broad industry perception of OpenAI as the premier AI brand, it’s clear that ChatGPT is the favored generative AI tool. In all likelihood, the adoption of OpenAI products will continue to grow, driven in part by the expected release of newer ChatGPT versions and the company’s text-to-video generative AI product, Sora.

Industry usage of ChatGPT closely maps to overall adoption patterns of AI tools in general. In this case, manufacturing is the clear industry leader, again followed by finance and insurance. Here, the technology sector lags slightly in fourth place, with 10.7% of ChatGPT transactions vs. third place and 14.6% overall. This is likely due in part to the tech sector’s status as a fast innovator, which may mean tech companies are more willing to embrace a broader variety of generative AI tools.

![ChatGPT transactions from April 2023 to January 2024 graph](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 9 ChatGPT transactions from April 2023 to January 2024

![Industries driving the largest proportions of ChatGPT transactions chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 10 Industries driving the largest proportions of ChatGPT transactions

014

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

### AI usage by country

AI adoption trends differ markedly worldwide, influenced by regulatory requirements, technological infrastructure, cultural considerations, and other factors. Here’s a look at the top countries driving AI and ML transactions in the Zscaler cloud.

As expected, the US produces the lion’s share of AI transactions. India, meanwhile, has emerged as a leading generator of AI traffic, driven by the country’s accelerated commitment to technology innovation. The Indian government also provides a useful example of how fast AI regulation is evolving, with its recent efforts to enact — and then drop — a plan that would require regulatory approval of AI models before they launch.⁴

![Countries driving the largest proportions of AI transactions chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 11 Countries driving the largest proportions of AI transactions

4. TechCrunch, India reverses AI stance, requires government approval for model launches, March 3, 2024.

015

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

#### Region breakdown: EMEA

EMEA Country Breakdown

Taking a closer look at the Europe, the Middle East, and Africa (EMEA) region, there are clear divergences in rates of AI and ML transactions between countries. While the UK accounts for only 5.5% of AI transactions globally, it represents more than 20% of AI traffic in EMEA, making it the clear leader. And while France and Germany unsurprisingly rank second and third as AI traffic generators in EMEA, rapid tech innovation in the United Arab Emirates has solidified the country as a top AI adopter in the region.

| Country           | Transactions | % of region |
| :---------------- | :----------- | :---------- |
| United Kingdom    | 763413289    | 20.47%      |
| France            | 504185470    | 13.53%      |
| Germany           | 471700683    | 12.66%      |
| United Arab Emirates | 238557680    | 6.40%       |
| Netherlands       | 222783817    | 5.98%       |
| Spain             | 198623739    | 5.30%       |
| Switzerland       | 129059097    | 3.46%       |
| Italy             | 97544412     | 2.62%       |

FIGURE 12 EMEA countries by total transactions

![EMEA countries by percentage of total AI transactions in region chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 13 EMEA countries by percentage of total AI transactions in region

![Growth in AI transactions in EMEA over time graph](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 14 Growth in AI transactions in EMEA over time

016

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

#### Region breakdown: APAC

Diving deeper into the Asia-Pacific region (APAC), ThreatLabz research shows clear and noteworthy trends in AI adoption. Although the region represents far fewer countries, ThreatLabz observed nearly 1.3 billion (135%) more AI transactions in APAC than EMEA. This growth is almost single-handedly being driven by India, which generates nearly half of all AI and ML transactions in the APAC region.

| Country    | Transactions | % of region |
| :--------- | :----------- | :---------- |
| India      | 2414319490   | 48.30%      |
| Australia  | 501562395    | 10.01%      |
| Japan      | 476425423    | 9.52%       |
| Singapore  | 284891384    | 5.70%       |
| Malaysia   | 268043263    | 5.36%       |
| Philippines| 243754578    | 4.87%       |
| Hong Kong  | 202119814    | 4.04%       |
| China      | 104545655    | 2.09%       |

FIGURE 15 APAC countries by total transactions

![APAC countries by percentage of total AI transactions in region chart](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 16 APAC countries by percentage of total AI transactions in region

![Growth in AI transactions in APAC over time graph](https://www.zscaler.com/blogs/security-research/new-ai-insights-explore-key-ai-trends-and-risks-threatlabz-2024-ai-security)
FIGURE 17 Growth in AI transactions in APAC over time

017

©2024 Zscaler, Inc. All rights reserved.
ZSCALER THREATLABZ REPORT 2024

## Enterprise AI Risk and Real-World Threat Scenarios

For enterprises, AI-driven risks and threats fall into two broad categories: the data protection and security risks involved with enabling enterprise AI tools; and the risks of a new cyber threat landscape driven by generative AI tools and automation.

### Enabling AI in the enterprise: top 3 risks

1.  **Protecting intellectual property and non-public information**
    Generative AI tools can lead to inadvertent leakage of sensitive and confidential data. In fact, sensitive data disclosure is number six on the Open Worldwide Application Security Project (OWASP) Top Ten for AI Applications.⁵ The past year has seen numerous instances of accidental data leakages or breaches of AI training data, including from cloud misconfigurations, from some of the largest AI tool providers—some exposing terabytes of customers’ private data.

    A related risk is the threat of model inversion, whereby attackers use the outputs of an LLM paired with knowledge about its model structure to make inferences about, and eventually extract, its training data. Of course, there is also the risk that AI companies themselves will be breached. There have been cases where the credentials of AI company employees have led directly to data leaks.

    Meanwhile, there is the chance that adversaries will launch secondary malware attacks, using information stealers like Redline Stealer or LummaC2, to steal employee login credentials and gain access to their AI accounts. In fact, it was recently disclosed that roughly 225,000 ChatGPT user credentials are listed for sale on the dark web, stemming from this type of attack.⁷ While privacy and data security remain top priorities at AI tool providers, these risks remain in play, and they extend equally to smaller AI companies