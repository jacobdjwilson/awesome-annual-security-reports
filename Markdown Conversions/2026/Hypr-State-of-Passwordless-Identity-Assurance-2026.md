# The State of Passwordless Identity Assurance 2026

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Section 1: AI-based Attacks](#section-1-ai-based-attacks)
- [Section 2: Phishing-resistant Adoption Trends](#section-2-phishing-resistant-adoption-trends)
- [Section 3: The Rise of Identity Verification](#section-3-the-rise-of-identity-verification)
- [Conclusion](#conclusion)
- [Appendix: About](#appendix-about)

---

## Foreword
### The Age of Industrialization
History rarely moves in straight lines. We tend to romanticize transformational eras by their singular breakthroughs: the lightning-bolt inventions that redefine the possible. But the more nuanced reality is, the slower, messier, and far more deliberate is the work of shaping innovation into systems that can scale.

The steam engine and the mechanized loom arrived in bursts of genius, but it took decades to architect the factory systems, safety standards, and global chain supplies that made them world-altering. Innovation makes change imaginable; industrialization makes it real. Identity is at that inflection point today.

Last year, we described an Identity Renaissance: a fundamental pivot away from the shared secrets and outdated authentication models of the past, and toward a more accurate understanding of identity as assurance of the person, not just the credential. The data provided the cutting criticism we needed: Identity vulnerabilities are driving the majority of breaches. Phishing-resistant authentication is more effective than traditional MFA. Attackers aren’t breaking in; they’re logging in.

Over the past year, our industry has moved from recognition to understanding. Security and identity leaders became more precise about what phishing resistance means. You evaluated passkeys, hardware-backed authentication, and identity verification with greater technical clarity. You mapped workflows and challenged legacy assumptions. And then, to the outside observer, progress appeared to slow.

That pause is not a retreat; it is a transition into the high-stakes work of industrial-grade execution. Identity is not a stand-alone control to be deployed once or optimized for a single use case. It is the connective tissue of the enterprise, spanning onboarding to account recovery, cloud infrastructure to help desk. It crosses the silos of HR, IT and Security. As a security leader, you know that scaling identity without discipline risks replacing one kind of fragility with another.

We have entered the Age of Industrialization. This is where innovation is tested by reality. Industrialization demands:
- **Intuitive User Experience**: Moving beyond the pilot to a repeatable system that prioritizes the user across all workflow paths.
- **Governance**: Integrating identity with HR, IT, Legal, and Security, allowing the system to react naturally and in real time.
- **Operational Efficiency**: Surfacing the legacy dependencies and organizational seams that keep overhead and maintenance costs from exposing a brittle system.

The lesson from history is clear: Breakthroughs ignite change, but systems are what sustain it. Today’s most resilient enterprises are acting on that lesson. They are slowing down to understand their full set of use cases. They are aligning teams that have historically operated separately. They are designing identity programs meant to scale correctly, not just quickly. The urgency remains blazing. AI-driven phishing, vishing and deepfakes are accelerating identity abuse at an alarming speed. Partial solutions and rushed, fragmented rollouts no longer provide meaningful protection.

This year’s State of Passwordless Identity Assurance report reflects this shift. It captures an industry that has had its breakthroughs and is now doing the harder work of turning insight into real change.

The Renaissance brought awareness. The Enlightenment brought understanding. Industrialization is where we finally win at scale.

Bojan Simic
HYPR CEO

---

## Introduction
The sixth annual State of Passwordless Identity Assurance report, commissioned by HYPR and produced by 451 Research from S&P Global Energy Horizons, demonstrates organizations are moving from identity awareness to understanding, but have not yet achieved broad, enterprise-wide execution.

Organizations have gained a clearer view of identity threats, phishing-resistant authentication and the importance of identity verification. However, the surge in adoption noted in our prior survey has stalled as early-adopter enthusiasm has waned. Deployments have also largely targeted specific use cases and user personas rather than being company-wide, and the same trend largely applies to identity verification (IDV). There are a host of potential reasons for this, including cost, compatibility, internal budget dynamics, deployment complexity, regulatory concerns and, most of all, a growing recognition of the requirements for enterprise-scale identity transformation.

Bridging this gap between awareness and execution marks the transition into the next chapter. We are entering the “Age of Industrialization,” where the insights gained during identity’s “Age of Enlightenment” are finally put into practice. The goal is to operationalize identity security at scale. This requires moving beyond the simple login to securing every touchpoint where identity is involved, from hiring and onboarding to sensitive application access, account recovery, device replacement and help desk interactions. The industry has moved past the “discovery” phase; enterprises no longer question what works but must now focus on universal execution and broader integration across the entire organizational structure.

---

## Key Findings
- **AI-driven attacks are the top security concern**: Generative AI and agentic AI have become the top identity security concerns. They are not only rearming existing threats such as phishing and ransomware but also creating new attacks, including deepfakes and employee impersonation fraud.
- **Passwordless adoption — more clarity but less action**: Respondents notably demonstrated increased clarity about the precise meaning of phishing-resistant and passwordless authentication methods compared to the 2025 study. Yet this understanding hasn’t directly translated into action; the spike in passwordless adoption observed in last year’s survey has plateaued.
- **Bridging the gap from pilot to production is critical**: Though passwordless adoption has stalled, plans remain positive. Respondents have more pilot projects for passwordless authentication than for any other method, and a large percentage still plan to deploy passwordless tools within the next two years.
- **Identity verification is a “must-have,” but usage is still fragmented**: IDV is the second most-deployed identity management tool and a key response to breaches. However, IDV is still primarily used for a narrow range of internal use cases and user personas.

---

## Section 1: AI-based Attacks
### AI has generated a new industrial ecosystem of identity-based attacks
While cybersecurity investments have steadily increased, the breach trajectory continues to steepen — a paradox driven by the fact that identity remains the primary vector for modern attacks. Generative and agentic AI offer unprecedented efficiency in automating identity governance while simultaneously enabling adversaries to execute sophisticated, identity-based attacks at a velocity and scale that threatens to outpace manual defenses and reactive risk-detection measures.

It is no surprise that this year’s survey results reflect a significant shift in the threat hierarchy. For the first time in report history, generative AI (53%) and agentic AI (45%) have emerged as the top identity-specific security concerns — displacing stolen or compromised credentials (38%) from its spot as the top identity security challenge.

These concerns are well-founded: 43% of respondents identified AI-driven tactics as the most significant change in the attack landscape over the last year. Notably, nearly 40% of organizations report having experienced a GenAI-related security incident in the past 12 months. Among the 40% of respondents impacted by AI-based attacks, personalized phishing was the dominant identity risk, cited by nearly two-thirds of respondents (65%).

![Chart: Types of AI-generated or AI-enhanced content encountered: Personalized phishing emails (65%), Pre-recorded deepfake videos (45%), Deepfake audio during live calls (43%), Altered or fake images (40%), Manipulated recorded voice messages (40%), Live video manipulation (39%)]

### Synthetic media and the new force multiplier
Synthetic media has emerged as a top-tier threat, with deepfakes registering concern across multiple formats including prerecorded videos (45%), live audio (43%) and the manipulation of live video such as Zoom calls (39%). Other AI-based identity attacks included altered or fake images or photos (40%) and manipulated voice messages or audio clips, such as voice cloning (voice phishing or “vishing”) (40%). Voice cloning is a new and increasingly common AI-based technique that creates a synthetic version of a person’s voice from audio samples that can be combined to form completely new sentences.

Beyond stand-alone AI attacks, generative AI and agentic AI are industrializing traditional vectors such as phishing and ransomware. Phishing (43%) remains the most common type of cyberattack organizations have faced in the past 12 months, followed by malware and ransomware (37%). These are followed closely by AI-generated attacks (36%) and identity impersonation (35%).

### The hindsight tax: Why reactive spending and fragmented ownership hinders resilience
Breach triggers budget: Almost 60% of organizations report increased budget and investment as the most common response to a breach. However, this reliance on “panic buying” often indicates an immature identity security posture. When forced to react, organizations prioritize rapid deployment of IDV (61%), MFA (57%), and identity threat detection and response (52%) to address the failure points identified during a breach.

---

## Section 2: Phishing-resistant Adoption Trends
### The education barrier: Why conceptual ambiguity slows phishing-resistant adoption
The 2025 State of Passwordless Identity Assurance report highlighted widespread ambiguity regarding the technical definition of phishing resistance. This year’s findings mark a significant breakthrough, with respondents demonstrating a clearer understanding. For the first time, FIDO passkeys emerged as the most widely identified phishing-resistant authentication method, at 64%, a significant increase from 40% in 2025. Similarly, hardware keys rose sharply to 54% from 34%, while smartcards increased to 52% from 37%.

### From pilot to adoption: Solving for infrastructure, legacy and scale
Despite increased market literacy, the momentum of passwordless adoption has encountered a strategic plateau, as usernames and passwords remain the dominant authentication method for 76% of respondents. By comparison, enterprise use of passwordless authentication remains low on the adoption curve, cited by just 43% of respondents.

![Chart: Workforce deployment levels across security technologies, showing high reliance on usernames/passwords and lower adoption of passwordless/FIDO passkeys]

Consistent with broader cybersecurity trends, financial constraints (40%) emerged as the top deterrent to passwordless adoption. Notably, user experience is now less of a concern, identified by only 23%. This indicates that the usability gap is closing, and that the greater challenge is no longer convincing users but obtaining the necessary budget.

---

## Section 3: The Rise of Identity Verification
### Establishing a new authentication baseline
With nearly two-thirds of respondent organizations (65%) now utilizing IDV, the technology has moved well beyond adoption to become a rising enterprise standard. Current deployment methods show biometrics leading at 67%, closely followed by government-issued documents such as driver’s licenses or passports (64%) and device recognition/fingerprinting (58%).

### From persona-based protection to enterprise-wide assurance
On average, 92% of enterprise employees still rely on usernames and passwords. The breadth of passwordless usage is more encouraging, with respondents reporting that 43% of their employees on average use passwordless technology. More than one-third of enterprises have successfully scaled passwordless to more than 50% of their workforce. Overall, these disparities suggest that phishing-resistant tools such as passwordless and IDV are currently confined to “persona-based” silos — prioritized for executives and privileged IT staff — while enterprise-wide protection remains a secondary roadmap objective.

---

## Conclusion
As organizations emerge from the Age of Enlightenment, a better understanding of what is needed marks a major step forward for the passwordless movement.

The gap between password usage and true passwordless authentication is narrowing, but not quickly enough to keep pace with the accelerating velocity of AI-driven threats. This leaves enterprises burdened by a massive and growing “password debt” — legacy credentials, fragmented controls and persona-based deployments that attackers are exploiting.

This pause in adoption does not reflect a lack of readiness or conviction; rather, it reflects a collision with reality. Scaling identity is not a feature rollout; it involves complex systems work. It forces organizations to confront legacy infrastructure, fragmented ownership across HR, IT, IAM and security, and the operational complexity of consistently enforcing trust across every workflow where identity is granted.

---

## Appendix: About
### Methodology
The online survey collected data from 950 global IT security decision-makers, specifically targeting those in managerial positions or higher, who are engaged in the identity life cycle and security measures. Conducted in November 2025, the global survey included respondents from the US, UK, France, Germany, Australia/New Zealand, Japan and Singapore.

### About the Author
Garrett Bekker is a principal research analyst at 451 Research from S&P Global Energy Horizons, leading the identity and access management (IAM) vertical within the Information Security channel.

### About HYPR
HYPR, the leader in passwordless identity assurance, delivers the industry’s most comprehensive end-to-end identity security for your workforce and customers. By unifying phishing-resistant passwordless authentication, adaptive risk mitigation, and automated identity verification, HYPR ensures secure and seamless user experiences for everyone. Visit: [hypr.com/get-a-demo](http://hypr.com/get-a-demo)