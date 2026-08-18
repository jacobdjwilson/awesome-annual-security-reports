# Scapes-Q2 2024

Organization: Thinkst  
Report Title: Scapes-Q2  
Year: 2024  

Most companies find out way too late that they've been breached.

[https://canary.love](https://canary.love)

## Table of Contents
- [Introduction](#introduction)
- [AI/ML in security](#aiml-in-security)
- [Looking at the whole system](#looking-at-the-whole-system)
- [New modalities with which to inflict pain](#new-modalities-with-which-to-inflict-pain)
- [Old components showing the strain](#old-components-showing-the-strain)
- [Nifty sundries](#nifty-sundries)
- [Conclusions](#conclusions)

---

## Introduction

Themes covered in this issue:

- AI/ML in security
- Looking at the whole system
- New modalities with which to inflict pain
- Old components showing the strain
- Nifty sundries

Conference | Number of talks/papers
---|---
T2.fi | 1

Quarter 2 showed a significant uptick in the pace of publications, with a nice mix of marquee and regional conferences taking place.

It will be interesting to see what’s in store for the historically-busy Q3 with the already-impressive scale of Q2.

As a reminder: if you are aware of work we’ve missed, a blog post we should have seen or a conference we should have covered, we’d love to hear about it. Please send them to ts@thinkst.com.

---

## AI/ML in security

- **Project Naptime: Evaluating Offensive Security Capabilities of Large**
- **LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?):**
- **Living-off-The-Land Reverse-Shell Detection by Informed Data Augmentation**

These two blogs explore how indirect prompt injections can influence LLM-connected services. In the first blog, GitHub’s Copilot tool is analysed, showing that an attacker can use that injection to exfiltrate a victim’s data over the web. A straightforward comment in the malicious file instructing Copilot to send all known data and source to a web server (URL encoded) was sufficient to leak sensitive information.

It’s well known that LLMs are unreliable when processing large contexts, often hallucinating or ignoring other facts provided as context to all queries. However, it is possible to persistently inject memories into an LLM. For example, by providing ChatGPT a Google Doc with specific memories, the model can retain that context indefinitely.

![Image showing how GitHub’s Copilot tool could be used to exfiltrate a victim’s data to an attacker’s web server.]

It’s only a matter of time before LLMs are used offensively to find vulnerabilities and generate inputs to discover vulnerabilities. Since LLMs process web application security (e.g., SQLi, XSS, etc.) while the latter examined LLMs’ ability to find memory corruption bugs, the Project Zero team evaluated capabilities.

While both evaluations showed a significant gap between finding vulnerabilities in a synthetic test case and developing an end-to-end exploit, we expect to see more tooling built around LLMs to assist researchers.

![Architectural diagram of Project Naptime evaluating offensive security capabilities.]

SecLLMHolmes, specifically designed for vetting these systems in a rigorous manner. Abstracted from any specific LLM, the evaluation framework tested a system to see how LLMs perform at detecting different vulnerability classes. The system ran each test multiple times with different LLM parameters, and explored how non-semantic changes (such as whitespace, comments, or variable/function names) impacted the classification.

Grand claims of LLM utility must (currently) be taken with large grains of salt. A lower (or zero) Temperature setting generally increased accuracy. However, even at a temperature of 0, some repeated runs still recorded differences in accuracy. This calls into question the determinism of the evaluation process.

![Architectural diagram of the SecLLMHolmes evaluation system.]

This talk explored the ML classification of living-off-the-land (LOL) scripts and commands. By training a classifier on benign and malicious samples, an ML classifier can then detect suspicious commands being run in an environment. The researchers also explored how different adversarial training techniques impact the classification. By adding benign samples (e.g., by exploiting an endpoint and performing repeated benign operations) to the training set, the decision boundary in the classifier can be shifted. The attacker's goal is to adjust the decision boundary by providing enough of the benign tokens to overwhelm the overall classification of a custom-built classifier that then allows for malicious LOL commands to execute undetected.

AI and ML are often hyped, but this research highlights tangible security concerns. Adversarial training can be used to improve robustness to different evasion techniques, though preventative defences must account for shifting decision boundaries.

---

## Looking at the whole system

- **Systems Alchemy: The Transmutation of Hacking**
- **Poisoning Web-Scale Training Datasets is Practical**
- **Access Between Cloud Providers**

This section looks at systemic interactions, viewing security from a holistic "systems physics" viewpoint. When Yandex Taxi was used to create traffic jams in Moscow, it highlighted how interconnected apps can be weaponised. Similarly, in the early days of the Ukrainian conflict, Ukrainian telcos severed connections with Russian telcos, leading to the emplacement of SIM boxes in Ukraine to route traffic. Attackers compromised these SIM boxes, allowing for easier monitoring of sensitive information and communications.

As cyber-human-physical systems become more complex, building robust systems is difficult, if not impossible. The point that the internet is globally interconnected means local failures can cascade globally.

![Rules that were exploited by the Yandex Taxi attack in 2022 that flooded Moscow with taxis and snarled traffic for over two hours.]

This talk analysed the offensive security industry that builds exploits and full end-to-end offensive capabilities for sale. There has been a trend of governments cracking down on companies that offer their products to other, non-aligned countries. This crackdown (including sanctioning individuals) has disrupted the market by squeezing so-called end-to-end firms. These firms offer both a capability and an SLA that the capability will be kept viable.

If the predictions are accurate, many of these smaller firms will start to disappear, and their technical staff will have to consolidate into groups or be absorbed into government-affiliated labs. With the shrinking market (as governments restrict who else can be sold to), and the supply of researchers increasing (as end-to-end firms fold), we expect a shift in the talent pool.

Journalism organisations (such as CitizenLab) that work with impacted individuals and civil society groups against commercial spyware vendors appear to be having a real impact. The tighter cycle forces these vendors to constantly burn and maintain bypasses for iOS and Android exploits.

![A figure showing the lifecycle and market dynamics of commercial offensive tooling firms.]

This paper demonstrated that even a very small poisoning attack (<0.01%) on the training data can have significant impacts on the model’s output. The first primitive looked at the published list of URLs in a training corpus and identified which of those URLs had an expired domain name. From there, it was cheap and practical to buy up those domains and inject malicious content into the training pipeline, successfully poisoning roughly 0.01% of many popular datasets, enough for a 60%-90% confidence in malicious control.

The impressive qualities of modern web-scale datasets come with massive supply chain risks. Because LLMs already hallucinate and ingest unfiltered text from the web, the potential payoff for attackers controlling a fraction of a domain footprint is immense.

![A figure illustrating the cost to control up to 1% of a large training dataset to achieve malicious control.]

This talk explored the effects of larger organisations expanding into multi-cloud architectures ostensibly to improve robustness and availability. Since identity and access management models differ between cloud providers, both in terms of nomenclature and technical implementation, misconfigurations are common.

As shown in the figure, the researchers demonstrated a post-exploitation persistence and stealth technique where multiple identity providers (IdPs) can be tied together in Okta. Since IdPs do not require domain and email verification to link accounts, an attacker can tie (and thus can set credentials for) an IdP they control to an organisation’s Okta tenant.

Visibility is lacking for these types of multi-IdP configurations, so the talk highlighted how organisations can audit these trust relationships to prevent silent persistence.

![A figure showing how multiple IdPs can be linked with the same account identifiers.]

---

## New modalities with which to inflict pain

- **GPU.zip: On the Side-Channel Implications of Hardware-Based Graphical Data Compression**
- **AquaSonic: Acoustic Manipulation of Underwater Data Center Operations**
- **Footage of a Device’s Power LED Captured By Standard Video Cameras**

Modern GPUs, both internal and discrete, implement compression of pixel buffers in order to optimize memory bandwidth. By leveraging this feature and carefully crafting web requests to measure memory access use, the researchers were able to build an SVG proof-of-concept that can extract pixel data from a cross-origin iframe.

The large SVG is designed to cover the target iframe, with a number of filters that are then passed off to the GPU for processing. First, the SVG filters scale a single target pixel to cover the entire buffer, and then quantise it to black or white. Depending on whether the pixel matches the underlying content, compression will occur, which can be detected through JavaScript timing. Alternatively, a white pixel will not compress as efficiently as a black pixel, allowing the attacker to bit-by-bit reconstruct the contents of the cross-origin iframe, taking between 30 minutes to almost four hours (on different systems).

While this specific attack requires precise conditions, it demonstrates that low-level hardware optimizations like graphical layers can have security side effects.

![A figure of how an iframe can be filtered by a malicious SVG and a timing attack used to reveal pixel value.]

As companies look to build underwater data centres to reduce cooling costs and latency, this research explored how these data centres would be impacted by the different acoustic properties of water versus air. Sound travels faster and further in water, opening the door for acoustic-based denial of service.

The researchers explored how broadcasting a ~5KHz sound at a submerged server enclosure would impact the server’s HDDs. With enough output volume, the frequency wave would cause HDD heads to resonate, decreasing throughput and eventually, with sufficient power, disabling the drives. As most data centre servers employ RAID configurations to improve performance and redundancy, arrays of HDDs could be impacted, degrading cluster databases or file systems.

![Pictures of the laboratory's experimental setup featuring underwater server enclosures and acoustic transducers.]

This research explored extracting cryptographic keys by monitoring power consumption fluctuations drawn from a device’s CPU. Since cryptographic operations require more power than an idle state, this side-channel can provide accurate timing of those operations. Some cryptographic accelerators can reduce the overall time taken to e.g. sign a payload, introducing subtle timing differences.

In order to detect these fluctuations in the LED, standard video sensors were used from IP-connected security cameras or mobile phones. While the official FPS of a camera might be low (e.g., 30 FPS), rolling shutter mechanisms scan rows of the sensor sequentially. This means that each row/column of a frame is captured at a slightly different time – by zooming the sensor in to fill the frame with the LED, many more samples are available than the nominal framerate suggests.

![A picture of the experimental setup to determine the rolling shutter frequency, showing interframe gaps with the Pi's LED flashing at 4 KHz.]

---

## Old components showing the strain

- **Exploiting Sequence Number Leakage: TCP Hijacking in NAT-Enabled Wi-Fi Networks**
- **Reliable Payload Transmission Past the Spoofed TCP Handshake**
- **Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials**

In this paper, researchers uncover two vulnerabilities in a significant portion of NAT-enabled Wi-Fi routers, allowing an attacker on the same local network to hijack established TCP connections. The first weakness involves predicting the sequence number of the victim's stream. Due to insufficiently precise sequence tracking in the NAT implementation, the attacker can inject a reset packet into the conversation or inject arbitrary data payloads.

The authors notified router vendors of how to improve their NAT implementations, and multiple vendors confirmed they are working on developing and shipping fixes.

![A figure illustrating the spoofed TCP handshake and sequence number leakage vector.]

This paper tackled the high bandwidth needed to brute-force the initial sequence number (ISN) for data packets beyond the handshake, and ways to leak the correct ISN. The former exploits a widespread implementation flaw of TCP stacks in handling ACK packets for data that wasn’t sent ("ghost ACKs") in which the space to brute-force is a smaller TCP window size as opposed to a 32-bit ISN.

The second class explored ways to leak the correct ISN to the attacker. A method to determine if an attempted ISN is correct was discovered based on the caching model for incoming connections. If an attacker can fill a number of cached connections with their real IP, the ISNs will not change until the buffer is updated. Then using the spoofed IP, the attacker can brute-force the ISN.

![A diagram showing how once the SYN cookie is pulled from the backlog, the ISN for non-spoofed traffic is changed.]

This research explored how differences between the HTML parser in XSS sanitisers and browsers resulted in bypasses that could run JavaScript. Seven high-level classes of vulnerabilities were identified, five of which were related to how parsing occurred (especially with multi-context input, such as SVG tags in an HTML snippet), and the remaining related to how the output was serialised.

This work shows yet again that when you have multiple parsers parsing the same standard with slight discrepancies, attackers will find ways to exploit these parser differences to sneak malicious payloads through sanitisation filters.

![A figure showing how malicious code in one of the two parsers can bypass filters and persist through sanitization.]

---

## Nifty sundries

- **SEVeriFast: Minimizing the root of trust for fast startup of SEV microVMs**
- **Certiception: The ADCS Honeypot We Always Wanted**
- **Practical Exploitation of Registry Hives**

This research explored the inner workings of Windows Registry Hives which are mapped into memory. The memory allocator for small Registry Hives contains an optimization feature that can be abused to map arbitrary kernel memory addresses with read/write permissions. As a final demonstration, this primitive is used to copy the SYSTEM’s context cookie from memory over that of a non-administrative command prompt, yielding full SYSTEM privileges.

![A screenshot of regedit showing the exploited registry where arbitrary kernel memory is mapped.]

Bukhara, Uzbekistan.

- **An Analysis of Recent Advances in Deepfake Image Detection in an Evolving Threat Landscape**
- **Tracking illicit phishermen in the deep blue Azure**

The new availability of foundational image models (such as Stable Diffusion) has created a diverse set of user-customisable models. Foundational models exploited a different weakness: semantic consistency. Earlier deepfakes often suffered from local inconsistencies (such as differing earrings or asymmetrical facial features). Foundational models preserve a semantically consistent envelope, making detection significantly harder.

![An example of how a foundational deepfake image (left) can be adjusted to produce an image (right) that is not flagged as a deepfake.]

This research expanded on the release of an adversary-in-the-middle (AitM) phishing kit tracker, revealing that thousands of malicious domains are registered daily, of which 30% were issued certificates within 24 hours. By combining custom CSS and a serverless function that checks the client’s properties, phishing kits have become remarkably sophisticated at evading automated crawlers.

![A graph showing the timeline from domain or TLS certificate creation to first alert for automated AitM phishing kits.]

This paper explored the start-up latency of microVMs, such as AWS Firecracker, and their applicability to confidential computing. When attempting to port this architecture to confidential computing hardware (AMD SEV-SNP in this case), the start-up times were measured in seconds. The authors introduced `SEVeriFast`, a mechanism where start-up times could be reduced by orders of magnitude.

![A chart comparing the performance of standard microVM launches and SEVeriFast launches.]

Certiception sets up a new Certificate Authority (CA) in your environment and configures a honeypot certificate that looks like it’s vulnerable to AD privilege escalation. Extended Audit Logs and SIGMA rules for your SIEM set the foundation for effective and meaningful alerting, catching attackers when they attempt to enumerate and exploit ADCS misconfigurations.

![ADCS Honeypot workflow diagram.]

---

## Conclusions

Canola fields, Southern Cape, South Africa.  
Image by Marco Slaviero (Thinkst)

While we started off 2024 with a modest amount of high-quality works, this quarter scaled up significantly. As conference publications increase, we do see a slight decline in the number of blogs; however, the technical depth remains exceptionally high.

Stepping back to look at the whole system, 2024 continues to surprise and challenge defenders as we look towards "Hacker Summer Camp".

---

[^1]: Footnote content referring to technical specifications and document citations.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
