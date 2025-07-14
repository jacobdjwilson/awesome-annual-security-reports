# State of Security 2025

## Table of Contents
- [Executive foreword](#executive-foreword)
- [Introduction: Transforming the SOC from overwhelmed to optimized](#introduction-transforming-the-soc-from-overwhelmed-to-optimized)
- [Chapter 1: Efficiency in the SOC is elusive](#chapter-1-efficiency-in-the-soc-is-elusive)
  - [Busywork stifles progress and passion](#busywork-stifles-progress-and-passion)
  - [Alert overload slows down SOCs](#alert-overload-slows-down-socs)
  - [Data deficits derail investigations](#data-deficits-derail-investigations)
- [Chapter 2: AI leads SOCs into the future](#chapter-2-ai-leads-socs-into-the-future)
  - [Building trust in AI](#building-trust-in-ai)
  - [Tapping into the power of generative AI](#tapping-into-the-power-of-generative-ai)
- [Chapter 3: Skills to power the future SOC](#chapter-3-skills-to-power-the-future-soc)
  - [Skills that drive resilience are biggest shortcomings](#skills-that-drive-resilience-are-biggest-shortcomings)
  - [Automating the mundane to find reprieve](#automating-the-mundane-to-find-reprieve)
- [Chapter 4: The new era of threat detection](#chapter-4-the-new-era-of-threat-detection)
  - [Data complexity creates new detection dilemmas](#data-complexity-creates-new-detection-dilemmas)
  - [Detection as code unlocks a flexible future](#detection-as-code-unlocks-a-flexible-future)
  - [Popular threats pack a punch](#popular-threats-pack-a-punch)
- [Chapter 5: Unifying and connecting the SOC](#chapter-5-unifying-and-connecting-the-soc)
  - [Everything in its right place](#everything-in-its-right-place)
  - [Data sharing accelerates operations](#data-sharing-accelerates-operations)
  - [Words to the wise](#words-to-the-wise)
  - [How to propel your SOC into the future](#how-to-propel-your-soc-into-the-future)
  - [Step into the SOC of the future with Splunk](#step-into-the-soc-of-the-future-with-splunk)
- [Industry highlights](#industry-highlights)
- [Country highlights](#country-highlights)
- [Methodology](#methodology)
- [About Splunk](#about-splunk)

## Executive foreword

![Splunk logo]

Building an effective SOC is one of the greatest lessons in adaptability. As a former SOC leader, I’ve built security operations ranging from the Department of Homeland Security to managed security services for small- and medium-sized businesses. No matter the size or mission, the lesson is always the same: If you’re not thinking ahead, you’re already behind.

Many of us, myself included, are drawn to cybersecurity because it’s so dynamic. Cybersecurity has always been a game of rapid shifts — new threats, new malware, and now, the breakneck pace of AI. But for all the external challenges, the real problem is often internal.

We surveyed 2,058 security leaders — including SOC managers, directors, analysts, and engineers — to understand the biggest barriers to evolving the SOC and the most impactful strategies for the future.

Our data uncovers that SOCs are burning too much effort on the wrong things — babysitting tools, chasing the same false alarms over and over, and wrestling with messy data. Nearly half of them admit they spend more time maintaining their tech stack than actually defending their organization. That’s not just frustrating — it’s a failure of strategy.

But the survey also reveals that some SOCs are embracing new forward-leaning technologies and processes to help eliminate these inefficiencies. They’re leaning on AI to boost productivity, uplevel their existing teams, and become more resilient. They’re exploring detection-as-code to stay ahead of attackers. They’re rethinking their approach to investigation and response, ditching silos for a unified strategy.

We hope that State of Security 2025: The smarter, stronger SOC of the future will help propel your SOC. Because if you’re still fighting yesterday’s battles, you’ve already lost.

**David Dalling**

GVP, Global Cyber Strategist, Splunk

## Introduction: Transforming the SOC from overwhelmed to optimized

Think of the biggest threats to the SOC. Industry stereotypes might lead you to picture a hacker in a hoodie, enveloped in shadows as they type prompts into a command line. Or perhaps a team of highly skilled and credentialed nation-state actors poring over top-secret threat intel in a windowless, undisclosed government office.

Imagining these threat actors can fuel any SOC member’s drive to defend. No doubt, these are all very real threats. But what’s often overlooked is internal — the threat of inefficiency. Analysts play an endless game of Whac-A-Mole™, missing critical incidents that end up as costly breaches. Teams spend more time maintaining tools than defending the organization. Faulty data leads to faulty detections, weakening cyber defenses. And persistent skills gaps continue to stretch existing teams thin.

Teams will reach a crossroads as toolsets expand, the skills gap widens, and technologies like AI become more central to the SOC. Will security tools pile up, creating even more complexity? Will collaboration across the business become second nature to SOC teams, or will they remain in their comfort zone?

It’s time to reimagine the SOC and what it could be. SOC teams of the future will elevate their skills by relying on AI and automation. As a result, analysts will spend their time building stronger defense methods like detection as code (DaC) and perfecting their investigation protocols. They’ll take a smarter, unified approach to threat detection and response, leading to tighter collaboration and bringing more context and speed to investigations.

Does this sound like sci-fi? Believe it or not, some teams are already taking steps to build a faster, stronger, and smarter SOC. These SOCs have evolved from overloaded to optimized and resilient.

Launching into the future is an exhilarating adventure, but it’s worth the ride.

## Chapter 1: Efficiency in the SOC is elusive

> “The future SOC is extremely streamlined. Analysts will be freed from mundane, repetitive tasks, so they can apply their expertise where it truly matters: defending the organization.”
>
> — Michael Fanning, CISO, Splunk

If you’ve spent time in the security weeds, you know the nuisance of troubleshooting with no clear resolution, the hassle of reconfiguring a setting for the tenth time, or the drudgery of managing inventory.

The SOC of the future, on the other hand, will run much more efficiently. Tools are well-orchestrated and generate alerts rich with context. Every team member performs strategic tasks typically reserved for senior analysts, like in-depth analysis and investigations. They also lean on automation and AI to resolve lower-level alerts.

![Chart: The top sources of inefficiency in the SOC, listing percentages for: maintaining tools (59%), tools not integrating (51%), alerting issues (47%), requisite skills (32%), inadequate processes (31%), normalizing data (28%), managing vendors (27%), and lack of incident response process (24%).]

### Busywork stifles progress and passion

What’s holding teams back from achieving a high level of efficiency? Tool maintenance, for one. Nearly half (46%) of respondents say they spend more time doing busywork — like configuring and troubleshooting tools — than addressing critical efforts like threat investigation and mitigation.

Don’t get us wrong; tool maintenance has its place in the SOC. It can optimize workflows and improve accuracy. But respondents point to the imbalance as a growing problem, with 59% saying that it’s the main source of inefficiency for their teams, followed closely by tools not integrating well together (51%).

“Maintenance is more complicated than it used to be,” says Marcus LaFerrera, director of SURGe at Splunk. “Tools are more feature-rich with more frequent updates. And while vendors have introduced support to cut down on the guesswork, there’s far more network complexity that makes the job harder.”

Passion and purpose motivate security professionals in their mission to keep organizations safe. But no one gets jazzed about tool maintenance. A team that spends the majority of its time defending is a team that maximizes the passions of its analysts. These SOCs enable the business by being strategic, innovative, and proactive.

46% spend more time maintaining tools than defending threats

> “Analysts who can flex their critical thinking muscles rather than say, endlessly adjusting alert thresholds, aren’t simply more satisfied — they’re doing more valuable work and contributing to the organization’s bottom line.”
>
> — Kirsty Paine, Field CTO and Strategic Advisor, EMEA, Splunk

### Alert overload slows down SOCs

Every second counts in the SOC, especially during a major investigation. Inefficiencies aren’t minor headaches. Even a small bottleneck — like a missed alert that results in a data breach — can cause significant reputational, legal, or financial consequences. Downtime is just one example, and it can cost organizations $540,000 per hour, according to The Hidden Costs of Downtime report.

Alerts are another “can’t live with them, can’t live without them” part of the job for analysts, with 47% pointing to alerting issues as the most common source of inefficiency in the SOC. Respondents said most troublesome issues were having too many alerts (59%), dealing with too many false positives (55%), and deciphering alerts that lack context (46%). Each of these issues waste analysts’ precious time as they question alert validity or ignore them altogether. And who can blame them? After investigating a string of alerts that turn out to be false positives, what’s the motivation for investigating the next one?

59% have too many alerts

### Data deficits derail investigations

Wasted time extends beyond just tool management and alert overload. Data problems also play a significant role. In fact, 57% of respondents report losing valuable time during investigations due to gaps in their data management strategies.

Whether those gaps are attributed to accessibility concerns (39%) or data silos (35%) — both common data challenges flagged by respondents — not being able to access the right data in the right place makes it even harder for SOC teams to act quickly and decisively when facing threats.

> “You want to bring your analytics to your data, not the other way around. SOC teams that recognize this and have strategies involving data federation are already a step ahead.”
>
> — Kirsty Paine, Field CTO and Strategic Advisor, EMEA, Splunk

57% have lost valuable investigation time due to data management gaps

## Chapter 2: AI leads SOCs into the future

> “In the future, AI will become an integral part of the security analyst experience. AI can enable self-healing systems to detect and mitigate malicious behavior in real time. Imagine what that technology could do once it’s embedded in the SOC.”
>
> — Tamara Chacon, Security Strategist, Splunk SURGe