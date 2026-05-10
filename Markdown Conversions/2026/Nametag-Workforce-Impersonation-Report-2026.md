# Rebuilding Trust in the Age of AI: The 2026 Workforce Impersonation Report

How AI-enabled impersonation is redefining identity security and shaping the future of enterprise trust.

## Table of Contents
- [Introduction](#introduction)
- [Six Workforce Impersonation Trends](#six-workforce-impersonation-trends)
- [Deepfakes & Generative AI](#deepfakes--generative-ai)
- [Helpdesk Social Engineering](#helpdesk-social-engineering)
- [MFA Bypass & Interception](#mfa-bypass--interception)
- [Phishing & Vishing](#phishing--vishing)
- [North Korean IT Workers](#north-korean-it-workers)
- [Agentic AI Misuse](#agentic-ai-misuse)
- [Understanding The Identity Assurance Gap](#understanding-the-identity-assurance-gap)
- [Solutions to Workforce Impersonation](#solutions-to-workforce-impersonation)
- [Combating Workforce Impersonation](#combating-workforce-impersonation)

---

## Introduction
Trust itself is now a primary target. Enterprise security strategies must adapt.

In 2025, a growing number of breaches began with someone pretending to be a legitimate member of the workforce. Nearly every major breach now carries an element of impersonation. Across industries, attackers are impersonating trusted insiders to access systems, people, and data, and legacy trust models are failing.

What once required special skills and resources is now available to anyone with access to AI tools like ChatGPT or Sora. Generative AI has fully blurred the line between real humans and deepfake clones, making it easier than ever for bad actors to convincingly impersonate others. We can no longer trust what we see, hear, or read, or even that someone is a real human.

In healthcare, attackers pose as clinicians or hospital staff to request password or MFA resets, gaining access to internal systems and patient records. In higher education, fraudsters are enrolling as "ghost students" to access academic resources and steal financial aid. Across SaaS and technology companies, bad actors pretend to be legitimate job candidates, current employees, or outside contractors so they can get hired or socially engineer an account recovery. Transportation and logistics organizations report bad actors disguising themselves as drivers, dispatchers, or vendor contacts to infiltrate distributed networks and redirect operations or payments.

Taken together, these incidents show that traditional device and credential authentication can’t keep pace with generative AI and deepfake driven impersonation. To protect their companies, IT and security teams will need to look for systems, technologies, and processes that verify people.

---

## Six Workforce Impersonation Trends
### Six Workforce Impersonation Trends Shaping Enterprise Security Strategies in 2026
Adversaries have learned to look, sound, and act legitimate to bypass traditional defenses.

Deepfakes make it easy to steal anyone’s voice or likeness. Social engineering scripts are being upgraded with generative AI. MFA bypasses and phishing proxies have evolved into precision tools for scalable session hijacking. Entire nation states are engaged in massive hiring fraud schemes. And autonomous AI agents are introducing an entirely new class of impersonation risk.

Together, these threats reveal how impersonation has become a linking thread across a wide range of attacks. This reveals a shift from credential-based compromise to identity-layer compromise, where trust itself is the target. Understanding how these threats are evolving is the first step toward restoring confidence in the people, processes, and systems we rely on.

> **ACCORDING TO GARTNER:**
> “As adoption accelerates, attacks leveraging GenAI for phishing, deepfakes and social engineering have become mainstream, while other threats – such as attacks on GenAI application infrastructure and prompt-based manipulations – are emerging and gaining traction.”
> — Akif Khan, VP Analyst at Gartner
> *Gartner Press Release, “Gartner Survey Reveals GenAI Attacks Are on the Rise”, Gartner – September 22, 2025*
> *GARTNER is a trademark of Gartner, Inc. and/or its affiliates.*

---

## Deepfakes & Generative AI
### Threat Summary
Deepfakes are synthetic audio, video, and image content created or manipulated by generative AI. What once required technical skills and high-quality source material became mainstream in 2025 with rapid improvements in accessible deepfake tools. Bad actors can now combine text-based AI tools like ChatGPT with AI video and photo generators like Sora 2 to convincingly impersonate others in dynamic, living scenarios that are virtually indistinguishable from reality.

Deepfakes make it substantially easier for bad actors to carry out their impersonation attacks, including helpdesk social engineering and hiring fraud. According to Gartner, 62% of organizations have experienced a deepfake attack in the past 12 months. IT and security teams should think in terms of how a bad actor might use deepfakes (and generative AI more generally) to impersonate someone in a particular communications channel or identity verification process.

### Example Incident
In early 2025, a Singaporean company almost lost $500,000 when a finance director was contacted via WhatsApp by scammers impersonating the CFO. The director joined a video conference where imposters used deepfakes to impersonate senior executives. The incident came a year after British engineering firm Arup lost $25 million to a scheme wherein a finance employee joined a video conference with what appeared to be the company’s CFO and senior colleagues. Investigators later confirmed that every participant on the call was deepfaked.

### 2026 Prediction
Criminals will commercialize "Deepfakes as a Service" (DaaS) kits, further lowering the barrier to entry. These kits will include advanced deepfake injection capabilities designed to trick identity verification systems by inserting false media directly into the data stream; many consumer-grade identity verification systems prove unable to reliably detect injected deepfakes. The ensuing fallout will result in a wholesale shift in enterprise trust models away from static visual checks and AI-based deepfake detection towards continuous, hardware-attested identity verification.

---

## Helpdesk Social Engineering
### Threat Summary
Helpdesk social engineering attacks target one of the most vital human interfaces in an organization: the IT support desk. Attackers pose as employees or contractors, using stolen credentials, publicly available personal information, and deepfake voice clones to trick helpdesk staff into resetting a victim’s password or MFA. After gaining access to the victim’s account, the bad actor performs reconnaissance, escalates privileges, steals data, and deploys ransomware.

In 2025, led by Scattered Spider, breaches traced to helpdesk social engineering saw a resurgence which will continue in 2026. Employee helpdesks and customer support centers are particularly vulnerable to social engineering because agents don’t have an effective way to verify the person on the other end of a phone call, chat, or support ticket.

### Example Incident
In early 2025, UK retailers Marks & Spencer and the Co-op Group experienced major disruptions after attackers socially engineered helpdesk representatives at a third-party service provider into resetting credentials for privileged accounts. The attacks, attributed to Scattered Spider, were estimated to cost nearly $600 million and followed similar attacks against Harrods, Transport for London (TfL) in 2024, and MGM Resorts International and Caesars Entertainment in 2023.

### 2026 Prediction
In 2026, deepfake impersonation (voice and video) will become a standard tactic in helpdesk social engineering playbooks. Solutions which rely on traditional authentication factors to verify users will fail to stop these attacks, leading organizations to equip their helpdesks with identity verification tools instead. Attackers will target more managed service providers (MSPs) whose helpdesks grant access to multiple downstream clients, pressuring MSPs to increase security.

---

## MFA Bypass & Interception
### Threat Summary
Multi-factor authentication (MFA) remains a critical, baseline security control, but adversaries have developed numerous reliable workarounds. A survey conducted by Portnox found that 96% of CISOs believe MFA “can’t keep up with today’s threat landscape.” Common tactics observed in 2025 include push notification (“push fatigue”) attacks; SIM swap attacks that move a victim’s phone number to an attacker’s device; and adversary-in-the-middle (AitM) techniques which steal authenticated session tokens.

### Example Incident
In early 2025, researchers uncovered a large-scale AitM campaign to intercept MFA challenges and steal valid Microsoft 365 session tokens. Later in the year, investigators found that threat actors were quietly harvesting OAuth tokens through malware and browser-based session hijacking, letting them replay authenticated sessions.

### 2026 Prediction
In 2026, successful MFA downgrade attacks which target humans and processes to bypass phishing-resistant MFA and passwordless factors will lead more organizations to implement a policy of using identity verification to upgrade security during MFA resets. Adversaries will combine MFA interception with MFA bypass in multi-stage campaigns to defeat mixed deployments. Hardening of the processes surrounding MFA will be key.

---

## Phishing & Vishing
### Threat Summary
Phishing and vishing (voice phishing) is the act of sending messages claiming to be from a trusted individual or company. In 2025, phishing attacks remained one of the most common forms of impersonation. 2025 saw an increasing shift towards AI-assisted polymorphic phishing campaigns and a diversification of channels; 34% of phishing attacks now come through non-email channels.

### Example Incident
In August 2025, researchers at Group-IB revealed an advanced vishing campaign wherein attackers posed as recruiters from major tech companies, using deepfake voice clones in follow-up calls after phishing emails. Victims were persuaded to download “application forms” that delivered credential-stealing malware.

### 2026 Prediction
In 2026, scalable, AI-personalized spear phishing kits will render traditional phishing cues nearly useless. Criminals will operationalize hybrid phishing campaigns using AI-generated text, voice, and video messages to launch individually-personalized attacks en masse. Organizations will begin implementing policies which require out-of-band authentication, using peer-to-peer verification solutions.

---

## North Korean IT Workers
### Threat Summary
Thousands of operatives working for the Democratic People’s Republic of Korea (DPRK) have infiltrated companies around the world through remote IT jobs. Their goal is to collect paychecks, steal source code, and exfiltrate data. They frequently use generative AI and deepfakes to mask their true identities.

### Example Incident
In July 2025, an American woman was sentenced to over 8 years in prison for her role operating a “laptop farm” on behalf of North Korean IT workers. The particular ring had reportedly breached more than 300 American companies and government agencies. It’s estimated that fake IT workers have funneled up to $1 billion to the DPRK regime.

### 2026 Prediction
In 2026, regulatory crackdowns and mandatory identity verification requirements will reshape hiring security. Enterprise HR departments and freelancer platforms will adopt policies of mandatory identity verification for job applicants, with re-verification at IT onboarding.

---

## Agentic AI Misuse
### Threat Summary
Agentic AI are autonomous software agents that can reason, plan, and act without direct human prompts. In 2025, AI agents became a first-class identity. For security teams, agentic AI is a serious new threat. If an attacker compromises an agent identity or manipulates its decision logic, they can initiate legitimate-looking actions that bypass human oversight.

### Example Incident
In August 2025, Anthropic revealed that attackers used its Claude Code tool to automate an entire data-extortion campaign with only minimal human input. Months later, the company uncovered what appeared to be the first AI-run espionage operation.

### 2026 Prediction
In 2026, more breaches stemming from over-permissioned AI agents will lead agentic identity governance to become a board-level and compliance priority. Standard policy will require verified human signatures for risky actions performed by AI agents on behalf of humans.

---

## Understanding The Identity Assurance Gap
Workforce impersonation works for a simple reason: most authentication methods verify access or ownership, not identity. The identity assurance gap is the fact that most organizations don’t know who is actually behind any given account, device, or action.

> "Insider threats are evolving faster than most people realize; economic uncertainties and AI tools are combining to create the perfect storm. The reality is that many companies don't actually know who they're hiring and onboarding."
> — Chris O’Rourke, Senior Manager, Cloudforce One - R.E.A.C.T., Cloudflare

---

## Solutions to Workforce Impersonation
### Phishing-Resistant MFA
Passwordless authentication factors like device-bound passkeys and physical security keys are widely regarded to be the most secure. In 2026, we expect phishing-resistant authentication will become a baseline requirement. However, any authentication factor is only as secure as its recovery process.

> "To deliver the maximum value from their MFA solutions, companies must replace existing, phishable processes for registration and recovery with easy-to-use, self-service and highly secure alternatives."
> — Derek Hanson, Field CTO, Yubico

### The Limits of Video Verification
Video calls create a false sense of security and should not be trusted. Live video deepfake filters are available on GitHub and their quality is improving rapidly. If someone is unable or unwilling to complete identity verification, require them to come in-person.

### Workforce Identity Verification
To cover the identity assurance gap, organizations are increasingly turning to workforce identity verification (IDV).
![Diagram showing the IDV process: Verify your identity, Open, Scan your ID, Take a selfie, All set!]

---

## Combating Workforce Impersonation
In 2026, attackers won’t rely on sophisticated exploits; they’ll rely on looking and sounding like the people your systems already trust. Closing the identity assurance gap will require a fundamental shift in how organizations think about workforce identity.

High-risk events—hiring and onboarding, device enrollment and replacement, account recoveries, role and privilege changes, high-value approvals, and oversight of AI agents—all demand higher assurance. That means verifying that the right human is behind the keyboard, phone, or AI agent.

Organizations that adapt will make the shift from periodic identity checks to continuous identity assurance, embedding workforce identity verification into the places where trust matters most.

Visit [getnametag.com](http://getnametag.com) to learn more.