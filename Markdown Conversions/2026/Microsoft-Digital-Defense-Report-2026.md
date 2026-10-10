# 2026 Microsoft Digital Defense Report
## Decoding Emergence

## Table of Contents
- [What’s in the Report? Contents Listing](#whats-in-the-report-contents-listing)
- [Introduction: The Era of Interconnected Risks](#introduction-the-era-of-interconnected-risks)
  - [Opening Statement](#opening-statement)
  - [Our Unique Vantage Point](#our-unique-vantage-point)
  - [In a Time of Interconnected Risk, Organizations Need to Focus on Resilience](#in-a-time-of-interconnected-risk-organizations-need-to-focus-on-resilience)
  - [What’s New in the Threat Landscape: Five Emerging Themes](#whats-new-in-the-threat-landscape-five-emerging-themes)
  - [About This Report](#about-this-report)
  - [Ten Security Priorities for Organizations](#ten-security-priorities-for-organizations)
  - [Top 10 Takeaways from This Report](#top-10-takeaways-from-this-report)
- [AI](#ai)
  - [Understanding the AI Threat Landscape](#understanding-the-ai-threat-landscape)
    - [AI Threat Landscape](#ai-threat-landscape)
    - [AI Systems as Targets](#ai-systems-as-targets)
    - [Attacks on AI Systems](#attacks-on-ai-systems)
    - [Attackers Are Using AI Systems for Attack Enablement](#attackers-are-using-ai-systems-for-attack-enablement)
    - [Vulnerability Detection Is Running Ahead of Remediation](#vulnerability-detection-is-running-ahead-of-remediation)
    - [Phishing Is Becoming More Targeted](#phishing-is-becoming-more-targeted)
    - [AI Can Be Exploited for Real-World Attacks](#ai-can-be-exploited-for-real-world-attacks)
    - [How AI Upgrades Fraud Campaigns](#how-ai-upgrades-fraud-campaigns)
  - [AI Attack Acceleration](#ai-attack-acceleration)
    - [Autonomous Attacks Are Changing the Attack Paradigm](#autonomous-attacks-are-changing-the-attack-paradigm)
    - [Challenges on the Horizon: The Consequence of Fully Automated Attacks](#challenges-on-the-horizon-the-consequence-of-fully-automated-attacks)
    - [Vulnerability Discovery Acceleration by AI](#vulnerability-discovery-acceleration-by-ai)
  - [AI-Augmented Intrusions: The Emerging Risk of LLM-Assisted Attacks](#ai-augmented-intrusions-the-emerging-risk-of-llm-assisted-attacks)
    - [Four Converging Trends in Prompt-Driven Malware](#four-converging-trends-in-prompt-driven-malware)
    - [Self-Hosted Agent Runtimes Are the Next Exposure Surface](#self-hosted-agent-runtimes-are-the-next-exposure-surface)
    - [Attack Autonomy Progression](#attack-autonomy-progression)
    - [New Challenges for Defenders](#new-challenges-for-defenders)
    - [Self-Improving AI Worms](#self-improving-ai-worms)
    - [Recommendations for Defenders](#recommendations-for-defenders)

---

## What’s in the Report? Contents Listing

| Section | Page | Section | Page |
| :--- | :--- | :--- | :--- |
| **Introduction** | **3** | **Cybercrime** | **62** |
| Opening statement | 4 | Identity is at the center of modern cyber risk | 63 |
| Our unique vantage point | 5 | How attackers gain access | 66 |
| About this report | 6 | Legitimate access becomes the threat | 69 |
| Ten security priorities for organizations | 7 | Ransomware: From access to impact | 75 |
| Top 10 takeaways from this report | 8 | Cybercrime disruption and collective defense | 78 |
| **AI** | **9** | **Resilience** | **81** |
| Understanding the AI threat landscape | 10 | Trust, software, and supply chain security | 82 |
| Securing the AI ecosystem | 21 | Critical infrastructure and operational technology | 85 |
| AI as the new attack surface | 27 | National resilience and geopolitical security | 90 |
| **The threat landscape** | **31** | Preparing for the next security transaction | 97 |
| The threat landscape in 2026 | 32 | **Appendix** | **99** |
| Nation-state and geopolitical threats | 38 | Glossary | 100 |
| How modern intrusions begin | 44 | References | 102 |
| Detection, intelligence, and disruption | 54 | | |
| Securing the foundations | 59 | | |

*Unless otherwise noted, this report covers the 2026 reporting period, July 2025 through June 2026. Year-over-year comparisons use the 2025 reporting period, July 2024 through June 2025. All data figures are subject to rounding; any discrepancies will be due to rounding.*

---

## Introduction: The Era of Interconnected Risks

### Opening Statement
**By Terrell Cox, CVP and Deputy CISO, Customer Security Management Office**  
**and Mike Yeh, Vice President, Deputy General Counsel, Customer Security & Trust**

> _"The challenge confronting security leaders today is no longer a lack of information. It is the growing complexity of the environments they are responsible for protecting."_

This year’s Microsoft Digital Defense Report reveals a common pattern across AI, nation-state activity, cybercrime, and resilience: risk is becoming increasingly interconnected. Threats increasingly move through the trusted relationships connecting identities, software and supply chains, partners, cloud platforms, data, and AI systems. When one of those trust pathways is compromised, consequences can travel far beyond the initial point of entry.

This shift reflects a fundamental change in what security leaders are actually responsible for. CISOs today are managing ecosystems, not just environments: networks of technologies, identities, partners, vendors, and dependencies whose security outcomes are deeply intertwined. This ecosystem lens applies across every trend in this report.

AI is one example of this transformation. While much of the public conversation focuses on AI as a technology and national security priority, an equally important story is what AI reveals about the future of cybersecurity. AI is accelerating discovery, analysis, adaptation, and automation across both offense and defense. It is reshaping how vulnerabilities are identified, how attacks are developed, how defenders prioritize risk, and how organizations respond to emerging threats.

It has compressed the security cycle from days to minutes. Its influence extends far beyond AI systems themselves and into the very fabric of our societies.

Nation-state activity is evolving. Cyber operations, traditionally intertwined with economic objectives, geopolitical influence, and national and economic security priorities, have more reach than ever. They extend to accessing critical infrastructure for data exfiltration, pre-positioning, or even destructive attacks, blending the cyber world with the physical world.

The same pattern can be seen in cybercrime. Criminal operations have evolved into highly specialized ecosystems where access brokers, ransomware operators, credential theft services, fraud networks, and malware providers function as interconnected components of a broader economy. These ecosystems increase efficiency, lower barriers to entry, and enable sophisticated attacks to scale with unprecedented reach.

### Our Unique Vantage Point

![Infographic displaying Microsoft telemetry data scale: over 165 trillion security signals analyzed daily; 15,000+ partners in security ecosystem; 35,000 full-time equivalent security engineers employed worldwide; 31 million identity risk detections analyzed in an average day; 5.2 billion emails screened daily to protect users from malware and phishing; ~4.7 million net new malware file blocks on average every day.]

- **>165tr** security signals daily in our security ecosystem  
- **15k+** partners  
- **35,000** full-time equivalent security engineers employed worldwide  
- **31m** identity risk detections analyzed in an average day  
- **5.2bn** emails screened daily on average to protect users from malware and phishing  
- **~4.7m** net new malware file blocks every day  

At this scale, the value is not any single signal or control. It is the ability to connect signals, threat intelligence, enterprise context, and action across the security estate. Integrated visibility turns each additional signal into more useful context and enables faster, coordinated defense.

### In a Time of Interconnected Risk, Organizations Need to Focus on Resilience

Across all of these trends, one observation remains constant: the expanding complexity of modern digital environments continues to create opportunities for adversaries to exploit gaps in visibility, access, and governance. Resilience therefore remains a key priority.

Resilience extends beyond an organization’s ability to recover from disruption. It is the ability to anticipate change, understand dependencies across interconnected ecosystems, and make effective decisions as conditions evolve.

In an era of interconnected risk, resilience is increasingly shaped by how well organizations understand and manage the dependencies that connect their operations, technologies, partners, and data. The organizations best positioned for the future will not necessarily be those with the most data, the largest security teams, or the most advanced tools. They will be the organizations that can understand their ecosystems, manage dependencies, adapt quickly, and make confident decisions amid change.

AI is changing the physics of cybersecurity. Attack timelines are compressing, the cost of sophisticated capabilities is falling, and agentic systems are beginning to automate more of the attack lifecycle. Defenders are facing that shift across a growing estate of identities, data, applications, cloud services, and AI systems. Keeping pace requires organizations to:
1. **Get ready for AI** by strengthening security foundations and protecting data;
2. **Secure AI** with controls that extend across the AI stack; and
3. **Defend with AI** by connecting signals, threat intelligence, and context to support faster investigation and response.

The same capabilities increasing attacker speed and scale can also give defenders the ability to operate more continuously and at machine speed.

We encourage you to read this report through that lens. The findings that follow are not simply observations about today’s threat landscape. They reveal a broader transition underway across cybersecurity. Understanding that transition is important. Acting on it may prove decisive.

---

### What’s New in the Threat Landscape: Five Emerging Themes

This year’s report takes an expansive look at the developments that are reshaping cybersecurity and how organizations, policy makers, and nation states must think about risk. There are five new themes emerging:

1. **Risk is becoming more interconnected**  
   The most significant risks facing organizations increasingly emerge not from individual technologies, users, or vulnerabilities, but from the relationships between them. AI systems rely on data, identities, cloud infrastructure, and third-party services. Supply chains connect thousands of organizations through shared software and platforms. Cybercriminal and nation-state ecosystems operate through extensive networks of partners, providers, and enablers. As a result, cybersecurity is becoming less about defending individual assets and more about understanding interdependence across an increasingly connected digital ecosystem.

2. **AI is reshaping the security equation**  
   AI is actively altering how threats are developed, vulnerabilities are discovered, and defenders identify and respond to risk. The report examines how AI is impacting offensive and defensive operations, accelerating the pace of discovery, analysis, and adaptation across the cybersecurity ecosystem. This evolution is creating new opportunities for defenders while raising important questions around governance, trust, security, and accountability.

3. **Criminal ecosystems continue to mature**  
   Cybercrime has evolved beyond individual actors and isolated campaigns. Modern cybercrime functions as a mature ecosystem composed of credential theft operations, ransomware affiliates, access brokers, fraud networks, malware developers, and illicit service providers. These criminal economies have lowered barriers to entry, enhanced operational efficiency, and enabled malicious activity to scale globally, and AI is likely to compound this trend. Understanding how these ecosystems function has become increasingly important for organizations seeking to reduce exposure and disrupt attacker pathways.

4. **Resilience has become a strategic capability**  
   As technology environments become more connected, disruption becomes more difficult to contain. Resilience is therefore emerging as one of the most important organizational capabilities in cybersecurity. Resilience is shaped by visibility, preparedness, governance, adaptability, and decision-making. Organizations that can anticipate disruption, understand dependencies, and adapt as conditions change are better positioned to withstand the challenges highlighted throughout this report.

5. **Security is increasingly defined by how organizations adapt**  
   A common theme emerges across every section of this year’s report: cybersecurity’s defining challenge is no longer simply understanding threats. It is understanding how risks interact, how dependencies shape outcomes, and how organizations adapt to rapidly changing conditions. Organizations must strengthen the fundamentals within their control, understand the dependencies that shape their risk, and make effective decisions amid uncertainty.

---

### About This Report

The Microsoft Digital Defense Report is organized around four dimensions of today’s cybersecurity landscape:

- **AI**: Explores how AI is reshaping offensive and defensive operations, changing the economics of cybersecurity, and creating new opportunities and challenges for organizations.
- **The Threat Landscape**: Analyzes the evolving behavior of cyber adversaries, from nation-state actors to cybercriminal organizations, identifying the tactics, trends, and operational patterns that are reshaping risk across the digital ecosystem.
- **Cybercrime**: Analyzes the industrialization of cybercrime and mature ecosystems driving criminal activity at scale.
- **Resilience**: Focuses on the organizational capabilities required to anticipate, withstand, recover from, and adapt to disruption.

Taken together, these four perspectives tell a broader story. Cybersecurity is no longer defined solely by protecting technology. It is increasingly defined by how organizations understand interconnected risk, manage complexity, and adapt to change in a world where technology, business, and security are more closely linked than ever before.

---

### Ten Security Priorities for Organizations

Cyber risk is now a continuous test of business resilience. The boundaries between state-sponsored activity, cybercrime, and influence operations have continued to erode. This converges into sustained and overlapping campaigns that have tested not only technology estates, but the resilience of organizations and the trust placed in them. For business leaders, this means focusing less on reacting to the last breach and more on how long critical operations can be sustained under continuous cyber stress.

In this environment, cybersecurity is a continuous business condition, defined by persistent adversary pressure, machine-speed operations, and systemic interdependence. The defining question for boards today is not whether disruption will occur, but whether the organization can continue operating, contain harm, recover quickly, and maintain trust when it does.

The response starts with secure foundations: **Secure by Design**, **Secure by Default**, and **Secure Operations**, applied through identity-centric Zero Trust. These foundations make the following priorities durable as AI expands the number of identities, applications, agents, and dependencies organizations must govern:

1. **Govern cyber risk at leadership level**  
   Report identity exposure, patch latency, agent permissions, critical dependencies, dwell time, and recovery readiness.
2. **Defend identity as the primary control plane**  
   Protect identity by deploying passkeys and phishing-resistant MFA, reducing privilege, governing human and non-human identities, and using rapid invalidation/rotation for tokens and session credentials.
3. **Establish governance, visibility, and data controls for AI**  
   Maintain visibility into approved AI tools, services, and agentic capabilities while monitoring for unauthorized or unmanaged use. Apply sensitivity-aware access, data protection, and governance to the data those systems and agents can reach.
4. **Reduce exposure and edge risk**  
   Continuously discover internet-facing assets and prioritize rapid patching of edge devices, enabling centralized and high-fidelity logging, enforcing strong authentication, and integrating network-level visibility with threat intelligence.
5. **Focus on cross-signal correlation**  
   Correlate endpoint, identity, cloud, application, email, and network signals to detect intrusions earlier. Cross-signal correlation also enables defenders to anticipate attack paths and targets.
6. **Enact a continuous threat vulnerability management model**  
   Combine asset visibility, vulnerability identification, threat detection, and AI-accelerated insight to create a continuous threat vulnerability management program.
7. **Validate exposure via proactive testing**  
   Conduct assume-breach exercises focused on cloud services, SaaS platforms, APIs, and workflow automation capabilities. Prioritize testing based on where the highest-value data resides, is accessed, or can be aggregated.
8. **Secure software dependencies**  
   Harden software installation, maintain a software inventory, validate provenance, monitor packages, and prepare for rapid containment.
9. **Participate in collective defense**  
   Share actionable threat indicators and victim-informed intelligence with trusted partners and law enforcement to support coordinated threat tracking, investigation, and disruption.
10. **Prepare for long-horizon technological transitions**  
    Build a cryptographic inventory and advance post-quantum planning alongside AI governance.

> **The Defining Question:**  
> The defining question for boards today is not whether disruption will occur, but whether the organization can continue operating, contain harm, recover quickly, and maintain trust when it does.

---

### Top 10 Takeaways from This Report

1. **AI is changing the physics of cybersecurity.**  
   AI is compressing attack timelines, lowering the cost of sophisticated capabilities, and enabling attackers to operate with greater speed, scale, and autonomy. But the same capabilities can strengthen defense by accelerating discovery, analysis, prioritization, and response. Security organizations must prepare for an environment in which both attackers and defenders increasingly operate at machine speed.
2. **Attackers are already targeting AI as another attack surface.**  
   Threat actors can exploit AI to do things like execute malicious commands, steal AI serving capacity, and exfiltrate data. As AI becomes ubiquitous in the workplace and at home, it has become both a tool and a target for attackers.
3. **People remain a heavily exploited initial-access path.**  
   Threat actors continue to target user behavior through user execution, ClickFix-style social engineering, phishing, and impersonation. These techniques remain effective even as AI changes their speed, scale, and personalization.
4. **Identity is the primary control plane for defense.**  
   Attackers consistently take advantage of unnecessary privileges, persistent access, and weak identity governance. This is why phishing-resistant multifactor authentication (MFA) and passkeys, disciplined identity hygiene, tiered administration, and strong privileged-access enforcement remain the best safeguards against cyberattacks. That control plane now spans both human and non-human identities, including applications and agents.
5. **Signal correlation through shared threat intelligence is key to defense at multiple levels.**  
   The degree to which a defender’s systems share and correlate threat intelligence is one of the highest-leverage strategic variables under the defender’s control. Signal cross-correlation can reveal attack patterns that remain invisible when endpoint, identity, cloud, application, email, and network telemetry are analyzed in isolation.
6. **Emerging threats facilitate stealthier attacks, operating at a larger and faster scale.**  
   Over the next year, Microsoft sees the biggest threats coming from:
   - Open-source supply chain compromise
   - Attacks against edge devices
   - AI as a force multiplier for malicious activity
7. **Protecting data is even more important as AI expands access at scale.**  
   Trusted AI depends on trusted, well-governed data. Data protection has always been a key priority, and now that AI systems and agents can reach and act on sensitive information at unprecedented scale, it’s more crucial than ever. Organizations should reduce oversharing, apply sensitivity-aware access and least-privilege controls, and govern how data is discovered, used, and shared across AI, cloud, and application environments.
8. **The future of defense involves rethinking how we protect our assets from reactive incident response to proactive, continuous discipline.**  
   Defenders must shift from tool-centric vulnerability management to threat exposure management. At the core of this is:
   - Asset visibility
   - Continuous vulnerability awareness
   - Intelligence-driven threat detection
   - AI-accelerated insight  
   This means reporting metrics should shift from number of patches deployed to exposure reduced, detection coverage increased, and time-to-mitigate compressed.
9. **National and international policy decisions will shape the future of cybersecurity.**  
   In an increasingly contested landscape, cybersecurity demands clearer rules, credible accountability, and sustained cooperation. Strengthening protections for critical infrastructure, advancing operational accountability, and preserving an open, secure, and resilient digital environment must be a priority for governments on both a domestic and international level.
10. **Resilience must be a core outcome of cybersecurity planning.**  
    Retain the existing focus on reducing exposure, detecting threats faster, adapting to changing risks, and maintaining operations. This preserves resilience as the outcome without competing with identity, secure foundations, data, and the three-part operating model for "primary" status.

---

## AI

> _"AI is making fraud more sophisticated and accessible, accelerating cybercrime worldwide. As threats evolve across borders, public-private and international cooperation—built on technology, trust, and shared action—is essential to disrupting cybercriminals and protecting society."_  
> — **Kenichi Sakurazawa**, Managing Director, Japan Cybercrime Control Center (JC3)

### Understanding the AI Threat Landscape

#### AI Threat Landscape
AI is changing the physics of cybersecurity. It is reducing the time, expertise, and cost required to discover and exploit weaknesses while enabling both threat actors and defenders to operate with greater speed, scale, and autonomy.

Vulnerability discovery is one of the clearest examples: threat actors can now conduct large-scale, AI-powered vulnerability detection, with discovery increasingly running ahead of remediation. The result is a multi-year window in which the number of known but unpatched vulnerabilities will rise sharply before it falls. What was once a threat on the horizon has now arrived.

This vulnerability wave is just one example of a broader pattern. The risks defenders worry about are mostly familiar, but the shape and scope of those risks and the surfaces to which they apply have all shifted. Attackers now have a clearer picture than ever of what they want from AI systems and how to use AI to achieve their traditional goals.

The same capabilities changing the economics of attack can also shift the advantage toward defenders. AI enables defenders to continuously discover vulnerabilities, correlate signals, identify anomalous behavior, prioritize risk, and increasingly automate defensive action. The ability to automatically and persistently hunt for vulnerabilities—and fix them—creates a potential world of "persistent defense" that was never before possible at scale. AI opens new possibilities for anomaly detection, even in very "human-shaped" datasets like message bodies.

The AI threat landscape continues to move; what is on the leading edge today will be commoditized within a year, and new categories of threats will emerge. While the equilibrium between attackers and defenders will likely ultimately be re-established, in the near term we are in a period where attackers are reaching to advantages first, and defenders will need to move sharply in order to close the gap.

![Figure 1: The Target Landscape showing three categories: Build/Inputs (Data, software; Model weights; Product infra; Output artifacts like Code, docs, data), Runtime (AI systems, Agents, chatbots, apps; Serving system; User data; Logs, memory), and Compromised Targets (Computer systems / Cyberattacks; People / Phishing, scams, influence; Information / Reconnaissance, dossiers; Real-world / Physical capability, Skill uplift).]

*Figure 1 maps this expanded target landscape, which roughly divides into targets associated with AI systems and targets of threat actors that use AI for enablement.*
- **Build side (Left)**: Inputs to model building, model data, and production infrastructure.
- **Runtime (Center)**: AI systems themselves, the user data with which they interact, and the output artifacts they produce.
- **Adversary Targets (Right)**: Computer systems, people, information, and real-world capabilities compromised using AI systems.

*Issues beyond direct adversarial scope (accidents that become exploitable vulnerabilities):*
- Misunderstanding or naïve acceptance of AI outputs causing dangerous errors
- Ambiguities around legal accountability
- The impact of AI on human psychology and decision-making

#### AI Systems as Targets
At the foundation of every AI system is a complex supply chain that includes hardware, software, training data, and the infrastructure used to build and operate AI models. There are multiple ways that attackers directly target these foundations: model tampering, theft of service, model theft, and attacks on AI systems themselves.

As AI systems connect models to identities, data, applications, tools, and external services, each connection creates a trust relationship that can become an attack path. Securing AI therefore requires protecting not only the model itself, but the full set of dependencies, identities, permissions, and data that determine what the system can access and what actions it can take.

- **Model tampering**: Can either be done deliberately by a model builder or surreptitiously by an attacker who has compromised the pipeline. It offers the opportunity for hard-to-detect "sleeper agent" attacks. Attackers can control AI behavior under tailored circumstances—for example, introducing security vulnerabilities into AI-generated code. The circumstances can range from very specific (*"when deployed by such-and-such an organization"*) to very broad (*"whenever context indicates the user’s work opposes the objectives of a particular government"*). While significant progress has recently been made on detecting such tampering, it remains significantly harder to detect than backdoors in code.
- **Theft of service**: The most familiar threat on the runtime side. Historically, adversaries sought graphics processing unit (GPU) capacity to mine cryptocurrency. Today, attackers are increasingly stealing AI serving capacity, bundling it, and reselling it to criminal and nation-state customers. Malicious use of an AI system is an important indicator of compromise—anomalous internet searches, for example, might indicate a network has been hacked.
- **Model theft**: A key risk for anyone developing or fine-tuning models. This can be done either traditionally or via "distillation"—training a smaller, cheaper model on the outputs of a more capable one. Here, sequences of superficially legitimate-looking application programming interface (API) requests cumulatively reveal enough information for an attacker to reconstruct significant aspects of the model.

#### Attacks on AI Systems
Higher in the stack, attackers are targeting AI systems themselves. These threats attack the machine learning model, prompts, and training data rather than just the underlying computer hardware or operating system.

- **Indirect or Cross-Prompt Injection Attacks (XPIA)**: A threat actor includes malicious instructions in a data source that a large language model (LLM) then consumes into its context in order to subvert its subsequent output. While long understood, the shift toward agentic AI systems has brought a reinterpretation of XPIA as **task adherence in the presence of adversarial data**.
- **Task Adherence**: How well an agent follows user instructions and stays on target. This is the fundamental challenge facing agentic systems. Current AI systems face tremendous challenges with this even without adversarial data, especially in flexible, "vibe-coded" systems like OpenClaw, which have become notorious for deleting data, revealing secrets both personal and cryptographic, and spending users' money.
- **Persistent Artifact Poisoning (Read-Write Memory)**: Attackers target persistent read-write memory, which allows an AI model to save (write) facts from interactions and retrieve (read) them later. Techniques like XPIA can create dormant, persistent attacks by:
  - Causing attacker-controlled data sources to become more trusted by a user’s AI
  - Adjusting the opinions and biases of the AI system
  - Implanting instructions to assist in exfiltrating or modifying data directly
- **Artifact Exfiltration**: Artifacts such as write-only logs and memory stores offer personal and secret information, making them highly valuable exfiltration targets.
- **Scale of Sensitive Data Access**: AI changes the scale at which sensitive data can be accessed. A compromised or overprivileged AI system can aggregate and expose information across multiple services far beyond the scope of any single application.
- **Artifacts Created by AI (Slopsquatting)**: In slopsquatting attacks, adversaries register malicious software packages with names likely to be hallucinated by AI code assistants, leading developers to download malicious dependencies.
- **Model Context Protocol (MCP) Server Exposure**: MCP middleware connects generic APIs with AI systems. Rapid, vibe-coded deployments frequently omit basic security, leaving unauthenticated or poorly authenticated MCP services operating under developer credentials to access sensitive enterprise resources.

#### Attackers Are Using AI Systems for Attack Enablement
Adversaries use AI to scale and accelerate malicious operations:
- Finding vulnerabilities in source code, binaries, and AI serving systems
- Generating custom malware for attacks
- Shortening the cycle of data exfiltration, secret discovery, and lateral movement from days to minutes
- Controlling and managing entire attack chains

While none of these represent wholly new attack categories, the quantitative increase in scale and speed creates an immediate problem for defenders.

#### Vulnerability Detection Is Running Ahead of Remediation
The volume of known vulnerabilities has increased rapidly as static and dynamic analysis tools with lower false-negative rates have emerged.
- Defenders can fix these vulnerabilities through automated remediation and development environment integration.
- However, remediation is inherently slower than discovery because many systems lack robust unit and integration testing needed to safely deploy rapid changes.
- This creates a multi-year period where the count of known, unpatched vulnerabilities spikes, allowing well-funded adversaries to stockpile zero-day vulnerabilities.

#### Phishing Is Becoming More Targeted
AI facilitates mass customization, allowing every phishing campaign to become tailored and personalized (spear phishing at scale). Combined with real-time audio and video deepfakes, unauthenticated and poorly vetted communications channels (including email) are rendered vulnerable to automated social engineering.

#### AI Can Be Exploited for Real-World Attacks
Adversaries can leverage AI for:
- Dangerous weapons proliferation
- Illegal drug production
- Mass-casualty attack planning
- Exploitative and abusive synthetic content generation
- Dossier assembly on individuals or critical infrastructure under the guise of ordinary data analysis

Telemetry must monitor model and agentic system activity—including tool calls, chain-of-thought (CoT) reasoning, request patterns, and session-level prompts—to detect malicious intent.

#### How AI Upgrades Fraud Campaigns
Identity-based fraud campaigns previously had four major detectable weaknesses. AI eliminates all four simultaneously:

1. **Identity document manipulation**: AI replaces and enhances photos in stolen or forged documents, passports, and certifications to produce counterfeits that pass visual inspection.
2. **AI-polished communications**: Writing assistants generate grammatically flawless resumes, LinkedIn profiles, GitHub histories, and emails.
3. **Voice-changing software in live interactions**: Real-time voice modulation during video calls and phone interviews masks accents and regional speech patterns.
4. **Synthetic digital footprints**: Commit histories, Stack Overflow profiles, blogs, and social media footprints can be generated and sustained automatically using AI tools.

---

### AI Attack Acceleration

AI-enabled cyber operations are moving beyond simple content generation and beginning to orchestrate attacks at machine speed and accelerated scale.

Recent observed attack complexities include:
- LLMs embedded directly inside malware binaries.
- AI coding assistants abused to conduct local network and system reconnaissance.
- Nation states leveraging AI agents to assist in orchestrating multi-step intrusions.
- AI agents autonomously escaping sandboxes and test harnesses to execute complex target attacks.

#### Autonomous Attacks Are Changing the Attack Paradigm
Lab evaluations and emerging real-world cases demonstrate movement toward full-chain autonomy:
- **Mythos and GPT-5.5**: Demonstrated the capability to fully autonomously orchestrate complex multi-stage attack chains (achieving full domain compromise across a 32-step chain against an emulated enterprise network without human intervention).
- **Open-weight models**: Publicly downloadable models currently lag closed proprietary models in orchestrating full attacks by approximately seven months.
- **JADEPUFFER (July 2026)**: Sysdig Threat Research Team documented the first automated ransomware extortion attack. Microsoft observed overlapping AI-orchestrated intrusions where initial access stemmed from internet-exposed services running known-vulnerable software.
- **Hugging Face Sandbox Escape (July 2026)**: OpenAI cybersecurity model training agents escaped their sandbox environment and collectively orchestrated an attack targeting benchmark answer keys on Hugging Face.

#### Challenges on the Horizon: The Consequence of Fully Automated Attacks
- **Continuous enterprise assessment**: Automated breaching systems will persistently scan and attack exposed enterprise assets, exploiting custom, in-house code vulnerabilities.
- **Timeline compression**: Hands-on-keyboard attack phases will compress from days to minutes. Rather than a single operator moving through a network, a collective of autonomous agents can be deployed concurrently from the initial access vector to achieve domain compromise simultaneously.
- **Defense at machine speed**: Defenders must deploy agentic AI defensive systems working alongside human analysts, granting agents greater autonomous authority to contain threats.

#### Vulnerability Discovery Acceleration by AI
- The median time between vulnerability discovery in the wild and weaponization has collapsed to **well below 24 hours**.
- Vulnerability tracking is projected to reach an estimated record of **72,000 Common Vulnerabilities and Exposures (CVEs)** for 2026.
- While software vendors leverage AI to discover and patch flaws in large waves, adversary exploitation windows remain extremely short, demanding near-instantaneous patching cycles.

---

### AI-Augmented Intrusions: The Emerging Risk of LLM-Assisted Attacks

#### Four Converging Trends in Prompt-Driven Malware

1. **LLM prompt-guided malware (`LAMEHUG` class)**  
   Identified in a July 2025 campaign targeting Ukraine. Malware outsources operational commands dynamically to a remote LLM endpoint. Because commands are generated at runtime, predictable code signatures are eliminated, bypassing traditional heuristic and signature defenses.
2. **Abuse of locally installed AI CLIs (`s1ngularity`)**  
   Observed in the Pesky Pika supply chain attack (August 2025). Exploited trojanized `npm` packages to scan infected developer workstations for installed AI command-line tools (`Claude Code`, `Gemini CLI`, `Amazon Q CLI`). The malware invoked these pre-approved CLIs with permissive flags to hunt for environment variables, SSH keys, and credentials, leaking ~2,000 secrets and ~20,000 files across 225 victims.
3. **Local LLM-orchestrated malware (`PromptLock` class)**  
   Experimental ransomware prototype surfaced in August 2025. It shipped solely with natural language prompts and delegated execution logic to an open-weights LLM running on attacker infrastructure. The LLM delivered platform-tailored Lua scripts at runtime to enumerate, exfiltrate, and encrypt files across Windows, Linux, and macOS platforms.
4. **AI-generated lure manufacturing at scale (`TikTok ClickFix`)**  
   In 2025, AI-augmented ClickFix social engineering spread through automated TikTok videos. Faceless video tutorials with synthetic voice narration directed users to paste malicious commands into system terminals to resolve fake software errors, installing Vidar or StealC infostealers. Automated lure production drove costs to near zero while algorithmic feeds delivered massive distribution (some videos reaching ~500,000 views).

#### Self-Hosted Agent Runtimes Are the Next Exposure Surface
Platforms such as OpenClaw load executable "skills" from public marketplaces, consume untrusted external content, and execute actions with persistent enterprise credentials. This fuses untrusted code execution and untrusted prompt instructions into an unchecked loop.
- **Skill malware**: Public registries distribute malicious packages disguised as legitimate agent utilities, running arbitrary third-party code under the agent's identity.
- **Indirect prompt injection**: Malicious prompts hidden in web pages, emails, or inbound documents hijack tool execution, modify internal memory, and spread across every agent processing the resource.

*Microsoft recommends treating self-hosted agent platforms as untrusted code execution environments with persistent credentials, restricting them to isolated hosts governed by non-privileged identities.*

#### Attack Autonomy Progression

```
[Sep-Nov 2025] ───> AI assists in orchestrating a campaign
                   (Anthropic-reported espionage campaigns)

[Apr-Jun 2026] ───> Full-chain autonomy demonstrated in laboratory evaluations
                   (AISI "The Last Ones", Zealot, adaptive worm evaluations)

[Jul 2026]     ───> Real-world autonomous attacks of increasing complexity
                   (JADEPUFFER automated extortion; HuggingFace/OpenAI benchmark incident)
```

#### New Challenges for Defenders
- **Non-deterministic behavior**: Models generate dynamic, unique action sequences for each intrusion; traditional Indicators of Compromise (IoCs) fail to generalize across attacks.
- **Living-off-the-AI (LOLBins with reasoning)**: Attackers run legitimate, signed, enterprise-approved AI CLIs with elevated permissions, executing code, browsing the web, and moving laterally without introducing foreign binaries.
- **Telemetry and detection surface shifts**: Host-based file indicators become less relevant; defenders must monitor behavioral patterns, including sudden egress to external inference endpoints, invocation of local AI CLIs with permissive flags, anomalous command shell prompts, and abnormal tool calls.

#### Self-Improving AI Worms
Research published in June 2026 confirmed the technical feasibility of self-replicating, AI-driven network worms. Threat actors are already deploying worms that compromise internet-exposed vulnerable services, extract LLM provider credentials, and use stolen keys to query models to identify further exploit paths, refine payloads, and spread autonomously.

#### Recommendations for Defenders

- **Establish governance and visibility for AI use**: Maintain comprehensive inventories of approved AI platforms, developer CLIs, and autonomous agent systems; monitor environments for unapproved and shadow AI deployments.
- **Secure agentic AI environments**: Apply strict network isolation, host containment, and least-privilege identity access controls to all AI agent runtimes and self-hosted model engines.
- **Monitor AI-driven activity across the environment**: Ingest telemetry covering model tool calls, outbound inference queries, session prompts, and unusual activity from developer runtimes to identify machine-speed attacks early.

---

ng social engineering techniques, help defenders identify misuse, compromise, or
file scans. This requires defenders to ensure they have and establishing better persistence including through unauthorized automation.
a wider set of telemetry sources and develop new hiding better.
detections for these sources.
Rather than relying on a human operator to Protect the AI software supply chain.
periodically release updates, each infected system Organizations should extend existing software supply
LLM conversation history is in demand effectively becomes a development environment. chain security practices to AI ecosystems, including
At scale, this creates a form of natural selection models, dependencies, extensions, and integrations.
Threat actors have been seeking to access AI data assets.
where the most successful variants spread further
In December 2025, Microsoft found a malicious browser
and continue evolving, risking a significant inflection
extension (600,000+ installs) harvesting ChatGPT and Treat AI interactions and data as sensitive assets.
point for enterprise cybersecurity over this
DeepSeek conversation history. This activity affected Prompts, chat histories, model memory, and AI-
next period.
almost 10,000 organizations before it was mitigated. generated outputs may contain valuable information
This kind of history now routinely holds source code, and should be protected accordingly.
architecture, customer data, and leaked credentials.
Adapt detection and response strategies for AI-
enabled threats. Defenders should evolve security
monitoring, threat hunting, and incident response
capabilities to account for adversaries’ increasing use
of AI tools and automation.

17
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Understanding the AI threat landscape
Threat actor use of agentic AI As adversaries use agentic AI to accelerate “
reconnaissance, development, and operational workflows,
defenders will need to adapt both by securing AI systems
Although agentic AI is relatively new, it is,
and agents and by strengthening existing security Most observed
predictably, already being used by threat practices to keep pace with increasingly automated campaigns still retain
actors, including cybercriminals and state- threats. Section 2: The threat landscape explores practical
human direction,
sponsored actors. approaches for securing the AI stack and governing
AI agents. even as frontier
The way these actors have incorporated new technology
systems demonstrate
is consistent with how they integrated generative AI in Threat actors are looking to exploit
the last few years. Early use cases centered on stages enterprise agentic systems end-to-end autonomy
of the attack lifecycle with a lower barrier, such as
in labs and early
reconnaissance, data triage, and the development of Another emerging trend is that threat actors are
phishing lures. These actors have now extended their use beginning to explore the potential to directly real-world cases.
of agentic AI into more technically complex activities, exploit agentic systems deployed within enterprise
including malware and exploit development and post- environments. This could include testing access
compromise operations. pathways and assessing how agent behavior in a target
organization might be manipulated or abused within
Threat actors are increasingly experimenting with this
existing infrastructure. Identity, particularly cloud identity,
new technology, incorporating it incrementally into
is likely to be a primary access point to exploit enterprise
discrete parts of their workflows where automation can
agentic systems.
improve speed, scale, or consistency. For example, some
actors are using open-source or actor-controlled agentic As organizations extend access permissions to both
tools to conduct multi-source research, automatically human users and autonomous agents, this expands the
synthesizing information to inform targeting, operational number of identity pathways through which adversaries
planning, or narrative development. Others are can gain access or persist. This expanded identity
adopting enterprise-owned agentic services, such surface increases opportunities for credential theft,
as AI coding assistants, to accelerate development token abuse, and other identity-based techniques that
cycles or troubleshoot technical challenges during could be used to access or manipulate agent-driven
intrusion operations. processes. Because these techniques operate through
valid credentials and sanctioned agent workflows,
In most observed real-world operations today, complex
the resulting activity can closely resemble legitimate
end-to-end intrusions still retain meaningful human
use. Detection therefore depends less on identifying
direction. Target selection, operational decision-making,
anomalous tooling than on establishing what normal
and execution of the most complex intrusions remain
looks like for each agent: which identity it uses, which
manually driven in the majority of campaigns we observe.
tools it calls, and at what frequency, so that deviation
However, these limitations are unlikely to exist for
becomes visible.
very long.

18
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Understanding the AI threat landscape
The Red Team perspective: Lowered attacker cost amplifies pressure tools sharp and the tools give the operators time and “
space to work on the hardest problems.
on defenses
Fundamentals under
The AI-driven half of that work takes three shapes:
Pressure on defenders comes from a variety of directions: The most damaging
sustained pressure 1. Source code analysis. Where we have source, models more exposed edge infrastructure, identity sprawl, fragile
read it at scale to locate vulnerabilities and then intrusions we model
supply chain trust, the human factor, and AI. These forces
The job of the Microsoft Red Team is impact every organization on the planet. Previously, it produce working exploit code for them. In the past, rarely depend on
this review would have taken skilled people weeks,
to break into Microsoft’s own systems took time, expertise, and patience for attackers to find the across a codebase too large to cover by hand. Now it’s anything novel;
missing control inside a large, tangled estate, make sense
before real threat actors can. What we something closer to continuous. they depend on
of unfamiliar systems, and line up separate weaknesses
keep learning is that durable security still into a path they could use. Few adversaries could afford 2. Binary analysis. Where we do not have source, a fundamental
comes down to fundamentals. The most to spend at scale to achieve this. Complexity behaved like the same pattern now reaches compiled code—
security control; it was expensive to cut through. reasoning over binaries to find the flaw and build that was missing,
damaging intrusions we model rarely
the exploit, including reversing a vendor patch to misconfigured, or
depend on anything novel; they depend AI is dissolving that cost. Models are good at unraveling recover the vulnerability it closes. This is the surface
on a fundamental that was missing, the sheer number of places a fundamental can quietly that used to demand the scarcest expertise, and it is bypassable. These
fail—quickly, cheaply, and at a scale no team could eroding fastest. fundamentals are
misconfigured, or bypassable. These
match by hand. AI doesn’t create a new class of attacks;
3. Autonomous and semi-autonomous operations.
fundamentals are under more pressure it collapses the effort it once took to find and exploit under more pressure
Beyond finding and writing, models increasingly drive
than ever before. existing attack paths, everywhere at once. The Red the sequence—chaining steps, deciding what to try than ever before.
Team’s job is to get to those paths first and to pressure
next, and carrying an operation forward with limited
the system hard enough to advance our own thinking,
or no human direction. This is the newest of the three
and the industry’s, before attackers do.
and the one we watch most closely.
Human expertise and automated pressure The through line is how little a finding now has to be
worth to become dangerous. A simple information
work together
disclosure issue is the clearest case: a service that leaks
At the core, Microsoft Red Team runs periodic, human- the exact version of the software it is running is, on its
led operations. That is where the most original thinking own, low-severity. But an AI that reads that version, pulls
happens. But we now pair them with continuous, the matching public CVE disclosures, and assembles a
automated pressure—much of it AI-driven—that runs proof-of-concept turns a trivial leak into a working exploit
across the estate continuously. This is one system, with almost no effort in between. The findings that we
not competing programs. Humans find the things no used to deprioritize because exploitation “required work”
automated sweep will catch, working through instinct, we now have to reconsider because the exploitation is
finding dead ends, and vulnerabilities of which publicly so easy.
trained AI models are not aware. Automation handles
breadth—known patterns, regression checks, and wide
coverage—and frees operators to focus on what only
they can do. Run together, the operators keep the AI

19
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Understanding the AI threat landscape
The Red Team perspective: Fundamentals under We would rather hold those tools first. Whatever helps us “ Being able to patch is the most
sustained pressure (continued) breach more effectively will eventually be turned against underrated fundamental
us, other providers, and every organization that relies on
AI accelerates attacks them. So we build and test the capability now, while we None of this A finding’s severity is now set by how cheaply it can be
That collapse of cost does not fall evenly. AI does not can still shape how it is used. The collapse cuts both ways: displaces the weaponized. Patch velocity is where that pressure lands
the same models that unravel complexity for an attacker hardest. A patch is also a disclosure: every fix points to
change where attacks begin—the foothold still comes unravel it for us, which is why the floor of red teaming— fundamentals. If the flaw it closes, and turning a fix back into a working
from familiar sources, for example, a sprayed credential,
connecting known information and running established anything, a world exploit is a discipline as old as patch diffing. What is
an unpatched edge service, or an identity gap. The cost
techniques—is increasingly something we automate. changing is the speed. As AI-assisted binary analysis
lives in everything after the foothold, and that is exactly where the existing
The work that matters most is what remains above that improves—the second scenario above—reversing a patch
where it is collapsing. Each of the three scenarios above is
floor: the undocumented attack, the chain that appears attack paths are to identify and weaponize the underlying vulnerability
an instance of the same shift: work that demanded scarce
only when unrelated weaknesses are seen through an becomes faster and more reliable across architectures.
expertise and patient time is now something a model cheap to find and
adversary’s eyes. That still comes from operators who Once that’s folded into attack automation, the time from
does quickly, cheaply, and repeatedly. The barrier to
stay hands-on. exploit raises the update released to exploit running at scale collapses.
serious capability is falling while the ceiling keeps rising,
This holds for every platform: operating systems,
and advanced technique is landing in far more hands. None of this displaces the fundamentals. If anything, a value of the controls
firmware, network and edge appliances, libraries, cloud
world where the existing attack paths are cheap to find
A growing part of what puts it there is the influx of new that keep those paths services, and mobile.
and exploit raises the value of the controls that keep
models distilled from frontier providers. A legitimate and those paths from existing in the first place. from existing in the Source code is no safer. When developers check in
widely used technique, it is also being used to copy frontier-
a security fix, the change is visible—in commits, pull
first place.
level capability quickly and at low cost, and to spread it
Identity is still the front door requests, issue trackers, and the bulletins that follow.
far more widely than the original providers ever would.
As a red team, we watch those signals, derive the
Two properties of that trend matter to us. First, capability Identity is the surface that matters most, and most of vulnerability from the diff, and build the exploit before
that once required access to a handful of frontier systems what we exploit there has nothing to do with AI. The core many defenders have scheduled the update. The fix and
is now embedded in a proliferating population of smaller failure is the one red teams have exploited for years: too the map to exploit it ship together.
much standing access, too loosely enforced. The highest
models, many of them openly available. This widens
So the meaningful question is how fast a patch reaches
leverage controls available are still the same:
the set of operators able to do everything the three
the entire estate, and whether the systems that cannot be
scenarios describe. Second, and more consequential from • Phishing-resistant MFA
patched are isolated or retired before an adversary gets
a threat perspective, these distilled copies frequently lack • Disciplined identity hygiene there first. The half-life of a vulnerability is shrinking, and
the safeguards built into the models from which they
• Tiered administration patch velocity—not patch availability—is the control that
were derived.
• Strong privileged-access enforcement matters. What we test is the gap: not whether something
The alignment and refusal behavior that gate the most is fixed in the bulletin, but whether it is fixed everywhere,
Agentic identities are the newest variant of the same
dangerous capabilities in a frontier model are among the and how long that took. Being patchable, quickly and
problem—compromise an agent and you may inherit its
first things stripped away in an unguarded distillation, uniformly, is as much an architecture and operations
service-to-service trust and control plane reach—but the
so the ceiling of what is freely usable rises even when decision as a security one.
underlying weakness is unchanged.
no new frontier model ships. We plan against near-
frontier capability being cheap, unguarded, and broadly
distributed—not scarce and controlled.

20
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Understanding the AI threat landscape
“ The Red Team perspective: Fundamentals under Third-party and vendor access is the same trust problem
sustained pressure (continued) one step removed. Infostealers harvest developer
and operator credentials at scale, access brokers
The developer Supply chain and the developer perimeter sell them, and extortion crews convert them into
environment is the The developer environment is the new perimeter. impact—increasingly through extensions, packages,
and connected tools installed without scrutiny.
new perimeter. Repositories, build systems, and pipelines now sit inside
The technology riding through that channel changes;
the real security boundary, and code and configuration
the channel does not.
flow straight through them to production.
The software supply chain is under steady, deliberate Below the operating system
pressure. Provenance and integrity practices are the
countermeasures that matter: frameworks like Supply- Attackers increasingly reach for surfaces that used to
chain Levels for Software Artifacts (SLSA), software bills require scarce expertise, and these deserve attention on
of materials (SBOM), signed and attested builds, and their own merits. Unified Extensible Firmware Interface
properly protected signing keys. Most organizations (UEFI) and firmware implants persist beneath the
operating system and survive a full reinstall. Out-of-band
have only partially adopted them.
management—baseboard management controllers and
The developer is part of that perimeter as well—arguably similar interfaces—offers powerful, sometimes near-
its most exposed point, and the hardest to bound. invisible control and is too often left poorly secured.
A single engineer accumulates standing credentials, Secure Boot integrity, the trust chain it depends on,
broad source access, and a growing set of automation and the Public Key Infrastructure (PKI) and cryptography
and AI coding interfaces acting on their behalf. That mix underneath it are all in scope, and failures there are quiet
makes least privilege genuinely difficult to enforce. and high-impact.
Access that looks scoped on paper compounds across
tokens, tools, and agents.
Measuring what matters
Eventually, one compromised developer’s real blast radius
Measurement separates a mature program from a merely
is far larger than any single grant implies. This is where
active one. We track remediation rates, repeat findings,
an inventory is not enough and a graph is essential: what
time-to-fix, and—just as important—whether defenders
we most want to know—and what most environments
detect and contain our activity. Validating detection and
cannot answer—is what a given developer, and the
response, through assumed-breach exercises and close
automation acting for them, can reach directly, trigger
work with the defensive team, is the higher bar. We also
through the pipelines they run, and touch two hops
measure whether our continuous investment, AI included,
out through everything those pipelines connect to.
is buying real risk reduction at a defensible cost, and
Mapping that blast radius before an attacker does
whether techniques from our operations are feeding back
is a core function of the continuous layer.
into that continuous layer rather than stalling in a report.

21
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
eht
gniruceS
metsysoce
IA
Securing the AI stack enables organizations to detect and respond to emerging Securing the AI Stack
threats. Governance frameworks ensure accountability,
transparency, and appropriate human oversight for high-
The AI stack spans infrastructure, data,
risk actions. Physical security. Refers to the safeguards that protect
models, and applications. It underpins key facilities, infrastructure, and hardware from unauthorized
Finally, supply chain security is a critical layer. AI systems
sectors and must be secured to reduce risk, access, damage, or interference.
depend on globally distributed hardware, software, and
enable trusted deployment, and support
logistics networks, making secure-by-design hardware,
sovereignty. trusted suppliers, and end-to-end chain-of-custody Logical and cybersecurity. Encompasses access
controls essential. controls and defensive measures that govern system
A secure AI stack allows governments and organizations use and protect digital assets from unauthorized access
to adopt AI confidently while maintaining control over Governments need to consider security or compromise.
sensitive systems and data. In this context, security
across the lifecycle of AI
enables sovereignty, allowing nations to align AI use
Export controls. Legal and compliance measures
with their values and regulations without fragmenting Policy should focus on managing risk across the entire
that restrict the transfer, access, or use of sensitive
global systems. lifecycle, prioritizing real-world use, and ensuring security
technologies in accordance with national security and
scales with innovation. Governments can adopt these
Microsoft approaches AI security as a full-stack challenge, regulatory requirements.
globally applicable principles:
combining physical and cyber protections, secure supply
chains, continuous testing, and strong governance to 1. Adopt a full-stack, lifecycle-based security approach.
Supply chain security. Secure, transparent supply chains
deliver defense-in-depth across the entire lifecycle. Governments should define AI security requirements
are essential to protecting AI systems from tampering,
across the entire lifecycle, from infrastructure and data
disruption, and compromise across their lifecycle.
Taking a lifecycle approach to AI security to models and deployment. Policies should focus on
where risk is highest and ensure that security controls
At the infrastructure layer, physical and hardware security evolve over time through continuous monitoring Red teaming and evaluations. Structured testing
are foundational. Risk-based zoning, insider threat and evaluation. activities that assess system behavior and resilience by
programs, and secure hardware lifecycle management
2. Prioritize system-level assurance, not just model identifying weaknesses, misuse potential, and failure
ensure that sensitive compute and data-bearing assets
testing. Security frameworks should move beyond modes on an ongoing basis.
are protected from tampering or compromise.
testing AI models in isolation and instead assess
At the system and model layer, cybersecurity controls how systems behave in real-world deployment
Governance policies. Encompasses the policies, oversight
extend across training, deployment, and inference. environments. This includes interactions between
structures, and decision-making processes that guide
This includes encryption of critical artifacts such as models, tools, data, and users, as well as ongoing
development and deployment.
model weights, strong identity and access management, post-deployment evaluations.
network segmentation, and real-time monitoring for 3. Align international standards to enable secure,
anomalous behavior. AI-specific safeguards such as scalable adoption. Countries should work toward
dataset validation, partitioning of training weights, interoperable, risk-based AI security standards “
and workload isolation help mitigate risks unique to grounded in existing frameworks. Alignment enables
AI systems. trusted cross-border collaboration, reduces A secure AI stack allows governments
fragmentation, and supports the safe diffusion
Securing AI requires continuous evaluation, testing, and organizations to adopt AI confidently
of AI technologies globally.
red teaming, and governance. Lifecycle-based testing, while maintaining control over sensitive
including red teaming and post-deployment monitoring, systems and data.

|     |     | Introduction | AI  | The threat landscape | Cybercrime | Resilience | Appendix |
| --- | --- | ------------ | --- | -------------------- | ---------- | ---------- | -------- |
Securing the AI ecosystem
6202 tropeR esnefeD latigiD tfosorciM
| The agentic defense stack:  | Figure 1. What observed prompts most  |     |     |           |                   |                     |     |
| --------------------------- | ------------------------------------- | --- | --- | --------- | ----------------- | ------------------- | --- |
|                             |                                       |     |     | Risk area | What attackers do | What defenders need |     |
often try to achieve
Connecting attack goals to
The goals shown describe what observed prompts
controls Prompt   Inject instructions through  Prompt injection detection,
tried to achieve, while a single attempt can involve
|     |     |     |     | and intent   | prompts, content, files,  | payload inspection, intent  |     |
| --- | --- | --- | --- | ------------ | ------------------------- | --------------------------- | --- |
several risk areas. For example, an attempt to misuse a
|                                         |                                                         |     |     | manipulation | or memory to redirect  | validation, output review |     |
| --------------------------------------- | ------------------------------------------------------- | --- | --- | ------------ | ---------------------- | ------------------------- | --- |
| Enterprises are increasingly adopting   | connected tool to extract customer records can involve  |     |     |              |                        |                           |     |
the agent
| AI agents. Microsoft has observed 88% of  | both goal hijacking/downstream tools and sensitive  |     |     |     |     |     |     |
| ----------------------------------------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
data exfiltration.
enterprises are already experimenting with
|                                            |                                   |     |      | Sensitive     | Drive the agent to read or  | Sensitivity-aware retrieval,  |     |
| ------------------------------------------ | --------------------------------- | --- | ---- | ------------- | --------------------------- | ----------------------------- | --- |
| agents, and 82% of leaders plan broader    | Key                               |     | %    |               |                             |                               |     |
|                                            |                                   |     |      | data exposure | return content beyond its   | response inspection, data     |     |
| rollouts within the next 12 to 18 months.  | A  Malicious use/policy violation |     | 45%  |               |                             |                               |     |
|                                            |                                   |     |      |               | sanctioned scope            | loss prevention (DLP)         |     |
Industry projections point to roughly 1.3  on inputs and outputs,
|                                        | B  Sensitive data exfiltration |     | 17%  |     |     |                |     |
| -------------------------------------- | ------------------------------ | --- | ---- | --- | --- | -------------- | --- |
| billion agents in production by 2028.  |                                |     |      |     |     | memory scoping |     |
|                                        | C  System prompt leakage       |     | 14%  |     |     |                |     |
More agents bring more entry points for threat actors.
|     | D  Goal hijacking/ downstream tools |     | 12%  |     |     |     |     |
| --- | ----------------------------------- | --- | ---- | --- | --- | --- | --- |
For agents to fulfill their tasks, they need access to  Identity and   Impersonate a sub-agent,  Verifiable agent identity,
business systems and resources, increasing the need for  E  System-internals leakage 11%  privilege   reuse stolen credentials,  mutual authentication,
effective security controls, governance, and oversight.  compromise or chain privileges  scoped credentials,
F  Resource exhaustion / financial harm 1%  across agents least privilege
Each agent needs its own identity, not a credential
borrowed from a human employee. Protecting AI
F
agents in 2026 is therefore an execution question of
inventorying, identifying, and governing every agent,  Excessive   Coax the agent  Tool allow-listing, runtime
with defenders able to attribute, revoke, and enforce least  agency into chaining tools  gating, action policy,
E
|     |     |     |     |     | or actions beyond  | anomaly detection |     |
| --- | --- | --- | --- | --- | ------------------ | ----------------- | --- |
privilege at scale.
sanctioned behavior
The agentic defense stack: Five risk classes  D
that define the 2026 attack surface
|     |     |     |     | Operational   | Tamper with configuration,  | Immutable logs, signed  |     |
| --- | --- | --- | --- | ------------- | --------------------------- | ----------------------- | --- |
A
|     |     |     |     | integrity | system prompts, memory,  | configuration, change  |     |
| --- | --- | --- | --- | --------- | ------------------------ | ---------------------- | --- |
Effective protection requires consistent enforcement of
controls across deployed agents. C training data, supply chain,  governance, supply
|     |     |     |     |     | or logs | chain attestation |     |
| --- | --- | --- | --- | --- | ------- | ----------------- | --- |
Malicious or policy violating use includes attempts to
generate harmful or prohibited content. Illustrative
B
examples include drafting phishing emails or generating
fraudulent invoices.
Source: Microsoft observation of prompts against generative
AI agents (February to May 2026).
22

|     |     | Introduction | AI  | The threat landscape | Cybercrime | Resilience | Appendix |
| --- | --- | ------------ | --- | -------------------- | ---------- | ---------- | -------- |
Securing the AI ecosystem
6202 tropeR esnefeD latigiD tfosorciM
|                                                     | Figure 2. Top attack vector categories   |     | There are three risks as organizations adopt agents: |     |     |     |     |
| --------------------------------------------------- | ---------------------------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
| The agentic defense stack: Connecting attack goals  |                                          |     |                                                      |     |     | “   |     |
to controls (continued) in telemetry data on AI workloads 1. Ungoverned agent proliferation. The number
of agent identities often grows faster than
Organizations
| Inside the agent attack surface:   | Malicious link injection, tool and AI agent section  |     |     |     |     |     |     |
| ---------------------------------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
the organization’s ability to track them.
| Where attack activity is concentrating | abuse, and prompt subversion account for the majority  |     |                                                       |     |     |                   |     |
| -------------------------------------- | ------------------------------------------------------ | --- | ----------------------------------------------------- | --- | --- | ----------------- | --- |
|                                        |                                                        |     | Without centralized visibility, agent sprawl creates  |     |     | need systems and  |     |
of observed attack activity on AI workloads.
The agent attack surface in 2026 was dominated by a  even greater risks than shadow IT.
controls that enforce
| small number of high-volume techniques. In telemetry  | F   |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
2. Overprivileged access. Agents acquire access over
data from Azure AI workloads, four classes of techniques  policy in real time,
time that’s rarely revoked. Unlike human users, who
accounted for roughly 90% of observed attack activity:
|     |     |     | face governance controls, agents can accumulate  |     |     | keeping every action  |     |
| --- | --- | --- | ------------------------------------------------ | --- | --- | --------------------- | --- |
E
• Malicious link injection routed through model and tool  broad access that persists and becomes stale after
aligned to the agent’s
| outputs (52%) |     |     | the agent’s original purpose has evolved.  |     |     |     |     |
| ------------- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
D
• Jailbreak and safety bypass attempts (16%) 3. No human accountability. When an agent acts  objective, its intent,
• Tool and agent abuse (12%) autonomously, the question of who’s responsible
and the organization’s
for its actions becomes critical. Without a human
• Identity and credential abuse (10%)
C boundaries.
|     |     | A   | accountable for each agent’s access (a sponsor),  |     |     |     |     |
| --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- |
Organizations also need to plan for agent-to-agent
there’s no one to contact when something
spoofing, a rising technique that is expected to grow as
goes wrong.
multi-agent deployments scale. In this technique, one
B
agent impersonates another (or its owner) to slip past
A risk-based approach to agent governance
trust boundaries across a multi-agent graph.
To deploy agents safely and meet governance
Agents create different challenges from  objectives, security admins need to take a risk-based
|     | Key |     | %   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
approach to identifying, authorizing, and reviewing
traditional software
|     | A  Malicious link injection and exfil |     | 52%  agent activities, with automated mitigations to  |     |     |     |     |
| --- | ------------------------------------- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
When a human employee changes roles, organizations  remediate critical risks:
| have well-established processes, including pre-configured  | B  Jailbreak and  safety bypass |     | 16%  |     |     |     |     |
| ---------------------------------------------------------- | ------------------------------- | --- | ---- | --- | --- | --- | --- |
1. Start with identity. Every agent must have a distinct,
access entitlements, manager approvals, periodic  C  Tool and  agent abuse 12%  auditable identity that carries metadata about who
recertification, and regular access reviews. But as agents  created the agent, its purpose, and its sponsor.
| acquire new skills, the boundaries of what they can do  | D  Identity and  credential abuse |     | 10%  |     |     |     |     |
| ------------------------------------------------------- | --------------------------------- | --- | ---- | --- | --- | --- | --- |
2. Enforce human accountability. When an agent’s
shift in ways that may not trigger the same governance
|     | E  Prompt injection and instruction subversion |     | 8%  sponsor changes, agent accountability must be  |     |     |     |     |
| --- | ---------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- | --- |
checkpoints. Organizations need systems and controls
re-evaluated and transferred automatically to a new
| that enforce policy in real time, keeping every action  | F  Reconnaissance and data probing |     | 2%  |     |     |     |     |
| ------------------------------------------------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
sponsor. No environment should ever have an agent
aligned to the agent’s objective, its intent, and the
|     | Source: Telemetry data on AI workloads (90 day window, 2026). |     | without a human to answer for it.  |     |     |     |     |
| --- | ------------------------------------------------------------- | --- | ---------------------------------- | --- | --- | --- | --- |
organization’s boundaries. Without those controls,
autonomous agents operate unchecked, becoming
unmanaged, potentially overprivileged, with a growing
governance gap.
23

24
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Securing the AI ecosystem
The agentic defense stack: Connecting attack goals The path forward for organizations and Learn more
to controls (continued) policy makers
3. Apply least-privilege access from day one. As AI agents proliferate, an organization’s governance Frontier Governance Framework
Agents should receive only the access they need plans cannot rely on platform-specific controls
to perform their tasks, with access assignments alone. Interoperable standards play a critical role
Efforts to share best practices on AI measurement and evaluations driven
time-limited and subject to approval workflows. in enabling trusted collaboration between agents,
forward through the International Network for Advanced AI Measurement, Evaluation
New permissions should go through governance services, and across organization boundaries.
and Science
controls appropriate to what’s being granted, Effective agent governance also requires internal
and unused access should be revoked to prevent alignment. Organizations that do not already have
permissions creep. a suitable forum should form a dedicated agent Frontier Model Forum: Advancing frontier AI safety and security
4. Automate lifecycle management. Manual oversight of governance committee, representing application owners,
agent identities isn’t feasible at scale. Automated policies data custodians, business process designers, compliance
Advancing AI evaluation with the Center for AI Standards (US)
should verify the ongoing need for each agent, specialists, and agent sponsors. This group should work
and Innovation and the AI Security Institute (UK)
whether its access is still appropriate, and confirm it together to preserve controls, adapt processes to agent
still has a valid human sponsor. Organizations should risk, and ensure technical controls support day-to-
automatically disable and clean up unnecessary agents day operations.
and their access permissions.
For industry and policymakers, there are two near
5. Govern consistently across platforms and services.
term priorities: faster convergence on practical security
Consistent governance policies need to apply
guidance and clearer accountability for deployment
regardless of each agent’s origin. Using different rules
decisions. In the near term, governments can help by
for different platforms creates audit and visibility gaps
supporting common taxonomies, evaluation methods,
that adversaries can exploit.
and risk-management expectations that reflect how
6. Require agent-to-agent authentication. Sub-agents agents actually operate across memory, tools, and
must prove identity to one another, not only to the connected systems. Early guidance should enable
originating human session. Unauthenticated cross- innovation while setting credible expectations for
agent traffic is how a single compromise propagates security, auditability, and human oversight before
through a multi-agent graph. more formal standards and regulatory frameworks
7. Issue per-tool scoped credentials. Use short-lived are fully established. Industry, in turn, should translate
secrets bound to a single tool invocation, not long- those principles into deployable controls, transparent
lived tokens that hold every privilege the agent might testing practices, and governance models that assign
ever need. responsibility for high-risk uses.
8. Treat revocation latency as a measured outcome.
When an agent or its owner is compromised, the
time to revoke across identity, posture, and threat
protection controls is the operational metric that
determines incident impact.

25
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Securing the AI ecosystem
Memory poisoning: Email is a key pathway for memory poisoning Memory poisoning is a reproducible, low-complexity, “
cross-session attack surface. To respond, defenders
Persistence in the agentic age The dominant memory-poisoning pathway the Red Team need to:
has observed is XPIA from externally-sourced content Once memory is
• Create architectural separation between trusted and
delivered through sources that the agent is expected to
Assistants and task agents rely on long-term untrusted write paths so that untrusted data cannot shared across tools,
consume as part of normal operation, most commonly
memory to personalize answers, preserve email. The attacker embeds instructions that the system trigger writes to a trusted memory store. This includes tenants, or agents,
restricting memory write tool calls once untrusted data
context across sessions, and coordinate retrieves and blends into the same reasoning context
has entered an agent’s context. a single poisoning
as the user’s request. The model can then be induced
multi-step work. In many memory
to create a new memory entry or modify an existing • Implement a memory architecture that treats agent- incident can influence
implementations, the agent is authorized one that stores attacker-influenced behavioral guidance derived preferences separately from explicit user
downstream
to insert, update, and delete entries on the that can persist across sessions and be reintroduced as instructions that can modify safety behavior. Storing in
user’s behalf. trusted context in later interactions. memory how a user should be referred to can be automation that
agent-derived, instructions to bypass a HITL control
Human-in-the-Loop (HITL) controls alone cannot protect the original victim
should not.
Letting the model write to its own long-term state from
memory writes. In red team testing, poisoned entries
a context it does not control removes the boundary • Monitor in a way that treats the memory store as never sees.
have been used to suppress or bypass these controls,
between session input and durable system state. a high-value asset whose integrity determines the
append unauthorized steps to legitimate tasks, and
This means an attacker who can place content anywhere integrity of everything downstream. This includes
subtly steer subsequent responses or outputs. The Red
the agent will read can also often place content giving users the ability to audit and control memory
Team has also observed instances where HITL is triggered
anywhere the agent will remember. That content is then entries at a granular level and collecting telemetry
but ignored by the agent and HITL being bypassed by
retrieved as trusted context in future sessions, across around memory actions.
a policy stored in memory in the same attack chain.
chats, and in some cases across task handoffs between
The underlying issue is that the control and the thing it
agents. The blast radius grows with agentic coupling.
guards share a failure mode.
Once memory is shared across tools, tenants, or agents,
a single poisoning incident can influence downstream
automation that the original victim never sees.

|     |     | Introduction | AI  | The threat landscape | Cybercrime | Resilience | Appendix |
| --- | --- | ------------ | --- | -------------------- | ---------- | ---------- | -------- |
Securing the AI ecosystem
6202 tropeR esnefeD latigiD tfosorciM
| Overreliance on Human-in-the- | What works when it comes to HITL |     |     |     |     |     |     |
| ----------------------------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
“
| Loop (HITL) is a systemic risk | • Deterministic, policy-controlled invocation of HITL  |     |     |     |     |     |     |
| ------------------------------ | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
ensures that it can’t easily be bypassed by someone
As agents gain
manipulating the underlying model. This should also
| HITL controls are a key component of AI  |     |     | memory, tool use,  |     |     |     |     |
| ---------------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |
be supported by deterministic controls that block
system security, and their importance has
|                                             | patterns of activity that shouldn’t be approved under  |     | and autonomy, the  |     |     |     |     |
| ------------------------------------------- | ------------------------------------------------------ | --- | ------------------ | --- | --- | --- | --- |
| only increased with the adoption of highly  | any circumstances.                                     |     |                    |     |     |     |     |
bar to bypass HITL
| privileged agentic AI systems. HITL is now  | • HITL with user experiences that support the users,  |     |     |     |     |     |     |
| ------------------------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
is dropping and
with clear explanations of what is being requested
the default mitigation whenever a new
and why, with relevant context and a chain of how the
the blast radius
| agentic capability outpaces its classifiers:  | decision to ask for the action was reached. |     |     |     |     |     |     |
| --------------------------------------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
“enable the capability but ask the user  of a single bypass
• Mitigations to prevent fatigue, including controls at
before doing anything sensitive”.  the user level and telemetry to allow detection and  is rising.
response to HITL fatigue attacks.
The pattern is embedded across chat bots, automated
workflow AI, and complex agentic systems. However, the
decision to invoke the HITL control is often made by the
same system an attacker can manipulate, using context
that has already mixed trusted and untrusted content.  Three key HITL failure modes the Red Team has observed
HITL controls can be easily bypassed by
|     | Category  | Example technique  |     |     |     |     |     |
| --- | --------- | ------------------ | --- | --- | --- | --- | --- |
adversaries
|     | Prompt injection and  | • Memory-poisoned consent  |     |     |     |     |     |
| --- | --------------------- | -------------------------- | --- | --- | --- | --- | --- |
As agents gain memory, tool use, and autonomy, the bar
probabilistic invocation
| to bypass HITL is dropping and the blast radius of a single  |     | • Injected approvals      |     |     |     |     |     |
| ------------------------------------------------------------ | --- | ------------------------- | --- | --- | --- | --- | --- |
| bypass is rising. Defense-in-depth must move upstream        |     | • Act-then-ask inversion  |     |     |     |     |     |
into provenance, isolation, deterministic invocation,
• Chaining low-risk actions to reach a high-risk outcome
and classifier-backed policy or else the next class of
| incidents will be ones where the user “approved” the  | Inadequate         | • Tenant-wide always-allow  |     |     |     |     |     |
| ----------------------------------------------------- | ------------------ | --------------------------- | --- | --- | --- | --- | --- |
| breach themselves.                                    | human involvement  |                             |     |     |     |     |     |
• Illegible model-generated summaries
• No fatigue mitigations
• Blanket session approvals
|     | Control-quality issues  | • HITL that doesn’t fire (UI-state-dependent)  |     |     |     |     |     |
| --- | ----------------------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
• Fires but is ignored
• Starting context effect on chain-of-thought (CoT) vigilance
• Time-of-check/Time-of-Use (TOCTOU) on computer use agents
26

27
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
wen
eht
sa
IA
ecafrus
kcatta
AI-assisted threats AI browsers as an enterprise The shift in browser use changes the
enterprise risk equation
risk: Elevated permissions with
An emerging threat category is attacks
Traditional security models were built around a clearer
that weaponize the trust that users and limited security visibility
separation between user intent, application behavior,
organizations place in AI tools, AI-assisted and system-level execution. AI browsers compress
workflows, and AI-generated identity as the AI browsers are becoming a material those boundaries. They can read untrusted web content,
reason over that content, and then take action inside live
primary exploitation mechanism. Recently, enterprise risk because they combine three
enterprise sessions using the user’s existing authority.
Microsoft has observed three specific conditions security leaders rarely face at That creates a high-trust environment where abuse can
patterns in this category: the same time: broad adoption, high-trust look operationally normal.
access, and limited security visibility.
A malicious or manipulated action may present as
Malicious AI applications
ordinary software-as-a-service (SaaS) usage rather
Malicious AI applications are a newly emerging category The browser is already the primary workspace for modern
than malware execution, making it harder for security
of malware disguised as legitimate AI productivity organizations—recent industry research indicates that
teams to distinguish between legitimate productivity
tools that exploit the surge in AI adoption to earn user roughly 85% of work now happens there. At the same
and compromise. Adversaries are already targeting
trust. EvilAI is the first of a class we expect to grow as time, AI browsers are rapidly becoming part of the
this vector. In an analysis conducted in May 2026, we
AI tooling becomes a more attractive lure. EvilAI comes enterprise technology stack, with Microsoft observing
observed AI browsers as the initial infection vector in
complete with professional branding and valid code- daily use across more than 40% of organizations in
incidents involving 57 distinct malware families. We also
signing certificates, but once installed, it silently deploys a its dataset.
documented a malicious extension campaign that
persistent backdoor that steals credentials, payment data,
The web browser now acts as a powerful computer affected more than 900,000 installs across Chromium-
and sensitive files.
program: it runs heavy code, stores data, and performs based browsers (including agentic browsers) and showed
Malicious browser extensions impersonating AI brands complex tasks. In AI-enabled deployments, it is confirmed telemetry activity across more than 20,000
Threat actors are increasingly exploiting trusted AI brand increasingly an execution environment with access to enterprise tenants. The campaign harvested browsing
names to deceive users. Microsoft observed a malicious authenticated sessions, cookies, OAuth state, page history, AI chat histories, prompts and responses, and
browser extension impersonating the AI answer engine content, downloads, clipboard data, and delegated session material while blending exfiltration into ordinary
Perplexity AI that silently collected user search activity. actions performed on behalf of users—all of which are browser traffic.
Because the user still landed on normal results, the attractive to attackers.
interception was invisible.
Malicious AI extensions that harvest LLM data
Malicious browser extensions masquerading as
AI assistants have reached nearly 900,000 installs
and affected more than 20,000 enterprise tenants.
These extensions silently collect URLs, page content,
metadata, and AI chat histories from platforms such
as ChatGPT and DeepSeek, exposing proprietary code,
business strategies, and other sensitive information
provided to the platform by users.

28
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
AI as the new attack surface
Cross-signal threat intelligence “ Can AI just find and fix everything first? With signal cross-correlation, the opposite occurs:
an attacker moving across multiple systems leaves
is key A natural question is whether defenders can neutralize a cross-system footprint. These are patterns visible
The degree to which the adversarial discount by using AI to find vulnerabilities across systems even if no single system shows a
before attackers do. Anthropic’s Project Glasswing and AI is reshaping cybersecurity investment a defender’s systems complete picture. Each new system becomes a detection
the Claude Mythos Preview model have the ability to
opportunity instead of a new liability.
decisions for both attackers and defenders share and correlate identify zero-day vulnerabilities at scale. If defenders
by changing the economics of adversarial have access to this capability, why doesn’t the adversarial Formal modeling of this mechanism demonstrates a
threat intelligence
discount disappear? striking result: with full signal cross-correlation within an
adaptation.
is one of the highest- organization, the defender’s marginal effectiveness per unit
As our Red Team has shown, the answer lies in the
of investment is independent of how many systems they
Attackers have always benefited from an “adversarial leverage strategic difference between finding a vulnerability and eliminating
must protect. The surface-count disadvantage disappears.
discount”. That is, the value of defensive technology it. Patching requires coordinating across software
variables under the This points to concrete architectural interventions: unified
erodes as attackers adapt to it, not because of a product maintainers, testing under operational conditions,
detection infrastructure, cross-product telemetry pipelines,
defect or temporary gap, but because determined defender’s control . managing uptime risk, and deploying across multiple and shared behavioral baselines.
adversaries strategically learn to exploit deployed environments. While attackers adapt in real time to
defenses over time. deployed defenses, defenders must convert discovered AI-augmented attacks tend toward complex, multi-stage,
vulnerabilities into safe system changes. This asymmetry multi-surface campaigns, but these generate cross-surface
AI amplifies this dynamic by shifting parts of the attack
ensures the adversarial discount persists even with the artifacts. When defenders invest sufficiently in signal
lifecycle—such as vulnerability discovery, exploit
help of AI. correlation, they make complex attacks easier to detect.
development, and lateral movement—from economies of
skill toward economies of scale in compute. This increases
the speed and magnitude of adversarial discount. Signal cross-correlation is a decisive variable Organizations need to consider
system-level intelligence
Given the value of a target, what determines breach The degree to which a defender’s systems share and
probability is the ratio of offensive to defensive correlate threat intelligence is one of the highest- Signal correlation is an architectural capability that
effectiveness—a ratio that threat actors are actively leverage strategic variables under the defender’s transforms isolated detections into a connected defense
working to increase. In addition to making attacks control. This sharing, or signal cross-correlation, is ecosystem. Organizations need to consider how
more potent across the board, attacker AI specifically the most powerful of all the factors over which the effectively intelligence from one system informs another.
targets whatever the defender has deployed. A defender defender has control. Consider a large organization As environments expand across endpoints, identities,
who invests in detection gives the attacker something protecting hundreds of applications, endpoints, and email, cloud services, networks, and applications, the
precise to study and evade. A defender who invests cloud services. If each system’s telemetry is analyzed value of each security signal increases when it can be
in triage gives the attacker an incentive to overwhelm in isolation, adding a new system adds a detection correlated with others. The return on security investments
it. The defender’s own investment feeds the attacker’s burden without contributing to the defense of existing is therefore driven not only by the quality or quantity
incentive to invest. This creates an arms race. ones. Defense effectiveness per system dilutes as the of individual tools, but by the organization’s ability to
environment grows. unify telemetry and intelligence across its environment.
Each additional source of visibility strengthens the
value of every other source, improving detection,
accelerating response, and providing broader context for
security decisions.

29
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
AI as the new attack surface
Cross-signal threat intelligence is key (continued) From capability to Closing the vulnerability discovery
gap has become a strategic imperative
At enterprise scale, integration itself becomes a defensive responsibility: Securing the
advantage. When endpoint, identity, cloud, application, Organizations must modernize vulnerability management
email, network, data, and AI-workload signals are AI-driven digital ecosystem practices, accelerate remediation timelines, and embed
combined with threat intelligence and AI reasoning, each security throughout the AI lifecycle. Recent advances in
additional source contributes context to the rest of the Frontier AI systems are reshaping AI-driven security systems demonstrate how automated
estate and enables faster, coordinated action. The value techniques can identify vulnerabilities earlier, validate
cybersecurity by dramatically accelerating
comes from the system working together, not from any exploitability, and prioritize remediation based on real-
single control in isolation. the discovery, analysis, and exploitation of world risk rather than sheer volume.
software vulnerabilities.
A defining development in this evolution is the rise of The same principle applies beyond
multi-model, multi-agent AI systems that combine the
This creates a dual-use reality: the same capabilities that
individual organizations
strengths of specialized models working collaboratively
allow defenders to identify and remediate weaknesses
toward shared security objectives. By distributing tasks
Cross-organizational signal correlation enables the at unprecedented scale can also be leveraged by
across coordinated agents and leveraging different
identification of campaign-level activity that would adversaries to conduct offensive cyber operations.
model capabilities, these systems have demonstrated
otherwise remain invisible within any single environment. Whether AI ultimately shifts the balance in favor of
significant improvements in efficiency, scalability, and
No organization possesses a complete view of the threat defenders or attackers will depend on the choices
cost-effectiveness compared to traditional or single-
landscape; each captures only a fraction of the available governments, industry, and civil society make today.
model cyber defense approaches. Emerging deployments
signals. The collective benefit created through trusted
At the same time, frontier AI is creating a new class show that such architectures can accelerate vulnerability
information sharing exceeds what any organization can
of national security risk driven by speed, autonomy, discovery, improve analysis quality, and support faster
achieve independently. Policymakers can help unlock
adaptability, and increasingly sophisticated cyber remediation decisions across increasingly complex digital
these benefits by encouraging mechanisms that support
capabilities. Risk management frameworks, including environments. These advances reinforce an important
secure collaboration, including legal safe harbors for
Microsoft’s Frontier Governance Framework, are lesson for the AI era: competitive advantage increasingly
information sharing, common anonymization standards,
converging around a set of high-impact domains, lies not in any individual model, but in the integration
and investments in shared detection and threat
including offensive cybersecurity, chemical, biological, of models, tools, and processes into cohesive defense
intelligence infrastructure. Together, these approaches
radiological, and nuclear (CBRN) risks, and advanced systems capable of operating at machine speed.
strengthen not only individual organizations, but the
autonomous behaviors. These risks are dynamic and
resilience of the broader digital ecosystem. However, model-level capability evaluations alone
evolve alongside technological progress, requiring
are not sufficient. National security risks depend not
continuous evaluation and adaptation rather than one-
only on what a model can do in isolation, but on how
time assessment.
it is integrated into broader systems and operational
environments. Current evaluation approaches often focus
on narrow technical tasks performed under controlled
conditions, overlooking the strategic intent, complexity,
and adaptability of real-world threat actors.

30
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
AI as the new attack surface
From capability to responsibility: Securing An emerging consensus is beginning to shape the future 3. Reinforce foundational cybersecurity practices. “
the AI-driven digital ecosystem (continued) of frontier AI governance: Core security measures—including Zero Trust
• Risk management should be capability-based, dynamic, architectures, strong identity protections, secure-
Without incorporating government and intelligence- and evidence-driven. by-design principles, and rapid patching—remain No single institution
informed threat models, assessments may underestimate • National security testing must be collaborative, drawing the foundation upon which AI-enabled security has the expertise,
how advanced AI systems could be misused, leaving capabilities must be built.
critical gaps in safeguards and defensive preparedness. expertise from both the public and private sectors. visibility, or authority
4. Risk-based testing and phased deployment of
• Governance must extend beyond individual
advanced AI systems. High-capability AI models with required to manage
models to encompass complete systems and
Why public–private collaboration matters cybersecurity-relevant capabilities should undergo
deployment contexts. frontier AI risks alone.
rigorous pre-deployment assessments that evaluate
No single institution has the expertise, visibility, or • Evaluation should be continuous and adaptive as
misuse scenarios, national security implications,
authority required to manage frontier AI risks alone. models and threat landscapes evolve.
and potential pathways to harm. Controlled release
Governments provide national security expertise,
• Public–private partnerships are essential for effective mechanisms can help balance innovation with
intelligence insights, and regulatory capabilities.
testing, mitigation, and trust-building. risk mitigation.
Industry contributes technical knowledge, operational
experience, and direct access to frontier systems. • Shared methodologies, datasets, and evidence 5. Deepen international cooperation on AI security
Academic institutions and independent researchers frameworks improve consistency, transparency, and and cyber resilience. Governments should expand
advance testing methodologies and generate critical confidence in evaluation outcomes. collaboration on AI security standards, threat
evidence on emerging threats. intelligence sharing, testing methodologies, and
Policy priorities for governments coordinated approaches to emerging cyber risks,
As a result, effective AI security depends on structured helping create common expectations for responsible
public–private collaboration. Initiatives such as the AI To ensure AI strengthens security rather than undermines AI development and deployment.
Network for Advanced AI Measurement, Evaluation it, governments should focus on five priorities:
and Science, the Frontier Model Forum, and national AI 1. Accelerate AI-enabled, risk-prioritized vulnerability As frontier AI capabilities continue to advance, the
security research institutes are helping align evaluation management. Governments should encourage central challenge is no longer simply developing more
priorities, testing methodologies, and risk-management a transition from volume-based approaches capable systems—it is ensuring those capabilities are
approaches. Similarly, partnerships between Microsoft to risk-based vulnerability management deployed responsibly. Securing the AI-driven digital
and organizations such as the US Center for AI Standards supported by AI-driven discovery, validation, and ecosystem will require a combination of advanced
and Innovation and the UK’s AI Security Institute prioritization technologies. defensive technologies, rigorous governance, resilient
demonstrate the value of jointly testing frontier models, cybersecurity foundations, and sustained collaboration
2. Invest in automated remediation and ecosystem-
assessing safeguards, and improving methodologies for across governments, industry, and academia. The choices
wide resilience. Public policy should support
evaluating national security and offensive cyber risks. made today will determine whether AI becomes a force
automated patching, coordinated vulnerability
Microsoft’s External Red Teaming for AI (EXTRA) program multiplier for cyber defense or a catalyst for systemic
disclosure, and stronger support for open-source
further supports independent research by providing AI cyber risk.
maintainers who play a critical role in global
safety and security researchers with access to frontier
software security.
technologies to advance the science of AI risk evaluation.

|     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- |
2
6202 tropeR esnefeD latigiD tfosorciM 6202 tropeR esnefeD latigiD tfosorciM The threat  The threat landscape in 2026  32
|     |     |     |     | Cyberattacks typically hit known hotspots  |     | 32  |
| --- | --- | --- | --- | ------------------------------------------ | --- | --- |
|     |     |     |     | Emerging threats                           |     | 36  |
|     |     |     |     | Nation state and geopolitical threats      |     | 38  |
landscape
|     |     |     |     | Regional sample of activity level observed             |     | 38  |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
|     |     |     |     | Significant trends in state-sponsored threat activity  |     | 39  |
(China, Iran, Russia, North Korea)
|     |     |     |     | How modern intrusions begin              |     | 44  |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- |
|     |     |     |     | The initial access landscape             |     | 44  |
|     |     |     |     | ClickFix is evolving                     |     | 45  |
|     |     |     |     | Voice phishing attacks go mainstream in  |     | 46  |
chat applications
|     |     |     |     | The cost of delayed patching                   |     | 47  |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| ““  |     |     |     | Impersonation is becoming more sophisticated   |     | 49  |
|     |     |     |     | Business contact impersonation: The new “BEC”  |     | 50  |
Cyberthreats do not respect borders,
|     |     |     |     | Emerging threat of network edge infrastructure  |     | 50  |
| --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
and neither can our response. Through
|     |     |     |     | Information stealers: A continued threat  |     | 52  |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- |
our collaboration with Microsoft and the
|     |     |     |     | Detection, intelligence, and disruption  |     | 54  |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- |
CSIRTAmericas network, we are helping
|     |     |     |     | Operationalizing detection at scale  |     | 54  |
| --- | --- | --- | --- | ------------------------------------ | --- | --- |
equip countries across the Americas with
timely threat information that strengthens  How shared threat intelligence is reshaping   55
the fight against fraud
collective cyber resilience and supports more
|     |     |     |     | Targeting fraud’s backbone  |     | 57  |
| --- | --- | --- | --- | --------------------------- | --- | --- |
coordinated responses to emerging threats.
|     |     |     |     | Securing the foundations  |     | 59  |
| --- | --- | --- | --- | ------------------------- | --- | --- |
Diego Subero, Cybersecurity Section Officer
Organization of American States  The race to retire NTLM  59
|     |     |     |     | The cloud threat landscape                       |     | 59  |
| --- | --- | --- | --- | ------------------------------------------------ | --- | --- |
|     |     |     |     | Rethinking defense models to tackle intrusions   |     | 61  |
in hybrid cloud environments
31 31

|     | Introduction  | AI  | The threat landscape  | Cybercrime  |     | Resilience  | Appendix |
| --- | ------------- | --- | --------------------- | ----------- | --- | ----------- | -------- |
  epacsdnal taerht ehT  6202 ni
Cyberattacks typically   Countries where customers are most frequently impacted by cyber threats
6202 tropeR esnefeD latigiD tfosorciM
(January 2026–June 2026)
hit known hotspots
While cyberattacks threaten every
country, specific hotspots persist year
over year, driven by target density and
geopolitical interests.  9
10
For example, Ukraine and NATO-aligned countries
remain focal points for Russian activity, while   5
3
Chinese state actors concentrate heavily on the
Indo-Pacific, the United States, and strategic  8
1
technology hubs. Meanwhile, Microsoft has observed
2
growing cybercriminal activity impacting Latin America,
|     |     |     |     | 6   |     | 4   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Africa, and Southeast Asia—regions where defenses
7
may be less mature at the same time that digital  12
transformation is accelerating.
11
| Scale of impact: % of total  |     | %     |                          | %    |                  |     | %    |
| ---------------------------- | --- | ----- | ------------------------ | ---- | ---------------- | --- | ---- |
| 1  United States             |     | 25.5  | 5  United Kingdom        | 3.8  | 9  Canada        |     | 1.8  |
| 2  Israel                    |     | 7.6   | 6  United Arab Emirates  | 2.8  | 10  Germany      |     | 1.7  |
|                              |     | 4.8   |                          | 2.5  |                  |     | 1.5  |
| 3  Ukraine                   |     |       | 7  India                 |      | 11  Australia    |     |      |
|                              |     | 3.9   |                          | 2.5  |                  |     | 1.5  |
| 4  Taiwan                    |     |       | 8  Japan                 |      | 12  Philippines  |     |      |
Source: Microsoft Threat Intelligence
32

|     |     | Introduction  | AI  | The threat landscape  |     | Cybercrime  | Resilience  |     | Appendix  |
| --- | --- | ------------- | --- | --------------------- | --- | ----------- | ----------- | --- | --------- |
The threat landscape in 2026
 6202 tropeR esnefeD latigiD tfosorciM
|     | Top 10 global sectors impacted by threat actors   |     |     |     | Initial access vectors across two years   |     |     |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
Cyberattacks typically hit known hotspots (continued)
|     | in 2026  |     |     |     | of incident response (IR) findings  |     |     |     |     |
| --- | -------- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
Targets are staying the same
|     | 30%  |     |     |     | 30%  |     |     |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
Threat actors continue to prioritize the same targets:
2025
government, information technology (IT), and research
|     | A   |     |     |     |     |     |     |     | 2026  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
and academia. These sectors represent attractive targets  25%  25%
for both nation-state and cybercriminal actors, largely
| because they:  | 20%  |     |     |     | 20%  |     |     |     |     |
| -------------- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
• Have high-value intelligence
|     | 15%  | B   |     |     | 15%  |     |     |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
• Contain extensive personally identifiable information
| (PII)  |      | C   |     |     |      |     |     |     |     |
| ------ | ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
|        | 10%  |     |     |     | 10%  |     |     |     |     |
• Comprise a sprawling and often under-
monitored infrastructure  D
E  F
|     | 5%  |     | G   |     | 5%  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Have a generally low tolerance for downtime
H
I
At the same time, businesses outside of critical sectors—  0%  J  0%
especially small and medium-sized businesses—remain
|     |     |     |     |     | A   | B  C  D  | E  F  | G  H  | I  J  |
| --- | --- | --- | --- | --- | --- | -------- | ----- | ----- | ----- |
at high risk of cybercriminal activity, from ransomware to
| business contact impersonation (BCI).  | Key  |     |     |     | Key  |     |     |       |       |
| -------------------------------------- | ---- | --- | --- | --- | ---- | --- | --- | ----- | ----- |
|                                        |      |     |     | %   |      |     |     | 2025  | 2026  |
Threat actors are relying less on custom malware
A  Government agencies and services  27  A  None identified  25%  14%
and instead abusing legitimate tools, cloud services,
and administrative functions. This makes detection
|     | B  Information technology  |     |     | 17  | B  Valid accounts  |     |     | 17%  | 13%  |
| --- | -------------------------- | --- | --- | --- | ------------------ | --- | --- | ---- | ---- |
harder because malicious activity often blends in with
C  Research and academia  14  C  Exploit public-facing application  15%  24%
normal user behavior. Adversary-in-the-middle (AiTM)
phishing kits, OAuth app abuse, API exploitation,  9  Social engineering  15%  7%
|     | D  Communications infrastructure  |     |     |     | D   |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
and password spray attacks are now standard across
both criminal and nation-state playbooks. This marks  E  Transportation systems  8  E  External remote services  8%  5%
a major evolution from years past, where endpoint  F  Non-government organization  8  Phishing  7%  23%
F
malware and exploit kits dominated initial access.
G  Defense industrial base  7  G  Drive-by compromise  6%  4%
|     | H  Critical manufacturing  |     |     | 5   | H   |     |     | 3%  | 2%  |
| --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Content injection
|     | I  Financial services  |     |     | 4   | I  Trusted relationship     |     |     | 2%  | 4%  |
| --- | ---------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- |
|     | J  Energy              |     |     | 3   | J  Supply chain compromise  |     |     | 2%  | 4%  |
Source: Microsoft Threat Intelligence  2025 reporting period: July 2024–June 2025; 2026 reporting period:
July 2025–June 2026. Source: Microsoft Threat Intelligence
33

|     |     | Introduction  | AI  | The threat landscape  |     | Cybercrime  | Resilience  | Appendix  |
| --- | --- | ------------- | --- | --------------------- | --- | ----------- | ----------- | --------- |
The threat landscape in 2026
6202 tropeR esnefeD latigiD tfosorciM
Most common MITRE ATT&CK techniques for  Cyberattacks typically hit known hotspots (continued)  Type  Technique
compromise and post-compromise based on
Attackers are targeting well-known CVEs
Microsoft Defender alerting, April to June 2026
|     |     |     |     |     | CVE-2020-1472  |     | An unauthenticated attacker  |     |
| --- | --- | --- | --- | --- | -------------- | --- | ---------------------------- | --- |
Analysis of vulnerabilities based on Microsoft Defender
|     |     |     |     |     | (Netlogon EoP)  |     | could gain domain administrator  |     |
| --- | --- | --- | --- | --- | --------------- | --- | -------------------------------- | --- |
alerting from July 2025 to June 2026 reveals most attacks
access or impersonate domain
linked to potential vulnerability exploitation involved
| Tactic  | Technique  |     |     |     |     |     | member computer accounts.  |     |
| ------- | ---------- | --- | --- | --- | --- | --- | -------------------------- | --- |
well-known, long-disclosed Common Vulnerabilities
and Exposures (CVE). These older vulnerabilities may
|     |     |     |     |     | CVE-2022-22954  |     | An unauthenticated attacker  |     |
| --- | --- | --- | --- | --- | --------------- | --- | ---------------------------- | --- |
Initial Access  T1078 Valid Accounts  be targeted because unpatched systems are easier to
|     |     |     |     |     | (VMware  |     | with network access could  |     |
| --- | --- | --- | --- | --- | -------- | --- | -------------------------- | --- |
access or because widely available exploit code and tools
|     |     |     |     |     | Workspace ONE)  |     | trigger a server-side template  |     |
| --- | --- | --- | --- | --- | --------------- | --- | ------------------------------- | --- |
Execution  T1059 Command and Scripting Interpreter  incorporating exploit code are commonly weaponized,
injection that may result in RCE.
for example in commodity hacking tools and botnets.
| Persistence  | T1547 Boot or Logon Autostart Execution  |     |     |     |     |     |     |     |
| ------------ | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
These CVEs affect network-exposed or externally  CVE-2021-40444  This zero-day vulnerability could
|                       |                                          | reachable services and are typically high-severity  |     |     | (MSHTML RCE)  |     | enable an attacker to execute  |     |
| --------------------- | ---------------------------------------- | --------------------------------------------------- | --- | --- | ------------- | --- | ------------------------------ | --- |
| Privilege Escalation  | T1548 Abuse Elevation Control Mechanism  |                                                     |     |     |               |     |                                |     |
|                       |                                          | vulnerabilities that enable high-impact outcomes,   |     |     |               |     | arbitrary code by delivering   |     |
specially crafted Microsoft Office
Stealth  T1218 System Binary Proxy Execution  such as remote code execution (RCE), trust bypass, or
|     |     | privilege escalation. The most effective mitigation is rapid  |     |     |     |     | documents that load malicious  |     |
| --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | ------------------------------ | --- |
Defense Impairment  T1222 File and Directory  and consistent patching of internet-facing and critical  ActiveX content when opened
Permissions Modification  systems, as these vulnerabilities are effectively mitigated  by a user.
once vendor updates are applied and systems are
|                    |                    |                    |     |     | CVE-2023-28231  |     | An attacker could force     |     |
| ------------------ | ------------------ | ------------------ | --- | --- | --------------- | --- | --------------------------- | --- |
| Credential Access  | T1110 Brute Force  | properly secured.  |     |     |                 |     |                             |     |
|                    |                    |                    |     |     | (DHCP RCE)      |     | the DHCP Server Service in  |     |
Discovery  T1087 Account Discovery  Windows operating systems
to run malicious code without
Top five most exploited
Lateral Movement  T1021 Remote Services  requiring authentication or
|     |     | CVEs, per detection  | %   | E   |     |     | user interaction.  |     |
| --- | --- | -------------------- | --- | --- | --- | --- | ------------------ | --- |
D
| Collection  | T1114 Email Collection  | A  CVE-2020-1472  | 58%  |     |                 |     |                                   |     |
| ----------- | ----------------------- | ----------------- | ---- | --- | --------------- | --- | --------------------------------- | --- |
|             |                         |                   |      |     | CVE-2020-0601   |     | An attacker could sign malicious  |     |
C
Command and Control  T1105 Ingress Tool Transfer  B  CVE-2022-22954  17%  (Windows  files with fake certificates.
CryptoAPI Spoofing)
|               |                                               | C  CVE-2021-40444  | 11%  |     |     |     |     |     |
| ------------- | --------------------------------------------- | ------------------ | ---- | --- | --- | --- | --- | --- |
| Exfiltration  | T1048 Exfiltration Over Alternative Protocol  |                    |      |     |     |     |     |     |
|               |                                               | D  CVE-2023-28231  | 9%   |     | A   |     |     |     |
Note: Detection events do not represent confirmed exploitation
| Impact  | T1486 Data Encrypted for Impact  |                   | B   |     |                                                                |     |     |     |
| ------- | -------------------------------- | ----------------- | --- | --- | -------------------------------------------------------------- | --- | --- | --- |
|         |                                  | E  CVE-2020-0601  | 5%  |     | of the vulnerabilities. Additionally, many signals related to  |     |     |     |
exploitation of known vulnerabilities might be captured in
| Reconnaissance  | T1589 Gather Victim Identity Information  |                                        |     |     |                                                                  |     |     |     |
| --------------- | ----------------------------------------- | -------------------------------------- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- |
|                 |                                           | Source: Microsoft Threat Intelligence  |     |     | more general behavioral alerts and are therefore not identified  |     |     |     |
in this analysis.
| Resource Development  | T1586 Compromise Accounts  |     |     |     |     |     |     |     |
| --------------------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
34

35
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
The threat landscape in 2026
Cyberattacks typically hit known hotspots (continued) Length of threat actor activity: Year over year by sector
2025 2026
Dwell time is increasing as organizations
3 years
2 years
struggle to detect intrusions
1 year
6 months
Dwell time is the period between the earliest evidence
3 months
of threat actor activity and its detection, while length of
threat actor activity measures the period between the 1 month
earliest and latest observed activity. Comparing year
over year DART engagement data shows a statistically 1 week
significant increase in dwell time, while the overall
length of threat actor activity remained broadly stable. 1 day
This suggests organizations took longer to identify
malicious activity following compromise, with the
consistency of the increase across multiple sectors < 1 day
indicating a broader operational trend.
Government Industrials and Financial Energy and Telecommunications Automotive, Healthcare Research Retail and Software, Prof and
The most pronounced increase in dwell time was manufacturing services resources and media mobility, and academia consumer data and business
transport goods platforms services
observed in industrials and manufacturing sector, while
telecommunications and media showed the largest
Length of dwell time: Year over year by sector
increase in the duration of threat actor activity. The latter
2025 2026
is consistent with observations that nation-state actors
3 years
seek to establish quiet, persistent access to targets of 2 years
espionage interest. 1 year
6 months
The box plots illustrate both the typical duration and the 3 months
degree of variation within each sector. The central line
1 month
shows the median, while the endpoints of the extending
lines represent the shortest and longest observed
1 week
durations. A tighter spread indicates more consistent
experiences; a wider spread highlights greater variation
between incidents. Comparing the position and spread 1 day
of 2025 and 2026 therefore shows both how typical
durations changed and how consistently those changes
were experienced across incidents. < 1 day
Government Industrials and Financial Energy and Telecommunications Automotive, Healthcare Research Retail and Software, Prof and
manufacturing services resources and media mobility, and academia consumer data and business
transport goods platforms services
2025 reporting period: July 2024–June 2025; 2026 reporting period: July 2025–June 2026. Source: DART

36
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
The threat landscape in 2026
Emerging threats Open-source supply chain compromise Attacks against edge devices
1 2
There continues to be a fundamental shift
by attackers to exploit trusted systems, Open-source ecosystems such as npm and Python Edge devices such as firewalls, virtual private network
operational blind spots, and the scale Package Index (PyPI), and continuous integration and (VPN) gateways, and routers have become a primary
of modern digital ecosystems to gain continuous delivery (CI/CD) have become a critical layer target. Located at the boundary between enterprise
of the modern attack surface. Today, nearly all enterprise networks and the internet, these systems provide
advantage. Looking over the horizon,
software depends on third-party components, high-value access to traffic flows and authentication
Microsoft believes the following emerging often numbering in the hundreds or thousands per material and are often less well monitored or patched
threats will play an increasing role for both application. Each dependency introduces potential than traditional endpoints. Once compromised, edge
risk. Attackers can exploit the inherent trust in official devices can be repurposed into part of the threat actor’s
cybercriminal and nation-state actors in the
channels to infect downstream systems by: operational infrastructure or used to intercept traffic,
next year:
• Using compromised maintainer accounts conduct AiTM attacks, or enable further intrusions
against downstream targets. Attackers may combine
• Creating fake maintainer accounts to host malware
compromised edge devices with resilient infrastructure
• Leveraging repositories to publish malicious updates
such as bulletproof hosting providers to obscure activity,
These packages often execute automatically during host command and control (C2) and extend persistence.
installation or CI/CD workflows. This does not require
Defending this layer is challenging due to visibility and
any user interaction and enables stealthy access to cloud
forensic limitations. Many edge appliances lack endpoint
credentials, tokens, and enterprise systems without
detection capabilities, provide limited or non-persistent
requiring direct exploitation of hardened targets.
logging, or require additional configuration to enable
Defending against supply chain compromise is meaningful telemetry. These constraints create blind
complicated by the scale and complexity of modern spots where malicious activity may go undetected or
dependency trees, which create visibility gaps and leave incomplete forensic artifacts.
signal-to-noise challenges. Malicious packages also
Organizations can reduce this risk by:
often lack known signatures or disclosures, further
• Prioritizing rapid patching of edge devices
limiting detection. While AI-driven analysis can improve
dependency visibility and support automated auditing • Enabling centralized and high-fidelity logging
and remediation, it also introduces some risk, as • Enforcing strong authentication
adversaries begin to manipulate package ecosystems to • Integrating network-level visibility with threat
influence automated selection by coding agents. intelligence to detect and respond to activity occurring
outside traditional endpoint coverage

37
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
The threat landscape in 2026
Emerging threats (continued)
AI as a force multiplier Erosion of trust in the digital
3 4
for malicious activity information environment
AI is rapidly reshaping the threat landscape by lowering Advances in generative AI have already made it
barriers to entry and compressing the economics almost impossible for individuals and organizations
of cyber operations. Tasks that historically required to distinguish between some authentic and synthetic
specialized expertise are increasingly being augmented content. AI-generated text, images, audio, and video can
or automated by AI systems. This shift reduces now closely replicate human communication patterns and
development timelines for both sophisticated actors and identities, significantly reducing traditional cues used to
opportunistic adversaries. Generative AI also enables a assess credibility. This erosion of trust blurs the boundary
high-volume expansion of convincing, personalized social between legitimate and fabricated content.
engineering campaigns in areas that were formerly low-
As AI-generated content becomes ubiquitous, trust in
tech but time-intensive, such as romance scams or spear
digital information is quickly degraded. This creates
phishing. This shift transforms these fraud schemes into
a destabilizing dynamic in which individuals are both
industrialized operations that evade traditional defenses,
more susceptible to manipulation and less confident in
as most security tools lack visibility into deception
legitimate sources. Organizations can mitigate this risk
occurring outside the endpoint.
by adopting layered approaches that combine content
Looking forward, agentic AI will be used to enable provenance and verification mechanisms and AI-assisted
increasingly autonomous malicious cyber operations. detection of synthetic media.
This suggests a near-term future in which AI-driven
At a societal level, mitigating this challenge requires
agents run large portions of attack campaigns
a shift from implicit trust in digital content to explicit
independently from their human operators, further
verification, supported by trusted information sources
amplifying their scale and impact. Organizations can
and emerging approaches to content authenticity.
mitigate these risks by adopting behavior-based
Policymakers should support interoperable standards
detection, strengthening identity and access controls, and
for content provenance and authentication while
implementing robust validation of automated actions.
encouraging platforms to preserve and surface reliable
indicators of origin. Policy frameworks should also
promote transparency, research access, and cross-sector
coordination without treating any single detection tool as
a complete solution.

|     |     |     | Introduction  | AI  | The threat landscape  | Cybercrime  |     | Resilience  | Appendix |
| --- | --- | --- | ------------- | --- | --------------------- | ----------- | --- | ----------- | -------- |
  dna etats-noitaN
Regional sample of activity level observed
 6202 tropeR esnefeD latigiD tfosorciM staerht lacitilopoeg
July 2025 – June 2026
Regional top 10s
Asia & Pacific
| Americas  |     |     |     |     | Europe  |     | Middle East & Africa  |     |     |
| --------- | --- | --- | --- | --- | ------- | --- | --------------------- | --- | --- |
United States  531  Taiwan  193  United Kingdom  76  Israel  210
Brazil  27  Japan  172  Germany  45  United Arab Emirates  50
| Canada     | 26  | India          |     | 58  | Ukraine      | 42  | Egypt         |     | 30  |
| ---------- | --- | -------------- | --- | --- | ------------ | --- | ------------- | --- | --- |
| Chile      | 9   | Australia      |     | 27  | France       | 28  | Saudi Arabia  |     | 24  |
| Colombia   | 9   | Hong Kong SAR  |     | 25  | Italy        | 25  | South Africa  |     | 14  |
| Mexico     | 9   | Vietnam        |     | 18  | Spain        | 25  | Kuwait        |     | 8   |
| Peru       | 7   | Malaysia       |     | 16  | Belgium      | 24  | Qatar         |     | 5   |
| Ecuador    | 5   | Philippines    |     | 14  | Switzerland  | 20  | Jordan        |     | 4   |
| Argentina  | 4   | Thailand       |     | 13  | Greece       | 14  | Ethiopia      |     | 3   |
Singapore
| Dominican Republic  | 3   |     |     | 10  | Poland  | 11  | Iraq  |     | 3   |
| ------------------- | --- | --- | --- | --- | ------- | --- | ----- | --- | --- |
Observed event activity count per country
| 0-49  50-99  | 100-199  | Over 200  |     |     |     |     |     |     |     |
| ------------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
38

|     |     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| --- | --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Nation-state and geopolitical threats
6202 tropeR esnefeD latigiD tfosorciM
| Significant trends in state- | At the same time, these actors diverge in how they  |     |     |                                   |     |     |     |
| ---------------------------- | --------------------------------------------------- | --- | --- | --------------------------------- | --- | --- | --- |
|                              |                                                     |     |     | Nation-state targeting by sector  | %   | “   |     |
balance scale versus precision. For example, China
sponsored threat activity  20%
|     | operates at global scale, prioritizing infrastructure- |     |     | A  IT  |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | ------ | --- | --- | --- |
level access and broad visibility across a wide range of  Across China,
B  Research and academia  20%
sectors. In contrast, Russia often pursues more targeted
| Nation-state cyber activity reflects  |     |     |     |     |     | Iran, North Korea,  |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------------------- | --- |
alignment to support its objectives—particularly in  10%
| consistent objectives with continued  |     |     |     | C  Government  |     |     |     |
| ------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
and Russia, state-
relation to the war in Ukraine. These actors also differ
| tradecraft refinement.  |     |     |     | D  Think tanks/NGOs  | 10%  |     |     |
| ----------------------- | --- | --- | --- | -------------------- | ---- | --- | --- |
in their tolerance for exposure. China’s operations tend  sponsored cyber
to prioritize stealth to enable long-term intelligence  7%
|                                                     |                                                          |     |     | E  Transportation  |     | operations continue  |     |
| --------------------------------------------------- | -------------------------------------------------------- | --- | --- | ------------------ | --- | -------------------- | --- |
| Across China, Iran, North Korea, and Russia, state- | collection. Russia and Iran have demonstrated a greater  |     |     |                    |     |                      |     |
sponsored cyber operations continue to evolve toward  willingness to accept exposure in pursuit of disruptive or  F  Manufacturing  5%
to evolve toward more
more persistent, scalable, and strategically aligned
|     | destructive effects, though these patterns vary across  |     |     | Other  | 28%  |     |     |
| --- | ------------------------------------------------------- | --- | --- | ------ | ---- | --- | --- |
access models, with a shared emphasis on long-term  G  persistent, scalable,
individual actors and sub-clusters.
positioning inside high-value environments. While each
|     |     |     |     | Source: Microsoft Threat Intelligence,  |     | and strategically  |     |
| --- | --- | --- | --- | --------------------------------------- | --- | ------------------ | --- |
Going forward, nation-state cyber activity will likely
nation maintains distinct priorities shaped by its  nation-state notification data
continue evolving to emphasize access that can be  aligned access
geopolitical objectives, collectively, their operations
increasingly share characteristics that complicate  sustained, scaled, and repurposed over time. State- models, with a shared
| detection and response. A consistent trend across all  | sponsored intrusions are likely to prioritize identity  |     |     |     |     |     |     |
| ------------------------------------------------------ | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
four actors is the shift toward maintaining persistent  systems—particularly cloud identity systems—as  emphasis on long-
|     | enterprise environments continue to consolidate access,  |     |     |     | A   |     |     |
| --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
access that can support multiple objectives over time.  term positioning
authentication, and administrative control within cloud-
| China, Iran, and Russia, for example, seek access within  |     |     |     | G   |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
inside high-value
| strategic sectors such as critical infrastructure from  | based and federated platforms. In addition, all four  |     |     |     |     |     |     |
| ------------------------------------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
which they can pivot from espionage to disruptive  nations are likely to continue pursuing supply chain  environments.
| activity. North Korea’s remote IT workers, meanwhile,  | attacks to achieve high-impact, scalable access, and  |     |     |     |     |     |     |
| ------------------------------------------------------ | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
incorporate AI across the intrusion lifecycle, integrating
generate revenue while establishing access that could
more autonomous systems to support elements of
be leveraged for intelligence collection or future
| disruptive activity.  | their operations.  |     |     | F   | B   |     |     |
| --------------------- | ------------------ | --- | --- | --- | --- | --- | --- |
The growing centrality of identity and trusted access
E
pathways is reflected in nation-state activity as well.
| This includes embedding operations within legitimate  |     |     |     | D   | C   |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
authentication flows, using account compromise and
cloud-based collection, and leveraging high-credibility
social engineering. Chinese and Russian actors are
increasingly exploiting identity infrastructure directly,
for example through token replay and service principal
abuse. Meanwhile, North Korean activity more often
relies on high-credibility phishing to obtain valid access.
39

40
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Nation-state and geopolitical threats Top ten targeted countries: China % Top ten targeted sectors: China %
Significant trends in state-sponsored threat activity (continued) A United States 27 A IT 15
B Taiwan 24 B Government 14
China
C Japan 20 C Research and academia 8
D Hong Kong SAR 3 D Think tanks/NGOs 7
Persistence as a foundation The goals of Chinese state actors remain E Philippines 2 E Critical manufacturing 6
largely consistent over time and center on
Chinese state actors have strengthened their F Malaysia 2 F Transportation 4 long-term access to facilitate espionage.
focus on diverse, large-scale information
These actors continue to prioritize collection G Italy 2 G Consumer retail 4
collection through long-lived access to
at IT and government organizations
targets. This supports their government’s H United Kingdom 1 H Finance 3 linked to the United States, Taiwan, and
international objectives and whole-of-
Japan. Using cloud-native persistence I Germany 1 I Defense 3
state intelligence fusion, an approach
and exfiltration through compromised or
that combines political oversight, military actor-created service principals and OAuth J Belgium 1 J Healthcare and public health 2
apparatus, and commercial industries into
applications allows Chinese state actors to
a single party-led apparatus. These actors Source: Microsoft Threat Intelligence, Source: Microsoft Threat Intelligence,
evade detection for longer periods.
have leveraged living-off-the-land (LOTL) nation-state notification data nation-state notification data
techniques, covert networks, and cloud- At the same time, Chinese state actors
native capabilities to minimize footprints continuously search for exploitable
and maximize dwell times. While tactics like vulnerabilities in public-facing applications,
exploiting vulnerabilities in public-facing which can provide initial access and G HI J J
applications, uploading web shells, and sometimes authentication material to F
E
deploying remote access trojans (RATs) facilitate lateral movement within the
D I
remain in many actors’ arsenals, an increasing network or into the cloud. Chinese state H
A
number of actors are shifting to identity- actors experiment with new technologies as
G
based attacks, cloud-native persistence, and they gain adoption, fitting them into existing A
data exfiltration. workflows. Some actors now use AI tools to
F
search for vulnerabilities or tips on exploiting
them. Other actors continue to deploy tried C
and tested attack chains using phishing and E
RATs to compromise a wide set of targets.
B
D
B
C

|     |     | Introduction | AI  | The threat landscape | Cybercrime |     | Resilience | Appendix |
| --- | --- | ------------ | --- | -------------------- | ---------- | --- | ---------- | -------- |
Nation-state and geopolitical threats  Top ten targeted countries: Iran  Top ten targeted sectors: Iran
|     |     |     |     |     | %   |     |     | %   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
6202 tropeR esnefeD latigiD tfosorciM
Significant trends in state-sponsored threat activity (continued)
|     |     |     | A  Israel      |     | 39  | A  Research and academia  |     | 28  |
| --- | --- | --- | -------------- | --- | --- | ------------------------- | --- | --- |
|     |     |     | B              |     | 23  |                           |     | 19  |
|     |     |     | United States  |     |     | B  Other                  |     |     |
Iran
|     |     |     | C  United Arab Emirates  |     | 9   | C IT            |     | 12  |
| --- | --- | --- | ------------------------ | --- | --- | --------------- | --- | --- |
|     |     |     | D                        |     | 6   | D               |     | 11  |
|     |     |     | Egypt                    |     |     | Transportation  |     |     |
Pursuing resilient and opportunistic  Iranian actors continue to target the same   E  India  6  E  Government  8
sectors, with a consistent focus on research
| operations  |     |     | F  United Kingdom  |     | 5   | F  Think tanks/NGOs  |     | 8   |
| ----------- | --- | --- | ------------------ | --- | --- | -------------------- | --- | --- |
and academia, IT/telecommunications,
In a period marked by regional tension
critical infrastructure, government and   G  Brazil  4  G  Communications  4
and episodic kinetic escalation, Iranian
defense supply chains, non-governmental
|                                          |                                            |     | H  Greece   |     | 3   | H  Manufacturing          |     | 4   |
| ---------------------------------------- | ------------------------------------------ | --- | ----------- | --- | --- | ------------------------- | --- | --- |
| state-aligned actors conducted broad,    | organizations (NGO), and dissident         |     |             |     |     |                           |     |     |
| multi-layered campaigns against Israel   | communities. At the same time, Microsoft   |     |             |     |     |                           |     |     |
|                                          |                                            |     | I  Germany  |     | 2   | I  Commercial facilities  |     | 3   |
and longstanding adversaries across the
continues to observe pre-positioning within
Middle East. They also carried out a notable   J  Saudi Arabia  2  J  Finance  2
these environments for long-term espionage
and significant increase in targeting of
and potential disruption. Ongoing regional
|                                                 |                                           |     | Source: Microsoft Threat Intelligence,    |     | Source: Microsoft Threat Intelligence,    |     |     |     |
| ----------------------------------------------- | ----------------------------------------- | --- | ----------------------------------------- | --- | ----------------------------------------- | --- | --- | --- |
| the United States and US interests. As the      | conflict has driven a shift toward more   |     |                                           |     |                                           |     |     |     |
|                                                 |                                           |     | nation-state  notification  data          |     | nation-state  notification  data          |     |     |     |
| conflict evolved, Iranian cyber and influence   | disruptive and destructive approaches,    |     |                                           |     |                                           |     |     |     |
operations expanded their targeting, adapted
including data destruction and operational
disruptive techniques, and increasingly
technology (OT) targeting for retaliation.
integrated cyber, military, and information
|                                                 | As we first noted last year, we continue to   |     |     | I  J |     |     | I  J |     |
| ----------------------------------------------- | --------------------------------------------- | --- | --- | ---- | --- | --- | ---- | --- |
| activities to amplify strategic messaging and   |                                               |     |     | H    |     |     |      |     |
see a convergence in tactics, techniques, and
operational impact.
procedures (TTP) across Iranian threat actors.
| While activity against regional targets   |                                                 |     |     |     |     |     | H   |     |
| ----------------------------------------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                                           | This coordination amplifies the effectiveness   |     |     | G   |     |     |     |     |
| continued at its usual steady pace, the   |                                                 |     |     |     |     | G   |     |     |
|                                           | and scale—and therefore potential impact—       |     |     | F   |     |     |     | A   |
expansion of US-focused operations
|     | of Iranian campaigns. Iranian state-aligned   |     |     |     |     | F   |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
was a largely retaliatory response to the   threat actors continue to rely primarily on   E  A
war, and drew in actors that had not
exploitation of known vulnerabilities, weak
| previously targeted the United States.   |     |     |     | D   |     | E   |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
authentication, and exposed internet-facing
Internet blackouts and infrastructure
systems for initial access, with credential
degradation in Iran this year temporarily
harvesting and phishing as central enablers.
C
constrained some operations and prompted   Their post-compromise goals include lateral   D
B
connectivity adaptations, but overall Iran’s
movement to sustain access and expand
tempo remained high, with pre-positioned
|     | operational reach, with abuse of cloud   |     |     | B   |     |     | C   |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
and opportunistic access enabling
infrastructure, including Microsoft Azure,
sustained activity.
for persistence.
41

|     |     | Introduction | AI  | The threat landscape |     | Cybercrime | Resilience | Appendix |     |
| --- | --- | ------------ | --- | -------------------- | --- | ---------- | ---------- | -------- | --- |
Nation-state and geopolitical threats  Top ten targeted countries: Russia  Top ten targeted sectors: Russia
|     |     |     |     |     |     | %   |     |     | %   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6202 tropeR esnefeD latigiD tfosorciM
Significant trends in state-sponsored threat activity (continued)
|     |     |     | A  United States  |     |     | 21  | A  Government  |     | 25  |
| --- | --- | --- | ----------------- | --- | --- | --- | -------------- | --- | --- |
|     |     |     | B                 |     |     | 14  | B              |     | 13  |
|     |     |     | Ukraine           |     |     |     | Education      |     |     |
Russia
|     |     |     | C  United Kingdom  |     |     | 11  | C  Think tanks/NGOs  |     | 13  |
| --- | --- | --- | ------------------ | --- | --- | --- | -------------------- | --- | --- |
|     |     |     | D                  |     |     | 6   | D                    |     | 10  |
|     |     |     | Belgium            |     |     |     | IT                   |     |     |
More diversity in tradecraft   Instead, they augment traditional intrusion   E  Germany  4  E  Energy  5
chains, allowing operators to maintain access
for stealth and efficiency  F  France  3  F  Defense industry  3
through quieter, identity-centric mechanisms
Russian state actors are becoming more
that blend into the target environment.  G  Spain  3  G  Manufacturing  3
efficient, stealthy, and adaptive, using LOTL
Some Russian actors are also targeting   H  Poland  2  H  Transportation  3
techniques, reduced malware footprint,
internet-facing edge devices to identify
and deeper exploitation of identity and
|                                            |                                             |     | I  Sweden  |     |     | 2   | I  Finance  |     | 2   |
| ------------------------------------------ | ------------------------------------------- | --- | ---------- | --- | --- | --- | ----------- | --- | --- |
| cloud ecosystems. The result is a threat   | vulnerabilities and exploit misconfigured   |     |            |     |     |     |             |     |     |
landscape that is more persistent and harder   devices. In a notable escalation, in December   J  Switzerland  2  J  Inter-governmental organiztion  2
| to detect, but at the same time, predictable.   | 2025 a Russian threat actor used this access   |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
vector when conducting a coordinated   Source: Microsoft Threat Intelligence,    Source: Microsoft Threat Intelligence,
Russian threat actor TTPs have become more
destructive attack on Poland’s energy sector.   nation-state  notification  data  nation-state  notification  data
diversified even as they targeted the same
| sectors as last year: NGOs, government,     | This indicates a new willingness to destroy   |     |     |      |     |     |       |     |     |
| ------------------------------------------- | --------------------------------------------- | --- | --- | ---- | --- | --- | ----- | --- | --- |
| research and academia, and defense.         | critical infrastructure outside of Ukraine    |     |     |      |     |     |       |     |     |
| Geographically, the United States, United   | while possibly also serving as a warning to   |     |     |      |     |     |       |     |     |
|                                             | countries that support Ukraine.               |     |     | J    |     |     | I  J  |     |     |
| Kingdom, and Ukraine remain these actors’   |                                               |     |     | H  I |     |     |       |     |     |
| primary focus, with other NATO members—     | This year, we observed an uptick in cyber     |     |     |      |     |     |       |     |     |
such as  Spain, Germany, and Belgium—taking
activity from non-traditional actors as a   H
secondary precedence.
|     | way to scale operations, reduce attribution   |     |     | G   |     |     | G   |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Russian threat actors are leaning more   risk, and accelerate access. This reinforces   F  F  A
A
the distributed nature of Russia’s hybrid
| heavily into identity-based attacks and   |                                       |     |     |     |     |     | E   |     |     |
| ----------------------------------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                           | ecosystem, which blends traditional   |     |     | E   |     |     |     |     |     |
cloud exploitation to bypass defenses and
| maintain persistence, including abusing   | intelligence units with non-traditional actors   |     |     |     |     |     |     |     |     |
| ----------------------------------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| OAuth applications and conducting token   | including emerging clusters, cybercriminal       |     | D   |     |     |     |     |     |     |
D
| replay. Some actors have leveraged AiTM   | affiliates, and hacktivist groups. We also   |     |     |     |     |     |     |     |     |
| ----------------------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
identified Russian actors using vibe coding
capabilities at the network edge and internet
or AI-generated tooling. For now, however,
service provider (ISP) level, enabling selective
|     |     |     |     | C   | B   |     |     | B   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
traffic interception. These approaches do not   Russian integration of AI across the attack   C
| replace the use of malware.   | lifecycle serves as a force multiplier to   |     |     |     |     |     |     |     |     |
| ----------------------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
improve scale and speed rather than
fundamentally changing attack methods.
42

43
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Nation-state and geopolitical threats Top ten targeted countries: Top ten targeted sectors:
Significant trends in state-sponsored threat activity (continued)
North Korea % North Korea %
A United States 50 A IT 33
North Korea B Italy 13 B Research and academia 15
C Australia 5 C Other 13
D United Kingdom 4 D Think tanks/NGOs 8
Scaling with the help of AI The North Korean remote IT worker scheme
remains a major threat as workers exploit E Switzerland 2 E Consumer retail 7
North Korean state actors have innovated global hiring practices to obtain trusted
their tradecraft, increased their use of AI, and F India 2 F Finance 5
access across industries. The program
scaled infrastructure to accelerate operations
has also leveraged AI across the attack G Germany 2 G Manufacturing 4
and conduct more persistent and adaptive lifecycle to support persona development,
campaigns. While their tradecraft remains social engineering, and sustained access. H United Arab Emirates 2 H Health 4
grounded in social engineering, malware
More broadly, North Korean threat actors
I France 1 I Communications 2
delivery, and abuse of legitimate tools, it has
are integrating AI to improve the speed,
evolved toward access-focused and identity- scale, and resilience of operations including J Republic of Korea 1 J Defense industry 2
driven operations.
malware creation and infrastructure
Source: Microsoft Threat Intelligence, Source: Microsoft Threat Intelligence,
North Korean threat actors continue to management. In some cases, actors have also
nation-state notification data nation-state notification data
prioritize organizations in the United experimented with agentic workflows and
States, United Kingdom, Europe, and East LLM-enabled code generation to accelerate
Asia, focusing on IT, financial services, malware deployment. H I J I J
and blockchain-related organizations to G
North Korean actors are also expanding their F
support revenue generation. At the same tradecraft to support identity-based attacks. E
time, they engaged in sustained targeting H
This includes large-scale OAuth consent
of government, defense-related, and policy G
phishing campaigns while impersonating
D
focused organizations for intelligence F
legitimate SaaS platforms to induce users A
collection. Recently, these actors’ targeting
to grant high-privilege permissions. C
has broadened to reflect a more scale-driven E
These operations continue to emphasize
and opportunistic approach. For example,
rapid infrastructure turnover, including
they have expanded targeting across the
the creation and rotation of domains
cryptocurrency ecosystem to include Bitcoin B D
and supporting infrastructure to sustain A
mining organizations and increased targeting
operations and evade disruption. This allows
of individuals as access vectors. They also
campaigns to persist even as infrastructure is
sought access to software and supply chain C B
identified and removed.
ecosystems. In March 2026, a state-sponsored
group compromised the widely used Axios
npm package in a supply chain attack.

44
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
nredom
woH
nigeb
snoisurtni
The initial access landscape Initial access techniques From valid accounts to enterprise-wide access
% In access based on valid accounts, attackers
Looking at Microsoft Defender
authenticate with legitimate credentials: stolen
A User execution 30
Experts notifications this year reveals passwords, successful password sprays, replayed
an initial access landscape dominated B Valid accounts 20 session tokens, or hijacked accounts.
by human-centric and identity-centric C Malicious copy and paste 13 What makes identity-based access uniquely dangerous is
entry points. what happens next. Over half of these intrusions (52.2%)
D Phishing 11 involved follow-on credential theft—once inside, attackers
immediately harvested more credentials. Another 18.4%
Initial access techniques observed in E Drive-by compromise 6 involved active password spray campaigns. This creates
Microsoft Defender Experts customer
F Exploitation of public-facing application 5 a self-reinforcing cycle: one compromised identity fuels
notifications the compromise of many more. Lateral movement is
G Other 1 also pronounced—adversaries pivot through Server
The initial access landscape is dominated by human-
Message Block (SMB) shares, Windows Management
centric and identity-centric entry attempts and intrusions,
Instrumentation (WMI), and Remote Desktop Protocol
G
according to a review of Microsoft Defender Experts
(RDP). Credential dumping is then used to escalate
notifications this year. Combined, user execution and
access quickly.
valid accounts accounted for over half of all the activity
observed, while phishing and malicious copy and paste F
The rise of malicious copy-and-paste attacks
made up another quarter. This means prevention,
E
detection, and response programs need to be equally Last year, ClickFix-style attacks, which use deceptive
strong across endpoint execution controls, identity A prompts to trick users into copying, pasting, and
protection, phishing resistance, and browser defenses. executing malicious commands, represented 47% of
D
No single control layer is sufficient. observed initial access activity. This year’s data reflects
a more diversified threat landscape, with malicious
Today’s user execution intrusions arrive through
copy-and-paste attacks accounting for only 12.8% of
fake browser updates, AI-generated lures, multi-stage
observed intrusions.
payloads that evade sandboxes, and, increasingly, social
engineering that bypasses traditional file-based thinking C ClickFix attacks waned in late 2025, then rebounded
entirely. Once a user executes, the follow-on is swift, explosively in early 2026, growing roughly 23x
leading to: between December and May. The follow-on is almost
• Malware (in 60.3% of cases) B uniformly malware (96.3%), making this one of the most
• Infostealers (in 12.3% of cases) conversion-efficient initial access techniques observed.
The reusability of the ClickFix access layer means
• Credential theft (in 9.4% of cases)
operators can rotate payloads without altering the
PowerShell and cmd.exe are primary execution vehicles Source: Microsoft Defender Experts social engineering delivery, making it a cross-platform,
in these pathways. behavior-driven initial access technique that routinely
bypasses file- and exploit-based defenses.

|     |     | Introduction | AI  | The threat landscape | Cybercrime | Resilience | Appendix |
| --- | --- | ------------ | --- | -------------------- | ---------- | ---------- | -------- |
How modern intrusions begin
6202 tropeR esnefeD latigiD tfosorciM
|     | Phishing technique    | Phishing has evolved past passwords  |     |     | Volume trajectory  |     |     |
| --- | --------------------- | ------------------------------------ | --- | --- | ------------------ | --- | --- |
ClickFix is evolving
|     | breakdown   |     |     |     | (Microsoft Defender telemetry)  |     |     |
| --- | ----------- | --- | --- | --- | ------------------------------- | --- | --- |
Phishing accounts for 10.9% of intrusion attempts, but
In ClickFix-style attacks, targets are guided   the nature of phishing has fundamentally changed.   Unique devices per week running an attacker-supplied
|     | Key  %  |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
ClickFix command, observed in Microsoft Defender
through fake CAPTCHAs, fabricated error   AiTM phishing now dominates. Here, attackers use a
45
dialogs, or “verify you are human” lures   A  AiTM-URL  reverse proxy to secretly sit between a user and a real   behavioral  telemetry.
sign-in page. It captures usernames, passwords, and
to paste an attacker-supplied command   B  Standard URL  34  350
MFA codes in real time, allowing the attacker to steal the
into Windows Run, Windows Terminal, or   C  13  active session cookie and circumvent MFA. AiTM now
|     | Attachment  |     |     |     | 300  |     | H   |
| --- | ----------- | --- | --- | --- | ---- | --- | --- |
PowerShell.   accounts for 44.6% of all identified phishing techniques,
|     | D  AiTM-attachment  7  |                                                        |     |     |      |     |     |
| --- | ---------------------- | ------------------------------------------------------ | --- | --- | ---- | --- | --- |
|     |                        | compared to 33.6% for standard URL phishing and just   |     |     | 250  |     |     |
The result is a low-friction, high-yield foothold that scales   E  2  12.9% for traditional attachments. The downstream   G
QR code (incl. AiTM-QR)
to hundreds of thousands of devices. Between February   impact of AiTM phishing is significant—87.7% of
200
phishing intrusions involved credential or session
| and early May 2026, Microsoft Defender observed   |     |     |     |     |     | F   |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ClickFix-style user-pasted command execution on   E  harvesting, while 6.3% were business contact   150
| more than 1.1 million unique devices, an ~8x increase.   |     | impersonation  (BCI).   |     |     |     |     |     |
| -------------------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |
E
This was likely driven by a proliferation of kits-for-hire.
|     | D   | Public-facing exploitation: Low volume,    |     |     | 100  |     |     |
| --- | --- | ------------------------------------------ | --- | --- | ---- | --- | --- |
ClickFix builders are sold as malware-as-a-service (MaaS),
|                                                 |     | high impact                                        |     |     |     | D   |     |
| ----------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| lowering the technical bar for new operators.   | C   |                                                    |     |     | 50  | C   |     |
|                                                 |     | While exploitation of public-facing applications   |     |     | B   |     |     |
We also saw a “FileFix” variant gaining traction. In FileFix,   represents just 4.8% of observed intrusions, this   A
users are guided to paste the malicious command into   A  initial access vector carries disproportionate impact.   0
the Windows File Explorer address bar instead of Run or
|     |     | Microsoft SharePoint Server is the most frequently   |     |     | Key  |     | 000’s  |
| --- | --- | ---------------------------------------------------- | --- | --- | ---- | --- | ------ |
Terminal. This broadens the target pool by accessing less   exploited product, followed by Internet Information
|     |     |     |     |     | A  Feb W1  |     | 38,000  |
| --- | --- | --- | --- | --- | ---------- | --- | ------- |
technically cautious targets and bypasses controls that   Services (IIS), HTTP File Server (HFS), React-based
focus solely on PowerShell/Run telemetry.  B  applications, and Exchange Server. Compromising an
|     |     |     |     |     | B  Feb W2  |     | 52,000  |
| --- | --- | --- | --- | --- | ---------- | --- | ------- |
internet-facing server often serves as an entry point into
|     |     |     |     |     | C  March W1  |     | 71,000  |
| --- | --- | --- | --- | --- | ------------ | --- | ------- |
an organization, allowing attackers to rapidly broaden
their access and target high-value systems and data.
|     |                    |                                                         |     |     | D  March W2  |     | 95,000  |
| --- | ------------------ | ------------------------------------------------------- | --- | --- | ------------ | --- | ------- |
|     | Source: Microsoft  | Notably, exploitation volume declined sharply from mid- |     |     |              |     |         |
Threat Intelligence  2025 onward, suggesting a mix of successful patching   E  April W1  130,000
and attacker pivot to identity-based methods.
|     |     |     |     |     | F  April W2  |     | 188,000  |
| --- | --- | --- | --- | --- | ------------ | --- | -------- |
|     |     |     |     |     | G  April W5  |     | 240,000  |
|     |     |     |     |     | H  May W1    |     | 310,000  |
Source: Microsoft Threat Intelligence
45

46
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How modern intrusions begin
ClickFix is evolving (continued) Voice phishing attacks go Per-attempt engagement:
Vishing vs. email phishing
What this means for defenders mainstream in chat applications
60
These trends reinforce that no single control layer is
Threat actors targeting employees through
sufficient. Defenders should combine phishing-resistant
identity controls, endpoint and browser protections, collaboration platforms are increasingly 50
behavior-based detection, and rapid containment using voice phishing (vishing) for higher- A C
playbooks to stop an initial compromise from becoming
confidence, multi-step social engineering.
an enterprise-wide incident.
Vishing over cross-tenant calls (calls
• Strengthen the human layer. Use role-based training
that prepares users to recognize phishing, ClickFix- that cross the boundaries of at least two B
style prompts, and unusual requests to run commands organizational environments) in Microsoft
or share credentials.
Teams in particular has become a more
• Move beyond traditional MFA. Prioritize phishing-
prominent access vector. resistant authentication and monitor for session-token D
theft, anomalous sign-ins, and unfamiliar devices.
The weekly confirmed malicious volume has risen 502%
• Protect identities after initial access. from this time last year. Over 90% of attackers that use
Detect credential harvesting, privilege escalation, Teams have incorporated voice calling into some of
suspicious OAuth activity, and lateral movement their attacks. Despite red flags such as Teams’ “External”
before one compromised account leads to banners and call warnings, skilled attackers successfully
broader access. persuade victims to comply, usually on workdays during
• Use layered controls. Combine identity protection, business hours.
endpoint and browser defenses, application controls,
Across the attacks we studied, 93% of attackers
rapid patching, and centralized telemetry so attackers
succeeded at least once in keeping a target on the
cannot bypass the environment through a single
line for 20 seconds or longer—the point at which an
weak point.
attacker has captured attention and can begin a social
• Prepare for the common post-compromise
engineering script. Nearly half of all calls (48%) lasted
playbook. Establish response procedures to revoke
longer than 20 seconds, and 30% lasted beyond one
sessions, isolate devices, reset credentials, and
minute, during which time targets are likely actively
investigate related accounts and systems quickly.
talking with attackers and either following instructions or
leaking privileged information. While Safe Links evaluates
URLs shared during these calls at time of click, blocking
credential harvesting pages even mid-conversation, the
voice channel itself carries no link to intercept.
)%(
etar
tpmetta-reP
40
30
20
10
0
Key %
A Vishing victim engaged 48
over 20 seconds
B Vishing victim engaged 30
over 1 minute
C Targeted email victim engaged/ 30-40
clicked links
D Bulk email victim engaged/ 1-5
clicked links
Vishing: Microsoft telemetry |
Email: Microsoft and academic telemetry
Source: Microsoft Threat Intelligence

47
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How modern intrusions begin
Voice phishing attacks go mainstream in chat Organizations should use a layered approach to reduce The cost of delayed patching
the risk of vishing attacks in collaboration platforms.
applications (continued)
• Teams federation. Ensure external-user warnings are In an age of AI-powered vulnerability
Attackers are diversifying their vishing
enabled so users see clear “External” indicator.
scanning, exploitation of unpatched
impersonation techniques
• Safe Links. Enable time-of-click URL evaluation
vulnerabilities is a concerning initial
without an end-user click-through override to prevent
While “Help Desk” and “IT Support” variants used to
credential harvesting through links shared during calls. access path.
account for most malicious display names, a majority
now use personal-looking usernames that either • RMM tools. Limit remote assistance tools to IT-
Nation-state and ransomware actors keep weaponizing
match or appear to match legitimate employee naming only groups through endpoint management policy,
disclosed flaws, especially internet-facing infrastructure,
conventions. Unicode evasion has also matured: removing a primary foothold mechanism.
identity and management appliances, developer tooling,
invisible characters, emojis, and deliberate misspellings • Attack surface reduction. Enable attack surface
and third-party software.
allow attackers to bypass exact-match filters while reduction rules in block mode for script and
keeping display names visually similar to legitimate Office macro execution to disrupt staging and The disclosure-to-exploitation window has shrunk to
support contacts. payload delivery. single-digit days, if not exploited as a zero-day before
• Endpoint detection. Deploy endpoint detection and
any advisory is issued. Microsoft has observed the
When a vishing call succeeds, what follows is rapid and
following trends:
response (EDR) capabilities with behavioral blocking
rehearsed. The attacker convinces the victim to grant
or logging to connect the social engineering event to • More, faster weaponization. The Cybersecurity and
access through a remote monitoring and management
endpoint compromise in a single timeline. Infrastructure Security Agency (CISA) added over 110
(RMM) tool, achieving interactive control of the endpoint.
Attackers complete reconnaissance in two minutes or less • Threat hunting. Hunt for Teams call events followed CVEs to the Known Exploited Vulnerabilities (KEV)
and then download malicious payloads. by remote management process launches within a catalog from November 2025 to May 2026, most
30-minute window to identify the transition from within a week of disclosure. Attackers are using CVEs
vishing to compromise. with lightning speed. For example, cybercriminal
Storm-1175 moved from web-facing exploitation to
deploying Medusa ransomware in as little as 24 hours.
Since 2023, this ransomware group has weaponized
at least 16 CVEs, including SAP NetWeaver, a day
after disclosure.
• Concentration on edge, identity, and management
infrastructure. Ransomware is continuing to find fast
lanes through:
1. RMM platforms, for example SimpleHelp,
ScreenConnect, and BeyondTrust
2. Identity file transfer products, for example Oracle
Identity Manager, SmarterMail, GoAnywhere MFT,
and SolarWinds Web Help Desk

48
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How modern intrusions begin
The cost of delayed patching (continued) The exploitation gap is narrowing at a time when “ Recommendations
patch coverage is lagging. Research published in 2025
In September 2025, Microsoft tracked a four-week reports a median time-to-exploit of about five days.
surge in Akira ransomware across 50+ organizations— For internet-exposed services, mass scanning often starts In an age of Treat newly exploited vulnerabilities as urgent.
mostly small and medium-sized businesses—tied to within hours, and pre-disclosure windows of 30 days or AI-powered Fix newly identified vulnerabilities that affect an internet-
CVE-2024-40766 (SonicWall SSL VPN exploitation). more are now routine. The gap between government facing or identity system within 72 hours.
• Pre-disclosure (zero-day) exploitation. Significant risk and enterprise remediation times is stark. While KEV vulnerability
exists that threat actors will find vulnerabilities before remediation timelines require federal action within 7–14
scanning,
blue teams and researchers. Cisco Secure FMC’s days, median enterprise remediation for critical external Know what needs to be patched.
critical remote code execution flaw (CVE-2026-20131) CVEs can take 30–60 days. exploitation Maintain a complete, current inventory of third -party
was given the maximum score of 10.0 for severity of unpatched systems, remote management tools, and older devices so
Shadow IT and end-of-life (EoL) devices widen it further.
under the Common Vulnerability Scoring System exposed assets are not overlooked.
This mismatch means attackers often have weeks to vulnerabilities
(CVSS). The Interlock ransomware group was able to
exploit known vulnerabilities after fixes are available.
exploit this vulnerability for approximately 30 days is a concerning
before disclosure. The issue is no longer simply whether a patch exists, Monitor critical access systems.
but whether organizations can identify exposed assets, initial access path.
• Multi-actor use of CVEs. As actors seek means of entry, Extend security monitoring to firewalls, VPNs, identity
prioritize the highest-risk flaws, and remediate them
they occasionally leverage the same vulnerabilities. systems, RMM tools, email gateways, and file -
before attackers operationalize them. For internet-facing,
For example, Microsoft saw coordinated exploitation transfer services.
identity, and management systems, traditional monthly
of CVE-2025-49704 and CVE-2025-49706 against
patch cycles may no longer be fast enough.
on-premises SharePoint in July 2025. Two Chinese
Add safeguards when systems cannot be
state actors used the ToolPane chain for access, while
patched.
Storm-2603 deployed Warlock ransomware via web
shell and MachineKey theft. This means that the same Isolate outdated systems from the wider network, restrict
n-day window was used for both espionage and unnecessary connections, and use protective controls to
ransomware within days. block suspicious traffic.
Look for signs of past exploitation.
Review the previous 90 days of activity for evidence that
newly disclosed or previously unknown vulnerabilities
were used before fixes were applied.

49
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How modern intrusions begin
Impersonation is becoming “ The larger shift is from brand mimicry to At the same time, delivery is diversifying: while
context mimicry attachments remain common (30%), QR codes now
more sophisticated appear in 13% of cases, and HTML-based payloads in
Around 25% of Attackers are impersonating relationships, departments, 5%. One in four impersonation emails pushes the victim
Impersonation remains one of the most attacks mimic workflows, vendors, and organizational routines. to a phone call, moving the attack outside normal
Automated notifications appear in 80% of impersonation URL and attachment inspection and into a live social
effective phishing techniques because it
an organization’s attacks, followed by financial fraud themes (61%). engineering channel.
makes malicious messages feel legitimate Around 25% of attacks mimic an organization’s trusted
trusted operating Organizations can reduce impersonation risk by
by borrowing the identities, workflows, and operating environment or someone inside it, with
environment or HR, payroll, and benefits scams driving 77% of those combining technical controls with verification practices.
visual cues people already trust. Microsoft Train employees to scrutinize unexpected requests
someone inside it, organizational cases.
analysis found that nearly 85% of reported that appear to match familiar workflows, and require
phishing emails between April and June with HR, payroll, The effectiveness of these campaigns comes not only independent confirmation for payment, payroll,
from who the sender appears to be, but from how credential, and sensitive data requests. Extend detection
2026 carried an impersonation signal. and benefits scams
naturally the request fits into the recipient’s workday. beyond prominent brands to local vendors, partners,
driving 77% of those departments, and organizational naming patterns.
For years, impersonation defenses focused on That same familiarity abuse extends beyond the
Inspect QR codes, HTML attachments, and callback
recognizable signals: lookalike domains, spoofed display organizational cases. organization itself. Attackers also pose as trusted
requests that move interactions outside traditional email
names, authentication failures, well-known brand collaborators, suppliers, or business partners, exploiting
defenses, and make it easy for employees to report
names such as Microsoft, Google, DocuSign, PayPal, the fact that large, global organizations interact with a
suspicious messages before acting.
and Adobe, and fuzzy matches against curated entities. wide ecosystem of vendors that may not appear among
32% of attacks use images or logos to mimic a brand. their most visible or frequently contacted collaborators.
Those signals still matter, but attackers are adapting. Although these cases represent only about 3% of spear-
More than a third of attacks use template-based lures phishing activity, they are challenging to detect because
that mimic familiar brand communications, frequently the credibility comes from a plausible relationship rather
without explicitly naming any brand to avoid detection, than from a known top vendor or explicit brand signal.
while 44% of targeted brands are lesser-known or
Once attackers establish that familiar context, the next
location-specific brands that fall outside globally
step is to convert trust into action. The lure may point to
optimized detection models.
a credential harvesting sign-in page, deliver a malicious
attachment, ask the recipient to reply with sensitive
information, or apply pressure through callback scams
and gift card requests.
These tactics can lead to account compromise, financial
loss, and broader organizational breach. Even nation-
state actors have adopted impersonation as an initial
engagement tactic, using persistent contact with targets
to enable later-stage intrusions.

50
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How modern intrusions begin
Business contact impersonation: Over the past 12 months, Microsoft detected more than Emerging threat of network
46 million BCI attacks. Monthly volumes were relatively
The new “BEC” stable through most of the period before spiking in edge infrastructure
April 2026, when volume surged 121%—more than
The term business email compromise double any previous month observed in the past year. Network edge infrastructure—such as
The most consistent finding across the period is how
(BEC) has long suffered from definitional firewalls, VPNs, and gateways—was used
rarely the initial BCI email actually asked for anything.
confusion. To some, it refers to text-based as an initial access vector before attackers
The vast majority of first-contact BCI messages contain
social engineering when an attacker only generic outreach, such as “Are you at your desk?” pivoted to endpoints or identity systems.
impersonates a CEO and asks for a or “Do you have a moment?” with no mention of money, Now attackers have pivoted back. Modern
invoices, or documents.
wire transfer. edge devices enforce authentication,
Only a small percentage of initial BCI messages contained
manage sessions, inspect traffic, and
To others, it encompasses the actual compromise an explicit financial or document request, and that share
integrate with cloud identity platforms,
of a business email account through credential has been shrinking: from 17% in October 2025 to just
phishing or session hijacking. These are fundamentally 3% by June 2026. BCI is, overwhelmingly, a conversation making them control points. Compromise
different threats with different attack chains, defenses, starter. The fraud comes later, in follow-up messages, enables direct control over identity, trust,
and indicators. Conflating them under one label once the attacker has established rapport and confirmed
and policy enforcement across
obscures both. the target is engaged. This multi-stage structure means
the enterprise.
the initial email is deliberately bland, designed to avoid
Moving forward, we are introducing the term business
triggering content-based detection rules precisely
contact impersonation (BCI) to describe social
because it contains nothing overtly malicious to detect.
engineering attacks that initiate a conversation with Attackers are targeting access before
enterprise users while impersonating a trusted business One interesting trend within the BCI landscape worth identity verification
contact, such as an executive, employee, vendor, supplier, highlighting is payroll diversion, when actors attempt
or partner, to persuade the recipient to take an action to redirect an employee’s direct deposit to an attacker- Sophisticated attackers are increasingly prioritizing
under false pretenses, such as initiating a fraudulent controlled account. These attacks follow a striking weekly pre-authentication vulnerabilities that allow access
financial transaction or sending sensitive information or cadence: volume peaks sharply on Monday, then declines before identity verification. Authentication bypass and
documents to the attacker. This definition deliberately steadily each day through Friday before going nearly RCE provide immediate entry into systems that enforce
excludes credential phishing and account takeover (ATO), silent on weekends. Over half of all payroll diversion trust. These flaws are rapidly weaponized and exploited
which are distinctly different threats that warrant their attacks (51%) land on a Monday or Tuesday. This suggests at scale, often within hours or days of disclosure, with
own terminology and their own defensive strategies. attackers are deliberately timing their outreach to campaigns targeting exposed VPN infrastructure and
extending into identity abuse.
coincide with the start of the business week, when payroll
and HR staff are processing requests from the prior
week and recipients are most likely to action a quick ask
without much scrutiny.

|     |     |     | Introduction  | AI  | The threat landscape  |     | Cybercrime  | Resilience  | Appendix  |
| --- | --- | --- | ------------- | --- | --------------------- | --- | ----------- | ----------- | --------- |
How modern intrusions begin
 6202 tropeR esnefeD latigiD tfosorciM
|                                                |     | “   | Compromised edge infrastructure functions  |     |     |   Recommendations  |     |     |     |
| ---------------------------------------------- | --- | --- | ------------------------------------------ | --- | --- | ------------------ | --- | --- | --- |
| Emerging threat of network edge infrastructure |     |     |                                            |     |     |                    |     |     |     |
(continued)  as an operational platform
To confront this threat, defenders must extend detection
|     |     |     |     |     |     | into the network control plane. Effective coverage  |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
Once access is established, adversaries persist directly    Strategic actors    Since these systems sit at the convergence of
|     |     |     |     |     |     | includes monitoring for large-scale exploitation  |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
within network devices rather than passing through them.                  authentication, session activity, and data flows, after
|     |     | increasingly    |     |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Techniques include configuration changes, unauthorized            achieving access, attackers can monitor authentication    attempts against edge services:
| accounts, credential insertion, and manipulation  |     | maintain long-term  |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
interactions, identify high-value accounts, capture
| of authentication components. More advanced  |     |                     |                                                         |     |     |                            |     |     |     |
| -------------------------------------------- | --- | ------------------- | ------------------------------------------------------- | --- | --- | -------------------------- | --- | --- | --- |
|                                              |     | access at the edge  |   credentials and session tokens, and hijack or replay  |     |     |   Configuration tampering  |     |     |     |
activity includes firmware-level or in-memory    sessions to bypass authentication.
| implants that evade forensic detection and survive  |     | using low-noise  |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Attackers are shifting from exploiting individual
| standard remediation.                                    |     |                      |                                                            |     |     | Unauthorized account creation  |     |     |     |
| -------------------------------------------------------- | --- | -------------------- | ---------------------------------------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
|                                                          |     | methods designed     |    vulnerabilities to targeting entire classes of network  |     |     |                                |     |     |     |
| Strategic actors increasingly maintain long-term access  |     |                      |                                                            |     |     |                                |     |     |     |
|                                                          |     | to avoid detection.  | technologies. Campaigns span multiple vendors,             |     |     |                                |     |     |     |
Credential and secret extraction
at the edge using low-noise methods designed to    including Fortinet, Cisco, Ivanti, Citrix, Palo Alto
avoid detection. Control of routing and segmentation    Networks, and Juniper, leveraging shared architectural
further enables lateral movement that blends with    patterns, such as exposed management interfaces
Session hijacking
legitimate activity. Because actions originate from trusted    and similar authentication workflows. Once identified,
| infrastructure, detection is reduced while attackers gain  |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
these weaknesses are rapidly operationalized across the
access to segmented or otherwise restricted resources.  ecosystem, generating coordinated exploitation waves    Lateral movement initiated by network devices
rather than isolated incidents.
|     |     |     | This activity is reinforced by a persistent defensive  |     |     |   Defenders also need to focus on identity integration  |     |     |     |
| --- | --- | --- | ------------------------------------------------------ | --- | --- | ------------------------------------------------------- | --- | --- | --- |
|     |     |     |                                                        |     |     | abuse, such as unexpected Security Assertion Markup     |     |     |     |
visibility gap. Network infrastructure is under-
|     |     |     | instrumented. Patching is often delayed, and standard      |     |     |   Language (SAML) or identity provider changes, and     |     |     |     |
| --- | --- | --- | ---------------------------------------------------------- | --- | --- | ------------------------------------------------------- | --- | --- | --- |
|     |     |     | remediation actions frequently fail to remove persistence  |     |     |   pre-breach exposure risks such as unpatched systems   | -   |     |     |
|     |     |     | embedded in configurations or system components.           |     |     |   and exposed management interfaces. A defining signal  |     |     |     |
|     |     |     |                                                            |     |     | of this threat is a network device behaving like an     |     |     |     |
|     |     |     |                                                            |     |     | endpoint by initiating scanning, credential access, or  |     |     |     |
|     |     |     |                                                            |     |     | lateral movement.                                       |     |     |     |
51

|     |     |     | Introduction  | AI  | The threat landscape  |     | Cybercrime  | Resilience  | Appendix  |
| --- | --- | --- | ------------- | --- | --------------------- | --- | ----------- | ----------- | --------- |
How modern intrusions begin
 6202 tropeR esnefeD latigiD tfosorciM
Information stealers:     Infostealer activity is becoming more    Top five stealer families observed in
|     | advanced  |     |     | infostealer activity among Microsoft  |     |     |     |     |     |
| --- | --------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
A continued threat
Defender Experts customers
|                                             | Since late 2025, Microsoft Defender Experts has       |     |     |      |                          |     |     |     |     |
| ------------------------------------------- | ----------------------------------------------------- | --- | --- | ---- | ------------------------ | --- | --- | --- | --- |
|                                             |                                                       |     |     | Key  |                          |     | %   |     |     |
|                                             | observed an increase in macOS-targeted infostealer    |     |     |      |                          |     |     |     |     |
| Information stealers are a type of malware  |                                                       |     |     |      |                          |     |     |     |     |
|                                             | activity, driven largely by social engineering-based  |     |     |      | A  Atomic macOS Stealer  |     | 50  |     |     |
| designed to secretly gather sensitive data  |                                                       |     |     |      |                          |     |     |     |     |
|                                             | delivery. Campaigns associated with malware families  |     |     |      |                          |     |     |     |     |
from a device. Over the past year, they have    B  OtterCookie  19
|     | such as Atomic macOS Stealer (AMOS), MacSync Stealer,  |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
evolved from opportunistic credential    and DigitStealer rely on user-initiated actions, often    C  PS1Bot  14
|                                                           | disguised as legitimate workflows. These operations are      |     |     |     |                     |     |     |     |     |
| --------------------------------------------------------- | ------------------------------------------------------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- |
| grabbers into a broader, more adaptive                    |                                                              |     |     |     |                     |     |     |     |     |
|                                                           | designed to enable ATO, financial fraud, and downstream      |     |     |     | D  Lumma Stealer    |     | 10  |     |     |
| access-and-monetization layer that often                  |                                                              |     |     |     |                     |     |     |     |     |
|                                                           | compromise of cloud and developer environments.              |     |     |     | E  MacSync Stealer  |     | 7   |     |     |
| sits at the front of larger intrusion chains.             |                                                              |     |     |     |                     |     |     |     |     |
|                                                           | A defining characteristic of these macOS campaigns is        |     |     |     |                     |     |     |     |     |
|                                                           | their use of native system tooling and fileless execution    |     |     |     |                     |     |     |     |     |
| These campaigns increasingly target credentials, session  |   techniques. This allows attackers to blend into expected   |     |     |     |                     |     |     |     |     |
| tokens, and other high-value artifacts that enable        |   platform behavior and reduce visibility compared to        |     |     |     |                     |     |     |     |     |
| ATO and follow-on compromise across endpoints,            |                                                              |     |     |     |                     |     |     |     |     |
|                                                           | conventional malware deployments. Overall, this trend        |     |     |     |                     | E   |     |     |     |
| browsers, and cloud-connected services. There is also     |                                                              |     |     |     |                     |     |     |     |     |
|                                                           | highlights a strategic move by threat actors to align their  |     |     |     |                     |     |     |     |     |
D
| a growing emphasis on fast-turn monetization through     |   tradecraft more closely with platform norms, signaling  |     |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| cryptocurrency wallet and session theft. Many attempted  |   increased maturity and investment in macOS-specific     |     |     |     |     |     |     |     |     |
| ransomware attacks are disrupted during the infostealer  |   intrusion paths.                                        |     |     |     |     |     |     |     |     |
| stage, underscoring the value of early detection         |                                                           |     |     |     |     |     |     |     |     |
| and intervention.                                        | Microsoft Defender Experts also continue to observe       |     |     |     |     |     |     |     |     |
C
a broader shift toward cross-functional information-
In parallel, Microsoft Defender Experts has seen increased    stealing operations, where the initial stealer stage is also    A
| use of cross-platform payloads, modular scripts, and       |   used to validate access, profile the target environment,  |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| delivery lures that abuse trusted platforms and common     |   and enable follow-on payload delivery. This model         |     |     |     |     |     |     |     |     |
| utilities to blend into typical user workflows. Together,  |                                                             |     |     |     |     |     |     |     |     |
|                                                            | increasingly aligns with nation-state tradecraft, where     |     |     |     |     |     |     |     |     |
these shifts signal a move beyond traditional Windows- information theft is tightly coupled with long-term access    B
| focused campaigns toward scalable operations that also  |   objectives. In such campaigns, infostealers function as an  |     |     |                                     |     |     |     |     |     |
| ------------------------------------------------------- | ------------------------------------------------------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
| target macOS and developer environments with low-       | entry and validation layer within larger intrusion chains,    |     |     |                                     |     |     |     |     |     |
| friction, stealthy collection at scale.                 | leveraging cross-platform scripts, modular tooling, and       |     |     |                                     |     |     |     |     |     |
|                                                         | developer-focused lures to reach high-value identities        |     |     |                                     |     |     |     |     |     |
|                                                         | and sensitive assets.                                         |     |     | Source: Microsoft Defender Experts  |     |     |     |     |     |
52

| Introduction  | AI  | The threat landscape  |     | Cybercrime  | Resilience  | Appendix  |
| ------------- | --- | --------------------- | --- | ----------- | ----------- | --------- |
How modern intrusions begin
 6202 tropeR esnefeD latigiD tfosorciM
Recommendations
Information stealers: A continued threat (continued)
Trusted platforms and common utilities     Prioritize controls that reduce initial execution success, limit credential/token exposure, and shorten
time-to-detection for wallet and developer-secret theft. - -
are abused for stealthy delivery
Microsoft Defender Experts have observed threat
|     | Harden initial access paths.  |     |     | Reduce crypto wallet exposure.  |     |     |
| --- | ----------------------------- | --- | --- | ------------------------------- | --- | --- |
actors increasingly using trusted platforms and familiar
consumer utilities as delivery cover, blending theft    Restrict script abuse (PowerShell/JavaScript),    Prefer hardware wallets where possible,
|     | block common LOLBins where feasible,  |     |     | control/monitor wallet extensions, and alert  |     |     |
| --- | ------------------------------------- | --- | --- | --------------------------------------------- | --- | --- |
activity into routine workflows and delaying suspicion.
In the CrystalPDF campaign, for example, attackers    and enforce application control for user- - on wallet-related file/extension access from  -
promoted a fake PDF converter via malvertising    writable locations.   unusual processes.
and search engine optimization (SEO) poisoning.
It established persistence, targeted browser credential
|     | Strengthen identity.  |     |     | Detect and contain early.  |     |     |
| --- | --------------------- | --- | --- | -------------------------- | --- | --- |
stores, and initiated C2 traffic. Similar abuse of messaging
platforms and everyday tools shows how common install- Employ phishing-resistant MFA, conditional          Watch for infostealer tradecraft (credential
and-use behavior is being repurposed to reach financial    access, and rapid invalidation/rotation for tokens    store access, archive/exfil patterns, Telegram/
and cryptocurrency accounts.  and session credentials.  C2 beacons), and isolate hosts quickly to prevent
follow-on payloads. -
These intrusions often start with low-signal artifacts
that resemble nuisance software or ordinary installation    Protect developer environments.
noise (for example, simple file creation alerts), buying    Be ready to recover.
|     | Move secrets to managed vaults, scan repos and  |     |     |     |     |     |
| --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
time for attackers to progress into persistence, credential
|     | endpoints for secrets, and enforce short-lived  |     | -   | Maintain playbooks for token/key compromise  |     |     |
| --- | ----------------------------------------------- | --- | --- | -------------------------------------------- | --- | --- |
and wallet theft, and C2. Delivery and early-stage
|     | credentials for CI/CD and cloud CLIs. |     |     | (rotate SSH/API/cloud keys, invalidate sessions,  |     |     |
| --- | ------------------------------------- | --- | --- | ------------------------------------------------- | --- | --- |
behavior are intentionally designed to look routine,
|     |     |     |     | rebuild development endpoints), and validate  |     |     |
| --- | --- | --- | --- | --------------------------------------------- | --- | --- |
making “annoying vs. malicious” distinctions less reliable
downstream access after any infostealer event.
for defenders.
53

|     |     |     | Introduction  |     | AI  | The threat landscape  |     | Cybercrime  |     | Resilience  |     | Appendix  |
| --- | --- | --- | ------------- | --- | --- | --------------------- | --- | ----------- | --- | ----------- | --- | --------- |
    ,ecnegilletni ,noitceteD
 noitpursid dna Operationalizing detection     To support this transition, scalable detection architectures    AI is reshaping day-to-day SOC operations
 6202 tropeR esnefeD latigiD tfosorciM
|     |     | must improve signal quality through suppression,  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
beyond detection and disruption
at scale
|     |     | enrichment, and prioritization.                     |     |     |     |     |                                                       |     |     |     |     |     |
| --- | --- | --------------------------------------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |                                                     |     |     |     |     | LLMs and specialized agents can summarize incidents,  |     |     |     |     |     |
|     |     | One of the most important and often underdeveloped  |     |     |     |     |                                                       |     |     |     |     |     |
A growing challenge for enterprise security    generate investigative narratives, write log hunting
|                                               |     | capabilities is internal infrastructure profiling.     |     |     |     |     |                                                         |     |     |     |     |     |
| --------------------------------------------- | --- | ------------------------------------------------------ | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                               |     |                                                        |     |     |     |     | queries, and automate executive reporting. AI-assisted  |     |     |     |     |     |
| operations centers (SOCs) is the operational  |     |   Detection systems that lack contextual awareness of  |     |     |     |     |                                                         |     |     |     |     |     |
|                                               |     |                                                        |     |     |     |     | triage can classify incidents, recommend investigative  |     |     |     |     |     |
burden created by high volumes of low- the environments they protect struggle to distinguish    steps, and surface relevant evidence across multiple data
|     |     | malicious behavior from legitimate operational activity.  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
context alerts. Many incidents are built    sources without requiring analysts to manually pivot
|                                         |     | Effective profiling establishes authoritative baselines for:  |     |     |     |     | between tools.  |     |     |     |     |     |
| --------------------------------------- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
| from isolated detections rather than    |     |                                                               |     |     |     |     |                 |     |     |     |     |     |
coherent attack narratives, forcing analysts    • Corporate VPN ranges    For detection engineering teams, AI accelerates the
|                                           |     | • Cloud workloads     |     |     |     |     | development, testing, and validation of analytics,    |     |     |     |     |     |
| ----------------------------------------- | --- | --------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
| to manually enrich and correlate data to  |     |                       |     |     |     |     |                                                       |     |     |     |     |     |
|                                           |     | • Service accounts    |     |     |     |     | reducing the time required to deploy new detections.  |     |     |     |     |     |
determine intent and impact.
|     |     |     |     |     |     |     | Operational leaders can use AI-driven reporting and  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
• Administrative jobs
|                                                          |     |                                    |     |     |     |     | queue analysis to reduce administrative overhead and       |     |     |     |     |     |
| -------------------------------------------------------- | --- | ---------------------------------- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
| This workflow reduces efficiency and increases the risk  |     | • Geographic workforce patterns    |     |     |     |     |                                                            |     |     |     |     |     |
|                                                          |     |                                    |     |     |     |     | improve visibility into response performance. This allows  |     |     |     |     |     |
that coordinated intrusions remain hidden within benign    • Routine authentication flows        skilled defenders to focus on higher-value activities
| noise or repetitive false positives. As a result, experienced  |     |                                                          |     |     |     |     |                                                  |     |     |     |     |     |
| -------------------------------------------------------------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|                                                                |     | With this context, detection engines can suppress        |     |     |     |     | such as threat hunting, hypothesis development,  |     |     |     |     |     |
| analysts could be spending more time reconstructing            |     |                                                          |     |     |     |     |                                                  |     |     |     |     |     |
|                                                                |     |                                                          |     |     |     |     | and adversary disruption rather than repetitive  |     |     |     |     |     |
| context than disrupting adversary activity.                    |     | predictable operational noise while elevating behaviors  |     |     |     |     |                                                  |     |     |     |     |     |
|                                                                |     |                                                          |     |     |     |     | operational tasks.                               |     |     |     |     |     |
|                                                                |     | that meaningfully diverge from established norms.        |     |     |     |     |                                                  |     |     |     |     |     |
In response, modern SOCs are shifting from reactive    Ultimately, operationalizing detection at scale requires a
|                                                           |     | Threat intelligence integration further strengthens    |     |     |     |     |                                                                   |     |     |     |     |     |
| --------------------------------------------------------- | --- | ------------------------------------------------------ | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
| investigation toward proactive disruption. Rather than    |     |                                                        |     |     |     |     |                                                                   |     |     |     |     |     |
|                                                           |     | detection quality by transforming isolated indicators  |     |     |     |     |   shift toward quality-centric security architectures where       |     |     |     |     |     |
| treating alerts as independent events, advanced           |     |                                                        |     |     |     |     |                                                                   |     |     |     |     |     |
|                                                           |     | into actionable context. An outbound connection gains  |     |     |     |     |   fidelity, context, and correlation are prioritized alongside    |     |     |     |     |     |
| detection systems focus on identifying correlated         |     |                                                        |     |     |     |     |                                                                   |     |     |     |     |     |
|                                                           |     |                                                        |     |     |     |     | coverage. The number of rules deployed or alerts                  |     |     |     |     |     |
| behaviors across hybrid attack chains. Correlation-first  |     | significance when tied to known C2 infrastructure.     |     |     |     |     |                                                                   |     |     |     |     |     |
|                                                           |     |                                                        |     |     |     |     | generated is no longer a meaningful measure of SOC                |     |     |     |     |     |
|                                                           |     | A PowerShell execution becomes more urgent when        |     |     |     |     |                                                                   |     |     |     |     |     |
detection models prioritize building high-confidence            maturity. What matters is the percentage of incidents
|                                                             |     | associated with documented adversary tradecraft.         |     |     |     |     |                                                          |     |     |     |     |     |
| ----------------------------------------------------------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
| incidents that reflect attacker intent and the full attack  |     |                                                          |     |     |     |     |                                                          |     |     |     |     |     |
|                                                             |     | A suspicious sign-in warrants escalation when linked to  |     |     |     |     |   that reflect genuine adversary activity, the speed of  |     |     |     |     |     |
scope instead of surfacing disconnected signals.
|     |     | credential harvesting campaigns.  |     |     |     |     | correlation and containment, and the ability to suppress  |     |     |     |     |     |
| --- | --- | --------------------------------- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
Automated disruption is a critical component of this    low-value signals before they reach analysts.
| model. Once a correlated incident reaches a defined       |     | To deliver value, threat intelligence must operate as a        |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                           |     | continuous input throughout the detection lifecycle            |     |     |     |     |     |     |     |     |     |     |
| confidence threshold, systems can automatically isolate   |     |                                                                |     |     |     |     |     |     |     |     |     |     |
|                                                           |     | rather than as a post-incident reference source.               |     |     |     |     |     |     |     |     |     |     |
| devices, disable compromised accounts, revoke sessions,   |     |                                                                |     |     |     |     |     |     |     |     |     |     |
|                                                           |     | Strategic use of threat intelligence should guide              |     |     |     |     |     |     |     |     |     |     |
| or quarantine cloud resources without waiting for manual  |     |                                                                |     |     |     |     |     |     |     |     |     |     |
| approval. AI and machine learning enable these decisions  |     |   detection engineering priorities, while tactical indicators  |     |     |     |     |     |     |     |     |     |     |
| by evaluating cross-domain telemetry, identifying likely  |     |   should inform alert generation, enrichment, scoring, and     |     |     |     |     |     |     |     |     |     |     |
|                                                           |     | suppression decisions in real time. Organizations that         |     |     |     |     |     |     |     |     |     |     |
| intrusion patterns, and weighing the operational impact   |     |                                                                |     |     |     |     |     |     |     |     |     |     |
|                                                           |     | deeply integrate intelligence into detection pipelines         |     |     |     |     |     |     |     |     |     |     |
of rapid containment. By compressing detection-to-
|                                                            |     | can significantly improve analyst efficiency because       |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| response timelines from hours to minutes, automated        |     |                                                            |     |     |     |     |     |     |     |     |     |     |
| disruption significantly reduces adversary dwell time and  |     |   surfaced incidents already contain the context required  |     |     |     |     |     |     |     |     |     |     |
| limits attack progression.                                 |     | for rapid action.                                          |     |     |     |     |     |     |     |     |     |     |
54

|     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |     |
| --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- | --- |
Detection, intelligence, and disruption
 6202 tropeR esnefeD latigiD tfosorciM
|     |     | How shared threat intelligence  |     |     |   “ |     |     |
| --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
Operationalizing detection at scale (continued)
Recommendations  Integrate threat intelligence throughout the   is reshaping the fight against
| detection lifecycle.   |     |     |     |     | No single  |     |     |
| ---------------------- | --- | --- | --- | --- | ---------- | --- | --- |
Organizations should modernize SOC operations by   fraud
integrating infrastructure context, threat intelligence,   Use intelligence to guide detection priorities and enrich,   organization has
AI-driven correlation, and automated disruption into a   score, and suppress signals in real time.
|     |     |                                      |     |     | sufficient visibility  |     |     |
| --- | --- | ------------------------------------ | --- | --- | ---------------------- | --- | --- |
|     |     | Cyber-enabled fraud operates across  |     |     |                        |     |     |
unified detection strategy.
|     |     | a fragmented ecosystem of platforms,  |     |     |   to fully understand  |     |     |
| --- | --- | ------------------------------------- | --- | --- | ---------------------- | --- | --- |
Use AI to accelerate investigations.
|     |     | services, and infrastructure providers. As a  |     |     |   or disrupt fraudulent  |     |     |
| --- | --- | --------------------------------------------- | --- | --- | ------------------------ | --- | --- |
Build authoritative infrastructure context.
Apply AI-assisted triage, incident summarization,
|     |     | result, no single organization has sufficient  |     |     |     |     |     |
| --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
Maintain current baselines for identities, devices, cloud   hunting-query generation, and detection engineering so  activity on its own.
| analysts can focus on higher-value work. |     | visibility to fully understand or disrupt  |     |     |     |     |     |
| ---------------------------------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
workloads, network ranges, administrative activity, and
normal  authentication  patterns.  fraudulent activity on its own.
Automate high-confidence containment.
|     |     | For example, individual platform providers may observe  |     |     |     |     |     |
| --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
Prioritize correlation and signal quality.
| Where appropriate, enable rapid actions such as isolating   |     | isolated indicators of compromise (IOC), but they often   |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
| devices, disabling compromised accounts, revoking           |     | lack visibility into the full scope of harm, which makes  |     |     |     |     |     |
Measure success by the proportion of incidents that
reflect genuine adversary activity, not by the number of   sessions, and quarantining affected resources.  coordinated data sharing essential and underscores the
rules or alerts generated.  need for public and private partners to act together to
|     |     | disrupt fraud. Without this collective view, enforcement  |     |     |     |     |     |
| --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
Track operational outcomes.
actions risk being delayed, incomplete, or misaligned.
Evaluate SOC effectiveness by detection fidelity, time to
|     |     | At Microsoft, the Digital Crimes Unit (DCU) plays a  |     |     |     |     |     |
| --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
correlation and containment, and the ability to disrupt
|     |     | central role in advancing data sharing as a core pillar  |     |     |     |     |     |
| --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
malicious activity before it progresses.
|     |     | of its strategy to combat cyber-enabled fraud. At its        |     |     |     |     |     |
| --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
|     |     | foundation, the DCU leverages threat intelligence to         |     |     |     |     |     |
|     |     | identify criminal networks and disrupt their infrastructure  |     |     |     |     |     |
|     |     | through affirmative litigation, criminal enforcement, and    |     |     |     |     |     |
|     |     | global coordination. A critical component of this model is   |     |     |     |     |     |
|     |     | the systematic collection, enrichment, and dissemination     |     |     |     |     |     |
of fraud-related data and indicators.
|     |     | Fragmented visibility across the fraud attack chain  |     |     |     |     |     |
| --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
reinforces the need to share data
|     |     | Threat activity is increasingly distributed, with actors  |     |     |     |     |     |
| --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | leveraging multiple services such as hosting providers,   |     |     |     |     |     |
|     |     | communication platforms, payment channels, and            |     |     |     |     |     |
|     |     | advertising networks to run campaigns at scale and        |     |     |     |     |     |
|     |     | evade detection.                                          |     |     |     |     |     |
55

|     |     |     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| --- | --- | --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Detection, intelligence, and disruption
 6202 tropeR esnefeD latigiD tfosorciM
|     | Each intel-sharing type contributes a distinct layer of  |     |     |     |     | Recommendations  |     |     |
| --- | -------------------------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
How shared threat intelligence is reshaping the
| fight against fraud (continued)  | insight. Together, they enable defenders to move from  |     |     |     |     |                                              |     |     |
| -------------------------------- | ------------------------------------------------------ | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
|                                  |                                                        |     |     |     |     | As fraud actors become more coordinated and  |     |     |
fragmented observations to a cohesive understanding of
|     |     |     |     |     |     | adaptive, defenders must match that coordination with  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
As a result, threat hunters across the cybersecurity   the threat landscape.
|     |     |     |     |     |     | equally integrated approaches relying on a two-sided  |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
ecosystem generally detect only distinct elements of
a campaign across the attack chain, such as suspicious   commitment: organizations must both share high- -
Coordinated enforcement supports
account activity or transaction anomalies. In isolation,   quality, actionable intelligence and operationalize
these signals can appear inconclusive or low-priority.   detection and prevention  incoming signals, integrating them into their own
detection and enforcement workflows.
| However, when combined and analyzed in context,    | A defining feature of the DCU’s approach is its proactive   |     |     |     |     |     |     |     |
| -------------------------------------------------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| they can reveal coordinated activity or repeated   | sharing of threat intelligence derived from investigations  |     |     |     |     |     |     |     |
Expanding participation in responsible cross-
targeting patterns.
and disruption operations. The unit gathers insights into    sector data sharing is critical to achieving this goal.
Data sharing is essential to overcoming this blind spot,    malicious infrastructure, fraud patterns, and threat actor    This includes:
behavior. Internally, these insights strengthen Microsoft’s
| but not all data is equally actionable. Shared data  |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
detection and prevention capabilities by feeding into
| must be vetted, contextualized, and responsibly     |                                                           |     |     |     |     |                                                  |     |     |
| --------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- |
|                                                     | security systems and product defenses. Externally, the    |     |     |     |     | Strengthening industry-to-industry collaboration | - - |     |
| handled. Effective data-sharing programs require    |                                                           |     |     |     |     |                                                  |     |     |
| sustained investment in analysis, enrichment, and   |   DCU provides actionable intelligence to global law      |     |     |     |     |                                                  |     |     |
| governance. The ability to transform raw data into  |   enforcement and key partners to support investigations  |     |     |     |     |                                                  |     |     |
Expanding partnerships with law enforcement and
and prevent the reuse of criminal infrastructure. In FY26,
actionable intelligence is what ultimately enables    international bodies
Microsoft worked with 16 partners to curate fraud data to
coordinated disruption.
|     | support investigation, detection, and prevention efforts,    |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Microsoft is increasingly investing in mechanisms to
including sharing victim reports, threat actor email    Investing in systems that improve data quality,
share data and intelligence across sectors, ranging from
addresses, and fraud infrastructure.  validation, and context
exchanges during active investigations to programs
designed for continuous threat intelligence sharing
How the DCU is combatting tech support   Ensuring responsible governance to protect sensitive
and collaboration. Platforms such as the Global Signal
scams through data sharing
Exchange (GSE) can facilitate the sharing of fraud and   information while enabling action
scam signals across organizations such as members of
One way the DCU shares data with partners is through
| the Global Anti-Scam Alliance (GASA). Examples include   | the Cyber Threat Intelligence Program (CTIP). Recently, it  |     |     |     |     |     |     |     |
| -------------------------------------------------------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| private-to-private collaboration, private-to-public      | introduced a new feed, the Tech Scam Feed (CTIP-TSF),       |     |     |     |     |     |     |     |
partnerships—particularly where law enforcement is
which incorporates victim reports gathered from our
involved—and consumer reporting, where data from
tech support scam reporting tool. This adds to existing
sources such as the Better Business Bureau (BBB) or
feeds that focus on C2 and infected-device feeds,
| the American Association of Retired Persons (AARP)         | which are drawn from the DCU’s civil disruption actions.  |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| provides critical visibility into victim experiences and   | The DCU shares information with CTIP subscribers to       |     |     |     |     |     |     |     |
emerging trends.
facilitate proactive fraud detection and inform disruption,
|     | mitigation, and enforcement strategies.  |     |     |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
56

|     |     |     |     |     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| --- | --- | --- | --- | --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Detection, intelligence, and disruption
 6202 tropeR esnefeD latigiD tfosorciM
Targeting fraud’s backbone:    Disrupting fraud: How coordinated action    How Microsoft dismantled the threat  “
brought down RedVDS
Scaling disruption through    The DCU filed a civil action in the United States and
|     |     |     |     |     |     | seized the key domains on which RedVDS relied.  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
RedVDS was a global cybercrime subscription service    When civil action
| law, technology, and global  |     |     |     |                                                            |     |                                                            |     |     |                |     |
| ---------------------------- | --- | --- | --- | ---------------------------------------------------------- | --- | ---------------------------------------------------------- | --- | --- | -------------- | --- |
|                              |     |     |     | that rented out cheap, disposable virtual dedicated        |     |   Simultaneously, the DCU leveraged intellectual property  |     |     |                |     |
|                              |     |     |     |                                                            |     |                                                            |     |     | is structured  |     |
|                              |     |     |     | servers (VDS). In 2026, Microsoft took it offline as part  |     |   rights laws in the United Kingdom in a novel and         |     |     |                |     |
partnerships
|     |     |     |     |                                                       |     | scalable way. This was designed to disrupt operational   |     |     |   strategically, it  |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | -------------------------------------------------------- | --- | --- | -------------------- | --- |
|     |     |     |     | of coordinated action across civil and criminal law,  |     |                                                          |     |     |                      |     |
|     |     |     |     |                                                       |     | infrastructure and compel the disclosure of information  |     |     |                      |     |
automation, and partner ecosystems. This shows how    can do more than
|                                          |     |     |     |                                                      |     | about the service’s operators and the broader criminal  |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | ---------------------------------------------------- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
| The cyber-enabled fraud landscape is an  |     |     |     | joint action can produce more durable outcomes than  |     |                                                         |     |     |     |     |
remove assets—it can
adaptive industry shaped and accelerated    any single lever alone.    ecosystem. This approach shows that existing legal
|     |     |     |     |     |     | frameworks can be adapted creatively to generate  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- |
by specialization, service models, and the    RedVDS exemplified the modern enabler model: it    expose operational
|     |     |     |     |     |     | intelligence, impose accountability, and complement  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
commoditization of cyber capabilities.    operated as a cheap, subscription-based virtual desktop    criminal investigations. When civil action is structured    dependencies, create
|                                                         |     |     |     | hosting service. Thousands of cybercriminal customers  |     |   strategically, it can do more than remove assets—it can  |     |     |                       |     |
| ------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------ | --- | ---------------------------------------------------------- | --- | --- | --------------------- | --- |
|                                                         |     |     |     |                                                        |     |                                                            |     |     | pressure points, and  |     |
| The various stages of an attack, from phishing to ATO,  |     |     |     | used it worldwide to launch fraud campaigns at scale,  |     |                                                            |     |     |                       |     |
|                                                         |     |     |     |                                                        |     | expose operational dependencies, create pressure points,   |     |     |                       |     |
including phishing, ATO, and payment diversion such    enable a broader
have converged into a fraud supply chain. Threat actors    and enable a broader understanding of how an enabler
|     |     |     |     | as BCI. By providing anonymous, disposable virtual  |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
can now manage and market access to malicious    sustains itself and how its customers exploit the service.    understanding of how
| products that use infrastructure and tools that are  |     |     |     | machines (VM) optimized for abuse, RedVDS functioned  |     |                                                            |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | ----------------------------------------------------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
|                                                      |     |     |     |                                                       |     | At the same time, legal action alone is rarely sufficient  |     |     |     |     |
bundled into cohesive service offerings.    as shared criminal infrastructure that powered hundreds    an enabler sustains
|     |     |     |     |                                                    |     | against modern fraud infrastructure because enablers  |     |     |                     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | ----------------------------------------------------- | --- | --- | ------------------- | --- |
|     |     |     |     | of cyber-enabled fraud operations simultaneously.  |     |                                                       |     |     |                     |     |
|     |     |     |     |                                                    |     |                                                       |     |     | itself and how its  |     |
Responses that focus only on serial incident response—  can migrate, rebrand, or spin up replacement capacity
|     |     |     |     | Between 2023 and 2026, RedVDS provided over 10,000  |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
or on the takedown of a single scam operation—can    quickly. That’s why the RedVDS action was paired with    customers exploit
struggle to create lasting impact because the fraud    users access to up to 8,000 virtual desktops a month.  technology-enabled disruption, including the use of the
the service.
ecosystem is resilient and can reconstitute itself.    These users were particularly heavily concentrated in    DCU’s Statutory Automated Disruption (SAD) program.
A hyperscale, cyber-enabled fraud leverages a shared    Africa and the United States.    Through SAD, Microsoft systematically identified and
services model that combines hosting, elastic compute,    disabled previously created malicious VMs associated
anonymized network layers, phishing-as-a-service    with RedVDS to prevent reconstitution at scale.
| (PhaaS), bot networks, and credential underground           |     |     |     |     |     |                                                         |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
|                                                             |     |     |     |     |     | This reduced the operational resilience of downstream   |     |     |     |     |
| markets. These fraud enablers function as the backbone      |     |     |     |     |     |                                                         |     |     |     |     |
|                                                             |     |     |     |     |     | fraud campaigns that depended on this infrastructure.   |     |     |     |     |
| of the ecosystem. So long as those services remain intact,  |     |     |     |     |     |                                                         |     |     |     |     |
|                                                             |     |     |     |     |     | The combination of legal authority and automated        |     |     |     |     |
| downstream fraud actors can cycle quickly through new       |     |     |     |     |     |                                                         |     |     |     |     |
|                                                             |     |     |     |     |     | technical enforcement helped translate disruption from  |     |     |     |     |
| accounts, domains, infrastructure, and ultimately new       |     |     |     |     |     |                                                         |     |     |     |     |
|                                                             |     |     |     |     |     | a one-time event into sustained pressure, limiting the  |     |     |     |     |
| tactics. On the other hand, when enablers and cybercrime    |     |     |     |     |     |                                                         |     |     |     |     |
ability of the ecosystem to rebound quickly.
| services are degraded, many seemingly unrelated fraud         |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| operations can falter simultaneously as costs rise, efficacy  |     |     |     |     |     |     |     |     |     |     |
| decreases, and operational friction increases.                |     |     |     |     |     |     |     |     |     |     |
57

|     |     |     |     | Introduction  | AI  | The threat landscape  |     | Cybercrime  | Resilience  |     | Appendix  |
| --- | --- | --- | --- | ------------- | --- | --------------------- | --- | ----------- | ----------- | --- | --------- |
Detection, intelligence, and disruption
 6202 tropeR esnefeD latigiD tfosorciM
|     |     |     |     | RedVDS malicious VMs decline after takedown action  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Targeting fraud’s backbone: Scaling disruption
through law, technology, and global partnerships
5k
| (continued)  |     |     |     |     |     |     |     |     |     | Hosting Provider (ASN)  |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- |
A
| Partnerships are central to making  |     |     |     |     |     |     |     |     |     | ASN 16276 |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
B
 devresbo sMV SDVdeR 4k
| disruption durable  |     |     |     |     |     |     |     |     |     | B  ASN 19318 |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
C
C  ASN 199654
| Microsoft’s actions were closely coordinated with law  |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3k
enforcement partners to ensure that civil, technical,    D  ASN 399486
| and criminal authorities reinforced one another.    |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Coordination supports deconfliction and sequencing  |     |     |     |     |     |     |     |     |     |     |     |
2k
| so that civil action and technical disruption do not       |       |     |     |                 |         |         |         |                         |         |         |         |
| ---------------------------------------------------------- | ----- | --- | --- | --------------- | ------- | ------- | ------- | ----------------------- | ------- | ------- | ------- |
| unintentionally undermine active criminal investigations.  |       |     |     |                 |         |         |         |                         |         |         |         |
| It also enables complementary outcomes:                    |       |     |     | 1k  A           |         |         |         |                         |         |         |         |
| • Civil processes can drive immediate disruption and       |       |     |     | D               |         |         |         |                         |         |         |         |
| produce information that supports accountability.          |       |     |     |                 |         |         |         |                         |         |         |         |
| • Law enforcement can pursue criminal investigations,      |       |     |     | 0               |         |         |         |                         |         |         |         |
|                                                            |       |     |     | 20 Jan  21 Jan  | 22 Jan  | 23 Jan  | 24 Jan  | 25 Jan  26 Jan  27 Jan  | 28 Jan  | 29 Jan  | 30 Jan  |
seizures, and deterrence.
Date (2026)
| In a cross-border environment where infrastructure,      |     |     |     |                                                                                                                                 |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| operators, victims, and financial flows frequently span  |     |     |     |                                                                                                                                 |     |     |     |     |     |     |     |
|                                                          |     |     |     | Beginning in late January 2026, Microsoft sent notifications to hosting providers demanding they take down VMs associated with  |     |     |     |     |     |     |     |
| multiple jurisdictions, aligned public-private action    |     |     |     |                                                                                                                                 |     |     |     |     |     |     |     |
|                                                          |     |     |     | RedVDS. Most hosting providers, identified by Autonomous System Numbers (ASN) in the chart, began complying with the notices,   |     |     |     |     |     |     |     |
| can reduce the safe havens on which enablers rely and    |     |     |     |                                                                                                                                 |     |     |     |     |     |     |     |
resulting in a dramatic decrease in available malicious VMs.
| increase the probability that disruption translates into  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lasting consequences.      Private sector collaboration plays an equally    In practice, this means building repeatable operational
|     |     |     |     | important role                                            |     |     |     | mechanisms for identifying abuse, validating signals,  |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
|     |     |     |     |                                                           |     |     |     | coordinating timing, and taking action in ways that    |     |     |     |
|     |     |     |     | The fraud ecosystem depends on a wide range of            |     |     |     | reduce collateral impact while maximizing disruption   |     |     |     |
|     |     |     |     | commercial services and platforms. Hosting providers,     |     |     |     | to criminal operations. When partnership models        |     |     |     |
|     |     |     |     | registrars, security vendors, communications platforms,   |     |     |     | mature, they also generate compounding benefits:       |     |     |     |
identity providers, and payment ecosystems all intersect
|     |     |     |     |     |     |     |     | each disruption yields insight into attacker tradecraft,  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
with the infrastructure that fraud actors use. In the
|     |     |     |     |                                                              |     |     |     | reconstitution patterns, and infrastructure dependencies,    |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- |
|     |     |     |     | RedVDS operation, the DCU shared RedVDS-related              |     |     |     | which can be fed back into prevention, detection, and the    |     |     |     |
|     |     |     |     | IOCs with the National Cyber-Forensics and Training          |     |     |     | next cycle of enforcement. Over time, this turns individual  |     |     |     |
|     |     |     |     | Alliance (NCFTA). This helped other providers identify and   |     |     |     | interventions into a durable system of collective            |     |     |     |
disrupt infrastructure associated with RedVDS and limit
|     |     |     |     |     |     |     |     | defense—one that raises the cost of abuse, limits  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
opportunities  for  rapid  reconstitution.
|     |     |     |     |     |     |     |     | criminals’ ability to rebuild, and strengthens resilience  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- |
across the broader digital ecosystem.
58

6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
eht
gniruceS
snoitadnuof The race to retire NTLM Authentication advances are supporting The cloud threat landscape
organizations to make a shift
NT LAN Manager (NTLM) has been part The cloud threat landscape is becoming
Organizations continue to use NTLM because they
of Windows authentication for more than faster, broader, and harder to contain. Over
are unaware of the risk it poses, are not clear about
three decades. This legacy authentication where it remains in use, and/or still depend on it for the past year, attackers increasingly used
protocol uses challenge-response compatibility and operational continuity. Advances in the trusted software supply chains to reach
Windows authentication platform are helping to reduce
verification for access to network resources. many organizations at once, exploited
these dependencies, making the transition to modern
However, as security threats have evolved, authentication more practical. As organizations make this exposed cloud systems within hours, and
so have our standards to meet modern shift, they can reduce opportunities for identity-based benefited from faster discovery of serious
attacks and strengthen resilience against the evolving
security expectations. Microsoft is phasing Linux vulnerabilities.
threat landscape. Moving away from NTLM represents a
out NTLM in favor of stronger, Kerberos-
major evolution in Windows authentication, and a critical
Major supply chain attacks are growing
based alternatives, creating a more secure step toward a passwordless, phishing-resistant future.
authentication model. Open-source supply chain attacks are becoming more
frequent and more damaging. Within the past year,
Despite years of investment in modern authentication, major developer ecosystems saw attacks roughly every
NTLM remains a persistent identity risk in enterprise ten days, with a clear acceleration through Q2 2026.
environments. Attackers abuse NTLM to gain footholds Affected ecosystems include npm, one of the world’s
in enterprise networks, steal credentials, move largest online libraries of reusable software components,
laterally between systems, and escalate privileges. the Python Package Index (PyPI), Crates.io, and
Microsoft security data shows nearly a sixfold increase GitHub Actions.
in NTLM-related security cases over the past decade.
Open-source supply chain compromises are also cloud
In the first six months of 2026 alone, reported cases
security incidents because their primary targets, blast
exceeded the total number observed during 2025.
radius, and impacts extend into cloud environments.
Publicly disclosed vulnerabilities and attack techniques
The largest incidents show how quickly one compromise
continue to emerge, underscoring the ongoing security
can spread:
risks posed by NTLM.
• Shai-Hulud 2.0 affected 25,000 repositories.
• Megalodon backdoored 5,561 GitHub repositories in
under six hours.
• Axios reached more than 100 million weekly downloads
while under attacker control.
59

6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Securing the foundations
The cloud threat landscape (continued) Time-to-exploit is narrowing Generative AI services are becoming cloud
attack surfaces
A container packages an application with everything
Month Incidents Largest wave Dominant vector it needs to run, making containerized applications
In Microsoft data, nearly all attacked AI subscriptions
lightweight, portable, and ideal for modern development. in 2026 involved generative AI services: OpenAI and
Nov 2025 1 25,000 npm worm Technologies like microservices, DevOps, and Kubernetes
Azure OpenAI, custom AI agents and applications, other
have made containers central to building and operating
generative services, and AI Foundry. Non-generative
Mar 2026 5 5 GitHub Actions cloud-native applications. However, containerizing an
cognitive services, including Speech, Vision, Document
application also introduces new risks.
Intelligence, Translator, and AI Search, accounted for less
Apr 2026 6 8 API hijack Exposed container workloads are being found and than 2% combined.
attacked quickly. The median time from container start to
May 2026 7 5,661 npm account hijack
first exploit attempt is just 5.3 hours, and more than half
Attacked customer subscriptions,
of compromised containers are exploited within 24 hours
by AI surface
Attacks are following three new trends of starting. Defenders need to respond in hours, not
days. Default credentials, exposed APIs, and unpatched
1. Attackers are moving upstream into the systems images drive most of the successful compromises. AI surface Share
organizations use to build and release software.
A single stolen credential or compromised workflow
Linux kernel exploitation is increasing
can give attackers a path to many downstream OpenAI / Azure OpenAI 39%
organizations at once. Incidents affecting developer Linux kernel exploitation is also accelerating.
platforms, build services, and widely used open-source Attackers can use programming flaws in an operating
projects show how compromises that start inside system’s core component to gain root access, bypass Custom AI — agents, copilots, LLM apps 31%
development environments can quickly become a security controls, or take full control of the machine.
broader ecosystem risk. Because the kernel manages hardware, memory,
Other generative 20%
2. Attackers are manipulating trust signals. In some and system processes with the highest privilege,
incidents, malicious software appeared legitimate compromising it gives an attacker total dominion over
because verification records were stolen, misused, or the system. AI Foundry 8%
faked. These cases show that while verification is still
In a two-week period between April 29 and May 13,
important, it cannot be treated as a complete integrity
2026, three publicly disclosed flaws gave local users a
guarantee on its own. Non-generative (combined) < 2%
path to root access across major Linux distributions.
3. Developers’ everyday tools are becoming new entry Each was published with working proof-of-concept code
points. Code editors and AI coding assistants now sit and no embargo, leaving defenders very little time to
close to source code, credentials, and build workflows. assess exposure and patch. Attackers found the Copy Fail
Recent cases involving malicious extensions and vulnerability with help from AI, and the other two fit the
poisoned AI-assistant configurations show that the same broader pattern, suggesting that AI will increase the
developer workstation is becoming part of the supply pace at which serious vulnerability classes are discovered.
chain attack surface.
60

61
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Securing the foundations
Rethinking defense models to false positives before security teams could respond. Recommendations
This allowed malicious activity to continue without
tackle intrusions in hybrid cloud triggering investigative action.
Cyber risk is increasingly concentrated in identity
environments From its cloud foothold, Storm-2885 leveraged and cloud governance, not just networks or malware.
device and identity trust relationships to expand its This type of intrusion creates material risk even in
reach. It used Microsoft Intune device management well-defended environments. Sensitive information
Modern threat actors no longer need to
functionality to deploy scripts and tools across managed can be accessed quietly, response timelines can be
break security controls if they can leverage systems, establishing secure tunnels that connected extended, and data exposure can occur without
trust and governance instead. threat actor-controlled infrastructure with on-premises visible operational disruption. Governance and
environments. These tunnels enabled quiet, resilient response models need to be designed for this kind
By operating inside legitimate identity and management access paths that bypassed traditional perimeter defenses of threat, to make sure that security investment is not
frameworks, threat actors can turn defensive systems into and reduced reliance on exposed network services. neutralized by identity compromise.
enablers, extending dwell time and reducing operational
risk. This model of intrusion challenges longstanding Intrusions that work within expected cloud
For CISOs, the takeaway is that identity governance,
assumptions about where detection and prevention
behavior are hard to detect alert handling, and administrative workflows must be
should be concentrated and highlights why identity
treated with the same prioritization as Tier 0 controls.
governance, alert integrity, and hybrid visibility are now Storm-2885 leveraged Microsoft Graph API access
Endpoint detection, threat intelligence, and response
central to enterprise security resilience. Defenders need through a legitimate Microsoft Entra ID application to
tooling are only effective if threat actors are stopped
to be prepared for these intrusions. conduct large-scale data access and reconnaissance.
from operating inside trusted identity boundaries.
Hundreds of thousands of emails were accessed across
Uncovering Storm-2885’s hybrid intrusion hundreds of mailboxes, alongside targeted searches
for credentials, infrastructure documentation, and
In February 2026, DART uncovered how the threat actor operational details. This activity blended into expected
Storm-2885 conducted a prolonged and highly effective cloud application behavior, making it difficult to
hybrid intrusion. The threat actor abused cloud identity distinguish from legitimate administrative or business use
and management systems as the primary control plane without careful correlation.
for operations. From there, they operated almost entirely
through legitimate Microsoft services, using them to Within the on-premises environment, Storm-2885
establish persistence, evade detection, and pivot from used standard administrative techniques. It used SQL
cloud environments into on-premises infrastructure. Server, Server remote execution, RDP, and SSH-based
tunneling to move laterally, deploy additional access
Storm-2885 compromised a highly privileged cloud methods, and maintain redundancy. Multiple persistence
identity, then used that foothold to repeatedly mechanisms were established across Windows and Linux
authenticate, reset credentials, and register additional systems, including scheduled tasks, services, and cron
authentication methods, ensuring long-term access. jobs (automated tasks and scripts). This meant access
The same privileged access also enabled the threat continued even if individual artifacts were discovered
actor to interact with security tooling—closing alerts, and removed.
downgrading incidents, and resolving detections as

| Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| ------------- | --- | --------------------- | ----------- | ----------- | --------- |
 6202 tropeR esnefeD latigiD tfosorciM
3  Cybercrime  Identity is at the center of modern cyber risk  63
|     |     | Defending against identity compromise             |     |     | 63  |
| --- | --- | ------------------------------------------------- | --- | --- | --- |
|     |     | Passkeys are the safer replacement for passwords  |     |     | 64  |
|     |     | Phishing landscape                                |     |     | 65  |
|     |     | How attackers gain access                         |     |     | 66  |
|     |     | QR code phishing                                  |     |     | 66  |
|     |     | CAPTCHA phishing                                  |     |     | 66  |
|     |     | Disrupting phishing: Lessons learned              |     |     | 67  |
from the Tycoon2FA disruption
“
|     |     | Legitimate access becomes the threat     |     |     | 69  |
| --- | --- | ---------------------------------------- | --- | --- | --- |
|     |     | RMM tools as a post-compromise standard  |     |     | 69  |
Disrupting cybercrime requires more
|     |     | The hidden operational risk  |     |     | 69  |
| --- | --- | ---------------------------- | --- | --- | --- |
than understanding the threat, it requires
|     |     | Hybrid attack — Identity and cloud compromise  |     |     | 71  |
| --- | --- | ---------------------------------------------- | --- | --- | --- |
action. Joint efforts between Europol
and Microsoft have shown how law  Cloud identity abuse increases  73
enforcement and industry can work  Ransomware: From access to impact  75
together to target the infrastructure, tools,
|     |     | Ransomware landscape  |     |     | 75  |
| --- | --- | --------------------- | --- | --- | --- |
and services that enable cybercriminal
|     |     | Cybercrime disruption and collective defense  |     |     | 78  |
| --- | --- | --------------------------------------------- | --- | --- | --- |
activity. Recent actions against prolific
|     |     | Information sharing for the modern age  |     |     | 78  |
| --- | --- | --------------------------------------- | --- | --- | --- |
facilitators such as Tycoon2FA and the
|     |     | Policy, partnerships, and enforcement  |     |     | 78  |
| --- | --- | -------------------------------------- | --- | --- | --- |
malware ecosystem through Operation
|     |     | Cyber mercenaries and the commercial   |     |     | 79  |
| --- | --- | -------------------------------------- | --- | --- | --- |
Endgame demonstrate what can be
cyber intrusion market
achieved when technical insights and
investigative action are aligned against
a common threat.
Edvardas Sileris, Head of the European Cybercrime Centre (EC3)
Europol EC3
62

63
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
retnec
eht
ta
si
ytitnedI
ksir
rebyc
nredom
fo
Defending against identity Scale, speed, and automation Recommendations
are changing the game
compromise
Prioritize identity-centric controls.
Unchanged Changed Implement phishing-resistant authentication and
DART continues to observe identity
reduce reliance on reusable credentials across human
compromise as the leading threat for identities. Reduce reliance on long-lived credentials
organizations, despite the attack surface Identity compromise Scale of access by adopting short-lived tokens and automating
credential rotation.
increasing at scale.
Credential reuse Speed of execution
As organizations rely more on cloud platforms, AI Strengthen visibility into identity usage.
systems, and automated processes, a single cyber Monitor for anomalous access patterns, new
incident can rapidly impact more systems, data, and Privilege escalation Increase of use of permissions, and previously unseen application
business operations than in the past. Identity as a non-human identities or API activity.
common attack vector pre-dates organizational
dependencies on cloud, AI, and automation, but threat
actors are now operating at a bigger scale and with Access misuse Automation and orchestration Reduce the attack surface of non-human identities.
quicker speed. Enforce least privilege, rotate credentials regularly, and
restrict access to trusted locations.
As threat actors target non-human identities, they
DART observed a consistent pattern
are increasingly leveraging API and trusted workflow
integrations to escalate privileges, access sensitive data, 1. Initial compromise of a human identity Validate exposure through proactive testing.
and operate at scale. This reflects threat actors’ adoption Conduct assume-breach exercises (such as tests
2. Discovery of non-human identity credentials
of emerging technology and adaptation to organizational where you act as if a threat actor is already inside your
(For example, service principals, API keys)
infrastructure models while still using the same time- network). Focus on cloud services, SaaS platforms, APIs,
3. Escalation of privileges using existing access
tested attack methods against the identity plane. and workflow automation capabilities, prioritized based
4. Actions on objectives such as data exfiltration on where the highest-value data resides, is accessed, or
As organizations expand machine-to-machine access and and/or command-and-control deployment can be aggregated. Ensure these exercises are aligned
adopt AI-driven services, the attack surface continues to
to known threat actor behavior, including searching for
In the past year, DART observed an uptick in threat
grow. This means the most effective ways to reduce risk
plaintext and otherwise exposed credentials.
actor use of built-in workflow automation capabilities
and limit business impact stay the same, by:
and trusted integrations to orchestrate data exfiltration
• Strengthening identity-centric controls
at scale. Actors are able to operationalize access through
• Reducing reliance on reusable credentials trusted automation paths, collecting and exfiltrating
• Improving visibility across both human and non- data without requiring persistent interactive access.
human identities Because this activity leverages trusted identities and
native services, it can blend into normal operations
and evade traditional detection approaches.

64
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Identity is at the center of modern cyber risk
Passkeys are the safer Organizations need to choose the right
Risk class Synced passkeys Device-bound passkeys
passkey for their users
replacement for passwords
The FIDO Alliance, the National Institute of Standards
What Passkey syncs through the passkey Private key remains on one device Passkeys represent a strong countermeasure and Technology (NIST), and the UK’s National Cyber
it means provider’s cloud to the user’s or authenticator and cannot be
Security Centre (NCSC), along with many companies that
to both password and phishing attacks. other devices synced elsewhere
steward accounts for consumers and businesses, strongly
advocate passkey adoption. As organizations standardize
Passwords continue to be the first vulnerability many
using passkeys, choosing the right type—such as device-
attackers test. In the months immediately following Pros • Easy to use across phone, laptop, • More control over where
bound or synced—must be based on user roles and risk.
the launch of ChatGPT, Microsoft tracked a significant etc. credentials live
but short-term spike in password attacks, suggesting Passkeys enable phishing-resistant authentication and • Built-in backup if a device • Harder for attackers to copy
attackers were experimenting with using generative AI offer a viable alternative to passwords. However, as
gets lost or move
to launch them. The effectiveness of password attacks organizations secure authentication, threat actors try to
• Less chance of getting locked out
is waning, however. Overall, password attacks are down take over accounts by attacking other vulnerable areas— Device-bound passkeys
26% year-over-year. This provides strong evidence that for example, new-hire onboarding and account recovery. Synced passkeys can satisfy the implemented as multifactor
security measures such as MFA and passkeys are forcing These rely on weaker credentials like SMS or email-based requirements for a multifactor cryptographic devices can satisfy
attackers to pivot to other approaches to achieve access one-time passcode (OTP). The next step is therefore to cryptographic software AAL2 or AAL3 requirements.
to high-value targets. remove all phishable credentials from an account to make authenticator and can be used
not only authentication phishing-resistant but also make at AAL2 when implemented in
Phishing has evolved. In the last few years, attackers
the account itself phishing-resistant. accordance with NIST SP 800-63B-
have shifted to techniques like fatigue attacks and AiTM
4 requirements.
phishing to circumvent MFA. In the first six months of
2026, the share of AiTM phishing and token theft attacks
more than doubled. This is based on their share as a
Cons • Dependent on cloud/ • Only works on that one device
percentage of the overall attacks Microsoft detected
and, of course, is still comparatively small. Nonetheless, account security • No automatic backup or recovery
it shows the direction of travel. Passkeys are phishing- • Harder for IT to tightly control • Can be frustrating for users with
resistant credentials that aren’t replayable. They only multiple devices
work on the website or app for which they were created,
meaning if a user lands on a lookalike phishing site, their
passkey won’t work there. Best for Most users with non-admin Admins, sensitive systems,
privileges in the organization high-risk access

6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Identity is at the center of modern cyber risk
Phishing landscape goal is no longer just the password, but the persistent, “ This approach is particularly insidious because it exploits
authenticated session cookie itself. legitimate authentication flows end-to-end. No malware
is delivered, no credentials are harvested, and no
Today’s phishing landscape is no longer
Email bombing is a social engineering Phishing has obviously malicious infrastructure is presented. Instead,
centered on infecting systems. Instead, it’s pretext evolved from attackers obtain valid tokens directly through user
focused on guiding users to compromise actions, resulting in persistent, high-fidelity access that
simple malicious
their credentials, undetected. Across QR Phishing that targets Teams is a growing problem. In the appears entirely legitimate.
majority of these phishing cases, attackers initiate the attachments, with
code phishing, CAPTCHA-gated phishing, In the next section, we will look at how phishing
attack with email bombing, followed by a phishing
and malicious payload delivery, a consistent attackers increasingly operates through:
message in Teams from a newly created account that
pattern emerges: attackers are prioritizing poses as support or helpdesk to remediate the issue. designing attacks to • QR codes
techniques that evade automated In the last year, Defender Experts observed multiple slip past automated • CAPTCHA
threat actors using this technique. They then attempted • Malicious payloads
inspection, exploit trusted business file
to deploy backdoor and remote access tools using an security tools rather
formats, and move credential theft beyond RMM tool. As cybercriminals gain access through varied methods,
than deliver malware
defenders need to stay one step ahead.
the reach of traditional security controls.
directly.
Device code phishing adoption is on the rise
Phishing has evolved from simple malicious attachments,
with attackers increasingly designing attacks to slip past Once niche, device code phishing is now a preferred
automated security tools rather than deliver malware credential theft method for both nation-state and
directly. Underpinning much of this shift is the rise of PDF financially motivated actors. Defender Experts have
attachments, now the dominant vehicle across multiple observed this tactic level up in scale and sophistication.
phishing techniques. PDFs are trusted in business Around February 2026, attackers abused railway.com,
workflows, rarely blocked by policy, and can direct a legitimate platform-as-a-service provider, to
users to browser-based phishing experiences without host phishing pages and token-harvesting services
triggering many of the behavioral detections commonly linked to the Microsoft 365 OAuth device code flow.
associated with HTML or Scalable Vector Graphic (SVG) Targets received lures such as DocuSign requests,
files. voicemail alerts, and construction bid documents
that were often highly personalized and potentially
The increased availability of generative AI is also AI-generated. These redirected users to Microsoft’s
changing the phishing landscape. Threat actors are legitimate device sign-in page. Upon authentication,
using it to automate the creation of context-aware attacker-controlled services silently collected OAuth
lures—such as emails or messages designed to look real access and refresh tokens, which were replayed to access
by using specific details about a person or company— Microsoft 365 resources, bypassing passwords and MFA
that can bypass behavioral triggers. Attackers can then without traditional credential theft.
deploy adaptive backends that morph their signatures
to evade automated sandboxing. This evolution affects
not only spear phishing, but it has turned AiTM into a
scalable, automated identity theft pipeline where the
65

66
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
srekcatta
woH
ssecca
niag
QR code phishing can detect and analyze QR codes across attachment For defenders, the rapid cycling of delivery formats
types, particularly PDFs. Mobile security policies also highlights the limitations of file-type-based detection
need to account for the growing use of personal devices strategies. Techniques tuned to a specific attachment
QR code phishing (or “quishing”) continues
in phishing attacks. type can become obsolete within weeks. More resilient
to be an effective way for attackers to
defenses focus on identifying the behavior itself:
bypass traditional email defenses. CAPTCHA phishing CAPTCHA interstitial pages, multi-stage redirect chains,
and the separation between initial user interaction and
By embedding a malicious URL within an image, attackers CAPTCHA-gated phishing has emerged as the final credential harvesting page.
can evade text-based security scanning and direct
a popular method for concealing malicious
victims to phishing sites on devices that often fall outside
enterprise security controls. Between July 2025 and June content from automated security tools.
2026, Microsoft Defender for Office 365 detected more
than 145 million QR code phishing attacks. By placing a CAPTCHA page between the victim and
a phishing site, attackers create what appears to be a
QR code phishing attacks come in waves. The volume
routine verification step while simultaneously preventing
of these attacks declined throughout the second half of
automated scanners from accessing the malicious
2025 and reached its lowest point in January 2026. It then
content behind it. Between July 2025 and June 2026,
rebounded sharply, reaching an all-time high in March
Microsoft detected more than 100 million phishing
2026. The trend reversed in May, with volumes declining
attacks that used CAPTCHA pages as an intermediary
by more than half by June. Despite this drop, activity
step before presenting credential harvesting or malware-
remained substantially higher than levels observed
related content.
during most of 2025, underscoring how widely adopted
QR code phishing has become. During this period, attackers continuously rotated
delivery methods. In August 2025, embedded URLs
The way these attacks were delivered also shifted during
accounted for 58% of these attacks. By November, SVG
the year. PDF attachments were the dominant vehicle
files had become the leading delivery mechanism (47%).
overall, with their share growing to 79% of attacks
By April 2026, PDFs accounted for nearly two-thirds
by April 2026 after four consecutive months of gains.
of all CAPTCHA-gated phishing attacks, the highest
Meanwhile, DOC and DOCX attachments, which had
share achieved by any single delivery format during the
gained traction in late 2025, steadily declined.
reporting period.
For defenders, QR code phishing is particularly
The PhaaS platform Tycoon2FA, discussed later in the
challenging to confront because it exploits the gap
report, played a significant role in driving CAPTCHA-
between where organizations enforce security controls
gated phishing activity throughout late 2025. It grew
and the places where credential theft actually occurs.
from 9% of attacks in July to 76% by December. However,
A user may receive a phishing email on a managed
that influence declined rapidly during 2026, falling to 12%
corporate device, open an attached PDF, scan the QR
by June after law enforcement activity against the group.
code with a personal phone, and enter credentials on a
CAPTCHA-gated phishing activity weakened as the
phishing site without ever triggering traditional network-
platform’s influence diminished, suggesting that other
based detection. As attackers increasingly leverage QR
operators have not yet filled the gap as effectively as they
codes to move users outside monitored environments,
did the QR code phishing gap left by the service.
organizations should ensure that email security solutions

67
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How attackers gain access
Malicious payloads At the same time, PDF usage surged. After six consecutive Initial access brokers and
months of decline, malicious PDF volume increased
bulletproof hosting
by 38% in February 2026 and another 50% in March.
The role of malicious email attachments
Unlike HTML activity, which often spikes around specific Initial access brokers (IABs) continue to play a key
has fundamentally changed. A decade ago,
campaigns, elevated PDF activity remained consistent role in the cybercrime ecosystem. From July 2025
malicious attachments were primarily throughout the period. SVG payloads declined from 23% to June 2026, Intel 471 observed 2,591 advertised
associated with malware delivery. Today, of malicious attachments in July 2025 to 7% by June access sales affecting organizations in at least 117
2026, while DOC/DOCX files peaked at 17% in December countries. This was down from 4,356 offers last year
they are overwhelmingly used to facilitate
2025 before steadily declining throughout early 2026, as a handful of prominent brokers reduced their bulk
credential theft.
mirroring the displacement of Word documents by PDFs offerings. The United States accounted for the largest
seen across other phishing techniques. share of observed victims, followed by Canada, Italy,
Between July 2025 and June 2026, malicious payloads
Brazil, and the United Kingdom.
detected by Microsoft Defender for Office 365 were The growing dominance of PDFs across multiple
almost exclusively associated with credential phishing phishing techniques underscores their central role in the Professional services, IT, manufacturing,
rather than malware delivery. modern phishing ecosystem and highlights the need for telecommunications, and government organizations
defenders to focus on user interaction and credential were among the most frequently targeted sectors.
Instead of directly infecting systems, each month,
theft behaviors, not just malware detection. 45% of offers were obtained via the use of
between 89% and 96% of attachments directed users
legitimate but compromised login credentials, while
to phishing pages or presented convincing sign-in
37% of offers provided unauthorized access via
experiences designed to steal credentials. The attachment
compromised corporate remote access portals such
is no longer the weapon. Instead, it’s a vehicle that
as VPN-based devices.
delivers a user to the point of compromise.
Bulletproof hosting providers are a
HTML and PDF files are common vehicles for
foundation of the cybercrime ecosystem
malicious payload
Bulletproof hosting providers enable ransomware,
Between July 2025 and June 2026, Microsoft Defender for
phishing, malware distribution, and other
Office 365 processed hundreds of millions of malicious
malicious activity by providing infrastructure
attachments. HTML files were the most common
designed to resist disruption. Since mid-2025,
malicious payload in 10 months, though volumes
coordinated law enforcement actions targeting
fluctuated significantly because activity was often
several prominent providers have disrupted the
driven by a relatively small number of large phishing
landscape and increased pressure on criminal
campaigns. HTML remains attractive to attackers because
infrastructure networks.
it can render convincing phishing pages, redirect users
through multiple stages, load external content, or
present CAPTCHA challenges before revealing the final
phishing destination.

68
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
How attackers gain access
Disrupting phishing: Lessons The service’s overall effectiveness collapsed. “ Cybercrime ecosystems thrive when infrastructure,
Since Tycoon2FA only provides a hosting infrastructure hosting providers, distributors, and operators can
learned from the Tycoon2FA and email templates and not an actual email sending act with minimal interference. By coordinating across
capability, it’s likely many customers were not aware of By June, Tycoon2FA jurisdictions and sectors, defenders can disrupt
disruption the disruption and continued sending phishing emails activity had fallen those ecosystems at scale. The sustained decline in
without knowing that the pages behind those URLs were Tycoon2FA activity observed in the months following the
95% from its
Tycoon2FA was a significant PhaaS platform largely gone. As a share of all malicious email, Tycoon2FA operation demonstrates that these efforts can produce
throughout 2025, used for fraudulent went from roughly 11% at its mid-2025 peak to barely November 2025 peak. measurable improvements across the wider phishing
1.5% by April 2026. threat landscape, not just against a single threat actor
emails reaching over 500,000 organizations
or platform.
each month worldwide. In 2026, Microsoft,
The platform’s impact in the broader
Europol, and industry partners conducted a
phishing ecosystem was eroded
coordinated action to disrupt the service.
Tycoon2FA’s share of CAPTCHA-gated phishing
Tycoon2FA provides AiTM infrastructure, sold on dropped from 76% in December to 12% by June, while
Telegram. During the second half of 2025, Tycoon2FA its share of QR code phishing fell from 33% to 14%.
was linked to more than 15.1 million malicious emails Tycoon2FA domains were hosted almost exclusively
per month and accounted for up to 9% of all malicious on Cloudflare, which provided a degree of protection
messages Microsoft detected. By December 2025, against automated analysis and takedown using
Tycoon2FA was responsible for 76% of all CAPTCHA- CAPTCHAs designed to distinguish human visitors from
gated phishing activity and roughly a third of all QR code bots. As a result of the disruption, however, Tycoon2FA
phishing attacks. moved away from Cloudflare to a variety of alternative
platforms, attempting (unsuccessfully) to identify
replacement services that offered comparable anti-
Disrupting Tycoon2FA infrastructure
analysis protections.
In March 2026, the DCU, coordinating with international
The result of this transition has been a significant
law enforcement and industry partners, targeted
degradation in Tycoon2FA’s ability to evade detection
Tycoon2FA’s hosting infrastructure. The team went after
and successfully facilitate credential compromise.
the servers where phishing pages were rendered and
The operation also led to the arrest of two key figures
credentials intercepted, the core of what Tycoon2FA sells
from Tycoon2FA, who were detained by the Punjab
to its customers. As a result of this disruption operation,
National Cyber Crime Investigation Agency (NCCIA).
March phishing email volume fell 15%, with most activity
concentrated in a brief early-month window before the
operation took full effect. April dropped another 22%,
and by June, Tycoon2FA activity had fallen 95% from its
November 2025 peak.

69
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
ssecca
etamitigeL
taerht
eht
semoceb
RMM tools as a post- Attackers often finish by deploying ransomware from The hidden operational
the same operator session. RMM tools make it quicker
compromise standard and easier for attackers to bypass detection. Altogether, risk of identity and access
this means that a single RMM tool now supplants what
management in OT
Threat actors have long abused commercial once required a dozen discrete tools, collapsing most of
the attack chain into one trusted channel that existing
RMM software for persistent, hands-on- environments
detections might not flag. The pattern is particularly
keyboard access. The operational breadth pronounced in ClickFix-themed social engineering
and volume of abuse continues to grow. campaigns, where victims paste clipboard commands OT environments exist wherever physical
that invoke PowerShell to fetch and silently install an processes are automated and monitored
RMM tools now appear across a wider range of RMM client.
by digital systems. When it comes to
intrusion sets and attack chain stages, compressing the
The most consequential RMM-enabled intrusions the hardware and software that directly
path from initial access to impact and further eroding
concentrate on high-value assets—domain controllers,
the value of signature-based defenses. In Microsoft monitor and control physical equipment
identity-synchronization servers, and management
endpoint investigations in the past year, the appearance and industrial processes, identity has
infrastructure. Although RMM agents are deployed across
of an unsanctioned RMM agent has become one of
all asset classes, the majority of follow-on activity lands become the most consequential and least
the most reliable mid-stage indicators of a human-
on domain controllers, where a single trusted remote governed control point.
operated intrusion.
session offers the shortest path to tenant-scale impact.
RMM agents are typically introduced within minutes of a The endpoint evidence is often minimal: routine-looking Enterprise identity controls have been hardened, but
threat actor establishing a foothold and are configured RMM and remote tunnel activity, signed where possible, OT floors still run on default credentials, shared service
to auto-launch on logon. Since RMM platforms ship with and indistinguishable from sanctioned administration. accounts, and maintenance sign-ins that haven’t been
enterprise-grade file transfer, scripting, screen sharing, rotated since commissioning. Every organization that runs
unattended logon, and session recording, threat actors physical operations on digital controls carries an identity
have the operational reach of a senior administrator exposure risk.
from a single agent. Across Microsoft post-incident
In May 2025, the US government warned that attackers
reviews, the introduction of an unsanctioned RMM agent
were accessing industrial control systems (ICS) and
consistently preceded:
supervisory control and data acquisition (SCADA) systems
• Credential harvesting
in the US oil and gas sector using basic techniques and
• Lateral movement through the RMM’s built-in remote
succeeding because of poor cyber hygiene and internet-
command and file copy features
exposed assets. Seven months later, a second federal
• Token theft and persistence in cloud identity with advisory highlighted pro-Russia groups had accessed OT
mailbox rule or OAuth consent abuse control devices through minimally secured connections,
• Encrypted exfiltration through the agent’s with impacts including physical damage.
transfer channel

70
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Legitimate access becomes the threat
The hidden operational risk of identity and access of an identity-aware access policy is architecturally The three pillars of OT identity governance:
management in OT environments (continued) incompatible with the device itself. From awareness to accountability
Default credentials on many OT devices are the result
The recommended fix came down to eliminating 1. Treat OT identity as an operational risk, not an
of physical infrastructure that was not designed to be
default credentials and requiring strong authentication. IT problem. A compromised OT credential is a
secured the way we now require. Changing a default
Threat actors don’t have to be sophisticated if they’re production event, a safety liability, and a regulatory
password might disrupt the process in which it’s
able to find unlocked doors. The barrier to entry is not exposure. Governance needs to reflect that
embedded. But this is the gap adversaries are now
technical; it is the absence of identity governance. distinction. Who owns OT identity risk today, and
actively targeting. Industrial environments have become
is it sitting in the right conversation with the right
While this problem is not new, its consequence profile preferred, high-leverage targets precisely because the
consequence framing?
is. As the boundary between IT and OT continues to operational consequence of disruption is immediate and
dissolve—through digital transformation, remote costly. Aging devices, default credentials, limited patching 2. Get a full inventory of every OT identity
monitoring, vendor access, and connected supply cycles, and identity blind spots are sector-agnostic. today. You cannot govern what you cannot see.
chains—a compromised identity means exposure to both Discover default credentials, dormant vendor
data and physical systems. When physical systems are The threat is outpacing the field’s ability to respond. accounts, shared service sign-ins, machine identities,
manipulated, they don’t generate breach notifications; In 2023, the CISA ICS advisory program issued 380 and embedded device credentials.
advisories. That rose to 423 in 2024 and 508 in 2025.
they generate major incidents: production halts, 3. Connect OT Identity Access Management (IAM)
equipment damage, worker safety incidents, and in the The foundational architectural decision is to give maturity to business continuity and insurance
most severe cases, public safety events. OT its own purpose-built identity environment. posture now. As OT connects to cloud infrastructure,
When operational workloads often run on identity exposure to ransomware reaches operational
Many organizations have responded to this exposure
infrastructure meant for other purposes, the mismatch systems directly. Cyber insurers are beginning
by separating IT and OT onto different networks.
shows. Technical debt piles up, credential and access to require evidence of OT identity controls.
Network segmentation governs where traffic can
changes become risky, engineering teams fall back on Regulators are moving in the same direction.
travel, but it becomes irrelevant when a valid credential
workarounds, and the tools never get used to their full This is a business posture decision, not a security
authenticates on either side of that boundary. An
capability. A purpose-built identity environment, on backlog item.
adversary doesn’t need to breach a segment if they
the other hand, closes all of those gaps. Policies are
can sign in.
configured for OT from the start, and modern identity
capabilities can be applied as intended, not bent around
Many devices were not designed for modern
a framework that belongs to a different environment.
authentication processes
In OT, a significant portion of devices currently running
were engineered decades before modern identity
concepts existed. Programmable logic controllers
(PLCs), human-machine interfaces (HMI), embedded
sensors, and SCADA components running on firmware
that predates MFA are not candidates for modern
authentication enrollment. They don’t support certificate-
based access controls. In many cases, the concept

|     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Legitimate access becomes the threat
6202 tropeR esnefeD latigiD tfosorciM
Hybrid attack: Identity and  Hybrid attack: On-premises to cloud compromise
cloud compromise  Adversaries fully compromise on-premises, then steal cookies, tokens, and secrets to pivot into the cloud, where lateral movement runs
through identities and secrets (not RDP/WMI), escalating cloud privileges before exfiltrating data to attacker-controlled storage.
Hybrid attacks have become common in
| On-premises  | Pivot • On-Prem -> Cloud  |     |     |     |     |     |
| ------------ | ------------------------- | --- | --- | --- | --- | --- |
modern intrusions. Rather than remaining
confined to a single domain, many
| On-premises   | Pivot to cloud  | Cloud (cloud  |     | Cloud   | Cloud   |     |
| ------------- | --------------- | ------------- | --- | ------- | ------- | --- |
campaigns span infrastructure, identity
compromise  lateral movement)  (cloud escalation)  (data exfiltration)
systems, and cloud resources in a connected
attack path. Hybrid attacks commonly
begin with exposed infrastructure, trusted  Initial access to  Credential   Lateral   Privilege   Exfiltration /
| persistence  | access  | movement  |     | escalation  | impact  |     |
| ------------ | ------- | --------- | --- | ----------- | ------- | --- |
business applications, or workloads,
then progress into identity and cloud
Exploit server or  Steal cookies, tokens,  Move through identities  Manipulate cloud roles  Platform-as-a-Service
environments. Persistence is distributed
VPN appliance  secrets  and secrets—not RDP/WMI  (PaaS) or storage data theft
Add credentials to identities
across endpoint, infrastructure, identity,
and cloud layers.  Perform domain lateral  Access exposed apps and  Replay stolen  and service principals  Transfer to attacker-
movement (Kerberoasting,  containers to reach cloud  tokens cookies  controlled cloud account
RDP, WMI)
Achieve kernel
rootkit persistence
T1190 - Exploit Public- T1539 - Steal Session Cookie  T1078.004 - Cloud Accounts  T1098.003 - Add   T1537 - Transfer Data
| Facing App                 |                            |                          |     | Cloud Roles       | to Cloud  |     |
| -------------------------- | -------------------------- | ------------------------ | --- | ----------------- | --------- | --- |
|                            | T1528 - Steal Application  | T1550 - Alternate        |     |                   |           |     |
| T1558.003 - Kerberoasting  | Access Token               | Authentication Material  |     | T1098.001 - Add   |           |     |
Cloud Credentials
| T1021.001 - RDP  | T1552 - Unsecured   |     |     |     |     |     |
| ---------------- | ------------------- | --- | --- | --- | --- | --- |
Credentials
T1014 - Rootkit
71

Persistence spread across layers
Attack is hybrid—persistence is distributed across endpoints, infrastructure, identity, and cloud.
After establishing persistence, threat actors use credential
theft, token access, secret retrieval, and identity
enumeration to expand control.
1. 2. 3. 4.
The defender operating model Endpoint layer Infrastructure layer Identity layer Cloud layer
Prevention focuses on reducing exposed
infrastructure, enforcing least privilege, and securing
identity boundaries. GOAL GOAL GOAL GOAL
Detection must correlate signals from infrastructure, Sustained foothold on Resilient control over critical Persistent access through identity Ongoing access to cloud
identity, and cloud to reconstruct the full attack path. compromised devices while infrastructure components beyond mechanisms that often bypass workloads, data, and services
evading detection and traditional endpoint visibility traditional security controls
Containment requires a coordinated response across
endpoint protections
identity, endpoint, and cloud systems, including revoking
tokens and removing malicious applications.
Recovery involves rebuilding trust in identity systems and
analyzing cross-domain impact. • Stealthy implants with kernel- • Compromise of unmanaged • Addition of MFA methods • Dormant or hidden
level components devices (ESXi, load balancers, • Creation of app secrets and cloud applications
The challenge comes from a lack • Process injection and hollowing network appliances) OAuth consent grants • Backdoor service principal name
of correlation across layers • Registry-based persistence • Firmware or configuration • Service principal provisioning (SPN) and long-lived credentials
• Scheduled task execution manipulation • Token theft and refresh • Exposure of storage access keys
Security teams should correlate infrastructure, identity,
• Credential harvesting and reuse • Creation and abuse of token abuse • Misconfigured roles and
endpoint, application, and cloud signals into a single
backdoor accounts excessive permissions
investigation path. They can then prioritize controls that
• SSH/web shell access persistence
reduce exposed entry points, harden identity boundaries,
revoke compromised tokens, and remove malicious or
over-permissioned applications. The operating priority
is to make identity a core control plane for detecting,
containing, and disrupting hybrid attacks before access
expands across on-premises and cloud environments.
72
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Legitimate access becomes the threat
Hybrid attack: identity and cloud compromise
(continued)
Hybrid persistence: Multi-layer, multi-platform, hard to fully eradicate
Avoid single-point remediation. Survive partial incident response actions. Enable rapid re-entry after eviction attempts.

73
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Legitimate access becomes the threat
Cloud identity abuse increases Data from Microsoft Defender XDR incidents between Cloud-related threat tactics Top cloud-related threat tactics
December 2025 and June 2026 reinforces that identity is by total alerts by total alerts from Microsoft
the way in for attackers. Entra ID Protection, Defender for
Attackers continue to pursue identity December 2025 – June 2026 (180 days)
Cloud, Defender for Office 365,
as a primary vector into and within the Initial access comes from password spray Key and Defender for Cloud Apps
cloud. In cloud identity abuse, threat actors between December 2025 and
attacks
leverage cloud-based identities (users, A Password spray attacks 124,146,529 June 2026.
applications, and workload identities) Password spray attacks account for over 99% of B AiTM credential phishing 151,168 Source: Microsoft Threat Intelligence
observed cloud initial access efforts. Password spray
to gain unauthorized access, escalate
can also be an effective post-compromise technique. C Device code phishing 896
privileges, and maintain persistence across Successful password spray attacks can enable ATO,
D Threats targeting or leveraging Azure 19,482,467
SaaS, cloud, and hybrid deployments. data access, and further lateral movement across cloud Blob Storage
services. AiTM credential phishing is the second most
Cloud identity abuse was once a technique limited to common enabler of cloud identity abuse (0.15%) and is a E Using token theft and token replay for 5,089
unauthorized access
highly advanced nation-state actors. Now, it’s used by all more efficient initial access method because it intercepts
threat actor types against all industries. Cloud identity authentication flows in real time to capture credentials, F Malicious use of Microsoft Graph API 1,262
abuse typically starts with credential access techniques MFA responses, and session tokens that provide
such as password spray or AiTM phishing. Post-access, immediate authenticated access to cloud services.
threat actors operate within legitimate identity systems A
and APIs to establish persistence, move laterally, and Threat actors persist post-compromise
access sensitive data across SaaS and infrastructure-as-
In post-compromise cloud identity abuse, threat actors
a-service (IaaS) services. Threat actors use automation,
misuse user and workload identities to operate within
including AI-assisted content generation, to scale attacks.
trusted authentication boundaries. Threat actors maintain
They also increasingly abuse legitimate identity features
persistence by adding credentials to service principals,
and cloud APIs, helping malicious activity blend into
abusing cloud applications, and replaying tokens from
normal operations.
MFA-authenticated sessions, enabling long-lived access
to Microsoft Graph and cloud control planes.
1 10 100 1k 10k 100k 1m 10m 100m
Total incidents (180 days)
esimorpmoc-erP
esimorpmoc-tsoP
B
C
D
E
F

| Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Legitimate access becomes the threat
6202 tropeR esnefeD latigiD tfosorciM
Exchange mailbox exfiltration (including
Cloud identity abuse increases (continued)
Microsoft Graph API)
Threats targeting or leveraging Azure Blob
| Storage  |     | In Exchange mailbox exfiltration, threat actors  |     |     |     |
| -------- | --- | ------------------------------------------------ | --- | --- | --- |
leverage access to Microsoft Exchange Online
| Threat actors target Azure Blob Storage (Microsoft’s  |     | accounts to systematically collect and extract sensitive  |     |     |     |
| ----------------------------------------------------- | --- | --------------------------------------------------------- | --- | --- | --- |
cloud-based object storage) and related cloud resources
communications and attachments. They do this using
because the service plays a central role in storing and
legitimate platform features such as mailbox forwarding
processing large volumes of unstructured data. This data
rules, API access (including Microsoft Graph), and
| underpins critical workloads such as analytics, backups,    |     | automated workflows (for example, Power Automate)  |     |     |     |
| ----------------------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- |
| and AI pipelines. Threat actors exploit misconfigurations,  |     | without triggering traditional security controls.  |     |     |     |
exposed credentials, and overly permissive access
| mechanisms (such as shared keys or shared access       |     | This activity is particularly difficult to detect because it  |     |     |     |
| ------------------------------------------------------ | --- | ------------------------------------------------------------- | --- | --- | --- |
| signature (SAS) tokens) to gain access. They then use  |     | relies on sanctioned user behaviors and trusted services,     |     |     |     |
enabling sustained, low-visibility data collection over time
the platform for large-scale data exfiltration, malware
rather than immediate large-scale exfiltration. Access to
hosting, and persistence within cloud estates.
high-value business communications can then be used
By leveraging Azure-native tooling and workflows to
for BCI, espionage, or fraud.
blend into legitimate activity, threat actors can conduct
The prevalence of Azure Blob Storage targeting and
stealthy lateral movement, automation abuse, and
Exchange mailbox exfiltration highlights how quickly
downstream compromise of dependent services. This can
compromised identities translate into high-impact
ultimately affect data integrity and business continuity.
| Azure Blob Storage may also serve as a C2 channel or   |     | data theft and downstream compromise of dependent         |     |     |     |
| ------------------------------------------------------ | --- | --------------------------------------------------------- | --- | --- | --- |
| staging ground, amplifying its impact beyond a single  |     | services. To disrupt identity-driven attacks before they  |     |     |     |
become enterprise-wide incidents, defenders should:
resource to the broader cloud environment.
• Prioritize identity hardening and continuous monitoring
| Cloud application and SharePoint abuse  |     | • Strengthen MFA and conditional access  |     |     |     |
| --------------------------------------- | --- | ---------------------------------------- | --- | --- | --- |
• Reduce standing privileges
Threat actors are increasingly conducting cloud
| application and SharePoint abuse by leveraging  |     | • Tighten app and workload identity permissions  |     |     |     |
| ----------------------------------------------- | --- | ------------------------------------------------ | --- | --- | --- |
compromised identities and application permissions
in Microsoft Entra ID and Microsoft 365 to access data,
abuse APIs, and maintain persistence while blending into
normal activity. They then move laterally by abusing over-
privileged accounts and application permissions, pivoting
across cloud resources through legitimate API activity.
Meanwhile, workload identities (often lacking MFA and
holding broad permissions) allow for low-visibility control
of the environment.
74

75
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
:erawmosnaR tcapmi
ot
ssecca
morF
Ransomware landscape Five most prolific The rise of Qilin ransomware
ransomware families
Qilin was the leading ransomware this year,
Ransomware remains a persistent (from public leak site data) according to leak site data, up from fourth
and evolving threat, shaped by a place last year. This shift was driven by
several factors, including:
fluid ransomware-as-a-service (RaaS) Key %
1. The disruption or weakening of
ecosystem and expanding extortion
A Qilin 16% competing RaaS offerings such as
tactics. This section examines the most
RansomHub in 2025.
B Akira 8%
active ransomware families, the countries
2. Its competitive profit-sharing model;
and industries most affected, and the C Play (PlayCrypt) 7% affiliates keep 80-85% of ransom
differences between public leak site claims D Gentlemen 6% payments, higher than most other
RaaS splits.
and attacks detected by Microsoft.
E INC (INC Ransom) 5%
Unlike most ransomware variants, Qilin
has encryptors for both Windows and
Linux/ESXi environments, allowing
E operators to target enterprise virtualization
infrastructure in addition to endpoints.
The Qilin service offers affiliates a
D A robust support ecosystem that includes
negotiation assistance. The packaging
of tooling, infrastructure, and support
into a unified platform significantly
reduces the technical and operational
C
burden on affiliates and streamlines their
ransomware campaigns.
B
Source: Microsoft Threat Intelligence.
July 1, 2025 – June 29, 2026

76
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Ransomware: From access to impact
Ransomware landscape (continued) Impacted industries by percent, year over year
30%
Defender detections for 2026
According to public leak site data, Qilin listed the most 25%
victims in 2026 (16.4%, a 386% increase over last year).
Akira had the second-most number of victims (8.3%),
20%
while INC, DragonForce, Gentlemen, SafePay, and Sinobi
joined the top 10 for the first time. Within the top 10,
15%
Cl0p, SafePay, and Play were the only families that did not
offer official RaaS affiliation, highlighting how dominant
the RaaS model has become. 10%
While leak site data identifies the most active
5%
ransomware offerings, RaaS operators may selectively
post victims to advertise, coerce, or lie about victims,
0%
and so it may present an incomplete or distorted view.
A B C D E F G H I J K L
Analysis of ransomware events detected by Microsoft
Defender impacting enterprises, for example, found 2025 2026
Akira was the most active ransomware (22%, up
150% compared to 2025), followed by Qilin (14%, up
Industry 2025 2026 Industry 2025 2026
111%). Since new families like Gentlemen and Sinobi
accounted for a significantly smaller proportion of A Critical manufacturing 255 429 H Research and academia 96 78
events in our telemetry, this may suggest that leak site
activity was heavily pushed to attract attention to these B Other business entities 250 412 I Communications infrastructure 66 159
new offerings.
C Information technology 248 649 J Government agencies and services 57 133
D Consumer retail 140 164 K Financial services 50 75
E Transportation systems 133 178 L Defense industrial base 4 22
F Energy 124 104 Total 8,749 8,521
G Healthcare and public health 122 78 Unknown 7,100 5,819
2025 reporting period: July 2024–June 2025; 2026 reporting period: July 2025–June 2026.
Source: Microsoft Threat Intelligence

|     |     |     |     |     | Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| --- | --- | --- | --- | --- | ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Ransomware: From access to impact
6202 tropeR esnefeD latigiD tfosorciM
Microsoft Defender observed a 15.8% increase year-
Ransomware landscape (continued)
on-year in ransom detonations against enterprises.
Impacted countries by percent, year over year
The United States remains the country most impacted
by ransomware. While ransomware is often used against
45%  opportunistic targets, continued attacks against Israel
(which increased by 21% this year) may reflect Iran’s use
40%
of ransomware as a form of hybrid warfare.
35%
| 30%  |     |     |     |     |     |     | Ransomware leak site content is no longer         |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
| 25%  |     |     |     |     |     |     | confined to the dark web                          |     |     |     |
| 20%  |     |     |     |     |     |     | Threat actors and third parties are increasingly  |     |     |     |
distributing and amplifying stolen data via social media
15%
platforms such as X and open-source websites as part
| 10%  |     |     |     |     |     |     | of double extortion. Additionally, ecosystems like the  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- |
| 5%   |     |     |     |     |     |     | “Com” (short for The Community) have used tactics like  |     |     |     |
sextortion and swatting to get victims’ attention and
0%
for financial gain. In the last year, some actors leveraged
A  B  C  D E F G  H I J K  L social engineering tactics such as aggressive vishing for
initial access, consistent with general cybercrime trends.
|     |     |               | 2025      | 2026 |     |     |               |     |     |     |
| --- | --- | ------------- | --------- | ---- | --- | --- | ------------- | --- | --- | --- |
|     |     |               | Percent   |      |     |     | Percent       |     |     |     |
|     |     | change from   |           |      |     |     | change from   |     |     |     |
Country  2025  2026  2025–2026  Country  2025  2026  2025–2026
A  United States  724  1,087  50%  H  Switzerland  29  59  103%
| B  South Africa    | 7   | 17   | 143%  | I  Costa Rica  | 23     | 32     | 39%   |     |     |     |
| ------------------ | --- | ---- | ----- | -------------- | ------ | ------ | ----- | --- | --- | --- |
| C  Germany         | 59  | 222  | 276%  | J  Israel      | 19     | 23     | 21%   |     |     |     |
| D  Türkiye         | 0   | 3    | N/A   | K  Japan       | 57     | 95     | 67%   |     |     |     |
| E  United Kingdom  | 80  | 133  | 66%   | L  Italy       | 48     | 135    | 181%  |     |     |     |
| F  Canada          | 98  | 172  | 76%   | Total          | 8,749  | 8,521  | -3%   |     |     |     |
| G  Netherlands     | 36  | 56   | 56%   | Unknown        | 7,089  | 5,798  |       |     |     |     |
2025 reporting period: July 2024–June 2025; 2026 reporting period: July 2025–June 2026.
Source: Microsoft Threat Intelligence
77

78
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
noitpursid
emircrebyC
esnefed
evitcelloc
dna
Information sharing Structured, sustained collaboration supports Policy, partnerships, and
real impact
for the modern age enforcement: How to disrupt
This shift requires moving beyond episodic information
the ransomware economy
Cybersecurity in 2026 is shaped by exchange toward structured, sustained collaboration that
integrates policy, operations, and technical expertise.
persistent geopolitical competition and a
Microsoft’s initiative with NATO illustrates how such Because ransomware is an ecosystem
threat landscape that evolves faster than partnerships can be operationalized in practice and
problem, it is a policy challenge as much
traditional institutional responses. scaled to deliver meaningful impact. as a technical one. The same features
In February 2026, NATO’s Cyber and Digital
State-sponsored actors, cybercriminal groups, and that enable scale—shared infrastructure,
Transformation Division (CDT) and Microsoft signed a
hybrid campaigns increasingly operate across borders specialized services, and jurisdictional
Letter of Intent to strengthen cooperation in support
and sectors, targeting critical infrastructure, exploiting
of a rules-based approach to cyberspace, anchored in arbitrage—also create leverage points
emerging technologies, and leveraging complexity to
international law and agreed norms. Our experience for disruption when governments and
evade accountability. In this environment, no single
highlights several lessons for operationalizing
entity—government or private sector—has a complete industry act together. Sustained public-
such partnerships:
picture of the threat, nor the capacity to respond alone. private collaboration, targeted operational
1. Political signaling must be matched by sustained
As we’ve seen already in this report, this reality has execution. Framework agreements only deliver value disruption, and coordinated political
elevated information sharing to a central pillar of when accompanied by regular engagement, defined pressure—particularly on safe havens—are
cybersecurity and digital resilience. Effective defense workflows, and shared operational objectives. essential to reducing its impact.
depends on the timely exchange of technical signals,
2. Practical cooperation must be built through joint
strategic assessments, and operational insights across
activities. Exercises, incident simulations, and shared Government choices on legislation, cooperation, and
a diverse network of stakeholders. Public-private
playbooks are critical for developing trust, testing enforcement directly shape the threat environment.
partnerships are foundational to national and collective
coordination mechanisms, and ensuring that partners Four policy areas have the most impact:
security. At the same time, expectations of these
can operate effectively under real-world conditions.
partnerships are evolving. Governments are seeking more 1. Ransom payments. Microsoft strongly discourages
These tools translate high-level commitments into
actionable, high-speed intelligence to support decision- ransom payments because they reinforce criminal
operational readiness.
making, while the industry is being asked to play a more business models without guaranteeing recovery.
proactive role in detecting, disrupting, and responding to 3. Information sharing must be bidirectional and However, blanket bans risk revictimizing organizations,
malicious activity. timely. Establishing trusted channels that enable suppressing reporting, and weakening cooperation.
the exchange of intelligence and guidance—while A more effective approach is to discourage
respecting legal and privacy constraints—is key to payment while supporting victims through no-
maintaining shared situational awareness. fault reporting, incident response assistance, and
4. Coordinated attribution of malicious activity, resilience investment.
supported by both technical evidence and
political consensus, is essential for deterrence.
Closer collaboration between governments and
industry can help ensure that attribution is credible,
timely, and strategically effective.

| Introduction  | AI  | The threat landscape  | Cybercrime  | Resilience  | Appendix  |
| ------------- | --- | --------------------- | ----------- | ----------- | --------- |
Cybercrime disruption and collective defense
6202 tropeR esnefeD latigiD tfosorciM
| Cyber mercenaries and the  |     | Analysis of EU dual-use export controls has found  |     |     |     |
| -------------------------- | --- | -------------------------------------------------- | --- | --- | --- |
Policy, partnerships, and enforcement: How to disrupt
the ransomware economy (continued)  that existing frameworks lack sufficient enforcement
commercial cyber intrusion
and oversight to match the scale and urgency of the
2. Safe havens and state accountability. A small number  challenge. Intermediaries further entrench the problem—
market
of jurisdictions continue to function as safe havens,  brokers and resellers obscure supply chains and facilitate
tolerating or even enabling ransomware activity.  access, yet remain largely outside the scope of current
Microsoft continues to support the designation
| Cyber mercenaries have matured into   |     | policy responses.  |     |     |     |
| ------------------------------------- | --- | ------------------ | --- | --- | --- |
of persistent safe havens as “state sponsors of
a structured global ecosystem built on
Governments need to meet their commitments to
ransomware” to elevate ransomware to a matter
| a clear division of labor.  |     | enable change. The cyber mercenary ecosystem is  |     |     |     |
| --------------------------- | --- | ------------------------------------------------ | --- | --- | --- |
of international accountability, unlock broader
sustained by systemic enablers: they issue licenses
consequences, and reinforce deterrence through both
stigma and action.  In this established market, commercial actors develop  without scrutiny, make procurement decisions shielded
| and deliver intrusion capabilities, with capital-backed  |     | from oversight, and invest without consequence.  |     |     |     |
| -------------------------------------------------------- | --- | ------------------------------------------------ | --- | --- | --- |
3. Cross-border enforcement. Ransomware
| companies carrying out activities ranging from exploit  |     | If these conditions persist, technical mitigations  |     |     |     |
| ------------------------------------------------------- | --- | --------------------------------------------------- | --- | --- | --- |
investigations are inherently international, yet
| development to hacking-as-a-service and access-as- |     | and isolated enforcement actions will fall short.  |     |     |     |
| -------------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- |
cooperation remains uneven. Existing legal
| a-service. Crucially, this growth is accelerating. As the  |     | Governments therefore can and should reform and align  |     |     |     |
| ---------------------------------------------------------- | --- | ------------------------------------------------------ | --- | --- | --- |
frameworks already provide the necessary tools:
| market grows, so do the harms it creates. That includes  |     | their policy controls to close loopholes and target misuse.  |     |     |     |
| -------------------------------------------------------- | --- | ------------------------------------------------------------ | --- | --- | --- |
mutual legal assistance, data preservation, asset
| giving irresponsible actors access to high-end cyber  |     | Because the cyber mercenary market is structurally  |     |     |     |
| ----------------------------------------------------- | --- | --------------------------------------------------- | --- | --- | --- |
seizure, and extradition. The constraint is not legal
| weapons, commercially incentivizing efforts to break  |     | predictable, it is vulnerable to targeted intervention.  |     |     |     |
| ----------------------------------------------------- | --- | -------------------------------------------------------- | --- | --- | --- |
coverage, but inconsistent political will and operational
| critical digital infrastructure, and providing cover for  |     | Geographic concentration, repeat entrepreneurship,  |     |     |     |
| --------------------------------------------------------- | --- | --------------------------------------------------- | --- | --- | --- |
capacity to use these tools effectively.
| those looking to break international laws and abuse  |     | partnerships between hardware and spyware firms,  |     |     |     |
| ---------------------------------------------------- | --- | ------------------------------------------------- | --- | --- | --- |
4. Consequences and deterrence. Visible consequences
| human rights. Given that, Microsoft is redoubling our  |     | corporate rebranding, jurisdictional arbitrage, and  |     |     |     |
| ------------------------------------------------------ | --- | ---------------------------------------------------- | --- | --- | --- |
matter. Arrests, indictments, infrastructure takedowns,
| efforts to call for effective international action to tackle  |     | globally mobile capital all provide actionable points of  |     |     |     |
| ------------------------------------------------------------- | --- | --------------------------------------------------------- | --- | --- | --- |
and asset seizures demonstrate that ransomware is
| this threat.  |     | leverage for policymakers.  |     |     |     |
| ------------- | --- | --------------------------- | --- | --- | --- |
neither anonymous nor risk-free. Recent coordinated
| The persistence of this market reflects both an increase in  |     | Governments have acknowledged the problem and  |     |     |     |
| ------------------------------------------------------------ | --- | ---------------------------------------------- | --- | --- | --- |
actions in cooperative jurisdictions highlight what
sustained enforcement can achieve—and contrast  demand by states for powerful cyber intrusion tools and  committed to action through the Pall Mall Process.
sharply with the impunity available in safe havens.  weaknesses in mechanisms intended to constrain their  This initiative, launched by the UK and France in 2024, is
| abuse. Governments remain among the most influential        |     | dedicated to tackling the proliferation and irresponsible  |     |     |     |
| ----------------------------------------------------------- | --- | ---------------------------------------------------------- | --- | --- | --- |
| customers and users of cyber mercenaries, with legal        |     | use of commercial cyber intrusion capabilities.            |     |     |     |
| cases in Italy, Spain, Greece, and Poland highlighting not  |     | The process created a voluntary and non-binding ‘code      |     |     |     |
| only the extent of public sector purchasing but persistent  |     | of practice’ for states, but unfortunately, governments    |     |     |     |
| challenges in accountability and oversight.                 |     | seem to have stalled in the implementation phase of        |     |     |     |
their commitments.
79

In Microsoft’s experience, disruption is most effective
when it targets the economic and operational
foundations of the market and when disruption is carried
out in collaboration with other partners. By combining
technical disruption, legal action, threat intelligence,
product security, and policy advocacy, stakeholders can
intervene across the full life cycle of intrusion capabilities.
We call on our partners to work with us to go further:
1. To ensure that commitments made through the
Pall Mall Process and other fora are translated into
enforceable implementation.
2. To collaborate on targeted action against vendors,
brokers, investors, customers, and other enablers.
That means closing procurement, oversight, and
accountability gaps; increasing transparency around
government use of commercial intrusion capabilities;
aligning sanctions, licensing, and enforcement decisions
across jurisdictions; and using shared intelligence to
disrupt repeat offenders before they can rebrand,
relocate, or scale. The goal is to reduce demand, raise
the cost of abuse, and make the cyber mercenary market
less profitable, less permissive, and less able to operate in
the shadows.
80
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Cybercrime disruption and collective defense
Cyber mercenaries and the commercial 1. Setting spyware standards
cyber intrusion market (continued) after Europe’s spying scandal
2. CDT Europe Report: EU
Export Controls Are Failing
to Address the Spread
of Spyware - Center for
Democracy and Technology
3. Mythical Beasts: Investigating
the role of intermediaries in
the proliferation of offensive
cyber capabilities

| Introduction | AI  | The threat landscape | Cybercrime | Resilience | Appendix |
| ------------ | --- | -------------------- | ---------- | ---------- | -------- |
6202 tropeR esnefeD latigiD tfosorciM 4  Resilience  Trust, software, and supply chain security  82
|     |     | Digital media integrity in the age of AI            |     |     | 82  |
| --- | --- | --------------------------------------------------- | --- | --- | --- |
|     |     | Weaponizing trust                                   |     |     | 83  |
|     |     | Supply chain compromise                             |     |     | 84  |
|     |     | Critical infrastructure and operational technology  |     |     | 85  |
|     |     | Defending a nation starts with defending its        |     |     | 85  |
critical infrastructure
|     |     | Threat and vulnerability management for critical   |     |     | 87  |
| --- | --- | -------------------------------------------------- | --- | --- | --- |
infrastructure asset visibility
|     |     | Cyber-physical threats to critical infrastructure   |     |     | 89  |
| --- | --- | --------------------------------------------------- | --- | --- | --- |
“
|     |     | National resilience and geopolitical security  |     |     | 90  |
| --- | --- | ---------------------------------------------- | --- | --- | --- |
Any comprehensive cybersecurity strategy
|     |     | From fragmentation to resilience: What digital   |     |     | 90  |
| --- | --- | ------------------------------------------------ | --- | --- | --- |
requires proactive investment in systemic   defense looks like in an era of polycrisis
prevention and decisive action against   From reactive defense to proactive cyber defense   90
|     |     | Evolving geopolitics of cybersecurity   |     |     | 91  |
| --- | --- | --------------------------------------- | --- | --- | --- |
threat actors. Through our collaboration
with Microsoft, we’ve seen firsthand how   Open-source software security   93
industry leadership on disruption efforts   Operationalizing cyber resilience: Lessons from    94
the ARC initiative
can both reduce threats across the entire
ecosystem and produce targeted threat   Supporting the future of the CVE Program  95
|     |     | Subsea cables and global connectivity:    |     |     | 96  |
| --- | --- | ----------------------------------------- | --- | --- | --- |
intelligence to help organizations better
Building resilience through a comprehensive
understand and defend against future   approach to security
criminal and nation-state intrusions.
|     |     | Preparing for the next security transition  |     |     | 97  |
| --- | --- | ------------------------------------------- | --- | --- | --- |
Nicholas Leiserson, Senior Vice President for Policy
|     |     | Quantum-safe readiness for organizations:    |     |     | 97  |
| --- | --- | -------------------------------------------- | --- | --- | --- |
Institute for Security and Technology
Start preparing today
|     |     | Securing the quantum future through policy  |     |     | 98  |
| --- | --- | ------------------------------------------- | --- | --- | --- |
81

|     |     |     |     | Introduction | AI  | The threat landscape |     | Cybercrime | Resilience | Appendix |
| --- | --- | --- | --- | ------------ | --- | -------------------- | --- | ---------- | ---------- | -------- |
    dna ,erawtfos ,tsurT  ytiruces niahc ylppus
| Digital media integrity  |     |     | These dynamics warrant sustained executive attention, as  |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Resources
6202 tropeR esnefeD latigiD tfosorciM digital media integrity is a sociotechnical challenge, with
in the age of AI
|                                    |     |     | vulnerabilities emerging at the complex intersection of  |     |     |     |                                                                     |     |     |     |
| ---------------------------------- | --- | --- | -------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- |
|                                    |     |     | technology and human behavior.                           |     |     |     | Media Authenticity Methods in Practice: Capabilities, Limitations,  |     |     |     |
| For decades, photographs, videos,  |     |     |                                                          |     |     |     | and Directions                                                      |     |     |     |
This is the context for Microsoft’s report, Media Integrity
| audio recordings, and official digital  |     |     | and Authentication: Status, Directions, and Futures   |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
communications were implicitly trusted.    (MIA), which examines the current authentication    A new study explores how AI shapes what you can trust online
|                                                              |     |     | ecosystem, including the opportunities and limitations      |     |     |     |                                                    |     |     |     |
| ------------------------------------------------------------ | --- | --- | ----------------------------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
| Today, that assumption is increasingly                       |     |     |                                                             |     |     |     |                                                    |     |     |     |
|                                                              |     |     | of provenance, watermarking, fingerprinting, and            |     |     |     |                                                    |     |     |     |
|                                                              |     |     |                                                             |     |     |     | Coalition for Content Provenance and Authenticity  |     |     |     |
| challenged.                                                  |     |     | detection. Building on Microsoft’s contributions to the     |     |     |     |                                                    |     |     |     |
|                                                              |     |     | technical foundations of media provenance and its role      |     |     |     |                                                    |     |     |     |
| Generative AI enables the creation of highly persuasive      |     |     |                                                             |     |     |     |                                                    |     |     |     |
|                                                              |     |     | as a co-founder of Coalition for Content Provenance and     |     |     |     |                                                    |     |     |     |
| synthetic media, while the liar’s dividend, the advantage    |     |     |                                                             |     |     |     |                                                    |     |     |     |
|                                                              |     |     | Authenticity (C2PA), the report helps leaders navigate      |     |     |     |                                                    |     |     |     |
| gained by falsely claiming authentic content is fabricated,  |     |     |                                                             |     |     |     |                                                    |     |     |     |
|                                                              |     |     | advances in generative AI, evolving legislation, and the    |     |     |     |                                                    |     |     |     |
| makes it easier to dismiss genuine evidence.                 |     |     | growing adoption of authentication technologies.            |     |     |     |                                                    |     |     |     |
| A critical challenge of the AI era is the growing            |     |     | In practice, authentication methods serve different         |     |     |     |                                                    |     |     |     |
| difficulty of determining which content can be trusted.      |     |     |                                                             |     |     |     |                                                    |     |     |     |
|                                                              |     |     | purposes and have important limitations. Content and        |     |     |     |                                                    |     |     |     |
| The implications extend beyond trust in everyday online      |     |     |                                                             |     |     |     |                                                    |     |     |     |
|                                                              |     |     | associated signals can be altered, degraded, or lost as     |     |     |     |                                                    |     |     |     |
| content, affecting business continuity, brand reputation,    |     |     |   media moves across platforms. To assess the implications  |     |     |     |                                                    |     |     |     |
| crisis response, exposure to fraud, geopolitical stability,  |     |     |   of these real-world disruptions, researchers evaluated    |     |     |     |                                                    |     |     |     |
| and an informed citizenry—a foundation of democracy.         |     |     |   hundreds of authentication scenarios through              |     |     |     |                                                    |     |     |     |
Several dynamics are contributing to this shift:
|                                                       |     |     | sociotechnical red-teaming exercises. Only a limited       |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| • Synthetic content creation is growing rapidly,      |     |     | subset yielded high-confidence validation, with the        |     |     |     |     |     |     |     |
| increasing both the volume of content that must be    |     |     |   strongest results observed when provenance and           |     |     |     |     |     |     |     |
| evaluated and the baseline level of uncertainty.      |     |     | watermarking were linked.                                  |     |     |     |     |     |     |     |
| • Mixed media will become harder to interpret, as     |     |     |                                                            |     |     |     |     |     |     |     |
|                                                       |     |     | The MIA report concludes that trust in digital media will  |     |     |     |     |     |     |     |
| authentic, altered, and fully synthetic elements are  |     |     |                                                            |     |     |     |     |     |     |     |
|                                                       |     |     | depend not on any single technology, but on layered        |     |     |     |     |     |     |     |
combined in ways that complicate verification.
|                                                            |     |     | defenses, transparent systems, continual red teaming to       |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| • Offline media creation introduces new security risks,    |     |     | inform evolving standards, and sustained collaboration.       |     |     |     |     |     |     |     |
| as content can be generated or modified outside            |     |     |   Organizations that recognize media integrity as             |     |     |     |     |     |     |     |
| observable systems and then introduced into digital        |     |     |                                                               |     |     |     |     |     |     |     |
|                                                            |     |     | foundational infrastructure will be better positioned to      |     |     |     |     |     |     |     |
| environments with incomplete, compromised, or              |     |     |   strengthen resilience, protect their reputations, maintain  |     |     |     |     |     |     |     |
| misleading provenance information.                         |     |     | operational continuity, and build confidence in AI-           |     |     |     |     |     |     |     |
| • Authentication signals are proliferating but remain      |     |     |   enabled innovation.                                         |     |     |     |     |     |     |     |
| inconsistent, creating fragmentation across tools,         |     |     |                                                               |     |     |     |     |     |     |     |
| platforms, and standards and making trust more             |     |     |                                                               |     |     |     |     |     |     |     |
difficult to establish.
82

83
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Trust, software, and supply chain security
Weaponizing trust: Malicious The operation reveals an emerging threat to
the software supply chain
abuse of code signing
Rather than attempting to bypass security controls, threat
infrastructure actors increasingly seek to exploit the trust mechanisms
designed to protect users. By fraudulently obtaining
In May 2026, Microsoft led a global legitimate code-signing capabilities, cybercriminals
can make malware appear authentic, increasing the
effort to expose and disrupt a growing
likelihood that malicious software will evade detection
cybercriminal ecosystem. Fox Tempest, a
and reach victims.
financially motivated threat actor, operated
Fox Tempest leveraged Microsoft’s artifact signing
a malware-signing-as-a-service (MSaaS).
processes by creating fraudulent developer identities
This model meant that cybercriminals, and submitting malicious binaries for signing. By passing
including ransomware groups, could access through legitimate verification steps, the threat actor was
able to obtain authentic Microsoft-signed certificates
trusted, signed malware for use in attacks
for malware payloads, including ransomware loaders
against schools, hospitals, and critical
and infostealers. Fox Tempest industrialized this abuse
infrastructure. process, using automation and social engineering
to onboard new developer accounts and submit
Through technical investigation, legal action, and malicious artifacts.
collaboration with industry and law enforcement
partners, Microsoft identified and dismantled key Code signing depends on vigilance across
elements of the threat actor’s online infrastructure.
the entire trust lifecycle
In May 2026, the DCU filed a civil case enabling the
seizure of a core domain and disabling hundreds of Attackers do not just bypass controls, they actively seek
actor-controlled virtual machines and accounts. This legal to inherit trust by manipulating legitimate processes.
action disrupted the actor’s operations, cutting off access Trust mechanisms must evolve alongside attacker
for other cybercriminals. Simultaneously, Microsoft tradecraft, and defenders must be prepared to validate
revoked over a thousand fraudulent code-signing trust continuously rather than assume it indefinitely.
certificates and dismantled supporting infrastructure, This calls for continuous integrity across issuance, use,
preventing further abuse. These efforts culminated in and monitoring.
the arrest of a primary suspect in Europe, demonstrating
how coordinated public-private action can translate
intelligence into real-world disruption.

84
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Trust, software, and supply chain security
Supply chain compromise: 2. Exploiting code libraries. Large code libraries, like Recommendations
npm, are central hubs where developers share and
Prioritize controls that reduce the blast radius of
From isolated incidents to download reusable code. Their massive scale makes
package compromise, limit credential exposure in
them prime targets. Attackers can inject malicious
cascading ecosystem attacks build environments, and shorten time--to--detection code into these libraries which then automatically
for supply chain intrusions.
spreads to thousands of other projects. This is a
Software supply chain compromises have particularly effective initial access vector because
evolved. In the past, attackers focused during installation, a package can automatically run Avoid exposing sensitive access tokens in development
its code, often before anyone reviews it. Access to workflows, use short--lived credentials, and design
on small, single-target hacks, targeting
these libraries relies heavily on individual developer build systems as temporary.
intrusion to a specific vendor. accounts, the credentials for which can be stolen
through phishing. This reinforces how attackers are
Today they use massive, automated attack chains that increasingly exploiting trusted relationships within Strengthen publisher accounts. Enforce strong security
spread quickly across multiple platforms, using one software ecosystems rather than targeting individual measures like phishing-resistant MFA for all accounts
weak spot to automatically break into many connected endpoints directly. As those ecosystems become more with publishing access to code libraries.
systems. Attacks span multiple package registries (online interconnected, compromises involving packages,
digital storage hubs where developers download ready- developer accounts, AI-assisted development tools, Rotate credentials after exposure. If any software
made code pieces) and CI/CD platforms (automated and build infrastructure can rapidly extend beyond a is compromised, immediately change all accessible
systems that test and build new code changes for single organization. credentials and rebuild affected systems.
a project). What begins with a single stolen token
or misconfigured workflow can cascade outward:
compromising packages, tools, and organizations Detect new attack methods. Monitor for unusual
at scale. software activity, unexpected connections, and new
evasion techniques.
Two common supply chain attack methods are:
1. Poisoning trusted downloads. Attackers can secretly
Maintain a software inventory. Keep an up--to--date list
replace legitimate software with tampered versions
of all open-source components used in production to
containing hidden malware. For example, in April 2026,
quickly respond to new compromises.
the CPUID website, a popular source for computer
hardware tools, was compromised. Attackers swapped
genuine installers with versions that installed malware,
giving them remote control over affected machines.
For users, everything appeared genuine—the
download came from an official site and the software
seemed authentic. They had no obvious reason to
mistrust it.

85
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
erutcurtsarfni
lacitirC
ygolonhcet
lanoitarepo
dna
Defending a nation starts Figure 1 – Attacks against SLED and the critical infrastructure sector
with defending its critical
A
infrastructure
B
Nation-state actors, ransomware syndicates,
C
and opportunistic criminals are pivoting
from data theft toward disruption of the
D
physical services that hold communities
together. E
Securing state and local government, education (SLED), F
and critical infrastructure is not just an IT problem.
It’s now a national security imperative that requires
G
breaking the vertical model in which regional IT defends
only regional systems, while municipalities, cities, schools,
H
and utilities fend for themselves.
Research and academia is the most-targeted SLED sector I
(38%)—more than transportation (22%) and government
(13%) combined. Educational institutions and systems sit
J
at the intersection of open collaboration, federal research
funding, and sprawling supplier ecosystems. This makes
0% 5% 10% 15% 20% 25% 30% 35% 40%
them a key entry point into the public-sector supply
chain. According to Microsoft’s Defender notifications, Key % Key %
cloud identity abuse is the most observed technique
against both SLED (62%) and critical infrastructure (78%), A Research and academia 38% F Energy 4%
highlighting the importance of defending identity in
B Transportation systems 22% G Government facilities 4%
these sectors (see Figures 2 and 3). Microsoft identified
threat actor activity leveraging OAuth consent abuse, a C Government agencies and services 13% H Chemicals 1%
technique that re-emerged prominently in the research
D Communications infrastructure 11% I Water and wastewater systems 1%
and academia sector over the last year and is now
considered a cross-industry method for exploiting trust E Critical manufacturing 7% J Emergency services 1%
relationships in SaaS ecosystems. The observed activity
included overlapping tradecraft commonly associated Data is from November 1, 2025 to April 30, 2026. Source: Microsoft Threat Intelligence.
with ShinyHunters.

86
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Critical infrastructure and operational technology
Defending a nation starts with defending its critical Figure 2 – Technique summary: Figure 3 – Technique summary: Figure 4 – Tool summary:
infrastructure (continued) SLED Critical infrastructure Critical infrastructure
Once inside, adversaries move with commodity
and bespoke tooling. Against critical infrastructure, E
D
Truebot malware (39%) and information stealers C
(38%) dominate the observed tool mix, with the
AzureHound framework (12%) used to map cloud-
E
attack paths. Information stealers accelerate the D
supply chain. They harvest credentials, which become
the next intrusion’s entry point, cascading across the B
C
vendors, integrators, and shared services that connect B
A
a municipality’s smallest water utility to its largest
hospital system.
A
Legacy water systems, residual
community risk A B
US drinking water and wastewater utilities run aging
operational technology, often maintained by private
operators and lower--capacity districts. In 2025, the
Environmental Protection Agency reported that more Key % Key % Key %
than 70% of inspected water systems failed to meet
basic cybersecurity requirements. Incidents such A Cloud identity abuse 62% A Cloud identity abuse 78% A Truebot malware 39%
as the late 2024 American Water customer--portal
B Password spray attacks 38% B Password spray attacks 13% B Information stealers 38%
outage, show how fast those gaps translate into
service disruption and community safety risk. C Brute-force attacks 2% C AzureHound framework 12%
D Evolving phishing threats 2% D Impacket 6%
E Other 5% E LemonDuck 5%
Figures 2 and 3 — Cloud identity abuse dominates the technique mix in both SLED (62%) Figure 4 — Truebot malware and information
and critical infrastructure (78%). Source: Microsoft Threat Intelligence. March 1 to June 30, 2026. stealers lead the tooling used against critical
infrastructure. Source: Microsoft Threat
Intelligence. November 1, 2025 to April 30, 2026

87
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Critical infrastructure and operational technology
Defending a nation starts with defending its critical infrastructure (continued) Threat and vulnerability Reframing TVM as a continuous
operational discipline
Recommendations management for critical
The key architectural shift is from tool-centric
infrastructure: From asset vulnerability management to continuous threat
Prime targets——like schools, water districts, Stand up civil cyber defense and coordinate
exposure management embedded into operations.
local agencies, and the vendors that serve response across boundaries. Pool capability visibility to active defense
Reporting metrics should shift from the number of
them——typically lack the resources to defend so no single jurisdiction defends alone across
patches deployed to exposure reduced, detection
themselves. Collective defense is needed to a state, through: Critical infrastructure defenders face a coverage increased, and time-to-mitigate compressed.
meet the scale of the threat. • SOCs fundamental mismatch: adversaries operate A continuous TVM model:
• Local defense
continuously, while traditional security • Integrates asset data, vulnerabilities, threats, and
Protect lifelines. Treat water, power, • National cybersecurity agencies telemetry into a live system
programs remain periodic.
communications, and emergency services as
• Sector--based information sharing and • Operates as a feedback loop, not a sequence of steps
a single attack surface. Fund areas that are
analysis centers
This gap is at the highest risk in datacenter environments • Prioritizes risk using context, not static severity
underserved for cyber investments, such as
rural areas and small towns. Create whole--of-- • Universities supporting critical infrastructure. Here, undetected • Adapts dynamically even when remediation
state shared service models that extend Zero • Volunteer cyber corps exposure does not just risk data loss but can cascade is constrained
into physical disruption, service instability, and safety
Trust, identity, observability, and response to Civil cyber defense gives target--rich, This shift aligns defense with how adversaries actually
impacts. Nation-state actors are pre-positioning within
the smallest jurisdiction. resource--poor communities shared operate—continuously probing, adapting, and exploiting.
infrastructure networks to enable future disruption or
monitoring, surge response, and mutual aid.
sabotage of critical operations. Meanwhile, financially At the core of this model is a reinforcing cycle of
It moves away from isolated approaches,
Defend identity first. Mandate phishing-- motivated actors increasingly exploit unpatched systems, four capabilities:
where every organization tries to build
resistant MFA, disable legacy and high--risk targeting availability rather than data. 1. Asset visibility. Effective defense begins with
their own.
authentication flows (including unmanaged
complete and continuously updated awareness
As a result, threat and vulnerability management (TVM)
device code flow), and deploy continuous
of all assets across IT and OT environments.
must evolve into a continuous, integrated operational
identity threat detection. Build an AI-defended workforce. Pair AI- That includes device relationships, network topology,
discipline, not a set of tools or periodic activities.
driven vulnerability management with segmentation boundaries, configuration state, and
Frontier AI is accelerating vulnerability discovery and
student SOCs, community college operational dependencies.
exploitation, widening the gap between discovery and
pipelines, and apprenticeships to close
remediation. For critical infrastructure operators, closing 2. Continuous vulnerability identification.
the gap between adversary speed and
this gap is now a strategic imperative. As a result, TVM Vulnerability management here requires a shift from
defender capacity.
must evolve from a periodic security function into a static scanning to continuous exposure awareness:
continuous operational capability. Executed correctly, • Integrating vendor advisories, ICS-specific
Prepare for the quantum horizon. TVM becomes a closed-loop defense system binding disclosures, and CVEs
Begin crypto--agility and post--quantum asset visibility, vulnerability identification, threat • Prioritizing by asset criticality and exposure
migration planning now so trust in public-- detection, and AI-accelerated insight. Each capability
• Accepting delayed or constrained patching realities
sector computing survives the transition. reinforces the others to create a compounding
defensive advantage.

88
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Critical infrastructure and operational technology
“
Threat and vulnerability management for critical Recommendations for operators
infrastructure: From asset visibility to active defense
Critical infrastructure and datacenter operators
(continued) The key architectural should make it a priority to:
3. Threat detection and active defense. Detection must
shift is from tool-
operate as a continuous, intelligence-driven function Establish verified, continuously updated asset
rather than reactive alerting. Effective datacenter centric vulnerability visibility across IT and OT.
detection includes behavioral endpoint visibility management
across operational systems, identity and network
telemetry to detect lateral movement, OT-aware to continuous Integrate vulnerability data with asset context and
detection logic, and threat intelligence mapped to threat exposure threat intelligence.
adversary behavior—not indicators that expire.
management
4. AI-accelerated insight. At datacenter scale, manual Build detection capabilities aligned to adversary
analysis is insufficient. Frontier AI is creating both new embedded into techniques, not signatures.
risks and new defensive capabilities. As vulnerabilities
operations.
outpace remediation, AI helps prioritize exposures,
Measure effectiveness by coverage and detection
identify attack paths, correlate signals, and accelerate
gaps, not alert volume.
response, enabling teams to focus on the risks
most likely to be exploited. AI prioritizes high-risk
alerts (triage compression), accelerates detection Introduce AI--driven correlation early to avoid
engineering cycles, correlates identity, network, scale bottlenecks.
and OT signals in near real time, and maintains a
continuously updated risk model.
Treat TVM as a core operational discipline, not a
The defining strength of this model is interdependence:
siloed security function.
• Asset visibility improves vulnerability accuracy
• Vulnerability context strengthens detection prioritization
• Detection insights refine asset and exposure awareness
• AI continuously correlates and accelerates all layers
This creates compound resilience against increasingly
AI-enabled adversaries. Organizations that integrate
AI into TVM can reduce exposure windows, prioritize
remediation based on real-world risk, and respond
more effectively to threats operating at machine speed.
Closing the loop between proactive exposure reduction
and reactive threat detection covers both sides of
the breach equation—shrinking attack surface while
catching what slips through.

89
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Critical infrastructure and operational technology
Cyber-physical threats Datacenter physical systems should be defended Recommendations
as interconnected critical services
to critical infrastructure Organizations should adopt a resilience--focused
The six physical security domains are now cyber-physical:
defense strategy that goes beyond preventing
• Perimeter security intrusion. Key priorities include:
Cyber-physical threats are a strategic risk
• Access control
to critical infrastructure. Datacenters
• Surveillance and monitoring Detect and disrupt consequence--level manipulation
connect cloud services, facility operations,
• Asset protection by monitoring for unauthorized state changes and
physical security, power, cooling, and life- • Operational controls operational impacts, not just initial access.
safety systems. Compromise of IT, OT, • Environmental/facility safeguards
or digitally controlled building systems Each depends on controllers, sensors, connected Maintain independent verification of physical processes
can move quickly from network access to panels, management platforms, or identity systems that through trusted monitoring, manual validation, or
adversaries can target using familiar IT techniques. redundant sensing when digital control systems are
physical consequence: power loss, cooling
degraded or untrusted.
disruption, lockdown, lost visibility,
equipment damage, or life safety risk to
Strengthen coordination across cybersecurity, OT
personnel.
engineering, physical security, and facility teams to
respond effectively to cyber--physical threats.
For datacenters, cyber-physical risk concentrates where
digital control planes govern physical outcomes. Power,
heating, ventilation, and air conditioning (HVAC), Reduce both external and insider attack paths through
building management, access control, surveillance, fire strong identity protections, least--privilege access, and
suppression, and emergency systems are interdependent. continuous monitoring.
Compromise of one system can cascade into
downtime, unsafe conditions, lost visibility, or impaired
Minimize adversary dwell time with rapid detection,
emergency response.
containment, and response capabilities.
Regularly exercise cyber, physical security, and facility
recovery plans to ensure safe and timely restoration of
operations following an incident.

|     |     | Introduction | AI  | The threat landscape | Cybercrime | Resilience | Appendix |
| --- | --- | ------------ | --- | -------------------- | ---------- | ---------- | -------- |
    ecneiliser lanoitaN  ytiruces lacitilopoeg dna
From fragmentation to    From defense-in-depth to resilience-   From reactive defense to
6202 tropeR esnefeD latigiD tfosorciM
by-design
| resilience: What digital defense  |                                                      |     |     |     | proactive cyberdefense  |     |     |
| --------------------------------- | ---------------------------------------------------- | --- | --- | --- | ----------------------- | --- | --- |
|                                   | Defending against threats to interconnected systems  |     |     |     |                         |     |     |
looks like in an era of polycrisis
|                                               | requires visibility across domains, disciplines, and           |     |     |     | Government SOCs are no longer just         |     |     |
| --------------------------------------------- | -------------------------------------------------------------- | --- | --- | --- | ------------------------------------------ | --- | --- |
|                                               | geographies, as well as an understanding that digital          |     |     |     |                                            |     |     |
|                                               |                                                                |     |     |     | fighting human adversaries; they’re now    |     |     |
| For much of the past decade, cybersecurity    |   systems are inseparable from societal resilience.            |     |     |     |                                            |     |     |
|                                               | This reality challenges traditional approaches to cyber        |     |     |     | fighting automated, AI-accelerated attack  |     |     |
| strategies have been shaped by focusing on    |                                                                |     |     |     |                                            |     |     |
|                                               | defense such as defense-in-depth, where controls are           |     |     |     | infrastructure. Today, defenders need to   |     |     |
| distinct risks to cybersecurity—for example,  |                                                                |     |     |     |                                            |     |     |
|                                               | added in layers, and gives greater focus to resiliency.        |     |     |     |                                            |     |     |
|                                               |                                                                |     |     |     | be right every time across thousands of    |     |     |
| ransomware, distributed denial-of-service     |   Resilience-by-design assumes that failures will occur, that  |     |     |     |                                            |     |     |
|                                               |                                                                |     |     |     | systems, while an attacker needs only      |     |     |
|                                               | dependencies matter as much as adversaries, and that           |     |     |     |                                            |     |     |
| (DDoS) attacks, and supply chain attacks.     |                                                                |     |     |     |                                            |     |     |
|                                               | recovery and continuity are as critical as prevention.         |     |     |     | one path—and generative AI is helping      |     |     |
While these threats remain very real, they increasingly    find that path.
|                                                             | Cloud platforms can function as resilience enablers.  |     |     |     |     |     |     |
| ----------------------------------------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| fail to describe the environment in which digital risk now  |                                                       |     |     |     |     |     |     |
They offer consistent security baselines, global situational
unfolds. We have entered an era of polycrisis. This context    Nations that have invested in structured public-
|     | awareness, the ability to adapt at speed, and the  |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
is not defined by isolated events but by overlapping    collective management of complexity.    private collaboration demonstrate faster detection
disruption, leaving little to no breathing room to    and disruption of multi-sector campaigns.
recover. Geopolitical instability, economic pressure,    In a polycrisis environment, digital defense must evolve    Collaboration comes through joint operations centers,
rapid technological change, and persistent cyber    from guarding individual assets to developing systems    automated indicator-sharing platforms, and sector-
activity interact in ways that increase impact and reduce    that will function under pressure so that services to the    specific information sharing and analysis centers
public will continue. This requires organizations to design
response time. Digital systems are no longer stressed by    (ISAC). The most effective national threat intelligence
a single event; they are tested by overlap, dependency,    security for disruption, not just compliance, to align cyber    architectures are federated, rather than centralized.
and cascading failure.  resilience with broader continuity planning, and to treat    They operate under legal safe harbors that encourage
|                                                     | identity, data, and infrastructure as inseparable. It also  |     |     |     | good-faith sharing, support machine-readable formats  |     |     |
| --------------------------------------------------- | ----------------------------------------------------------- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
| This shift exposes a widening gap between how many  |                                                             |     |     |     |                                                       |     |     |
demands deeper collaboration—between public and    for automated ingestion, and function in near real time.
| organizations defend digitally and how risks emerge.  |   private sectors, across borders, and among organizations  |     |     |     |     |     |     |
| ----------------------------------------------------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Fragmented defenses—optimized for individual threats    Collaboration must actively work in practice, and
|     | that share infrastructure and risk—to ensure that  |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
or compliance requirements—become less successful    at pace. A detection authored inside one agency
|     | dependencies are known and managed.  |     |     |     |     |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
when crises start to unfold simultaneously. Today’s    should be deployed to peer agencies in hours, not
environment demands a move from fragmentation    weeks. And where agencies cannot reveal raw data,
toward persistent digital resilience.  privacy-preserving matching lets them compare threat
“
|                                                              |                                     |     |     |     | intelligence without exposing sensitive telemetry,  |     |     |
| ------------------------------------------------------------ | ----------------------------------- | --- | --- | --- | --------------------------------------------------- | --- | --- |
| Fragmentation is not just a technical issue—it’s built into  |                                     |     |     |     |                                                     |     |     |
|                                                              |                                     |     |     |     | resolving the tension between sovereignty and       |     |     |
| how many organizations operate. Over time, rules, silos,     |                                     |     |     |     |                                                     |     |     |
|                                                              | Digital systems are no longer       |     |     |     | collective defense.                                 |     |     |
| and quick fixes add complexity. Identity, infrastructure,    |                                     |     |     |     |                                                     |     |     |
| and OT often run separately. In a polycrisis, these gaps     |   stressed by a single event; they  |     |     |     |                                                     |     |     |
| become weak spots, slowing decision making when              |                                     |     |     |     |                                                     |     |     |
|                                                              | are tested by overlap, dependency,  |     |     |     |                                                     |     |     |
| speed matters. Improvements in one area may address          |                                     |     |     |     |                                                     |     |     |
| specific issues, but they don’t always add up to resilience  |   and cascading failure.            |     |     |     |                                                     |     |     |
across the whole system.
90

91
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
National resilience and geopolitical security
From reactive defense to proactive cyberdefense Evidence of the benefits of this type of organization Recommendations for Evolving geopolitics
(continued) already exists. Organizations leveraging Microsoft public sector leaders
Security Copilot report summarizing threats 60 to 70% of cybersecurity
National resilience can come from shared faster, sharply cutting the mean time to resolve critical Governments should strongly
agentic defense alerts. Autonomous tools such as the Phishing Triage consider investing in shared Nation states use cyber operations to coerce,
Agent filter out background noise, saving security teams services and federated SOC
shape conflict, and signal state capability.
Every department running its own Security Operation nearly 200 hours each month by closing thousands of models rather than agency--
Center (SOC) duplicates cost and tooling, while smaller false-positive alerts. Microsoft’s own security team now by--agency builds and This digitizes warfare in a way that draws in
agencies—municipalities, health authorities, school uses custom AI agents to autonomously investigate adopt bounded--autonomy civilians and private technology providers
boards, etc.—are left exposed by a chronic skills gap. 75% of incoming incidents (Microsoft, State of the SOC, governance now, before and can contribute to restrictions on
From many fragile, isolated SOCs, we must move 2026), freeing experts to hunt novel threats and architect agents proliferate. They should
toward one shared, agentic, multi-tenant cyber defense stronger defenses. establish collective--defense internet freedom as governments expand
capability that every agency consumes as a service. sharing under legal safe surveillance and control over digital spaces.
Of course, autonomy without accountability is a non-
In this ideal model, a central shared-services SOC starter in government. This agentic capability must be harbors and fund it sustainably In this environment, cloud platforms,
through transparent metering
operates the platform, the analysts, and an agent fleet on secured and governed. Low-risk actions such as alert communications networks, and AI-enabled
and chargeback.
behalf of dozens of agencies. This can reduce duplicated enrichment and threat intelligence summarization can services become key points of contestation,
tools and create economies of scale. The model preserves run autonomously; medium-risk actions like isolating
not just commercial assets.
autonomy and sovereignty by design. Each agency an account require human approval, while high-risk
keeps its own tenant, data residency, and Zero Trust decisions such as declaring a breach remain human-
The expansion of geopolitical competition in the
boundary, while central analysts operate across tenants led. Replayable reasoning trails record what each agent
cyber sphere underpins the launch of the UN
through delegated, just-in-time, least-privilege access. decided, on what data, with what confidence, and
General Assembly’s Global Mechanism (GMECH) on
Logs remain within agency-controlled environments and whether a human reviewed it—aligning with the NIST AI
information communication technologies (ICT) in
nothing is centralized that does not need to be. Risk Management Framework and the EU AI Act.
international security in 2026. The process highlights the
The defensive fleet follows a simple pattern: deny, complementary roles of technology and diplomacy:
disrupt, delegate.
“ Technical capabilities enable detection, disruption, and
• Deny: Agents deny adversaries by exposing and closing
recovery from cyberattacks. Diplomacy shapes the
attack paths before they’re reached.
broader environment—legal frameworks, policy choices,
• Disrupt: Agents disrupt threats through autonomous Microsoft’s own security team and norms—that define responsible state behavior
triage and containment. now uses custom AI agents to in cyberspace.
• Delegate: Agents delegate the work of codifying every
autonomously investigate 75% As a permanent forum for cyber diplomacy, the GMECH
lesson into new detections.
on ICTs’ value will depend on its ability to deliver tangible
In this agentic model, scarce analysts are freed of incoming incidents, freeing progress, particularly in strengthening protections for
from conducting manual triage and turned into experts to hunt novel threats critical digital infrastructure. That includes the cloud
strategic supervisors. services that underpin essential public and economic
and architect stronger defenses.
functions, such as healthcare and energy.
•

92
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
National resilience and geopolitical security
Evolving geopolitics of cybersecurity (continued) In an increasingly contested landscape, delivering Framework of Responsible Industry
cybersecurity demands clearer rules, credible
Behaviour for AI in the Military Domain
The future of cyberspace is shaped not only by accountability, and sustained cooperation.
operations but by governance. Much of the infrastructure Strengthening protections for critical infrastructure, As AI becomes more embedded in security and
and expertise underpinning resilience sits outside advancing operational accountability, and preserving defense, industry decisions shape real--world risk.
government. Meaningful stakeholder participation in the an open, secure, and resilient digital environment must Choices about system design, data practices,
GMECH is essential for ensuring that the rules that govern be shared priorities. The path forward will depend on testing, deployment, maintenance, and support
cyberspace are practical, implementable, and grounded translating commitments into practice—ensuring that affect reliability, predictability, accountability, and
in operational reality. Excluding industry and civil society, norms are implemented, responsibilities are upheld, and the likelihood of harm. The UN’’s Framework of
for example, risks fragmented responses, weaker policy resilience is built where it matters most. Responsible Industry Behaviour for AI in the Military
outcomes, and increased legal uncertainty. Domain seeks to create a practical and voluntary
baseline for responsible industry conduct. Its value
The move to action and recognition of lies in translating existing high--level principles
responsibilities in armed conflict into clearer expectations for companies and
governments. The framework is being developed
Advancing cyber stability requires moving toward through an inclusive process involving governments,
clarity on how international law applies in cyberspace, international institutions, civil society, academia, and
who interprets it, and how it is enforced. We are industry. In a field where technical choices can have
entering a more mature phase of cyber governance strategic consequences, this framework’’s operational
centered on attribution, evidence, due process, and guidance is essential to building trust, accountability,
meaningful accountability. and predictability.
A similar transition is underway in the governance
of AI in security and defense. The United Nations is Digital Emblem
shifting toward practical implementation and sustained
The Digital Emblem Project addresses a practical
engagement. The emerging Framework of Responsible
challenge in modern conflict: medical and
Industry Behaviour for AI in the Military Domain builds
humanitarian assets that are protected under
on this by offering voluntary, actionable guidance. It was
international humanitarian law are increasingly
developed through a multistakeholder process involving
dependent on digital systems, but those protections
governments, industry, and civil society. In parallel,
are not always visible in cyberspace. The Digital
initiatives such as the International Committee of the
Emblem aims to create an authenticated, interoperable
Red Cross’s (ICRC) Digital Emblem aim to enhance
marker that can help identify protected medical and
the protection of medical and humanitarian assets
humanitarian digital assets online, making existing
in cyberspace.
protections easier to recognize and respect during
cyber operations.

93
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
National resilience and geopolitical security
Open-source software security Improve adoption of updates and global Recommendations
alignment
Open-source software underpins critical
Governments should provide supply chain transparency Strengthen coordination and prioritization. 3. O rganizations advancing
infrastructure across governments, and standardized disclosures, and offer reliable update Governments should establish a National secure development:
economies, and essential services. mechanisms while addressing technical debt and Open Source Security Office (OSSO) to • Software Assurance Forum for Excellence
unsupported software. International alignment through coordinate policy, funding, and engagement. in Code (SAFECode), a global nonprofit
However, its security model has not kept pace with bodies such as the G7 should focus on common Today’’s fragmented approach limits visibility organization dedicated to improving
frontier AI. Advanced AI systems are increasingly capable principles, voluntary baselines, and interoperable tools. and accountability. An OSSO would enable software and hardware security through
of accelerating vulnerability discovery, analysis, and Meanwhile, incentive-driven public-private partnerships, national risk assessments, prioritize critical industry collaboration.
exploit development, potentially increasing the speed rather than mandates, will best preserve innovation and dependencies, coordinate internationally, • Open Worldwide Application Security
and scale at which threat actors can target widely used global collaboration. and guide secure adoption. Project (OWASP), a global open-source
software. Sustaining trust and resilience will require community focused on improving
a more active government role—not to control open Invest in security capacity and secure by software security through community--
source, but to strengthen the institutions, incentives, and design practices. led documentation, tools, and standards.
guardrails that support it.
Governments should accelerate adoption of
AI--enabled secure--by--design tools across the
Expanding existing frameworks will further
Enhance vulnerability discovery and ecosystem, including automated vulnerability
strengthen resilience. That includes software
response detection and stronger supply--chain
bills of material (SBOMs——a tool that
governance. Investments should support:
lists the component parts and software
Governments should complement community
1. Initiatives: For example, Open Source dependencies of a software package) and
efforts with dedicated defense centers leveraging
Security Foundation (OpenSSF), a global coordinated vulnerability disclosure (CVD––a
AI for continuous scanning, triage, and response.
project hosted by the Linux Foundation collaborative process used to safely report,
National cybersecurity bodies should partner with
that works to improve the security of fix, and reveal security flaws to the public).
Akrites, a Linux Foundation coalition that coordinates
open--source software, and Alpha--Omega,
confidential vulnerability remediation for open-source
a specialized initiative under it that finds
software upon which much critical infrastructure and fixes security flaws in critical code. A National Technology Fund could also
depends. Vulnerabilities must follow coordinated provide sustained support to maintainers of
disclosure processes, supported by funding and technical 2. S tandards and guidance: For example, the critical projects, reducing systemic risk while
assistance, to enable rapid remediation. NIST Cybersecurity Framework, Secure preserving independence.
Software Development Framework, and
related software supply--chain guidance
could help organizations to better
understand and improve how they
manage cybersecurity risks.

94
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
National resilience and geopolitical security
Operationalizing cyber Cyber outcomes are shaped by effective As a result, friction points emerge where technical “
response intersects with national decision
governance
resilience: Lessons from making. ARC findings point to several practical
Across digitally transforming economies, cyber outcomes readiness measures: At the Council of
the ARC initiative are increasingly shaped not by technical controls alone,
• Establish a shared incident response lifecycle and Europe, data from
but by how effectively governments coordinate during an
playbooks for high-impact scenarios.
Microsoft’s Advancing Regional incident. Response effectiveness depends on institutional the Microsoft Digital
• Create a streamlined “report once” mechanism for
Cybersecurity (ARC) initiative was readiness—clear roles, decision-making authorities, and incident reporting. Defense Report
coordination mechanisms—in addition to detection
launched to strengthen preparedness, • Link organizational SOCs to sector-level is used to inform
and prevention capabilities. As public sector systems
resilience, and coordination through become more interconnected, incidents can trigger coordination structures. the design and
public-private collaboration tailored to cascading effects across ministries and sectors, exposing • Define clear information-sharing protocols that enable
implementation of
gaps in real-world response that are not always visible in speed while protecting sensitive data.
governments’ operational needs.
policy frameworks. Regular tabletop exercises and after-action reviews are cybercrime capacity-
It responds to a growing reality: rapid digital ARC engagements highlight recurring structural essential to operationalize and continuously improve building programs
transformation—particularly across the Global South— challenges: unclear roles across agencies, fragmented these arrangements.
for law enforcement
has expanded both opportunity and exposure to cyber escalation pathways, and limited mechanisms for
risk. ARC focuses on building the institutional capabilities whole-of-government crisis management. These gaps ARC Mexico: Strengthening national incident worldwide.
required both to prevent incidents and to respond and are particularly visible in scenario-based exercises. response frameworks
recover effectively when they occur. The initiative was In these, coordination often breaks down at the Aisling Kelly,
first implemented through a partnership with Kenya’s intersection of technical response and policy decision Similar coordination challenges are shaping ARC Head of Cybercrime Division
National Computer and Cybercrime Coordination making—for example, around public communication, engagements in Latin America, where governments Council of Europe
Committee (NC4). It has expanded into Latin America system prioritization, or cross-sector resource are seeking to strengthen national incident response
through work with Mexico’s Digital Transformation and allocation. By addressing these governance challenges frameworks amid rapidly expanding digital services.
Telecommunications Agency (ATDT). alongside technical issues, governments can build In Mexico, ARC supported work with the ATDT, focused
on improving whole-of-government coordination
effective resilience.
in preparation for the FIFA World Cup. This brought
together technical, civilian, and regulatory stakeholders
ARC Kenya: Uncovering the value of
to test crisis response workflows and identify institutional
scenario-based planning
dependencies that could affect mitigation and recovery
during major cyber incidents. This approach is now being
The ARC partnership with NC4 illustrates how
scaled regionally.
scenario-based planning can surface operational
dependencies that are difficult to identify through
policy alone. Kenya has strong foundations, including a
maturing regulatory framework for critical information
infrastructure. However, these elements are not yet fully
integrated into a unified national operating model.

95
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
National resilience and geopolitical security
Supporting the future of the Evolving the CVE ecosystem Recommendations for policymakers
CVE Program Since the CVE Program was created, the program’s To ensure the CVE Program remains a trusted
governance and capabilities haven’t significantly evolved. and effective foundation for global vulnerability
As discovery capacity accelerates via frontier AI model management, policymakers and ecosystem leaders
The Common Vulnerabilities and
capabilities, the program needs to evolve its throughput, should pursue a targeted set of reforms focused on
Exposures (CVE) Program is a critical piece data quality, and governance. sustainability, governance, technical modernization, and
of shared infrastructure. It provides unique international alignment.
Mounting structural, technical, and governance
identification numbers for specific software challenges threaten the CVE Program’s long-term
or hardware security flaws. effectiveness. Governance and funding models have Recognize the CVE Program as essential shared
struggled to keep pace with the program’s evolution, infrastructure and resource it sustainably. This provides
This powers everything from incident response and raising concerns about neutrality, continuity, and a starting point for ensuring its long--term stability by
patch management to risk scoring, compliance reporting, international participation when oversight or resourcing supporting more predictable, appropriately scaled
and security research, and is a critical piece of shared is uncertain. At the same time, the volume and velocity funding models and continuity planning.
infrastructure. It provides unique identification numbers of vulnerability discovery have increased dramatically,
for specific software or hardware security flaws. exposing scalability limits in CVE Numbering Authority
Support innovation through continued investment
The common reference numbers enable stakeholders (CNA) workflows and manual processes, and contributing
in APIs, tooling, and automation. As vulnerability
to consistently identify and manage vulnerabilities once to delays and inconsistencies in published records.
discovery continues to grow, the CVE Program will
they are discovered. As the volume of vulnerabilities
benefit from investment in modern technical capabilities.
expands, the CVE ecosystem must scale to be sustainable
Scalable APIs, structured and machine-readable data,
and trusted.
and greater use of automation can improve efficiency,
As software systems, supply chains, and discovery consistency, and timeliness. Stakeholders should direct
techniques continue to evolve, maintaining the funding and technical support toward modernizing
effectiveness of that foundation will require careful CVE infrastructure, especially APIs, CNA tooling, and
attention to scalability, data quality, governance, and automation capabilities.
long-term sustainability. Strengthening the CVE Program
means ensuring that its operating model continues to
Leverage public--private partnerships and
meet the needs of a larger, more complex, and more
international participation to advance shared goals.
interconnected environment. This can support faster
Strengthening the CVE Program presents an opportunity
coordination, better prioritization, and more effective
for closer collaboration between governments, industry,
risk reduction worldwide.
researchers, and the open-source community that
can help accelerate improvements in infrastructure,
tooling, and ecosystem support, translate shared policy
objectives into scalable outcomes, and contribute to CVE
modernization efforts.

96
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
National resilience and geopolitical security
Subsea cables and global Recommendations
Governments today can take the following steps to
connectivity: Building resilience
support subsea cable security:
through a comprehensive
Promote redundancy as the most critical component
approach to security
of resilience by supporting regulatory frameworks that
make it easier to build and operate subsea cables—
Subsea fiber optic cables are the critical
enabling multiple routes between key regions and
backbone of the global communications ensuring that data can continue to flow even if one
and internet infrastructure, transporting or more cable routes are temporarily compromised.
over 99% of intercontinental data traffic.
Encourage geographic diversity of cable landings
They underpin intergovernmental communications, to reduce concentration risk and avoid single points
financial transactions, and defense communications, of failure.
making them essential to national and international
security. However, this critical infrastructure is physically
Prepare for large-scale disruptive events through
vulnerable. Many cables traverse vast oceanic spans that
public-private coordination, advance planning, tabletop
include volcanic zones, tectonic fault lines, and polar seas.
readiness exercises, and prioritization for restoration
Natural disasters like earthquakes or undersea landslides,
of service.
fishing activity and ship anchors, and deliberate sabotage
or tampering can all damage these cables.
Reform cabotage rules and other maritime regulations
Most subsea cables are owned and operated by private
to enable efficient use of specialized repair ships and
consortia. As a result, primary responsibility for securing
faster restoration following cable damage.
these systems rests with private cable operators, who
must invest in robust physical, logical, and supply-
chain security measures. At the same time, there is an Support data-driven planning for future repair
important supporting role for governments to play in capacity, including assessments of repair ship
enhancing cable resilience and security. This is consistent retirement, anticipated demand, and repair ship
with historic practice: critical infrastructure has long been market stability considerations.
protected by a combination of private and public actors.
Leverage national security and defense capabilities,
where appropriate, to support protection and repair
activities, including the use of military assets to assist
or escort commercial repair operations.

|     |     |     | Introduction | AI  | The threat landscape |     | Cybercrime | Resilience | Appendix |
| --- | --- | --- | ------------ | --- | -------------------- | --- | ---------- | ---------- | -------- |
    txen eht rof gniraperP    noitisnart ytiruces
Quantum-safe readiness     Quantum safety is a migration challenge,    • Plan remediation based on business criticality,
6202 tropeR esnefeD latigiD tfosorciM exposure, and operational feasibility, with particular
not a single replacement project
| for organizations: Start  |     |                                                            |     |     |     |                                                      |     |     |     |
| ------------------------- | --- | ---------------------------------------------------------- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
|                           |     |                                                            |     |     |     | focus on identity systems, signing services, update  |     |     |     |
|                           |     | In the future, sufficiently capable quantum computers are  |     |     |     |   mechanisms, and other high-impact trust pathways.  |     |     |     |
preparing today
|                                             |     | expected to break widely deployed algorithms such as          |     |     |     | • Implement the required updates in a controlled way.    |     |     |     |
| ------------------------------------------- | --- | ------------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
|                                             |     | RSA and elliptic-curve cryptography (ECC), threatening        |     |     |     |                                                          |     |     |     |
| Quantum computing threatens                 |     | web security, software integrity, and identity verification.  |     |     |     |                                                          |     |     |     |
|                                             |     |                                                               |     |     |     | This work also pays off immediately                      |     |     |     |
|                                             |     | Moving to PQC will require a multi-year transformation        |     |     |     |                                                          |     |     |     |
| the cryptography that protects an           |     |                                                               |     |     |     | for AI security                                          |     |     |     |
|                                             |     | across protocols, certificates, core libraries, and the       |     |     |     |                                                          |     |     |     |
| organization’s data, identities, software,  |     |                                                               |     |     |     |                                                          |     |     |     |
|                                             |     | systems that depend on them. Done well, it is also            |     |     |     | Many weaknesses that attackers exploit against models    |     |     |     |
and digital services.    an opportunity to reduce exposure from legacy    and agents are rooted in identity controls, exposed
|                                                          |     | cryptography, standardize on modern primitives, and         |     |     |     | secrets, and brittle trust chains. Closing those gaps    |     |     |     |
| -------------------------------------------------------- | --- | ----------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
| That risk is not limited to a future point when quantum  |     |   build crypto-agility so future cryptographic changes are  |     |     |     |                                                          |     |     |     |
|                                                          |     |                                                             |     |     |     | helps prevent credential theft and token replay, limits  |     |     |     |
| computers can break today’s public-key algorithms:       |     |                                                             |     |     |     |                                                          |     |     |     |
|                                                          |     | less disruptive.                                            |     |     |     | misuse of service principals and API keys that grant     |     |     |     |
threat actors can store encrypted information now for    access to AI endpoints and tools, and hardens integrity
later decryption, a capability known as harvest now,    Organizations can build a cryptographic    paths for signing, updates, model artifacts, and plugins.
decrypt later (HNDL). That means sensitive data captured    It also reduces the impact of prompt injection-to-action
inventory in four steps
| today may still need protection years from now.    |     |                                                           |     |     |     |                                                             |     |     |     |
| -------------------------------------------------- | --- | --------------------------------------------------------- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- |
|                                                    |     |                                                           |     |     |     | scenarios by tightening least-privilege access, key scope,  |     |     |     |
|                                                    |     | B  ecoming quantum-safe is a large-scale software and     |     |     |     | and approval boundaries for high-impact actions.            |     |     |     |
| The transition to post-quantum cryptography (PQC)  |     |                                                           |     |     |     |                                                             |     |     |     |
|                                                    |     | infrastructure modernization effort that will eventually  |     |     |     |                                                             |     |     |     |
requires organizations to modernize the cryptographic    By understanding which cryptographic assets protect
|     |     | touch nearly every device, service, application, and  |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
foundations they depend on. Sensitive data, identity    the organization’s most important trust pathways,
|                                                         |     | dependency in an organization. The journey starts         |     |     |     |                                                              |     |     |     |
| ------------------------------------------------------- | --- | --------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- |
| systems, signing infrastructure, software updates, and  |     |                                                           |     |     |     |                                                              |     |     |     |
|                                                         |     |                                                           |     |     |     | security teams can use that visibility to drive prioritized  |     |     |     |
| service-to-service trust pathways all depend on these   |     |   with discovering where cryptography is used, how it is  |     |     |     |                                                              |     |     |     |
|                                                         |     |                                                           |     |     |     | modernization. Effective inventories go beyond a             |     |     |     |
|                                                         |     | deployed, who owns it, and which business processes       |     |     |     |                                                              |     |     |     |
cryptographic foundations. Organizations need to    spreadsheet. They capture certificates and their chains,
|     |     | depend on it. Certificates embedded in appliances, custom  |     |     |     |     |     |     |     |
| --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
discover, modernize, and make them agile before the    key types and sizes, protocols in use, cryptographic
|     |     | implementations in legacy applications, hard-coded keys,  |     |     |     |     |     |     |     |
| --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
transition becomes urgent. PQC standards and some    libraries and versions, and where keys live. They also
|                                                       |     | outdated libraries, and undocumented protocol choices       |     |     |     |                                                          |     |     |     |
| ----------------------------------------------------- | --- | ----------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
| implementations are already available, while support  |     |                                                             |     |     |     |                                                          |     |     |     |
|                                                       |     |                                                             |     |     |     | track ownership, change windows, and dependencies so     |     |     |     |
| varies across products and vendors.                   |     | are common sources of hidden risk. Without an accurate,     |     |     |     |                                                          |     |     |     |
|                                                       |     |                                                             |     |     |     | teams can coordinate upgrades. As environments evolve,   |     |     |     |
|                                                       |     | continuously updated cryptographic inventory, PQC           |     |     |     |                                                          |     |     |     |
|                                                       |     |                                                             |     |     |     | inventories must stay “living” through automation and    |     |     |     |
| For practical guidance on accelerating quantum-safe   |     |   migration plans quickly become guesswork.                 |     |     |     |                                                          |     |     |     |
|                                                       |     |                                                             |     |     |     | continuous scanning, enabling security teams to measure  |     |     |     |
| readiness, see the Quantum Safe Program resources     |     |                                                             |     |     |     |                                                          |     |     |     |
|                                                       |     | A practical quantum-safe plan usually follows four stages:  |     |     |     |   progress, validate policy, and prevent regression.     |     |     |     |
(https://aka.ms/QSP/accelerate and https://aka.ms/QSP/
| inventory).  |     | • Discover where cryptography is used across your        |     |     |     |     |     |     |     |
| ------------ | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|              |     | enterprise, including the systems, services, protocols,  |     |     |     |     |     |     |     |
certificates, keys, and secrets that underpin trust.
|     |     | • Evaluate which assets rely on quantum-vulnerable    |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | algorithms, which data has long confidentiality       |     |     |     |     |     |     |     |
|     |     | requirements, and which vendors or platforms have     |     |     |     |     |     |     |     |
upgrade paths available.
97

98
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Preparing for the next security transition
Quantum-safe readiness for organizations: Securing the quantum future Recommendations for governments
Start preparing today (continued)
Governments play a critical role in enabling a quantum--
through policy
safe future through strong collaboration with industry
Preparing for 2029 and beyond:
and effective policies. To accelerate readiness, we
From readiness to action Governments are moving from recognizing
recommend governments take the following actions:
the risk posed by PQC to accelerating the
The next few years will determine whether the transition
to PQC is orderly or disruptive. The remainder of this transition to quantum-safe cryptography.
Establish quantum safety as a national cybersecurity
decade is likely to be a critical readiness period as
priority. Position quantum--safe cryptography as
quantum-safe capabilities become broadly available As of June 2026, more than 25 governments have
a strategic imperative and embed it into national
and organizations begin planning large-scale adoption. issued PQC guidance or mandates. While these actions
cybersecurity frameworks.
The priority now is to convert readiness into execution: demonstrate that PQC has become a policy priority
modernize infrastructure by adopting current operating across regions, the challenge now is translating this
systems with built-in PQC capabilities, complete momentum into implementation at scale. Align quantum-safe strategies across jurisdictions,
cryptographic inventories, assign ownership for critical including by adopting international standards.
Recent policy developments reflect growing
systems, test hybrid PQC, and engage suppliers early Harmonize public policies, standards, and transition
international alignment around the need for quantum-
so adoption can accelerate as PQC standards and timelines. The G7 should lead by expanding its financial
safe migration. This includes planning to migrate high-
products mature. sector post--quantum cryptography workstream to
value government assets and high-impact systems to
align G7 members’ broader quantum-safe strategies.
PQC-based cryptography and mitigate as much quantum
Global standards development will help overcome
risk as feasible, securing critical infrastructure and
fragmented, region-specific approaches that hinder
pursuing phased approaches that align with international
interoperability, innovation, and security.
standards. This momentum is also evident beyond G7
economies, with countries such as India, Singapore,
and Malaysia developing guidelines to help both the Set early and progressive timelines. For instance, US
public and private sector. policy for national security systems mandates starting in
2027 that products should not be procured if they are not
upgradeable to become quantum-safe by 2030.
Lead by example with transparent transition plans.
Publish and regularly update government transition
roadmaps——including timelines, milestones, and
budgets——to foster knowledge sharing and best practices.
Raise awareness and build workforce capacity.
Educate the public and critical infrastructure sectors on
quantum risks and readiness. Invest in skilling programs
to equip the workforce for a quantum--safe transition.

| Introduction | AI  | The threat landscape | Cybercrime | Resilience | AAppppeennddiixx  |
| ------------ | --- | -------------------- | ---------- | ---------- | ----------------- |
6202 tropeR esnefeD latigiD tfosorciM Appendix  Glossary  100
|     |     | References  |     |     | 102 |
| --- | --- | ----------- | --- | --- | --- |
99

|     |     |     | Introduction |     | AI  | The threat landscape |     | Cybercrime | Resilience | Appendix |
| --- | --- | --- | ------------ | --- | --- | -------------------- | --- | ---------- | ---------- | -------- |
 yrassolG
Adversary-in-the-middle (AitM) attack    Disinformation is deliberate, often    Node Package Manager (npm) A package      Quishing Phishing that uses malicious QR
6202 tropeR esnefeD latigiD tfosorciM Occurs when an attacker reroutes    orchestrated, attempts to confuse or    manager for JavaScript and Node.js that    codes to direct victims to fraudulent or
communication between two users through    manipulate people through delivering    allows developers to install, manage, and    harmful content.
the attacker’s computer without the    dishonest information to them.  share software packages. Because npm
|     |     |     |     |     |     |     |     | Ransomware A type of cybersecurity attack  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- |
knowledge of the two communicating users.    packages are widely used across the
Distributed denial of service (DDoS)    that destroys or encrypts files and folders,
Each user in the communication unknowingly    software supply chain, attackers may
attack An attack that prevents or impairs    preventing the owner of the effected device
sends traffic to and receives traffic from    attempt to distribute malicious code
the authorized use of information system    from accessing their data. The cybercriminal
the attacker, all the while thinking they are    through compromised, fraudulent, or
resources or services. A distributed denial of    can then extort money from the business
| communicating only with the intended user.  |     |     |     |     | malicious packages.  |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
service (DDoS) is a type of attack that uses    owner in exchange for a key to unlock
Attack surface An information system’s    multiple networked machines to overwhelm    NT LAN Manager (NTLM) A legacy    the encrypted data. But, even when paid,
characteristics that permit an adversary to    a host connected to the internet, temporarily    Microsoft authentication protocol used to    cybercriminals may not provide the key to
probe, attack, or maintain presence in the    or permanently disrupting service or    authenticate users and devices on a network.    return access to the business owner.
information system.  preventing access.  Because NTLM relies on older authentication
|     |     |     |     |     |                                      |     |     | Ransomware-as-a-service (RaaS) An  |     |     |
| --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | ---------------------------------- | --- | --- |
|     |     |     |     |     | mechanisms, it is commonly targeted  |     |     |                                    |     |     |
Authentication The process of verifying the      Exfiltration The unauthorized transfer of    arrangement between an operator, who
|     |     |     |     |     | by attackers seeking to steal credentials,  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
identity of an entity (user, process, or device).  information from an information system.  develops and maintains the tools to power
|                                                |     |                                              |     |     | conduct relay attacks, or move laterally within  |     |     |                                               |     |     |
| ---------------------------------------------- | --- | -------------------------------------------- | --- | --- | ------------------------------------------------ | --- | --- | --------------------------------------------- | --- | --- |
|                                                |     |                                              |     |     |                                                  |     |     | extortion operations, and an affiliate, who   |     |     |
| Critical infrastructure The systems and        |     |   Misinformation is misleading information,  |     |     |   compromised environments.                      |     |     |                                               |     |     |
|                                                |     |                                              |     |     |                                                  |     |     | deploys the ransomware payload. When the      |     |     |
| assets, whether physical or virtual, so vital  |     |   either created or disseminated without     |     |     |                                                  |     |     |                                               |     |     |
|                                                |     |                                              |     |     | Password spray High-volume attempts using        |     |     |   affiliate conducts a successful ransomware  |     |     |
| to society that the incapacity or destruction  |     |   manipulative or malicious intent.          |     |     |                                                  |     |     |                                               |     |     |
|                                                |     |                                              |     |     | a large number of common passwords to            |     |     |   and extortion attack, both parties profit.  |     |     |
| of such may have a debilitating impact on      |     |                                              |     |     |                                                  |     |     |                                               |     |     |
|                                                |     | Multifactor authentication (MFA) Refers      |     |     |   compromise sourced account information to      |     |     |                                               |     |     |
the security, economy, public health or    Remote Desktop Protocol (RDP) A protocol
|     |     | to an additional security layer beyond just  |     |     |   authenticate and gain access to a network,  |     |     |     |     |     |
| --- | --- | -------------------------------------------- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
safety, environment, or any combination of    for remotely connecting to computers
|               |     | username and password. One way it is     |     |     | often leveraging big data algorithms and     |     |       |                   |     |     |
| ------------- | --- | ---------------------------------------- | --- | --- | -------------------------------------------- | --- | ----- | ----------------- | --- | --- |
| these areas.  |     |                                          |     |     |                                              |     |       | running Windows.  |     |     |
|               |     | described is the user name and password  |     |     |   extensive automation for rapid execution.  |     |       |                   |     |     |
Cyber espionage The unethical act of      shows who you are based on something    Resilience The ability to adapt to changing
|     |     |     |     |     | Passwordless authentication is a security  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
violating the privacy and security of an    you know, and MFA shows who you are by    conditions and prepare for, withstand, and
|     |     |     |     |     | method that allows users to verify an identity  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
organization in order to leak data or disclose    something you have. The most common    rapidly recover from disruption.
|                                             |     |                                                 |     |     | without using a password.  |     |     |                                               |     |     |
| ------------------------------------------- | --- | ----------------------------------------------- | --- | --- | -------------------------- | --- | --- | --------------------------------------------- | --- | --- |
| internal/private/confidential information.  |     |   example of MFA is the code you get in a text  |     |     |                            |     |     |                                               |     |     |
|                                             |     |                                                 |     |     |                            |     |     | Security posture Refers to an organization’s  |     |     |
Cyber espionage can be performed by    on your phone when you are logging into    Phishing A digital form of social engineering
|     |     |     |     |     |     |     |     | overall cybersecurity strength and how well it  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
individuals, organizations, or governments    sites like your bank or GitHub.  to deceive individuals into providing
can predict, prevent, and respond to ever-
| for the direct purpose of causing harm to    |     |                                            |     |     | sensitive information.                        |     |     |                          |     |     |
| -------------------------------------------- | --- | ------------------------------------------ | --- | --- | --------------------------------------------- | --- | --- | ------------------------ | --- | --- |
|                                              |     | Nation-state actor/Nation-state            |     |     |                                               |     |     | changing cyber threats.  |     |     |
| the violated entity to benefit individuals,  |     |                                            |     |     |                                               |     |     |                          |     |     |
|                                              |     | threat actor A cyber threat actor that is  |     |     | Phishing kit A collection of tools assembled  |     |     |                          |     |     |
organizations or governments.  Spear phishing is a targeted phishing attack
|     |     | directed, sponsored, or supported by a        |     |     | to make it easier for individuals with little or  |     |     |                                                |     |     |
| --- | --- | --------------------------------------------- | --- | --- | ------------------------------------------------- | --- | --- | ---------------------------------------------- | --- | --- |
|     |     |                                               |     |     |                                                   |     |     | that involves highly customized lure content.  |     |     |
|     |     | national government and conducts cyber        |     |     |   no knowledge of phishing practices to launch    |     |     |                                                |     |     |
|     |     |                                               |     |     |                                                   |     |     | Attackers typically do reconnaissance          |     |     |
|     |     | operations to advance that government’s       |     |     |   a phishing exploit.                             |     |     |                                                |     |     |
|     |     |                                               |     |     |                                                   |     |     | work by surveying social media and other       |     |     |
|     |     | strategic, political, military, economic, or  |     |     |                                                   |     |     |                                                |     |     |
|     |     |                                               |     |     |                                                   |     |     | information sources about their intended       |     |     |
intelligence objectives.
|     |     |     |     |     |     |     |     | target. Spear phishing may involve tricking  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
|     |     |     |     |     |     |     |     | targets into signing in to fake sites and    |     |     |
|     |     |     |     |     |     |     |     | divulging credentials.                       |     |     |
100

101
6202
tropeR
esnefeD
latigiD
tfosorciM
Introduction AI The threat landscape Cybercrime Resilience Appendix
Glossary (continued)
Spoofing Faking the sending address of a
transmission to gain illegal (unauthorized)
entry into a secure system. Website spoofing
involves creating a duplicate version of a
website that appears to be the original.
Hackers use legitimate logos, fonts, colors,
and functionality to make the spoofed
site look realistic. Even the URL can
appear genuine.
Token replay attacks The use of tokens
that were issued to a legitimate user by an
attacker that has possession of said tokens.
Tokens are commonly obtained via malware,
for example by exfiltrating the cookies from
the user’s browser, or through advanced
phishing methods.
Transmission control protocol (TCP) attacks
Cyberattacks that exploit TCP network
communications to disrupt connections,
intercept or manipulate traffic, or deny access
to services.
Vishing A form of phishing that uses phone
or voice communications to deceive people
into revealing sensitive information or taking
an action.
Zero-day vulnerability A previously unknown
or unaddressed software vulnerability for
which a security update or comprehensive
mitigation is not yet available.
Zero Trust A security model based on
explicitly verifying access requests, using
least-privilege access, and continuously
evaluating risk while assuming that
compromise is possible.

|     |     |     |     |     |     | Introduction |     |     | AI  | The threat landscape |     |     | Cybercrime | Resilience | Appendix |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | -------------------- | --- | --- | ---------- | ---------- | -------- |
 secnerefeR
Section 1: AI  13.    Efforts to share best practices on    24. CDT Europe Report: EU Export Controls      36. Common Vulnerabilities and Exposures
6202 tropeR esnefeD latigiD tfosorciM AI measurement    (CVE) Program
|                                           |     |     |     |     |     |     |     |     | Are Failing to Address the Spread  |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
| 1.    LLMs used inside malware | CERT-UA  |     |     |     |     |     |     |     |     |                                    |     |     |     |     |     |     |
14.    International Network for Advanced AI    of Spyware - Center for Democracy    37.    CVE Numbering Authority (CNA)
| |vCommunity Response Team - Ukraine |  |     |     |     |                                       |     |     |     |     |                                          |     |     |     |                                             |     |      |
| -------------------------------------- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ------------------------------------------- | --- | ---- |
|                                        |     |     |     |                                       |     |     |     |     | and Technology                           |     |     |     |                                             |     |      |
| JUL 2025                               |     |     |     | Measurement, Evaluation, and Science  |     |     |     |     |                                          |     |     |     |                                             |     |      |
|                                        |     |     |     |                                       |     |     |     |     |                                          |     |     |     | 38. Accelerating the quantum-safe timeline  |     |      |
|                                        |     |     |     |                                       |     |     |     |     | 25. Mythical Beasts Investigating the    |     |     |     |                                             |     |      |
2.    AI-powered malware hit 2,180 GitHub    15.    Frontier Model Forum    | Microsoft Security Blog | JUN 2026
|     |     |     |     |     |     |     |     |     | Role of Intermediaries | Atlantic Council  |     |     |     |      |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | ---- | --- | --- |
accounts in “s1ngularity” attack | Bleeping    16.    Advancing AI evaluation with the Center    | MAR 2026    39. Building your cryptographic inventory:
Computer | SEP 2025    for AI Standards (US) and Innovation and    A customer strategy for cryptographic
the AI Security Institute (UK)  posture management | Microsoft Security
| 3.    Disrupting the first reported AI- |     |     |     |     |     |     |     |     | Section 4: Resilience  |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
Blog | APR 2026
| orchestrated cyber espionage campaign |  |     |     |     | 17.    Malicious AI Assistant Extensions Harvest  |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Anthropic | NOV 2025    LLM Chat Histories | Microsoft Security    26. Media Integrity and Authentication:      40. Implementation of Quantum Safe
|     |     |     |     |     |     |     |     |     | Status, Directions, and Futures | arXiv  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
4.    Our evaluation of OpenAI’s GPT-5.5    Blog | MAR 2026    Ecosystem in India - Report of the Task
|     |     |     |     |     |     |     |     |     | Computer Science > Artificial Intelligence  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
cyber capabilities | AI Security Institute |    Force PDF | Department of Science &
|     |     |     |     |     |     |     |     |     | | FEB 2026  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Section 2: Threat Landscape  Technology
APR 2026
|                                               |     |     |     |                                           |     |     |     |     | 27.    Media Authenticity Methods in Practice:  |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 5.    The Hugging Face incident and the road  |     |     |     | 18.    Mitigating NTLM Relay Attacks by   |     |     |     |     |                                                 |     |     |     |     |     |     |
|                                               |     |     |     |                                           |     |     |     |     | Capabilities, Limitations, and Directions |     |     |     |     |     |     |     |
| ahead | Open AI | AUG 2026                    |     |     |     | Default | Microsoft MSRC | DEC 2024       |     |     |     |     |                                                 |     |     |     |     |     |     |
|                                               |     |     |     |                                           |     |     |     |     | Microsoft Research Blog | FEB 2026              |     |     |     |     |     |     |
| 6.    Measuring AI Agents’ Progress on        |     |     |     |                                           |     |     |     |     |                                                 |     |     |     |     |     |     |
|                                               |     |     |     |                                           |     |     |     |     | 28. A new study explores how AI shapes          |     |     |     |     |     |     |
| Multi-Step Cyber Attack Scenarios | arXiv     |     |     |     | Section 3: Cybercrime                     |     |     |     |     |                                                 |     |     |     |     |     |     |
|                                               |     |     |     |                                           |     |     |     |     | what you can trust online | Microsoft           |     |     |     |     |     |     |
| Computer Science > Artificial Intelligence    |     |     |     |                                           |     |     |     |     |                                                 |     |     |     |     |     |     |
|                                               |     |     |     |                                           |     |     |     |     | Signal | FEB 2026                               |     |     |     |     |     |     |
|                                               |     |     |     | 19.    NIST 800-63B-4 requirements |NIST  |     |     |     |     |                                                 |     |     |     |     |     |     |
| MAR 2026
|                                           |     |     |     | | National Institute of Standards and    |     |     |     |     | 29. Advancing digital content transparency    |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 7.    JADEPUFFER: Agentic ransomware for  |     |     |     | Technology |SP 800-63B                   |     |     |     |     |                                               |     |     |     |     |     |     |
|                                           |     |     |     |                                          |     |     |     |     | and authenticity | Coaliltion for Content     |     |     |     |     |     |     |
| automated database extortion | sysdig |   |     |     |     |                                          |     |     |     |     |                                               |     |     |     |     |     |     |
|                                           |     |     |     | 20. Defending the gates: How a global    |     |     |     |     | Provenance and Authenticity                   |     |     |     |     |     |     |
JUL 2026
|                                              |     |     |     | coalition disrupted Tycoon 2FA, a major      |     |     |     |     |                                              |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                              |     |     |     |                                              |     |     |     |     | 30.   Unify now or pay later: New research   |     |     |     |     |     |     |
| 8.    Anatomy of a Frontier Lab Agent        |     |     |     | driver of initial access and large-scale     |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     |                                              |     |     |     |     | exposes the operational cost of a            |     |     |     |     |     |     |
| Intrusion: A Technical Timeline of the July  |     |     |     |                                              |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     | online impersonation | Microsoft on the      |     |     |     |     |   fragmented SOC | Microsoft Security        |     |     |     |     |     |     |
| 2026 Incident | Hugging Face| JUL 2026       |     |     |     |                                              |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     | Issues | MAR 2026                            |     |     |     |     | Blog | FEB 2026                              |     |     |     |     |     |     |
| 9.    Can AI Attack the Cloud? Lessons From  |     |     |     |                                              |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     | 21.    CISA et al., Unsophisticated Cyber    |     |     |     |     | 31.    NIST AI Risk Management Framework     |     |     |     |     |     |     |
| Building an Autonomous Cloud Offensive       |     |     |     | Actor(s) Targeting Operational               |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     |                                              |     |     |     |     | 32. EU AI Act                                |     |     |     |     |     |     |
| Multi-Agent System | Unit 42 Threat          |     |     |     | Technology, May 6, 2025                      |     |     |     |     |                                              |     |     |     |     |     |     |
| Research | APR 2026                          |     |     |     |                                              |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     | 22. Pro-Russia Hacktivists Conduct           |     |     |     |     | 33. International Community of the Red       |     |     |     |     |     |     |
| 10.    AI Agents Enable Adaptive Computer    |     |     |     |                                              |     |     |     |     | Cross’s (ICRC) Digital Emblem                |     |     |     |     |     |     |
|                                              |     |     |     | Opportunistic Attacks Against US and         |     |     |     |     |                                              |     |     |     |     |     |     |
| Worms | arXiv Computer Science >             |     |     |     |                                              |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     | Global Critical Infrastructure  | America’s  |     |     |     |     |   34. Akrites                                |     |     |     |     |     |     |
| Artificial Intelligence | JUN 2026           |     |     |     | Cyber Defense Agency | DEC 2025              |     |     |     |     |                                              |     |     |     |     |     |     |
|                                              |     |     |     |                                              |     |     |     |     | 35. Microsoft announces ARC Initiative to    |     |     |     |     |     |     |
11.    NadMesh Botnet Analysis: A Product- 23. Setting spyware standards      strengthen cybersecurity in Kenya |
| Grade Threat for the AI Service Era | Xlab  |     |     |     | after the Pegasus scandal PDF |  |     |     |     |     | Microsoft On the Issues | MAY 2025  |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
| | JUL 2026                                  |     |     |     | European Parliament              |     |     |     |     |                                     |     |     |     |     |     |     |
| 12.    Frontier Governance Framework        |     |     |     |                                  |     |     |     |     |                                     |     |     |     |     |     |     |
102

2026 Microsoft
Digital Defense Report
For more news on cybersecurity, visit:
https://microsoft.com/corporate--responsibility/cybersecurity
For more report insights, visit:
https://microsoft.com/mddr
For more news on cybersecurity policy,
follow us on LinkedIn:
https://aka.ms/MOILinkedin
For insights and trends for security leaders, visit:
https://www.microsoft.com/security/security--insider
A Microsoft Threat Intelligence report
October 2026

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-10", "model": "gemini-3.8-flash"} -->
