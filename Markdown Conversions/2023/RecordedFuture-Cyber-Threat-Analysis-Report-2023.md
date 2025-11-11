# THREAT ANALYSIS

By Insikt Group®
March 21, 2024

2023 Annual Report

## Table of Contents
- [Section I Setting the Stage: Technology, Geopolitics, Economics, and Policy](#section-i-setting-the-stage-technology-geopolitics-economics-and-policy)
  - [Major Technology Trends](#major-technology-trends)
  - [Geopolitical Events: Global Conflicts Reshape Strategic Partnerships](#geopolitical-events-global-conflicts-reshape-strategic-partnerships)
  - [Macroeconomic Trends](#macroeconomic-trends)
  - [Cyber Policy’s Uphill Battle](#cyber-policys-uphill-battle)
- [Section II Cyber Threat Intelligence](#section-ii-cyber-threat-intelligence)
  - [Evolution of Exploited Vulnerabilities](#evolution-of-exploited-vulnerabilities)
    - [Expanding Attack Surfaces Increase Opportunity for Mass Exploitation of Vulnerabilities](#expanding-attack-surfaces-increase-opportunity-for-mass-exploitation-of-vulnerabilities)
    - [Technology Product Types That Were Repeatedly Exploited](#technology-product-types-that-were-repeatedly-exploited)
  - [Evolution of Cyber Threats](#evolution-of-cyber-threats)
    - [Early Malicious Use of Generative AI Focuses on Social Engineering, Influence Operations](#early-malicious-use-of-generative-ai-focuses-on-social-engineering-influence-operations)
    - [Third-Party Threats](#third-party-threats)
      - [Software Supply-Chain Attacks Remain Prevalent, Evolving](#software-supply-chain-attacks-remain-prevalent-evolving)
      - [Criminals Target Business Process Organizations to Facilitate Social Engineering](#criminals-target-business-process-organizations-to-facilitate-social-engineering)
      - [Trusted Tools Abused Through Legitimate Internet Services](#trusted-tools-abused-through-legitimate-internet-services)
    - [Extortion Trends](#extortion-trends)
      - [Regulation Abuse Fails to Take Hold](#regulation-abuse-fails-to-take-hold)
    - [Offensive Tooling Increasingly Targets Linux and macOS Systems](#offensive-tooling-increasingly-targets-linux-and-macos-systems)
    - [Gaza War Increases Hacktivist Activity: Capitalizing on Chaos](#gaza-war-increases-hacktivist-activity-capitalizing-on-chaos)
    - [Valid Accounts Increasingly Used for Initial Access, While Phishing Tactics Evolve](#valid-accounts-increasingly-used-for-initial-access-while-phishing-tactics-evolve)
    - [Converging Influence Narratives Between Ideological Groups](#converging-influence-narratives-between-ideological-groups)
- [Section III Reflections on 2022 Predictions](#section-iii-reflections-on-2022-predictions)
- [Section IV Outlook](#section-iv-outlook)
  - [Cyber Threat Landscape](#cyber-threat-landscape)
  - [Contextual Landscape](#contextual-landscape)
- [Appendix A Top Exploited Vulnerabilities in 2023](#appendix-a-top-exploited-vulnerabilities-in-2023)
- [About Insikt Group®](#about-insikt-group)
- [About Recorded Future®](#about-recorded-future)

## FOREWORD

When creating this annual report, we had two goals: to give you insight into the adversary’s playbook and to assess future scenarios so that your organization can reasonably prepare for them.

In 2023, attack surfaces expanded, software supply-chain vulnerabilities were widely exploited, and the expanded use of generative AI increased the velocity of malicious content at scale.

Get insights from the adversary’s playbook of tactics, techniques, and procedures (TTPs).

The report presents the industry’s most comprehensive analysis of intelligence from 2023. It covers threat actors and their playbook of targets, methods, and attacks to help you eliminate blind spots in your current security posture. You’ll discover how:

- Threat actors exploited enterprise software at scale, as observed in CL0P ransomware group’s attack on third-party managed file transfer (MFT) services such as Fortra’s GoAnywhere and Progress Software’s MOVEit.
- Offensive tooling is increasingly targeting Linux and macOS systems: Ransomware kits continue to expand beyond Windows environments, facilitating an expanded range of victims.
- Nation-states such as China-linked Spamouflage Dragon (tracked by Insikt Group as Empire Dragon) are already using AI-generated images to improve information operations (IO).

Prepare for upcoming threats with a roadmap for 2024 and beyond.

The report also offers our predictions regarding key vulnerabilities, third-party threats, extortion groups, and more for the year ahead. Wherever you are in your threat intelligence journey, you can use this report as a roadmap. It will help you strengthen your operations, create a forward-looking strategy, and protect your organization’s data, intellectual property, and brand reputation.

Levi Gundert
Chief Security Officer

## Executive Summary

2023 was a year of unrealized expectations. A rumored global recession failed to materialize. The Ukrainian counteroffensive did not decisively shift the tide of its war against an invading Russia. Any movement toward Israel-Saudi rapprochement was significantly set back following the October 7 Hamas terrorist attack in Israel and the launch of a new war in Gaza. Despite the initial hype around ChatGPT, disruptive applications of generative AI are likely still years off.

Nonetheless, Insikt Group continued to track cyber threat actors capitalizing on this chaos and uncertainty to steal data, conduct espionage, and disrupt their geopolitical rivals. Occasionally, these objectives converged. Chinese state-associated threat actors increasingly targeted Taiwanese semiconductor companies to gain both an economic and political advantage in that industry. At the same time, profit-minded actors took advantage of the surge in hacktivism to sell tools (such as DDoS-as-a-service) or monetize “hack-and-leak” operations.

### 2023 The Year of the Enterprise Software Hack

While “zero trust” may be a buzzword in enterprise security, the reality is that the internet relies on trust now more than ever. The work-from-home era accelerated the adoption of “as-a-service” enterprise software, shared cloud infrastructure, and virtualized workspaces. As a result, even the most security-focused companies rely on a vast array of third-party services and tools to get work done.

Cybercriminals are taking advantage of this increasingly interconnected environment to amplify their attacks. The number of weaponized vulnerabilities in enterprise software increased fourfold from the previous year. Some of the year’s most high-profile attacks targeting enterprise services, such as the MOVEit File Transfer Application exploit in May 2023, garnered attention due to the high volume of second- and third-party entities whose data was exposed. The ransomware gang behind MOVEit, CL0P, is estimated to have earned between $75 to $100 million in profit on that hack alone, suggesting these types of attacks will continue well into 2024.

Exploitation of enterprise software wasn’t the only way threat actors took advantage of trusted technologies and services. Abuse of legitimate internet services — such as messaging platforms and cloud services — was detected in almost 25% of malware families in one Recorded Future study, allowing threat actors to hide their command-and-control (C2) communications by blending in with ordinary traffic. Threat actors also increasingly incorporated exploits for Linux and macOS operating systems into their attack sequences, breaching the “walled garden” and allowing ransomware to be deployed on a wider variety of systems. Finally, threat actors compromised business process organizations (BPOs) to facilitate SIM swapping and other social engineering scams.

## Key Findings

- **Expanding attack surfaces increased the opportunity for mass exploitation of vulnerabilities**: Throughout 2023, threat actors increasingly favored vulnerabilities that would allow the exploitation of multiple victim enterprises through a single vulnerability in a third-party product. The continued hybrid and remote work environment likely fueled this trend.
- **Early malicious use of generative AI focused on social engineering and influence operations**: Initial use cases for malicious use of generative AI have facilitated the creation of large amounts of convincing, fraudulent content. Modified versions of large language models (LLMs) for sale on the dark web have made it easier for users to evade safety guardrails on legitimate tools.
- **Software supply-chain attacks remain prevalent**: The increasingly interdependent nature of software has allowed threat actors to exploit third- and fourth-party dependencies in new ways, such as through the first double-software supply-chain compromise.
- **Criminals targeted business process organizations to facilitate social engineering**: Social engineering scams run through business process outsourcing (BPO) made it easier for criminals to commit fraud, such as SIM swapping.
- **Trusted tools are being abused through legitimate internet services**: Threat actors increasingly exploited trusted tools and services to gain access to an organization’s infrastructure and remain undetected. This included abuse of cloud services for command-and-control.
- **Regulation abuse failed to take hold**: Ransomware and extortion campaigns experimented with new ways to coerce their victims into paying, including reporting their breach to regulators. However, the increased government scrutiny that followed likely made adversaries reconsider this extortion approach.
- **Offensive tooling is increasingly targeting Linux and macOS systems**: Ransomware kits continue to expand beyond Windows environments to provide the opportunity to exploit an expanded range of victims.
- **The war in Gaza increased hacktivist activity, capitalizing on chaos**: While most claims were false or exaggerated, hacktivist activity contributed to the terror and confusion surrounding the October 7 terrorist attack. Hacktivists are increasingly taking advantage of growing “grassroots” interest in their cause by selling exploits, DDoS-for-hire, and other services.
- **Valid accounts are increasingly being used for initial access, while phishing tactics evolve**: While phishing prevention measures have increased in sophistication, threat actors have adapted by adopting new phishing techniques and other initial access vectors, including valid accounts.
- **There is a convergence of influence narratives between ideological groups**: 2023 was characterized by an increasing convergence in narratives used in Chinese covert influence operations with narratives originating from the Russian disinformation ecosystem and US domestic violent extremists, coupled with an increased presence on alt-tech platforms.

![Metrics associated with key themes in the 2023 cyber threat landscape]

## Section I Setting the Stage: Technology, Geopolitics, Economics, and Policy

### Major Technology Trends

It is nearly impossible to talk about trends in 2023 technology developments without acknowledging the ubiquitous discussions around generative artificial intelligence (AI) — specifically, following the release of products such as ChatGPT by OpenAI in November 2022. Immediate uses ranged from global companies debuting AI customer-facing chatbots to research developments in healthcare. We also saw developments in different kinds of AI models, like Microsoft’s research on Explainable Boosting Machines, or AI models that focus on transparency for users to understand how a model reached its conclusion. Further discussion of artificial intelligence trends, specifically how threat actors are using AI, can be found in the Evolution of Cyber Threats section of this report.

In 2023, increased demand for services like cloud computing and generative AI drove vendors to seek increased computing power. Most organizations report deploying applications on at least two infrastructure-as-a-service platforms, while almost half (47%) follow a cloud-first strategy for deploying new applications in their enterprise. Reports estimate that OpenAI will require nearly 30,000 graphics processing units (GPUs) to meet customer demand, according to current projections. The expansion of cloud service providers (CSPs) to meet demand means that certain regions that are powerhouses for cloud computing data centers, like Southeast Asia, are increasingly strategically important locations for the technology industry as a whole.

Another trend in technology products, specifically in customer-facing applications, was increased offerings of passwordless authentication, such as through magic link logins. To balance security and convenience for users, some companies began to allow users and even employees to log into accounts (such as from Microsoft) using a link delivered to their inboxes. The use of magic links was accompanied by passwordless products launched by Google, which now allow users to sign into Google accounts using their phone’s authentication methods.

### Geopolitical Events: Global Conflicts Reshape Strategic Partnerships

In its second year, Russia’s full-scale invasion of Ukraine entered a phase in which both sides wrestled to maintain their territorial gains and the world’s wavering attention. As fighting continued unabated in 2023, both Russia and Ukraine faced threats of resource depletion, personnel shortages, and military offensives that have, at this point, failed to achieve their desired gains. For Ukraine, foreign aid saw more uncertainty this year than the year prior; the resounding tone of NATO’s “unwavering” support for Ukraine took a conditional edge in 2023, with EU members flagging in their support for Ukraine, and US funding stalled in Congress. Meanwhile, the Kremlin turned to partners in Iran, China, and North Korea to secure weapons transfers and logistics. Russia is almost certainly emerging from 2023 emboldened and continues to inject funds into its defense industrial base (DIB), reaching levels higher than any DIB investments since the end of the Soviet Union.

Exacerbating Ukraine’s struggle to maintain its foreign aid from NATO partners is the threat of another geopolitical conflict: the Israel-Hamas War, which began with Hamas’s kinetic terrorist attack on Israel on October 7, 2023. In response, Israel launched a military campaign in the Gaza Strip, supported by $3 billion in military aid from the United States (US). Fears of regional escalation continue to characterize the ongoing war, especially in light of fighting by Iran proxy forces at regional flashpoints, the most capable of which is Hezbollah, an Iran-backed Lebanese militia group. Meanwhile, Russia used the attack as an opportunity to reframe the violence as a direct result of failed US foreign policy initiatives in the Middle East. Moscow’s growing ties to Iran have alienated its once-warming relationship with Israel, and in turn, have demonstrated once again Russia’s direct ideological opposition to perceived Western (especially US) hegemony.

United through anti-Western bloc sentiment, China’s strategic partnerships with both Russia and Iran played out in political, economic, and military areas throughout the year. Robust trade ties and shared geopolitical interests have forged a close relationship between Iran and China, and China has continued to extend military and economic support to Russia in its ongoing invasion of Ukraine. That said, China’s “peace plan” for Ukraine signaled an attempt to keep the US and Europe from alienating it due to its association with Russia. Meanwhile, the US continues to see China as a “competitor” and a “challenger”; this relationship has been exemplified in the last year in a series of tariffs and controls on microchip technology.

![The trilateral relationship between Russia, China, and Iran is based on converging goals]

### Macroeconomic Trends

Entering 2023, the macroeconomy faced headwinds marked by an ongoing global health crisis, growth slowdowns, geopolitical uncertainty, and shifting trade alliances. A wave of mass layoffs also began in the first quarter of 2023, spurred by efforts to readjust after hiring sprees over the previous couple of years. This downsizing hit the technology sector the hardest, with 260,000 jobs lost in 2023. For cybercrime, a sudden pool of unemployed workers exposes prospective job seekers to scam campaigns preying on job uncertainty and job-seeking platforms, and — from a tactical standpoint — exposes the technology sector to the potential loss of talent and innovation.

International businesses and corporate decision-makers were forced to reconcile with the cyber and non-cyber effects that geopolitical events are having on the macroeconomy. China’s cyber-espionage program, for example, has become more mature, stealthy, and coordinated over the past half-decade. This year, Chinese cyber threat groups conducted focused geopolitical targeting on strategic technologies, defense industries, governments, and critical infrastructure, all of which are industries in line with China’s continued striving for military modernization and regional hegemony. Continued economic sanctions on Russia by the West have fractured the global market, placing supply chains under growing tension. In some instances, corporations had to choose between Western and Russian markets based on perceived support to either Ukraine or Russia and were the target of cyberattacks or “hack-and-leak” operations as a result of their decision to leave the Russian market.

### Cyber Policy’s Uphill Battle

In cybersecurity law enforcement, 2023 was a major year of law enforcement takedowns against cybercriminal operations, including ransomware extortion domains as well as dark web forums and marketplaces — primarily in the context of an explicit strategy from the US Department of Justice to focus on direct takedowns versus prolonged investigations. These takedowns were the result of coordinated international efforts by countries including the US, the UK, Germany, and others. While many operations had immediate success in taking down cybercrime infrastructure, replacements eventually popped up in their place. As a result, it remains unclear whether or not these takedown efforts will result in long-lasting reductions in criminal activity levels, or if these actions serve more as an international show of force.

Plenty of sector-specific cybersecurity regulations emerged in 2023, particularly in the US, which affected the transportation and healthcare sectors, among others. With more regulation planned for 2024, the White House is eyeing a set of minimum cybersecurity hygiene standards for entities in the healthcare sector (mirroring other sector-specific efforts). But perhaps one of the most anticipated cyber policy developments this year was the finalization of the Securities and Exchange Commission’s (SEC) regulations for covered entities to report incidents of “materiality” within four business days, following industry feedback that stretched back to mid-2022. While the full effects and implications of this regulation have yet to be seen (especially in the face of reconsideration from some US lawmakers), early examples of effects include companies that reported a drop in stock prices on the same day they reported attacks.

On the other hand, we also observed a focus on regulating cybersecurity in all industries. While Singapore’s cybersecurity law was originally focused on regulating critical infrastructure industries (CII), in late 2023, it proposed amendments to add more requirements for CII while also expanding its scope to regulate more non-CII entities. In Brazil, the country’s national telecommunications agency (ANATEL) updated a national regulation that tightened an existing minimum security requirement for covered entities by adding specific requirements, including password requirements and software vulnerability updates. Both cases are examples of national governments fine-tuning landmark cybersecurity policies that, at the outset, were likely too broad to effectively regulate cybersecurity requirements. At the global level, the UN’s ad hoc cybercrime committee failed to vote on a final treaty text that would set international legal standards to combat cybercrime following negotiating sessions in 2023, meaning that the committee will now have to add an extra session’s worth of work to attempt to pass a viable international treaty.

Additionally, we observed two examples of cyber threat actors using extreme extortion tactics, in the form of reporting victims to their respective regulatory agencies. Threat actors reported the victims under the pretext that because the threat actors were able to breach the victims, the latter had subpar cyber defenses and were, therefore, not in compliance with various regulations. However, we assess that this extortion tactic is unlikely to become commonplace, and is more likely based on garnering public attention. This trend is further discussed in the Extortion Trends section of this report.

## Section II Cyber Threat Intelligence

### Evolution of Exploited Vulnerabilities

#### Expanding Attack Surfaces Increase Opportunity for Mass Exploitation of Vulnerabilities

In 2023, threat groups successfully exploited several vulnerabilities at scale in singular third-party tools (GoAnywhere, MOVEit, and Citrix NetScaler devices) to inflict widespread damage on thousands of organizations. Increasing instances of successful mass exploitation in recent years can be explained, in part, by two factors: enterprises’ increasingly complex and difficult-to-manage attack surfaces, driven by a widespread transition to hybrid work and cloud computing; and increasingly sophisticated ransomware groups that are improving their strategies and tradecraft, including the development and exploitation of zero-day vulnerabilities. Some security researchers have also suggested that enterprise software, like that targeted in numerous mass exploitation events this past year, makes a good target because the software is updated in periodic maintenance cycles that are not conducive to real-time patch deployment.

The most notable instances of mass exploitation this year were carried out by the CL0P ransomware group (CL0P) on two third-party managed file transfer (MFT) services, Fortra’s GoAnywhere MFT and Progress Software’s MOVEit MFT. In a particularly concerning case study, from May 2023 to mid-August 2023, CL0P attacks on MOVEit alone are estimated to have affected a staggering 2,750 enterprises and approximately 94 million individuals. CL0P first exploited the vulnerabilities that enabled these attacks as zero-days, prior to their disclosure and patching, and then systematically exploited those vulnerabilities after they were remediated, as organizations struggled to identify the vulnerabilities in their systems and apply a patch. CL0P’s development of zero-day exploits prior to their disclosure and patching likely assisted in the rapid staging and successful exploitation of those vulnerabilities, even after their disclosure.

In another notable example of mass exploitation, from August to December 2023, both nation-state and ransomware threat actors exploited Citrix Bleed (CVE-2023-4966), affecting NetScaler ADC and NetScaler Gateway devices, to carry out successful attacks on hundreds of organizations. Again, ransomware groups accounted for the majority of reported attacks, including prominent groups like LockBit gang, Medusa gang, and ALPHV.

There are some commonalities among product vulnerabilities that enable mass exploitation. Each case of mass vulnerability exploitation observed this year had the following characteristics in common:

- The vulnerabilities were discoverable via public scans of internet-facing infrastructure, setting threat actors up for easy vulnerability discovery and exploit deployment.
- The vulnerabilities were exploited before they were publicly known (as a zero-day) and patched, and they continued to be widely exploited after being disclosed, as enterprises struggled to patch them.

While zero-day vulnerabilities are cause for concern, it should be noted that in most instances of mass exploitation, successful attacks took place after a vulnerability was disclosed and patched. This trend probably reflects different levels of resourcing for victim organizations. While some organizations have sophisticated security programs, implementing behavioral analytics to combat the exploitation of zero-day vulnerabilities, many organizations still struggle to implement the patch management measures necessary to prevent the most basic opportunistic attacks. Recent Microsoft research suggests that 99% of cyberattacks can be prevented through basic security practices like maintaining a strong patch management program, the application of zero trust principles, the use of extended detection and response (XDR) solutions, and the use of multi-factor authentication (MFA).

#### Technology Product Types That Were Repeatedly Exploited

The increased virtualization and migration to the cloud are driving more dependency on a narrowing supply chain of vendors, introducing new security risks to the enterprise environment. Aligning with a trend from 2022, threat actors continued to target vulnerabilities in operating systems across major software vendors such as Microsoft, Google, Apple, and Cisco in 2023, as befits their high market share. However, compared to high-risk vulnerability exploitation observed in 2022, we observed increasing instances of active exploitation targeting vulnerabilities in enterprise software and network infrastructure in 2023. Figure 3 shows an approximately 290% rise in the number of vulnerabilities exploited in attacks against enterprise software in 2023 compared to 2022, both by volume and by individually targeted software. Due to the prevalent use of these products in enterprise environments, these high-risk vulnerabilities can be exploited to provide widespread unauthorized access to corporate environments and the sensitive data that ransomware groups desire. Similarly, we saw a 309% increase in the number of vulnerabilities exploited in attacks against network infrastructure.

![High-risk vulnerabilities actively exploited in 2022 and 2023 per the Recorded Future® Intelligence Cloud]

Several ransomware threat actors deliberately targeted vulnerabilities in file transfer software as part of their extortion operations. The most prominent example of this trend is CL0P’s data theft campaign targeting Progress Software MOVEit Transfer instances vulnerable to CVE-2023-34362. Other similar instances involved CL0P, ALPHV, and LockBit’s exploitation of CVE-2023-0669 affecting GoAnywhere secure managed file transfer (MFT) software, as well as Reichsadler’s exploitation of CVE-2023-40044 in Progress Software’s WS_FTP Server. Additionally, IceFire and Buhti were observed exploiting CVE-2022-47986 affecting IBM’s Aspera Faspex file-sharing solution. In hindsight, file transfer platforms are an obvious target for ransomware groups — they can contain high volumes of sensitive data, and they offer the potential to compromise organizations at scale.

In 2023, ransomware groups, including the newly identified ALPHV ransomware gang UNC4466, also exploited vulnerabilities in backup software for initial access to networks. UNC4466 targeted Veritas Backup Exec, a data recovery solution for small and medium businesses, exploiting three vulnerabilities that were patched in 2021. Cuba ransomware gang attacked critical infrastructure organizations in the US and IT firms in Latin America by exploiting a newer, but already-patched vulnerability, CVE-2023-27532, in Veeam Backup & Replication, Veeam’s proprietary backup application developed for virtual environments. Although CVE-2023-27532 was patched in March 2023, Cuba Ransomware Gang conducted the campaign in June 2023. By exploiting CVE-2023-27532, the threat actors were able to extract credentials from configuration files, enabling access to the backup infrastructure hosts.

### Evolution of Cyber Threats

#### Early Malicious Use of Generative AI Focuses on Social Engineering, Influence Operations

Generative artificial intelligence (AI) is a paradigm-shifting technology that is already widely used; for example, over 95% of smartphone users have used AI through the use of voice assistants like Alexa or Siri. The breakout of generative AI in 2023 has led to a surge in new services — while defenders have experimented with AI for threat intelligence, incident response, and code patching, cybercriminal and nation-state threat actors are experimenting with novel ways to enable and amplify their tactics using AI.

Currently, the most tangible risks associated with generative AI are linked to influence operations, social engineering, data privacy breaches, and intellectual property violations. Security researchers have observed threat actors using AI-powered chatbots to craft convincing phishing emails, support scam operations, and analyze e-commerce merchants’ anti-fraud systems to facilitate payment fraud. More sensationalized fears, such as AI autonomously developing and executing complex cyberattack strategies, remain largely speculative and have not been observed in the wild.

An emerging concern still not fully understood is the potential misuse of uncensored LLMs. A study by Indiana University conducted at the end of 2023 uncovered fourteen LLMs for malicious services that were generally advertised as subscription services similar to ChatGPT Plus, and 198 malicious open-source LLM projects advertised on the dark web. Many of these models advertise the ability to produce malware, create phishing emails, and construct ready-to-use scam sites. However, it must be reiterated that there have not yet been definitive, comprehensive studies on the real-world use or impact of AI-created malware, phishing, or scam sites.

While it is almost certain that threat actors will eventually be able to exploit AI for more sophisticated attacks, this capability will take time to mature. Like legitimate practitioners, cyber threat actors almost certainly had to wrestle with generative AI’s limitations in 2023, such as “hallucinations”, processing power, context window limitations, and the need for problem- and sector-specific datasets. The complexity of effectively integrating AI into advanced cyber threat operations requires not just access to LLMs, which is now nearly