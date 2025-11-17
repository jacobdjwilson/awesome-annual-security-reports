# The State of Threat Exposure Management

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Key Recommendations](#key-recommendations)
- [Methodology](#methodology)
- [Overall Prevention and Detection Effectiveness Performance](#overall-prevention-and-detection-effectiveness-performance)
- [Real-World Performance of Cybersecurity Products](#real-world-performance-of-cybersecurity-products)
- [Uncovering Critical Defensive Gaps with Automated Penetration Testing](#uncovering-critical-defensive-gaps-with-automated-penetration-testing)
- [Detection Rule Effectiveness](#detection-rule-effectiveness)
- [Performance by Industry](#performance-by-industry)
- [Performance by Region](#performance-by-region)
- [Performance by Attack Vector](#performance-by-attack-vector)
- [Performance by MITRE ATT&CK® Tactics](#performance-by-mitre-attck-tactics)
- [Performance by MITRE ATT&CK® Techniques](#performance-by-mitre-attck-techniques)
- [Performance by Threat Group](#performance-by-threat-group)
- [Spotlight on Ransomware Attacks](#spotlight-on-ransomware-attacks)
- [Spotlight on Vulnerabilities](#spotlight-on-vulnerabilities)

---

# Introduction

![Chart showing Prevention Score dropping from 69% to 62%, Log Score remaining stable at 54%, and Alert Score rising from 12% to 14% (At a Glance)](./images/at-a-glance-scores.png)

Currently in its third year, the 2025 edition of the Blue Report continues to deliver data-driven insights and actionable recommendations for cybersecurity professionals by evaluating the real-world effectiveness of prevention and detection capabilities. Developed by Picus Labs, this annual study is based on over 160 million attack simulations performed on the Picus Security Validation Platform, providing a comprehensive view of how security products and configurations perform across modern enterprise environments.

The Blue Report 2025 is designed to serve as a practical guide for security teams and decision-makers aiming to mature their security posture through Continuous Threat Exposure Management (CTEM). By identifying blind spots, validating assumptions, and fine-tuning defenses based on adversary behavior, organizations can reduce uncertainty, better prioritize resources, and build a more resilient cybersecurity foundation.

## What’s New This Year

- This year, weʼve deepened the reportʼs focus on prevention and detection effectiveness across attack vectors, regions, and industries. For the 2025 report, weʼve expanded our analysis to assess prevention performance against MITRE ATT&CK techniques, revealing alarmingly low prevention effectiveness across industries against frequently used adversary behaviors.

- The vulnerability section now focuses exclusively on CVEs disclosed in 2024 and 2025, offering a clearer view of how well organizations are addressing new and emerging threats. Findings from Attack Path Validation (APV) and Detection Rule Validation (DRV) highlight persistent gaps in lateral movement prevention, privilege escalation defense, and overall detection effectiveness.

# Executive Summary

![Infographic showing Data Theft Prevention Effectiveness at 3%, Password Cracking Success Rate at 46%, and Valid Accounts Prevention Failure Rate at 98%](./images/executive-summary-stats.png)

The Blue Report 2025 highlights the essential role of Continuous Threat Exposure Management (CTEM) and emphasizes the critical importance of Adversarial Exposure Validation (AEV) in confronting increasingly sophisticated cyber threats and operational blind spots. While the *Red Report 2025* highlighted the rise of credential-targeting malware and infostealers, the Blue Report identifies surprising defensive gaps, particularly in data exfiltration and password-based attacks.

Of particular concern, password cracking attempts succeeded in **46%** of tested environments, nearly doubling the previous year's rate. Compounding this risk, attacks using **Valid Accounts (T1078)** achieved a **98%** success rate, highlighting persistent challenges in maintaining effective password policies and detection.

Data exfiltration defenses suffered a severe decline, dropping to an alarming prevention rate of just **3%**. This decrease is particularly concerning given the rise of double-extortion ransomware attacks designed specifically to evade traditional encryption-focused defenses.

Despite these critical gaps, Picus Attack Path Validation (APV) assessments reveal significant improvements. Domain administrator compromise rates notably fell from 24% in 2024 to 19% in 2025, with domain admin access also decreasing significantly from 40% to 22%. These advances demonstrate strengthened lateral movement defenses, improved network segmentation, and better operationalization of security validation insights.

Average prevention effectiveness declined from 69% to 62%, indicating that security controls lose efficacy without continuous validation and tuning. While detection effectiveness improved slightly, with alert scores rising from 12% to 14%, a significant gap remains between logging and detection alerts, with log failures found in 54% of Picus Detection Rule Validation (DRV) assessments.

The Blue Report 2025 reinforces that static defenses are no match for adaptive threats. To stay ahead, organizations must adopt AEV into their CTEM programs to move beyond assumptions, prioritize with confidence, and respond faster to the threats that matters most.

# Key Findings

The Blue Report 2025 reveals a shifting cybersecurity landscape, where progress in some areas is tempered by persistent and in some cases, deepening challenges and failures in others. This yearʼs analysis shows the growing complexity of defending against real-world threats and the importance of continuous validation to reduce exposure. Below are some of the most significant findings from the report:

## Data Exfiltration Defense Is Getting Worse Despite Rising Risk

For the third year in a row, data exfiltration remains the least prevented attack vector, but this year the prevention score has deteriorated even further, dropping from 9% in 2024 to just **3%** in 2025.

This decline comes at a critical moment: the *Red Report 2025* revealed a 3x surge in infostealers, while ransomware groups are increasingly use double extortion tactics to steal and leak sensitive data. Despite these escalating threats, most organizations remain woefully unprepared to detect or block data theft, highlighting a widening and urgent blind spot.

## Password Cracking Threat Intensifies

In **46%** of environments, at least one password hash was successfully cracked and converted into cleartext, nearly doubling last yearʼs rate of 25%. This points to an ongoing reliance on weak password policies, particularly in internal domains.

The *Red Report 2025* also found credential theft techniques like *Credentials from Password Stores (T1555)* were used in 25% of malware samples, with attackers leveraging stored logins and password managers to accomplish lateral movement and escalate privileges. These trends show how quickly a single compromised credential can open the door to broader access.

## Significant Improvements in macOS Endpoint Security

In a notable reversal from last year (23%), macOS endpoints achieved a **76%** prevention rate, outpacing both Windows (79%) and Linux (69%) endpoints.

The dramatic gain in macOS protection reflects growing investment and maturity in securing Apple environments, which have been historically underprotected.

## Prevention Effectiveness Declines

After a strong improvement in 2024, the average prevention score fell slightly from 69% to **62%** in 2025. This drop suggests that many organizations are struggling to keep up with increasingly sophisticated attack techniques and that their previously effective controls may be losing their edge without continuous validation and tuning.

## Detection Shows Modest Recovery

The log score remained stable at **54%**, indicating consistent data capture and monitoring capabilities. However, alert score improved ever so slightly from 12% to **14%**, signaling slow but positive momentum in converting logs into actionable intelligence. Still, the wide delta between logs and alerts points to persistent gaps in detection engineering and threat correlation.

## SIEM Rule Failures Still Mainly Due to Logging Issues

Analysis on detection rules revealed that log collection issues caused **50%** of failures. Other core problems included performance issues (24%) and configuration errors (13%), highlighting weaknesses in the detection engineering pipeline. Additional gaps, such as improper log coalescing (17%), unavailable sources (7%), and broken sources (4%), reflect ongoing integration blind spots and monitoring lapses that continue to leave threats undetected.

## BlackByte Continues to Challenge Ransomware Defense

Ransomware remains a top concern, and **BlackByte** continues to be the hardest strain to prevent, with a prevention effectiveness of just **26%**, even after its prominence in last yearʼs findings. BabLock and Maori followed at 34% and 41%, respectively.

## Infrastructure Hardening Shows Measurable Progress with APV

This yearʼs Attack Path Validation (APV) findings indicate meaningful gains in internal security posture. In 2025, only **19%** of simulations led to full domain administrator compromise, down from 24% in 2024. Similarly, domain admin access occurred in just **22%** of environments, a significant drop from 40% the previous year.

These improvements reflect stronger lateral movement defense, segmentation, and better use of validation insights. Still, with nearly a quarter of environments vulnerable to privilege escalation, regular testing and targeted remediation both remain essential to closing critical gaps.

## Cybersecurity Product Effectiveness Still Varies in Practice

Despite strong lab performance, cybersecurity products often show significant variability in real-world environments. Solutions that score 100% in MITRE ATT&CK evaluations frequently fall short in production due to infrastructure differences, misconfigurations, and integration gaps.

These results help make the case for continuous, context-aware validation and fine-tuning to ensure controls perform reliably where they matter most.

## Core Adversary Techniques Remain Effective

Despite growing awareness of adversary behavior, many common ATT&CK techniques remain under-prevented. In 2025, **Valid Accounts (T1078)** had the lowest prevention rate at just **2%**, showing how easily attackers blend in using stolen credentials. Discovery techniques like *System Network Configuration Discovery* and *Process Discovery* also scored below 12%, exposing blind spots in early-stage detection.

Low prevention rates for Defense Evasion and Command and Control techniques, such as *Execution Guardrails (8%)* and *Data Encoding (3%)* further highlight the limitations of static detection. These trends point to a need for stronger behavioral detection to identify subtle, context-driven attacker techniques.

# Key Recommendations

The findings of the Blue Report 2025 highlight the growing need for organizations to revisit their security strategies with a sharper focus on validation, visibility, and control hardening. Based on our analysis, we recommend the following actions to reduce exposure and improve threat readiness:

## Validate Exposure, Not Just Inventory

Shift from simply knowing where exposures exist to proving which ones matter. Adopt the adversarial exposure validation approach that goes beyond asset and vulnerability discovery to confirm exploitability. This enables faster, more informed prioritization and reduces the noise and wasted effort created by theoretical risks.

## Strengthen Data Exfiltration Defenses

With data exfiltration prevention falling to just 3%, itʼs essential to enhance controls that monitor and restrict outbound data flows. Implement and validate data loss prevention (DLP) rules, outbound traffic filters, and behavioral detection to reduce the risk of silent data theft, especially as infostealers and ransomware continue to rise.

## Enforce Stronger Password Hygiene

In 46% of environments tested, at least one password hash was successfully cracked, often due to weak password complexity, outdated hashing algorithms, or the reuse of credentials across systems. Organizations should enforce strong password policies and regularly validate credential defenses through simulated password cracking attacks.

## Continuously Validate and Tune Preventive Controls

The drop in prevention effectiveness signals the need to regularly test and refine your existing defenses. Security controls, no matter how advanced, can deteriorate over time. Use real-world attack simulations to continuously validate IPS, NGFW, and endpoint security tools, ensuring they remain effective against constantly changing adversary behaviors.

## Improve the End-to-End Detection Pipeline

A 54% log score means that nearly half of attacker behaviors go unlogged, leaving organizations with significant blind spots. Even more concerning, the alert score is also critically low at just 14%, far below the levels needed for effective detection and response. Organizations must strengthen the full detection pipeline from ensuring comprehensive log coverage to fine-tuning correlation rules and alert logic.

## Strengthen Ransomware Defenses in the Era of Encryptionless Extortion

As more organizations adopt modern backup and recovery solutions, ransomware groups are shifting tactics toward encryptionless extortion, threatening to leak stolen data without deploying encryption. Ensure endpoints have up-to-date security controls, and regularly simulate full ransomware scenarios, including data exfiltration and extortion techniques, to test your ability to detect, contain, and respond before any actual damage is done.

## Improve Detection of Common Techniques with Behavioral Analysis

To address persistent gaps in preventing common ATT&CK techniques, organizations must strengthen their behavioral detection capabilities. Static rules and signature-based controls often miss subtle attacker actions, especially those that mimic legitimate user behavior. Techniques like *Valid Accounts (T1078)* and early-stage *Discovery* techniques require context-aware monitoring and identity-aware detection logic to be effectively surfaced. Regularly validate your controls against common techniques such as credential abuse, discovery, and command and control to ensure your defenses can detect and respond to the tactics adversaries rely on the most.

# Methodology

The findings in this yearʼs report are based on the results of simulated attack scenarios executed by Picus Security customers from January to June 2025. The data has been anonymized and aggregated from over 160 million attack simulations. Research and analysis was completed by Picus Labs and Picus Data Science teams.

## Definitions

**Prevention Effectiveness** evaluates an organization's ability to block potential cyber attacks through its security controls. This metric is the percentage of successfully prevented attacks out of all simulated attacks executed. For example, an effectiveness score of 80% means that 80 out of every 100 simulated attacks were effectively prevented. A high prevention effectiveness score indicates strong security controls that significantly lower the risk of successful breaches. Conversely, a low score highlights gaps in an organizationʼs current security measures, suggesting the need for security teams to conduct a thorough review and enhance their existing controls.

**Detection Effectiveness** assesses an organizationʼs capability to identify potential cyber threats through the security controls they already have in place. This report uses two key indicators for evaluating detection performance: Log Score and Alert Score.

- **Log Score**: This measures the percentage of simulated attacks where the attackersʼ behavior was logged. A higher log score demonstrates the efficacy of monitoring controls like SIEMs in capturing a large volume of events and identifying threat indicators. Effective logging is crucial for maintaining a comprehensive security posture and understanding attack patterns.

- **Alert Score**: This indicates the percentage of simulated attacks that generate alerts. High alert scores are crucial for ensuring that security teams are promptly informed of any and all threats, enabling them to take immediate action to neutralize potential risks. Alerts serve as critical triggers for initiating a timely and effective response to attacks.

## Scoring Legend

Results are color-coded and categorized into five distinct levels of threat exposure management: Inadequate, Basic, Moderate, Managed, and Optimized (see table below).

This classification provides a clear, visual representation of an organization's cybersecurity effectiveness, facilitating easy benchmarking and identifying areas for improvement.

| Level | Description |
| :--- | :--- |
| **Optimized** | Organizations with optimized security controls continuously monitor, refine, and update them to keep up with the an ever-evolving threat landscape and maintain their edge in exposure management. |
| **Managed** | Managed security controls offer a high level of protection against a wide range of threats, significantly reducing the risk of successful attacks. Organizations at this level should maintain their strong security posture, regularly assess the effectiveness of their controls and address identified gaps in their exposure management. |
| **Moderate** | Moderate security controls provide a reasonable level of protection against various threats. Organizations at this level should continue to refine their security controls and consider additional measures to further reduce their threat exposure. |
| **Basic** | Basic security controls offer limited protection against a narrow range of threats. Organizations at this level should invest in enhancing and expanding their security controls to keep building a more effective threat exposure management program. |
| **Inadequate** | Inadequate security controls provide almost no protection to a very minimal level of protection against threats, leaving the organization highly vulnerable to attack. At this level, only a few basic security measures are in place. Organizations with this level of exposure need to urgently review and improve their security posture. |

# Overall Prevention and Detection Effectiveness Performance

This yearʼs report reflects a mixed landscape for organizations attempting to prevent and detect cyber attacks. While certain metrics held steady or showed incremental improvement, others signaled areas of real regression. The drop in prevention effectiveness, combined with stagnant detection performance, suggests that many organizations are struggling to maintain hardened defenses in the face of a growing volume of sophisticated threats. Itʼs a reminder that security controls are not set-and-forget tools. They degrade over time and require continuous validation to remain effective.

## Prevention Effectiveness

In 2025, the prevention effectiveness score declined to 62%, down from 69% in 2024. This marks a reversal of last yearʼs significant 10-point gain, where scores had improved from 59% in 2023. This yearʼs slip backward suggests that many organizations are now falling behind on maintaining and fine-tuning their security controls. While 62% still represents the ability to block nearly two-thirds of simulated attacks, the decline highlights how quickly and easily defenses can degrade without continuous oversight.

The findings reinforce the importance of continuous exposure validation and real-world attack simulation to remain operationally effective against evolving threats.

## Detection Effectiveness

In 2025, the detection effectiveness scores showed only modest recovery and remain a critical area of concern. The log score held steady at 54%, meaning nearly half of attacker behaviors are still not logged in most environments. While the alert score increased slightly from 12% to 14%, this still indicates that less than 1 in 7 attacks generate a meaningful alert. For most organizations, this level of performance is far below what's needed for timely detection and effective response.

The stagnation in logging coverage is concerning, as it reflects persistent weaknesses in the foundational layer of the detection pipeline. Without full visibility into attacker activity, no amount of analytics or correlation can compensate. At the same time, the low alert rate reinforces that even when logs are captured, they are often not correlated, prioritized, or escalated effectively, leaving threats undetected and security teams uninformed.

This growing gap between what is logged and what is alerted highlights systemic issues in detection engineering. Many organizations are still operating with ineffective detection pipelines that are prone to silent failure, either because telemetry never reaches the SIEM or because detection logic fails to trigger relevant behaviors.

To address these issues, organizations need to move beyond basic telemetry collection and invest in validating the entire detection lifecycle. This includes not only verifying log availability and quality but also testing whether detection rules are functioning as intended and whether they generate high-fidelity alerts in response to real-world attacker behaviors. Without these validations, organizations risk overestimating their detection capabilities and underestimating their exposure.

## Addressing the Gaps

Once again, our findings reveal a troubling pattern: many organizations believe their controls are working until they're tested. This false sense of security stems from an overreliance on dashboards, static metrics, and assumptions that logging equates to visibility or that prevention implies protection. In reality, security controls degrade over time due to configuration drift, tool misalignment, software updates, new adversary techniques, and evolving infrastructure. Without continuous validation, these failures stay hidden until it's too late.

> Log collection is essential, but not enough for effective detection.

The flatlining log score and persistently low alert score expose this illusion. Collecting telemetry is not the same as understanding it, and logging alone does not guarantee that threats will be detected, prioritized, or acted upon. Likewise, even high-performing prevention controls can degrade if not regularly tested against modern threats. In many cases, what appears to be protection is merely a lack of visibility into successful bypasses.

To close these gaps, organizations must adopt an "assume breach" mindset that assumes failure is possible at every layer of defense and seeks to find it before adversaries do. This means regularly testing whether logs are complete, detection rules are firing, alerts are being generated, and controls are blocking attacks in real-world conditions. It also means challenging assumptions, removing reliance on static assessments, and integrating exposure validation into daily security workflows.

# Real-World Performance of Cybersecurity Products

Cybersecurity products are often evaluated in controlled test environments using curated attack scenarios, tightly defined metrics, and ideal configurations. Benchmarks like ATT&CK® Evaluations offer valuable insight into a productʼs potential, but they do not reflect the full complexity of production environments, where configuration drift, integration friction, and operational constraints can significantly impact outcomes. This yearʼs findings reinforce this persistent reality: strong performance in a lab does not guarantee effectiveness in production.

Even security solutions that achieve 100% prevention and detection scores in lab tests often exhibit inconsistent effectiveness once deployed. This isnʼt because the products lack potential. Itʼs because they are rarely deployed or maintained under ideal conditions.

![Chart showing Prevention Score and Detection Score variability in real-world environments](./images/real-world-performance-chart.png)

Our analysis shows that control degradation is more common than most teams realize. Security tools that were properly installed and configured at deployment may fail over time due to:

- **Configuration drift**: Policy changes, software updates, and integration rollouts gradually alter how tools behave.
- **Broken integrations**: A misconfigured log source or disabled alerting rule may render a detection pipeline ineffective without anyone noticing.
- **Operational complexity**: Each organization has a unique mix of systems, staffing levels, compliance requirements, and network architecture. These variables can significantly impact product effectiveness.
- **Dynamic threats**: The threat landscape evolves constantly. Products must be regularly tested and updated to keep up with new TTPs. Static signatures and stale configurations quickly become obsolete.

Itʼs not uncommon for security teams to assume that a product is working simply because it exists in the stack. But presence is not proof of performance. Without validation, thereʼs no way to confirm whether a detection rule triggers, whether a prevention control actually blocks a live threat, or whether an alert is ever escalated.

This disconnect between expected and actual performance results in unseen exposure, even within well-resourced security programs. To ensure cybersecurity investments deliver their intended value, organizations must recognize that security products require continuous maintenance, not one-time deployment.

We recommend:

1. **Treat evaluations as guidance, not guarantees.**
   MITRE ATT&CK® Evaluations and other independent tests offer valuable starting points. But they must be validated in your own environment, with your configurations, controls, and constraints.
2. **Expect degradation and plan for it.**
   Even the best tools lose effectiveness without maintenance. Routine validation is the only way to detect control drift and silent failures before attackers do.
3. **Make continuous validation part of your workflow.**
   Use simulated attack scenarios to test both prevention and detection capabilities in context. Confirm that controls behave as expected, that alerts are generated, and that response processes activate when they should.

# Uncovering Critical Defensive Gaps with Automated Penetration Testing

Automated penetration testing remains a vital capability for uncovering real-world weaknesses across enterprise environments. Leveraging the Picus Attack Path Validation (APV) module, organizations can emulate full-chain adversarial behavior starting from initial access and credential compromise to lateral movement and privilege escalation without requiring red team resources or intrusive manual efforts.

This yearʼs findings from Picus APV assessments show clear progress in infrastructure hardening. In 2025, only **19 percent** of simulations resulted in full domain administrator compromise, down from 24 percent in 2024, indicating more effective lateral movement defense, tighter network segmentation, and broader adoption of exposure validation practices.

Additionally, domain administrator access was achieved in **22 percent** of tested environments, a significant improvement from 40 percent the previous year. In other words, fewer than one in four organizations had a viable attack path to full domain compromise. While this marks meaningful progress, the fact that nearly a quarter of environments still contain exploitable privilege escalation paths highlights the ongoing need for continuous validation and targeted remediation.

Despite improvements in overall infrastructure resilience, password cracking success rates increased dramatically. In **46%** of APV simulations, attackers were able to crack at least one dumped password hash and obtain valid credentials, up from 25% in 2024. This rise points to persistently weak password policies and outdated hashing algorithms, especially in internal domains where complexity requirements, rotation policies, or multi-factor protections may be inconsistently applied. In many scenarios, a single cracked credential triggered a chain of lateral movement events that led to broader exposure. These findings emphasize that even with better segmentation and endpoint visibility, compromised credentials remain a fast track to privilege escalation.

Organizations must complement hardening efforts with:

- Stronger password complexity and rotation policies
- Elimination of legacy or deprecated hashing methods
- Regular validation of credential exposure through simulated attacks

# Detection Rule Effectiveness

Detection rules serve as the core logic layer of threat detection. When properly written, validated, and maintained, they allow SIEM and EDR platforms to raise meaningful alerts from massive volumes of telemetry. However, our analysis of detection rules reveals that many organizations still struggle with rule reliability, precision, and operational readiness. This yearʼs findings highlight a familiar pattern: log source issues remain the dominant root cause of rule failure, but configuration and performance issues also continue to silently undermine detection capabilities across the board.

The most common and high-impact failure point in 2025 was **Improper Log Source Coalescing**, affecting 21% of assessed rules. This problem occurs when event coalescing is enabled for specific log sources such as DNS systems, proxy servers, Windows servers, and endpoints, leading to data loss. When critical threat behaviors are compressed or dropped, detection logic becomes partial, delayed, or entirely ineffective.

**Unavailable Log Sources** accounted for 9% of issues, often resulting from telemetry pipeline disruptions, misconfigured forwarding agents, or network segmentation. Together with **Inactive Log Source Usage** (5%) and **Broken Log Source** connections (5%), these issues collectively account for nearly 20% of failures and represent a persistent visibility gap that detection teams must address urgently.

Beyond logging gaps, configuration-related issues such as **Empty Reference Sets** (7%), **No Log Source Field Usage** (6%), and **Wrong Rule Configuration** (3%) continued to impact rule integrity. These failures often stem from a drift between detection content and infrastructure changes, resulting in rules that exist but silently fail to trigger in production.

In 2025, performance-focused issues were also evident. For instance, **Not Starting Cost-Effective Test Filters** (8%) and **Wide-Ranging Custom Property Definitions** (8%) were among the top issues affecting rule performance and scalability. These overly broad configurations consume excessive processing power, slow down query response times, and often lead to alert fatigue due to imprecise matches.

The dataset for these statistics is sourced from Picus Detection Rule Validation (DRV), which leverages a continuously updated checklist to identify and categorize over 50 recurring issues in detection rules. This yearʼs findings once again highlight the operational fragility of SIEM detection pipelines.

Log collection issues accounted for **50%** of all detection rule failures, reinforcing that visibility gaps remain the single largest barrier to effective detection. In addition, performance-related problems (24%) and configuration errors (13%) continue to impact detection quality, precision, and scalability.

Together, these categories represent the majority of rule failures observed this year. The findings emphasize the need for continuous validation, fine-tuning, and regular updates to maintain detection rule effectiveness. By addressing these systemic weaknesses, security teams can dramatically improve the reliability and responsiveness of their detection infrastructure.

# Performance by Industry

In