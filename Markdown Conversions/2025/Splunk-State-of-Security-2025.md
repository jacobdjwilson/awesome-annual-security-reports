# State of Security 2025

![Report Cover: State of Security 2025 - The stronger, smarter SOC of the future](image-of-report-cover)

## Table of Contents
- [Executive foreword](#executive-foreword)
- [Introduction: Transforming the SOC from overwhelmed to optimized](#introduction-transforming-the-soc-from-overwhelmed-to-optimized)
- [Chapter 1: Efficiency in the SOC is elusive](#chapter-1-efficiency-in-the-soc-is-elusive)
  - [Busywork stifles progress and passion](#busywork-stifles-progress-and-passion)
  - [Alert overload slows down SOCs](#alert-overload-slows-down-socs)
  - [Data deficits derail investigations](#data-deficits-derail-investigations)
- [Chapter 2: AI leads SOCs into the future](#chapter-2-ai-leads-socs-into-the-future)
  - [Building trust in AI](#building-trust-in-ai)
  - [Distrust of AI lingers in the SOC](#distrust-of-ai-lingers-in-the-soc)
  - [Tapping into the power of generative AI](#tapping-into-the-power-of-generative-ai)
- [Chapter 3: Skills to power the future SOC](#chapter-3-skills-to-power-the-future-soc)
  - [Skills that drive resilience are biggest shortcomings](#skills-that-drive-resilience-are-biggest-shortcomings)
  - [Today’s biggest skills gaps are also the most important for the future](#todays-biggest-skills-gaps-are-also-the-most-important-for-the-future)
  - [Automating the mundane to find reprieve](#automating-the-mundane-to-find-reprieve)
- [Chapter 4: The new era of threat detection](#chapter-4-the-new-era-of-threat-detection)
  - [Data complexity creates new detection dilemmas](#data-complexity-creates-new-detection-dilemmas)
  - [Detection as code unlocks a flexible future](#detection-as-code-unlocks-a-flexible-future)
  - [Popular threats pack a punch](#popular-threats-pack-a-punch)
- [Chapter 5: Unifying and connecting the SOC](#chapter-5-unifying-and-connecting-the-soc)
  - [Everything in its right place](#everything-in-its-right-place)
  - [Data sharing accelerates operations](#data-sharing-accelerates-operations)
  - [A more collaborative SOC is coming](#a-more-collaborative-soc-is-coming)
- [Words to the wise](#words-to-the-wise)
- [How to propel your SOC into the future](#how-to-propel-your-soc-into-the-future)
  - [1. Spring clean your toolset](#1-spring-clean-your-toolset)
  - [2. Adapt your team’s skillsets for the future](#2-adapt-your-teams-skillsets-for-the-future)
  - [3. Lighten the load of alerts](#3-lighten-the-load-of-alerts)
  - [4. Opt for domain-specific generative AI](#4-opt-for-domain-specific-generative-ai)
  - [5. Set the groundwork for collaboration](#5-set-the-groundwork-for-collaboration)
  - [6. Make detection as code a team sport](#6-make-detection-as-code-a-team-sport)
- [Step into the SOC of the future with Splunk](#step-into-the-soc-of-the-future-with-splunk)
- [Industry highlights](#industry-highlights)
  - [Communications and media](#communications-and-media)
  - [Financial services](#financial-services)
  - [Public sector](#public-sector)
  - [Manufacturing](#manufacturing)
- [Country highlights](#country-highlights)
  - [Australia and New Zealand](#australia-and-new-zealand)
  - [France](#france)
  - [Germany](#germany)
  - [India](#india)
  - [Japan](#japan)
  - [Singapore](#singapore)
  - [U.K.](#uk)
  - [U.S.](#us)
- [Methodology](#methodology)
- [About Splunk](#about-splunk)

---

## Executive foreword

Building an effective SOC is one of the greatest lessons in adaptability. As a former SOC leader, I’ve built security operations ranging from the Department of Homeland Security to managed security services for small- and medium-sized businesses. No matter the size or mission, the lesson is always the same: If you’re not thinking ahead, you’re already behind.

Many of us, myself included, are drawn to cybersecurity because it’s so dynamic. Cybersecurity has always been a game of rapid shifts — new threats, new malware, and now, the breakneck pace of AI. But for all the external challenges, the real problem is often internal.

We surveyed 2,058 security leaders — including SOC managers, directors, analysts, and engineers — to understand the biggest barriers to evolving the SOC and the most impactful strategies for the future.

Our data uncovers that SOCs are burning too much effort on the wrong things — babysitting tools, chasing the same false alarms over and over, and wrestling with messy data. Nearly half of them admit they spend more time maintaining their tech stack than actually defending their organization. That’s not just frustrating — it’s a failure of strategy.

But the survey also reveals that some SOCs are embracing new forward-leaning technologies and processes to help eliminate these inefficiencies. They’re leaning on AI to boost productivity, uplevel their existing teams, and become more resilient. They’re exploring detection-as-code to stay ahead of attackers. They’re rethinking their approach to investigation and response, ditching silos for a unified strategy.

We hope that State of Security 2025: The smarter, stronger SOC of the future will help propel your SOC. Because if you’re still fighting yesterday’s battles, you’ve already lost.

**David Dalling**

GVP, Global Cyber Strategist, Splunk

State of Security 2025 | Splunk

## Introduction: Transforming the SOC from overwhelmed to optimized

Think of the biggest threats to the SOC. Industry stereotypes might lead you to picture a hacker in a hoodie, enveloped in shadows as they type prompts into a command line. Or perhaps a team of highly skilled and credentialed nation-state actors poring over top-secret threat intel in a windowless, undisclosed government office.

Imagining these threat actors can fuel any SOC member’s drive to defend. No doubt, these are all very real threats. But what’s often overlooked is internal — the threat of inefficiency. Analysts play an endless game of Whac-A-Mole™, missing critical incidents that end up as costly breaches. Teams spend more time maintaining tools than defending the organization. Faulty data leads to faulty detections, weakening cyber defenses. And persistent skills gaps continue to stretch existing teams thin.

Teams will reach a crossroads as toolsets expand, the skills gap widens, and technologies like AI become more central to the SOC. Will security tools pile up, creating even more complexity? Will collaboration across the business become second nature to SOC teams, or will they remain in their comfort zone?

It’s time to reimagine the SOC and what it could be. SOC teams of the future will elevate their skills by relying on AI and automation. As a result, analysts will spend their time building stronger defense methods like detection as code (DaC) and perfecting their investigation protocols. They’ll take a smarter, unified approach to threat detection and response, leading to tighter collaboration and bringing more context and speed to investigations.

Does this sound like sci-fi? Believe it or not, some teams are already taking steps to build a faster, stronger, and smarter SOC. These SOCs have evolved from overloaded to optimized and resilient.

Launching into the future is an exhilarating adventure, but it’s worth the ride.

State of Security 2025 | Splunk

## Chapter 1: Efficiency in the SOC is elusive

> The future SOC is extremely streamlined. Analysts will be freed from mundane, repetitive tasks, so they can apply their expertise where it truly matters: defending the organization.
>
> — Michael Fanning, CISO, Splunk

State of Security 2025 | Splunk

If you’ve spent time in the security weeds, you know the nuisance of troubleshooting with no clear resolution, the hassle of reconfiguring a setting for the tenth time, or the drudgery of managing inventory.

The SOC of the future, on the other hand, will run much more efficiently. Tools are well-orchestrated and generate alerts rich with context. Every team member performs strategic tasks typically reserved for senior analysts, like in-depth analysis and investigations. They also lean on automation and AI to resolve lower-level alerts.

![Infographic showing top sources of inefficiency in the SOC](image-of-top-sources-of-inefficiency-in-the-soc)

The top sources of inefficiency in the SOC

- **59%** We spend too much time and/or effort maintaining tools and associated workflows
- **51%** Our tools do not integrate well with one another
- **47%** We face alerting issues
- **32%** Our team does not have the requisite skills
- **31%** We have inadequate and/or outdated processes
- **28%** We spend too much time normalizing data
- **27%** Managing the number of vendors is complex
- **24%** We lack an established incident response process

State of Security 2025 | Splunk

### Busywork stifles progress and passion

What’s holding teams back from achieving a high level of efficiency? Tool maintenance, for one. Nearly half (46%) of respondents say they spend more time doing busywork — like configuring and troubleshooting tools — than addressing critical efforts like threat investigation and mitigation.

Don’t get us wrong; tool maintenance has its place in the SOC. It can optimize workflows and improve accuracy. But respondents point to the imbalance as a growing problem, with 59% saying that it’s the main source of inefficiency for their teams, followed closely by tools not integrating well together (51%).

“Maintenance is more complicated than it used to be,” says Marcus LaFerrera, director of SURGe at Splunk. “Tools are more feature-rich with more frequent updates. And while vendors have introduced support to cut down on the guesswork, there’s far more network complexity that makes the job harder.”

Passion and purpose motivate security professionals in their mission to keep organizations safe. But no one gets jazzed about tool maintenance. A team that spends the majority of its time defending is a team that maximizes the passions of its analysts. These SOCs enable the business by being strategic, innovative, and proactive.

**46%** spend more time maintaining tools than defending threats

> Analysts who can flex their critical thinking muscles rather than say, endlessly adjusting alert thresholds, aren’t simply more satisfied — they’re doing more valuable work and contributing to the organization’s bottom line.
>
> — Kirsty Paine, Field CTO and Strategic Advisor, EMEA, Splunk

State of Security 2025 | Splunk

> You want to bring your analytics to your data, not the other way around. SOC teams that recognize this and have strategies involving data federation are already a step ahead.
>
> — Kirsty Paine, Field CTO and Strategic Advisor, EMEA, Splunk

### Alert overload slows down SOCs

Every second counts in the SOC, especially during a major investigation. Inefficiencies aren’t minor headaches. Even a small bottleneck — like a missed alert that results in a data breach — can cause significant reputational, legal, or financial consequences. Downtime is just one example, and it can cost organizations $540,000 per hour, according to The Hidden Costs of Downtime report.

Alerts are another “can’t live with them, can’t live without them” part of the job for analysts, with 47% pointing to alerting issues as the most common source of inefficiency in the SOC. Respondents said most troublesome issues were having too many alerts (59%), dealing with too many false positives (55%), and deciphering alerts that lack context (46%). Each of these issues waste analysts’ precious time as they question alert validity or ignore them altogether. And who can blame them? After investigating a string of alerts that turn out to be false positives, what’s the motivation for investigating the next one?

**59%** have too many alerts

### Data deficits derail investigations

Wasted time extends beyond just tool management and alert overload. Data problems also play a significant role. In fact, 57% of respondents report losing valuable time during investigations due to gaps in their data management strategies.

Whether those gaps are attributed to accessibility concerns (39%) or data silos (35%) — both common data challenges flagged by respondents — not being able to access the right data in the right place makes it even harder for SOC teams to act quickly and decisively when facing threats.

“You want to bring your analytics to your data, not the other way around,” says Paine. “SOC teams that recognize this and have strategies involving data federation are already a step ahead.”

**57%** have lost valuable investigation time due to data management gaps

State of Security 2025 | Splunk

## Chapter 2: AI leads SOCs into the future

> In the future, AI will become an integral part of the security analyst experience. AI can enable self-healing systems to detect and mitigate malicious behavior in real time. Imagine what that technology could do once it’s embedded in the SOC.
>
> — Tamara Chacon, Security Strategist, Splunk SURGe

State of Security 2025 | Splunk

Peanut butter and jelly. Thunder and lightning. AI and the future. Some pairings simply make sense.

AI is already a powerful tool for both adversaries and defenders. In the SOC of the future, analysts will learn to wield AI to their advantage, applying it to the right tasks at the right time. No magic AI pixie dust needed.

AI isn’t a cure-all, but it’s certainly an appealing remedy for teams seeking more efficiency. Let AI search through endless rows of logs for a specific IP address? We’d be hard-pressed to find any SOC team not on board with that.

Applying AI to security workflows was this year’s highest cybersecurity priority, with 56% listing it as one of their top three initiatives. Productivity gains are real for those who’ve jumped in; 59% say they’ve moderately or significantly boosted their efficiency with AI.

### Building trust in AI

Security pros are notoriously skeptical. It’s sort of their job. But trust comes in different shades — from blind faith to complete cynicism and everything in between. Successfully adopting AI is all about balance — trusting it enough to reap the benefits while staying cautious enough to put the right checks and safeguards in place.

Only about 11% of respondents say they trust AI completely to perform mission-critical activities within the SOC. But it’s unlikely that this group is blindly trusting AI; rather, they may be running their own models and are more easily able to trust a system they’ve built themselves.

“Trust will grow as organizations mature in their AI implementations,” says Petra Jenner, senior vice president and general manager for EMEA at Splunk. “Teams with the resources to build, train, and test their own models will naturally have a higher level of trust in that system.”

However, the majority of respondents (61%) say they somewhat trust AI for mission-critical operations. Security teams need some trust to successfully adopt AI in the SOC, but taking a human-in-the-loop approach is paramount — especially when it comes to generative AI.

“Generative AI is like that overconfident colleague who will never say they don’t know, and will assuredly tell you about something they read about once,” says Paine. “Expert checking and proper tests will make sure you’re getting the right outputs.”

> Trust will grow as organizations mature in their AI implementations. Teams with the resources to build, train, and test their own models will naturally have a higher level of trust in that system.
>
> — Petra Jenner, Senior Vice President and General Manager, EMEA, Splunk

**59%** have moderately or significantly boosted their efficiency with AI

State of Security 2025 | Splunk

### Distrust of AI lingers in the SOC

![Bar chart showing extent of trust in AI for mission-critical activities](image-of-ai-trust-levels)

AI in the SOC is a reality, but the extent of trust varies when it comes to mission-critical activities

- **11%** Trust completely
- **61%** Trust somewhat
- **26%** Distrust somewhat
- **2%** Distrust completely

State of Security 2025 | Splunk

### Tapping into the power of generative AI

Reaping the benefits of generative AI involves leaning on its biggest superpower: filling in the blanks. For example, it can create search query strings and suggest investigative steps based on what it’s seen before. Nearly a third (31%) currently use generative AI to query security tasks in the SOC, and another 48% say they will do so in the near future.

General AI tools like ChatGPT or Google Gemini are trained on broad datasets, so they have some knowledge on just about everything — from obscure dog breeds to the military history of ancient Rome. But using these tools for threat detection and response is like trying to build a house with a Swiss Army knife — a highly technical field demands a specialized approach.

Other security tasks require a bit more finesse. Respondents were more likely to be wary of generative AI developing security content, such as scripts and signatures, with 29% saying that it should never or will never perform these duties.

Domain-specific generative AI tools can help build trust with embedded intelligence about cybersecurity use cases, surfacing the right information at the right time with context. This is the future of generative AI, and respondents are enthusiastic about its role in cybersecurity. Nearly two thirds (63%) agree that it extremely or significantly enhances security operations compared to publicly available tools.

Domain-specific generative AI, on the other hand, is trained on datasets that focus on a particular subject, like cybersecurity. With this deep knowledge it can make more expert recommendations. It also reduces the risk of data leakage by keeping the workflows in-house. Keeping data from unauthorized access is a top priority for security pros, as nearly half (46%) cite data loss prevention as one of their top three priorities they’ll focus on over the next year.

“Domain-specific AI will simply have better outputs because it’s dialed into a specific function,” says Hao Yang, VP of AI at Splunk. “It’s the next chapter of AI.”

> Domain-specific AI will simply have better outputs because it’s dialed into a specific function. It’s the next chapter of AI.
>
> — Hao Yang, VP of AI, Splunk

**63%** say domain-specific AI significantly or extremely enhances security operations compared to publicly available tools

State of Security 2025 | Splunk

## Chapter 3: Skills to power the future SOC

> Cybersecurity is far from stagnant. The SOC teams that thrive will be the ones that quickly adapt and harness emerging skills and technology.
>
> — David Dalling, GVP, Global Cyber Strategy, Splunk

State of Security 2025 | Splunk

Tomorrow’s SOC may be a well-oiled machine, but that doesn’t mean it relies only on technology. It’s home to some pretty major decisions. Kick off your breach communications immediately after an incident, or wait to understand the full scope? Protect customer-facing services first, or internal infrastructure that supports the core business?

None of these are simple choices, and they’ll only become more nuanced. Regulations deepen. Attackers hone their techniques. New technologies emerge. That’s why people (and their skillsets) will always be at the cornerstone of the SOC — to be decisive and analytical as they navigate these situations.

### Skills that drive resilience are biggest shortcomings

Being understaffed and underskilled are serious dilemmas for security teams. Nearly half (49%) call this the biggest cybersecurity challenge in their organization. What’s more, when we asked respondents to rank the most vital skills for building a resilient SOC and then about proficiency of those skills, we found glaring gaps. Respondents say detection engineering, DevSecOps, and compliance management are simultaneously the most crucial for the future and their weakest capabilities.

**49%** say being understaffed and underskilled is the biggest cybersecurity challenge in their organization

State of Security 2025 | Splunk

### Today’s biggest skills gaps are also the most important for the future

![Bar chart comparing current skills gap experienced vs. top skill needed for a resilient future SOC](image-of-skills-gap-vs-future-needs)

Skill | Current skills gap experienced* | Top skill needed for a resilient future SOC**
--- | --- | ---
Detection engineering | 41% | 74%
DevSecOps | 36% | 74%
Compliance management | 46% | 60%
Analytical investigation of incidents | 30% | 55%
Threat hunting | 28% | 20%
Prompt engineering | 18% | 4%

* Respondents could select all that apply
** Top 3 rankings combined

State of Security 2025 | Splunk

These three in-demand skills paint a picture of what the future SOC will look like.

1.  **Detection engineering**

    Respondents rated detection engineering as the most important skill for building the future SOC, with nearly three-quarters (74%) ranking it in the top three. Forty-one percent report a proficiency gap in this area.

    Detection engineers set the bar for the quality and accuracy of an organization’s detections. They design, build, and fine-tune detections so their organizations can better identify sophisticated threats. They’re also responsible for adopting detection as code (we’ll get to that later) to update this content quickly based on real-time performance indicators.

    Fast and accurate detections will be even more vital in the future as threat actors continue to advance their tactics. Nailing down a detection strategy will also address some other pressing concerns for SOC teams, like reducing false positives, minimizing time on tweaking thresholds, and easing maintenance as the SOC scales.

2.  **DevSecOps**

    DevSecOps closely followed detection engineering as a high-priority capability. Yet over half (53%) report their teams aren’t up to speed in this area.

    An evolution of DevOps methodology, DevSecOps involves baking security into the software development lifecycle (SDLC) early and often. It’s a practice that arguably should be the standard as every business becomes even more tied to software — and organizations that embrace a DevSecOps culture will be more apt to uphold that standard.

    “The future of the SOC comes down to streamlining and making it less onerous to perform maintenance and deployment,” says LaFerrera. “DevSecOps is a part of that evolution.”

3.  **Compliance management**

    Sixty percent of respondents rate compliance management as a top three skill, yet 46% say they fall short here. That’s no surprise — the speed at which regulatory requirements change and assets multiply challenge security teams to keep pace. In fact, over half (52%) of respondents failed compliance mandates because they couldn’t see data about their assets. The implementation side of compliance management — the ‘box checking’ tasks like patching — also requires heavy maintenance, an area in which security teams are already drowning.

The demand for these three skills suggest that critical thinking, collaboration, and creativity — qualities that are unique to people rather than tech — will never go out of style. DevSecOps and compliance management require tight collaboration with other departments, from IT and engineering to legal. Detection engineering leans on creativity to get in the mindset of an attacker, and to build custom detections to the organization’s specific environment.

“You can’t tool your way out of detection engineering. It requires a very specific skillset that isn’t easily cultivated,” says Tamara Chacon, security strategist at Splunk’s SURGe security team research.

> The future of the SOC comes down to streamlining and making it less onerous to perform maintenance and deployment. DevSecOps is a part of that evolution.
>
> — Marcus LaFerrera, Director of SURGe, Splunk

State of Security 2025 | Splunk

### Automating the mundane to find reprieve

By their nature, high-pressure roles in the SOC are stressful, but there are more factors that test security pros’ mental health. For one, the skills gaps that SOC teams have been battling for years are taking a toll. Over half (52%) say their team is overworked and 42% say they’re understaffed. So it’s no surprise that 52% say stress on the job has prompted them to think about leaving the cybersecurity industry altogether.

Job-related stress is a historical trend that’s likely to continue, but there are more solutions ahead. Some organizations will take traditional paths, such as hiring and upskilling current employees (44% plan to fill gaps this way) or enlisting third-party partners (19%). But a considerable number are focusing forward — about a third (33%) plan to resolve these deficiencies with AI and automation.

Don’t panic — this doesn’t necessarily mean jobs in the SOC will be automated away (or at least the parts of the job your teams actually enjoy). Addressing skills shortages could take the form of an automated response to non-critical alerts (forget the days of chasing down “malicious IPs” only to find a user torrenting The Sopranos).

Threat analysis is an area that’s ripe with opportunity here, with 38% of respondents saying it’s their top priority for future automation implementations.

“Automated security tools can take phishing emails, run them against threat feeds, use these results to create a score, and use that score to either quarantine, block, or report the email,” says Paine. “They can work faster than any human.”

**42%** The team is understaffed

![Bar chart showing top staffing challenges for SOC teams](image-of-soc-staffing-challenges)

SOC teams are getting squeezed

Respondents reveal the top staffing challenges

- **43%** The team faces unrealistic expectations by leadership
- **3%** No staffing challenges
- **27%** The team is underfunded
- **34%** The team is underskilled
- **52%** The team is overworked

State of Security 2025 | Splunk

## Chapter 4: The new era of threat detection

> Detection as code represents a new era of threat detection. It’s a smarter, faster, and more automated way to outpace the next generation of adversaries.
>
> — Jose Hernandez, Director, Splunk Threat Research Team

State of Security 2025 | Splunk

A live phone call that sounds exactly like your CEO. An automated script that scrapes GitHub repositories for security keys. A malicious website that appears in the top spot of a Google search, or masks as a legitimate ad.

Five years ago, these attack techniques were considered obscure and sophisticated. In 2025, they’re relatively commonplace. In another five years, these antics will give way to even more creative threats. But while the toolsets of threat actors have expanded significantly, so will the solutions for defending against them.

### Data complexity creates new detection dilemmas

Detections are one of the most important tools in a defender’s arsenal. Like every powerful tool, detections aren’t one-size-fits-all. Many teams lean heavily on vendor detections but also rely on internal analysts to fine-tune them — this is the most common detection method for respondents, with nearly half (46%) reporting they take this approach frequently or always. Some depend on their in-house engineering teams to manually author and manage detections. A few are adopting the emerging approach, detection as code (DaC), to enable their SOC or engineering teams to create detections quickly and at scale.

Still, teams want to up their detection game. Looking ahead, while over three quarters (77%) say their standing is good, they still plan to increase the quality of their SOC’s detections. Only 8% rate their detection quality as excellent. Most respondents blame a few factors; 62% point to poor data quality, whether it’s due to lack of the right data, or lack of data overall. Over half (53%) report that their SOC doesn’t have the skills or expertise to create effective detections.

Detections are only as strong as the data they rely on. An explosion of ephemeral data such as service accounts, APIs, token keys, and other data not attached to a person — also called non-human identities — makes it difficult for analysts to effectively capture the data they need for robust detections.

“Every non-human identity represents a potential entry point for attackers,” says Shannon Davis, principal security strategist at SURGe. “They proliferate quickly, and it’s easy for organizations to lose track of them. Forgotten APIs, orphaned service accounts, and leaked tokens create hidden risks — especially as SOCs struggle to sift through massive amounts of ephemeral data to detect real threats.”

According to LaFerrera, it’s a challenge for teams to get data in the right spot and in the right format.

“Security teams aren’t just dealing with raw syslogs anymore, but massive blobs of data in a multitude of formats that need to be parsed, ingested, and analyzed properly,” he says. “It’s an incredibly complex endeavor.”

![Bar chart showing leading causes of poor detection quality](image-of-causes-of-poor-detection-quality)

The leading causes of poor detection quality

- **62%** We have poor data quality
- **53%** Our SOC does not have the skills or expertise to create effective detections
- **48%** We don’t have time to create effective detections
- **39%** Creating detections is not a priority in our organization

State of Security 2025 | Splunk

### Detection as code unlocks a flexible future

To realize the value of detection as code, SOCs first must bridge the divide between aspiration and adoption. Teams might be wary of the upfront setup involved — especially since 41% say they don’t have sufficient detection engineering skills.

A maturing market has produced more solutions to ease detection as code adoption for SOC teams by helping to train analysts and validate detections on their behalf. When SOC teams clear initial hurdles like setting KPIs and piloting noisier detections, the benefits will unfold exponentially.

“When you have good detections in place, it becomes a virtuous cycle,” says Paine. “Analysts have fewer false positives and more time to refine existing processes, detections become more efficient, and those capabilities keep expanding.”

> Out-of-the-box detections will only take you so far. Every environment is unique. At the end of the day, there will always be a specific threat that your vendor isn’t aware of.
>
> — Jose Hernandez, Director, Splunk Threat Research Team

In the SOC, speed and efficiency reign supreme. As attacks become faster and more unpredictable, detections must be even more nimble, standardized, and high quality to keep up. Detection as code is a detection strategy that helps defenders pivot in an instant and adapt.

Detection as code ushers in a new era of detection engineering that’s agile, dynamic, and automated. Those who have adopted this practice report considerable benefits. Sixty-two percent say it enables test-driven development practices, such as roll back and auditing — a key element of flexibility. Others say it’s allowed them to automate workflows (52%) and standardize deployment (45%), functions that often translate to time savings and efficiency.

Detection as code will be front and center in the SOC of the future. Currently, about a third of respondents (35%) frequently or always use detection as code, but 63% say they would like to frequently or always adopt this