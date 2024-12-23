```markdown
# Table of Contents
- [State of the Software Supply Chain](#state-of-the-software-supply-chain)
- [Open Source Scale and Consumption Behaviors](#open-source-scale-and-consumption-behaviors)
- [Persistent Risk and Consumer Complacency](#persistent-risk-and-consumer-complacency)
- [Efficiency and Waste: The Time Drain on Developers](#efficiency-and-waste-the-time-drain-on-developers)
- [A Call to Action and Vigilance: Proactive Management, Continuous Security, and Advanced Tooling](#a-call-to-action-and-vigilance-proactive-management-continuous-security-and-advanced-tooling)
- [10 Year Look Back](#10-year-look-back)
- [Attackers and the Evolution of Software Supply Chain Exploits](#attackers-and-the-evolution-of-software-supply-chain-exploits)
- [Consumers of Open Source](#consumers-of-open-source)
- [Publishers of Open Source](#publishers-of-open-source)
- [SBOM Production by Open Source Projects](#sbom-production-by-open-source-projects)
- [A Decade of Software Regulations](#a-decade-of-software-regulations)
- [Navigating the Future of Open Source and Software Supply Chain Security](#navigating-the-future-of-open-source-and-software-supply-chain-security)
- [Scale of Open Source](#scale-of-open-source)
- [Open Source Supply Balloons Due to Malicious Actors](#open-source-supply-balloons-due-to-malicious-actors)
- [Open Source Consumption Rockets Through npm](#open-source-consumption-rockets-through-npm)
- [2024 Ecosystems by the Numbers](#2024-ecosystems-by-the-numbers)
- [Individual Ecosystem Analysis](#individual-ecosystem-analysis)
- [Differentiating Software Vulnerabilities and Open Source Malware](#differentiating-software-vulnerabilities-and-open-source-malware)
- [Vulnerabilities in the Open Source Ecosystem](#vulnerabilities-in-the-open-source-ecosystem)
- [Open Source Malware & Next Gen Supply Chain Attacks are Now Commonplace, Dangerous Business](#open-source-malware--next-gen-supply-chain-attacks-are-now-commonplace-dangerous-business)
- [Malware Types](#malware-types)
- [Notable Malicious Packages](#notable-malicious-packages)
- [Evolution of Open Source Risk](#evolution-of-open-source-risk)
- [Persistent Risk](#persistent-risk)
- [Open Source Consumption](#open-source-consumption)
- [Can We Minimize Persistent Risk](#can-we-minimize-persistent-risk)
- [Choice](#choice)
- [The Impact of Foundation Support on Open Source Quality](#the-impact-of-foundation-support-on-open-source-quality)
- [Complacency](#complacency)
- [Contamination](#contamination)
- [Optimizing Efficiency & Reducing Waste](#optimizing-efficiency--reducing-waste)
- [Size Doesn’t Matter: All Applications Have Sizable Risk](#size-doesnt-matter-all-applications-have-sizable-risk)
- [Stop Wasting Developer Time — What to Look for in an SCA Tool](#stop-wasting-developer-time--what-to-look-for-in-an-sca-tool)
- [Open Source License Risk Profile](#open-source-license-risk-profile)
- [Best Practices in Software Supply Chain Management](#best-practices-in-software-supply-chain-management)
- [Best Practices](#best-practices)
- [Cybersecurity is a Universal Issue](#cybersecurity-is-a-universal-issue)
- [Preparing for Governance and Regulations Around the World](#preparing-for-governance-and-regulations-around-the-world)
- [Reliable Dependency Management](#reliable-dependency-management)
- [Acknowledgments](#acknowledgments)
- [About the Analysis](#about-the-analysis)

© 2015-PRESENT, SONATYPE INC. ALL RIGHTS RESERVED.

# State of the Software Supply Chain

As we mark the 10th annual State of the Software Supply Chain report, the transformation of open source software has been nothing short of profound. Open source consumption has exploded, with estimates placing this year’s downloads at over 6.6 trillion. This reliance on open source components, now making up to 90% of the modern software application, has ushered in both unprecedented innovation and complex challenges for software supply chains. Because of this, the industry has also become increasingly regulated, moving from a hands-off approach in the early 2010s to proactive frameworks that address growing cybersecurity risks in the global software supply chain.

This year’s report, backed by data from over 7 million open source projects, double-clicks on many of the unsettling trends in security and risk management we’ve been following in the past 10 reports. Notably, the rise of open source malware and software supply chain attacks has become a critical threat. Examples such as the LUMMA malware found in PyPI and the XZ Utils package backdoor highlight the growing sophistication of these attacks, which often bypass traditional security measures, leaving organizations vulnerable. In fact, the number of malicious packages has grown by 156% year-over-year, posing a significant risk to enterprises that fail to manage their OSS dependencies effectively.

Here’s what else we found.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
1
EXECUTIVE SUMMARY

# Open Source Scale and Consumption Behaviors

Open source software adoption is at a multitrillion request scale, with ecosystems like JavaScript (npm) and Python (PyPI) leading the charge:

- JavaScript (npm) accounted for a staggering 4.5 trillion requests in 2024, representing 70% year-over-year growth in requests​.
- Python (PyPI), driven by AI and cloud adoption, is estimated to reach 530 billion package requests by the end of 2024, up 87% year-over-year.​

But this growth brings new risks. A rise in open source malware has infiltrated open source ecosystems at an alarming rate.

Over 512,847 malicious packages have been logged just in the past year, a 156% increase year-over-year​, highlighting a critical need for organizations to adapt their consumption practices. Traditional security tools often fail to detect these novel attacks, leaving developers and automated build environments highly vulnerable. This has resulted in a new wave of next-generation supply chain attacks, which target developers directly, bypassing existing defenses.

Further, each ecosystem presents different challenges. For instance, npm has experienced much of its growth from spam; Python is the fastest-growing in projects and volume, and shows more vulnerabilities per package compared to others; and Java (Maven) has an average of 28 versions per project.

Read more in our chapter on Open Source Scale.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
2
EXECUTIVE SUMMARY

## OPEN SOURCE SCALE AND CONSUMPTION BEHAVIORS BY THE NUMBERS

530 BILLION
Python (PyPI) package requests, 80% YoY increase LARGELY DRIVEN BY AI & CLOUD

4.5 TRILLION
JavaScript (npm) requests, 70% YoY growth

512,847
malicious packages discovered since November 2023

156%
YoY growth of malicious packages

# Persistent Risk and Consumer Complacency

In parallel, organizations continue to struggle with efficient risk mitigation. This is why this year, we introduce the concept of “Persistent Risk,” a combination of unfixed and corrosive vulnerabilities that continues to erode the security integrity of software over time. A prime example of this is Log4j, where 13% of downloads remain vulnerable three years after the Log4Shell vulnerability was exposed. While we’re extremely focused on this rise in contaminated open source projects, or malware, the reality is all open source or commercial software will eventually have bugs that evolve into vulnerabilities; they age more like steel, not aluminum, becoming rusty after extensive corrosion.

The prevalence of such risks underscores the complacency that still defines much of the industry’s approach to open source consumption.

- 80% of application dependencies remain un-upgraded for over a year, even though 95% of these vulnerable versions have safer alternatives readily available. It’s not a matter of ‘if’ a breach will occur, but ‘when.’
- Only 0.5% of OSS components have no available update (No Path Forward), meaning that nearly all risk is preventable if organizations take proactive steps to update their dependencies.
- Even when updates are applied, 3.6% of dependencies are still vulnerable because they were updated to another insecure version.
- Our analysis of over 20,000 enterprise applications shows that reliance on EOL (end-of-life) components, which no longer receive updates, leads to the gradual breakdown of software integrity, strongly indicating increased security vulnerabilities.
- Looking at discoverability revealed that, despite over seven million open source components, only 10.5% (about 762,000) are actively used. This disparity highlights the noise developers face when selecting components.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
3
EXECUTIVE SUMMARY

## PERSISTENT RISK AND CONSUMER COMPLACENCY BY THE NUMBERS

3.6%
dependencies are upgraded to another insecure version, so are still vulnerable

ONLY 0.5%
OSS components have no available update. NEARLY ALL RISK IS PREVENTABLE

80%
application dependencies remain un-upgraded for over a year

13%
Log4j downloads remain vulnerable 3 years after Log4shell exposure

Despite advances in supply chain security practices, consumer behavior lags, illustrating a critical failure in consumption practices. To address these issues, organizations must embrace best practices like proactive dependency management, choosing high-quality components, and avoiding malware risks.

To better understand how to actually choose high-quality components, we took a look at key heuristics - which include active community engagement, projects publishing Software Bills of Materials (SBOMs), and support from recognized foundations. We notably found that projects backed by recognized foundations have better security practices and reduced vulnerabilities.

# Efficiency and Waste: The Time Drain on Developers

Efficiency in the development process is also at risk. Managing open source risks requires optimizing security policies and practices to keep up with the fast-paced evolution of new OSS libraries. Organizations struggle with the impracticality of slowing down DevOps processes for manual vulnerability reviews, leading to frustration among developers. Enterprises must aim to reduce waste by optimizing their remediation effort with the best possible software composition analysis tool.

Through our analysis, we know:

- Size of application does not matter—with the average applications containing 180 components, even small applications face unmanageable workloads due to increasing dependencies.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
4
EXECUTIVE SUMMARY

## EFFICIENCY AND WASTE BY THE NUMBERS

69%
vulnerabilities initially scored below 7 were corrected to 7 or higher on the CVSS scale upon closer review

ONLY 10.5%
of open source components are actively used out of over 7 million available

180
average number of components per application | EVEN SMALL APPLICATIONS FACE UNMANAGEABLE WORKLOADS

92%
crowdsourced or publicly available data needed a correction once reviewed by a security researcher

- Quality data does matter. 92% of crowdsourced or publicly available vulnerability data needed a correction once reviewed in more detail by a security researcher; 69% of vulnerabilities that were initially scored below 7 on the CVSS scale were corrected to 7 or higher, creating what we’re calling surprise risk and a false sense of comfort.
- Efficiency isn’t just about security, but about licenses: while an open source project typically has an overarching license, individual files may have different licenses as contributions grow, potentially impacting the project downstream.

The current reactive approach to vulnerabilities and license reviews wastes developer time, leading to inefficiency and higher costs. To combat this, enterprises need effective software composition analysis tools that provide high-quality component intelligence and integrate seamlessly into the development process.

# A Call to Action and Vigilance: Proactive Management, Continuous Security, and Advanced Tooling

As attackers evolve their strategies to target the very foundation of software supply chains, the responsibility falls on software manufacturers, consumers, and regulators to adopt robust security practices. We can stop the bleeding and mitigate these mounting risks with proactive dependency management, advanced tooling, and earlier security intervention.

- Always-on security practices, when tools like Software Composition Analysis (SCA) are integrated directly into CI/CD pipelines, and throughout the development process — this can reduce wasted developer time and provide context for informed decision-making​ and get ahead of this risk.
- Reducing Persistent Risk is possible by focusing on tools that help manage dependencies and apply real-time vulnerability detection. In fact, we found that projects using a Software Bill of Materials (SBOM) to manage OSS dependencies showed a 264-day reduction in mean time to remediate (MTTR) compared to those that did not​.

By embedding these practices early and managing OSS consumption more rigorously, organizations can cut down on risks before they grow corrosive and costly. Organizations must prioritize an advanced SCA tool that helps by selecting high-quality, well-maintained components, addressing risks as early as possible, and remaining vigilant against the evolving landscape of supply chain attacks. This proactive approach not only reduces developer frustration but also cuts down on wasted resources. Failure to do so leaves software ecosystems open to catastrophic breaches and operational inefficiencies.

The balance between innovation and security is more critical than ever. Open source ecosystems will continue to fuel technological breakthroughs, but organizations must evolve their security practices to avoid becoming victims of their own success. By addressing complacency, adopting robust tooling, and staying vigilant, software manufacturers can mitigate the Persistent Risks that threaten the future of innovation.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
5
EXECUTIVE SUMMARY

# 10 Year Look Back

As we look back on 10 years of data collection for the State of the Software Supply Chain, it’s a good time to reflect on what has changed — and what hasn’t. This retrospective examines four key dimensions: attackers, publishers, consumers, and regulators.

A decade ago, the cultural landscape was vastly different. Social media was just beginning to show its widespread impact. Instagram had recently been acquired by Facebook, while Snapchat rejected a multibillion-dollar offer from the same giant. Smartphones were everywhere, but apps like TikTok, which would later reshape digital culture, were still far out on the horizon.

In the tech world, cloud computing was maturing, but not yet as integrated into daily life as it is today. Amazon Web Services (AWS) was proliferating, but the full implications of cloud-native development and the shift towards serverless architectures were just beginning to be understood. Kubernetes, which has subsequently revolutionized container orchestration and become a cornerstone of modern infrastructure, was only recently open-sourced by Google.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
6
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
6
LOOK BACK: 10 YEARS OF SSCR

## 10 YEAR LOOK BACK

72,065
SBOMS published by the end of 2023

463%
CVE Growth from 2013–2023

704,102
Malicious Packages Discovered, since proactive identification began in 2019

1,466%
Growth in release frequency between 2014–2023

Many of today’s tech staples were in their infancy. Zoom, now key to remote work, was starting to gain traction, and Slack had just launched, reshaping workplace communication. The Apple Watch and Amazon Echo were just exciting rumors. Smart assistants in every home were still a futuristic idea.

During this period, cybersecurity concerns, particularly in the software supply chain, were gaining attention. The Cyber Supply Chain Management and Transparency Act of 2014, commonly known as the Royce Bill, highlighted the growing recognition of these risks.

One of its most forward-thinking provisions was the Software Bill of Materials (SBOM) requirement — a comprehensive and confidentially supplied list of each binary component within the software, firmware, or product. Though the bill never became law, it’s worth considering how aggressive software transparency a decade ago could have led to a more secure ecosystem today. Had the SBOM requirement been implemented back then, we would have a much deeper understanding and control over the components that make up our digital infrastructure today. In fact, we might have mitigated many of the supply chain attacks and vulnerabilities that have plagued the industry in recent years, setting a higher standard for security and trust in software development long before these issues reached the critical point they now occupy.

This period also preceded the mainstream rise of AI. While AI research was active, and companies like Google and Facebook were investing heavily, public exposure was limited to Netflix recommendations and early virtual assistants like Siri and Alexa.

# Attackers and the Evolution of Software Supply Chain Exploits

Over the past decade, the software supply chain has become a primary attack vector for malicious actors. What was once a relatively niche method of attack has evolved into one of the most significant cybersecurity threats today, driven by the interconnectedness of modern software ecosystems and the increasing reliance on open source components. As software supply chains have grown in complexity, so too have the strategies employed by attackers, who have shifted their focus from directly targeting organizations to exploiting vulnerabilities within the broader supply chain and all of its downstream consumers.

## Early Years: Struts, Heartbleed, and Shellshock (2014–2016)

In the mid-2010s, the software supply chain began attracting more attention from attackers, exemplified by early incidents like CVE-2014-0094, a remote code execution flaw in Apache Struts that allowed attackers to execute arbitrary code on servers running vulnerable framework versions. Although this vulnerability didn’t gain the same notoriety as later software supply chain incidents, it highlighted

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
7
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
7
LOOK BACK: 10 YEARS OF SSCR

> An SBOM mandate when it was first suggested 10 years ago could have redefined software security and stopped today’s supply chain attacks before they began.

the risks posed by unpatched open source components that many organizations relied on for critical infrastructure. This issue came to a head in 2017 with the Equifax breach, but the 2014 vulnerability served as an early warning of the dangers of failing to manage the security of widely-used software dependencies.

Around the same time, Heartbleed and Shellshock sent shockwaves through the cybersecurity world. Heartbleed, a flaw in OpenSSL, exposed millions of servers to data breaches, while Shellshock allowed remote code execution on Unix-based systems. Both demonstrated the vast attack surface of widely-used open source components and emphasized the importance of securing the software supply chain.

These early attacks revealed how vulnerabilities in core open source software could ripple across industries, underscoring the need for better patch management, transparency, and proactive security measures.

## 2017: The Equifax Breach and the Rise of Targeted Supply Chain attacks

The 2017 Equifax breach, caused by the failure to patch a known Apache Struts vulnerability (not the 2014 vulnerability discussed above), marked a turning point for software supply chain security. It showed how a single unpatched flaw in a widely-used framework could lead to a catastrophic breach, as attackers exploited weaknesses in open source components to access critical systems and exfiltrate confidential information for millions of consumers. The incident was a wake-up call for many organizations, illustrating the devastating effects of not properly managing and securing your software supply chains, and bringing open source supply chain vulnerabilities into nationwide headlines for the first time.

2017 marked another significant turning point as the year when the first targeted attacks on the software supply chain began to emerge using open source malware. Data from the Sonatype State of the Software Supply Chain reports in 2017 and 2018 shows that this was the period when attackers started to intentionally inject malicious code into popular open source libraries, targeting the very foundation of the software supply chain. These early attacks were highly selective and designed to infect specific projects with high adoption rates. For instance, compromised versions of popular npm packages and other open source components were downloaded by developers, inadvertently spreading malware to downstream systems.

This shift from opportunistic to targeted exploitation signaled a new era of supply chain attacks. Attackers recognized the strategic value of compromising software at its source, potentially reaching thousands of users with a single strike. This laid the groundwork for more sophisticated and large-scale exploits in the years to come.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
8
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
8
LOOK BACK: 10 YEARS OF SSCR

> This shift from opportunistic to targeted exploitation signaled a new era of supply chain attacks. Sadly, seven years later, in 2024, this is still one of the least understood and recognized attack vectors by security teams. The number of attacks detected in the software supply chain doubled again in 2024, indicating that our industry is mainly defenseless against these growing risks.

## 2020: SolarWinds and the Expansion of Supply Chain Attacks

The SolarWinds attack in late 2020 further demonstrated the growing sophistication of software supply chain threats. In this highly coordinated operation, attackers infiltrated SolarWinds’ build environment and embedded malicious code (Sunburst) into software updates for the company’s Orion platform, distributed to thousands of government agencies and corporations worldwide. SolarWinds represented a new attack level, where adversaries exploited vulnerabilities deep within the development pipeline to compromise trusted software used by high-value targets. This attack was a technical success and underscored the strategic value of supply chain compromises for espionage and broader cyber warfare — and was the roadmap nation state attackers needed to recognize how effective a software supply chain attack could truly be.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
9
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
9
LOOK BACK: 10 YEARS OF SSCR

![Image description](Next Generation Software Supply Chain Attacks (2019–2024) Malicious OSS packages discovered (2019-2024).)

## 2021–2022: Log4Shell, the Vulnerability that Set the Internet on Fire

The discovery of the Log4Shell vulnerability in late 2021 marked another critical moment in the evolution of supply chain threats. A widely used open source logging utility, Log4j was embedded in thousands of enterprise applications and its critical vulnerability opened a massive attack surface. Attackers quickly capitalized on this flaw, and, within hours of its public disclosure, began launching widespread exploitation campaigns. Log4Shell demonstrated how vulnerabilities in a seemingly obscure open source component could ripple through the entire software ecosystem, impacting organizations across industries.

It was only in the wake of Log4shell did the industry become widely conscious of the impacts of the massive growth of open source dependency consumption combined with lack of mature controls — the very thing this report has been evangelizing since 2014 which could have been markedly impacted had the Royce bill passed back then. This incident finally accelerated the urgency around supply chain security, pushing governments and organizations to adopt more stringent practices like Software Bills of Materials (SBOMs) and continuous monitoring of open source components.

## 2024: The Attempted XZ-Utils Supply Chain Attack

In 2024, the attempted supply chain attack on XZ Utils, a widely used compression library, marked a dangerous escalation in open source software security. Unlike typical attacks, this sophisticated, likely nation-state-backed operation followed the “benevolent stranger” playbook. The attackers played a long game, leveraging social engineering to gain trust within the project, which had been maintained by a single developer for nearly two decades. In 2022, pressure from suspected bogus accounts paved the way for a new contributor, Jia Tan, who gradually gained the maintainer’s trust.

Over two years, Jia introduced encrypted malicious code into binary test files embedded in the XZ source code. These files, common in compression packages, went unnoticed due to their subtle nature. The attackers were just days away from having this compromised version ingested by major Linux distributions, which would have allowed backdoors to be deployed to countless systems globally.

The attack was thwarted only by chance, averting widespread infiltration of Linux-based devices and enterprises worldwide. This incident highlights the growing trend of highly organized attackers targeting essential open source projects, aiming for maximum disruption within the global software ecosystem.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
10
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
10
LOOK BACK: 10 YEARS OF SSCR

# Consumers of Open Source

Since we published the first State of the Software Supply Chain Report, the profile of open source software consumers has expanded significantly. It has evolved from primarily being for developers and smaller organizations to now being integral to organizations of all sizes, from startups to large enterprises to government agencies around the world.

The growing reliance on open source reflects confidence in its flexibility and innovation, as well as its ability to reduce time-to-market and development costs and increase organizational agility. But it also brings new risks, particularly with poor dependency management and the rise of open source malware.

Nearly three years after the discovery of the Log4Shell vulnerability, 13% of Log4j downloads are still for known vulnerable versions. While this is an improvement, it should be near zero based on the broad public awareness of the vulnerability, signaling persistent issues with dependency management. Additionally, our research in both 2022 and 2023 found that 96% of vulnerable components downloaded had a fixed, non-vulnerable version available. In this year’s report, this figure only improved slightly to 94.9%, highlighting poor consumption practices aren’t really changing and organizations are bringing in exponentially more risk by not paying attention.

Worse, our research clearly shows that poor dependency management often pairs with other poor choices. Failure to regularly update and oversee open source components allows known vulnerabilities to persist, posing serious risks to the software supply chain.

Meanwhile, the threat of open source malware continues to grow as attackers exploit gaps in poor consumption practices. As mentioned above, the XZ Utils project takeover demonstrated how widely used components, often maintained by overworked and underfunded teams, can become entry points for malicious code.

As open source consumption evolves, so must best practices. Organizations must adopt rigorous practices, improve dependency management, and address open source malware risks to ensure the security and reliability of software supply chains. For more details, see The Evolution of Open Source Risk section in this year’s report.

# Publishers of Open Source

Over the past decade, open source publishers (developers/projects that are creating and then sharing components via public registries like Maven Central) have shown a remarkable transformation in their behavior, driven by both increased demand and growing expectations for rapid innovation. The data on release frequencies highlights key trends in how projects are maintained and evolved.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
11
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
11
LOOK BACK: 10 YEARS OF SSCR

> Poor consumption practices aren’t really changing and organizations are bringing in exponentially more risk by not paying attention.

> 13% of Log4j downloads are still for known vulnerable versions, nearly 3 years after the vulnerability’s discovery.

From 2010 through 2024, there has been a consistent increase in the number of projects where release frequency grew year-over-year. In particular, 2023 and 2024 saw massive growth, with over 1.8 million projects increasing their release cadence in 2023 alone. This surge reflects the accelerating pace of development as publishers race to release new features, fix bugs, and address security vulnerabilities to meet the growing demands of consumers and regulatory pressures. However, this also introduces challenges related to sustainability and stability, as smaller, independent projects struggle to keep up with the pressure to update and improve continuously.

Despite the overall increase, a significant number of projects saw their release frequency decrease or remain unchanged, particularly after 2020.

By 2024, over 300,000 projects had slowed or halted their release cadence, indicating burnout, resource shortages, or shifting priorities among smaller publishers. This shows that while some thrive in a fast-paced environment, many struggle to maintain activity.

Interestingly, projects with stable release cadences have steadily increased, though remain smaller in comparison. These mature projects likely prioritize long-term maintenance and reliability over rapid development, catering to industries that require stable, well-tested software.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
12
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
12
LOOK BACK: 10 YEARS OF SSCR

![Image description](Release Frequency of Open Source Projects Projects that released faster, slower or the same as the prior year.)

> Mature projects likely prioritize long-term maintenance and reliability over rapid development, catering to industries that require stable, well-tested software.

While projects are generally moving more quickly now than they were a decade ago, the rate of vulnerability remediation is slowing significantly.

The data showing how long it takes projects to update their dependencies in response to disclosed vulnerabilities reveals both progress and ongoing challenges in the open source community. While the need for rapid responses to vulnerabilities is well-understood, the actual time it takes for publishers to update dependencies and release secure versions has varied significantly over the years.

In 2017, the mean time to remediate vulnerabilities was relatively short, with some fixes implemented in under 25 days. However, by 2023 and 2024, delays had increased significantly, with some projects taking over 400 days to release secure updates. In 2024, several projects had average fix times exceeding 300 days, with one reaching 470 days. This trend highlights a growing lag in security response, even as timely updates become more critical.

This pattern reflects a growing complexity in software supply chains, where projects often rely on multiple layers of dependencies. As the interconnectedness of open source projects increases, so do the challenges of maintaining prompt security updates. Publishers, especially smaller or less-resourced teams, may struggle to keep up with the need for constant vigilance and fast releases.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
13
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
13
LOOK BACK: 10 YEARS OF SSCR

![Image description](Rate of Vulnerability Remediation Over Time How long a project took to remediate known vulnerabilities in their dependencies.)

> As the interconnectedness of open source projects increase, so do the challenges of maintaining prompt security updates.

The increasing mean time to remediate vulnerabilities points to the strain on publishers to manage their dependency chains efficiently, despite the growing regulatory and consumer expectations for faster responses.

This delay in addressing vulnerabilities has significant implications for the overall security of the open source ecosystem. As projects take longer to implement fixes, the risk of exploitation by malicious actors increases, creating a ripple effect across the software supply chain. The slow pace of updates demonstrates the need for more robust tooling, automation, and support for overwhelmed open source maintainers.

If we break down the mean time to remediate into buckets by vulnerability severity, we see some additional trends.

Over the past decade, the mean time to remediate vulnerabilities has shown a troubling upward trend. While critical vulnerabilities historically received the fastest attention, with average fix times between 200 and 250 days, the data from 2024 shows that even critical issues are now taking significantly longer to address. Some critical vulnerabilities in 2024 took over 500 days to fix, indicating that the response times for the most severe security issues are worsening as complexity in the software supply chain increases.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
14
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
14
LOOK BACK: 10 YEARS OF SSCR

![Image description](Release Frequency by Severity How long projects took on average to remediate dependency vulnerabilities broken down by severity.)

> Some critical vulnerabilities in 2024 took over 500 days to fix, indicating that the response times for the most severe security issues are worsening as complexity in the software supply chain increases.

For high-severity vulnerabilities, the pattern is similar. Earlier in the decade, the average fix times ranged between 150 and 300 days, but in recent years, these have extended beyond 400 days. This growing lag poses a substantial risk to organizations that rely on open source components, as longer fix times create larger windows of exposure for potential exploits.

The most alarming aspect of the data is the spike in fix times for medium- and low-severity vulnerabilities, where we see the clearest indication that publisher capacity has been exceeded. Low-severity vulnerabilities, which previously took 300-400 days to fix, are now seeing delays of 500-700 days or more, with some stretching out nearly 800 days in 2024. This sharp increase suggests that publishers are overwhelmed, struggling to keep up with both the volume of security issues and the ongoing demands of innovation and feature development. The backlog of unresolved low-severity vulnerabilities could lead to greater security risks as these issues accumulate over time.

When we look at the growth of CVE reports over the last decade, it shines a light on why publishers are struggling to keep up.

The massive uptrend beginning in 2016 directly correlates to the increased MTTR seen in the previous analysis.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
15
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
15
LOOK BACK: 10 YEARS OF SSCR
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
15

> Publishers are overwhelmed, struggling to keep up with both the volume of security issues and the ongoing demands of innovation and feature development.

![Image description](Yearly Growth of CVEs, 1999–2023 Vulnerabilities published year over year.)

Overall, the data highlights that the software supply chain has reached a critical point where publisher resources cannot keep pace with the rising volume of vulnerabilities. Without improved automation, tooling, and support for maintainers, the delays in addressing vulnerabilities will continue to increase, leaving organizations exposed to many security risks.

# SBOM Production by Open Source Projects

Following the publication of two new SBOM standards, CycloneDX and SPDX v3, and guided by global government regulations requiring or heavily encouraging SBOMs, we have seen some progress in the number of projects publishing SBOMs alongside their components.

Initiatives like the U.S. Executive Order 14028 have driven increased awareness of SBOMs across the industry, and as a result, we’ve seen open source projects begin to create SBOMs. However, we are still seeing essentially linear growth. In the early days of March 2022, we saw about 68 new SBOMs published per day. More than two years later in June of 2024, we are seeing a little over 200 per day (inconsistently).

While this 3x growth is encouraging, if we compare it to the overall growth in new components in the same time period, the view is much darker.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
16
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
16
LOOK BACK: 10 YEARS OF SSCR

![Image description](Cumulative SBOM Publishing Counts How many components were published with SBOMs.)

Although the number of published SBOMs is increasing, it is far outpaced by the growth rate of new components. This disparity suggests that while SBOM adoption is growing, it has not yet reached a point where it matches the pace of component releases. This needs to change. As more regulations and security practices mandate transparency and traceability through SBOMs, particularly for open source projects that form the backbone of modern software, ecosystems must keep pace.

We don’t want to ignore the progress, but the software industry has significant work to do to embrace comprehensive software transparency.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
17
EXECUTIVE SUMMARY
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
17
LOOK BACK: 10 YEARS OF SSCR

![Image description](Cumulative SBOM Publishing Counts vs Cumulative Published Components Comparing the growth of components with SBOMs vs the overall total shows we are not even beginning to keep up.)

## DISPARITY IN SOFTWARE TRANSPARENCY & TRACEABILITY

60,813
SBOMs published in the last 12 months

VS

6,971,092
Components published in the last 12 months

# A Decade of Software Regulations

## Regulators of Open Source

Over the past decade, regulation of open source software has evolved significantly, driven by the increasing recognition of its critical role in the global software supply chain. A hands-off approach in the early 2010s has given way to more proactive regulatory frameworks, aimed at addressing the growing cybersecurity risks associated with software supply chains. Below is a listing of some of the most impactful recent regulations and their effects on the software supply chain:

### 2014:

The Cyber Supply Chain Management and Transparency Act 2014 (Royce Bill) was an important early milestone. While the Royce Bill ultimately didn’t become law, it called for a Software Bill of Materials (SBOM), now a cornerstone of modern supply chain security efforts. The Bill’s vision, requiring organizations to maintain a comprehensive, confidential list of software components, stood in stark contrast to the industry’s slow pace of embracing this level of transparency, and it