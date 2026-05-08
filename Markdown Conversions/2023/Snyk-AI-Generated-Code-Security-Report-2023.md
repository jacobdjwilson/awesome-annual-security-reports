# AI-Generated-Code-Security-Report

**Organization:** Snyk  
**Year:** 2023

## Table of Contents
- [Executive Summary](#executive-summary)
- [Part One: Risks of Outsourcing Code Security to AI](#part-one-risks-of-outsourcing-code-security-to-ai)
- [Part Two: Developers Recognize Risks of AI Blindness, Reliance](#part-two-developers-recognize-risks-of-ai-blindness-reliance)
- [Conclusion: To Fix the AI Infallibility Bias, Educate and Automate Security](#conclusion-to-fix-the-ai-infallibility-bias-educate-and-automate-security)
- [About this report](#about-this-report)

---

## Executive Summary
AI coding assistants have achieved widespread adoption among developers across all sectors. However, many developers place far too much trust in the security of code suggestions from generative AI, despite clear evidence that these systems consistently make insecure suggestions. Unfortunately, security behaviors are not keeping up with AI code adoption.

Technology organizations need to protect themselves against AI code completion risks by automating more security processes and inserting the right guardrails to protect not only against bad AI code but also against the unproven perception that AI-generated code is always superior to novel human code.

---

## Part One: Risks of Outsourcing Code Security to AI

In a short period of time, AI code completion tools have gained significant market penetration. In our survey of 537 software engineering and security team members and leaders, 96% of teams use AI coding tools and over half of those teams use the tools most or all of the time. It is safe to say that AI coding tools are now part of the software supply chain at most organizations. 

The use of AI tools has likely accelerated the pace of software code production and sped up new code deployment. On top of that, AI coding tools are polished and convincing. Unfortunately, this polish and ease-of-use has generated misplaced confidence in AI coding assistants and have created a herd mentality that AI coding is safe. In reality, AI coding tools continue to consistently generate insecure code. Among respondents, 91.6% said that AI coding tools generated insecure code suggestions at least some of the time.

The risks of AI coding tools are magnified by the resulting accelerated pace of code development. This is particularly true in open source code, where keeping up with the latest security status of open source libraries and packages is challenging. Despite these risks and challenges, our survey found that technology teams are not putting the proper measures and guardrails in place to best secure their code in this new AI coding age. Less than 10% of survey respondents have automated the majority of their security checks and scanning. 80% of respondents said that developers in their organizations bypass AI security policies. 

![Chart showing percentage of code submissions with secure answers to coding questions, comparing using AI vs not using AI across Encryption & Decryption, Signing a Message, Sandboxed Directory, and SQL]

### 56.4% Commonly Encounter Security Issues in AI Code Suggestions
Despite voicing strong confidence in AI code completion tools and demonstrating strong adoption of the tools, respondents acknowledge that AI does introduce security issues. 56.4% admit that AI introduces coding issues sometimes or frequently.

![Chart showing frequency of encountering issues due to AI code suggestions: 20.5% Frequently, 35.9% Sometimes, 34.6% Rarely, 5.8% Never, 3.2% Not sure]

### 79.9% Bypass Security Policies to Use AI, but Only 10% Scan Most Code
While most organizations had policies allowing at least some usage of AI tools, the overwhelming majority reported that developers bypass those policies. Only 9.7% of respondents said their team was automating 75% or more of security scans. 

![Chart showing percentage of security scanning that is automated]
![Chart showing frequency of developers bypassing security policies: 23.1% All the time, 31.8% Most of the time, 25% Some of the time, 12.7% Rarely, 7.4% Never]

> “By using Snyk Code’s AI static analysis and its latest innovation, DeepCode AI Fix, our development and security teams can now ensure we’re both shipping software faster as well as more securely.”
> — Steve Pugh, CISO at ICE/NYSE

### AI Further Exposes Open Source Supply Chain Security
In the survey, 73.2% of respondents said they contributed code to open source projects. Only 24.8% used software composition analysis (SCA) to verify the security of code suggestions from AI tools. 

![Chart showing methods of verifying security of open source packages: SCA tool, Code reviews, Security scorecard, Repository rates, Community activity, Check information in registry, Do not check]

### AI Considered Part of Software Supply Chain, But Few Change Practices
55.1% of respondents said that their organizations now consider AI code completion to be part of their software supply chain. However, the relative impact of AI coding tools on security practices appears to be rather small.

![Chart showing changes in software security practices: More frequent code audits, More detailed code audits, More frequent security scans, Added new tooling, Implemented security automation, Added new security processes, Has not changed]

---

## Part Two: Developers Recognize Risks of AI Blindness, Reliance

### 87% Are Concerned About AI Security, Indicating Cognitive Dissonance
The overwhelming majority of respondents expressed concerns about security implications of using AI code completion tools. This appears to contrast with the strong confidence in the ability of AI coding tools to generate secure code.

![Chart showing level of concern about broader security implications: 37.1% Very concerned, 49.9% Somewhat concerned, 13% Not concerned]

### Developers Concerned About AI Overreliance
A common concern is that developers using AI will become overly reliant on the coding tools and lose their ability to write code on their own. 46% said they were somewhat concerned and 40% saying they were very concerned.

![Chart showing level of concern regarding developer overreliance on AI tools]

### Security, Data Privacy Concerns Are Main Reasons for AI Code Restrictions
For the small subset of companies that restrict AI coding tools, the most common concern was code security (57%) followed by data privacy (53.8%) and code quality (46.4%).

![Chart showing reasons for restricting AI coding tools]

---

## Conclusion: To Fix the AI Infallibility Bias, Educate and Automate Security

There is an obvious contradiction between developer perception that AI coding suggestions are secure and overwhelming research that this is often not the case. This is a perception and education problem, caused by groupthink. The antidote is for organizations to double down on educating their teams while securing their AI-generated code with industry-approved security tools.

### 58.7% of AppSec Teams Are Struggling to Keep Up
Respondents said that over half of all AppSec teams are struggling to some degree, with one-fifth struggling significantly to keep up with the new pace of AI-driven code completion.

![Chart showing if AppSec teams are struggling to adapt to the speed of development: 20.5% Struggling significantly, 38.2% Struggling moderately, 35% Coping well, 6.3% Not affected]

---

## About this report
The survey contained 30 questions covering how organizations perceive and use AI code completion tools and generative coding. The survey polled 537 respondents working in technology roles. 45.3% were from the United States, 30.9% from the United Kingdom, and 23.6% from Canada. The panel included developer management (42.1%), developers (37.6%), IT management (30.9%), and security management (30.7%). The largest percentage of respondents cited ChatGPT (70.3%) as a tool used, followed by Amazon CodeWhisperer (47.4%), GitHub Copilot (43.7%), Microsoft Visual Studio IntelliCode (35.8%), and Tabnine (19.9%).