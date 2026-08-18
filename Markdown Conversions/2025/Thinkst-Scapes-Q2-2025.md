Organization: Thinkst
Report Title: Scapes-Q2
Year: 2025

Most companies find out way too late that they've been breached.

[https://canary.love](https://canary.love)

## Table of Contents
- [Introduction](#introduction)
- [Beyond the Horizon: Uncovering Hosts and Services Behind Misconfigured Firewalls](#beyond-the-horizon-uncovering-hosts-and-services-behind-misconfigured-firewalls)
- [Language Models Large and Small](#language-models-large-and-small)
- [Parser Differentials: When Interpretation Becomes a Vulnerability](#parser-differentials-when-interpretation-becomes-a-vulnerabilities)
- [Nifty Sundries](#nifty-sundries)
- [Conclusions](#conclusions)

---

## Introduction

Themes covered in this issue:

- Networking is always tricky
- Language models large and small
- When parsing goes right, and when it goes wrong
- Nifty sundries

Between the first of April and ts@thinkst.com.

---

## Beyond the Horizon: Uncovering Hosts and Services Behind Misconfigured Firewalls

This research systematically scanned the IPv4 internet space for firewall misconfigurations and the inadvertently-exposed services. While most modern firewalls operate via stateful rules to only allow external traffic through the firewall when associated with an internally-initiated request, firewalls can be (or configured to be) stateless. This lack of tracking of connections (or related UDP packets) means that if a stateless firewall allows TCP connections to, e.g., port 80, it must also allow externally-generated traffic with a source port of 80 through. This led to a common misconfiguration in the past where stateless firewalls permitted source port 80 or source port 53 traffic to be...

This vulnerability was publicised widely in 2014 as both Microsoft and Apple’s firewalls...

This research worked to understand the prevalence of these misconfigurations and what could be accessed with this vulnerability. The study found almost 2.5 million newly accessible...

While the source port manipulation technique...

It makes sense...

While the research showed limited evidence... that is not going to last. Check your firewall rules, firewalls.

---

## Language Models Large and Small

### Beyond the Horizon: Uncovering Hosts and Services Behind Misconfigured Firewalls
- Accessing client local ports, differences in how the address `0.0.0.0`...
- The first talk...
- The second research release...
- Comparative pixeling scripts would share unique identifiers to correlate the...
- Both of these works...
- The confusion...
- The ability to open listening sockets is difficult to contextualise...
- Permission...
- Sadly, Facebook was all too keen...
- ![A figure demonstrating browsing traffic]

### SNI Censorship on the TLS-Layer
To bypass such systems while still interoperating with unmodified servers. Blocking specific IP addresses and unencrypted traffic flows is simple enough, but the growth of encrypted traffic and IP addresses that host multiple services makes censorship a tougher challenge. As of TLS 1.3, support is mandated for the SNI field, which is used...

Modify certain parameters of the connection. These modifications were then tested against a variety of different web servers and configurations to determine which would allow for successful HTTPS browsing. Finally, each attempted bypass modification...

Ship systems. These systems see traffic as it flows by and can decide to inject a RST packet to kill the connection. By using TLS fragmentation, the SNI field can be split...

Fragmentation and out-of-order reassembly offers a powerful primitive to bypass network filters. Such filters (e.g., censorship devices, WAFs, etc.) either...

While as an anti-censorship technique...

### How I used o3 to find CVE-2025-37899, a remote zeroday vulnerability in the Linux kernel’s SMB implementation

### Enhancing Secret Detection in Cybersecurity with Small LMs

The first blog post shows that it’s possible to scale up LLM vulnerability...

When it comes to determining the impact of a vulnerability on a specific... to static measures such as software bill-of-materials and the CVSS...

Takes significant manual effort to determine if a newly-discovered vulnerability will impact a specific organisation. If, for example, the... accessible to LLMs, this nuanced analysis can be offloaded (partially...

LLM-reported real security findings to...

While readers looking for hard technical details...

As XBOW continues to scale up, their findings could indi-... time are removed, will XBOW continue to find bugs in well-ex-... to find new vulnerabilities (sparse)? This sparse vs. dense de-...

LLM-assisted impact analyses... and more system data is codified... on a static CVSS score.

Was a human-LLM teaming effort, and that every line was human reviewed. The commit logs for the library also detail each modification as human or LLM-sourced.

At first glance, the library was designed with a solid foundation, but diving deeper, flaws became evident. Overall, the author noted insufficient testing code, missing security best-practices, and a few instances where OAuth-specific functionality was...

Security flaws in the candidate implementation. Overall, the library suffers from the...

Or flat out wrong, the LLM code was influenced negatively.

Software development education... As seen in the commit logs... Without sound tools... It is worrying...

Vulnerability in the kernel’s SMB file-sharing implementation to measure o3’s ability to find the vulnerability. The LLM was provided the...

Use-after-free... the performance was improved, but with more manual upfront effort... port a vulnerability that did not exist in the code). This finding, despite... tections, and power bug-find...

This post highlights... Automation to validate outputs... More work is needed...

This blog helps show how changing context size can influence... the tradeoffs of inferences, context size and performance... tion CVEs, and are difficult to find automatically, so they can...

This talk detailed the process of building a secrets scanner for code with a fine-tuned... and fine-tuning it to recognise secrets that existing scanners typically miss. By quan-...

This model of fine-tuning... The privacy, scalability and cost benefits... As more use cases of language models are optimised into more specific... acceptance – allowing for a flourishing ecosystem of specialised models for...

![Figure 5]

This work aims to detect if an LLM has been trained or fine-tuned maliciously to add a backdoor. Backdoors in LLMs are specific input tokens (or sequences thereof) that...

But only when prompted to generate a Node.JS source file. Existing detection algo-... determine if there are triggering inputs that cause the model to generate specific...

Set looking for specific tokens (or sequences thereof) that will cause the entropy of responses to drop significantly. Over a varied host of different LLM types and backdoor architectures, BAIT averages 98% accuracy with an average runtime of under 15...

As the ecosystem around customised/fine-tuned models matures, these types... CI/CD pipelines... The scale of investments needed...

---

## Parser Differentials: When Interpretation Becomes a Vulnerability

- 3DGen: AI-Assisted Generation of Provably Correct Binary Format Parsers
- GDBMiner: Mining Precise Input Grammars on (Almost) Any System
- Parser Differentials: When Interpretation Becomes a Vulnerability
- Inbox Invasion: Exploiting MIME Ambiguities to Evade Email Attachment Detectors

![Greyton to McGregor trail in Boesmanskloof, South Africa. Image by Tom Windell (Thinkst)]

Loop effort needed to generate formal specifications for network protocols. EverParse allowed Microsoft to replace much of their network code in Azure and Hyper-V with formally-verified code synthesised from specification. While the size of the specification is significantly smaller than the code generated, EverParse still required human experts to write the specification. This research effort explored human-...

Humans to reduce ambiguities, and generate specifications.

Specification contains the same flaws as the implementation. 3DGen is able to create multiple “flavours” of the specification and generate simple test cases to show the differences between them. This allows the process of specification generation to...

Been tested on 20 different network protocols and has contributed to specifications used for real-world network components, including finding incomplete human-written specifications.

![Figure 7]

While showing a natural strength generally ambiguously defined, this approach offers a path forward for LLM-...

Few human developers... documentation and generate formally-verified parsers for a complex protocol.

3DGen aims to automate... canonical specification... By adding formal tools...

To recover its input grammar. When fuzzing software to find bugs, there are two main...

Within (or the edges of) those specifications to generate inputs that can reach deeper...

Seed inputs, the miner can generate a control-flow graph. It then identifies the steps...

While fuzzing has shown to be incredibly effective at finding bugs, even...

![Figure 8]

Running GDBMiner is a time-consuming process... be performed once per application – after that, it can accelerate bug finding... more efficient by only generating inputs that will be processed more deeply.

Expect to see tools like GDBMiner used with LLM-augmented bug finding...

Differentials in diverse systems. Parser differentials are when two components of a system understand the same data differently. As a simple example, the most...

Whereas in JavaScript, the key’s value will be the last value declared. This differential...

Leged roles, but Erlang components would include the first-defined value containing...

Talk switched focus to how parser differentials are often discovered separately from the context in which they are impactful. By “stockpiling” discovered differentials, a...

In the figure below, a cute YAML snippet is shown that is parsed such that the lang...

And systems. By finding combinations of heterogeneous parsers where one fulfills... differentials can have an impact. Such a combination was discovered in GitLab, where...

While not treading any new theoretical ground,... As more examples of differential-based vulnerabilities come to light, intuitions for how to make use of newly-discovered differentials will increase the speed of...

Slipped in as almost an afterthought in the talk,... Reusing well-built parsers (or synthesising them from a specification) across a...

![Figure 9]

Parsed differently by...

This work applied parser differentials to a high-impact area: email malware scanning... emails (those bearing binary content), the researchers were able to find a large num-... ments. However, the end client would have a different parsing logic that could allow...

Duplicated content-type headers, where a gateway would only analyse the first header, but a client would use the second. A bypass using ambiguous structure modifica-... test-case generation and testing, the research team was able to find bypasses for all 16 tested products, including combinations between the same and differing vendors.

Exploiting parser differentials... It’s a difficult balancing act for service providers...

![Figure 10]

---

## Nifty Sundries

- Impostor Syndrome: Hacking Apple MDMs Using Rogue Device Enrolments
- Your Cable, My Antenna: Eavesdropping Serial Communication
- GoSonar: Detecting Logical Vulnerabilities in Memory Safe Language Using Inductive Constraint Reasoning
- Show Me Your ID(E)!: How APTs Abuse IDEs
- Inviter Threat: Managing Security in a new Cloud Deployment Model
- Carrier Tokens—A Game-Changer Towards SMS OTP Free World!

![Lake Powell, Utah, USA. Image by Vittoria Toso (Thinkst)]

Configured with scripts and software pushed to the device.

Apple serial numbers have a known format, and with so many devices fielded, gen-... in the fleet, and API tokens to the MDM tenant itself.

This research highlights... It is surprising that, enforcement on fetching the enrolment profile multiple times would fall to the... Even if addressed,... putting credentials in enrolment profiles and generating device-specific...

Similar to “Unveiling the Power of Intune: Into Your Cloud and On-Premise” we covered in our ’24 Q4 edition, enrolment...

![A figure showing how a...]

It at a wire carrying serial data, the data would impact the reflected RF to a separate...

The error rate of the recovered data across: stand-off distance (both line-of-sight and...

Setup, but successful data collection was performed at up to 14.5 metres (line-of-sight), or 4.5 metres when situated through multiple walls.

This work nicely fills the gap... extremely sensitive receivers and short stand-off distances, and high-power...

The power needed... is comparatively modest (less than 15W); the components are thus smaller and...

Using off-the-shelf components... While still mostly in the realm...

This work explored program analysis techniques to find classes of logic bugs written... ruption to logic flaws. GoSonar is a research tool to analyse binaries written in the Go...

Into resource exhaustion denial-of-service attacks when provided a specifically-craft-... find five new vulnerabilities in the library, each issued a CVE and patched. A single false positive highlighted some of the challenges with how Go specifically converts...

Memory corruption has dominated the bug finding and fixing landscape since the...

While this tooling only supports... safe programs, finding five novel... Expect to see more tools and techniques... attack surface of finding bugs in fielded systems.

Developer-focused tooling. VS Code has become a popular target, be it through malicious extensions, dot-files that gain command execution on project load, or tech-...

Oper-focused attacks that are starting to be seen in the wild. Beyond the IDE-specific... expand control, and malicious low-code data exfiltration techniques.

The research also highlights how VS Code has built-in capabilities to deploy and...

While few of these techniques... ![A figure showing how...]

There are few management controls... before it gets better, especially with vibe-coding VS Code forks.

IDEs are a juicy target;...

Ware or software deliverable for deployment with first-party management and SaaS.

The talk highlights a number of risks associated with the BYOC model, such as differing definitions for data sensitivity, the need to change security policies for the prod-...

As with all new deployment models, BYOC will take some time to figure out... vendor access is abused and security controls are not correctly configured (e.g.,...

At first blush,... your organisation’s cloud tenant. If done well, the model could offer better...

For products that don’t need much access... BYOC can offer more control and visibility with specific touchpoints to the main...

![Figure 15]

This talk detailed a new protocol for offering stronger authentication based on phone... for security, SMS OTPs do increase the effort needed by an attacker to compromise...

Already built standardised APIs on the carrier side to offer more functionality for device interactions. The presented Enhanced Number Verification scheme builds on...

Verification. This process doesn’t require any manual steps (like copying and pasting...). Vice logging in has SIM credentials that are mapped to a specific phone number.

There will be a long tail... insecure SMS. This solution should offer a substantial improvement in both...

Passkeys have fewer barriers to adoption... ![A flow diagram showing...]

Number Verification login flow is able to...

---

## Conclusions

Especially at the 2025 Hacker Summer Camp. We’ll be back next time!

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
