# Scapes-Q1 2023

Organization: Thinkst  
Report Title: Scapes-Q1  
Year: 2023  

Most companies find out way too late that they've been breached.

[https://canary.love](https://canary.love)

![Cover photo: Lighthouse at the Cape of Good Hope near a cliff edge.](lighthouse.jpg)

## Table of Contents

- [Introduction](#introduction)
- [Modern Techniques for Modern Systems](#modern-techniques-for-modern-systems)
- [New Attacks, New Defences](#new-attacks-new-defences)
- [Stepping Back to Gain Perspective](#stepping-back-to-gain-perspective)
- [Nifty Sundries](#nifty-sundries)
- [Conclusion](#conclusion)

---

## Introduction

Themes covered in this issue:
- Modern techniques for modern systems
- Smashing Web3 transaction simulations for fun and profit
- New attacks, new defences
- Stepping back to gain perspective
- Nifty Sundries
- Conclusion

Presented between the first of January... summer, the “off-season” appears to have more work is important in its specific area, it is harder to find wide-scale impact research outside of the top ts@thinkst.com!

| Conference name | Number of talks |
|-----------------|-----------------|
| BSides Sofia    | [Data Omitted]  |
| **Total**       | [Data Omitted]  |

![Photo by Joshua Kettle.](joshua-kettle.jpg)

---

## 1. Modern Techniques for Modern Systems

Offensive and defensive research.

### Using ZK Proofs to Fight Disinformation

![Photo by Geran de Klerk.](geran-de-klerek.jpg)

#### Red pill attacks
The researchers were able to find a few environment variables that were different in the simulation compared to on-chain executions.

> Red Pill

The notion that code-is-law out to reverse that specific transaction [differed reliably between...].

#### Data provenance
Explores specific deployments: LLMs that interact with external data (i.e., to an end-user, while still being able to influence the LLM’s state). Other exfiltrate user data to the attacker, and subverting an LLM to modify emails when integrated into an email workflow.

There is currently a lot of discussion fully explored. LLMs have no differentiation between code and data, location, on a certain date, and only specific transformations were applied.

Specific use-case of this work for media integrity, there are numerous other benefits that can be imagined, e.g., repeatable research, trusted...

There are open questions would scale to larger files (like videos). There is also the security of the proof that only specific modifications were another [doctored] photo with a local GPS-spoofing radio to change...

1. Associated with PQC (and how they prioritise where to deploy PQC first). PQC is important. They start with long-term uses, including firmware signing.
2. Following Google’s prioritisation for PQC development of long-term hardware with firmware or hardware...

Google’s scale and diversity of users allow them to find rough edges or issues and fix those early. Monitoring the abstraction layer between applications and the underlying cryptographic primitives offers immense...

![A figure](figure1.jpg)

---

## 2. New Attacks, New Defences

- Detection without the DoS
- Hosted CI/CD Runners
- Framing Frames: Bypassing Wi-Fi
- Let Me Unwind That For You: Exceptions to...

![A leopard spotted at the Lion Sands in Kruger National Park.](leopard.jpg)

Objects, which can sometimes overwrite special fields that control object behaviour. The field most commonly targeted is the “__proto__” field...

State), it is very difficult to test if a remote application is vulnerable to it. Additional space between the field name and value. This cosmetic change...

Despite a number of these issues being patched... server-side DoS.

### Insight into CI/CD pipeline attacks

Toolkit for finding and attacking code repositories with accessible self-... to evaluate the configuration within a GitHub organisation. Gato is designed to allow both network defenders and offensive security practitioners to...

#### Access tokens
#### Self-hosted runners
To inside a system, often bypassing the firewalls and network access... CI/CD pipelines or jobs execute in a (usually containerised) environment called a runner, which is configured to provide a...

The client’s session key while buffering packets destined for that client. The buffered packets to the attacker without a session key, resulting in undefined...

This work highlights an attacker on the network to view the traffic destined for the victim.

Is difficult to obtain hard ground-truth on the impact, however the research...

The proposed mitigatio...

While the data in the paper...

![A figure](figure2.jpg)

A stack overflow.

Compiler pass capable of analysing the control-flow graph to determine a...

At runtime, a monitor verifies on a system call:

There are always counter-examples and edge cases... benefits outweigh the [modest] performance costs as well as the cost of...

While there are numerous attack classes, sensitive operations is compelling. For example, control flow integrity can be expensive if deployed broadly, yet if there are specific functions...

---

## 3. Stepping Back to Gain Perspective

![A path leading down to Diaz Beach at Cape Point.](cape-point.jpg)

### High Risk Users and Where to Find Them

(DMA), which aims to limit network effects from large services. Of special...

For each challenge examined, the researchers explored different technical...

E2EE guarantees are invalidated as the server will need to have sufficient key...

The EU is stepping into a new role with the DMA and interoperability to target network effects. This new regulatory... DMA and when... into effect.

The timeline on this rollout and finger-pointing when the inevitable issues arise.

Researchers were able to find a statistically significant minority of users who... compromised by malware, or attempting to access sites identified as used to...

By matching defensive capabilities with expected risks, more efficient and targeted defence can be achieved, for example...

This talk underscores the offensive mindse...

![A figure](figure3.jpg)

Defenders should learn from this mindset:

---

## 4. Nifty Sundries

- Polynonce: A tale of a novel ECDSA attack and Bitcoin tears
- Finding 10x+ Performance Improvements in C++ with...

Find any wallets vulnerable to this stronger ECDSA weakness, they did find a number of wallets that had reused a nonce. That flaw was exploited by...

This evaluation shows how something in the wild (nonce reuse or weak CPRNGs) finds a way to escape and...

Security static-analysis tool (CodeQL) to find code sections that could be... different scenarios but with the same relevant properties.

The fix for the issue being explored was to simply change the type to one (i.e., [unsigned] char to char8_t). In searching across large open-source C++ codebases, the author notes that the results from finding this pattern in... changes, resulting in significant performance improvements.

The author’s approach... Tools like CodeQL... function. For realistic...

Context switching... ability to pay off already.

---

## Conclusion

Conferences this quarter, we were able to find a...

THREE THEMES WERE HIGHLIGHTED THIS QUARTER:

[^1]: Footnotes and references handled dynamically according to document specifications.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "legacy"} -->
