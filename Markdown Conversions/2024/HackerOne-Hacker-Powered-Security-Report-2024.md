# Hacker-Powered Security Report
8th Edition–2024/2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [The Impact of AI on Security Research and Vulnerability Management](#the-impact-of-ai-on-security-research-and-vulnerability-management)
- [Security Researchers Expand Their Expertise Into AI, APIs, and More](#security-researchers-expand-their-expertise-into-ai-apis-and-more)
- [Run a Top-Tier Program That Won’t Break the Bank](#run-a-top-tier-program-that-wont-break-the-bank)
- [The Top Ten Vulnerabilities Need to Change](#the-top-ten-vulnerabilities-need-to-change)
- [Media and Entertainment](#media-and-entertainment)
- [Computer Software](#computer-software)
- [Internet and Online Services](#internet-and-online-services)
- [Crypto and Blockchain](#crypto-and-blockchain)
- [Retail and E-commerce](#retail-and-e-commerce)
- [The Best Defense Has Layers of Depth](#the-best-defense-has-layers-of-depth)
- [Measuring Success: Invest in Return on Mitigation](#measuring-success-invest-in-return-on-mitigation)
- [Conclusion](#conclusion)

## Executive Summary
Cyberthreats are always evolving. So must your defenses. Faster, smarter, and always ahead.

Every organization is a technology organization. Car manufacturers, government agencies, and banks do very different things, but they all conduct business digitally. With AI deployments—as well as AI-powered threat actors—now mainstream, the digital threat landscape is growing and changing faster than ever.

Just a few years ago, organizations only had to worry about one OWASP Top 10 list. Now there are OWASP Top 10 lists for mobile security, LLMs and more. What's next? And how do you stay ahead of it all?

We've been watching these trends and reporting on them for over eight years now in the Hacker-Powered Security Report. Read on to learn about the impact of AI on security research, what the researchers themselves are thinking and seeing, industry trends, and more. We report on the top vulnerability types, and how the most resilient companies have adopted a defense-in-depth strategy, fortifying every layer of their security posture and using continuous vulnerability testing throughout the software development life cycle.

1    |    8th Annual Hacker-Powered Security Report    |     
Human-powered, AI-enabled security testing remains vital in identifying vulnerabilities that automated scanners often miss, as the creativity and expertise of skilled researchers are unmatched by machines.

Since the first Hacker-Powered Security Report in 2017, the security researcher community has consistently been proven to keep pace with technological changes, deliver ongoing value, and gain the trust of even the most risk-averse organizations.

Over the past decade, we’ve seen significant progress for trust in good-faith research, including updated safe harbor guidelines from the Department of Justice, legislation requiring organizations to implement vulnerability reporting processes, and increasing adoption of vulnerability disclosure and bug bounty programs by leading enterprises. In fact, these programs are now cited in S1 filings as evidence of an organization's commitment to security.
[^1]
[^2]

[^1]: U.S. Department of Justice Office of Public Affairs. Department of Justice Announces New
[^2]: Vulnerability disclosure policies eyed for federal contractors in Senate bill.

1, 2
1
2
Aggregated, anonymized data from the HackerOne Platform, made up of over 500,000 valid vulnerability reports.
Aggregated, anonymized data from the HackerOne Platform, made up of over 500,000 valid vulnerability reports.
A survey, conducted in partnership with Opinion Matters, of 500 security leaders globally about their approach to cybersecurity challenges.
Our annual survey of 2,000+ highly skilled and active members of the security researcher community, covering topics ranging from the time they dedicate to hacking to their views on AI regulations. The respondents reflect the diversity of location, experience, expertise, and age that defines HackerOne’s global community of security researchers.
Our annual survey of 50 customers, representing a range of organizational sizes, structures, and industries.

This 8th Annual Hacker-Powered Security Report compiles insights, data, and analysis from customers, security researchers, and HackerOne’s comprehensive vulnerability database. The insights are gathered from:

3    |    8th Annual Hacker-Powered Security Report    |     
Researchers and security professionals alike see AI as both a risk and an opportunity. 48% of security leaders said that generative AI (GenAI) was one of the most significant risks they saw impacting their organization, with data integrity being a key priority to secure.

The security researcher community is maturing its skill sets to meet the demands of customers, with more members focusing on mobile, APIs, and AI deployments as testing scope expands to more varied attack surfaces. Nearly 10% of researchers now specialize in AI to meet the growing demand of AI testing engagements. 

The top vulnerability reported to a bug bounty program is cross-site scripting (XSS), whereas for a pentest it’s misconfiguration. Pentests tend to uncover more systemic or architectural vulnerabilities while security researchers working on bug bounty programs focus more on real-world attack vectors, user-level issues, and business logic flaws. 

The most security-resilient organizations have refined their engagement with the researcher community to achieve the ideal formula for impactful results, focusing on a broad scope and a select team of trusted researchers. High-impact programs—those with over 30% of valid vulnerability submissions rated as high or critical—work with fewer researchers; the average number of researchers on a high-impact program is 56, vs. 97 on lower-impact programs. 

The most technologically advanced industries are seeing results when it comes to the efforts to reduce common vulnerabilities in production, with Web3 companies seeing 65% fewer reports for cross-site scripting than the industry average. 

Key Findings from the Report    |    8th Annual Hacker-Powered Security Report    |    4
    |    8th Annual Hacker-Powered Security Report    |    4

## The Impact of AI on Security Research and Vulnerability Management
Last year we introduced a dedicated AI section in the Hacker-Powered Security Report, recognizing the growing influence of GenAI on how organizations operate and plan ahead. This year we’re digging deeper into both security for AI (how organizations manage risks in AI deployments) and AI for security (how researchers and organizations use AI to improve vulnerability management). We also highlight the crucial role human expertise plays in keeping AI innovation trustworthy and secure for everyone.

“The downside of AI is that it introduces more vulnerabilities. If a company uses it, we’ll find bugs in it. AI is even hacking other AI models. It’s going so fast and security is struggling to catch up.”
Jasmin Landry, @jr0ch17
Security Researcher and HackerOne Pentester5    |    8th Annual Hacker-Powered Security Report    |     
5    |    8th Annual Hacker-Powered Security Report    |     
We surveyed 500 security professionals to understand their experiences and opinions around AI adoption within their industries and organizations. Nearly half (48%) cited GenAI as one of the most significant risks facing their organizations. The top concerns included training-data leaks (35%), unauthorized AI usage within their organizations (33%), and the hacking of AI models by external parties (32%).

### Security for AI
Which of the following IT-related risks are of most concern to your organization?    |    8th Annual Hacker-Powered Security Report    |    6
    |    8th Annual Hacker-Powered Security Report    |    6

64% of respondents believe GenAI will have a major impact on their organization, with 62% confident in their ability to secure its use. Additionally, 70% believe that AI legislation will help enhance safety and security. However, 51% are concerned about the reputational risks tied to AI, and another 51% highlight that basic security practices are being overlooked in the rush to implement GenAI.

When we asked the same questions to a group of HackerOne customers, we found similar views on the impact of GenAI—64% agreed it would significantly affect their operations. However, only 38% felt confident in their ability to defend against AI-related threats, and just 39% believed that legislation would make AI safer.

As highly knowledgeable and technologically advanced organizations, HackerOne’s customers have a deep understanding of the challenges involved in securing this rapidly evolving technology. Interestingly, they were less concerned about the reputational risks of AI than non-customers were, with 48% of customers expressing worry.

Which of the following GenAI risks are of most concern to your organization? 
7    |    8th Annual Hacker-Powered Security Report    |     
“It’s been previously observed in research from red teaming exercises of AI models that some individuals are significantly more effective at breaking the models’ defenses than others. I was surprised that many of the researchers did not know much about AI but were able to use creativity and persistence to get around our safety filters.”
Ilana Arbisser
Technical Lead, AI Safety, Snap Inc.

HackerOne customers are taking proactive steps to avoid AI-related security incidents. The number of AI assets included in HackerOne programs has surged by 171% over the past year and will soon surpass 1,000 assets. 

AI red teaming—where organizations invite security researchers to identify safety and security flaws in their AI products—is gaining traction as a best practice for testing GenAI deployments. In fact, 67% of security leaders and HackerOne customers believe that an external, unbiased review of GenAI implementations is the most effective way to uncover AI safety and security issues.    |    8th Annual Hacker-Powered Security Report    |    8
    |    8th Annual Hacker-Powered Security Report    |    8

LLM06: Sensitive Information Disclosuure
LLM06: Sensitive Information Disclosuure

Concerns about AI safety are driving more organizations to seek third-party testing. Of all AI vulnerability reports submitted, 55% are related to AI safety issues. AI safety issues often have a lower barrier to entry for valid reporting and present a different risk profile compared to traditional security vulnerabilities. The reduced barriers to entry for AI safety reports means bounties for these reports are slightly lower, with an average payout of $401, versus $689 for AI security programs. While AI safety vulnerabilities are currently in scope for a limited number of programs, the volume of reports is notably higher, making AI safety one of the top five reported vulnerabilities. 
9    |    8th Annual Hacker-Powered Security Report    |     
Establish continuous testing, evaluation, verification, and validation throughout the AI model life cycle.
Provide regular executive metrics and updates on AI model functionality, security, reliability, and robustness. Regularly scan and update the underlying infrastructure and software for vulnerabilities.
Determine country-, state-, or government-specific AI compliance requirements. Some regulations exist around specific AI features, such as facial recognition and employment-related systems. Establish an AI governance framework outlining roles, responsibilities, and ethical considerations, including incident response planning and risk management.
Train all users on ethics, responsibility, legal issues, AI security risks, and best practices such as warranty, license, and copyright. Establish a culture of open and transparent communication on the organization’s use of predictive or generative AI.

For a more detailed checklist for both safety and security testing engagements, download The Ultimate Guide to Managing Ethical and Security Risks in AI.

### What’s the difference between AI Safety and AI Security?
AI Safety
Focuses on preventing AI systems from generating harmful content, from instructions for creating weapons to offensive language and inappropriate imagery. It aims to ensure responsible use of AI and adherence to ethical standards.
AI Security
download The Ultimate Guide to Managing Ethical and Security Risks in AI.
    |    8th Annual Hacker-Powered Security Report    |    10

### Recommendations
    |    8th Annual Hacker-Powered Security Report    |    10

AI and automation are powerful efficiency tools, saving organizations an average of $2.2 million per breach[^3] by helping to detect and contain breaches faster, reducing overall impact. Companies without AI and automation face longer response times and higher breach costs.

In a survey of over 2,000 security researchers on the HackerOne Platform, 20% now see AI as an essential part of their work, up from 14% in 2023. However, only 38% reported using AI in any capacity, down from 53% last year, suggesting that researchers who find real value in AI are investing more deeply, while others may have pulled back after finding less success with initial experiments.

[^3]: IBM. Cost of a Data Breach Report 2024.
Are you currently using, or do you plan to use, GenAI for any of the following purposes? 
11    |    8th Annual Hacker-Powered Security Report    |     
11    |    8th Annual Hacker-Powered Security Report    |     
“I leverage AI-powered vulnerability scanners to quickly identify potential weak points in a system, allowing me to focus on more complex and nuanced aspects of security testing. I also use AI for reporting. Previously, I spent 30-40 minutes writing reports to ensure all details were included, the tone was appropriate, and there were no grammatical mistakes. AI has streamlined this process, reducing the time to an average of 7-10 minutes per report.” 
Hazem Elsayed, @hacktus
Security Researcher

“When pentesting, I use AI to automate repetitive and time-consuming tasks so I can concentrate on finding security issues. I also use AI to summarize documentation when I want a general overview of a new technology. When I do content discovery before my pentest, AI allows me to generate customized wordlists to find niche content that can fly under the radar of commonly used wordlists."
Adam Deziri, @a_d_a_m
Security Researcher

33% of security researchers are using AI to summarize information and write reports.

HackerOne customers can also use AI to streamline and enhance their vulnerability management process via the platform’s GenAI copilot, Hai. Hai provides a deeper, more immediate understanding of incoming reports, enabling faster decision-making and quicker fixes.

### Accelerate Vulnerability Remediation with Hai
    |    8th Annual Hacker-Powered Security Report    |    12
    |    8th Annual Hacker-Powered Security Report    |    12
Use Hai’s tailored advice to quickly interpret complex vulnerability reports with concise summaries and deeper insights for faster decision-making in the context of your unique technology stack and business needs.

Use Hai to optimize vulnerability reports by having it suggest accurate titles, CVSS scores, and vulnerability classifications. Hai can also help you craft clear and succinct messages for effective communication between security, development teams, and researchers.

Automate tasks by integrating Hai to assist with writing assistance, generating custom vulnerability scanner templates, and managing large reports, reducing manual effort.
Automate tasks by integrating Hai to assist with writing assistance, generating custom vulnerability scanner templates, and managing large reports, reducing manual effort.

Cybersecurity Consultant, Enterprise, Financial Services

### Recommendations
“Hai is a game-changer for our communication with researchers. Managing relationships and keeping messages clear and concise can be challenging, especially with high expectations from both researchers and managers. Short replies can be misunderstood, while longer responses are time-consuming. Hai helps us craft more precise and neutral messages, proofreads our communications, and maintains a consistent tone. This efficiency allows us to engage with more researchers and allocate time to other critical tasks." 13    |    8th Annual Hacker-Powered Security Report    |     
13    |    8th Annual Hacker-Powered Security Report    |     

## Security Researchers Expand Their Expertise Into AI, APIs, and More
More of the security researcher community is choosing the flexibility of a full-time career as security researchers are dedicating more hours to developing their skills. 30% now hack full-time, up from 24% in 2023, and 44% spend over 20 hours a week hacking, compared to 35% the previous year.

While 77% of researchers cite earning money as a key motivator, 64% view hacking as a valuable way to learn and develop their skills, and 48% do it to advance their careers. Additionally, 34% are driven by a strong desire to protect businesses and end users, highlighting the community's commitment to making a positive impact.
    |    8th Annual Hacker-Powered Security Report    |    14
    |    8th Annual Hacker-Powered Security Report    |    14
What motivates you to hack?

When HackerOne first launched, most hacking activity focused on web applications, and while 88% of researchers still specialize in this area, the landscape is shifting. Organizations are now calling on the community to test a wider range of products and technologies. 56% of researchers also specialize in APIs, while almost 10% now focus on AI and large language models (LLMs). Although the number of AI-focused researchers has grown by just 2% since last year, it's promising that nearly 10% are already working to secure this emerging technology. As more organizations include AI models in their scope, we expect this number to keep growing.

When hacking web applications, what vulnerability types do you focus on?
15    |    8th Annual Hacker-Powered Security Report    |     
Security researchers excel in reconnaissance and manual exploitation—two key hacking skills that automated scanners can't match. These tasks require human creativity, like uncovering an unsecured, overlooked domain or spotting a unique vulnerability from an outsider’s view. Even more advanced is exploit chaining, where vulnerabilities are combined into a larger, more impactful exploit. While chaining might be more challenging for individuals, researchers often collaborate, blending their strengths to create powerful, high-impact exploits.

Data indicates many researchers feel less confident in writing detailed reports, but GenAI tools are bridging this gap, enabling clearer communication of findings and higher-quality reports.

Which asset types do you focus on in the bug bounty programs you participate in?    |    8th Annual Hacker-Powered Security Report    |    16
    |    8th Annual Hacker-Powered Security Report    |    16
Clearly communicate expected response times for report acknowledgment, triage, and resolution. This builds trust and helps researchers understand when they can expect feedback.
Offer constructive feedback on the report, explaining the vulnerability’s impact and any necessary remediation steps.
Respond to researchers with respect and professionalism, even if the report is invalid or a duplicate. Positive interactions encourage ongoing collaboration.

The more you and your organization know and understand about researchers and their skills, motivation, and approaches, the stronger the relationship will be and the more impactful your program will be.

“With scanning tools, false positives are through the roof. A human researcher, however, can provide more information and context about a vulnerability, often leading to Goldman fixing the problem quickly. We don’t want problems to sit around.”
Matt Levine
Global Head of Technology Risk Advisory, Goldman Sachs
Respond to researchers with respect and professionalism, even if the report is invalid or a duplicate. Positive interactions encourage ongoing collaboration.

What part of the hacking process do you consider yourself most skilled at?17    |    8th Annual Hacker-Powered Security Report    |     
17    |    8th Annual Hacker-Powered Security Report    |     

## Run a Top-Tier Program That Won’t Break the Bank
The most security-resilient customers on the HackerOne Platform share the following attributes:
Thoughtfully designed rewards that direct researcher attention toward the organization’s priorities
Thoughtfully designed rewards that direct researcher attention toward the organization’s priorities
Excellent communication with researchers who report vulnerabilities
Clear expectations set from the start, including a well-defined scope and descriptive policy
Safe harbor legal protections for security researchers
Clear expectations set from the start, including a well-defined scope and descriptive policy
Safe harbor legal protections for security researchers
    |    8th Annual Hacker-Powered Security Report    |    18
    |    8th Annual Hacker-Powered Security Report    |    18
How do you choose the companies you hack?

What would make you decide not to hack on a program?
19    |    8th Annual Hacker-Powered Security Report    |     
Focus researchers’ efforts on the most critical components of your attack surface. These could be assets that have stagnant testing, have lacked attention, are new feature investments, or are recent acquisitions.
Offer more advanced testing opportunities with unique scope or access to gated assets.
Provide researchers with additional documentation to clarify scope, free test accounts, or even company swag to maximize impact without solely relying on increased bounties.

“The bounty table is important. but I invest in programs that give back to me in the way they communicate and their time to fix. If they fix bugs fast, there will be fewer duplicates, which provides greater motivation for me.”
Jasmin Landry, @jr0ch17
Security Researcher and HackerOne Pentester

Beyond the financial aspect, researchers value strong relationships with security teams, transparent communication, and quick responses to bounties and report resolutions. Clear updates on report status build trust, and offering context when a report's criticality is downgraded helps foster collaboration. Additionally, 41% mentioned that negative peer reviews would discourage them from participating, underscoring how important perception is for attracting researchers, driving engagement, and scaling a program effectively.

### Recommendations
    |    8th Annual Hacker-Powered Security Report    |    20
    |    8th Annual Hacker-Powered Security Report    |    20
Bounty table alignment with industry standards
Brand impact and target organization profile (e.g., a Fortune 500 financial services company under media scrutiny may offer higher payouts than a local bank)
Transparent, collaborative communication with the researcher community
The organization's reputation among researchers
Opportunities for public disclosure and transparency of vulnerabilities
Opportunities for public disclosure and transparency of vulnerabilities

### Perspectives From the Hacker Advisory Board
"Gather feedback from hackers to improve your program. Ask what they'd like to see, such as adding assets to scope—something I’ve requested in the past, which led to discovering additional vulnerabilities. Lower barriers to entry; extra policies or special requirements may discourage researchers from participating."
21    |    8th Annual Hacker-Powered Security Report    |     
21    |    8th Annual Hacker-Powered Security Report    |     
Most security researchers are attracted to a wide range of assets in scope, and only a few shy away from targets seen as tough to crack. With the right incentives, they’re more than ready to take on the challenge. 
Higher bounties: Offering average payouts of $3,300 at the 95th percentile, compared to $2,000 for lower-impact programs.
Smaller, focused communities: Engaging fewer researchers, with an average of 56 versus 97 in lower-impact programs. However, being able to curate a smaller, highly engaged group depends on having a large researcher pool from which to choose the most applicable talent for your program.
Higher bounties: Offering average payouts of $3,300 at the 95th percentile, compared to $2,000 for lower-impact programs.
Smaller, focused communities: Engaging fewer researchers, with an average of 56 versus 97 in lower-impact programs. However, being able to curate a smaller, highly engaged group depends on having a large researcher pool from which to choose the most applicable talent for your program.
Broader testing scope: Providing more assets for testing, averaging 60 assets compared to 34 in lower-impact programs.    |    8th Annual Hacker-Powered Security Report    |    22
    |    8th Annual Hacker-Powered Security Report    |    22
Collaborate with a select group of skilled researchers who align well to your program’s scope.
Establish reward structures aligned with the criticality of the assets being tested, ideally offering compensation above market standards.
Ensure your testing scope is broad and varied, allowing researchers with diverse skill sets to contribute meaningfully. This targeted approach fosters deeper engagement and drives more impactful security outcomes.
Collaborate with a select group of skilled researchers who align well to your program’s scope.
Establish reward structures aligned with the criticality of the assets being tested, ideally offering compensation above market standards.
Read more about how HackerOne customers get the best results from researchers.

### Recommendations
“I believe in a blanket approach when it comes to which assets to test with bug bounty. Test everything across the board. People say, ‘We don’t want to put everything out there,’ but, if one asset is compromised, then the next is too. If it’s external facing, it should be tested.”
Jose Ramos
Leader in Offensive Security and Penetration Testing, Uber
23    |    8th Annual Hacker-Powered Security Report    |     

### Community Events Bring the Best and the Brightest Together for Maximum Impact
HackerOne's most security-resilient customers excel at incentivizing researchers to focus on specific scopes at strategic times. Through high-caliber, targeted engagements, HackerOne replicates real-world threats to pinpoint vulnerabilities, especially during flagship community events.

#### Live Hacking Events
Live Hacking Events (LHEs) bring together top security researchers to focus on high-priority scopes for mature customers. These events produce 34% high and critical vulnerability reports, compared to the platform average of 27%. Collaboration is a major factor, with 48% of valid reports and 69% of bounty awards in 2023 resulting from joint efforts. LHEs also have lasting benefits, boosting post-event engagement by an average of 15%, making them a key driver of impactful security improvements.
    |    8th Annual Hacker-Powered Security Report    |    24
“Capital One puts the security of our customers and our systems at the forefront of everything we do. Live Hacking Events are a key component of our robust security testing strategy and are a unique and dynamic way to engage with the ethical hacking community, allowing us to form close partnerships with each of the hackers. Across the industry, these types of events are considered a gold standard to ensure companies are approaching risk from every potential angle, and we're grateful for the hackers' hard work and partnership to help us further bolster our defenses.”
Kathryn Torelli
Bug Bounty Lead, Capital One

“A Live Hacking Event is an experience removed from day-to-day hacking with new scope, higher bounties, and direct access to the customer team. The customers benefit from having nearly 100 of the most elite hackers in the world concentrating on their program for a solid three weeks. My approach to hacking at an LHE is to pick an obscure scope early on, something that I know other people won’t be looking at.”
Douglas Day, @arch_angel
LHE Researcher, Most Valuable Hacker Award Winner

#### Ambassador World Cup
The Ambassador World Cup (AWC) is an annual event that brings international researcher teams together for a friendly competition, with the goal of delivering the most impactful results for participating customers. While more accessible than a Live Hacking Event, the Ambassador World Cup still provides customers with dedicated attention from highly motivated and skilled researchers. Beyond the contributions of the competing teams, the event's visibility encourages wider community engagement, as researchers are drawn to test on high-profile customer programs after seeing the activity through their networks and social media. In the 2023 Ambassador World Cup, researchers reported over 800 valid vulnerabilities for the 11 participating customers, demonstrating the event's ability to drive meaningful security outcomes.
25    |    8th Annual Hacker-Powered Security Report    |     
“Participating in the Ambassador World Cup was an incredible opportunity for Adobe to build deep relationships with the hacker community. I received great feedback about our bug bounty program and the AWC experience. Many hackers were new to our program, which was a great way to expand Adobe's outreach to the hacking community.”
Daniel Ventura
Product Security Manager, Adobe PSIRT & Bug Bounty, Adobe

"The Ambassador World Cup was transformative, offering a unique chance to enhance my skills on programs like Mercado Libre, where I had one of my best triage experiences. AWC introduced me to new programs, expanding my horizons."
Sandip Oli, @notsandip
Team Nepal of the AWC
    |    8th Annual Hacker-Powered Security Report    |    26

### Budgeting for Bounties
Bounties can make or break a bug bounty program, the bounty table being the number-one factor for researchers making a decision on which programs to spend time, with half being put off a program that has uncompetitive bounties. 

Average bounty payouts have remained steady over the past 12 months, with a 5% increase year over year, from $1,066 to $1,116. However, that’s a decrease of 10% from 2021, when the average bounty was $1,246. Organizations need to be wise to the fact that without competitive compensation, talented researchers may move to more lucrative programs, or focus only on low-hanging fruit that doesn’t require detailed research effort, resulting in less exploitable, less critical vulnerabilities. Dynamic, fair compensation is key to keeping researchers engaged and improving organizational security.

Bounties are typically more competitive in the critical vulnerability category, with the most technology-reliant organizations seeing an increase of between 20% (internet and online services) and 450% (crypto and blockchain) since 2023. 

Low-severity bounties, however, have not changed significantly year over year. This could be as a result of an increase in automated tools that surface low-level vulnerabilities before researchers can find them, reducing the competition. 

The following table shows the median, average, and 95th percentile bounty payouts across various industry sectors. As in previous years, crypto and blockchain organizations continue to pay well above the average for vulnerabilities. The high financial risk, technical complexity, and reputational stakes in this space drive these organizations to offer significantly higher bounties to attract top-tier security researchers. We also see more differences between the industries when we look at the 95th percentile, with traditionally security-mature industries like internet and online services and retail and e-commerce paying toward the top end of the average across all levels of severity.
27    |    8th Annual Hacker-Powered Security Report    |     
Median, Average, and 95th Percentile Bounty Rewards
    |    8th Annual Hacker-Powered Security Report    |    28
Make a strong business case for your budget that speaks to the priorities of your stakeholders and board members. Check out the Measuring Success section of this report to see how the most security-resilient organizations are making the financial case for their bounty budgets using a return on mitigation (ROM) approach.
Take a tiered-award approach, with bounty awards weighted by asset type. Bounty award
Make a strong business case for your budget that speaks to the priorities of your stakeholders and board members. Check out the Measuring Success section of this report to see how the most security-resilient organizations are making the financial case for their bounty budgets using a return on mitigation (ROM) approach.
Take a tiered-award approach, with bounty awards weighted by asset type. Bounty award amounts can be adjusted to incentivize testing on your most critical assets as well as assets that may require a more unique skill set.
Set bounties high enough to attract interest. If you're falling behind your budget and not receiving reports on business-critical assets, it's a clear sign that your bounties may need adjustment.

### Recommendations

## The Top Ten Vulnerabilities Need to Change
HackerOne has been measuring the top ten vulnerabilities reported on our platform for eight years. Despite the investment in security, and industry calls for better security practices earlier in the software development life cycle (SDLC), we see steady increases in vulnerability reports year over year and most industries are still seeing the most common vulnerabilities reported again and again. 
29    |    8th Annual Hacker-Powered Security Report    |     
29    |    8th Annual Hacker-Powered Security Report    |     
# of Valid Reports per Year
What Percentage of Vulnerability Reports Is High or Critical for Your Industry?    |    8th Annual Hacker-Powered Security Report    |    30
    |    8th Annual Hacker-Powered Security Report    |    30
Organizations that spend less on technology often see more severe vulnerabilities, sometimes hitting 42%. In comparison, tech-focused sectors like crypto, travel, and internet services show around 20% for severe issues, while critical infrastructure areas like energy and healthcare exceed 35%. Telecoms and media, with their large asset counts, also face a higher rate of critical findings, suggesting that as an attack surface grows, it's harder to stay on top of potential vulnerabilities.

High and critical reports might be a smaller portion of overall findings, but they account for most of the bounty spend, especially as severe reports increase. This trend is even more pronounced in the crypto and blockchain sectors, where top bounties can hit up to $1 million in the 95th percentile.

Over the past year there was a sharp 180% jump in breaches exploiting vulnerabilities, according to Verizon’s Data Breach Investigations Report.[^4] Incidents like MOVEit and other zero days fueled this surge, mainly driven by ransomware and extortion-focused attackers, with web applications being the primary entry point.

Looking at the percentage of valid high or critical reports reveals an interesting trend:
[^4]: Verizon. 2024 Data Breach Investigations Report.
31    |    8th Annual Hacker-Powered Security Report    |     
31    |    8th Annual Hacker-Powered Security Report    |     
The good news? There’s a clear path to stronger security. HackerOne data shows that the top ten vulnerabilities reported to customer programs are common and mostly preventable with proactive measures. Catching these issues early in the SDLC can significantly cut down on bounty costs. Check how your industry stacks up against the average for common vulnerabilities, and see the 5
Reports for the three most common vulnerabilities are all down by a small percentage platform-wide since 2023, with reports for cross-site scripting down 10%, suggesting that some of the tactics to reduce common vulnerabilities are having an impact. When we look at where specific industries are seeing the most reports, however, we see a different trend, with significant increases in reports for the vulnerability types most common in their systems.

Despite the rising threat, vulnerabilities are often still seen as just part of the tech landscape. As Jen Easterly, Director of CISA, stressed in her 2024 Black Hat address,[^5] the industry needs a shift toward building software with security as a priority.
[^5]: Cyberscoop. Easterly: Cybersecurity is a software quality problem.
    |    8th Annual Hacker-Powered Security Report    |    32
    |    8th Annual Hacker-Powered Security Report    |    32
The Top Ten Vulnerabilities Reported to Customer Programs
33    |    8th Annual Hacker-Powered Security Report    |     

### Financial Services
Financial services is one of the most targeted and regulated sectors, having experienced 70 compromises in Q1 2023, impacting about 1.7 million victims.[^6] Due to strict regulations like GDPR and PCI-DSS, they tend to receive more vulnerability reports, as these standards incentivize researchers to flag potential issues.

Insecure direct object reference vulnerabilities are particularly prevalent in financial services because of their complex, multi-layered applications that manage sensitive data, like personal financial information and transactions. The frequent user actions, such as money transfers and account access, heighten the risk of IDOR exploits when access controls are weak, making them prime targets for bug bounty hunters.
[^6]: SANS 2023 Attack and Threat Report.
    |    8th Annual Hacker-Powered Security Report    |    34
    |    8th Annual Hacker-Powered Security Report    |    34
Implement a strong authorization framework that relies on user policies and hierarchy, and validate authorization for every request that involves accessing sensitive objects or resources.
Avoid using functions that automatically bind a client's input into variables, internal objects, or object properties. 
Use indirect, random, and unique identifiers instead of exposing direct references to internal objects and resources. Map these identifiers to the actual objects on the server side while validating and authorizing user-supplied input.

### Recommendations
“Having hacked on a variety of financial service targets, I've noticed that these organizations often have a wider and more complex attack surface due to their company structures, which often include numerous acquisitions and subsidiaries. As a result, I’ve found vulnerabilities on obscure hosts—sometimes on newly launched or less commonly known domains. Due to the need to obtain an account for deeper testing, which is difficult and sometimes even impossible due to geographical restrictions (applying for a loan/credit card), a significant portion of the attack surface remains untouched." 
Implement a strong authorization framework that relies on user policies and hierarchy, and validate authorization for every request that involves accessing sensitive objects or resources.
Avoid using functions that automatically bind a client's input into variables, internal objects, or object properties. 
Use indirect, random, and unique identifiers instead of exposing direct references to internal objects and resources. Map these identifiers to the actual objects on the server side while validating and authorizing user-supplied input.
Richard Alviarez, @Rhack
Security Researcher Specializing in Financial Services Organizations
35    |    8th Annual Hacker-Powered Security Report    |     

### Government
Government agencies see a much higher rate of XSS vulnerability reports than the industry average. This is likely due to their many complex web environments, as they manage a wide range of websites and services for various public functions. This diversity can lead to inconsistent security practices, making some sites more vulnerable. Plus, many government systems run on older