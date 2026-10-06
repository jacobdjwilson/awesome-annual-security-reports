# State-of-AI-in-OT

**Organization:** Takepoint  
**Report Title:** State-of-AI-in-OT  
**Year:** 2026  

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [AI in OT Cybersecurity 2026](#ai-in-ot-cybersecurity-2026)
- [State of Adoption and Value](#state-of-adoption-and-value)
- [Agentic AI and Operational Authority](#agentic-ai-and-operational-authority)
- [Implementation Barriers](#implementation-barriers)
- [Physical-Consequence Risk and AI Security Controls](#physical-consequence-risk-and-ai-security-controls)
- [Governance, Regulation, and Consequence Mapping](#governance-regulation-and-consequence-mapping)
- [Takepoint Outlook: Next 6 to 12 Months](#takepoint-outlook-next-6-to-12-months)
- [Conclusion](#conclusion)
- [Methodology and Participant Profile](#methodology-and-participant-profile)
- [About Takepoint Research](#about-takepoint-research)
- [Disclaimer](#disclaimer)

---

## Executive Summary

Takepoint Research conducted the AI in OT Cybersecurity Industry Survey 2026 between April 13 and July 10, 2026, gathering 302 completed responses from professionals working in or closely supporting operational technology (OT), industrial control systems (ICS), industrial cybersecurity, automation, engineering, and critical infrastructure operations.

The aim is to provide a clear view of AI adoption, reported benefits, and emerging risks in OT cybersecurity, and to assess where the market is likely to move over the next 6 to 12 months.

## Key Findings

- 87.7% of respondents are already using, evaluating, piloting, or planning AI for OT cybersecurity, but only 7.9% have deployed AI for multiple OT cybersecurity functions.
- 69.9% believe AI's benefits in industrial cybersecurity outweigh the risks, though only 20.9% hold that view without qualification.
- AI use is concentrated in detection, monitoring, and analyst-support workflows: threat detection and alerting (33.8%), network monitoring and anomaly detection (31.5%), and SOC augmentation (24.5%) lead current use, and 63.6% of respondents report using AI for at least one OT cybersecurity function.
- Agentic AI engagement is broadening: 42.7% have evaluated, piloted, or deployed it, while 21.2% report an active pilot or production environment and 5.0% report production deployment.
- Data quality and legacy integration (45.4% and 42.4%) are the top implementation barriers, well ahead of regulatory uncertainty (18.5%).
- 63.9% treat AI-related physical-consequence risk (corrupted decisions leading to safety events, equipment damage, or downtime) as a top-tier or emerging priority, yet only 11.9% have formally mapped the AI-driven decisions that could cause it.

## AI in OT Cybersecurity 2026

AI adoption in OT cybersecurity has moved beyond early market curiosity, but most organizations remain closer to evaluation and targeted use than operational scale. The 2026 findings reveal broad engagement with AI, qualified confidence in its benefits, and a widening gap between adoption and formal assurance. This report examines where AI is being used, what value respondents report, which barriers are slowing implementation, and how organizations are approaching agentic AI, governance, and physical-consequence risk. This report provides an in-depth, data-grounded view of where AI in OT cybersecurity actually stands in 2026: how it is being used, where it is delivering value, and where governance and assurance have not yet caught up with adoption.

Takepoint Research conducted its first AI in OT Cybersecurity Industry Survey in 2024, gathering 284 responses. This report presents the second cycle: 302 completed responses gathered between April 13 and July 10, 2026. The 2026 instrument was substantially redesigned to reflect how the market has changed, most notably with new questions on agentic and autonomous AI, AI-related physical-consequence risk, technical assurance, and consequence mapping that did not exist in the 2024 survey.

The survey was supported by:

![Supported by partner logos](partner-logos.png)

© 2026, TP Research. All rights reserved.

---

## State of Adoption and Value

This section covers how much AI is currently in use across OT cybersecurity programs, whether the market believes it is worth the risk, where specifically it is being applied, and whether it has actually delivered results.

**Survey Question:** How would you describe your organization's current use of AI within your OT cybersecurity program?

### Takepoint Analysis: AI adoption is advancing, but most organizations have not yet scaled beyond targeted use

Almost one-third of respondents, 30.8%, have deployed AI for at least one OT cybersecurity function. However, only 7.9% have deployed AI for multiple OT cybersecurity functions, indicating that broad operational adoption remains concentrated among a relatively small group of more mature organizations.

The largest segment, 37.1%, is piloting or evaluating AI, indicating that the market is moving beyond general interest and into practical assessment. A further 19.9% expect to implement AI within the next 12 months. Combined, 87.7% of respondents are already using, evaluating, piloting, or planning AI for OT cybersecurity. Only 12.3% report no current implementation plans.

**Survey Question:** Overall, do you believe the potential benefits of AI in industrial cybersecurity outweigh the risks?

### Takepoint Analysis: The industry is positive about AI, but confidence remains conditional

More than two-thirds of respondents, 69.9%, believe the potential benefits of AI in industrial cybersecurity outweigh the risks. However, only 20.9% express a clear conviction that the benefits are significantly greater. The largest group, 49.0%, takes a more measured position, recognizing material risks around reliability, data integrity, model manipulation, and need for human oversight.

The most important finding is not simply that seven in ten respondents are positive: most of that support is qualified. Organizations increasingly see value in AI-assisted detection, analysis, prioritization, and analyst support, while remaining cautious about opaque recommendations, autonomous actions, and decisions that could affect physical operations.

**Survey Question:** Which OT cybersecurity functions is your organization currently applying AI to? Percentages exceed 100% because respondents could select multiple functions.

### Takepoint Analysis: AI adoption is concentrating in monitoring, detection, and analyst-support workflows

Threat detection and alerting is the most widely reported OT cybersecurity function for AI use (33.8%), followed by network monitoring and anomaly detection (31.5%), SOC augmentation (24.5%), and incident response and triage (22.2%). Organizations are introducing AI first where it can process large data volumes, identify patterns, reduce alert burden, and help experienced personnel investigate and prioritize activity.

Reported AI use is lower in vulnerability management (19.5%), risk assessment and prioritization (17.5%), and predictive maintenance or asset health (12.9%), OT cybersecurity functions that typically require stronger asset context and higher-quality operational data. A total of 192 respondents, 63.6%, report using AI for at least one OT cybersecurity function. Among these respondents, AI is being used across an average of 2.55 functions.

**Survey Question:** Has your organization experienced a measurable, demonstrable benefit from AI in your OT cybersecurity operations?

### Takepoint Analysis: AI is producing visible value, but formal measurement remains limited

Almost one-third of respondents, 32.4%, report that AI has already delivered either a quantifiable or qualitative improvement in OT cybersecurity operations. However, only 8.6% can demonstrate a clear, formally measured improvement; a much larger group, 23.8%, has observed benefit but has not translated it into an established performance measure.

Among the 184 respondents whose AI use is advanced enough to assess outcomes, 53.3% report some level of improvement and only 10.9% report none, but 35.9% say it is still too early to determine. Reported benefits are substantially more common among organizations at more mature stages of deployment: among the 93 respondents that have deployed AI for at least one OT cybersecurity function, 82.8% report some improvement, including 28.0% with a clear, quantifiable result.

---

## Agentic AI and Operational Authority

Agentic AI raises a single underlying question: how much authority AI is given, and who watches it. This section pairs agentic and autonomous AI adoption with the human-in-the-loop protocols meant to govern it.

**Survey Question:** Has your organization deployed or formally evaluated agentic or autonomous AI (AI that can take actions without step-by-step human instruction) for any OT security function?

### Takepoint Analysis: Agentic AI engagement is broadening, but production deployment remains rare

More than four in ten respondents, 45.7%, have moved beyond general awareness to formally evaluate, pilot, or deploy agentic AI for an OT cybersecurity function. This indicates broadening market engagement, but active use remains considerably narrower.

A total of 21.2% report that agentic AI has reached an active pilot, proof of concept, or production environment. This includes 16.2% conducting a pilot or proof of concept and only 5.0% reporting production deployment.

The results indicate that evaluation is progressing more quickly than operational deployment. The gap may reflect unresolved requirements around operational context, data quality, integration, assurance, and accountability, several of which appear elsewhere in the survey as material implementation barriers.

**Survey Question:** Does your organization have a defined human-in-the-loop protocol for AI-driven decisions that could affect operational safety, availability, or physical processes?

### Takepoint Analysis: Human oversight is common where AI-driven decisions apply, but formal protocols remain limited

Among the 183 respondents for whom the question applies, 78.7% report some form of human oversight for AI-driven decisions that could affect operational safety, availability, or physical processes. Most rely on informal practices: 55.7% have oversight that is not formally codified, while 23.0% have a documented and enforced human-in-the-loop protocol. A further 18.6% report no defined protocol, and 2.7% say AI-driven decisions are largely automated.

Formal protocols are closely associated with consequence mapping. Among the 42 respondents with a documented and enforced human-in-the-loop protocol, 90.5% have also completed at least some mapping of the AI-driven decisions that could affect physical processes. Findings for this subgroup should be treated as directional.

---

## Implementation Barriers

**Survey Question:** What are your organization's biggest challenges when implementing AI in OT cybersecurity? Percentages exceed 100% because respondents could select up to 3 options.

### Takepoint Analysis: Data readiness and legacy integration are greater barriers than regulation

Data quality, availability, and labeling is the most widely reported challenge (45.4%), followed closely by integration with legacy OT systems and infrastructure (42.4%). The findings indicate that practical implementation conditions are more immediate barriers than lack of market interest: OT data is frequently fragmented across systems, sites, vendors, and proprietary formats.

Concerns about AI reliability in safety-critical environments rank third (38.7%), distinct from general concerns about model accuracy, since an inaccurate output in an OT environment can contribute to downtime, equipment damage, or a safety event. More than one-third, 34.1%, cite a lack of skilled personnel. By comparison, regulatory uncertainty is selected by only 18.5%.

Organizations planning implementation reported more barriers, selecting an average of 2.93 challenges, compared with 1.21 among organizations that have deployed AI for multiple OT cybersecurity functions. Only 22 respondents, 7.3%, reported no significant challenges; 21 of them had already deployed AI.

---

## Physical-Consequence Risk and AI Security Controls

This section pairs awareness of AI-related physical-consequence risk with the technical controls meant to prevent it.

**Survey Question:** Are you concerned that a cyberattack targeting your AI systems or operational data could lead to corrupted decisions and ultimately cause physical consequences such as safety events, equipment damage, or unplanned downtime?

### Takepoint Analysis: Concern about AI-related physical consequences is widespread, but formal safeguards remain limited

Almost two-thirds of respondents, 63.9%, consider attacks targeting AI systems or operational data either a top-tier operational risk (20.5%) or an emerging priority they are beginning to address (43.4%). Overall, 87.7% acknowledge at least some potential for an AI-related cyberattack to contribute to downtime, equipment damage, or a safety event.

Concerns are higher among organizations currently using AI for at least one OT cybersecurity function. Among these respondents, 79.2% placed the issue in one of the two highest concern categories, compared with 37.3% of non-users. The risk is not limited to autonomous systems. A compromised AI tool could suppress an alert, misclassify an incident, recommend an inappropriate response, or corrupt information used in an operational decision.

Formal safeguards remain less developed than risk recognition. Only 35.1% report having AI security controls, whether tested or not, while 15.6% have an enforced OT-specific AI policy and 11.9% have formally mapped which AI-driven decisions could influence physical processes.

**Survey Question:** How confident are you that the AI tools and models used in your OT environment are adequately protected against manipulation, adversarial inputs, or supply chain compromise?

### Takepoint Analysis: Controls are emerging, but tested assurance remains rare

Just over one-third of respondents, 35.1%, report having controls intended to protect AI tools and models against manipulation, adversarial inputs, or supply chain compromise. However, only 7.6% are very confident because those controls have been tested; a much larger group, 27.5%, has introduced controls that have not yet been fully validated.

Among the 187 respondents able to assess their AI security position, 56.7% say some controls exist, yet fewer than one in eight have tested them sufficiently to express strong confidence.

Traditional cybersecurity measures remain necessary, but AI introduces additional questions around training and operational data, model behavior, prompt and input manipulation, third-party components, and the integrity of AI-generated outputs. Until testing against adversarial conditions becomes routine, confidence in AI security will remain largely provisional.

---

## Governance, Regulation, and Consequence Mapping

This section covers the three pillars of formal AI governance in OT: written policy, regulatory preparation, and mapping of the decisions AI can influence.

**Survey Question:** Does your organization have a formal AI governance or AI use policy that specifically covers the use of AI within OT or industrial environments?

### Takepoint Analysis: Half of organizations are building OT-specific AI governance, but only a small minority actively enforce it

Just over half of respondents, 50.3%, either have a formal OT-specific AI policy or are developing one. However, only 15.6% report a policy that is already actively enforced; more than twice as many, 34.8%, remain in development. A further 30.8% rely on general IT or cybersecurity policy, which may not account for AI's distinct operational, safety, and physical-process consequences in OT.

More mature stages of AI deployment are associated with stronger governance activity: 81.7% of organizations that have deployed AI for at least one OT cybersecurity function have an enforced OT-specific policy or one in development, compared with 44.6% of piloting organizations still relying on general IT policy.

A formal policy does not automatically mean supporting controls are implemented: among the 47 organizations with an enforced policy, only 17 have tested the specific controls protecting their AI tools and models. AI governance in OT is moving from awareness into policy development, but enforcement and operationalization remain the weak points.

**Survey Question:** Is your organization actively tracking or preparing for AI-specific regulatory requirements/frameworks, such as the EU AI Act, NIST AI RMF, or sector-specific AI guidelines, that may affect your industrial operations?

### Takepoint Analysis: Most organizations are monitoring AI requirements and guidance, but relatively few have established a dedicated response

More than half of respondents, 54.3%, are monitoring or preparing for AI-specific requirements, voluntary frameworks, or sector guidance. However, only 17.9% have moved beyond monitoring into a formal initiative; the largest group, 36.4%, is watching developments but has not yet taken structured action.

Regulatory monitoring and preparation are more common among organizations at more mature stages of deployment: 79.6% of organizations that have deployed AI for at least one OT cybersecurity function are tracking or formally preparing for AI-specific requirements, frameworks, or sector guidance, versus 63.4% of piloting organizations. Only 18.5% of respondents named regulatory uncertainty among their top three implementation challenges, well below the 54.3% actively tracking regulation, indicating organizations are preparing for AI regulation without treating it as the principal obstacle to adoption.

**Survey Question:** Has your organization mapped which AI-driven decisions in your OT environment could directly influence physical processes, safety systems, or operational continuity?

### Takepoint Analysis: Formal mapping of AI-driven operational consequences remains uncommon

Only 11.9% of respondents have formally mapped and reviewed which AI-driven decisions could directly affect physical processes, safety systems, or operational continuity; a further 25.2% have assessed selected systems. Among the 176 respondents for whom the question applies, 63.6% have completed at least some mapping, but only one in five has a formal, reviewed process.

Formal governance is strongly associated with mapping maturity: all 36 respondents with a formally mapped and reviewed process also have an enforced OT-specific AI policy, compared with almost none among organizations relying on general IT policy. Organizations with agentic AI in pilot or production are more likely to have started consequence mapping.

The critical assurance gap is not simply whether organizations have mapped their AI systems. It is whether they have mapped the decisions those systems can influence: connecting the AI-generated output, the decision it informs, the operational action that may follow, and the control that can interrupt an unsafe outcome.

---

## Takepoint Outlook: Next 6 to 12 Months

Across the survey findings, one pattern recurs: industrial organizations are advancing AI adoption faster than they are putting formal safeguards in place. Use is likely to continue expanding across detection, monitoring, triage, investigation, and other analyst-support functions, while deployment across multiple OT cybersecurity functions remains limited.

Agentic AI will continue moving through evaluation and constrained pilots, but production deployment is likely to remain rare. Most organizations will favor systems that collect evidence, correlate events, and prepare recommendations over those permitted to make unrestricted changes to operational environments.

Data quality, legacy integration, and reliability in safety-critical settings will remain the principal implementation barriers. At the same time, governance is likely to become more OT-specific, with greater emphasis on documented human oversight, tested AI security controls, and mapping the decisions AI can influence.

## Conclusion

The market has moved beyond debating whether AI has a role in OT cybersecurity. The question is now where it can be used safely, effectively, and with sufficient operational control.

The survey shows broad engagement, qualified confidence, and emerging operational benefits. It also shows that formal safeguards remain less mature than adoption. Over the next 6 to 12 months, the organizations that progress furthest are likely to be those that expand AI use without granting it more authority than their controls, evidence, and operating models can support.

© 2026, TP Research. All rights reserved.

---

## Methodology and Participant Profile

### Research methodology

Takepoint Research conducted the AI in OT Cybersecurity Industry Survey 2026 from April 13 to July 10, 2026, gathering 302 completed responses from professionals working in or supporting OT, ICS, industrial cybersecurity, automation, engineering, and critical infrastructure operations.

The 12-question survey covered AI adoption, use across OT cybersecurity functions, agentic AI, implementation barriers, reported benefits, physical-consequence risk, AI security controls, governance, human oversight, regulatory preparation, and consequence mapping. Responses were collected anonymously and are presented in aggregate. Single-select results are based on the full sample unless stated otherwise; multi-select totals may exceed 100%.

### Independence and limitations

The survey and analysis were developed independently by Takepoint Research. Nozomi Networks, BlastWave and Industrial Cyber provided support for this research. They did not access individual responses or influence the survey design, analysis, findings, or conclusions.

The self-selecting sample may over-represent larger organizations, respondents already engaged with AI or industrial cybersecurity, and participants from North America and Europe. The findings should therefore be read as an indicator of market direction rather than a statistical representation of all industrial organizations.

### Participant Profile

The sample is composed mostly of industrial asset owners and operators (73.2%), with the remainder split between technology and service providers or systems integrators (17.9%) and government, regulatory, research, or advisory organizations (8.9%).

![Participant profile chart](participant-profile-chart.png)

North America accounts for the largest share of respondents (40.1%), followed by Europe (26.2%), Asia-Pacific (15.6%), the Middle East and Africa (11.3%), and Latin America (7.0%).

By organization size, 61.9% of respondents work at organizations with more than 5,000 employees and 16.2% at organizations with up to 1,000 employees; larger enterprises are somewhat over-represented relative to smaller operators.

By role, respondents were led by OT/ICS cybersecurity managers or directors (21.2%), security architects, engineers, and analysts (17.9%), and OT, automation, or control engineers (16.6%).

© 2026, TP Research. All rights reserved.

---

## About Takepoint Research

Takepoint Research is an independent analyst firm focused on industrial cybersecurity across manufacturing and critical infrastructure. Our research is shaped by a value protection approach that connects cyber risk to operational consequence, business value, safety, resilience, and execution. We examine how threat pathways, crown jewels, high-consequence events, organizational capability, and market conditions affect the decisions industrial organizations need to make. Through research and advisory services, we help CISOs, OT security leaders, engineering teams, and operations teams interpret complex developments, set clearer priorities, evaluate vendors, and direct investment where it can protect the most value. The measure of our work is whether it improves decisions and changes what organizations do in practice.

## Disclaimer

This document is proprietary to Takepoint Research and cannot be replicated or shared without written permission. The opinions here are those of Takepoint Research's analysts and are not definitive statements of fact. While efforts have been made to verify the information, its accuracy and completeness are not warranted. Takepoint Research does not provide legal or financial advice through its publications. Use of this document is subject to Takepoint Research’s Usage Policy. The company ensures its research is independent and not influenced by third parties. This research must not be used for developing or training AI, machine learning, or related technologies.

© 2026, TP Research. All rights reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-05", "model": "gemini-3.5-flash-lite"} -->
