# Threat Report H1 2026
Threat Intelligence, January to June 2026  
Organization: Gen  
Report Title: Threat-Report  
Year: 2026

## Table of Contents
- [Foreword](#foreword)
- [Threat Landscape Highlights](#threat-landscape-highlights)
  - [Security Threats & Scams](#security-threats--scams)
- [Telemetry Deep Dive](#telemetry-deep-dive)
- [AI-Driven Attacks & Defenses](#ai-driven-attacks--defenses)
- [Privacy](#privacy)
- [Trust & Identity](#trust--identity)
- [Financial Wellness](#financial-wellness)
- [In Closing](#in-closing)
- [Acknowledgments and Credits](#acknowledgments-and-credits)
- [About Gen](#about-gen)

Attackers spent the first half of 2026 abusing trust that already exists: hotel workflows, messaging sessions, browser data, developer tools, AI agents, payment habits and identity signals.

**20.3M**  
Tech support scam attacks blocked  
_Up 61.6% vs H2 2025_

**1.9B+**  
Tracking attempts blocked  
_310.8M average per month_

**3.3M**  
Breach notification alerts sent  
_Up 628.1% vs H2 2025_

**1M**  
Web Skimming  
_Blocked attacks in H1 2026, up 212% vs H2 2025._

**18,618**  
Breach events  
_Up 94.5% vs H2 2025_

**1.5M**  
Depository activity alerts  
_Up 734% vs H2 2025_

---

## Foreword

### The trust layer became the battlefield

The strongest pattern in the first half of 2026 was the way different threats converged around trust. Scams, account takeovers, malicious packages and AI agents all moved closer to the systems, workflows and permissions people already rely on.

A hotel scam became convincing because it knew real reservation details, an attack we dubbed Reservation Hijack Scams. A WhatsApp account takeover worked by turning the attacker’s browser into an approved linked device. A tech support scam looked more credible because it appeared on familiar infrastructure and used real-angling system errors. A malicious package reached developers through normal install and update paths. An AI agent became risky not because it could write fluent text, but because it could act with permissions the user had already granted.

That is the common thread running through this report: attackers are moving closer to the trusted parts of digital life. They are not only sending malicious links or dropping malware. They are abusing context, sessions, workflows, brands, update systems, advertising platforms and delegated authority. The attack often succeeds before the victim reaches the obvious danger point, because the surrounding situation already feels legitimate, and in many cases, the victim has actually given their attacker approval.

The numbers show the scale. From January to June, scams accounted for almost 46% of threat detections, making them the leading malware type in Gen telemetry. Malvertising was also a major driver, representing almost 30% of detections. Within that broader scam landscape, tech support scam detections reached 20.3 million blocked attacks, while e-shop scams reached 114.2 million. Imposter scams rose 387%, with government impersonation driving most of that activity. Gen’s Scam Ad Machine research found that scam-related ads made up nearly 1 in 3 ads analyzed from Meta’s EU and UK ad dataset, generating more than 304 million impressions in less than a month. Financial abuse also appeared closer to the point of payment: Gen blocked 996.3K web skimming attacks in H1 2026, up 212% from H2 2025, showing how attackers continued to target checkout flows where users already expect to enter payment details.

On the privacy side, Gen blocked an average of 310.8 million tracking attempts per month, around 1.9 billion across the half-year. On the identity side, Norton and LifeLock users received more than 3.3 million breach notification alerts with identified source of the breach, up 628.1%, and credit inquiry issues-resulted in almost half a million alerts per month; a sign that exposed personal data was being tested or used in financial contexts.

AI added another layer to this picture. The risk is no longer limited to fake images, synthetic voices or better phishing text. Agentic systems can browse, install, read, write, connect and execute. That makes them useful, but it also means security has to move into the places where agents act: before tool use, before package installation, before memory access, before network connections and before a user is asked to trust an autonomous system.

That is the gap protection has to close. People cannot inspect every booking workflow, validate every advertisement, reverse-engineer every software component, audit every linked device or understand every AI agent decision. Protection has to sit closer to the moment trust is granted, transferred and abused.

**Luis Corrons**  
Security Evangelist (aka Threat Whisperer)

#### ABOUT THIS REPORT

This is our first Gen half-year Threat Report. Until now, we published quarterly reports that also carried featured stories from Gen Threat Labs. That research is not going away. We are moving those deeper stories to our blog, where we can publish them as soon as they are ready and get the information to people faster. This report now has a different job: to step back, connect the signals across the first half of the year and show where the threat landscape is moving.

---

## Threat Landscape Highlights

### Five areas, one underlying pattern

H1 2026 showed attackers abusing the same systems people rely on to make digital life work: communication platforms, browsers, cloud services, developer tools, AI assistants, financial checks and identity workflows.

## Security Threats & Scams

### Malicious activity moved into trusted context

In H1 2026, many of the most effective attacks did not look like attacks at first. They arrived through hotel conversations, support pages, booking processes, business inboxes, cloud-hosted pages, developer tools and social media ads. The mechanism varied, but the logic was consistent: attackers placed malicious activity inside contexts that users, platforms and security systems already trust.

### Tech support scams moved through familiar infrastructure

Tech support scam detections reached 20.3 million blocked attacks in H1 2026, up 61.6% half-over-half. Part of this increase still reflects broader detection coverage, after Gen introduced a dedicated URL filtering capability for this type of content, but coverage was not the whole story. Gen also observed strong tech support scam campaigns using content hosted on ondigitalocean[.]app domains, which helped the scams appear on legitimate-looking cloud infrastructure. The United States remained the largest single target, with 4.67 million blocked attacks. France and Germany together slightly surpassed the US in raw attack count, with 2.54 million and 2.3 million blocked attacks, respectively. Japan also stood out, with nearly 2.2 million blocked attacks. Windows users accounted for 92% of blocked tech support scam attacks, showing that this platform is particularly targeted. Often, Tech Support Scams resemble alerts from Windows Defender.

![Tech support scam targeting Apple users]

The infrastructure behind these Tech Support Scams often looked legitimate at first glance. In Germany and France, fake Windows error pages impersonated Windows Defender Security Center, used various Windows-style error codes and were hosted on Google Cloud Storage, making the pages look more credible to victims and harder to dismiss as obvious fraud. In France, adult-site malvertising redirected users to fake support pages. In Australia and the US, some campaigns reached victims through Facebook advertising. Other attacks used fake PayPal receipt PDFs, including Microsoft 365-themed lures, to create a billing dispute that victims were told to resolve by calling fraudulent support. The scam script was familiar, but the delivery was better aligned with situations where users already expect errors, invoices, payments or customer support.

### Impersonation scams used official pressure and personal urgency

Government impersonation was the main driver behind the rise in imposter scams. Gen blocked almost 1 million government scam attacks in H1 2026, up 387% from H2 2025. The number of protected users more than doubled, but the activity was heavily concentrated in the United States, which accounted for almost 800K blocked attacks alone, or 81% of the total. One single campaign shown on the image accounted for the majority of the blocks by itself, showing how a single campaign can dominate the half-year numbers when the lure and delivery path scale.

Family impersonation scams also rose sharply, up 454.2% over the second half of 2025. The activity was concentrated in Western Europe, led by the Netherlands, France, Ireland and Germany. These campaigns mostly reached Android users through SMS, and one SMS campaign accounted for 39% of all blocked family scam attacks in the period. Some documented cases used AI voice cloning, but the core technique remains older than AI: urgency, emotional pressure and a message that appears to come from someone the victim already knows. AI can make that cheaper and more convincing. It does not replace the social engineering, it improves the packaging.

![Family impersonation SMS]

![Government impersonation lure from the H1 2026 campaign set. The page borrows official-looking IRS framing and moves the user toward downloading and running an app.]

### Fake e-shops and scam-yourself attacks scaled through repeatable flows

E-shop scams (fake online stores) became one of the highest-volume scam categories in H1 2026. Gen blocked 114.2 million e-shop scam attacks, up 109% from H2 2025. The US accounted for 38.9 million blocked attacks. Western Europe was also heavily targeted, with the UK, Germany, France, Italy and Spain together accounting for 30.9 million blocked attacks. One large variant accounted for more than 10 million blocked attacks in which threat actors registered .click domains promoted through online ads. In practice, this means a victim could see an ad for a convincing-looking online store, click through to a disposable shopping site and be pushed toward a fake checkout or payment flow. The scale shows how quickly one repeatable store template can spread once the ads, domains and payment lure are in place.

Fake tutorial scams, part of the broader “Scam-Yourself Attack” pattern, increased 193% in H1 2026, rising from 1.79 million to 5.26 million blocked attacks. These attacks do not always try to break into the device directly. Instead, they guide the user into doing the attacker’s work: following fake instructions, copying commands, approving prompts or completing deceptive verification flows. Many sites imitated familiar anti-bot and security checks, including Cloudflare-style messages such as “Checking if you are human” and “needs to review the security of your connection before proceeding.” FakeCaptcha variants were a major component of this activity, with two campaigns alone accounting for more than 416K blocked attacks. Windows users were disproportionately targeted, accounting for almost 87% of blocked fake tutorial attacks, but the activity was also visible on Android and iOS, making it a cross-platform scam pattern rather than a Windows-only problem.

### Security Threats & Scams: H1 2026 Signals

- **TECH SUPPORT SCAMS**: 20.3M Blocked attacks, up 61.6% vs H2 2025.
- **IMPOSTER SCAMS**: Reached almost 1M blocked attacks, up 387% H/H.
- **FAMILY IMPERSONATION**: 5x increase. Family scams spread in Western Europe.
- **SCAM AD MACHINE**: 4.51M Scam-related ads in the analyzed dataset.
- **E-SHOP SCAMS**: 114.2M Blocked attacks, up 109% vs H2 2025.
- **FAKE TUTORIAL SCAMS**: +193% (5.26M blocked attacks in the “scam yourself” pattern).

### Reservation hijacking put fraud inside real customer service

Reservation Hijack scams are another good example of scammers breaking into trusted daily digital flows. The attack uses real reservation context, and in stronger cases compromised hotel-side or partner workflows, to make fraud feel like normal customer service. Victims may receive WhatsApp, iMessage, SMS, email or booking-platform messages that reference a real trip, a real property or a real payment issue. Once enough of the message is true, the false part becomes much harder to detect.

### Malvertising gave fraud operators reach

Scam advertising gave fraud operators a different advantage: reach. In our Scam Ad Machine research, we analyzed 14.57 million ads representing 10.76 billion impressions across the EU and UK over 23 days. We identified 4.51 million scam-related ads, nearly one in three ads in the dataset, generating 143.8 million impressions in the EU and 304.11 million impressions across the EU and UK in less than a month.

The follow-up research showed why this model survives individual takedowns. Scam advertisers used multi-facet ads, disposable advertiser accounts, deceptive presentation tricks and short-lived campaign tactics. A scam ad does not need to stay online forever. It only needs to look acceptable long enough to reach the right audience.

### Banking trojans and RATs were wrapped in local context

Malware campaigns followed a similar trust-abuse pattern, but with more regional tailoring. Banking trojan campaigns in Czechia, Slovakia and Poland used email-based JavaScript droppers that impersonated normal business correspondence, such as shipment notices, scanned document notifications or invoice-related emails. One lure simply told the recipient: “Dear Customer, I am attaching a scanned copy of the shipment.” In some cases, the messages came from compromised corporate mailboxes, which helped them look legitimate to recipients and email security systems. The payload modified proxy settings and installed browser add-ons to intercept banking sessions. In Brazil, fake payment PDFs impersonated ecommerce and banking brands to target the Boleto payment ecosystem.

RAT (Remote Access Trojan) campaigns were also localized and staged. In Italy, fake invoice PDFs, including Booking.com-themed lures, showed realistic Italian error dialogs, then delivered Vercel-hosted scripts with per-victim JavaScript obfuscation before moving to Blogspot-hosted PowerShell stages. In Poland, fake invoices delivered a steganographic .NET loader that installed Remcos RAT. In Czechia, a compromised third-party domain served multi-stage PowerShell that installed Babylon RAT. The payload families were not the novelty. The delivery layer was doing the work: local language, familiar documents, credible hosting and several steps before the final malware.

### Infostealers and crypto malware fed the next stage of fraud

Infostealers remained one of the main upstream suppliers for account takeover and identity fraud. Gen Threat Labs identified Remus, a new 64-bit infostealer attributed to the Lumma Stealer family. The analysis tied Remus to Lumma through shared obfuscation, string handling, syscall behavior and browser credential-theft techniques, and documented an Application-Bound Encryption bypass used by Remus and Lumma.

Crypto appeared in H1 2026 not only as a scam lure, but also as part of malware infrastructure. One cryptocurrency campaign used a four-stage infection chain that ended in a Rust-compiled multi-coin clipboard hijacker. The malware monitored the clipboard for wallet addresses across 21 blockchain types, including BTC, ETH and LTC. When a victim copied a wallet address, the malware replaced it with an attacker-controlled one, redirecting any pasted transaction to the criminals.

The same campaign also used Binance Smart Chain for command-and-control resolution through EtherHiding. Rather than relying only on a hardcoded C2 domain that can be seized or taken offline, the malware retrieved infrastructure pointers from data stored on-chain. That makes disruption harder: defenders can still block the resolved infrastructure, but they cannot remove the blockchain record like they would a malicious domain.

---

## Telemetry Deep Dive

### A Kimsuky-looking spike turned out to be coinminer activity

Most of this report looks at trends. But when a line suddenly jumps, the first job is not to explain the trend, it is to explain the jump.

That happened in January. Gen telemetry showed a visible increase in activity initially associated with obfuscation techniques previously observed in Kimsuky-related campaigns. At first glance, that could look like a possible actor signal. The campaign told a different story.

The rest of the evidence did not fit Kimsuky activity. The campaign targeted general consumers, not espionage targets. The lures referenced OnlyFans dumps and BTC wallets in VBS filenames. The payloads, code patterns and domains did not resemble known Kimsuky operations, and the activity led to coinminer detections rather than espionage tooling.

After analysis, the increase was classified as coinminer activity. Reused techniques can make telemetry noisy, especially when a detection is tied to behavior that later appears in unrelated campaigns. A spike has to be checked against the payload, lure, infrastructure, affected users and geography before it becomes a conclusion.

![Obfuscation techniques previously associated with Kimsuky-related activity appearing in coinminer campaigns, 7-day moving average]

### Software supply chain attacks abused developer trust

Developer tools and software packages also became a delivery route. Instead of targeting each victim directly, attackers compromised pieces of the software supply chain: public package repositories, developer accounts, code repositories and update processes. These are systems developers use every day, which is exactly why they are attractive. If a trusted package or repository is altered, malicious code can reach users through a normal install or update.

H1 2026 saw several examples of this model. Attackers compromised Node Package Manager (npm) and Python Package Index (PyPI) packages, hijacked maintainer accounts to publish malicious versions, and used compromised GitHub accounts to push malware into existing repositories while preserving a convincing commit history. AI developer tooling was also affected: in one case, a compromised npm publishing token was used to push an unauthorized Cline CLI update that installed OpenClaw on developer systems during an eight-hour window.

These incidents are different in detail, but the lesson is the same: the software supply chain is a trust system. Attackers are not only trying to fool end users with fake pages and scam messages. They are also trying to compromise the tools and components that legitimate developers trust, so the malicious code arrives through channels that look routine.

Gen Threat Labs saw a related version of the same trust problem on macOS. In March, we documented a cracked-software distribution chain where users looking for free or older versions of Mac apps were pushed through mirror sites, torrent uploads, forums, Telegram channels and repacked archives. In one tracked wave, Gen protections blocked about 108,000 attempts to launch these applications in the first 48 hours. The payloads included cryptominers, infostealers, backdoors and adware, but the more important mechanism was permission abuse: install guides often told users to disable Gatekeeper, turn off System Integrity Protection, run crack tools with administrator privileges or grant Full Disk Access. A Mac user may think they are only bypassing a license check. In practice, they may be giving an unsigned binary the permissions it needs to steal data, persist on the machine or use the device for someone else’s profit.

The main lesson from H1 2026 is that attackers are not abandoning old tactics. They are placing them inside trusted systems with better timing and better context.

---

## AI-Driven Attacks & Defenses

### Agents turned AI output into execution

AI agents changed the security discussion in H1 2026 because they turn model output into execution. An agent can fetch a URL, install a package, edit a file, connect to a service or call an API, often with the user’s credentials and local access. That makes agent security closer to endpoint, identity and application control than to traditional chatbot safety.

The OpenClaw incident mentioned in the previous section is a useful bridge into the AI risk story. The supply-chain angle was the compromised update path. The AI angle is delegated authority: once an agent is installed in a developer environment, it may have access to files, terminals, repositories, credentials or cloud resources. That makes agentic tools valuable, but it also means a compromise, a bad instruction or an execution mistake can have real consequences.

Agent risk does not always require a malicious actor. TechCrunch reported that a Meta AI security researcher gave an OpenClaw agent access to her inbox and asked it to suggest messages to delete or archive. Instead, the agent began deleting emails while ignoring stop commands sent from her phone. TechCrunch noted that it could not independently verify what happened to the inbox, so this should be treated as a reported incident rather than forensic evidence. Even with that caveat, the case illustrates the same problem: once an agent has real permissions, a mistake in interpretation, memory or context handling can become a real-world action.

Prompt injection became more practical in that environment. Unit 42 documented web-based indirect prompt injection observed in the wild, where attackers placed hidden or manipulated instructions inside web content later processed by an AI system. The risk depends on what the affected system can do: a summarizer may produce a bad answer, while an agent with permissions may leak data, click, transact or invoke tools.

Overprivileged agents create another failure path. “Double Agents” research found excessive default permissions in a cloud AI agent deployment, allowing a pivot from the agent’s execution context into customer project resources. This is a familiar security problem, too much privilege assigned to a workload, but agents make it easier to trigger because they combine interpretation, automation and access in one system.

Scammers also kept using AI as a persuasion tool. Gen Threat Labs research on celebrity deepfakes and avatar farms showed that the face is often only the wrapper. The message does most of the work: the script, the promise, the pressure and the call to action. In some cases, the presenter is synthetic. In others, real footage is reused with scam audio or narration. Defending against this means looking at behavior and intent, not only whether the face looks fake.

The same shift is visible in video-based scams. As customers encountered videos online, Gen’s on-device protection analyzed them for signs of AI-generated, synthetic or manipulated content that could be used to mislead them. During H1, tens of millions of those video encounters showed AI involvement. An average monthly share of the identified AI content, around 3.2%, was classified as scam activity, and at that scale even a low percentage represents a meaningful scam volume. AI-generated video gives scammers a cheap way to produce persuasive faces, voices, testimonials, fake news clips and celebrity-style endorsements at speed. Most AI-generated content is not malicious, but when synthetic media becomes this easy to produce and distribute, even a small scam rate can translate into a large number of attempts to mislead users.

The Anthropic Mythos and Fable 5 sequence exposed a simple problem: once a frontier model can materially improve cyber work, the model itself becomes part of the security problem. Anthropic said Mythos Preview could identify and exploit vulnerabilities in major operating systems and browsers when directed to do so. Project Glasswing showed the defensive use case, with Anthropic reporting more than 10,000 high- or critical-severity flaws found across important software. That changes the pressure on defenders. Finding bugs is no longer the only hard part. Vendors and maintainers also need to validate, disclose, prioritize and patch at a pace that can keep up with AI-assisted discovery.

Fable 5 then showed the access problem. After launch, Anthropic said it received a US export-control directive requiring it to suspend access to Fable 5 and Mythos 5 for foreign nationals, including foreign-national employees inside the United States. Because Anthropic could not verify nationality in real time, it disabled both models for all users while it worked through compliance. The restrictions were later lifted after new safeguards were added, with Fable 5 restored more broadly and Mythos 5 access being restored through Project Glasswing.

> **Deepfake and AI video scams: small share, meaningful volume**  
> **3.2% average monthly share classified as scam activity**  
> Among tens of millions of AI-related video encounters, only a small share was classified as scam activity. But at that scale, even a low percentage translates into meaningful scam volume, especially when deepfakes, synthetic presenters and manipulated video are used to make fraudulent messages look more credible.

For this report, the point is not to decide whether the government or Anthropic was right. The security issue is broader: once a model can accelerate cyber activity, access becomes part of the threat model. Who can use it, where they are located, what safeguards exist, what gets logged and who can remove access all become operational questions. For defenders building on these systems, trust depends on more than model behavior. It also depends on availability, governance and control.

Gen’s response in H1 2026 was to build controls around the parts of agentic AI where risk actually happens: before installation, during execution, at the tool boundary and at the network boundary. The Agent Trust Hub addresses the pre-use layer, helping establish trust before an agent or skill is used through static identity and verification checks.

Sage, developed by Gen’s AI Foundry, brought that idea into the execution loop. It checks agent actions before they happen, including shell commands, URL fetches, file writes and package installs. It also ships with hundreds of detection rules covering command injection, persistence, credential exposure, obfuscation and supply-chain attacks.

Because Sage launched during the period and its user base was still ramping, these detections should be read as an initial signal rather than a full H1 trend. In any case, they give us a useful view into one of the most important points in the agent lifecycle: the moment an AI agent moves from producing an answer to taking an action.

Once an agent can fetch a URL, install a package, read a file, write to the system or run a command with the user’s permissions, the security question changes. It is no longer enough to ask whether the model produced a safe response. We also need to know whether the next action should be allowed to happen.

Early Sage telemetry shows which rules fired most often when an agent was about to act. These detections fall into two broad groups. The first is risky local behavior produced by the agent itself while working through a task: fetching and running code in one step, reverse-shell patterns, forced deletion, access to SSH authorized_keys, and attempts to read authentication files, environment files or API-key patterns. Security teams would immediately recognize these as dangerous because they can expose credentials, create persistence, open a command channel to an outside operator or damage the local system.

The second group is external manipulation aimed at the agent. Hidden prompt injection, including instructions concealed inside markdown links or HTML comments, tries to make the agent follow commands the user never saw. Instruction-override attempts try to push the agent away from its original task or safety constraints. In these cases, the agent itself becomes the target, and the risky action may happen only after the agent processes hostile content.

Both groups point to the same conclusion. Runtime enforcement has to sit at the point of action, when the agent is about to fetch, install, read, write or execute. Model-level safeguards and user warnings still help, but they are too far away from the moment where the risky behavior becomes system activity.

![Top 10 Sage detections in H1 2026, ranked by observed rule activity.]

Agent Detection and Response, or ADR, extends that same model. Verification tells users what an agent or skill is before use. ADR watches what the agent is doing at runtime, where risk becomes real. Gen’s ADR work runs client-side, inside the agent’s execution loop, so actions can be assessed close to execution, with limited cloud-assisted checks for specific security signals such as extracted URLs and package file hashes. When malicious activity is blocked, sanitized detection metadata may also be used to improve protection through Gen’s Community IQ systems.

AARTS, the AI Agent Runtime Safety Standard, addresses a different but related problem: every agent host exposes different events, context and enforcement options. Without a shared contract, security integrations become one-off projects with uneven visibility. AARTS defines where security decisions can be made, what data is available for evaluation and how decisions are enforced across hosts.

Gen also moved beyond its own products and into the wider AI skills ecosystem. The Vercel partnership brought Agent Trust Hub verification and transparent risk ratings to skills.sh, where developers can publish and install reusable AI agent skills. Each skill can be classified as Safe, Low Risk, High Risk or Critical Risk before users execute it.

The OpenClaw event reinforced the same direction. Gen and members of the OpenClaw team co-hosted a post-RSA event focused on verifying, monitoring and securing AI agents in real-world environments, with Agent Trust Hub presented as infrastructure for safe deployment.

The April announcements showed how far this work was moving into consumer-scale AI. Gen announced VPN for Agents through the Agent Trust Hub and expanded Norton AI Agent Protection inside Norton 360, including protections for plugins, skills and tools, prompt injection defense, and code and file scanning for content accessed or generated by supported AI agents.

Gen’s partnerships with xAI and Microsoft point to the same conclusion from another angle: trusted AI is becoming part of mainstream consumer workflows, not a lab problem. The xAI partnership brings Grok models into Gen consumer platforms, starting with Norton Neo AI Browser, with Agent Trust Hub verifying, monitoring and enforcing agent behavior. The Microsoft integration brings Engine by Gen into Copilot, MSN and Bing surfaces to ground financial recommendations in compliant product data.

This combination of threat research, open-source tooling, standards work, runtime enforcement and consumer product integration moves the discussion from warning to implementation. The field already knows AI can be abused. The harder work is building controls that govern what agents can install, access, call, remember and connect to.

---

## Privacy

### Persistent access became the privacy problem

The privacy story in H1 2026 was not limited to exposed databases. The larger issue was persistent access: to messages, memories, location trails, browser data and the files AI agents are allowed to read. Some of that access came from criminal compromise. Some came from normal product features used in ways most people do not fully understand.

Gen blocked an average of 310.8 million tracking attempts per month in H1 2026, adding up to around 1.9 billion tracking attempts blocked across the half-year. The privacy risk here is not only in headline breaches or spyware. It also comes from the constant background economy of tracking, profiling and data collection that follows people across everyday browsing.

GhostPairing is the clearest example on the messaging side. The attack abuses WhatsApp’s legitimate device-linking feature, tricking the user into approving an attacker-controlled browser as a linked device. There is no password theft and no need to intercept an SMS code. Once the pairing is approved, the attacker has a fully authorized session that can remain active until the victim manually removes it.

The privacy impact goes beyond account misuse. A linked device can give the attacker access to conversations, media and voice notes, which can reveal how people talk, who they trust and what kind of request they might respond to. That material can later support impersonation, fraud, extortion or deepfake-enhanced scams. The practical issue is visibility: many users do not regularly check linked devices, so a session created in one distracted moment can stay connected for a long time.

Infostealers put the same privacy problem inside the browser. Gen Threat Labs identified Remus, a new 64-bit infostealer attributed to the Lumma Stealer family, with capabilities focused on browser passwords, cookies, cryptocurrency data and other stored secrets. For attackers, the browser is no longer just a place to steal passwords. It is a store of sessions, wallets, extensions and account context that can be reused without asking the victim to log in again.

AI agents added another privacy boundary. When an agent can read files, browse websites, use memory, connect to tools and act inside a local environment, privacy depends on what the agent can access at runtime, not only on what the user typed into a prompt. This is why agent memory and tool use are now privacy issues as much as security issues. Gen’s AARTS work explicitly includes hook points for memory read and write operations, tool use, model requests, plugin loading and MCP connections, because those are the places where sensitive data can be exposed or misused.

Research in H1 2026 showed how this can fail. One paper, “Your LLM Agent Can Leak Your Data,” described a backdoored agent that retrieves stored user context through memory-access tool calls and exfiltrates it through disguised retrieval calls. Another, “Trojan Hippo”, focused on long-term memory attacks where a dormant payload planted through an untrusted tool call can later activate when the user discusses sensitive topics such as finance, health or identity. These are research settings, not mass consumer campaigns, but they describe a risk pattern we should treat seriously: memory turns a temporary interaction into a lasting data surface.

Location data remained a separate privacy problem because it can be collected and sold through commercial data ecosystems without looking like a breach. In May 2026, the FTC announced a settlement that would prohibit Kochava and its subsidiary from selling, sharing or disclosing sensitive location data without affirmative express consent. The FTC said the data was linked to hundreds of millions of mobile devices and could be used to trace people’s movements, including visits to sensitive locations.

That case followed earlier FTC action against Mobilewalla, where the agency alleged that the company collected precise location data from real-time advertising auctions and third-party aggregators, often without consumers’ knowledge. The FTC said the raw data was not anonymized and could identify individual mobile devices and sensitive places people visited.

These examples point to the same privacy lesson from different directions. Users rarely think in terms of sessions, cookies, memory stores, SDKs or linked-device lists. Attackers and data brokers do. Privacy protection now depends on making persistent access visible and revocable: linked devices that are easy to audit, browser data that is harder to steal, agent permissions that are scoped and enforced at runtime, and location data that cannot quietly move through advertising and broker ecosystems without meaningful consent.

### Privacy: tracking at scale

- **TRACKING ATTEMPTS BLOCKED**: $\approx 1.9\text{B}$ (Tracking attempts blocked in H1 2026.)
- **MONTHLY AVERAGE**: $310.8\text{M}$ (Average tracking attempts blocked per month.)

Tracking was the clearest measurable privacy signal in H1 2026. The broader privacy risk came from persistent access: linked messaging sessions, browser session data and AI agent memory can all keep exposing information after the user thinks the interaction is over.

---

## Trust & Identity

### Exposed data moved quickly toward attempted use

Identity risk in H1 2026 was less about one stolen password and more about how exposed identity data, trusted sessions and real-world context were reused. Attackers were not always trying to break into an account by force. They were trying to make themselves look authorized: a linked device, a booking contact, a credit inquiry, a service validation request, a message from a known person.

The breach signal was strong. Gen telemetry recorded 18,618 breach events discovered so far affecting our customers in H1 2026, up 94.5% from 9,571 in H2 2025. Breach notifications sent to Norton and LifeLock users, where the source of the data leak was identified, rose much faster, increasing 628.1%, from almost half a million in H2 2025 to 3.3 million in H1 2026.

The pressure was clearest in February, when breach notifications peaked at more than 1 million alerts in a single month, affecting close to 1 in 26 active users that month. That single month accounted for roughly a third of all H1 2026 breach notifications. A small increase in breach events can still produce a much larger increase in affected people if the exposed datasets are larger, richer or more useful to criminals.

May and June showed why the event count alone can understate the risk. In May, breach events reached 3,554, and exposed records reached 9.62 million, including 9.36 million records with email addresses. In June, breach events passed 5,000 in a single month.

### Trust & Identity: breach and downstream fraud signals

- **BREACH EVENTS IDENTIFIED**: `18,618` (Up 94.5% compared with 9,571 events in H2 2025.)

#### BREACH EVENTS IDENTIFIED IN H1 2026
| Jan | Feb | Mar | Apr | May | Jun |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2,393 | 2,321 | 2,828 | 2,486 | 3,554 | 5,036 |

_Breach intelligence is continuously processed and enriched. Monthly figures may change as additional breach data is identified, attributed or reclassified._

- **BREACH NOTIFICATION ALERTS**: `+628.1%` (Alerts with an identified breach source sent to Norton and LifeLock users grew from almost half a million to 3.3M in H1 2026.)

#### MONTHLY ALERTS
| Jan | Feb | Mar | Apr | May | Jun |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 301K | 1.04M | 489K | 387K | 860K | 228K |

- **CREDIT INQUIRY ALERTS**: `460K` (Credit inquiry alerts in June, close to half a million in a single month.)
- **IDENTITY VALIDATION ALERTS**: `7x increase` (Service-industry identity validation alerts compared with H2 2025, when this alert was introduced.)
- **MAY RECORDS EXPOSED**: `9.62M` (May had the highest exposed-record volume of H1, including 9.36M records with email addresses.)

One likely contributor to the February spike was a large third-party e-commerce incident in the United States. The timing lines up with the Under Armour breach reported in January 2026. Public reporting said the incident affected around 72 million email addresses, with some records also including names, genders, birthdates and ZIP codes. Under Armour said at the time that it had not seen evidence that passwords, payment systems or financial data were compromised. The breach was believed to have taken place late in 2025, even though it surfaced publicly in January 2026.

This is a useful example of how breach risk moves through time. The compromise may happen in one reporting period, become public in another and trigger consumer alerts later, once the exposed data is processed, matched and pushed to affected users. The exposed data in this type of incident may not include passwords or payment cards, but that does not make it harmless. Email addresses, names, birthdates and ZIP codes can make phishing, account-recovery abuse, credential stuffing and other scams far more targeted and convincing, especially when combined with data from earlier breaches.

Gen also identified a recurring source of combo lists, including datasets posted to the Telegram channel “Wings Daily Updates FREE,” that aggregated credential-related data month after month and remained active into H1 2026. The datasets included usernames, passwords, salts, target URLs and other records useful for credential abuse. When this kind of data is processed and matched against protected users, it can create visible spikes in breach-related records even if some of the original credential theft happened earlier.

This is one reason breach telemetry does not always follow the calendar of the original compromise. Data can be stolen, traded, repackaged, posted to Telegram, copied into new lists and only later detected at scale. By the time a customer receives an alert, the exposure may already have moved through several hands.

This proved to be true in May, when the second large spike occurred. The exposed record count reached 9.62 million, including 9.36 million records with email addresses, driven by a large credential exposure rather than a single newly disclosed corporate breach. Across H1 2026, breached records containing email addresses increased by 287%, from 4.43 million in H2 2025 to 17.16 million. For users, the practical risk is straightforward: if the exposed password is still in use, attackers can try it against the original service or reuse it against other accounts. That is why password reuse turns one exposed credential into a much larger identity risk.

![Breached records with email addresses, H1 2026 monthly trend]

Another large exposure surfaced in January. Public reporting described a dataset containing primarily Chinese citizen data exposed online. The data reportedly sat inside 39 organized indexes and appeared to have been collected and aggregated since late 2025 for unknown purposes. One portion of the dataset, indexed as “wyy,” contained usernames, passwords, email addresses and other compromised user details. Other reporting on the wider exposure described a much larger set of personal data, including names, mobile numbers, addresses, national ID numbers, birth details and social media identifiers.

This kind of incident is better understood as an aggregated identity dataset than as a single breach. The original compromises may have happened across different services, at different times, and for different reasons. Once the data is collected into a searchable structure, the attacker no longer needs to care where each field came from. A password from one source, an email address from another and an identity number from a third can become one usable profile.

That is why large exposed datasets can keep creating risk long after the first compromise. The data can be copied, repackaged, merged with other leaks and used again in credential stuffing, phishing, account recovery abuse or identity fraud.

This pattern also appeared outside our telemetry. The Identity Theft Resource Center reported 780 publicly reported compromises in Q1 2026, leading to nearly 140 million victim notices, with Under Armour contributing 72.7 million of those notices. The ITRC noted that the quarter had fewer breaches than Q1 2025, but victim notices remained very high, partly because a small number of large events accounted for a large share of affected individuals.

The downstream signal was harder to ignore. Credit Inquiry alerts reached 460K alerts in June. A credit inquiry is not proof of fraud by itself, but at this scale it is a strong indicator that exposed identity data is being tested or used in financial contexts.

Identity validation alerts also rose. Identity Validation with Service Industry alerts increased 577%, from about 1,700 to about 11,500. Part of that increase reflects product coverage, as LifeLock started supporting this alert type during H2 2025. April accounted for more than a third of the period’s activity. This is lower volume than breach notifications or credit inquiries, but it points to the same underlying issue: stolen or exposed identities are being used beyond classic credit fraud. They are being tested in onboarding flows, service accounts and verification processes where trust is created automatically if the data looks right.

GhostPairing shows the identity problem from the account side. As described earlier, the attack turns WhatsApp’s linked-device approval flow into the point of compromise. Once the victim approves the device, the attacker is no longer outside the account. They are operating through an authorized session that can stay active until the victim finds and removes it.

The attacker does not need to become the victim permanently. They only need enough authorized access to read conversations, collect context and send messages from a trusted account. In practical terms, the identity being abused is not only the phone number or the account. It is the relationship graph around that account: contacts, conversations, groups and the trust other people place in messages coming from it.

The identity problem in H1 2026 was increasingly built from fragments. A breached email address, a credit inquiry, a service validation request, a linked device and a known contact are separate signals in isolation. Criminals combine them until a system or a person accepts the interaction as legitimate. Identity protection has to account for that full chain, from exposure to attempted use, not only the moment data first leaks.

---

## Financial Wellness

### Financial risk surfaced before the final transaction

Financial risk in H1 2026 showed up earlier in the attack chain. The strongest signals were not only users being pushed to pay a scammer. They were alerts around credit checks, account activity, loan applications, lease activity and other moments where exposed identity data can turn into financial harm.

Financial alerts give us a different view of identity risk. Breach notifications show where personal data has been exposed. Financial alerts show where that data may be getting tested, reused or turned into activity that can affect a person’s credit, accounts or money.

Across H1 2026, we saw increases in several alert categories tied to financial activity, including credit inquiries, depository activity, account-related changes and other signals that can appear before a consumer sees direct financial loss. These alerts do not always prove fraud by themselves. They are early warnings: something has changed, someone is checking, opening, moving, applying or modifying in a way the user may not recognize.

Gen telemetry showed a sharp rise in financial activity alerts after these alert types were introduced. Financial Activity, Depository alerts increased 734%, about eight times, from about 175K in H2 2025 to almost 1.5 million in H1 2026. Financial Activity, Credit alerts increased more than tenfold, from about 16K to 163K.

### Financial Wellness: early warning signals

- **DEPOSITORY ACTIVITY ALERTS**: `+734%` (Almost 1.5M alerts in H1 2026 vs 175K in H2 2025.)
- **CREDIT ACTIVITY ALERTS**: `>10x` (163K alerts in H1 2026 vs about 16K in H2 2025.)
- **CREDIT INQUIRY**: `460K` (Credit inquiry alerts reached 460K in June.)
- **INSTALLMENT LOAN APPS**: `+150%` (New application alerts rose from 55K to 137K.) [Note: Text mentions 140K later]
- **LEASE APPLICATIONS**: `+261%` (New Application, Lease alerts rose from 3K to almost 11K.)
- **WEB SKIMMING**: `3x increase` (Almost 1M blocked attacks in H1 2026 [996.3K].)

Credit inquiry alerts added another strong signal. May alone saw 450K credit inquiry alerts, with the trend continuing in June, reaching 460K alerts. A credit inquiry does not automatically mean fraud, but a spike at this scale tells us that exposed identity data is being tested or used in financial contexts.

Loan and lease-related activity followed the same direction. LifeLock introduced this alert type during H2 2025, so the increase reflects both observed activity and broader protection coverage. New Application, Installment Loan alerts increased by 153%, from 55K in H2 2025 to 140K alerts in H1 2026. New Application, Lease alerts rose 261%, from 3K in H2 2025 to almost 11K in H1 2026. Coverage also expanded in H1 2026, with Soft Inquiry alerts complementing this category. These signals can appear before a victim sees money leave an account, when personal data is being tested or converted into attempted financial access.

Web skimming added a more transaction-level signal. Gen blocked 996.3K web skimming attacks in H1 2026, up 212% from H2 2025, roughly a threefold increase. Unlike a credit inquiry or loan application alert, web skimming appears when the user is already near the point of payment. The attack typically abuses a checkout flow or payment page to capture card data while the purchase still looks normal to the victim. That makes it part of the same trust problem seen across the report: the user is not necessarily being pushed into an obviously suspicious action. The abuse is inserted into a process where payment is already expected.

This connects directly to the identity patterns described in the previous section. A breach notification is the first sign that data is exposed. A credit inquiry, loan application, account activity alert or web skimming block may be the first sign that exposed data, payment context or financial trust is being abused. That gap between exposure and use is where financial protection increasingly has to operate.

### First-party abuse: real accounts, recruited users

MoneyLion observed another pattern in H1 2026 that fits the same trust-abuse model: fraud operators are recruiting real people and turning their verified accounts into tools for financial abuse.

This is different from stolen identity or synthetic identity fraud. The person is real. The documents are real. The account can pass normal onboarding and KYC checks because, at the beginning, there may be nothing fake to detect. The risk appears later, when that real account is used in ways the financial institution did not intend.

In one pattern, fraud operators used social media platforms and online communities to recruit people with offers of quick cash, commissions or referral incentives. Recruited users created accounts under their own names and completed verification successfully. After that, some shared their credentials with an external operator. Others stayed involved, helping the operator pass authentication or verification checks when needed.

Once the account was available, it could be used for cash advance abuse, credit product misuse, wallet funding, large-scale money movement, referral program exploitation or mule activity. In some cases, the user may know they are participating in abuse. In others, they may think they are taking part in a side hustle or a referral scheme, without understanding that their identity, credit profile and account access can be misused.

This makes first-party abuse hard to stop at the usual checkpoint. At account creation, many signals look legitimate because the customer, the identity documents and the onboarding flow are legitimate. Blocking too early creates friction for real users. Waiting too long gives fraud operators time to move funds, test products or coordinate activity across accounts.

Identity verification is still necessary, but it cannot be the last serious checkpoint. When fraud moves through real accounts, protection has to continue after onboarding. Behavioral intelligence, account ownership checks and detection of coordinated activity become the signals that show whether a verified account is still being controlled and used as expected.

![First-party abuse turns real accounts into vehicles for financial fraud after onboarding.]

Financial protection is also becoming part of AI-driven consumer experiences. Gen’s Engine was integrated into Microsoft’s Copilot, MSN and Bing surfaces to provide financial product intelligence grounded in compliant product data. That points to a wider shift: as consumers rely on AI assistants for financial decisions, the quality and trustworthiness of the underlying financial data becomes a security and safety issue, not only a user experience issue.

The financial wellness story for H1 2026 is that harm is moving across a chain. It can start with exposed identity data, move through validation or credit activity, and end in account misuse, loans, leases, payments or scam losses. Waiting for the final transaction is too late. The useful signals are often earlier: breach alerts, credit inquiries, account activity, new applications and payment requests that do not fit the user’s normal behavior.

---

## In Closing

### Protecting trust is now part of protecting people

The first half of 2026 showed how much digital safety depends on context. The same action can be harmless or dangerous depending on where it appears, who appears to be asking, what happened before, and what authority has already been granted.

A hotel payment request is not suspicious in the abstract. It becomes suspicious when it arrives through the wrong path, at the wrong time, or asks the guest to verify details through a fake flow. A linked device is a normal messaging feature until the user is tricked into approving an attacker’s browser. A package update is routine until the trusted maintainer account has been compromised. An AI agent is useful until it acts on the wrong instruction with permissions the user did not fully understand.

That is why the old warning signs are no longer enough. Bad grammar, strange links and unknown senders still matter, but many H1 2026 attacks were built to avoid exactly those signals. They used real reservation details, familiar infrastructure, known brands, legitimate sessions, normal developer workflows and financial events that users expect to see. The attack often hid inside the ordinary.

For defenders, this changes the question. The issue is not only whether something looks malicious. It is whether the action makes sense in context. Should this booking message be asking for payment? Should this browser session still be linked? Should this package update be trusted? Should this agent be allowed to write files, call a tool or connect to a service? Should this credit inquiry or financial activity match what the user actually did?

This is where Gen’s role as a trust layer becomes more concrete. Consumers should be able to use modern digital services, including AI agents, financial intelligence, messaging platforms, online travel, cloud services and developer tools, without personally auditing every model, app, package, prompt, session, ad or payment flow. Protection has to operate closer to the moment trust is granted or abused.

That means blocking scam pages before a user enters payment details. It means detecting malicious infrastructure even when it sits behind legitimate cloud services. It means identifying account access that looks authorized but was socially engineered. It means enforcing agent decisions before a tool is used, a file is changed or a connection is opened. It means following exposed identity data after the breach, when criminals try to turn it into credit activity, account misuse or financial loss.

Attackers will keep adapting old methods to new trust systems. The response has to be just as practical: better telemetry, stronger runtime controls, identity protection that follows data after exposure, privacy controls that reveal persistent access, and financial signals that surface before damage becomes harder to reverse.

The threat landscape is not moving toward one single problem. It is moving toward attacks that connect scams, malware, identity, privacy, AI and financial abuse into the same chain. Protecting people now means protecting the trust they place in that chain, before attackers do.

---

## Acknowledgments and Credits

### Primary Researchers
- Luis Corrons
- Patrik Holop

### Communications
- Aneta Šeráková
- Brittany Posey

### Brand design
- Alisha Robinson

### Contributors
- Alex Arazi
- Alexej Savčin
- Břetislav Šopík
- Daniel Beneš
- Daniel Snášel
- Eliška Lorenzová
- Filip Husák
- Ganesh Choudhari
- Jakub Křoustek
- Jan Rubín
- Jan Širmer
- Michal Salát
- Ondřej Mokoš
- Saketh Kodam

---

## About Gen

Technology solutions for the next generation of digital life.

Gen (NASDAQ: GEN) is a global company dedicated to powering Digital Freedom through its trusted consumer brands including Norton, Avast, LifeLock, MoneyLion and more. Gen brings award-winning products and services in cybersecurity, online privacy, identity protection and financial wellness to nearly 500 million users in more than 150 countries.

### Our Story

### Join our Team
We're always looking for smart, fearless and dedicated people to join Gen. Our global workforce has dual headquarters in Prague, Czech Republic and Tempe, Arizona, USA. Ready to help today’s and tomorrow’s generations take control of their digital lives?

- [Join our Team](#join-our-team)
- [Legal](#legal)
- [Procurement](#procurement)
- [Privacy Center](#privacy-center)
- [Cookie Policy](#cookie-policy)
- [Accessibility](#accessibility)
- [Privacy Settings](#privacy-settings)

---

Copyright © Gen Digital Inc. All rights reserved. NortonLifeLock, the NortonLifeLock Logo, the Checkmark Logo, Norton, LifeLock, and the LockMan
Logo are trademarks or registered trademarks of NortonLifeLock Inc. or its affiliates in the United States and other countries. Other names may be
trademarks of their respective owners.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
