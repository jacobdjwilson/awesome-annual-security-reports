# Organization: Splunk
# Report Title: State-of-Security
# Year: 2022

The State of Security 2022

Global research: Security leaders’ priorities for cloud integrity, the talent gap and the most urgent attack vectors

## Table of Contents
- [The Heat Is (Still) On](#the-heat-is-still-on)
- [The State of Cloud: Business-Critical Baseline](#the-state-of-cloud-business-critical-baseline)
- [Responding to Rising Challenges](#responding-to-rising-challenges)
- [The Path Forward](#the-path-forward)
- [Key Recommendations](#key-recommendations)
- [Appendix](#appendix)

---

## The Heat Is (Still) On

The state of security in 2022 is highly adrenalized — more so than usual. Two years into the deadly and disruptive global pandemic, not only are we continuing to see more attacks, we’re also seeing more actual breaches.

New global research conducted by Splunk and the Enterprise Strategy Group of more than 1,200 security leaders found that 49% of organizations say they’d suffered a data breach over the past two years, up from 39% in our survey a year earlier. And while certain attack vectors dominated headlines in the last year or two, criminals are still finding success with traditional playbooks:

- 51% report business email compromise, up from 42% a year ago.
- 39% of organizations report insider attacks, up from 27% a year ago.
- 79% say they’ve encountered ransomware attacks, and 35% admit one or more of those attacks led them to lose access to data and systems.

Additionally, 40% of respondents report a regulatory violation (up from 28% a year ago). More and more sophisticated attacks, acute talent shortages and pandemic-specific challenges have SOCs reeling.

- Security teams are falling behind
- Remote workers remain a challenge
- Supply chain worries are front and center
- Ransomware: Playbooks and payoffs
- Security teams reel from talent crisis

It’s not clear whether these numbers are a sobering indication that attackers are significantly more successful today or if, as Splunk Distinguished Security Strategist Ryan Kovar notes, it’s a question of causation versus correlation. Are intruders better at penetrating our defenses, or are security teams better at detecting intruders? The answer is probably “both,” with offense and defense each improving aspects of their game.

> “And ransomware skewers this because they actively tell you that you’re compromised,” Kovar says, “while traditional attackers try to get in and out without being detected.”

Regardless of why security teams are detecting more breaches, they’re having to work a lot harder, and are feeling greater effects than ever before.

All told, 59% of security teams say they had to devote significant time and resources for remediation (up from 42% a year ago). Forty-four percent say they’ve suffered disruption of business processes (versus 35% a year ago), and 44% say they’ve lost confidential data (up from 28% a year ago).

### Methodology
- Researchers surveyed 1,227 security and IT leaders who spend more than half their time on security issues.
- **11 Countries**: Australia, Canada, France, Germany, India, Japan, Netherlands, New Zealand, Singapore, United Kingdom, United States
- **15 Industries**: Aerospace and defense, consumer packaged goods, education, financial services (banking, securities, insurance), government (federal/national, state and local), healthcare, technology, life sciences, manufacturing, media, energy, retail/wholesale, telecom, transportation/logistics, utilities

The costs of these incidents are not theoretical, and they matter to more than the security budget. In addition to lost business, ransoms and reputation loss, downtime is hugely expensive for the entire organization. The majority of respondents (54%) report that business-critical applications suffer unplanned downtime due to a cybersecurity incident on at least a monthly basis, with a median of 12 outages per year.

Moreover, the median time to recover for business-critical workloads suffering from unplanned downtime tied to a cybersecurity incident is 14 hours. We asked respondents to estimate the hourly cost of downtime for business-critical apps, which across the survey sample averaged about $200,000. That told us that the average annual cost of downtime tied to cybersecurity attacks for organizations today is about $33.6 million.

In short, the eternal battle between attackers and defenders has been made worse by rising complexity. Intricately woven hybrid, multicloud environments host modern cloud-native, microservices-based applications alongside legacy technologies, and now everyone needs to be able to access it all from their spare bedroom.

Security teams must gain complete understanding of, and visibility into, their cloud infrastructures to focus on cloud hygiene. They face new challenges around secure configuration, software vulnerabilities, compliance, and the need to maintain an audit trail of access and activity for all of it. At the same time, they need to revisit org-specific threat models based on novel attack chains.

Let’s see how that’s going.

![Chart showing Cyberattacks Cause Frequent Downtime: 21% Weekly or more often, 19% Once every few weeks, 14% Monthly, 16% Once every few months, 11% Once every few quarters, 19% Once per year or less often, 1% Don't know. 54% report at least monthly outages]

### Security teams are falling behind

Fully 64% of respondents say keeping up with security requirements has gotten harder in recent years, up from 49% a year ago. Top reasons include:

- The dangerous threat landscape (say 38% of respondents; down from 48% but still ranked first).
- An overwhelmingly complex security stack (30%, up from 25% and fifth place a year ago).
- Skilled labor recruitment and retention issues (both 29%, both up slightly from last year).

Top challenges for security teams include:

- Over-rotating to focus on compliance over best practices (29%, up from 23% and the fourth most cited response last year).
- Spending too much time addressing emergencies (28%, up from 26% and the second most frequently cited response a year ago).
- Struggling to manage the complexity of security technologies (26%, up from 24% and maintaining its position as the third most cited challenge).
- Dealing with the challenges of being understaffed (26%, up from 22% a year ago and the fifth most cited challenge).

All told, the necessary attention to compliance, too much time on reactive footing, and the challenges of too much complexity and too few people conspire to distract the SOC from focusing on emerging threats.

![Chart showing Why Security Keeps Getting Harder comparing 2022 and 2021 responses]

### Remote workers remain a challenge

The advent of the COVID-19 pandemic in early 2020 created unprecedented challenges for security experts and, as we noted in last year’s report, new levels of collaboration and cooperation among security, IT and business teams. Two years later, many of the challenges remain vexing, perhaps none more than remote work.

Organizations are still supporting, on average, double the number of remote workers compared to pre-pandemic norms. While today’s average, 46% of workforces, is 10 points lower than in 2021, there’s no return to pre-pandemic levels in sight. Organizations expect that 12 months out, 41% of their workers will remain remote. As a result, 90% see a need to adjust security controls and policies.

This shift to more remote work has resulted in operational challenges, including ensuring access to the corporate network (noted by 29% of respondents), making sure devices in use are securely configured (28%) and securing access to cloud assets (27%).

![Infographic showing Remote Work: Yesterday, Today, Tomorrow (21% pre-pandemic, 46% today, 41% projected a year from now)]

While remote work and other pandemic measures have been stressful for IT organizations and business units, security teams have been particularly hard hit: 80% say that the SOC has to continually create and implement new threat detection rules to accommodate remote workers.

Additionally, 65% of organizations have seen a measurable increase in attempted cyberattacks, which is particularly problematic since 78% say remote workers are harder to secure.

As noted above regarding successful breaches, these rising numbers aren’t necessarily caused only by proliferating attacks. Organizations may also be getting better at detecting attacks.

Still, respondents attributed the rise in attacks at least in part to the greater attack surface that widespread remote work presents.

![Chart showing Remote Work, Rising Attacks: 26% Yes, significant increase; 39% Yes, slight increase; 29% No, things about the same; 2% No, significant decrease; 3% No, slight decrease. 65% have seen a measurable increase]

### Supply chain worries are front and center

There has been a lot of buzz around the concept of supply chain attacks since the discovery, in late 2020, of the SolarWinds hacks, followed by the Kaseya attack, log4Shell and others. Our State of Security survey in 2021 was conducted two months after the SolarWinds disclosure, and at that time, only 47% of CISOs had briefed boards or the C-suite on supply chain risks. A year later, the continued buzz has inspired strategic action.

Ninety percent of organizations — nearly everyone — reported that they have increased their focus on third-party risk assessment as a result of those high-profile attacks. In fact, 61% of CISOs are now regularly briefing their boards and/or line of business executives about activity in this space (up from 47% a year ago, just two months after SolarWinds).

New attention to this attack vector has led 97% of organizations in our survey to have taken some kind of action. Most often (33%, up two points year-over-year), respondents have increased their cybersecurity budget. Also of importance is the CISO’s ability to engage business leaders and the board of directors. Fifty-four percent of respondents say that such discussions accelerated actions, and another 38% say these actions wouldn’t have taken place otherwise.

> “All of this is a huge change,” Kovar says. “In my 20 years in IT security, I’ve never seen software supply chain threats reach this level of visibility.”

The change may not be entirely a hype response. Forty percent of survey respondents said that their organization had been affected by a supply chain attack. Kovar says that supply chain attacks will soon change how software is bought and sold.

> “We’re likely to see buyers require an SBOM, a software bill of materials,” he says. “It will list the elements within a complex software package, so that when a supply chain attack is discovered, you can quickly know if your organization is vulnerable.”

### Ransomware: Playbooks and payoffs

If there’s something driving more concern in 2022 than supply chain attacks, it’s probably ransomware (which, as in the Kaseya and log4Shell cases, can come through the supply chain). Last June, in the wake of its executive order on cybersecurity, the Biden Administration issued a memo specifically on ransomware. Beyond concern, organizations are taking action: 84% of organizations surveyed have developed a formal ransomware playbook — a list of required steps for responding to a ransomware attack. But to date it’s been a reactive response; of organizations that suffered a successful ransomware attack, 71% only developed a playbook after they had been successfully attacked.

The top response to ransomware: Pay up. Among respondents who fell victim to a successful ransomware attack, only 33% avoided the ransom by restoring from backup. About 66% reported that the criminals were paid, either by the organization (in 39% of cases) or their insurance company (27%). Asked how much the largest ransom paid to attackers was, the average response was about US$347,000.

It’s worth noting that those who have not been successfully hijacked have more swagger. Among respondents who had not fallen victim, only 42% reported that their organization is likely to pay off the attackers.

> “That may be a case of overconfidence in remediation plans,” Kovar says. “Once their disaster recovery or backup capability is put to the test, many orgs might discover that it’s not as easy as they thought.”

Apart from better response planning, security leaders are putting their faith in data: 88% agreed that better capture and analysis of detection data is one of their most effective tools for preventing successful ransomware attacks.

![Chart showing Most Orgs Were Ransomware Targets: 20% Data and systems held hostage, 44% Detected and remediated before losing access, 15% Both are true, 21% Not a target, 1% Don't know]

### Security teams reel from talent crisis

Security talent is always scarce. But this year, security leaders are facing an especially daunting labor shortage.

Fully 87% of respondents report skills or staffing challenges; 53% say they can’t hire enough staff and 58% cite an inability to find talent with the right skills. Again, a perennial issue, but these trends are heading in the wrong direction: 85% say it has gotten harder to recruit and retain talent over the past 12 months — during which the so-called “Great Resignation” played out across industries.

The ongoing talent challenges have led to a number of issues:

- 70% say that the resulting increase in their workload has led them to consider looking for a new role.
- 76% say team members have been forced to take on responsibilities they aren’t ready for.
- 68% report that talent shortages directly led to the failure of one or more projects/initiatives.
- 73% say that workers have resigned, citing burnout.

That last stat is especially troubling. If resignations lead to more resignations, the talent crisis becomes self-perpetuating.

---

## The State of Cloud: Business-Critical Baseline

Across the board, the still-growing role of cloud computing has become essential to organizations. About 73% use multiple public clouds today, and when compared to a year ago, we see multicloud realities have continued to expand: 34% use three or more public cloud service providers (up from 29% a year ago). The trend will continue: 56% expect they will use three or more public cloud service providers (IaaS and PaaS) 24 months from now.

And those secondary clouds aren’t secondary. Sixty-five percent of multicloud users report meaningful utilization across clouds; only 35% say that their secondary clouds are minor/niche.

Cloud-hosted applications are now performing business-critical functions across lines of business; 66% of respondents say the majority of their business-critical apps are cloud-hosted, up from 41% a year ago.

- 39% of organizations have a cloud-first policy.
- 41% say they weigh cloud and on-premises options equally before making decisions.
- Only 20% of organizations still have an on-premises-first approach.

### Cloud hampers security visibility

Though the migration to cloud has been a steady story for years, it greatly accelerated with the COVID-19 pandemic. Security teams find the resulting complexity daunting. The growing criticality of cloud puts pressure on security leaders to understand the cloud. More than three-quarters of respondents (79%) say their CISO is under pressure to demonstrate increased cloud fluency.

Two cloud-native security challenges continue to stand out:

- Maintaining consistency across data centers and cloud (45%, down from 50% but still the top cloud security challenge)
- Use of multiple security controls leads to cost and complexity (37%, down from 42% but still the No. 2 response)

It would seem that one problem begets the other: More point tools create more silos and potential blind spots, which may spur the adoption of more narrowly focused tools.

In terms of cloud security visibility areas in need of improvement, the top two responses were also leaders last year. A notable change is that the no. 3 response, maintaining a clear audit trail of account activity, rose from the fifth most common spot last year to no. 3 in 2022.

As with talent shortages leading to burnout leading to attrition, cloud complexity has a self-perpetuating aspect: The complexity of infrastructure elements leads to a crazy quilt of multiple point tools. The resulting silos further hamper visibility and exacerbate operational cost challenges.

> “Security teams generally seem to just be figuring out the scope of their cloud challenges,” says Ryan Kovar. “Three years ago, I was hearing, ‘Wait, I have to monitor the cloud?’ now it’s, ‘Of course I have to monitor the cloud. But how?’ That’s what I think of in terms of increasing organizations’ cloud fluency.”

![Chart showing Most Important Ways to Improve Cloud Visibility]

---

## Responding to Rising Challenges

Having taken measure of the multifarious challenges of modern IT security, we turn our attention to solutions, to the technologies and techniques that organizations worldwide are using to keep up with — and maybe get ahead of — the bad guys.

### Talent solutions

Asked to pick strategies that will overcome the talent crisis, our respondents picked a combination of tools and training.

- 58% selected “increase funding for training” from a list of options.
- 52% picked “increase use of cybersecurity tools with AI/ML.”

Additional strategies included:

- Better capture and analysis of security data: 47%
- Simplifying security tool portfolio (vendor rationalization or platform-based controls): 45%
- Increasing use of MSSPs/outsourcers: 41%
- Increasing investment in commercial security controls: 41%

Of course, those two strategies are not mutually exclusive, and pretty much everyone is embracing automated tools powered by AI/ML: 80% agree that at some point in the next three years, the majority of security operations center activities (e.g., threat detection, investigation and response) at their organizations will be automated with little human oversight.

That’s not to say that you can automate your way out of a talent crunch, and many organizations are trying new approaches. One of the more difficult cybersecurity roles to find are cloud security architects and cloud security engineers. The Venn diagram of cybersecurity skills and cloud computing knowledge just doesn’t have enough overlap. In response, many organizations are asking their developers to codify security processes so that they are reusable and repeatable across project teams.

> “Automation can help, if you’re careful that you’re not just giving people more tools to monitor,” says Splunk Distinguished Security Strategist Ryan Kovar. “And on the recruitment front, we have to start considering alternative talent pools because there will never be enough security talent as it’s traditionally defined.”

#### The talent shortage, in brief:
- 30% of security leaders say they can’t hire enough staff to handle the workload.
- 35% say they can’t find staff with the right skills.
- 23% say both factors are a problem.
- A lucky 13% say they suffer neither challenge.

### Analytics and automation are increasingly essential

Analytics and automation capabilities let security analysts work smarter and respond to threats at machine speed. Eighty-two percent of respondents say their CISO is under pressure to increase their data analysis capabilities. Fully 85% (up from 82% last year) say that security analytics plays a bigger role in their overall cybersecurity strategy and decision-making today than it did two years ago.

Organizations’ strong investment in analytics, automation and SOAR (security orchestration, automation and response) technologies continues:

- 67% of organizations are actively investing in technologies designed for security analytics and operations automation and orchestration.
- Of those, 35% report that their organization uses or will use the automation and orchestration capabilities built into their security information and event management (SIEM).

The embrace of automation and analytics tools correlates with DevSecOps trends; 35% of respondents report that their organization has built or will build security rules using DevOps tools for automation and orchestration (the most frequently cited approach).

77% of organizations have integrated non-security analytics solutions (for business, IT operations, risk management) with cybersecurity-specific analytics to support decision-making.

Analytics and automation technologies are not only more prevalent in SOCs worldwide, they’re increasingly sophisticated. Now 63% of organizations (up from 54% a year ago) have deployed machine learning technologies for security analytics. Most often organizations look to ML-based technologies to improve threat detection (37%), get more scale from junior analysts (31%) and to automate remediation (30%).

The top priorities for incident response automation were to:

- Integrate security tools with IT operations systems: 29%
- Improve security/ITOps collaboration: 28%
- Provide capabilities for “hunting” activities: 28%
- Automate basic remediation tasks: 26%
- Integrate external threat intel with internal security data analysis: 26%
- Collect and centralize data from various security tools: 24%

![Chart showing Most Orgs Bet on SOAR]

### The shift toward DevSecOps

DevSecOps has increasing mainstream appeal to help security scale alongside pressures to drive faster development and deployment of applications. Fully 80% of respondents say their CISOs are under pressure to develop their DevSecOps skill sets.

For our research, we defined DevSecOps as “a collaborative software engineering, operations and cybersecurity practice of incorporating the cybersecurity measures and controls at each phase of the CI/CD [continuous integration and delivery/deployment] process.” Not that we needed to tell them — 75% of organizations say they use DevSecOps today.

Roughly three-fifths report that DevSecOps entails automating security workflows such as:

- Identifying and remediating software vulnerabilities prior to production (62%)
- Identifying and remediating malware prior to production (64%)
- Applying runtime API security controls (61%)
- Logging code changes for audit (59%)

Though the general DevSecOps principle of baking security into the beginning of the development process, rather than as a late-stage gating factor, is well understood, we asked respondents why they’ve adopted the DevSecOps approach. The leading drivers:

1. To allow cybersecurity to keep pace with fast-moving development teams (46%)
2. To establish a more proactive security posture (43%)
3. To gain greater operational efficiencies via automation (41%)
4. To better secure cloud-resident data (41%)
5. To foster collaboration between our cybersecurity, development and operations teams (39%)

But does it work? Yes. Seventy percent of DevSecOps adopters report an improvement in the cybersecurity team’s ability to keep pace with development teams; 70% report a more proactive posture; and 69% report an improvement in their ability to secure cloud-hosted data.

![Chart showing DevSecOps Is Mainstream]

---

## The Path Forward

While the challenges continue to increase, our research shows that organizations are taking smart steps to keep up — and maybe even get ahead — of the ever-shifting threat landscape.

Pressure is a key theme coming out of this 2022 research. Criminal and nation-state adversaries maintain pressure through attacks of increasing volume, variety and sophistication. And as business leaders better recognize the intensity of the cybersecurity landscape, and the existential stakes, they demand more of security leaders. Fortunately, there’s also a degree of willingness to pay for it.

Nearly every organization we surveyed — 93% — expect to increase spending on security over the next 12-24 months (up from an already impressive 88% a year ago). Increasing training for cybersecurity and IT operations staff is still the leading area of focus (cited by 26% of respondents).

![Chart showing Immediate Security Priorities]

---

## Key Recommendations

There’s more attention on security concerns, from the board of directors on down. There’s more pressure on security teams, from the CISO on down. And for many organizations, there’s more funding, but does anyone ever think it’s enough?

In a world suffering ever-rising threats of ransomware, supply chain attacks and staff burnout, to say nothing of the constant threats of insider attacks and social engineering — here is the advice that emerges from this global survey.

### 1. Seek talent, teach skills.
Organizations are already telling us that they’re prioritizing efforts to find, train and retain talent. All the traditional efforts in that sphere are important, and recommended. But they’re not enough. The field of security analysts is just too small to ever meet the demand, which is why Ryan Kovar focuses on “talent” in its original meaning, not just as a euphemism for “workers.”

> “You’re never going to fill the gaps with the traditional security workforce,” he says. “We have to consider alternative candidate pools.”

That can include people with experience in non-security IT roles, but Kovar says he looks even further afield. “We need raw talent, not trained skills,” he says. “I’ve had a lot of luck recruiting people with journalism, HR and creative backgrounds. I just need people with innate curiosity and a talent for synthesizing and understanding data.”

People with a degree in the humanities, he has found, can be phenomenal at that — often better than those with traditional computer science degrees.

> “I can teach the security analyst role to someone who can synthesize data and communicate it more easily than I can teach someone who just knows how to code in C++.”

### 2. Know your cloud.
Nearly eight in 10 respondents told us that CISOs are under pressure to increase their cloud fluency. A significant number also expressed confusion over where security responsibilities between their teams and their cloud providers connect. Everyone from senior security leadership to tier one security analysts needs to understand their hybrid, multicloud environment.

Organizations must dedicate time and training to understand the complex interplay of their public, private and SaaS solutions. They need the tools and training to securely configure various environments, to manage access and authentication, and to minimize MTTD and MTTR (mean times to detect and recover).

### 3. Build an SBOM.
We mean really know your cloud. And all your software. Every software organization should maintain — as in, keep relentlessly current — a software bill of materials that lists all software components running in production via software composition analysis (SCA).

> “A lot of organizations don’t do this yet,” Kovar notes. “Thanks to the attention to supply chain attacks, customers are going to begin demanding SBOMs from their vendors, and it will quickly become standard.”

### 4. Use automation to enhance human analysts.
If we’re never going to have enough humans on the team, the solution is to just automate everything, right? Kovar warns that automation can create as many human headaches as it solves.

> “Analysts being overwhelmed, and then burned out, is a difficult challenge, and in one sense, automation can make it worse,” he says. “The more disparate tools you give someone, the more things they have to do, the more they have to keep up with. That doesn’t necessarily help with burnout.”

So automate with the intention of liberating your human analysts to do their job better. That can mean fewer tools, not more.

### 5. Take DevSecOps forward.
To the 23% of respondents who haven’t gotten around to DevSecOps yet, we say, “Don’t delay.” To the 2% who aren’t even thinking about it, we really urge you to do some reading on the topic. For the vast majority who are already making strides: Keep going.

The next step, Kovar says, is to apply DevSecOps specifically to defending against ransomware and advanced persistent threats.

### 6. Consolidate sprawling tool sets.
You need the right tool for the right job, as pretty much everyone’s grandfather would say. But a piece of software isn’t just a tool waiting in a box. It’s an active application that requires monitoring to be effective.

Consolidation is about having the right tools for the right jobs, while also making sure that your team can manage the responsibility of care.

---

## Appendix

### Industry highlights
Standout data points from seven select industries worldwide.

- **Communications and media**: Suffer from more frequent downtime (33% weekly outages vs 22% average). 46% attribute project failures to skills gaps. CISOs have outsized impact on supply-chain focus. Diversified cloud usage.
- **Financial services**: Tend to have larger SOCs (27% report >50 FTEs vs 16% average). Less likely to report daily attacks keep them from refining tools. Take a cloud-friendly tack (50% cloud-first policy). Ahead in DevSecOps adoption (84%).
- **Healthcare and life sciences**: More cloud reliant (81% run important apps on cloud vs 64%). Higher difficulty keeping up with security requirements (46% vs 25%). Higher reporting of data breaches (58% vs 37%).
- **Manufacturing**: Smaller SOCs (8% report >50 FTEs vs 20%). Fewer incidents/attacks reported recently. More reactive approach to software supply chain attacks.
- **Public sector (Education and government agencies)**: Lower expected increase in cybersecurity investments. Analytics catching on more slowly. DevSecOps has less momentum (24% extensive adoption). More cloud reticence (45% critical apps in public cloud).
- **Retail**: Embrace cloud (50% cloud-first policy). Higher understanding of security responsibility models (31% vs 21%). More likely to pay off ransomware (51%). Smaller SOCs (8% report >50 FTEs).
- **Technology**: Larger SOCs (28% report >50 FTEs). Lead on multicloud adoption (42% partner with 3+ providers). Seen more malicious activity. More apt to see promise of data to bridge skill gaps.

### Country highlights
Standout data points from 10 countries worldwide.

- **Australia and New Zealand**: Fewer attacks reported in previous 24 months. Experience longer downtime. Lower uptick in difficulty and stress. Less bullish on AI/ML automation.
- **Canada**: Slower rate of increased investment in cybersecurity. Less extreme pressure on CISO for data analytics. Less far along on security analytics. Higher average remote workers (56%).
- **France**: Lower current cloud infrastructure reliance (41%). Greater resilience to downtime. Expect slower multicloud adoption.
- **Germany**: Higher cloud-first policy alongside on-prem-first policies. Greater struggles with project delays from talent shortages. Betting on automation to solve talent crisis.
- **India**: Lower remote workers percentage (33%). Significant uptick in attempted attacks on remote workers. Aggressive integration of non-security analytics. Leading edge in machine learning security controls. Expected high investment increases (90%).
- **Japan**: Less reliant on cloud infrastructure (53%). Report issues keeping up with new devices and alerts lacking context. Fewer security incidents experienced. More conservative DevSecOps adoption (22%).
- **Singapore**: More tentative approach to the cloud (22% cloud-first). Fewer cybersecurity incidents faced recently. Greater resilience in downtime. Severe cybersecurity skills shortages.
- **United Kingdom**: Labor market challenges do not result in as many project failures. Supply chain attacks made smaller impressions. Less reliance on cloud infrastructure (57%).
- **United States**: 63% expect to use 3+ public cloud providers. More sophisticated security controls. Suffer from more alert fatigue (30%). See more promise for machine-learning-backed security analytics.

---

Learn how Slack, REI, Aflac, Nasdaq and others use Splunk’s data-centric security operations platform to deliver accurate threat detection, investigation and automated response across cloud, on-premises and hybrid environments.

[Learn More]

Splunk, Splunk> and Turn Data Into Doing are trademarks and registered trademarks of Splunk Inc. in the United States and other countries. All other brand names, product names or trademarks belong to their respective owners. © 2022 Splunk Inc. All rights reserved.

22-22513-Splunk-State of Security-EB-108

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-16", "model": "gemini-3.5-flash-lite"} -->
