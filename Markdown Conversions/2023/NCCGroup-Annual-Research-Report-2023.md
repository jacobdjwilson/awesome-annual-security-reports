# 2022 & 2023 NCC Group Research Report

## Table of Contents
- [Executive Summary: Research at NCC Group (2022 & 2023)](#executive-summary-research-at-ncc-group-2022-2023)
- [Message from Global Head of Research, Matt Lewis](#message-from-global-head-of-research-matt-lewis)
- [Foreword from Research Coordinator, Ristin Rivera](#foreword-from-research-coordinator-ristin-rivera)
- [Artificial Intelligence & Machine Learning (ML)](#artificial-intelligence-machine-learning-ml)
- [Incident Response & Threat Intelligence Research](#incident-response-threat-intelligence-research)
- [Applied Cryptography](#applied-cryptography)
- [Cloud & CI/CD Pipeline Security](#cloud-cicd-pipeline-security)
- [Hardware & Embedded Systems](#hardware-embedded-systems)
- [Operating System Security](#operating-system-security)
- [Exploit Development Group](#exploit-development-group)
- [Collaboration with Industry & Academia](#collaboration-with-industry-academia)
- [Other Interesting Research](#other-interesting-research)
- [Acknowledgments](#acknowledgments)
- [About Research at NCC Group](#about-research-at-ncc-group)
- [Appendices](#appendices)
    - [Appendix 1: Open-Source Security Tool & Code Releases](#appendix-1-open-source-security-tool-code-releases)
    - [Appendix 2: Publicly Reported Security Audits](#appendix-2-publicly-reported-security-audits)
    - [Appendix 3: Technical Advisories](#appendix-3-technical-advisories)
    - [Appendix 4: Conferences & Talks](#appendix-4-conferences-talks)

Our 2022-2023 Research Report is also available in downloadable PDF.

NCC Group
Research Report
2022 & 2023
Matt Lewis, Global Head of Research &
Ristin Rivera, Research Program Coordinator
research.nccgroup.com

## Executive Summary: Research at NCC Group (2022 & 2023)
Over the past two years, our global cybersecurity research has been characterized by unparalleled depth, diversity, and dedication to safeguarding the digital realm. The highlights of our work not only signify our commitment to pushing the boundaries of cybersecurity research but also underscore the tangible impacts and positive change we bring to the technological landscape. This report is a summary of our public-facing security research findings from researchers at NCC Group between January 2022 and December 2023.

With the release of 18 public reports and presenting our work at over 32 international conferences and seminars, encompassing a variety of technology and cryptographic implementations, we have demonstrated our capacity to scrutinize and enhance key security functions. Notably, our collaborations with tech giants such as Google, Amazon Web Services (AWS), and Kubernetes underscore our pivotal role in fortifying the digital ecosystems of industry leaders.

Commercially, 2022 and 2023 saw us deliver over $3million in revenue in collaborative research engagement across various technologies and many sectors, increasingly across Artificial Intelligence (AI) and AI-based systems.

In our bid to democratize cybersecurity knowledge, we have released 21 open-source security tools and repositories. These invaluable tools have catalyzed efficiency gains across multiple domains of cybersecurity.

Our research has positioned us at the forefront of evolving cryptographic paradigms. With significant work in Post-Quantum Cryptography, Elliptic Curve Cryptography, and Blockchain security, we remain key players in shaping the future of digital privacy and security.

The meteoric rise of AI/ML applications has been matched by our intense focus on understanding their security dynamics. Our research in this arena has grown exponentially since 2022, providing critical insights into the strengths and vulnerabilities of these transformative technologies.

Modern cloud environments, coupled with rapid shifts in software development and deployment, have necessitated deep dives into their security mechanisms.

Our outputs in this domain have been instrumental in pioneering robust cyber defense tactics for contemporary digital infrastructures. Our exhaustive studies into hardware vulnerabilities and Operating System security have set benchmarks in comprehending and countering potential threats.

The external presentation of our research, particularly by our Exploit Development Group (EDG), has won us accolades, most notably a third-place finish at the 2022 Pwn2Own Toronto competition. EDG’s work on exploiting consumer routers and enterprise printers has been groundbreaking. Ken Gannon and Ilyes Beghdadi successfully exploited the Xiaomi 13 Pro smartphone at the 2023 Pwn2Own Toronto competition, demonstrating our continued excellence in mobile security.

Our research has spanned several other pivotal areas including Vulnerability Detection & Management, Reverse Engineering, Modern Networking & Security, and Secure Programming & Development. Unearthing over 69 security vulnerabilities across third party products, we’ve reinforced our commitment to digital safety through responsible and coordinated vulnerability disclosure. Each discovery, while highlighting potential threats, also underscores our unwavering dedication to proactively fortifying global digital infrastructures.

In conclusion, our journey through 2022 and 2023 has been marked by rigorous research, collaboration, and an unwavering commitment to excellence. As we continue to gain intelligence, insight and to innovate, our role in shaping a secure digital future remains paramount.

32+ Global Conferences
$3 million revenue from collaborative and commercial research engagements
69+ CVEs
21 Open-Source Tools
276+ Blog Posts
18 Public Reports

## Message from Global Head of Research, Matt Lewis
The big cybersecurity challenges for the next 5-10 years relate to ever-evolving technology and threat landscapes, and the need for agility to keep pace in line with these evolutions against the backdrop of a volatile geopolitical landscape. Research has never been more important to help us in our endeavor to achieve security and resilience in these times.

On a technology level, legacy IT systems and maintenance of software patches remain a key challenge. Organizations are currently in mixed states of security posture in terms of legacy equipment and cloud migration and adoption. Many of the security promises of cloud haven’t been met (or understood), meaning that even cloud systems can and do suffer from legacy issues such as out of support, potentially vulnerable components. Advanced Persistent Threat (APT) intrusions and Ransomware outbreaks routinely exploit legacy or unpatched systems for their gain, thus there is still much to do in terms of mitigating risk around legacy, noting that the new technologies of today, will also become legacy in 5 or 10 years’ time, therein establishing legacy IT as a permanent challenge for cybersecurity.

While APTs are a huge threat to organizations and the global economy, the reality is that in terms of impact, ransomware is a much more pressing and damaging threat. A key challenge here is how to ensure organizations remain resilient in the face of a ransomware outbreak, since even a fully patched, cyber mature organization could be subject to a sophisticated ransomware attack exploiting a 0-day vulnerability.

AI and Machine Learning is already proving a challenge in terms of the requirement to gain a robust understanding of their relative opportunities and threats. The sudden accessibility of performant Large Language Models (LLMs) like ChatGPT in 2022 took most sectors, cybersecurity included, by surprise. There are already several potential negative impacts of LLMs in terms of cyber security, the security of the models themselves in how they are created and understanding how and why they produce their outputs. There is also concern for how and where and by whom LLMs are used – perhaps in generating source code for malware, or attack methodologies that make it easier for less technical individuals to perform offensive cyber activities. There are also big challenges in the realm of misinformation and, with related commoditized capabilities like Deepfakes, the emerging threat of Identity Compromise to support fraudulent activities – certainly, the industry is already seeing a natural evolution and sophistication of misinformation and targeted phishing campaigns leveraging these capabilities.

The growing use of AI as a security control also presents a huge challenge – the efficacy of such solutions demands robust testing, evaluation and assurance, lest we become too trusting of automated decision making in security governance that we believe to be optimal but in fact may be silently rendering our systems more vulnerable.

It is possible we will see Quantum Supremacy in our lifetime, meaning there is a burgeoning challenge in preparing businesses for Post-Quantum Cryptography (PQC). While the preparation requirements and PQC algorithms are broadly understood, ensuring a worldwide migration to robust PQC presents a challenging undertaking.

Related to quantum is the need to manage the threat model of classical computing integration with quantum components. The traditional vulnerabilities in classical computing will inevitably present potential for adversary exploitation to gain unauthorized access to quantum computing resources. There are also challenges in needing to understand and assure applications of quantum computing to cryptographic processes, namely Quantum Random Number Generation (QRNG) for seeding cryptographic material, and Quantum Key Distribution (QKD) for managing cryptographic keys and exchange.

Despite their challenges, the technologies discussed above can be seen as the foundations and backbone for the broader concept of the connected society or connected world. Exponentially, this concept increases the attack surface of global economies, as seen through Internet of Things (IoT), Smart Cities and Connected Places, Connected and Autonomous Vehicles to name but a few. These application areas also move us rapidly into the cyber-physical domain, meaning the cyber challenges here are not only impacting on a security level, but also safety, whereby the effects of compromise of some systems could lead to environmental impact, physical harm or worst-case loss of life.

> Fueled by the COVID-19 pandemic push for increased home working, we have inadvertently lost the concept of the ‘network perimeter’, but also legitimized this through concepts such as Zero Trust networks. This brings huge challenges around the need to authenticate and authorize directly connected Internet users and machines in trusted, secure and reliable ways.

Supply chain and sovereignty also pose challenges in the present and near future. Lack of trust in supply chains and countries of manufacture has led to a strategic goal for many developed economies to increase their sovereign capabilities and therefore reduce reliance on global manufacturing hubs. Challenges here mostly relate to funding and skillsets required to demonstrate that countries have their own secure capabilities that can deliver in this space.

There is also a broader research challenge relating to horizon scanning and knowing how and where to prioritize security advice and guidance on technologies in terms of their likely adoption. Examples we can expect to see in the next 10 years include Brain Computer Interfaces (BCIs), the Metaverse and its associated VR/AR technologies, increased space-based telecoms, neuromorphic computing and synthetic biology to name but a few – understanding the security capabilities and issues with these technologies will require vast amounts of research.

Finally, yet crucially, there is a fundamental research challenge around energy use in the face of an energy crisis and climate change. There are estimates that 21% of the world’s overall energy usage by 2030 will be computing power alone, yet technologies in AI, Cloud and Quantum are inherently power-hungry. We therefore need to be incredibly mindful of, and proactive in the development of secure, power-efficient and sustainable technical solutions for the technologies and systems that we will create and use over the coming decade.

> Continuously evolving technology and threat landscapes is why research is at the heart of what we do at NCC Group. Our global team of researchers routinely tackle many of these topics and themes to understand risk and remediation across all technologies in all sectors. This report sets out just some of the research insights from our broad research program over the past couple of years. The research doesn’t stop however, and we’re already embracing the research challenges of 2024 and beyond...

## Foreword from Research Coordinator, Ristin Rivera
In our increasingly digital world, the first indication of a security breach often emerges only after the damage has been done, leaving individuals and organizations to grapple with the aftermath. For the average person, without a security team to monitor their network and devices, the assumption is often made that regulatory safeguards would prevent the release of vulnerable products into the market. This assumption, however, can prove to be a significant risk.

Take for example the pervasive world of white-labelled products, particularly in everyday technology. As shown from many of our research outputs from the past couple of years, these cost-effective, ubiquitous products are not always synonymous with security. Repeatedly, our research on white-labelled products, like home routers and IoT devices, reveals that they have little to no security assurance or onward maintenance by manufacturers. They never receive crucial firmware updates or security patches, thus rendering them vulnerable and exposing users and consumers to a myriad of risks. The rise of Bluetooth technology in security-critical applications, such as car key unlocking systems, further highlights this issue which doesn’t necessarily correlate with ‘cheap’ products and services alone - despite Bluetooth’s own guidance on the limitations of its security features, the trend persists, as seen through our research demonstrating remote keyless attacks to gain entry to, and drive off with Tesla motorcars (a premium product) as just one example.

This unseen vulnerability represents the Achilles heel of cybersecurity. Proactive security measures, regular check-ups, and a comprehensive understanding of the limitations of our technology through continued research and innovation are not merely best practices; they are essential pillars of a robust cybersecurity strategy.

## Artificial Intelligence & Machine Learning (ML)
- Potential and Pitfalls of AI/ML: The transformative power of AI and ML in cybersecurity is clear, but so are the associated risks and challenges
- Impersonation and Privacy Concerns: AI’s capability to mimic human interactions can lead to serious privacy concerns, especially in community-driven platforms
- ML in Malware Analysis: ML significantly enhances malware detection but is not immune to challenges like adversarial attacks
- Security Implications in ML Systems: Adversarial attacks, data poisoning, and model extraction are major concerns in ML security
- Large Language Models (LLMs): Their power and potential come with challenges around overfitting and data reproduction
- Human Oversight: Despite AI’s capabilities, human expertise remains paramount in cybersecurity tasks, from code review to threat detection

In the dynamic landscape of cybersecurity, the domain of Artificial Intelligence and Machine Learning (AI/ML) security research has emerged as a paramount focal point. As AI/ML systems become deeply integrated into the very fabric of our society, influencing sectors from healthcare to finance, and from transportation to communication, their security and safety cannot be understated. Ensuring the robustness of these systems is not merely a technical necessity but a societal imperative. With AI playing an ever-impacting role in decision-making processes, personal interactions, and infrastructure, researching its security contours is critical to safeguarding the trust and wellbeing of individuals and institutions that increasingly rely on it. Unsurprisingly, AI/ML research at NCC Group has grown exponentially since 2022, as we continue to grasp the security and safety strengths and limitations of these powerful capabilities. Key observations from our AI/ML research since 2022 were:

**Potential and Pitfalls of AI/ML**

Jon Renshaw summarized much of our research in an informative whitepaper, to assist those wishing to better understand how AI applies to cybersecurity. The paper provides high-level summaries of how AI can be used by both cyber professionals and adversaries, the risks AI systems are exposed to, safety, privacy and ethics concerns and how the regulatory landscape is evolving to meet these challenges.

Practical Attacks on Machine Learning Systems: NCC Group’s Chief Scientist authored this formative paper which collects a set of notes and research projects conducted by NCC Group on the topic of the security of ML systems. The paper provides industry perspective to the academic community, while collating helpful references for security practitioners, to enable more effective security auditing and security-focused code review of ML systems. Details of specific practical attacks and common security problems are described throughout the paper.

Security Implications in Machine Learning: Chris Anley’s blog, “Five Essential Machine Learning Security Papers,” underscores the security challenges in ML systems as seen through landmark exploitation techniques described across five key academic papers.

> Don’t use ChatGPT for security code review. It’s not meant to be used that way, it doesn’t really work (although you might be fooled into thinking it does), and there are some other major problems that make it impractical. Also, both the CEO of OpenAI and ChatGPT itself say that you shouldn’t. - Chris Anley, NCC Group Chief Scientist

Code Review with AI and ML: We wrote articles discussing the intersection of code review and ML. From using Semgrep with Jupyter Notebook files by Jose Selvi to Chris Anley’s caution against using ChatGPT for security code reviews, there is a clear acknowledgment of ML’s growing influence in this domain. However, there is also a recognition of its limitations, emphasizing human expertise’s continued relevance.

Intelligent Web Crawling with ML: Project Bishop, performed by Thomas Atkinson and Jose Selvi, was a continuation of Project Ava and explored the use of ML for intelligent web crawling. It emphasized the power and potential of ML in enhancing web application security testing tasks.

Eric Schorn provided great insight across a range of ML topics in a blog series that will continue into 2024 across 10 eventual lessons:

> Generative AI is stealing the spotlight at the moment but smaller, specialized AI/ML models that can be run locally are also becoming usefully powerful to run on accessible consumer grade hardware. In the coming years we should expect both attacker and defender tooling to increasingly make use of these smaller, localized models. - Thomas Atkinson, Managing Security Consultant

- Machine Learning 101: The Integrity of Image (Mis)Classification: This blog highlights various security-related weaknesses in ML systems. Topics range from the brittleness of image classification models to attacking facial authentication systems with poisoned data, emphasizing the criticality of mitigating these weaknesses.
- Machine Learning 102: Attacking Facial Authentication with Poisoned Data: This blog post demonstrates exactly how a data poisoning attack might work to insert a backdoor into a facial authentication system.
- Machine Learning 103: Exploring LLM Code Generation: This executable blog post explores code generation from a 16 billion-parameter large language model (LLM).
- Machine Learning 104: Breaking AES with Power Side-Channels: In this post, Eric discusses how deep ML techniques can be used in cryptography, revealing potential vulnerabilities in systems hitherto considered impregnable.

**ML in Malware Analysis**

Machine Learning for Malware Analysis: Matt Lewis’ work with University College London (UCL) on “Machine Learning for Static Analysis of Malware: Expansion of Research Scope” showed the utility of ML in enhancing static analysis of malware. By leveraging ML, there is potentially improved efficiency in processing data and recognizing malicious patterns, thus offering better detection rates than traditional methods. However, adversarial attacks present a potential challenge to these methods, underscoring the importance of robust defenses.

**Impersonation & Privacy Concerns**

AI-generated Impersonation: In the article “Impersonating Gamers with GPT-2”, David Brauchler deep dived into the use of OpenAI’s GPT-2 model to mimic gamers’ conversations. The key theme here was the potential security and privacy risks that come with AI-generated content, especially within online communities like gaming. The research effectively demonstrated GPT-2’s ability to create a convincing imitation of user interactions, emphasizing the urgent need for countermeasures against AI-driven impersonation attacks.

**Large Language Models (LLMs)**

Prompt Injection Vulnerabilities: “Exploring Prompt Injection Attacks” by Jose Selvi delved into the vulnerabilities in terminal sessions, where attackers can manipulate command prompts to inject malicious LLM behaviors.

> Treat the output of your Large Language Model (LLM) as untrusted data within your threat model. While AI providers implement safeguards against threats such as Prompt Injection, attackers can still manipulate inputs to generate unexpected outputs. These outputs may include payloads that exploit vulnerabilities in the underlying application or infrastructure.  - Jose Selvi, Executive Principal Security Consultant

Matt Lewis explored the potential data security challenges around LLM prompt security, through an example of how a seemingly innocent set of user prompts could potentially lead to unwanted profiling of that user.

Large Language Models (LLMs) and Overfitting: Several articles, such as “Exploring LLM Code Generation” and “Exploring Overfitting Risks in Large Language Models” by Jose Selvi, address the potential and pitfalls of LLMs. Concerns like overfitting, data inference, and the reproduction of copyrighted content underline the caution required in leveraging these models.

> AI security is a pressing concern in security research. As artificial intelligence systems become increasingly integrated into our lives, safeguarding them against malicious attacks and ensuring their ethical use is paramount. Ongoing research is crucial to stay ahead of emerging threats and develop robust defense mechanisms.” - ChatGPT (prompted about its own security)

## Incident Response & Threat Intelligence Research
Several high-caliber research outputs from our threat intelligence and incident response teams the past two years provide a multi-faceted view of the current threat landscape, from nation-state advanced persistent threats (APTs) to new malware variants and evolving ransomware tactics.

Across this research, several recurring themes and trends emerged:

- Lateral Movement via Remote Desktop Protocol (RDP): Multiple threat actors, including those deploying ShadowPad, LockBit 3.0, Everest, and Black Basta, utilized RDP for lateral movement within a compromised environment
- Use of Legitimate Tools for Malicious Purposes: Tools like ADFind, PowerView, and Cobalt Strike are leveraged by various threat actors for information gathering, command and control, and lateral movement
- Persistent Threats in App Stores: Despite ongoing efforts to secure platforms like the Google Play Store, malicious actors continue to infiltrate it, as seen with SharkBot
- Diverse Initial Access Methods: From exploiting vulnerabilities to leveraging social engineering on platforms like LinkedIn, threat actors employ a range of methods to gain initial access to target environments

> Cyber threat is a constantly evolving space, presenting unique challenges for organizations aiming to safeguard their digital assets. One of the most effective ways to stay ahead of these threats is through vigilant incident response and in-depth threat intelligence research. These two facets of cybersecurity not only facilitate timely responses to attacks but also offer insights into the tactics, techniques, and procedures (TTPs) of adversaries.- Matt Hull, Global Head of Threat Intelligence

In summary, these research outputs underscore the need for organizations to continuously adapt and evolve their cyber defenses, given the dynamic nature of threats and the sophisticated tactics employed by adversaries.

**Real-World Compromise & TTPs**

2000 Citrix NetScalers backdoored in mass-exploitation campaign: Fox-IT uncovered a large-scale exploitation campaign of Citrix NetScalers in a joint effort with the Dutch Institute of Vulnerability Disclosure (DIVD). An adversary had been identified exploiting in automated fashion, placing webshells on vulnerable NetScalers to gain persistent access. The adversary could execute arbitrary commands with the webshell, even when a NetScaler was patched and/or rebooted. The Dutch Institute of Vulnerability Disclosure notified the victims as identified by Fox-IT. At the time of the exploitation campaign, Fox-IT enumerated 31,127 NetScalers worldwide that were vulnerable to CVE-2023-3519.

ShadowPad Intrusion: William Backhouse, Michael Mullen, and Nikolaos Pantazopoulos provided insights into the TTPs of a Chinese APT leveraging the ShadowPad malware. Initial access was achieved through a vulnerability, with successive backdoors being installed. Tools like ADFind and PowerView were used for information gathering, and ShadowPad was used extensively for lateral movement, command and control, and data exfiltration.

BUMBLEBEE Malicious Loader: This research highlighted BUMBLEBEE, a new loader that incorporates anti-analysis techniques and utilizes Rabbort.DLL for process injection. It can download and execute malicious payloads such as Cobalt Strike beacons.

Post-Conti Data Leaks: Despite the public disclosure of Conti’s tools and conversations, Conti operators continued their activities. Techniques observed include the use of Cobalt Strike and different legitimate remote access software for persistence.

> In light of several serious FortiGate, Citrix and Cisco vulnerabilities, edge device exploitation is picking up its pace. As your network’s first line of defence, visibility on these devices is often scarce and overlooked, making responding to these threats difficult. We believe investing in visibility, such as central logging, patch management and Incident Response readiness will make the difference when it comes to responding to these types of threats. “– Security Research Team, Fox-IT (part of NCC Group)

Saitama Implant Detection: A novel malware sample named ‘Saitama’ used DNS for C2 communications, making detection challenging. This article outlined the development of a server-side implementation for the implant to aid detection.

Karakurt Extortion Actor: NCC Group’s CIRT discovered indicators of compromise from Karakurt, an extortion-focused threat actor, especially in environments using single factor Fortinet VPN access.

LAPSUS$ TTPs: Incidents involving LAPSUS$ revealed tactics such as scraping corporate SharePoint sites, accessing password managers, and cloning git repositories.

MetaStealer Analysis: MetaStealer emerged as a new information stealer, notable for its reliance on open-source libraries and a range of functionalities including password stealing and keylogging.

Lazarus Initial Access: The Lazarus group’s initial access phase involved impersonating LinkedIn profiles, enticing victims to download malicious documents, and using scheduled tasks for persistence.

Popping Blisters for research: An overview of past payloads and exploring recent developments. Mick Koomen provided an overview of payloads dropped by the Blister loader, based on 137 unpacked samples across an 18-month period.

The Spelling Police: Searching for Malicious HTTP Servers by Identifying Typos in HTTP Responses: Margit Hazenbroek of Fox-IT blogged about identifying servers that host nefarious activities by looking for anomalies in responses of HTTP servers.

SharkBot on Google Play: Our Threat Intelligence team identified and reported instances of the SharkBot Android banking Trojan being distributed through the official Google Play Store.

**Ransomware**

LockBit 3.0 Ransomware Attack: Ross Inman explored a LockBit 3.0 ransomware deployment, highlighting initial access via SocGholish, Cobalt Strike for command and control, and the disabling of defensive measures like Windows Defender. Exfiltration occurred through Mega.

Everest Ransomware Group: This article dived into the TTPs of the Everest Ransomware group, noting techniques such as lateral movement via RDP and the use of LSASS and NTDS.dit dumps.

Ransomware Entry Techniques: Michael Mathews delved into common entry methods used by ransomware affiliates, shedding light on the increasing trend of Ransomware as a Service (RaaS).

Black Basta Ransomware: Ross Inman and Peter Gurney shed light on the TTPs of the Black Basta ransomware, including lateral movement using Qakbot and the technical breakdown of the ransomware executable.

Unveiling the Dark Side: A Deep Dive into Active Ransomware Families: The CIRT Team look at the return of the BlackCat Ransomware-as-a-Service (RaaS)

D0nut encrypt me, I have a wife and no backups: Ross Inman provided a deep dive into the D0nut extortion group.

Don’t throw a hissy fit; defend against Medusa: Molly Dewis provided a deeper dive into the Medusa ransomware family.

Is this the real life? Is this just fantasy? Caught in a landslide, NoEscape from NCC Group: Alex Jessop delved into a real-world incident response engagement handled by NCC Group’s CIRT, which involved the RaaS known as NoEscape.

## Applied Cryptography
NCC Group’s Crypto Services team continued to perform leading research throughout 2022 and 2023. The variety of their rich outputs reflects the ever dynamic and evolving nature of the field of cryptography. Key themes from our crypto research during this period were:

- Post-Quantum Cryptography: The push towards post-quantum cryptography is evident, with discussions on both its challenges and the introduction of new algorithms
- Elliptic Curve Cryptography: A significant portion of our research focused on elliptic curves, highlighting their continued importance in cryptographic systems
- Security Vulnerabilities: From erroneous computations to time-based side-channel attacks, we further explored vulnerabilities in cryptographic implementations and their implications
- Blockchain and Cryptography: Several of our outputs emphasized the relationship between cryptographic principles and blockchain technology

> Cryptography is a key component of every organization’s data security. Cryptography analysis and research is critical to identify impactful cryptography vulnerabilities in today’s products and applications. Cryptography Services’ research in the ever-changing cryptography landscape ensures that the team continually contributes to the secure design and implementation of cryptography in a wide variety of areas. Javed Samuel, Global VP for Cryptography Services

**Elliptic Curve Cryptography**

Pairing-Based Cryptography: Giacomo Pope detailed pairing-based cryptography, especially the “pairing-friendly” elliptic curves. A key highlight was the estimation of bit security and the advancements in solving the discrete log problem, which has implications on the reported bit-security of several widely used curves.

Elliptic Curve Cryptography: Thomas Pornin’s contributions encompassed the domain of practical elliptic curve cryptographic systems. A new pair of elliptic curves, jq255e and jq255s, were proposed as efficient alternatives to existing standard curves.

Giacomo Pope presented on Superspecial Cryptography Computing Isogenies Between Elliptic Products

Thomas Pornin published several papers on Elliptic Curve Cryptography:
- Faster Complete Formulas for the GLS254 Binary Curve
- EcGFp5: a Specialized Elliptic Curve
- Truncated EdDSA/ECDSA Signatures
- Point-Halving and Subgroup Membership in Twisted Edwards Curves
- Efficient and Complete Formulas for Binary Curves
- Optimized Discrete Logarithm Computation for Faster Square Roots in Finite Fields
- Double-Odd Jacobi Quartic and https://doubleodd.group/

**Post-Quantum Cryptography**

Post-Quantum Cryptography: Thomas Pornin, among others, introduced BAT, a post-quantum key encapsulation mechanism, promising better performance than other forthcoming standardized solutions. Additionally, NIST’s standardization process for post-quantum cryptographic algorithms, which aims to resist cryptanalysis by quantum computers was discussed by Thomas Pornin.

The team released multiple post-quantum cryptography papers:

Cryptanalysis: Giacomo Pope discussed the implementation of a cryptanalytic attack against SIKE, a finalist of the NIST Post-Quantum Cryptography Project. This attack could break the highest-level security parameters in a short time.
- Thomas Pornin on Improved Key Pair Generation for Falcon, BAT and Hawk
- Thomas Pornin on BAT: Small and Fast KEM over NTRU Lattices
- Thomas Pornin on Hawk which been submitted to NIST
- Giacomo Pope on A Note on Reimplementing the Castryck-Decru Attack and Lessons Learned for SageMath
- Giacomo Pope on A Direct Key Recovery Attack on SIDH
- Giacomo Pope on FESTA: Fast Encryption from Supersingular Torsion Attacks

**Crypto Attacks**

Cryptography Side Channels: Gérald Doussot explored side channel findings in implementations of the QUIC protocol. The focus was on timing side channels arising from data processing at secret offsets.

Random Number Generators: Paul Bottinelli highlighted the vulnerability in a Pseudo-Random Number Generator (PRNG) based on the ChaCha20 cipher, emphasizing the importance of robust random number generators in cryptographic protocols.

Software Vulnerabilities and Blockchain: Aleks Kircanski examined erroneous computation patterns in Golang, highlighting their implications in blockchain, where they can lead to unintended ledger states or netsplits, which have significant consequences like double-spend attacks.

**Signatures & Algorithmic Considerations**

Lattice-Based Signatures: In a two-part blog, Elena Bakos Lang provided an intuitive understanding of the two lattice-based signature schemes – Falcon and Dilithium – set for standardization by NIST.

Multivariate Cryptography: Sam Markelon blogged on the topic of multivariate digital signature themes, by walking through an illustrative example of a multivariate digital signature scheme called Unbalanced Oil and Vinegar (UOV) signatures. UOV schemes serve as the basis for a number of contemporary multivariate signature schemes like Rainbow and MAYO.

Cryptography in Practice: Various posts, like the one by Giacomo Pope on the SIAM Conference on Applied Algebraic Geometry, showcased real-world applications and discussions on cryptography. Eli Sohl continued work on Cryptopals video solutions. Paul Bottinelli presented on Selected Cryptography Vulnerabilities of IoT implementations at ICMC 2022. Javed Samuel presented on Practical Cryptography at Geek Week 2023,

Implementation Strategies: Thomas Pornin’s blog post shed light on the coding strategy choices during the implementation of cryptographic algorithms on certain elliptic curves, particularly Curve25519.

## Cloud & CI/CD Pipeline Security
Over the course of 2022 and 2023, several NCC Group research outputs on cloud and CI/CD pipeline security emerged from our experts. These studies were a deep dive into the intricacies of ensuring robust cyber defense mechanisms in modern cloud environments, software development and deployment paradigms.

Key themes in this category were:

- Security Vulnerabilities in Modern DevOps: The vulnerabilities in CI/CD pipelines and their real-world implications
- Dynamic Testing and Infrastructure as Code (IaC): The role of dynamic tools in IaC and the complexities they introduce
- Cloud Platform Benchmarks: The efficacy and importance of benchmarks like CIS for cloud platforms such as Microsoft 365, AWS and GCP
- Data Integrity in CRM Platforms: Challenges and best practices for maintaining data integrity in platforms like Salesforce
- Access Control Mechanisms: Evolving authentication and authorization paradigms, particularly in Azure and AWS

> It’s been great to devote more attention to CI/CD and pipeline security research. The era of exploiting Jenkins script console is over and now we can focus on other basics and TOP 10 misconfigurations.- Viktor Gazdag, Principal Security Consultant

Some of our outputs in this domain included:

**CI/CD Pipeline Security**

Aaron Haymore, Iain Smart, Viktor Gazdag, Divya Natesan and Jennifer Fernick delved into vulnerabilities in CI/CD pipelines by narrating ten real-world scenarios. They found avenues of compromise through means such as vulnerable code, credential theft, or permission abuse. The compromised pipelines could lead to malicious code injections, sensitive data theft, or pipeline disruptions.

**Infrastructure as Code (IaC) Testing**

Erik Steringer explored dynamic tooling’s role in ensuring the security of IaC. While IaC offers advantages like version control and reusability, it also brings new complexities and potential vulnerabilities. Steringer emphasized integrating robust testing processes with dynamic tools like Inspec, Pulumi, and Terratest. Viktor Gazdag further contributed to this theme by providing a comprehensive guide on integrating security into infrastructure as a code, emphasizing the significance of security checks, tools, and procedures in cloud automation.

**Cloud Platform Security**

Viktor Gazdag evaluated the efficacy of the Center for Internet Security (CIS) benchmarks for Microsoft 365 and the Google Cloud Platform. These benchmarks serve as yardsticks for securing cloud environments against prevalent attack vectors.

Ken Wolstencroft used a threat modeling approach to understand security challenges on Google Cloud Platform (GCP) and point out necessary security controls.

Alberto Verza discussed the evolution of Multi-Factor Authentication in Azure Active Directory, highlighting tools to identify gaps emerging from conditional access policies.

Rennie deGraaf introduced AWS’s attribute-based access control, underscoring the innovative use of tags for implementing ABAC.

Luis Toro introduced Post-exploiting a compromised etcd – Full control over the cluster and its nodes, releasing a tool, which includes multiple functions for post-exploitation of compromised etcds.

**Data Integrity and Exception Handling**

Jerome Smith explored the challenges related to maintaining data integrity and handling exceptions in the prominent CRM platform Salesforce. He showed how misconfigurations, inadequate exception handling, and flawed data management can lead to data corruption or loss. Jerome also highlighted vulnerabilities in custom Salesforce development, emphasizing the potential for exploitable attack opportunities due to language-specific vulnerabilities.

**Cloud Platform Security**

Viktor Gazdag evaluated the efficacy of the Center for Internet Security (CIS) benchmarks for Microsoft 365 and the Google Cloud Platform. These benchmarks serve as yardsticks for securing cloud environments against prevalent attack vectors.

Ken Wolstencroft used a threat modeling approach to understand security challenges on Google Cloud Platform (GCP) and point out necessary security controls.

Alberto Verza discussed the evolution of Multi-Factor Authentication in Azure Active Directory, highlighting tools to identify gaps emerging from conditional access policies.

Rennie deGraaf introduced AWS’s attribute-based access control, underscoring the innovative use of tags for implementing ABAC.

Luis Toro introduced Post-exploiting a compromised etcd – Full control over the cluster and its nodes, releasing a tool, which includes multiple functions for post-exploitation of compromised etcds.

**Data Integrity and Exception Handling**

Jerome Smith explored the challenges related to maintaining data integrity and handling exceptions in the prominent CRM platform Salesforce. He showed how misconfigurations, inadequate exception handling, and flawed data management can lead to data corruption or loss. Jerome also highlighted vulnerabilities in custom Salesforce development, emphasizing the potential for exploitable attack opportunities due to language-specific vulnerabilities.

## Hardware & Embedded Systems
Our hardware and embedded systems security experts engaged in a wide range of research across 2022 and 2023, delving deep into the intricacies of device vulnerabilities, secure development practices, and real-world implications of compromised hardware.

Key themes and observations from this research domain were:

- Early-stage Security: We highlighted the significance of integrating security measures right from the initial stages of hardware and system development
- Vulnerability Analysis: Comprehensive investigation of vulnerabilities in various hardware appliances including printers, routers, and storage devices revealed systemic vulnerabilities
- Secure Boot: Our deep dives into ROM vulnerabilities and secure boot bypasses emphasized the importance of robust initial stages of device operation
- Microcontroller Security: As microcontrollers become ubiquitous in IoT and embedded systems, their security remains paramount

> Product security cannot be easily added after the product is complete. Engaging your security team early and often is the only cost-effective way to ensure that you are protecting your customers. The system threat model and security requirements need to be understood by the development team before they begin their foundational component selection and implementation decisions. Relying on your chipset and Board Support Package (BSP) vendors to provide a complete security story is rarely viable. - Rob Wood, Global VP for Hardware & Embedded Security

The overarching message from our research outputs was the imperative, continued need for proactive measures, deep analysis, and consistent vigilance in the domain of hardware and embedded security.

**Firmware Extraction and Analysis**

Catalin Visinescu detailed a methodology to bypass software update package encryption and directly extract the firmware of the Lexmark MC3224i printer. By desoldering the flash