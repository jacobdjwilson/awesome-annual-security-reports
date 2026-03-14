# SANS 2025 AI Survey: Measuring AI’s Impact on Security Three Years Later

**Organization:** SANS  
**Report Title:** AI-Survey  
**Year:** 2025  
**Written by:** Ahmed Abugharbia  
**Date:** September 2025  
©2025 SANS™ Institute

## Table of Contents
- [Key Findings](#key-findings)
- [Survey Authors](#survey-authors)
- [Introduction](#introduction)
- [Respondent Demographics](#respondent-demographics)
- [Use Cases for AI in Security](#use-cases-for-ai-in-security)
  - [AI in Incident Response](#ai-in-incident-response)
  - [AI in Application Security (AppSec) and Code Review](#ai-in-application-security-appsec-and-code-review)
  - [AI in Red Teaming](#ai-in-red-teaming)
- [Using AI for Security Challenges and Concerns](#using-ai-for-security-challenges-and-concerns)
- [AI Attacks Are Feared More Than Defenses Are Used](#ai-attacks-are-feared-more-than-defenses-are-used)
- [Governance and Ethical Oversight](#governance-and-ethical-oversight)
- [Workforce Impacts and Future Trends](#workforce-impacts-and-future-trends)
- [Conclusion](#conclusion)

---

## Key Findings

- **Security Is Lagging Behind Advancements in the AI Industry**: Only half of the respondents who say their organization is currently using AI are using it for cybersecurity tasks.
- **Robust Implementation Is Limited**: Only 33% use AI for investigating incidents.
- **Incident Response Teams Are Heavily Pursuing AI**: 75% believe AI will complement existing tools like SIEM, SOAR, and EDR over the next three years.
- **False Positives Are Overwhelming Analysts**: 66% report that AI systems/agents generate many false positives, leading to alert fatigue.
- **AI Attacks Are Feared More Than Defenses Are Used**: Although AI is sparingly adopted by security teams, 81% are concerned about emerging AI-powered threats.
- **Security Teams Are Not Involved Enough**: Only 20% of respondents have limited involvement in governing generative AI (GenAI).
- **More Training Is Needed**: 51% say AI has affected security team training; 65% emphasized the need for more specialized AI/cybersecurity courses; 64% stressed the importance of continuous learning.
- **Respondents Are Optimistic AI Will Not Take Their Jobs**: 67% anticipate growing demand for professionals with AI and cybersecurity expertise in the next three years.

---

## Survey Authors

**Ahmed Abugharbia**  
SANS Certified Instructor  
![Ahmed Abugharbia profile photo]

**Brandon Evans**  
SANS Senior Instructor  
![Brandon Evans profile photo]

---

## Introduction

AI is not on the horizon. It is here. It has been here. Generative AI (GenAI) and large language models (LLM) entered the cybersecurity zeitgeist nearly three years ago when ChatGPT became available to the public. Business leaders are clearly interested in using GenAI. They are scrambling to incorporate it in any way that makes sense—and many ways that might not make sense.

Security leaders are also interested in implementing AI. Similarly to the business as a whole, even if they do not have a fully fleshed out use case for GenAI, they do not want to fall behind their peers. Half of respondents stated that they are currently leveraging GenAI for security while 30% said they are planning to within the next 12 months.

How are early adopters applying GenAI to security? What security problems has GenAI made more manageable, if any? What problems and threats does GenAI pose to security teams? How should we expect GenAI-driven security to evolve over time? This report answers these questions using the survey responses from SANS’s vast community of security experts.

GenAI, like anything else, is just a tool. Let us explore whether we should keep it in our utility belt at the ready or leave it in the toolshed for niche operations.

### Expert Corner
> I agree completely with the majority of respondents that security teams are lagging behind when it comes to AI adoption. In my opinion, this is because leadership teams are sure that they need AI but are not usually able to clearly articulate what that means. This, coupled with the dominant fascination with LLMs (which are amazing!) tends to impact the variety of AI/ML solutions in the cybersecurity space. Honestly, this is the reason SEC595 exists. I created it to teach SOC teams and threat hunters how to leverage AI and ML to create real-world solutions today that far exceed the commercial offerings available … and without ever using an LLM!
>
> **David Hoelzer**  
> SANS Faculty Fellow and COO at Enclave Forensics, Inc.

---

## Respondent Demographics

Most respondents were based in the United States (51%), with Europe second at 20%. The top industries represented were technology (15%), government (14%), and cybersecurity (14%) with the largest response from companies with fewer than 100 employees (18%). Figure 1 shows the survey demographics in detail.

![Figure 1. Demographics]

---

## Use Cases for AI in Security

Artificial intelligence continues to reshape cybersecurity. Its adoption varies across different cybersecurity disciplines. Although many security leaders see AI as a powerful tool they can use, the reality is more nuanced. Some domains, like application security, are already seeing meaningful integration and benefit. Others, such as incident response and red teaming, remain in earlier stages of adoption.

### AI in Incident Response

According to the respondents, incident response teams are currently adopting AI to a moderate degree. Only 26% of organizations use AI for responding to incidents and 33% for investigating incidents (see Figure 2). At the same time, 55% of organizations plan to incorporate AI into incident response for automated threat detection and analysis.

![Figure 2. How Organizations Currently Automate Detection and Response]

Most of the survey respondents expect AI to be complementary rather than disruptive, with 75% seeing AI as a complement to existing tools like SIEM, SOAR, and EDR over the next three years and only 13% expecting complete replacement.

### Expert Corner
> When two-thirds of teams report AI-driven noise, yet over half plan to expand automation, it’s clear we’re confusing urgency with readiness. False positives are not a glitch. They result from skipping the hard work of data curation, process integration, and precision tuning. To succeed, strategy must come before scale.
>
> **Seth Misenar**  
> SANS Faculty Fellow

### AI in Application Security (AppSec) and Code Review

More than a third (37%) of organizations currently use AI in their AppSec activities, while 30% do not, and 32% are unsure. Just like incident response, the primary applications focus on security analysis enhanced with AI capabilities with the most augmented AppSec tool being static analysis security testing (SAST) at 65% (see Figure 3).

![Figure 3. AI Usage for Security Tasks]

### AI in Red Teaming

Not many organizations are using GenAI for red teaming (15%). This aligns with interest respondents ranked “red team activities” as, by far, the least area they are planning to use AI technology in. The top ethical concern respondents have regarding GenAI and red teaming is whether it can adequately respect the privacy of real users (37%).

---

## Using AI for Security Challenges and Concerns

AI implementation in cybersecurity reveals a significant gap between ambition and execution. While 50% of organizations currently use AI as part of their cybersecurity strategy and another 30% plan to start within 12 months, the depth of implementation remains shallow across most use cases.

---

## AI Attacks Are Feared More Than Defenses Are Used

Security teams are reckoning with the fact that their adversaries also have access to GenAI platforms. While roughly half of the respondents’ security teams are currently using GenAI, a whopping 81% are concerned with AI-powered threats.

### Expert Corner
> The 2025 AI Survey has revealed a concerning disconnect that I’ve witnessed firsthand between red and blue teams. While 81% of security teams are concerned over growing AI-powered attacks, only 50% use these same tools for cybersecurity defense, and worse yet, just 33% leverage it for incident response. This gap between threat perception and defensive implementation suggests we’re preparing for yesterday’s war while tomorrow’s adversaries are already weaponizing these capabilities.
>
> **Foster Nethercott**  
> Certified Instructor Candidate

---

## Governance and Ethical Oversight

AI governance in cybersecurity reveals a concerning gap between recognition and implementation:
- Most of the cybersecurity professionals surveyed (68%) believe they should have a role in governing AI use across their enterprises.
- Only 35% have a formal AI risk management and compliance program in place.

Table 1 provides recommendations from the Critical AI Security Controls Guidelines to address these governance gaps.[^1]

[^1]: “Critical AI Security Guidelines,” www.sans.org/mlp/critical-ai-security-guidelines

---

## Workforce Impacts and Future Trends

The impact of AI on the cybersecurity workforce is already substantial. 51% of organizations report AI has affected training requirements for their security teams, and 54% have observed job-related changes due to AI integration (see Figure 4).

![Figure 4. AI Effect on Training Requirements and Jobs]
![Figure 5. How Organizations Are Preparing Their Workforce for the Evolving AI-Driven Cybersecurity Landscape]

---

## Conclusion

The survey data shows that the cybersecurity industry underestimates the transformational nature of AI. Organizations have made many first steps toward AI adoption, but much more is needed. Security teams are implementing AI in basic use cases like alert enrichment and anomaly detection, but they are not focusing nearly as much on transformational applications like autonomous code review, threat hunting, and incident investigation.

The window for getting ahead of this curve is narrowing. The organizations and professionals who treat AI as a fundamental shift will have a role in defining the changes in the cybersecurity field. Those who do not embrace it responsibly will risk irrelevance.