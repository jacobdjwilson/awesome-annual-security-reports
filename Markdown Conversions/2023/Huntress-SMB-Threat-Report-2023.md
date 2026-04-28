# SMB Threat Report 2023

## Table of Contents
- [Executive Summary](#executive-summary)
- [Quarterly Summary](#quarterly-summary)
- [Intrusion Trends](#intrusion-trends)
- [Identity-Focused Security](#identity-focused-security)
- [Adversary Tooling & Behaviors](#adversary-tooling--behaviors)
- [Adversary Trends](#adversary-trends)
- [Additional DarkGate Observations & Software Impersonation](#additional-darkgate-observations--software-impersonation)
- [Continued AsyncRAT Infections & Process Chains](#continued-asyncrat-infections--process-chains)
- [Espionage in the SMB Environment](#espionage-in-the-smb-environment)
- [Response & Defensive Guidance](#response--defensive-guidance)
- [Conclusions](#conclusions)

---

## Executive Summary

While the world of cybersecurity often revolves around high-profile breaches and larger enterprises, this report stands apart with a unique mission: to prepare small and medium-sized businesses (SMBs) against the evolving tides of cyberthreats. At Huntress, we believe in empowering SMBs and the managed service providers (MSPs) who defend them with the knowledge, strategies, and tools needed to effectively protect themselves.

The contents of this report reflect the notable adversarial behaviors, tradecraft, and trends we saw over the third quarter of 2023. Our aim is for this report to serve as your resource to understand, adapt to, and take action against the threats that target SMBs and those who protect them.

In the past quarter, the Huntress team witnessed a continuing shift in the nature of threats against SMBs. Threat actors have largely moved away from malware-focused tactics. Instead, threat actors focus on non-malware mechanisms and abuse of legitimate tools and system commands in most incidents. Notably, 56% of recorded incidents in this time frame were, in essence, “malware free” across multiple types of intrusions. Of particular note is the increasing use of remote monitoring and management (RMM) software as an avenue of intrusion. In 65% of incidents, threat actors used RMM software as a method for persistence or remote access mechanisms following initial access to victim environments.

![Infographic showing 56% of incidents in Q3 2023 were malware free and 65% involved threat actors exploiting RMM software]

These trends are concerning, especially within the managed service provider (MSP) space. IT administrators, who rely on the same techniques and software that are now favored by threat actors, face an increasingly complex conundrum—distinguishing “good” from “bad” becomes a much more difficult task than it has been historically. Consequently, this may introduce an immediate need to move toward more behavior-based threat identification and a heightened focus on monitoring seemingly “legitimate” commands and software.

Furthermore, the migration toward cloud platforms and similar developments have placed an even greater premium on securing identities. Whether leveraged as an initial access mechanism through credential capture and replay, or for inbox access for information gathering, adversaries have migrated to cloud services along with end users to facilitate operations ranging from information theft to business email compromise (BEC) to pre-ransomware operations. Thus, MSPs and system owners need to extend their own visibility and security awareness beyond the traditional network perimeter to encompass external services and providers, as well as to fully capture the scope of identity-based actions and potential intrusions.

The following research reveals that the cybersecurity landscape for SMBs in Q3 2023 calls for a profound reassessment of defense strategies. The dominance of non-malware tactics, coupled with the exploitation of RMM software and identities, necessitates a nuanced approach to threat detection and response and expanding one’s security purview beyond conventional perimeters.

---

## Quarterly Summary

In Q3 2023, 40% of incidents responded to by Huntress analysts were categorized as “high” or “critical” in severity.

Reported items were distributed across Huntress monitoring mechanisms: Managed Endpoint Detection and Response and (increasingly) Managed Detection and Response for Microsoft 365. This multi-pronged approach to security monitoring and response enables Huntress to review adversary operations across the attack lifecycle—from initial access and exploitation, through lateral movement and persistence mechanisms, to final adversary actions in victim environments.

Through further analysis and refinement, Huntress researchers were able to discern overall trends in the threat landscape facing SMBs—a sector typically overlooked or ignored in threat reporting. Huntress researchers identified several notable trends in adversary operations facing the SMB space:

- **Decreased reliance on custom tools** and especially malicious binaries in intrusions until final actions, such as ransomware deployment. As a result, many classic mechanisms for identifying or mitigating threats (such as pure anti-malware solutions) are less effective for countering intrusions.
- **Increased reliance on malicious use of legitimate commands and tools**, with particular emphasis on RMM software. The shift to RMM (as well as built-in system commands) means greater emphasis must be placed on behavioral analysis of adversary operations for detection and response.
- **A highly diversified ransomware ecosystem** including many families and strains that do not appear to impact many enterprises or similar entities, but are commonly found in the SMB space. This includes a diverse ecosystem of ransomware entities beyond “headline” entities and many commodity strains that are often dismissed in large enterprise security models.

![Infographic highlighting decreased reliance on custom tools and increased reliance on legitimate tools]

---

## Intrusion Trends

Huntress focuses on defending the SMB—the organizations that are below the enterprise level and represent 99% of businesses in the US—and thus maintains distinct visibility from most other security firms. Within this visibility, we have identified continuing trends towards “living off the land” binaries (LOLBins) and credential compromise activity in Q3 2023. While custom or outright malicious tools still feature in events, adversaries are largely seeking to “blend in” to legitimate network operations through multiple mechanisms to evade detection and response.

At the SMB level, LOLBin use is especially concerning given the state of monitoring and review for many organizations. Many critical entities—from local school districts to medical offices—may find themselves at best leveraged for cryptomining or botnet purposes, and at worst, the victims of disruptive ransomware.

Figure 1 shows the distribution of tool “types” observed in Huntress-identified incidents, differentiating between compiled malware (e.g., a malicious EXE file), the use of scripting frameworks (such as PowerShell) for malicious activity, and the use of LOLBins and legitimate tools (including RMM software). While malware represents a significant portion of overall activity (44%), the remaining 56% of incidents are effectively “malware free.” Huntress thus observes a majority of incidents featuring LOLBin or similar abuse, or leveraging built-in scripting frameworks for actions.

![Figure 1: Breakdown of Tool Usage in Intrusions (44% Malware, 29% Non-Malware, 27% Scripting Object)]

56% of incidents were “malware free,” meaning adversaries opted for exploiting scripting frameworks or legitimate tools in place of malicious software.

The weaponization of legitimate tools, such as RMM tools in particular, remains an interesting and increasingly popular item in adversary arsenals. As reported by CISA and others, RMM abuse is increasingly popular in intrusions for several reasons:

- The applications in question are legitimate software, thus evading anti-malware solutions.
- Many organizations already run RMM software, allowing adversaries to “blend in” to the environment.
- RMM tool use is not typically audited, especially in small organizations, allowing for multiple RMM frameworks to be observed in the same environment. This diffusion of tools defeats potential detections, such as identifying a “new” RMM framework different from an existing baseline.

From Huntress observations, RMM and remote access tools are distributed among several frameworks, with ConnectWise ScreenConnect figured most prominently, as seen in Figure 2 below.[^1]

> **RMM**, or remote monitoring and management, IT software that helps MSPs proactively locate, update, and monitor client endpoints.

![Figure 2: Breakdown of Observed RMM Tools (56% ConnectWise, 18% AnyDesk, 13% NetSupport, 3% TeamViewer, 10% Other)]

[^1]: While ConnectWise ScreenConnect, AnyDesk, TeamViewer, and NetSupport are not technically RMMs, for simplification we are aligning with CISA’s categorization of these and similar tools.

---

## Identity-Focused Security

IT and business operations currently witness a growing importance of securing digital identities. Adversaries have set their sights on cloud services and identity-based attacks for initial access and the perpetration of fraud, such as business email compromise (BEC). These tactics have emerged as a favored intrusion vector for threat actors, and therefore should become a top priority for SMBs.

In Q3 2023, Huntress began rolling out its MDR for Microsoft 365 service. Even through initial trials and roll-out, Huntress has already observed a number of concerning trends in identity-based intrusions and manipulation, leading to actions such as mailbox manipulation and outcomes such as BEC. Unfortunately, data is not yet complete to enable trend analysis, but Huntress anticipates Microsoft 365 and related cloud targeting to continue growing as a concerning and popular intrusion vector through Q4 and into 2024.

Reviewing identified incidents, as seen in Figure 3, Huntress observes an overwhelming emphasis on identity-focused malicious activity. Identity is something to be stolen, spoofed, or manipulated—and adversaries increasingly focus on precisely these mechanisms. Primarily, we’ve seen a greater concentration on manipulating or compromising communication channels, such as setting up malicious forwarding or other inbox rules, which make up 64% of observed Microsoft 365 incidents. Other activity includes attempting to compromise accounts, as seen in 24% of cases with logons from unusual or suspicious locations.

![Figure 3: Breakdown of Microsoft 365 Incident Types (47% Suspicious Inbox Rule, 24% Suspicious Logon Location, 17% Suspicious Forwarding, 12% Other)]

---

## Adversary Tooling & Behaviors

Trends in adversary activity—both the specific tools leveraged in intrusions and the more general behaviors that these items support—are critical in mapping the threat landscape. Identifying commonalities in adversary tradecraft as well as the convergence of operations on increasingly standard techniques can be of great value to defenders in orienting visibility and threat detection.

Using the MITRE ATT&CK framework, Figure 4 shows the behaviors most often observed in Huntress-detected incidents for Q3 2023. Notably, in one quarter (25%) of incidents, abuse of scripting frameworks (T1059) shows continued adversary reliance on built-in tools such as PowerShell, WMI, and related items for intrusion operations.

![Figure 4: Breakdown of Adversary Intrusion Behaviors (25.3% Command and Scripting Interpreter, 20.7% Other, 9.1% User Execution, 8.0% Native API, 7.4% Remote Access Software, 6.4% OS Credential Dumping, 6.1% Ingress Tool Transfer, 6.1% Process Injection, 4.2% System Network Configuration Discovery, 3.6% Remote Services, 3.2% Software Discovery)]

As part of investigations as well as an integral feature of Huntress’ Managed EDR product, Huntress gathers antivirus (AV) detections in addition to analyst identification of malicious software or related tooling. The coordinated takedown of Qakbot in Q3 2023 represents one of the more significant events in the identified time period. As shown in Figure 5, we have observed a declining number of Qakbot-related incidents over 2023.

![Figure 5: Trends of Incidents Involving Qakbot by Quarter]

Aside from intermediate tooling, ransomware continues to be a scourge across all organizations. As seen in Figure 7, LockBit accounts for the majority of known-variant ransomware deployments observed by Huntress (25%). However, a long tail of uncategorized, unknown, or “defunct” strains make up the majority of all identified ransomware events (60%).

![Figure 7: Breakdown of Ransomware Families Observed (60% Other, 25% Lockbit, 5% BianLian, 3% Royal, 3% Akira, 2% INC, 1% BlackCat, 0.6% GrandCrab, 0.3% Hive, 0.2% Phobos, 0.2% MedusaLocker)]

---

## Adversary Trends

Adversaries continue to leverage a consistent triad of initial access techniques: user-targeted phishing activity, credential theft and replay, and external-facing system or application exploitation.

One of the key themes of Q3 2023 is an emphasis on “hot zero day summer”—a series of vulnerabilities disclosed in external-facing applications (such as MoveIT) or systems (such as VPN concentrators, firewalls, or email security gateways) enabling adversaries to rapidly establish presence in victim environments.

Adversaries continue to look for new payload mechanisms to deliver malicious content to end users. For example, TrueSec published on activity leveraging Microsoft Teams for distributing phishing links in early September 2023. Huntress identified similar activity between September 6–8, 2023, leveraging LNK objects masquerading as PDFs to encourage user interaction, resulting in the installation of DarkGate malware.

---

## Additional DarkGate Observations & Software Impersonation

Roughly simultaneously with the Teams-focused campaign described previously, DarkGate continued to evolve beyond direct phishing to likely search engine poisoning and social engineering victims to download legitimate software from malicious resources.

In observed intrusions, Huntress identified a variety of legitimate applications “spoofed” for delivering DarkGate payloads, such as:
- Advanced IP Scanner
- ColaSoft MAC Scanner
- Lightshot
- KeyScrambler

Notably, the malicious variants of the above software are provided as MSI files, whereas the legitimate versions available on company websites are all EXEs. After coercing or convincing a victim to download a malicious software package masquerading as a legitimate download, execution would result in an LNK created in the user’s StartUp folder as a persistence mechanism to load on start a DarkGate variant.

---

## Continued AsyncRAT Infections & Process Chains

AsyncRAT is a remote access tool (RAT) designed as an open-source RMM tool. In Q3 2023, Huntress observed convoluted infection chains starting with downloaded HTML files (likely delivered via phishing) leading to the download of password-protected archives.

![Figure 8: Infection and Process Chain of AsyncRAT (HTML -> Password Protected ZIP -> WSF Object -> PowerShell Script -> BITS Job -> Additional Archive -> VBScript Object -> PowerShell Script -> Scheduled Task)]

---

## Espionage in the SMB Environment

Huntress identified and responded to intrusions at a small enterprise in the defense industrial base (DIB) in Q3 2023. The intrusion, despite penetrating deep into the victim’s environment and having a dwell time of several weeks, did not result in ransomware or similar monetization behaviors. Instead, Huntress analysts observed systematic identification and collection of sensitive files related to defense projects.

Several lessons emerge from this activity:
- Sensitive areas of national economies, including the DIB, extend well into the SMB space.
- Intrusions into such organizations need not rely on exploits or exotic tradecraft to succeed.
- Increasing visibility and monitoring of such environments is necessary.
- Implementing increasingly standard security controls, such as MFA, are necessary steps in defeating intrusions.

---

## Response & Defensive Guidance

Visibility remains key to defense. Particularly given trends in adversary operations, relying more on abusing legitimate applications than distributing custom code and tools, the ability of organizations to identify and differentiate “malicious” from “normal” and “benign” is vital to enable meaningful, useful defense.

In line with the above trends, implementing MFA across all available systems (and especially ALL externally facing or publicly available systems) is now a minimally acceptable security measure. Defenders must assume that any single-factor authentication system exposed to the internet will be compromised eventually.

Beyond external access, legitimate credentials remain key to adversary operations following initial access. At minimum, organizations must look to enforce MFA for critical accounts such as local and (especially) domain administrator accounts, work to limit the use and access to these privileged accounts, and then audit their use to better identify their abuse by threat actors.

---

## Conclusions

Q3 2023 demonstrated that there is no slowdown in the information security space. More importantly, from a Huntress perspective, the landscape remains a difficult one for the majority of organizations that lack the resources and expertise residing in enterprise network environments.

The path forward entails a dual-pronged approach—enhancing visibility into events while simultaneously reducing the available attack surface. This adaptive approach is indispensable in coevolving with threat actors in today’s ever-changing cybersecurity landscape.

---

## About Huntress

Huntress is the leading cybersecurity partner for small and mid-sized businesses (SMBs) and the managed service providers that support them. Combining the power of the Huntress Managed Security Platform with a fully staffed 24/7 Security Operations Center (SOC), Huntress provides the technology, services, education, and expertise needed to help SMBs overcome their cybersecurity challenges and protect critical business assets.

© 2023 Huntress Labs Incorporated. All rights reserved.