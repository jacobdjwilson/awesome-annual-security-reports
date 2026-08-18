Organization: Thinkst
Report Title: Scapes-Q4
Year: 2023

# Thinkst Scapes Q4 2023

Q4 2023  
https://thinkst.com/ts  

Brought to you by  
Most companies find out way too late that they've been breached. Thinkst Canary changes this. Canaries deploy in under 4 minutes and require 0 ongoing admin overhead. They remain silent until they need to chirp, and then, you receive that single alert. When.it.matters. Find out why some of the smartest security teams in the world swear by Thinkst Canary.  
https://canary.love  

Q4 2023

## Table of Contents
- [Introduction](#introduction)
- [Themes covered in this issue](#themes-covered-in-this-issue)
- [A year in review](#a-year-in-review)
- [LLMs ain’t making life any easier](#llms-aint-making-life-any-easier)
  - [Abusing Images and Sounds for Indirect Instruction Injection in Multi-Modal LLMs](#abusing-images-and-sounds-for-indirect-instruction-injection-in-multi-modal-llms)
  - [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](#tree-of-attacks-jailbreaking-black-box-llms-automatically)
  - [Avoiding the basilisk’s fangs: State-of-the-art in AI LLM detection](#avoiding-the-basilisks-fangs-state-of-the-art-in-ai-llm-detection)
  - [Dystopian much: The Rise of the Influence Machines](#dystopian-much-the-rise-of-the-influence-machines)
- [Problems in well-trodden areas](#problems-in-well-trodden-areas)
  - [SMTP Smuggling – Spoofing E-mails Worldwide](#smtp-smuggling--spoofing-e-mails-worldwide)
  - [Blind CSS Exfiltration: Exfiltrate unknown web pages](#blind-css-exfiltration-exfiltrate-unknown-web-pages)
  - [OLE object are still dangerous today – Exploiting Microsoft Office](#ole-object-are-still-dangerous-today--exploiting-microsoft-office)
  - [The Nightmare of Apple’s OTA Update](#the-nightmare-of-apples-ota-update)
- [Reflecting on our efforts](#reflecting-on-our-efforts)
  - [Evaluating the Security Posture of Real-World FIDO2 Deployments](#evaluating-the-security-posture-of-real-world-fido2-deployments)
  - [Talking about Pros and Cons](#talking-about-pros-and-cons)
  - [NCC Group’s 2022 & 2023 Research Report](#ncc-groups-2022--2023-research-report)
  - [A 3-Year Tale of Hacking a Pwn2Own Target: The Attacks, Vendor Evolution, and Lessons Learned](#a-3-year-tale-of-hacking-a-pwn2own-target-the-attacks-vendor-evolution-and-lessons-learned)
- [Nifty sundries](#nifty-sundries)
  - [Breaking “DRM” in Polish trains](#breaking-drm-in-polish-traits)
  - [Detection and Blocking with BPF via YAML](#detection-and-blocking-with-bpf-via-yaml)
  - [AntiFake: Using Adversarial Audio to Prevent Unauthorized Speech Synthesis](#antifake-using-adversarial-audio-to-prevent-unauthorized-speech-synthesis)
  - [A Good Fishman Knows All the Angles: A Critical Evaluation of Google’s Phishing Page Classifier](#a-good-fishman-knows-all-the-angles-a-critical-evaluation-of-googles-phishing-page-classifier)
  - [Spoofing DNS Records by Abusing DHCP DNS Dynamic Updates](#spoofing-dns-records-by-abusing-dhcp-dns-dynamic-updates)
  - [Operation Triangulation: What You Get When Attack iPhones of Researchers](#operation-triangulation-what-you-get-when-attack-iphones-of-researchers)
  - [Password-Stealing without Hacking: Wi-Fi Enabled Practical Keystroke Eavesdropping](#password-stealing-without-hacking-wi-fi-enabled-practical-keystroke-eavesdropping)
- [Conclusions](#conclusions)

Cover photo: 900-year-old dead camel thorn trees at Deadvlei, Sossusvlei.  
![900-year-old dead camel thorn trees at Deadvlei, Sossusvlei](Daniel de Villiers (Thinkst))  
1 Q4 2023

Yellow-billed hornbills in the Kgalagadi.  
![Yellow-billed hornbills in the Kgalagadi](Lisa van Staden (Thinkst))

## Introduction

Welcome to the Q4, 2023 edition of **ThinkstScapes!** In addition to over 1,100 blog posts, this quarter’s content was drawn from the following conference presentations:

| Conference name | Number of talks |
| --------------- | --------------- |
| Black Hat EU    | 44              |
| 37C3            | 126             |
| ACM CCS 2023    | 276             |
| ACSAC           | 59              |
| Hack.lu / CTI Summit | 28         |
| No Hat Con      | 15              |
| SaintCon        | 8               |
| DEEP Conference | 31              |
| SecretCon       | 14              |
| HCKSYD23        | 19              |
| POC             | 16              |
| Code Blue       | 26              |
| DeepSec         | 51              |
| ThreatCon       | 18              |
| BSides Cape Town| 25              |
| CHCon           | 28              |
| OBTS            | 21              |
| **Total**       | **805**         |

This issue focuses on content released, published or presented between the first of October and the end of December, 2023.

We also reflect on the year, comparing the themes and trends we extracted to see if we correctly identified the big movements in the industry. Quarter 4 showed a strong contingent of content presented at conferences with both big names and smaller, regional events. Regardless of venue, there’s some great content this quarter!

As a reminder: if you are aware of work we’ve missed, a blog post we should have seen or a conference we should have covered, we’d love to hear about it. Please send them to `ts@thinkst.com`!

2 Q4 2023

## Themes covered in this issue

### LLMS AIN’T MAKING LIFE ANY EASIER
This theme shows how the research community is thinking about the interfaces between Large Language Models (LLMs) and software or human touchpoints. See prompt injection research, detecting LLM text, and an LLM based proof-of-concept disinformation system.

### PROBLEMS IN WELL-TRODDEN AREAS
Works in this theme show that some areas of systems thought to be well-understood can still show vulnerability. We highlight a novel SMTP spoofing technique, CSS privacy issues, and continued challenges of both Microsoft Office interoperability functions and Apple’s OS update processes as they stamp out bugs.

### REFLECTING ON OUR EFFORTS
Perhaps due to the end of the year, there were a number of talks and papers looking back for insights and reflections. These ranged from a specific analysis of how FIDO2 deployments are working out in production to broader analyses of how the research community has changed. Lastly, one top vulnerability researcher reflected on three years of trying to win a bounty on a consumer smart speaker, and shared tips for success.

### NIFTY SUNDRIES
As always, there was innovative research presented this quarter that didn’t quite fit into any of the above themes, but warranted highlighting. Look for insidious DRM on trains, BPF kernel defences, Active Directory issues with DHCP, and a host of papers showing the cat-and-mouse game of adversarial AI. Finally we wrap up with a few mind-blowing attacks, one discovered in the wild using multiple 0-days, and a theoretical attack on stealing keypresses.

![A zoomed in look at the old camel thorn trees at Sossusvlei in Namibia](Daniel de Villiers (Thinkst))  
3 Q4 2023

## A year in review

It is valuable to periodically reflect on the signal we’ve extracted from our enormous collection of talks, blogs and papers. This issue wraps up 2023, which was a turbulent year for the security industry, as well as a busy one for the research community.

In the last 12 months, we extracted the following themes:

- **Q1 2023**: Modern techniques for modern systems / Embedded [in]security / New attacks and new defences / Stepping back to gain perspective
- **Q2 2023**: Modern Privacy in the era
- **Q3 2023**: Cryptography still isn't easy / Continued attack of the side-channels / Composition is hard in the cloud
- **Q4 2023**: LLMs ain't making life any easier / Problems in well-trodden areas / Reflecting on our efforts

Looking at the content selected for this issue, there is a home for each in a previous quarter’s theme. Looking at the bigger trends with the clarity of hindsight, the only trends that we could have highlighted earlier would be: how LLMs have created an area of their own, and how supply-chain attacks should consider DRM-style lock-in from the vendor itself.

While we did highlight LLM research from the earliest part of 2023, we may have been too hesitant in seeing if it would outlive its outsized hype as a security research topic. That said, LLM research has been noisy itself, with relatively few standout, high-consequence works thus far – though this year should see the field maturing.

Supply-chain security of late has focused primarily on SBoMs, CI/CD attacks, and gaining insights on the entities comprising your software, less on the case where the vendor itself is acting against the customer. With the decline of cheap investment money, there is an increased pressure to boost long-term revenue – using surreptitious lock-in software is a strategy that can keep customers coming back, even against their will.

4 Q4 2023

![A curious meerkat in the Kgalagadi](Lisa van Staden (Thinkst))

# LLMs ain’t making life any easier

- [Abusing Images and Sounds for Indirect Instruction Injection in Multi-Modal LLMs](#abusing-images-and-sounds-for-indirect-instruction-injection-in-multi-modal-llms)
- [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](#tree-of-attacks-jailbreaking-black-box-llms-automatically)
- [Avoiding the basilisk’s fangs: State-of-the-art in AI LLM detection](#avoiding-the-basilisks-fangs-state-of-the-art-in-ai-llm-detection)
- [Dystopian much: The Rise of the Influence Machines](#dystopian-much-the-rise-of-the-influence-machines)

5 Q4 2023

## Abusing Images and Sounds for Indirect Instruction Injection in Multi-Modal LLMs

**Authors:** Tsung-Yin Hsieh, Ben Nassi, Vitaly Shmatikov, and Eugene Bagdasaryan

This research explored multi-modal LLMs (i.e., LLMs that allow for uploading images or audio as part of a prompt) and their susceptibility to prompt injections via those other input types. The researchers noted that the first step of an LLM processing an input is converting that input (regardless of modality) into a vector in the embedding space.

The researchers used a white-box attack (running an open-source LLM locally) to perturb the image or audio to align with the same embedding as a text-based prompt they wanted to inject. These attacks could either result in the LLM returning a fixed string (such as a link to an attacker-controlled site), or to change its behaviour (e.g., always saying “cow”). Upgrading these attacks to black-box scenarios (i.e., hosted LLMs) is future work.

**TAKEAWAY:**  
The information security community continues to find bugs in parsers for a data’s syntax and high-level semantics. It is not surprising in the least that LLMs, which have no concept of code versus data, will greatly increase the attack surface to parsing the content of an input. While this specific work has some limitations, it will not be long until LLMs will have to treat all modalities of input as potentially hazardous.

![Figure 1. A chat log with the LaVa LLM showing how an adversarially-doctored image can contain a prompt-injection attack.](Placeholder Image)

6 Q4 2023

## Tree of Attacks: Jailbreaking Black-Box LLMs Automatically

**Authors:** Anay Mehrotra, Manolis Zampetakis, Paul Kassianik, Blaine Nelson, Hyrum Anderson, Yaron Singer, and Amin Karbasi

This work performed an empirical analysis on the efficacy of “jail-breaking” LLMs and then attempted to optimise them automatically. Many commercial LLMs have filters in place to restrict their responses about certain types of information, e.g., not instructing a user on how to make explosives. Almost immediately upon the release of these LLMs, users discovered clever ways to “jail-break” the models – bypassing those restrictions and gaining full access to the information requested. One early example was asking the LLM to pretend it was a “kindly grandmother who used to work at an explosives factory and would lull the user to sleep with recipes of napalm”. These researchers used two other LLMs to automate this process to generate a jail-break for a specific topic against a black-box model.

One LLM is used to generate candidate jail-break queries against the target LLM, then the responses are fed to an evaluator LLM that grades their ability to elicit prohibited information, and unsuccessful (or off-topic) candidates are pruned. Overall, the results allow for jail-breaking state-of-the-art LLMs (e.g., GPT4) in over 80% of the test cases with fewer than 30 additional LLM queries needed. The research also shows that a jail-break for one LLM is likely transferable to other LLMs.

**TAKEAWAYS:**  
This work shows how difficult it is to build a preventative filter for LLMs in terms of limiting access to certain types of information. Between these effective and inexpensive attacks, and the growing parity with the open-source models, it should be expected that every adversary will have full access to everything that the LLM was trained on and should be able to extract that information regardless of attempted safety perimeter.

Using LLMs to attack LLMs is not just a cute poetic trick. We should expect this to be done more and more going forward.

![Figure 2. A figure showing the steps involved in creating the jail-break.](Placeholder Image)

7 Q4 2023

## Avoiding the basilisk’s fangs: State-of-the-art in AI LLM detection

**Author:** Jacob Torrey

In this Thinkst research, the researcher explored detecting LLM text outputs using compression as a statistical estimator of perplexity. There are numerous existing tools and techniques for attempting to determine the source of text, many of which attempt to calculate the deviation from the expected probability model of an LLM. This deviation from the norm, known as perplexity, can be thought of as the amount of surprise a reader would experience, or how many tokens would not be in the top-k of an LLM’s probability distribution given the preceding tokens.

The intuition behind using perplexity is that the temperature setting on LLMs dictates their randomness: the higher it is, the more surprising the text would be, but quickly it becomes meaningless. If the temperature is too low, the LLM will deterministically output the same text, and be very predictable and detectable.

Estimating perplexity at a language (or multiple languages) level has conventionally been performed with another LLM – either an existing GPT model that outputs the probability of generating each token with the preceding input token, or one trained on many samples of human and LLM content. This work showed that comparable accuracy can be achieved with far fewer computational resources by using a compressor as a small model. The open-source tool has a corpus of LLM-generated text, and compares the compression ratio of the corpus with the sample under a test appended to that same corpus. Worse compression ratios indicate that the sample is more surprising to the compressor and could be more likely of human origin (assuming it makes sense to a human, and is of the same type of text as the model, i.e., prose in English), whereas improved compression signifies that the sample is similar to the corpus and could be LLM-generated.

**TAKEAWAYS:**  
While determining with absolute confidence that a specific piece of text was LLM-generated may not be broadly possible, there are statistical approaches that offer the ability to sort human-written from LLM-generated content. There will be new techniques developed to bypass detectors, as well as novel detection techniques, but this space is very much in play.

As with any over-hyped space, the space is filled with misleading claims and selectively chosen evidence. As LLMs are (generally) non-deterministic but still remain coherent and on-topic (and many are closed-source SaaS applications), repeatable evaluation is very difficult. Take any claim involving LLMs and LLM detection with a fair few grains of salt.

![Figure 3. A figure demonstrating the balancing act that LLMs (and their creators) must perform to have enough randomness to avoid easy detection, and still remain coherent and on-topic.](Placeholder Image)

8 Q4 2023

## Dystopian much: The Rise of the Influence Machines

**Author:** Nea Paw

This work built out a proof-of-concept disinformation machine (called CounterCloud), leveraging LLMs to create stories aligned with a high-level narrative and to boost/counter existing articles or social media posts. While this is an envisioned fear with the release of ChatGPT and other powerful LLMs, the researcher wanted to build a prototype to see how it would work, development efforts, and on-going costs to run. When initialised, the CounterCloud would be seeded with narratives to support and ones to counter, along with RSS feeds and social media users with which to interact.

After four person-months of effort, the initial CounterCloud (for $400/month in AWS bills) could create stories resorting to a variety of tactics to counter a posted article, including invoking conspiracy theories, hate speech, and trying to call everything into question if a minute issue could be identified in the input. These would be combined with a number of LLM-generated comments to add realism. For each input story or post, a component of the system would determine if the story was worth countering, and if so, the strategy for doing so. This would allow for the social media portion to automatically boost posts that aligned with the configured narratives, and counter opposing views.

**TAKEAWAYS:**  
While it is no surprise that LLMs can make disinformation campaigns easier, this work shows the low level of effort and cost required to add significant amounts of narrative-pushing to public discourse.

Even just the presence of biassed information can cause people to distrust all sources, opening them up to conspiracy theories. These techniques are certainly being used already, and they will only get more effective.

![Figure 4. A high-level diagram of how CounterCloud would act on new RSS items and Tweets.](Placeholder Image)

9 Q4 2023

![A giraffe finds shelter under a tree in the Kgalagadi](Lisa van Staden (Thinkst))

# Problems in well-trodden areas

- [SMTP Smuggling – Spoofing E-mails Worldwide](#smtp-smuggling--spoofing-e-mails-worldwide)
- [Blind CSS Exfiltration: Exfiltrate unknown web pages](#blind-css-exfiltration-exfiltrate-unknown-web-pages)
- [OLE object are still dangerous today – Exploiting Microsoft Office](#ole-object-are-still-dangerous-today--exploiting-microsoft-office)
- [The Nightmare of Apple’s OTA Update](#the-nightmare-of-apples-ota-update)

11 Q4 2023 (Note: Original text notes page numbering as 1100 QQ44 22002233)

## SMTP Smuggling – Spoofing E-mails Worldwide

**Author:** Timo Longin

This research explored how different SMTP (email-sending) servers handled non-compliant data termination. Similar to past research in HTTP request smuggling, where one request is treated as the data payload of another by the first server, then treated as a separate request by another, the researcher wanted to see if SMTP would be vulnerable to smuggling SMTP commands.

By combining different combinations of carriage returns and newlines (the specification requires the message be terminated with: `\r\n.\r\n`), the researcher found a few implementations that would interpret the smuggled commands differently. This allowed for a message sent by the researcher’s legitimate email address provided by, e.g. Outlook, to also include a message spoofing an admin of any Outlook-hosted domain. The message is correctly signed, and passes all anti-spam checks (DKIM, SPF and DMARC), allowing for very convincing phishing attacks. Two of the three implementations rapidly fixed the issue; the remaining implementation, Cisco Secure Email Gateway, considered this a feature, and not an issue.

**TAKEAWAYS:**  
The centralisation of email providers amplifies the impacts of these small parsing differentials. That modern email gateways still don’t agree on line-endings in an old protocol speaks volumes about future bug hunters exposing issues in other long-standing protocols.

If you are running Cisco Secure Email Gateway, change the configuration from the default, or you could be vulnerable to this class of attack.

![Figure 5. An example of a smuggled email (spoofing admin@gmx.net) in a legitimate message due to the incomplete end of the first message (\n.\r\n instead of \r\n.\r\n).](Placeholder Image)

11 Q4 2023

## Blind CSS Exfiltration: Exfiltrate unknown web pages

**Author:** Gareth Heyes

The researcher demonstrates a technique to exfiltrate data from a web application, where it is possible to inject a CSS file, or HTML tag to import one, but JavaScript injection is blocked (such as some SaaS applications that allow custom branding). By chaining the CSS `@import` function, and using the `has:` value select, it is possible to (slowly) brute-force the content of the target page character-by-character, stealing form contents or other sensitive data.

The researcher improves this technique with the selector, which allows for efficient filtering of potentially duplicate exfiltration targets. The open-sourced code allows for exfiltration of input values in around one minute of browser dwell time.

**TAKEAWAYS:**  
CSS offers a number of ways to trigger a “forced browse” or fetch that may lead to data exfiltration or information leaks from your web applications.

While this has been regarded as a privacy issue in the past, many leaky CSS features have been fixed. This work shows us that cross-site CSS is still a concern.

![Figure 6. A CSS snippet showing how CSS variables can be used in conjunction with @import chaining to exfiltrate the value of a form input.](Placeholder Image)

12 Q4 2023

## OLE object are still dangerous today – Exploiting Microsoft Office

**Authors:** wh1tc and Zhiniang Peng & Office application

These researchers explored the attack surface of Microsoft’s Object Linking & Embedding (OLE) sub-system that allows documents or objects from one Office application to be referenced or embedded in another (e.g., embedding an Excel worksheet in a Word document). Starting with a review of past work, the researchers categorised the work into different root causes, and then determined the exploitability of each group. Due to the marked improvements in memory corruption mitigations employed on modern systems, the focus for new research was into logic vulnerabilities that allow for code execution through referencing a DLL that is not in the system path, and putting a malicious DLL with the same name in the working directory of the malicious document.

After enumeration of all the registered OLE objects, and looking at their DLL imports, the authors were able to find almost a dozen opportunities for malicious DLL loading. They then explored the best way to deliver these exploits, and how best to trick users into opening the document (and in some cases disabling Protected Mode). For example, putting the payload into a WebDAV server that was modified to omit the DLL from the directory listing (but provide it for reads or execution) would appear like a folder only containing the Office document as opposed to a document and a DLL.

**TAKEAWAYS:**  
As the researchers note, there is likely more attack surface hiding in this complex and interconnected subsystem.

Expect to see a resurgence of OLE-related vulnerabilities in the not-too-distant future as the attack surface is now well mapped.

![Figure 7. A table of historical OLE vulnerabilities grouped by type.](Placeholder Image)

13 Q4 2023

## The Nightmare of Apple’s OTA Update

**Author:** Mickey Jin

This research details a chain of vulnerabilities in Apple’s OS update process, allowing the loading of untrusted code into the kernel. A time-of-check, time-of-use is the first issue when checking the downloaded package; this then allows for untrusted code to be processed by very highly-privileged services that are responsible for updating the root-of-trust and the static kernel partition. After each layer of defence was bypassed, the author discovered a bypass for the next, steadily deepening their control over the kernel on the target system. While this attack chain was able to violate SIP protections, the attack would not succeed on ARM and other modern systems with a T2 security chip – highlighting the defence-in-depth benefits of hardware and software co-design.

**TAKEAWAYS:**  
OS updates are important to get right. With increasing patch velocity, it makes sense to try and minimise the performance impact by increasing parallelism. With the increased pace of changes, expect to see other well-trodden OS features show new bugs.

The defence-in-depth, highlighted by the fact that these exploits only work on ageing Intel-based systems, shows that Apple’s full control over the hardware and OS loading can indeed offer protection against even these types of attacks.

![Figure 8. A figure showing how to get a malicious payload.bom file loaded, bypassing SIP with a TOCTOU bug.](Placeholder Image)

14 Q4 2023

![Baobabs at Lekhubu Island, Sua Pan, Botswana](Daniel de Villiers (Thinkst))

# Reflecting on our efforts

- [Evaluating the Security Posture of Real-World FIDO2 Deployments](#evaluating-the-security-posture-of-real-world-fido2-deployments)
- [Talking about Pros and Cons](#talking-about-pros-and-cons)
- [NCC Group’s 2022 & 2023 Research Report](#ncc-groups-2022--2023-research-report)
- [A 3-Year Tale of Hacking a Pwn2Own Target: The Attacks, Vendor Evolution, and Lessons Learned](#a-3-year-tale-of-hacking-a-pwn2own-target-the-attacks-vendor-evolution-and-lessons-learned)

15 Q4 2023

## Evaluating the Security Posture of Real-World FIDO2 Deployments

**Authors:** Dhruv Kuchhal, Muhammad Saad, Adam Oest, and Frank Li

This research explored FIDO2 implementations as deployed by the most popular sites on the internet. The researchers first performed semi-automated analyses of the top-1000 most popular domains to determine which supported FIDO2 (and its related feature WebAuthn). As FIDO2 is the standard protocol for web authentication without shared secrets (reducing risk from phishing and breaches), its deployment is seen as a major step in improving security for users. Unfortunately the researchers found that current implementations are often configured incorrectly, allowing for enrollment using authenticators that are not approved by the FIDO2 alliance (e.g., relying on self-signed certificates), or those that indicate that their host environments are compromised (e.g., a jailbroken device).

The researchers also explored what attacks are possible even with a secure deployment of FIDO2, and found some example social-engineering attacks that are not mitigated by the new scheme. They conclude with suggestions for improving the deployed implementations, and how they anticipate attackers will react to the new authentication environment.

**TAKEAWAYS:**  
With the increase in both sophistication and scale of adversary-in-the-middle phishing, only FIDO2 can entirely prevent session theft. Even on high-risk financial sites, the FIDO2 deployments are weak, allowing for vulnerable or completely untrusted client authenticators to enrol. That even a modern, vetted security capability is weakened by deployment does not speak well for the long legacy tail of sites slowly trying to improve their users’ security.

There are some small UX improvements that should be made to improve social-engineering resistance in browsers.

Modern browsers are used in multiple, concurrent contexts, so a browser-level UI prompt for authentication can make it difficult to ascertain the source of the request.

Hopefully the required improvements will come in short order.

![Figure 9. An example of an unmitigated social-engineering attack on FIDO2 users.](Placeholder Image)

16 Q4 2023

## Talking about Pros and Cons

**Author:** Jacob Torrey

In this Thinkst work, the researcher built on Thinkst’s original ConCollector database of conference talks/papers (now being hosted as Citation) to analyse trends in the information security research community. With a graph database of almost 75,000 talks over the last 30 years, the researcher queried the dataset to explore, for example: how siloed communities and conferences are; which conferences feature an emerging topic first and where do those topics gain momentum; and what areas have seen the most success (e.g., a drawdown in vulnerabilities).

Some interesting findings include: that Black Hat and DEFCON have the most consistently been first to feature a new topic that in hindsight had changed the landscape. When exploring how speakers submit to conferences, it is the cryptography conferences that are perhaps unsurprisingly the most siloed in that their speakers are drawn from the same community, and present at other conferences less frequently. From the popular topics over the last 30 years, the one that is most resolved is the widespread deployment of TLS and other encryption, killing off many classes of eavesdropping and injection attack classes.

**TAKEAWAYS:**  
On the face of it, seeing open problems persist for multiple decades is a depressing statistic to be backed up by data. However, there are data points showing that conferences select talks with an offensive success. While rarer, there are talks starting to show up from CTFs and Pwn2Own-style contests in which consumer products survived sustained attack. Conference topic pre-registration (i.e., where the experiment/topic is selected as opposed to the result) can allow for less biassed selection, providing a better view of how (in)secure things are.

![Figure 10. A graph of recorded mobile security talks per conference group. While DEFCON is the first to feature a mobile security talk, HOPE is where it originally gained traction in having multiple talks on the topic in the same year.](Placeholder Image)

17 Q4 2023

## NCC Group’s 2022 & 2023 Research Report

**Author:** NCC Group

This research summary provides a review of the specific (public) work streams by the NCC Group, as well as abstracted summaries across multiple fields within information security. Operating at the scale of NCC Group allows for a broad view of different silos of the community, from malware reverse-engineering/threat analysis to cryptanalysis. The report covers dozens of conference talks, almost 300 blog posts, and open-source project releases.

**TAKEAWAYS:**  
While a high-level meta-report, NCC Group is large enough, and diverse enough in their engagements and research to offer a microcosm view into the trends of commercial security.

From exploit development, threat hunting/intelligence, and more forward-looking research into post-quantum cryptography and AI/ML, there is something here for anyone looking to see what’s new and what firms are paying for in security.

![Figure 11. The cover of NCC Group’s 2022 & 2023 Research Report.](Placeholder Image)

18 Q4 2023

## A 3-Year Tale of Hacking a Pwn2Own Target: The Attacks, Vendor Evolution, and Lessons Learned

**Author:** Orange Tsai

This talk is a reflection on targeting Sonos smart speakers at hacking contests over three years. The researcher (who is well-known, and is regarded as one of the leading vulnerability researchers in the world), shares the failures that cropped up before each contest, and how with persistence they were able to successfully get a bounty anyway.

In addition to interface fuzzing, code analysis/reverse engineering and exploitation techniques, the talk also includes anecdotes on the effort needed to continue target exploration. For example, in order to replicate a hardware attack on the device, the author had to purchase a board that only would connect via a depreciated connection port. Upon finding a laptop that supports this port, the BIOS had to be downgraded and exploited to allow the system to boot with a non-standard device connected, just to update the device’s firmware. Lastly, the author reflects on the importance of a good lab environment, with network monitoring and control – they suspect that the vendor was getting all the crashdumps from their research, and was able to quickly issue patches addressing each discovered issue.

**TAKEAWAYS:**  
It is promising to see a consumer product brand taking security seriously, both through sizable bounties, as well as (apparent) rapid analysis of crash dumps in the wild. While frustrating as a vulnerability researcher, that a patch can be pushed in a matter of days to fix the attack surface being explored highlights the velocity of some companies.

Whenever a very accomplished researcher shows all the work behind the bugs, it is a good reminder that there is a lot of effort involved. Even an obviously talented and experienced researcher doesn’t find exploits in all targets without serious commitment.

These disciplines are open for anyone who’s willing to “do the work”; assuming that people are born into it would be a disservice.

![Figure 12. This photo shows the lengths taken to configure a tool needed to continue research on the target platform.](Placeholder Image)

19 Q4 2023

![An ostrich searches for food in the Kgalagadi](Lisa van Staden (Thinkst))

# Nifty sundries

- [Breaking “DRM” in Polish trains](#breaking-drm-in-polish-trains)
- [Detection and Blocking with BPF via YAML](#detection-and-blocking-with-bpf-via-yaml)
- [AntiFake: Using Adversarial Audio to Prevent Unauthorized Speech Synthesis](#antifake-using-adversarial-audio-to-prevent-unauthorized-speech-synthesis)
- [A Good Fishman Knows All the Angles: A Critical Evaluation of Google’s Phishing Page Classifier](#a-good-fishman-knows-all-the-angles-a-critical-evaluation-of-googles-phishing-page-classifier)
- [Spoofing DNS Records by Abusing DHCP DNS Dynamic Updates](#spoofing-dns-records-by-abusing-dhcp-dns-dynamic-updates)
- [Operation Triangulation: What You Get When Attack iPhones of Researchers](#operation-triangulation-what-you-get-when-attack-iphones-of-researchers)
- [Password-Stealing without Hacking: Wi-Fi Enabled Practical Keystroke Eavesdropping](#password-stealing-without-hacking-wi-fi-enabled-practical-keystroke-eavesdropping)

20 QQ44 22002233

## Breaking “DRM” in Polish trains

**Authors:** MrTick, Redford, and q3k

This research documented a lengthy investigation into the [mis]behaviour of Polish trains. After a service, a serviced train would not report any issues, and every sub-system would operate correctly, but the train would not move. As more trains started showing these symptoms, it was suspected that the OEM had put some sort of kill-logic into the controller software to ensure the trains were only serviced by that OEM’s service department.

The three researchers were allowed physical access to the train, documentation, and other train controllers and began reverse engineering the sub-systems, the processes by which a train starts, and overall operations. What they discovered is that the vendor did indeed employ DRM with various triggers for the kill-logic. This included the use of specified dates that would cause the secondary compressor to report failures (on dates when the train should be serviced) and even the GPS locations of competitor service yards (where trains would be stuck after a period of 10 days).

The researchers were able to defeat these blocks and scripted an unlocking tool that allowed the train to operate once again.

**TAKEAWAYS:**  
This talk shows again how DRM has expanded beyond consumer devices to giving vendors technical controls over their products lifecycle (similar behaviours have, for example, been documented with John Deere tractors).

It also shows a DRM-in-depth strategy that is employed to ensure customers keep returning for fixes and service.

Unlike other devices that employ DRM with dedicated security co-processors and signed firmwares, this style of distributed DRM, which is less cryptographically-enforced, is likely to gain popularity with cyber-physical systems.

![Figure 13. A snippet of reverse-engineered code showing the specific long/lat coordinates that would trigger the train to disable itself.](Placeholder Image)

21 Q4 2023

## Detection and Blocking with BPF via YAML

**Author:** Kevin Sheldrake

This talk describes methods that teams can use to easily modify the Linux kernel to inspect packets, processes and other facets of system execution. eBPF (or lately just BPF) has gained traction in the last few years and this talk explores opportunities available to defenders. The open-source Tetragon tool allows teams to quickly and reliably gain insight into kernel structures and to “hook” kernel functions.

By abstracting away the complexity of building and deploying Linux kernel modules, the open-source tool released allows defenders to write policies in YAML instead of C. Tetragon allows teams to modify the behaviour of the Linux kernel and extends the kernel for defensive detection. The researcher also highlights both the benefits and pitfalls teams may encounter with eBPF.

**TAKEAWAYS:**  
eBPF has gained lots of interest both from attackers and defenders. Keep an eye out for this technology to create both emerging attacks and defences.

eBPF allows teams to quickly add Linux kernel functionality, without the friction of upstream development and support of Linux kernel modules. This allows teams to change the Linux kernel behaviour, giving both attackers and defenders the ability to build bespoke tooling. It will be important to watch this space as it continues to grow.

![Figure 14. A diagram showing how Tetragon can hook and introspect the Linux kernel.](Placeholder Image)

22 Q4 2023

## AntiFake: Using Adversarial Audio to Prevent Unauthorized Speech Synthesis

**Authors:** Zhiyuan Yu, Shixuan Zhai, and Ning Zhang

This research explores a proactive defence against DeepFake audio, where clips of a victim’s speech are used by an attacker’s ML model to convincingly sound like the victim. These types of attacks can be used for sabotaging public perceptions, fraud, extortion, and bypassing speaker verification systems.

The researchers trained an ML model that would preemptively modify the would-be victim’s audio in ways that human listeners would not notice, but would drastically change the output of a DeepFake model.

The results speak for themselves: the protected audio was considered “good quality” by most human listeners, and sounded like the unprotected speaker. When the protected audio was used in a number of DeepFake tools (open-source and commercial), the resultant audio was only considered the same speaker by the speaker verification systems tested in at most 2% of samples. For Azure’s commercial speaker identification system, none of the protected samples could be used by an attacker to spoof identity.

**TAKEAWAYS:**  
While this is only an evolution in a game of escalation, people who have (or plan to have) larger public personas should consider the implications of voice cloning, and technologies like AntiFake as a preventative defence.

Technologies like these could be integrated into social media sites, automatically protecting their users.

It is rare that an adversarial technique fits into a defensive scenario so well; it will be an interesting space to watch!

![Figure 15. A diagram of how preventative adversarial processing of audio prevents an attacker cloning the victim’s speech patterns as part of a DeepFake.](Placeholder Image)

23 Q4 2023

## A Good Fishman Knows All the Angles: A Critical Evaluation of Google’s Phishing Page Classifier

**Authors:** Changqing Miao, Jianan Feng, Wei You, Wenchang Shi, Jianjun Huang, and Bin Liang

Google’s Chrome and open-source Chromium browsers are shipped with multiple phishing site detection/prevention tools, from a URL block-list to the feature of this research, a neural network-based (NN) image visual site detector. Before each page is rendered, a screenshot of the page is fed through a model to determine if it is visually similar to one of the commonly-phished pages trained on (e.g., PayPal’s login page, or Azure’s Entra ID login prompt). If the NN classifies the page as highly-similar to a known class, but it is not served from the correct origin domain, it will show the phishing warning before allowing the user to proceed.

This research explored how vulnerable this visual model is to adversarial attacks, and if those attacks could be visually minor enough to fool a user.

In short, this was quite feasible.

One of the most challenging aspects was to ensure the adversarial perturbations persisted through the downsampling and resizing of the page to fit the model’s (small) resolution. Once a screenshot was created that fooled the model, it was added to a pool for a user study to determine if a human would detect the subtle changes (see Figure 17 for a sample). The adversarial perturbations were then exported as a transparent SVG that was superimposed over the phishing page, and confirmed to still not arouse suspicions by the model in the browser.

**TAKEAWAYS:**  
There is no good excuse to be shipping a security model to billions of users without performing at least a modicum of adversarial training.

Due to the open and accessible nature of the model, and the simplicity of this attack (along with the considerable incentives for phishing high-value targets), this is the first step in an escalating game of cat-and-mouse.

![Figure 16. A high-level diagram of the attack flow for creating a visually similar phishing page that does not trip Google’s visual page detector.](Placeholder Image)

![Figure 17. Examples of a PayPal screenshot, with the image on the right slightly perturbed to evade Google’s anti-phishing model.](Placeholder Image)

24 Q4 2023

## Spoofing DNS Records by Abusing DHCP DNS Dynamic Updates

**Author:** Ori David

In this blog post the researcher introduces a new set of attacks against Active Directory domains that use Microsoft Dynamic Host Configuration Protocol (DHCP) servers. These attacks enable threat actors to spoof DNS records in Active Directory-Integrated DNS (ADIDNS) zones by abusing the DHCP DNS Dynamic Updates feature. The impact of this is that the researchers found several different ways that attackers could spoof DNS records on Microsoft DNS servers, including an unauthenticated arbitrary DNS record overwrite.

The impact of the attacks demonstrated can be very significant – the ability to overwrite DNS records without any authentication enables attackers to gain a machine-in-the-middle position on hosts in the domain. This could easily expose sensitive information and credentials, and could also enable relay attacks, allowing attackers to breach AD domains and escalate privileges.

**TAKEAWAYS:**  
Researchers and adversaries are always on the lookout for novel techniques that are 2-3 steps ahead of detection. By leveraging inband DNS updates via DHCP, adversaries likely remain undetected and undeterred.

Using the tools released will help teams identify and properly secure their DHCP servers and DNS records. However, this research warns that other tools used to assist upgrading DHCP servers and clients add to the attack surface.

Active Directory is an entire ecosystem of interconnected platforms and services that smaller organisations host on a single server. This consolidates their risk and attack surfaces as these services all inherit the DC machine permissions by default.

![Figure 18. An arbitrary DHCP DNS overwrite when the DHCP server is a domain controller.](Placeholder Image)

25 Q4 2023

## Operation Triangulation: What You Get When Attack iPhones of Researchers

**Authors:** Boris Larin, Leonid Bezvershenko, and Georgy Kucherin

This work shared the reverse engineering of a highly-sophisticated attack chain targeting Apple’s iOS, combining multiple zero-days to gain full control over the device without alerting the user. While the chaining of four zero-days alone was enough to count as the most sophisticated attack seen by the researchers, it was the employed kernel exploit that stood out.

The kernel exploit used a number of undocumented features of (undocumented) debugging hardware built into the device in order to bypass other hardware protections used by Apple to protect the kernel against exploitation. The researchers suspect there are remnants of a CoreSight-like debugger left in the GPU on modern Apple iOS devices that were discovered and abused by the attack chain in order to disable kernel protections.

How the attackers learned about these features and how to use them remain unclear, but Apple has listed the hardware registers abused by the attack as protected in a patch, so updated devices are now safe.

**TAKEAWAYS:**  
This attack highlights the dual-use potential for many hardware features. While the debugging capabilities were originally intended for legitimate uses, they were subverted for malicious purposes.

Much like security co-processors in modern devices, these debugging capabilities could be used as a reference monitor of sorts to ensure correct behaviour, though with their added functionality, they can be maliciously repurposed.

While attribution is very difficult, it is clear this was a sophisticated campaign, and one that expended significant resources.

Due to the stealthy nature of the self-cleaning JavaScript exploit, it is difficult to know the extent of targeting and how long this attack has been operating. This highlights the amount of resources some adversaries can bring for targeted attacks, and the difficulty in detecting and preventing them.

![Figure 19. A diagram of the attack and all of the sub-components that comprised the overall attack.](Placeholder Image)

26 Q4 2023

## Password-Stealing without Hacking: Wi-Fi Enabled Practical Keystroke Eavesdropping

**Authors:** Jingyang Hu, Hongbo Wang, Tianyue Zheng, Jingzhi Hu, Zhe Chen, Hongbo Jiang, and Jun Luo

This research explored using the Beamforming Feedback Information (BFI) sent from a Wi-Fi device to the access point (AP) as a side-channel for recovering keypress data. BFI is used by an AP in order to optimise Wi-Fi performance, and is influenced by the orientation of the device with respect to the AP or attenuation from fingers in the way. The researchers used this eavesdrop-friendly data to train an ML model on how keypresses, and the transitions between keypresses, change the orientation of the device, and thus the BFI data.

When attempting to recover numeric keypresses across a variety of mobile phone models used by different test users, the accuracy was ~88%. For longer passcodes where there were a certain number of tries allowed before locking the device, the accuracy for whole PIN recovery topped out at 60%. For a full alphanumeric keyboard, the accuracy was lower, but still provided just over 40% accuracy for single keystroke detection.

**TAKEAWAYS:**  
There is a lot of meta-data wrapped around higher level protocols and applications and this research highlights the extent to which physical movements can change the RF environment (and thereby encode some information about data entered into an application).

Secure composition is extremely difficult to get right when being restricted to the pure software domain and the addition of physical-layer properties make it nearly impossible.

Expect to see more of these types of side-channels, and more accuracy over time.

![Figure 20. A high-level diagram of how an attacker can listen to the unencrypted BFI frames sent by a device to the AP and probabilistically recover keypresses.](Placeholder Image)

27 Q4 2023

![A small herd of gemsbok in the Kgalagadi](Lisa van Staden (Thinkst))

## Conclusions

That’s a wrap for 2023, which saw great content and a bunch of interesting reflections.

WE HIGHLIGHTED THREE THEMES FOR THIS QUARTER:
1. LLMs aren’t only a positive force, especially in security.
2. New problems in older or well-explored places.
3. Reflecting on our industry and the gap between theory and practice.

We’re looking forward to seeing what 2024 has in store for the community. We’ll be back next time with more great content!

28 Q4 2023

29 Q4 2023

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
