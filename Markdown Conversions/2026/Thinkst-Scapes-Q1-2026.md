Organization: Thinkst  
Report Title: Scapes-Q1  
Year: 2026  

Q1 2026  
https://thinkst.com/ts  

Brought to you by  
Most companies find out way too late  
that they've been breached.  
Thinkst Canary changes this.  
Canaries deploy in under 2 minutes  
and require 0 ongoing admin overhead.  
They remain silent until they need to chirp,  
and then, you receive that single alert.  
When.it.matters.  
Find out why some of the smartest security teams  
in the world swear by Thinkst Canary.  
https://canary.love  
2 Q1 2026

## Table of Contents
- [Introduction](#introduction)
- [Themes covered in this issue](#themes-covered-in-this-issue)
- [Pushing browsers to the limit](#pushing-browsers-to-the-limit)
  - [Abusing Modern Browser Features for Phishing](#abusing-modern-browser-features-for-phishing)
  - [Committing CSS Crimes for fun and profit](#committing-css-crimes-for-fun-and-profit)
  - [Improving the Trustworthiness of Javascript on the Web](#improving-the-trustworthiness-of-javascript-on-the-web)
- [LLMs standing tall](#llms-standing-tall)
  - [Black-hat LLMs](#black-hat-llms)
  - [On the Coming Industrialisation of Exploit Generation with LLMs](#on-the-coming-industrialisation-of-exploit-generation-with-llms)
  - [AI Security with Guarantees](#ai-security-with-guarantees)
  - [200 Bugs/Week/Engineer: How We Rebuilt Trail of Bits Around AI](#200-bugsweekengineer-how-we-rebuilt-trail-of-bits-around-ai)
  - [Systematic debugging for AI agents: Introducing the AgentRx framework](#systematic-debugging-for-ai-agents-introducing-the-agentrx-framework)
- [LLMs taking a fall](#llms-taking-a-fall)
  - [Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias](#trust-me-i-know-this-function-hijacking-llm-static-analysis-using-bias)
  - [AI Agent Traps](#ai-agent-traps)
  - [Leaking secrets from the claud](#leaking-secrets-from-the-claud)
  - [Scary Agent Skills: Hidden Unicode Instructions in Skills ... And How To Catch Them](#scary-agent-skills-hidden-unicode-instructions-in-skills--and-how-to-catch-them)
- [Nifty sundries](#nifty-sundries)
  - [Data Honeytokens for the Cloud Era](#data-honeytokens-for-the-cloud-era)
  - [The Offense Death Cycle: Proactive Environmental Control as a Method of Persistent Cyber Defense](#the-offense-death-cycle-proactive-environmental-control-as-a-method-of-persistent-cyber-defense)
  - [The AWS Console and Terraform Security Gap](#the-aws-console-and-terraform-security-gap)
  - [The Limit Is the Sky… (Or Not)?](#the-limit-is-the-sky-or-not)
  - [Coruna: The Mysterious Journey of a Powerful iOS Exploit Kit](#coruna-the-mysterious-journey-of-a-powerful-ios-exploit-kit)
- [Conclusions](#conclusions)

Contents  
Introduction 4  
Themes covered in this issue 5  
Pushing browsers to the limit 6  
Abusing Modern Browser Features for Phishing 7  
Committing CSS Crimes for fun and profit 8  
Improving the Trustworthiness of Javascript on the Web 9  
LLMs standing tall 10  
Black-hat LLMs 11  
On the Coming Industrialisation of Exploit Generation with LLMs 12  
AI Security with Guarantees 13  
200 Bugs/Week/Engineer: How We Rebuilt Trail of Bits Around AI 14  
Systematic debugging for AI agents: Introducing the AgentRx framework 15  
LLMs taking a fall 16  
Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias 17  
AI Agent Traps 18  
Leaking secrets from the claud 19  
Scary Agent Skills: Hidden Unicode Instructions in Skills ... And How To Catch Them 20  
Nifty sundries 21  
Data Honeytokens for the Cloud Era 22  
The Offense Death Cycle: Proactive Environmental Control as a Method 23  
of Persistent Cyber Defense  
The AWS Console and Terraform Security Gap 24  
The Limit Is the Sky… (Or Not)? 25  
Coruna: The Mysterious Journey of a Powerful iOS Exploit Kit 26  
Conclusions 27  
Cover photo: Giant Water Lilies, Vietnam. Image by Vittoria Toso (Thinkst).  
3 Q1 2026

## Introduction

Welcome to this edition of ThinkstScapes for Quarter 1, 2026!  
This issue focuses on content released, published or presented from the first of January through to the end of March 2026.  

This quarter saw more talks than last quarter, which is to be expected after the holidays. A few conferences have moved around this year (such as RSAC occurring earlier and Offensive Con later) – it will be interesting to see how that changes the pace of content release over the remainder of 2026.

Unless you’ve been living under a rock, you’ve been awash in a constant stream of news, research, and social media regarding how generative AI is changing everything. Unsurprisingly, security research isn’t exempt from this trend as over 33% of the talks we reviewed involved AI, compared to 11% last quarter. LLMs may be the first security-relevant tooling being subsidised to the tune of billions of dollars per year (even with Super Bowl ads!) as model vendors cast a broad net to find where LLMs can demonstrate fit-for-purpose.

It’s worth noting that a previously hot vulnerability research tool, fuzzers, found thousands of vulnerabilities in real-world software, and their mainstream adoption was hailed as the era of near-infinite bugs. While this in no way disputes the ability of language models to find new bugs from more classes (and weaponise them in hours), it’s likely that generative AI doesn’t (yet) require a fundamental shift in how to defend an organisation.

We liked this post advocating for what we’ve known for a while, that implementing least-privilege, rapid patching, network segmentation, ephemeral credentials, and assume-breach mentalities (such as lateral movement detections) will pay off in an LLM world just as they have in the past.

Enough time on the soapbox, let’s return to the heart and soul of ThinkstScapes – the great research from across the community.

In addition to more than 1,100 blog posts, this quarter’s content was drawn from talks and papers presented at the following conferences:

| Conference venue | Number of talks/papers |
| --- | --- |
| BOB | 17 |
| BSides Limburg | 14 |
| BSides SF | 110 |
| Cactus Con | 37 |
| ChiBrrCon 2026 | 32 |
| DISOBEY THE NORDIC SECURITY EVENT | 40 |
| District Con 1 | 51 |
| HICSS 59 | 712 |
| Insomni’hack | 46 |
| m0leCon 2026 | 7 |
| NDSS 2026 | 63 |
| Nullcon Goa | 14 |
| RSAC 2026 | 273 |
| RWC 2026 | 46 |
| RE//verse | 16 |
| Securi-Tay | 22 |
| WWHF'26 | 42 |
| [un]prompted The AI Security Practitioner Conference | 54 |
| Zer0Con | 10 |
| **Total** | **1,606** |

As a reminder: if you are aware of work we’ve missed, a blog post we should have seen or a conference we should have covered, we’d love to hear about it. Please send them to ts@thinkst.com!  
4 Q1 2026

Clarence Drive, Cape Town. Image by Dev Dua (Thinkst).  

## Themes covered in this issue

### PUSHING BROWSERS TO THE LIMIT
This theme covers research into using browser functionality in wild security-relevant ways without exploiting the browsers themselves. Look for: a novel phishing technique that uses WebGL to hide browser warnings, CSS and SVG doing more than ever thought possible, and finally, adding more security to the countless plain-text scripts downloaded and executed by browsers every day.

### LLMS STANDING TALL
This theme highlights some of the wins stemming from LLMs and their use in different aspects of security. Check out: evidence of a phase-change in automated vulnerability detection capabilities, architectures to secure agents against prompt injections, how a security company is selling AI internally, and what a debugger for agents looks like.

### LLMS TAKING A FALL
As a counterpoint, LLMs are still contributing to security missteps. Look at this theme for: a class of attack that causes LLMs to lose the plot when analysing code, a taxonomy of agent attacks, how LLM development tools are doing more than ever thought possible, and how plain-text skills can pack a malicious punch.

### NIFTY SUNDRIES
As always, there’s great research to feature that doesn’t fit into this quarter’s themes. We start with using DLP tools to honeytoken clouds, then move to how heavily-contested cyber environments must adapt, followed by the growing security divergence in secure defaults in clouds and IaC stacks, then a research talk into farming cosmic ray bit-flips, concluding with a peak at the top tier of nation-state exploitation.  
5 Q1 2026

# Pushing browsers to the limit

- [Abusing Modern Browser Features for Phishing](#abusing-modern-browser-features-for-phishing)
- [Committing CSS Crimes for fun and profit](#committing-css-crimes-for-fun-and-profit)
- [Improving the Trustworthiness of Javascript on the Web](#improving-the-trustworthiness-of-javascript-on-the-web)

Clarence Drive, Cape Town. Image by Dev Dua (Thinkst).  
6 Q1 2026

## Abusing Modern Browser Features for Phishing

**Author:** Alexander Hurbean  
[Blog](url) | [Video](url)  

This blog post details a novel phishing technique that tricks victim users into thinking their OS requires them to unlock the screen. A cookie notification modal button is used as implied user consent to activate the browser’s full-screen mode. This usually would show a pop-up that informs the user they are still interacting with their browser. The technique uses WebGL to freeze the UI by creating an infinitely-looping shader. After the UI disappears, the UI is unfrozen. This is coupled with using the keyboard lock API to prevent quick keyboard shortcut escapes. Finally, CSS is used to re-skin the social sign-in iframe containing the user’s name and image to add to the realism. While the same-origin policy prevents the malicious site from directly accessing the social sign-in details, the image and name can be moved, reshaped, and recoloured using CSS.

This technique was disclosed to both Google and Mozilla for browser-based fixes in 2024. After years without movement, the author decided to fully disclose the technique.

**TAKEAWAYS:**  
- These sorts of deceptive UI techniques highlight the diminishing returns of user awareness training. Since the user is not planning to log in to the phishing site, e.g. they’ve clicked on a blog link, there will be little scrutiny of the domain.  
- Technical controls will also struggle to prevent this technique without significant UX degradation. Hopefully disclosure will drive browser vendors to add additional protections around WebGL access that prevent security UI elements.

![Figure 1. A screenshot of the phishing site’s deceptive, full-screen Windows login prompt.](url)  
7 Q1 2026

## Committing CSS Crimes for fun and profit

**Author:** Lyra Rebane  
[Slides](url) | [Blog](url) | [Video](url)  

This talk explores some out-of-the-box CSS and SVG techniques, and how these “safe” execution environments can be used maliciously. Starting off with a brief history of how CSS was pushed to the limit for fun in a now-defunct social media site, the talk quickly shows how CSS can have significant security implications.

Minor parsing differentials between browsers and the regular expressions webmail services use can allow emails to manipulate the appearance of regions outside of the email body, or include references to an attacker-controlled server. This would leak the IP and browser identity of the recipient. In one vendor, an off-by-one error in CSS sanitisation allowed for the injection of an `@import` rule, which could allow the exfiltration of arbitrary content from anywhere on the page.

From CSS, the researcher moved to SVG, showing how all basic logic can be implemented within SVG without JavaScript needed. The filtering capabilities of SVG allow for recovering data from the screen, as well as complex clickjacking attacks (see Figure). To end, the researcher demonstrated generating a QR code dynamically in an SVG that could encode arbitrary data in the destination – allowing for exfiltration to an attacker-controlled server.

**TAKEAWAYS:**  
- On the whole, building constrained execution environments can limit the risk of abuse. That said, CSS and SVGs are still sandboxes that can have gaps in the separation between the sandbox and the unconstrained processor. Special care is needed whenever untrusted data of any type can be treated as instructions, regardless of the sandbox or virtual machine it’s contained within.  
- Complex click-jacking highlights how the user can play a vital role in the attacker’s execution environment. Evaluating the security of only the digital components in the “system” is insufficient when attackers are thinking about how the humans are involved.

![Figure 2. A diagram showing how an SVG can be used to perform complex, multi-step click-jacking attacks within Google Docs.](url)  
8 Q1 2026

## Improving the Trustworthiness of Javascript on the Web

**Authors:** Ezzudin Alkotob, Giulio Berra, Benjamin Beurdouche, Richard Hansen, Daniel Huigens, Dennis Jackson, Cory Francis Myers, and Michael Rosenberg  
[Slides](url) | [Blog](url)  

This presentation outlines a model, WAICT, for a scalable root-of-trust for web application code. While desktop and mobile applications have signed binaries that are checked at installation or runtime, web applications (even those handling sensitive data) are unverified. With the plethora of third-party, externally-hosted JavaScript libraries, there are few checks in place to ensure that a change doesn’t allow malicious code to execute.

While there have been a few proposed options for client-side verification of code prior to execution, they’ve been limited and often require a browser extension. This work aims to extend those initial projects by leveraging some of the design decisions in certificate transparency logs to allow for the publication of a witnessed and transparent application manifest. The append-only public log will allow for analysis of malicious application distribution. Firefox Nightly includes the client-side verification logic as a way to slowly roll out this technology to browsers.

**TAKEAWAYS:**  
- Turning everything into a web application has security drawbacks. While there has been considerable investment in securing browsers, without integrity on the code being run, there are still wide-open holes.  
- From remote attestation to software enclaves, there is a large existing body of work on operationalising root-of-trust in software deployment. Expect to see these techniques protecting high-value web applications in the near future.

![Figure 3. A high-level diagram of WAICT’s goal to provide integrity and transparency to web applications without any single point-of-failure.](url)  
9 Q1 2026

# LLMs standing tall

- [Black-hat LLMs](#black-hat-llms)
- [On the Coming Industrialisation of Exploit Generation with LLMs](#on-the-coming-industrialisation-of-exploit-generation-with-llms)
- [AI Security with Guarantees](#ai-security-with-guarantees)
- [200 Bugs/Week/Engineer: How We Rebuilt Trail of Bits Around AI](#200-bugsweekengineer-how-we-rebuilt-trail-of-bits-around-ai)
- [Systematic debugging for AI agents: Introducing the AgentRx framework](#systematic-debugging-for-ai-agents-introducing-the-agentrx-framework)

The Otter Trail, Garden Route National Park, South Africa. Image by Bradley Jayanath (Thinkst).  
10 Q1 2026

## Black-hat LLMs

**Author:** Nicholas Carlini  
[Video](url) | [Slides](url)  

This speaker is a research scientist at Anthropic, and the overarching thrust of his research is to see what bad things can be done with language models, in order to make them safer. To this end, he has been exploring LLMs in the realm of vulnerability finding and exploit development.

His conclusions are stark: language models are better vulnerability researchers than the vast majority of industry practitioners, and since we haven’t yet seen a downward bend in the exponential curve of their capabilities, they’re getting better, even as we write, at an increasing rate today. He predicts that the capability of the frontier models today could be accessible to local models in 12 months.

As evidence he pointed to example bugs that Claude had found and exploited, including a remotely exploitable blind SQL-injection vulnerability in Ghost CMS that had been lying around for five years, and a remote Linux kernel bug in the NFSv4 code that was introduced 22 years ago. These are simply some of the bugs he was able to publicly talk about; he mentioned sitting on several hundred Linux kernel crashes he hasn’t yet had time to look at.

His remarks were unsettling in that he describes a transitional period of upheaval that we’re about to enter, as the models greatly benefit attackers in the short term. In the long term he believes defenders will see the bugs shaking out of their software, but referenced the industrial revolution as an analogy for the pain it caused those who experienced that period. These capabilities are no longer gated to a select few, but are making it out into publicly-available models.

**TAKEAWAYS:**  
- His talk was a call-to-action for the security community to immediately face the reality of language models superseding manual security research.  
- LLMs in their current state are finding bugs and writing exploits in so-called well-tested software. And the models are still improving exponentially.  
- While inevitably the model capabilities will plateau, at this time the evidence still suggests we’re on an exponential path at this time.  
- The lack of detail on how these bugs were discovered hinders reproducibility. Without more transparency, it will be difficult to judge what aspects of vulnerability research models can contribute to the most.  
- In the short term, we will see a deluge of discovered vulnerabilities, reported and unreported. There isn’t a silver bullet to dealing with this. Patching frequently and reducing software dependencies will help matters, but these are hard and aren’t specific to AI security.

![Figure 4. A chart showing the exponentially increasing monetary value of Smart Contracts that LLMs have found bugs in. He uses this, among other examples, to argue for the exponentially increasing capabilities of language models.](url)  
11 Q1 2026

## On the Coming Industrialisation of Exploit Generation with LLMs

**Author:** Sean Heelan  
[Blog](url) | [Code](url)  

This blog post includes a reflection on how LLMs are changing software security using recently-discovered vulnerabilities to show the rapid pace of improvement. Models from 6 to 12 months ago struggled and found vulnerabilities a small percentage of the time, whereas more recent models discovered them more reliably.

The post concludes with a larger analysis of how the software industry handles vulnerabilities. The CVE and vulnerability management ecosystem has been designed and shaped to a certain pace of discovery – that is looking unlikely to continue to fit reality. If there is an exponential increase in the amount of vulnerabilities discovered, the pipelines that validate, remediate, and deploy fixes will be put under increasing stress.

**TAKEAWAYS:**  
- The rapid pace of model change needs constant re-evaluation of fit-for-purpose. Just because LLMs are not able to handle a class of tasks today doesn’t mean that they will not be able to do so in a matter of months.  
- Historically, vulnerability discovery tools shifted the burden of effort to other parts of the process. For example, fuzzing tools shifted the effort in vulnerability research towards crash analysis and determining exploitability. LLMs alone are a static analysis technique, which can over-approximate vulnerabilities, shifting the burden to triage, reachability, and determining real-world impact. Expect to see continued shifts in processes until a new equilibrium is reached.  
- Even with powerful tools, there is still a divide between expert practitioners and novices. While the narrative claims that anyone will be able to find high-impact exploits in any piece of software, LLMs are still a tool that amplifies the practitioner.  
12 Q1 2026

## AI Security with Guarantees

**Author:** Ilia Shumailov  
[Slides](url) | [Paper](url) | [Video](url)  

This talk discusses the game of cat and mouse for LLM prompt injection defenses and attacks. While models have improved their utility and capabilities significantly in the past few years, they still are vulnerable to prompt injections. Each proposed defense is quickly defeated by the next paper. Fundamentally, as LLMs are language models, there is little to no separation between the instructions provided to a model and the data to process. This leads to a utility issue where models that are only able to operate on wholly-trusted data are limited, but allowing even controlled access to untrusted data opens the door for full model takeover.

There have been proposed architectural changes that separate the “execution” model from the data being operated on. This talk highlights that for many seemingly open-ended tasks, it is possible to build a deterministic plan for executing the task without any access to the data. As shown in the figure, the planner LLM can create browser automation scripts to perform a task while isolated from any content on the internet.

The speaker concludes with a new attack class for these segregated model architectures: a cookie notice injection. As cookie notice modals are incredibly common, all the browser plans have logic that will identify and accept the notice. By purchasing banner ads that look like cookie banners, the browser automation clicks the ads, being drawn away from the expected plan path.

**TAKEAWAYS:**  
- The key insight that agentic operations must have a task-data separation analogous to the separation of instructions and data is valuable. With this “lens”, it’s possible to separate out the types of tasks that can be performed safely even when processing malicious data, and the tasks that are too open-ended to be done reliably.  
- Expect to see both more platforms using this model to add more protections to LLM-in-the-loop operations, and more adversarial research into expanding the bypass techniques. While a strong step forward for defenders, this space continues to be actively contested.

![Figure 5. A diagram showing how a planner model is tasked to create the tools to perform a task without being exposed to any potentially-malicious prompt injection data.](url)  
13 Q1 2026

## 200 Bugs/Week/Engineer: How We Rebuilt Trail of Bits Around AI

**Author:** Dan Guido  
[Slides](url) | [Blog](url) | [Video](url)  

This presentation, by the CEO of a security-engineering consultancy, breaks down the organisational shifts they undertook to become “AI-native”. The speaker examines the reasons that many organisations haven’t achieved significant lasting adoption of generative AI and defines a three-tier model for adoption: models are available to employees, models and agents are used by employees, and where models are integrated as core components of a majority of business flows.

By identifying some core psychological reasons for resistance to adoption, each could be remedied and measured. A core barrier is when employees view AI as a threat to their self-worth and identity; this was remedied by reframing AI adoption into a way to contribute and scale that experience across the entire organisation to produce a lasting artefact.

Building a comprehensive body of MCP servers, prompts, guardrails, etc. along with user-facing rules and documentation helps get new employees using and adopting AI into their workflows more quickly and with more confidence. Finally, hosting hackathon competitions instead of simple top-down mandates encourages use as part of competitive spirit.

**TAKEAWAYS:**  
- Looking at AI adoption and usage through an organisational behaviour lens is a great way to engineer and measure approaches to increase model usage. Reframing AI away from a potential threat to a way to leave a lasting mark across the organisation should improve human-machine cooperation, but only if coupled with job security assurances.  
- One of the open challenges noted in the presentation is prompt injections embedded into the source code being audited. With greater use of models that can be corrupted by e.g. source code comments, non-executable elements of software are now a threat vector.

![Figure 6. A table showing how each psychological barrier to AI adoption was remedied by the speaker’s organisation.](url)  
14 Q1 2026

## Systematic debugging for AI agents: Introducing the AgentRx framework

**Authors:** Shraddha Barke, Arnav Goyal, Alind Khare, and Chetan Bansal  
[Blog](url) | [Paper](url) | [Code](url)  

This blog post details a debugging tool, AgentRx, built specifically for LLM agents. Due to the non-determinism and new failure modes inherent in generative AI models, as longer-running agents proceed, a single failure can cascade into catastrophe. This is especially pertinent when interacting with untrusted data that may contain prompt injections. Starting with the available tools, any organisational guardrails, and a log of each agent step, AgentRx converts these inputs into a series of constraints for each step. Once the step that violated the constraint is identified using an automated checker, an LLM judge is used to interpret the failure mode. AgentRx is ~23% better than existing tools at finding the root cause and determining what caused the failure.

The authors then explored a number of traces from different agent executions, and built a taxonomy of failure mode types. These range from hallucinations to not having a tool available for the selected sub-task. By identifying the most common failure classes for a particular agent, additional guardrails or tools can be put in place to reduce error rates.

**TAKEAWAYS:**  
- The ecosystem of tooling to support (e.g., unit-test frameworks, debuggers, static analysis tools, etc) traditional software is considerably more mature than for agent-in-the-loop software. The non-determinism of today’s models introduce stochastic behaviours that didn’t exist before, and traditional support tooling isn’t built to handle.  
- The development of tooling to provide more observability and debugging capabilities for LLM-augmented software is vitally important. This capability is a great early step, but we’re still some way off from parity to the ecosystem for traditional software.

![Figure 7. A high-level diagram showing how the AgentRx tool can take a trace of an agent run and isolate the first step that went awry.](url)  
15 Q1 2026

# LLMs taking a fall

- [Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias](#trust-me-i-know-this-function-hijacking-llm-static-analysis-using-bias)
- [AI Agent Traps](#ai-agent-traps)
- [Leaking secrets from the claud](#leaking-secrets-from-the-claud)
- [Scary Agent Skills: Hidden Unicode Instructions in Skills ... And How To Catch Them](#scary-agent-skills-hidden-unicode-instructions-in-skills--and-how-to-catch-them)

Stony Point Nature Reserve, South Africa. Image by Dev Dua (Thinkst).  
16 Q1 2026

## Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias

**Authors:** Shir Bernstein, David Beste, Daniel Ayzenshteyn, Lea Schönherr, and Yisroel Mirsky  
[Slides](url) | [Paper](url) | [Code](url)  

This research explores hiding software logic from LLM-based code analyses. Leveraging the models’ frequency of training on certain software patterns, the researchers found that often the samples trained on would override the actual code when being analysed. With subtle changes from the common pattern, the attackers could create a familiar pattern of attack (FPA), or a differential between the runtime where the code was executed and the LLMs’ model of its execution. An example is to modify a common function such as `nth_prime(int n)` (which would return the $n^{\text{th}}$ prime number), by subtracting 1 from the return value. A conditional later that used this value and checked if the value was even would almost always be ignored by the LLM as its model precluded the value being even.

The researchers evaluated this model by automatically searching for FPAs and measuring how FPAs discovered in one model would transfer to other models; how robust the FPAs were to thinking models; whether specific prompting to look for FPAs would expose them; and whether agents that could run the software would find the FPAs. Across the board, FPAs had a high likelihood of success, especially when generated for a thinking model as those FPAs would both transfer to other thinking models as well as more basic inference.

**TAKEAWAYS:**  
- There’s no doubt that LLM code auditing can (and does) find issues, but it is by no means a silver bullet. Many of the types of minor changes in FPAs would slip past a quick review scan by a human as well.  
- These FPAs open the door to inject non-executable “chaff bugs” into code that waste analysis tokens and create false positives. While chaff bugs were popular in their day, they were rarely (if ever) deployed into real-world software – it will be interesting to see if FPAs are ever used in real-world applications.  
- Building comprehensive testing suites enables both more aggressive use of automation for code generation, and catches these types of differentials between actual and modeled runtime. Hopefully, we’ll see improved rigor in test coverage as AI-assisted development becomes more mainstream.

![Figure 8. A figure showing how injecting FPAs can hide behaviour from LLM code analyses.](url)  
17 Q1 2026

## AI Agent Traps

**Authors:** Matija Franklin, Nenad Tomašev, Julian Jacobs, Joel Z. Leibo, and Simon Osindero  
[Paper](url)  

This paper presents a taxonomy of “traps”, or attack classes that autonomous agents are exposed to when consuming untrusted data. The authors start by enumerating the agent pipeline and exposed processes to develop five high-level types of traps. From the familiar jailbreaking (in the behavioural control category) to the obscure (exploiting feedback loops with multiple, interconnected agents), each class of trap is examined for what research exists, and what may be feasible.

While the emphasis of this survey is on defining the taxonomy and exploring recent work in each category, there are some high-level mitigations mentioned. General hardening against prompt injection, through adversarial training and inference-time monitoring will protect against many attack classes. Additionally, the authors note that web scraping is a legal and ethical grey area in many jurisdictions, and due to agents’ susceptibility to injection, this grey area is more pressing to define. For example, could hosting invisible injection content be legally considered an attack in the same light as hosting malware?

**TAKEAWAYS:**  
- At the speed of development, it’s likely that this taxonomy will soon have gaps. That said, it is still valuable to step back and understand the scope of attack surface agents can bring into an organisation.  
- While certain classes have captured the community’s attention (e.g., jailbreaks and prompt injection), look for less-popular attack classes in this taxonomy to have their day in the sun.

![Figure 9. A table of the proposed taxonomy of attacks against agents autonomously accessing data.](url)  
18 Q1 2026

## Leaking secrets from the claud

**Author:** Niels Hofmans  
[Blog](url) | [Code](url)  

This blog post covers how the author accidentally committed a Claude-specific configuration file containing secrets to a git repository. While most git users are aware of the `.gitignore` file and its use to prevent secrets from being added to the repository and pushed, LLM-assisted development tools (e.g., Claude Code) create new directories to store their configuration. Unless these vendor-specific directories are added to the ignore list, their contents can be accidentally added to the git repository and pushed. Within the configuration files are allow-listed commands, which often contain environment variables and secrets.

The author suspected they were not the only one to mistakenly commit secrets from these sources, and wrote a tool, claudleak, to automatically search and validate any findings. In searching a sample of public repositories, over 2% had committed secrets. Because version control systems preserve history, simply removing the file doesn’t remove the contents from the repository’s memory.

**TAKEAWAYS:**  
- The pace of toolchain development has outstripped conventions and best practices. Dot-files and directories should be excluded from source control except in specific exceptions.  
- The proliferation of vendor-specific hidden directories with sensitive information will result in some bad leaks before other parts of the toolchain adapt.  
19 Q1 2026

## Scary Agent Skills: Hidden Unicode Instructions in Skills ... And How To Catch Them

**Author:** wunderwuzzi  
[Blog](url) | [Code](url) | [Video](url)  

This blog post looks at how LLM skills (YAML & Markdown files) containing invisible Unicode characters or prompt injections can maliciously control agents. Skills offer a way to encode expert knowledge and techniques into a reusable artifact that agents can leverage when performing relevant tasks. Skills are the spiritual successor to MCP tools, but directly instruct the model how to act instead of providing an API endpoint to call. An advantage of skills is their auditability, as, like MCP servers, there are repositories of open skills which may contain untrusted contents.

Previous research has shown that invisible Unicode tag codepoints (designed for controlling formatting, but reflect printable ASCII) are interpreted by many models as their ASCII equivalent. These Unicode values are not rendered, thus auditing a skill for malicious instructions is challenging without a specialised scanner or hex editor. For models that ignore the invisible Unicode, the skill files are treated as prompting instructions, and can be instructed to only show a subset of the skill in the UI.

**TAKEAWAYS:**  
- Skills have won out over MCP tools, but both have security considerations. Remotely hosted MCP servers are opaque and can corrupt the models’ context window. While skills can be audited, they can directly drive local execution. Given the pace of movement, there are certain to be other rough edges discovered.  
- Unicode injection is nothing new, but has repeatedly been brought back to light with generative AI. Continue to be on the lookout for edge cases in handling Unicode with LLMs.  
- Ensure that skills only come from trustworthy sources, and are kept internally instead of referencing the online version to prevent malicious changes.

![Figure 10. A screenshot of the skill file and Claude Code’s behaviour upon executing the benign-looking skill.](url)  
20 Q1 2026

# Nifty sundries

- [Data Honeytokens for the Cloud Era](#data-honeytokens-for-the-cloud-era)
- [The Offense Death Cycle: Proactive Environmental Control as a Method of Persistent Cyber Defense](#the-offense-death-cycle-proactive-environmental-control-as-a-method-of-persistent-cyber-defense)
- [The AWS Console and Terraform Security Gap](#the-aws-console-and-terraform-security-gap)
- [The Limit Is the Sky… (Or Not)?](#the-limit-is-the-sky-or-not)
- [Coruna: The Mysterious Journey of a Powerful iOS Exploit Kit](#coruna-the-mysterious-journey-of-a-powerful-ios-exploit-kit)

Aspiring National Park, Otago, New Zealand. Image by Jacob Torrey (Thinkst).  
21 Q1 2026

## Data Honeytokens for the Cloud Era

**Author:** Petrus Vasenius  
[Blog](url) | [Video](url)  

This talk created data honeytokens in Azure by using Microsoft’s Purview data governance tool to monitor honeytoken accesses. Honeytokens [ed: or Canarytokens] are tempting bits of data scattered across your real IT assets that alert if accessed by a malicious insider or an attacker who’s breached the perimeter. Many honeytokens trigger alerts via special modifications to the files themselves. These modifications can lead them to only trigger when opened by certain applications, however, this work used a data governance tool to alert on arbitrary files in a monitored cloud environment.

Using automated infrastructure-as-code tools, the researcher was able to create juicy-looking files throughout Microsoft Azure’s data lake hosting services that embedded specific GUIDs. These GUIDs would form the basis for a data classification rule that Purview would use to monitor any access or movement of the honeytokens. By connecting Purview to Sentinel, SIEM incidents would be created for any access.

**TAKEAWAYS:**  
- We’re big fans of canary/honeytokens. This approach of modifying the storage environment to report on access instead of specially-crafting files that self-report access will be increasingly powerful as cloud storage solutions are standardised.  
- As organisations are usually not fully cloud-native, there is an opportunity to combine both approaches to track stolen data internally and externally from an organisation’s environment. Expect to see more tokening of environments as an early warning system that can span platforms and hybrid environments.

![Figure 11. A high-level diagram showing how decoy data automatically deployed into Azure storage can be monitored by Purview and alerted on with Sentinel.](url)  
22 Q1 2026

## The Offense Death Cycle: Proactive Environmental Control as a Method of Persistent Cyber Defense

**Author:** Volodymyr Styran  
[Paper](url)  

This strategy paper lays out a conceptual framework for creating friction for persistent attackers. Looking at the conflicts between attackers and defenders in computer networks through the lens of traditional military engagements, the author notes that cyber defenders have more ability to control the environment than in real-world situations. Typically the environment is not changed, leading to reactive defenses, instead of one where defenders can add friction to attackers proactively. The paper cites a few case studies where attackers were either discovered or repulsed through dynamic changes to the environment, not a reactive countering.

The framework shows there are security benefits to changing the environment as it can interrupt the processes of attackers. These benefits should be weighed against the organisational costs of deploying such changes. Finally, the proposed framework is compared with existing security approaches that alter the environment, such as moving target defense and deception.

**TAKEAWAYS:**  
- Defenders often treat the “terrain” of their networks and environments they protect as mostly fixed. This mindset shift of considering that terrain as something that can play into an asymmetric defender advantage is powerful.  
- It’s always worth considering the threat environment facing your organisation as part of the defensive strategy. While a member of the Ukrainian government must operate in an assumed-permanently-compromised mode, that may not be feasible (or valuable, even) for all types of entities.

![Figure 12. The Offense Death Cycle.](url)  
23 Q1 2026

## The AWS Console and Terraform Security Gap

**Authors:** Laurence Tennant  
[Blog](url)  

This blog post highlights a few examples of divergences between the default security configurations of AWS resources created via the AWS console and Terraform. Over time, the console has worked to tighten the defaults, guiding users towards a higher standard of protection. However, to remain backwards-compatible, the AWS API still allows the less secure configurations.

Because Terraform (and other infrastructure-as-code IaC platforms) use the API under the hood, the resources are often created with a different configuration than expected. To prevent breakage risks if the same Terraform code is re-run, the defaults cannot be changed. A few examples presented include:
- AWS RDS defaulting to no encryption-at-rest;
- Lambda functions that can be invoked by any (including an attacker’s) API gateway; and
- IAM password policy that resets the complexity rules if any single requirement is changed.

The post concludes with suggestions for detecting and preventing these insecure defaults. These include static analysis tools that analyse the resources that are created, enforcing organisation-wide policies on AWS API calls, and having internal golden standard templates that encode the best configurations by default.

**TAKEAWAYS:**  
- Third-party defaults are always difficult to retroactively improve – there’s a high risk of surprising a customer. When applied to a multi-cloud IaC solution, there are even more defaults that are hidden. If there are configurations that are never acceptable to your organisation, set and enforce policies on those – cutting through the abstractions.  
- While this post focused on AWS and Terraform, expect similar for other cloud and IaC platforms that have worked to ratchet up security defaults.  
- Static analysis tools that can audit IaC exist, but they add third-party dependency risks. A first-party Terraform audit capability (like npm audit) would help flag shifting defaults while remaining idempotent.

![Figure 13. An example Terraform snippet that will silently remove all other password complexity requirements.](url)  
24 Q1 2026

## The Limit Is the Sky… (Or Not)?

**Author:** Antonio Nappa  
[Slides](url) | [Code](url) | [Video](url)  

This talk is about a researcher trying to replicate memory bit-flips induced by cosmic rays. A single bit-flip in the right region of memory can open an entire system – if it could be done consistently and affordably, it would be a valuable tool for reverse engineers. Three different methods were explored: putting the device adjacent to a nuclear neutron emitter, using a laser, and attaching the device to a high-altitude weather balloon.

While a device from ~25 years ago did see bit-flips from being close to the neutron emitter, a more modern device (Raspberry Pi 4) built with a smaller process did not. The laser was able to cause bit-flips, but due to the small scale of modern transistors, many bit-flips occurred from one laser pulse – causing the system to crash.

Finally, using a weather balloon to launch devices checking for bit-flips to the stratosphere had the same issue – too many bit-flips at once to reliably use as part of a workflow. Nonetheless, the researcher is undeterred and has future plans for crowdsourcing bit-flip information.

**TAKEAWAYS:**  
- While the results haven’t [yet] advanced our ability to affordably control high-energy rays for reverse-engineering, the talk offers strong evidence into how constraints breed creative solutions.  
- Very few threat models include hardware glitching attacks, though they are becoming more in scope for secure hardware. A number of consultancies offer deep hardware attacks using their significant investments in equipment. Research like this talk shows that the budget barriers are shrinking, and these types of attacks will be more common in the future. Now is the time to prepare.

![Figure 14. A photo of an experiment using a laser to induce localised thermal upsets in the memory to cause bit-flips.](url)  
25 Q1 2026

## Coruna: The Mysterious Journey of a Powerful iOS Exploit Kit

**Author:** Google Threat Intelligence Group  
[Blog](url)  

This blog post (and several related ones) documented the discovery of a novel and sophisticated iOS exploit kit called “Coruna” (an internal name revealed by a debug build of the exploit kit). We don’t typically cover exploits in ThinkstScapes, and Coruna has certainly received much attention since the publication in March. However, we think it’s an important milestone that deserves recognition.

In 2010, Haroon delivered a talk where one of the central conclusions was that professional attackers (i.e., nation states) were building and using toolchains with sophistication far in excess of what was publicly available. The Coruna analysis validates that view several times over. This exploit kit included five separate iOS exploit chains (encompassing 23 separate exploits), targeting iOS versions between June 2019 and December 2023 (iOS 13 to 17.2.1). GTIG found it to be “extremely well engineered”, and Kaspersky’s analysis showed how the single kit fingerprinted the iOS device in order to choose the correct exploit for the device’s version and state.

There are several points to be made on the Coruna saga. Kaspersky links Coruna to the Operation Triangulation report they released in June 2023 through the similarities in exploits they observed compared to exploits in Coruna. Kaspersky’s claim was that Triangulation was the work of Western intelligence agencies, and other commentators have backed that view. Regardless of how Kaspersky became aware of Coruna, GTIG makes the point that proliferation of the exploit kit needs discussion.

Assuming Coruna was, indeed, written for and used by Western intelligence agencies, we cannot ignore that GTIG saw it first being used (in Feb 2025) by a customer of a commercial surveillance company (i.e., it was used outside of an intelligence agency). A few months later in July 2025, it was seen in a watering-hole attack targeting Ukrainian websites (almost certainly not a Western attack), and by December 2025 it was being used in a mass attack against Chinese crypto users (very firmly a commercial attack). The only reasonable conclusion is that the kit made its way through several hands, increasingly public.

There is well-explored tension deciding whether to report vulnerabilities or keep them secret to maintain capability, which we won’t discuss further. But it is notable that this wasn’t the first time NOBUS capabilities have leaked with externalities (EternalBlue was the NSA’s Windows RCE that led to WannaCry).

**TAKEAWAYS:**  
- The top-end of exploitation against the most hardened platform is impressive, hands down. With all Apple’s work on security, the top-tier exploitation teams can still maintain exploit chains that work on uninterrupted version sequences. Having said that, Apple’s Lockdown Mode was effective against these attacks and is a no-brainer.  
- The most well-funded and sophisticated agencies still cannot prevent the leaking of exploits.  
26 Q1 2026

## Conclusions

This quarter saw some interesting research, both in the world of LLMs as well as traditional security.

FOR THIS QUARTER WE HIGHLIGHTED THREE THEMES:
1. Browsers pushed to the limit  
2. LLMs uplifting security  
3. LLMs weakening security  

We’ll see you next quarter with more great content to share, and to see if the community stays fascinated with all things AI as costs rise to match compute expenditures.

Cittá Alta, Bergamo, Italy.  
Image by Pavel Nekoranec (Thinkst).  
27 Q1 2026

28 Q1 2026

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
