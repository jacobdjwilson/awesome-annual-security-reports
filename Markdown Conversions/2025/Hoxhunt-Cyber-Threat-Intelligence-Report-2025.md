# Cyber Threat Intelligence Report 2025

## Table of Contents
- [Executive Summary & Introduction](#executive-summary--introduction)
- [Threat Landscape Overview](#threat-landscape-overview)
- [Human Risk Findings](#human-risk-findings)
- [Campaigns, Tooling and Environments Research](#campaigns-tooling-and-environments-research)
- [Strategic Guidance](#strategic-guidance)

---

## Executive Summary & Introduction

While AI-generated voice and video deepfakes dominated headlines and discussions in the cyber community in 2025, these attacks accounted for a fraction of the threats that bypassed filters and actually reached employees. The vast majority of attacks leveraged more traditional impersonation and deception techniques that have been updated to trick filters and slide into new communication environments, including social media.

Sometimes developments in the threat landscape were enhanced by AI and sometimes not. Their effectiveness was fueled by familiarity, not visibly slick deception and sophistication. The new generation of attacks imitated normal business processes, credible brands, trusted tools and everyday communication patterns.

### 3 key developments

*   **First**, attackers are using AI to improve classic phishing techniques with cleaner language, more convincing formatting and more believable workflow mimicry.
*   **Second**, adversary-in-the-middle (AitM) phishing kits have become easier to deploy and are becoming more widely adopted. These toolkits intercept logins in real time, forward the authentication to the legitimate service, and capture session tokens in addition to passwords. AitM attacks can circumvent MFA.
*   **Third**, social engineering is increasingly expanding beyond email environments and moving into social platforms, recruitment channels and other communication layers that shape professional identity.

### Updating Your Security Awareness and Defense Playbook

Overall, the findings imply a steady shift toward stealth, automation, and token-based compromise. Defenders should assume that attackers can bypass common filters and instead focus on detecting anomalies after login, binding tokens to devices, and shortening session lifetimes.

The development of error-free phishing messages reinforces the need for behavioral training that teaches employees to question routine, not just urgency and errors. Awareness programs should emphasize routine-looking lures over sensational ones, while technical teams implement token-centric incident response and phishing-resistant MFA. Finally, every organization should reinforce a “Pause → Verify → Act” culture that treats ordinary requests with the same caution reserved for high-urgency scams.

---

## Threat Landscape Overview

### Top Social Engineering Tactics

Attackers mimic familiar workflows and exploit urgency and authority.

**Top entities impersonated**
- Microsoft
- Human resources
- Supply chain third parties

**Top emotions exploited**
- Urgency
- Curiosity
- Trust
- Approval
- Reward-seeking

![Example of a voicemail-themed Microsoft impersonation]

Age-old tactics remain effective and have continued to evolve over the past year, with themes such as Microsoft impersonations still among the largest campaigns observed by Hoxhunt’s analysts. Attackers commonly utilize a security alert theme, exploiting urgency, or claim a new voicemail transcript is available to exploit curiosity.

---

## Human Risk Findings

### Generative AI and Phishing Visuals

Lately, the visual outlook of common bulk phishing has shifted from minimal, unformatted emails to more refined templates with branding elements and structured layouts, with timing that aligns with the increasing quality and availability of generative AI tools.

![Microsoft impersonation utilizing a security alert theme from 2025]

Although newer emails look more polished, improved visuals do not necessarily make a campaign appear more legitimate. In fact, the simpler “full mailbox” alert from 2023 more closely mirrored genuine Microsoft notifications, appearing more authentic than the newer, more elaborate version.

### Top Techniques

#### Attachment types
In 2025, PDF attachments remain the top file type used in attachment-based phishing, accounting for 23.7% in the first half of the year.

![Top 5 attachment types of 2025 compared to their shares in 2024]

#### On the rise: SVGs
In 2025, attacks utilizing SVG attachments saw a 50-fold increase in volume compared to 2024. SVGs appear as harmless graphic files and bypass many anti-spam email tools, making them an attractive technique to attackers.

---

## Campaigns, Tooling and Environments Research

### Microsoft vs. Google: Environment Analysis

This section details findings from comparing emails reported by users of Microsoft environments with those reported by users of Google environment in H1 2025.

| Metric | Google | Microsoft |
| :--- | :--- | :--- |
| % of reported emails confirmed malicious | 34.7% | 12.1% |
| Top sender domain | gmail.com (17.9%) | gmail.com (30.1%) |

### Meta Campaign Comparisons – Two killchains, one goal

This section highlights two attack examples: (1) a recruitment-themed Meta impersonation, and (2) an Instagram impersonation alleging ad-account suspension due to policy violations.

![Parallel killchain tracks aligned to one objective]

### Phishing Kits 2025

During 2025, phishing kit developers standardized adversary-in-the-middle (AitM) techniques, professionalized their tooling, and focused on stealth over splash. Kits increasingly capture session tokens in addition to passwords, reduce visible page tells, and support faster post-compromise automation.

---

## Strategic Guidance

### Top 5 Actions for Security Practitioners

1.  **Pause before acting**: Institutionalize brief pauses for context checks, particularly for sensitive requests or routine workflows.
2.  **Raise authentication assurance**: Require phishing-resistant factors for high-risk roles and restrict unreviewed OAuth/app consents to reduce token-grant exposure.
3.  **Publish & enforce trusted channels**: Define the approved services for signing, sharing, scheduling, and paying, and route anything else through known portals until verified.
4.  **Handle attachments by behavior**: Preview before action and assess the request (links, forms, credential capture, payments) rather than relying on the file type alone.
5.  **Embed business-process guardrails**: Require verified callbacks and two-person approvals for payments or bank-detail changes, and do not permit approvals by email.

### CISOs: Priorities and Risk Comms

- **Turn intel into action**: Use this year’s findings to drive simulations and training on what actually lands in inboxes.
- **Personalize by role and region**: Favor solutions that auto-target by latest threats, org landscape, and geography at scale.
- **Retire outdated advice**: Drop “look for typos” and “be wary of links.” Teach *Pause → Verify → Report*.
- **Keep workflows & tools private**: Remove process docs, portal URLs, and tool names from public pages to raise attacker effort.
- **Make dwell time a KPI**: Encourage fast reporting and track two metrics quarterly: report rate and time to report.

---

, mirror social platform
killchains. Emphasize the “small ask →
bigger ask” escalation.

✔ Build a modern GenAI literacy module.
Show side-by-sides of older vs. newer
templates, the 2×2 HTMLtable Microsoft
logo trick, and failed personalization tokens
like “##victimdomain##.” Reframe flawless
language as something to question.

47

Cyber Threat Intelligence ReportStrategic Guidance ✔ Teach third-party sender
baselines. Walk through what
common third-part service use
(Salesforce, Docusign…) looks like in
your organization and when to report
variances.

✔ Measure “routine skepticism”.
Track whether people escalate or
verify when a message looks internal
but arrives via a third-party sender,
and how quickly routine-looking lures
get reported.

✔ Change culture with managers.
Managers can help implement the
Pause → Verify → Act model and create
a culture where blameless reporting,
even after a click, is encouraged.

Start / Continue / Stop

Start: Designing multi-
message and fake thread
simulations

Continue: Reinforcing “pause
when it feels like routine”
and encouraging blameless
reporting.

Stop: Over-emphasizing
grammar, typos and heavy
urgency as primary cues:
teach employees to question
routine requests too.

SOC / IT / Defender: Controls, Detection and IR

Attackers are leaning on legitimate
services to reach inboxes; gmail.com is the
single most common sending domain
in malicious phishing reports during H1
2025. Third-party service misuse is also
notable. SVG attachments matter now.
Outlook for the web and the new Outlook
for Windows no longer display inline
SVG as of September–October 2025; SVG
attachments still arrive, and their share
rose from negligible to ~5% of attachment-
based phishing. Links might route via t.co
and google.com/url and Dropbox remains a
popular document-share destination within
phishing flows. Treat these destinations
as resolvable, not inherently safe. Reverse-
proxy kits and browser-in-the-middle

workflows make token theft scalable.
Defenses need to assume session theft
rather than just password theft.

Checklist:

✔ SVG attachments. Consider blocking
or quarantining image/svg+xml by default
and introducing an exception path. When
exceptions are granted, inspect SVG DOM
for scripting, xlink:href, and data: URIs.

✔ QR-in-attachments pipeline. Extract QR
codes from PDFs/images/SVGs and resolve
targets inside a sandboxed redirect resolver
at click-time.

48

Cyber Threat Intelligence ReportStrategic Guidance ✔ Thirdparty sender posture. Add
mailflow analytics for often misused
domains like salesforce.com and docusign.
net. Consider extra scrutiny for noreply@
salesforce.com given it’s often abused.
Prefer per-business-unit allowlists over
global ones.

✔ Redirect handling. Expand common
redirecting URLs like t.co and google.
com/url chains in a sandboxed resolver at
click-time and make decisions on the final
eTLD+1, not the intermediary.

✔ “Fake-thread” heuristics. Alert when
In-Reply-To/References claim a thread
the tenant has never seen, or when
a message reads as internal but the
MessageID domain is external. Start
in audit mode to tune for legitimate
edge cases.

✔ Identity hardening for AitM
reality. Move admins and high-risk roles
to phishing-resistant MFA (passkeys/
FIDO2). Bind tokens to devices (e.g.,
Token Protection (Entra CA) for refresh/
app tokens) and enable Automatic Attack
Disruption; shorten session lifetimes
for sensitive apps. Add hunts for same
session ID from different IPs, midsession
user agent pivots, mailbox rule creation
or MFA changes shortly after login, and
automatically revoke tokens and sign out
on detection. Favor detections that score
interaction/proxy artifacts over fragile DOM
lookalikes; these help against noVNC/
browserinthemiddle kits.

✔ Marketing / business platform
guardrails. Enforce SSO + phishing resistant
MFA for Meta Business accounts and other
similar services and centralize ownership.

Start / Continue / Stop

Start: 1) Token-centric incident response: on suspicious post-login
changes, revoke tokens first and then reset credentials. 2) Fake-thread
heuristics and tighter posture for commonly misused third-party services.

Continue: Tight conditional access and session control (CAE, shorter
token lifetimes) and steady expansion of phishing-resistant MFA.

Stop: 1) Treating google.com or t.co links as low risk purely because of
brand familiarity. 2) Relying on DOM/image look-a-like signatures as
primary controls: modern kits randomize and obfuscate aggressively.

49

Cyber Threat Intelligence ReportStrategic Guidance We invite you to share your
thoughts and insights
on the evolving threat
landscape. Your perspective
is invaluable in enhancing our
collective understanding and
preparedness!

For further discussion or to learn more,
please contact the Threat Operations
team at threat.ops@hoxhunt.com.

Stay ahead of emerging
threats and empower your
people to become your
strongest line of defense.

Schedule a demo to see how Hoxhunt
can elevate your security readiness.

WWW.HOXHUNT.COM