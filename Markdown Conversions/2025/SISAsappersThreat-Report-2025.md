oup

2025-02-27

US

US

Recent Activity
• Feb 2025: Published stolen data from multiple Indian financial firms (e.g., Axis Bank,
Indiabulls) on its DLS.
• May 2025: Listed CheckCity.com as a victim, leaking customer loan and PII records.
• Ongoing: Active maintenance of a high-traffic Tor leak site; frequent updates to
victim lists with sample data dumps.

Tactics, Techniques & Procedures (TTPs)
Cl0p is known for its “big game hunting” approach, focusing on high-value data
exfiltration rather than mass encryption. Key TTPs include:
• Exploiting Zero-Day Vulnerabilities: Cl0p is highly skilled at identifying and
weaponizing vulnerabilities in managed file-transfer (MFT) software (e.g., MOVEit,
Accellion, GoAnywhere).
• Data-Only Extortion: Often skips the encryption phase entirely, focusing on
stealing sensitive data and threatening to leak it. This allows them to maintain a
lower profile and avoid triggering ransomware-specific alerts.
• Double Extortion: When encryption is used, they combine it with the threat of
publicly releasing stolen data on their DLS.
• Sophisticated Laundering: Cl0p uses complex money-laundering chains, including
mixing services and multiple cryptocurrency hops, to obfuscate ransom payments.

Attribution
Cl0p is widely attributed to the TA505 cybercrime group, a prolific Russian-speaking
threat actor. TA505 has been active for over a decade, evolving from banking trojans
(like Dridex) to large-scale ransomware operations. While the core members remain
elusive, their operational maturity and ability to exploit zero-day vulnerabilities suggest
a highly organized, well-funded criminal enterprise.

Risk Mitigation
Defending against Cl0p requires a focus on data protection and vulnerability
management:
• Patch Management: Prioritize patching for all MFT and edge-facing software.
Implement a rigorous vulnerability scanning program to identify and remediate
critical flaws before they can be exploited.
• Data Loss Prevention (DLP): Deploy robust DLP tools to monitor and block
unauthorized data exfiltration, especially from file-transfer servers and databases.
• Network Segmentation: Isolate critical data stores and MFT systems from the
broader corporate network to limit the impact of a potential breach.
• Access Control: Enforce strict least-privilege access and multi-factor authentication
(MFA) for all administrative and service accounts.
• Incident Response: Develop and test incident response plans specifically tailored to
data-extortion scenarios, including communication strategies and legal/regulatory
reporting requirements.

3.4. Lazarus Group (APT38)

Background
The Lazarus Group, also known as APT38, is a state-sponsored threat actor linked to
the Democratic People’s Republic of Korea (DPRK). Unlike typical ransomware gangs,
Lazarus is a sophisticated, nation-state-backed entity focused on generating revenue
for the regime through cyber-enabled financial theft. They are responsible for some of
the largest and most complex cyber heists in history, including the 2016 Bangladesh
Bank heist and the 2025 Bybit crypto exchange exploit.

Motive
Financial gain to support the DPRK regime, circumvent international sanctions, and
fund state-sponsored activities. Their operations are highly strategic, targeting
cryptocurrency exchanges, banks, and financial institutions globally.

Targeted BFSI Victims
Lazarus Group targets high-value financial entities, particularly those involved in
cryptocurrency and international banking. In 2025, they were linked to a $1.5 billion
exploit of the Bybit cryptocurrency exchange, demonstrating their ability to execute
large-scale, complex attacks on digital asset platforms.

Recent Activity
• 2025: Executed a $1.5 billion exploit of the Bybit cryptocurrency exchange.
• Ongoing: Continuous targeting of crypto exchanges, DeFi protocols, and
international banking systems.

Tactics, Techniques & Procedures (TTPs)
Lazarus Group employs advanced, multi-stage attack vectors:
• Spear-Phishing: Highly targeted, contextually relevant phishing campaigns
designed to compromise key personnel at financial institutions.
• Custom Malware: Development and deployment of sophisticated, custom-built
malware (e.g., backdoors, wipers, and financial trojans) to maintain long-term
persistence and exfiltrate data.
• Supply-Chain Attacks: Compromising third-party software or service providers to
gain access to the target’s network.
• Advanced Financial Fraud: Manipulating SWIFT systems, exploiting
cryptocurrency exchange vulnerabilities, and conducting complex money-laundering
operations.

Attribution
Lazarus Group is widely attributed to the North Korean government, specifically the
Reconnaissance General Bureau (RGB). Their operations are characterized by a high
level of technical sophistication, strategic planning, and alignment with the geopolitical
interests of the DPRK.

Risk Mitigation
Defending against a nation-state actor like Lazarus requires a comprehensive,
defense-in-depth approach:
• Advanced Threat Intelligence: Utilize high-quality threat intelligence to stay
informed about Lazarus Group’s evolving tactics, techniques, and indicators of
compromise (IOCs).
• Zero-Trust Architecture: Implement a zero-trust security model to minimize the
attack surface and prevent lateral movement.
• Behavioral Analytics: Deploy advanced behavioral analytics and AI-driven
anomaly detection to identify suspicious activity that signature-based tools might
miss.
• Rigorous Third-Party Risk Management: Conduct thorough security assessments
of all third-party vendors and software providers.
• Employee Awareness: Provide specialized training for high-risk personnel on
recognizing and reporting sophisticated spear-phishing and social-engineering
attempts.
• International Cooperation: Collaborate with law enforcement, intelligence
agencies, and industry partners to share information and coordinate defense
efforts.

04

Top Malware Campaigns & Indicators

4.1. AsyncRAT

Description: AsyncRAT is a remote access trojan (RAT) that has seen widespread use in
2025, particularly in phishing campaigns targeting the BFSI sector. It provides
attackers with full control over infected systems, including keylogging, screen
capturing, and file exfiltration capabilities.

Indicators of Compromise (IOCs):
- C2 Domains: [List of known malicious domains]
- File Hashes: [List of known malicious file hashes]
- Registry Keys: [List of known malicious registry keys]

4.2. Latrodectus

Description: Latrodectus is a sophisticated malware loader that has emerged as a
significant threat in 2025. It is often used to deliver secondary payloads, such as
ransomware or other malicious tools, and is known for its advanced evasion
techniques.

Indicators of Compromise (IOCs):
- C2 Domains: [List of known malicious domains]
- File Hashes: [List of known malicious file hashes]
- Registry Keys: [List of known malicious registry keys]

4.3. Emotet

Description: Emotet, a long-standing and highly resilient malware, continues to be a
major threat in 2025. It is primarily used as a downloader for other malicious payloads
and is known for its ability to spread laterally through networks.

Indicators of Compromise (IOCs):
- C2 Domains: [List of known malicious domains]
- File Hashes: [List of known malicious file hashes]
- Registry Keys: [List of known malicious registry keys]

4.4. AgentTesla

Description: AgentTesla is a popular information-stealing malware that targets
credentials, browser data, and other sensitive information. It is frequently delivered
via phishing emails and is a common tool for initial access in BFSI-targeted attacks.

Indicators of Compromise (IOCs):
- C2 Domains: [List of known malicious domains]
- File Hashes: [List of known malicious file hashes]
- Registry Keys: [List of known malicious registry keys]

4.5. LockBit

Description: As noted in the threat actor section, LockBit ransomware continues to be
a major threat. Its indicators include specific file extensions, ransom note formats,
and unique encryption routines.

Indicators of Compromise (IOCs):
- Ransom Note Filename: [e.g., Restore-My-Files.txt]
- File Extensions: [e.g., .lockbit]
- C2 Domains: [List of known malicious domains]

4.6. Prilex POS Malware Variant

Description: Prilex is a specialized point-of-sale (POS) malware that targets payment
card data. A new variant in 2025 has shown enhanced capabilities for bypassing
chip-and-PIN security measures.

Indicators of Compromise (IOCs):
- File Hashes: [List of known malicious file hashes]
- Network Traffic Patterns: [Description of malicious traffic]

4.7. Cogui Phishing Kit

Description: Cogui is a highly effective phishing kit used to harvest credentials for
banking and financial platforms. It is known for its realistic templates and ability to
bypass some MFA implementations.

Indicators of Compromise (IOCs):
- Phishing URLs: [List of known phishing URLs]
- HTML/JS Patterns: [Description of malicious code patterns]

05

Top 5 Vulnerabilities of 2025

5.1. CVE-2025-22457

Description: A critical remote code execution (RCE) vulnerability in Ivanti Connect
Secure VPN gateways. Attackers have exploited this to gain initial access to corporate
networks.

Impact: Full system compromise, lateral movement, and data exfiltration.

5.2. CVE-2025-2783

Description: A sandbox escape vulnerability in the Google Chrome V8 engine. This
flaw allows attackers to execute arbitrary code outside the browser sandbox.

Impact: Remote code execution, potential for full system compromise.

5.3. CVE-2025-5419

Description: A critical vulnerability in the 7-Zip archive utility that allows for
Mark-of-the-Web (MotW) bypass. This enables attackers to execute malicious files
without triggering security warnings.

Impact: Increased success rate for phishing and malware delivery.

5.4. CVE-2025-42999

Description: A deserialization vulnerability in SAP NetWeaver. Attackers can exploit
this to execute arbitrary code on SAP application servers.

Impact: Full compromise of SAP environments, potential for data theft and
manipulation.

5.5. CVE-2025-0411

Description: A high-severity vulnerability in a widely used enterprise authentication
library that allows for authentication bypass.

Impact: Unauthorized access to sensitive systems and data.

---

oup

2025-02-27

interfactura.com

Interfactura.com

2025-02-27

morrisgroup.co

Morris Group

2025-02-12

cassinfo.com

Cass Information
Systems, Inc.

2025-02-10

-

-

MX

CO

CO

Recent Activity
2025 Q1–Q2: Multiple Indian BFSI institutions named on Cl0p’s DLS, alongside a
high-profile data dump from Qualys. Victim advisories included column-extraction
samples to prove authenticity.

30

Tactics, Techniques & Procedures (TTPs)
Cl0p operators exploit zero-day flaws in file-transfer systems. In 2023 they used a
SQL-injection in MOVEit (CVE-2023-34362) to deploy the “LEMURLOOT” web shell and
steal files. Prior campaigns used zero-days in Accellion FTA (2020–21) and GoAnywhere
MFT (2023). Once inside, Cl0p exfiltrates data through its C2 infrastructure but often
does not deploy any ransomware payload – the victim’s files remain intact. The stolen
data is listed on its Tor DLS (“CL0P^_-LEAKS”) with a countdown. Cl0p has a history of
quadruple extortion: data theft, publication threats, plus DDoS and stakeholder
harassment, but in practice the tech side is “stick a webshell, grab data, post leaks.” Its
toolkit includes off-the-shelf RATs (FlawedAmmyy, FlawedGrace), and it often uses highly
credentialed phishing lures to gain initial access.

Attribution
Cl0p is widely attributed to the Eastern-European criminal group TA505. CISA and FBI
note that Cl0p’s operators are part of TA505, one of the largest phishing-and-malware
syndicates globally. In fact, CISA calls Cl0p “TA505” when discussing its MOVEit
campaigns. A known alias is “Graceful Spider” (per CrowdStrike). Analysts have linked
Cl0p to sophisticated criminal networks with possible Russian-speaking members, but as
with LockBit no intelligence agency has publicly blamed a specific country. U.S.
advisories simply treat Cl0p as a top-tier ransomware gang (albeit one that often skips
encryption).

Risk Mitigation
CISA/FBI have published specific guidance for Cl0p, focusing on the exploited MFT
systems. Key mitigations include patching or isolating vulnerable file-transfer software
(apply vendor fixes to MOVEit, Accellion, GoAnywhere, etc.). Limit exposure: if you must
run MFT servers, avoid internet-facing deployments and monitor for any signs of
compromise (unexpected IIS endpoints, novel web shells). In general, practice rigorous
cyber hygiene: take inventory of all assets, whitelist only approved applications, and
grant admin privileges sparingly. Segment the network so that even if an MFT server is
breached, attackers cannot wander freely. Keep up-to-date network monitoring – log
and alert on suspicious port usage and external communications. Maintain up-to-date
patching and vulnerability scans. Continuously review and revoke any unknown accounts.
And, as always, maintain secure offsite backups.

Security Note
Because Cl0p often publishes stolen data without warning, organizations should also
consider data governance measures (e.g. encryption at rest of sensitive data, strict access
controls) and be prepared for breach response even if encryption hasn’t occurred.
Victims should promptly involve law enforcement; FBI/CISA advisories contain IoCs for
Cl0p breach campaigns.

31

3.4. Lazarus Group (APT38)

Background - The Lazarus Group, specifically its financially-focused subgroup APT38
(a.k.a. TraderTraitor in FBI parlance), is a North Korean state-sponsored cybercrime team
that has been active since at least 2009. Operating under the DPRK’s Reconnaissance
General Bureau, APT38 conducts large-scale thefts from banks and cryptocurrency
platforms to fund Pyongyang’s nuclear and missile programs. Notoriously cunning,
Lazarus employs both custom malware and human-intensive intrusion techniques.

Motive - State-directed fundraising. Lazarus’s goal is to steal money (fiat or crypto) for
the North Korean government’s illegal weapons programs. This is espionage-motivated
theft rather than personal gain. The group is sanctioned globally (OFAC designated
Lazarus/ APT38 in 2019, and its cyber-heists are considered acts of economic warfare.

Targeted BFSI Victims - In 2025 APT38 scored several high-profile cryptocurrency heists.
On February 21, 2025, the FBI publicly confirmed North Korean hackers stole ~$1.5
billion worth of cryptocurrency from Bybit – the largest crypto heist ever recorded. (The
FBI bulletin identified “North Korea” – calling them “TraderTraitor” – as responsible for
this massive breach Then on May 9, 2025, Taiwanese exchange BitoPro disclosed an
$11.5 million loss to a hacker, publicly attributing it to the Lazarus Group. (BitoPro’s
forensic analysis found the attackers had compromised a cloud admin account and
deployed crypto-stealer malware.) Both victims are crypto exchanges (BFSI-equivalent
targets) handling large user funds. Lazarus has also historically hit conventional banks
(SWIFT heists) and other financial infrastructure, though the 2025 incidents were all
crypto-based.

Recent Activity -
• Feb 21, 2025: Conducted the largest crypto heist ever, stealing $1.5 billion from Bybit

cold-to-hot wallet transfers; FBI confirmed Lazarus attribution and released 51
Ethereum addresses for sanctions blocking.

• May 9, 2025: Exploited a vulnerability in BitoPro’s internal tooling to exfiltrate $11.5
million; BitoPro publicly confirmed the incident and invoked emergency forensics.

32

Tactics, Techniques & Procedures (TTPs) -
Lazarus uses highly targeted, multi-stage attacks. Typical elements include:
• Developer/cloud credential compromise: For Bybit, investigators reported that

Lazarus hacked the exchange’s developer environment and multisig wallet setup,
allowing them to initiate fraudulent transactions from cold wallets. Similarly, BitoPro’s
breach began with social-engineering into a cloud engineer’s AWS account, followed
by malware that grabbed hot-wallet key. In short, they subvert the signing process for
transactions.

• Custom malware and scripts: Lazarus deploys in-house tools (e.g. “FallChill”

backdoors, “FastCash” trojans) tailored to financial networks. These backdoors give
persistent access to exchange infrastructure.

• Layered laundering: After theft, Lazarus uses thousands of intermediate wallets and

mixers to obscure the crypto trail. (The FBI even published a list of over 60 Ethereum
addresses linked to the Bybit theft and urged providers to block them).

• No ransomware: Unlike the above actors, Lazarus’s operations are pure theft, not

extortion via encryption. There is no ransom note – they simply steal assets directly.

Attribution
Law enforcement unambiguously attributes these thefts to North Korea’s Lazarus/
APT38. The FBI’s February 2025 alert explicitly names the DPRK and uses the code name
TraderTraitor for this actor. Security news outlets likewise report that Lazarus was behind
Bybit and BitoPro, citing FBI and independent analyses. The U.S. government long ago
identified Lazarus as part of DPRK’s Reconnaissance General Bureau (sanctioned as an
“agency or instrumentality” of the DPRK).

33

Risk Mitigation
Defending against Lazarus requires both cybersecurity and financial controls:
• Protect wallet infrastructure: Enforce strict governance over cryptocurrency wallets.
Use multi-signature cold wallets requiring multiple hardware keys. Keep private keys
in Hardware Security Modules or physically air-gapped devices. Rotate and lock down
keys after any suspected compromise.

• Harden development/devops environment: As Lazarus used stolen dev credentials in
these incidents, secure the entire software development pipeline. Enforce MFA and
strict access controls for all cloud accounts (e.g. AWS IAM), and regularly audit any
privileged sessions. Limit third-party code and thoroughly vet any crypto software
updates.

• Monitor blockchain activity: Use blockchain analytics to watch for suspicious

movement of funds. The FBI has published dozens of crypto addresses linked to
Lazarus thefts, exchanges and coin services should block or flag transactions involving
these addresses. Proactively collaborate with regulators to trace and freeze illicit
transfers.

• General security: Regularly patch and update all software, especially systems related

to transactions. Employ network segmentation: isolate systems handling crypto wallet
keys from general enterprise networks. Maintain comprehensive monitoring and
incident response plans.

• Sanctions compliance: Ensure all financial dealings comply with international sanctions

on DPRK. Report any contacts or transactions that may involve sanctioned
individuals/addresses.

34

04

Top Malware Campaigns & Indicators

Others

Latrodectus

24%

5%

8%

AgentTesla

Estimated 2025
malware market share

LockBit

33%

10%

AsyncRAT

20%

Emotet

4.1. AsyncRAT

Behavior and Capabilities: A modular Windows remote-access trojan (RAT) first seen in
2019, now widely used in targeted campaigns. AsyncRAT is typically delivered via
spear-phishing, often using obfuscated JavaScript or shortcut files. For example, recent
attacks used malicious JScript (e.g. Lana_Rhoades_Photoos.js) and zipped LNK/BAT files
hosted on trusted platforms (Dropbox, Cloudflare) to launch the RAT. Once running, it
performs in-memory injection (e.g. into addinprocess32.exe) to evade disk detection. Its
command channel often uses DNS tunneling or legitimate cloud services (e.g. Google
Drive, paste.ee) for C2. AsyncRAT can exfiltrate system info, download plugins, capture
screenshots, terminate processes, and update itself. It also uses WMI and nested
PowerShell to bypass execution policies.

Attack Chain & Tactics: Typical chain: Initial Access via phishing (malicious script).
Execution happens through script hosts (cscript/wscript) or PowerShell (T1059.001) that
launch the RAT. It may create mutexes for Persistence (T1050) or use token manipulation
for Privilege Escalation (T1134, e.g. enabling SeDebugPrivilege). Defense Evasion is
achieved by injecting into other processes (T1055) and by masquerading as benign
traffic (C2 over DNS/TLS). C2 Communication uses application-layer protocols
(T1071.004) such as DNS or HTTPS channels (e.g. Google Drive URLs). Its broad toolkit
maps to ATT&CK techniques like phishing (T1566), command-shell execution (T1059),
injection (T1055), and DNS tunnel (T1071.004).

35

Tactic

Technique

MITRE ID

Initial Access

Phishing (malicious JScript)

Execution

Persistence

Privilege Escalation

Command-Line Interface
(PowerShell, cscript)

Create/Modify System Process
(mutex)

Access Token Manipulation
(SeDebugPrivilege)

Defense Evasion

Process Injection

T1566

T1059

T1050

T1134

T1055

C2 (Command &
Control)

Application Layer Protocol: DNS

T1071.004

Detection & Prevention:
• Network Rules: Block or monitor known AsyncRAT infrastructure, e.g. the IP

148.113.165.11 on port 3236 (observed in C2 traffic and domains like paste.ee used
to stage payloads Inspect and block unusual DNS requests or cloud-storage URLs
from endpoints.

• Endpoint Monitoring: Alert on script hosts (cscript.exe or mshta.exe) spawning

PowerShell or unknown executables. Enforce PowerShell Constrained Language
Mode and strict execution policies. Disable unused WMI subsystems and regularly
audit for unexpected WMI/WBEM scripts.

• YARA/IOCs: Deploy YARA rules tuned for AsyncRAT payloads (e.g. known AsyncRAT
function strings or loader patterns). Monitor for the creation of mutexes indicative of
AsyncRAT (if known).

• User Education: Phishing awareness (e.g. don't click suspicious links/attachments)

helps prevent the initial script download.

Usage & Targets:
AsyncRAT has been notably active in early 2025. It ranked #4 on Check Point’s Global
Threat Index for Feb 2025. Analysts report it is especially used against IT,
telecommunications, and education sectors. The malware’s use of trusted services
(Dropbox, Cloudflare tunnels) makes detection challenging, so defenders should pay
special attention to anomalous use of those services.

36

4.2. Latrodectus

Behavior and Capabilities - Latrodectus is a stealthy Windows loader/downloader first
identified in late 2023. It often arrives via small downloader scripts or MSI installers (for
example, a malicious MSI can spawn msiexec.exe, which then launches a hidden “NVIDIA
Notification” process that loads the Latrodectus payload). Once running, it immediately
self-deletes using an Alternate Data Stream (ADS) trick: the loader renames its own
executable into an ADS (suffix like :wtfbbq) and schedules it for deletion via Windows
APIs. This leaves little forensic trace. Latrodectus then fetches a secondary payload over
HTTPS (typically on port 443) – often ransomware or an info-stealer. The loader persists
by creating a registry Run key (HKCU\...\Run) to relaunch on login. Internally, Latrodectus
uses string obfuscation (XOR/loops), dynamic WinAPI resolution, and sandbox checks
(e.g. process count, ptrace detection) to hinder analysis.

Attack Chain & Tactics - A representative chain is: Initial Access via malicious email link
or attachment that runs a JS/VBS/Msi script. Execution often involves a hidden window
or script interpreter (T1059) launching msiexec or powershell to load the payload.
Persistence is via the Run key (T1547.001) so it restarts at logon. Defense Evasion is
shown by the ADS self-deletion (Indicator Removal T1070.006). C2 and payload
download occur over standard HTTPS (non-standard ports are not really needed since
443 is standard; however, because traffic looks normal it’s harder to flag). The malware’s
TTPs include Run key persistence, ADS deletion, and encrypted HTTP communication.

Tactic

Technique

MITRE ID

Defense Evasion

Indicator Removal on Host (ADS)

T1070

Persistence

Registry Run Keys

T1547.001

C2 Communication

Non-Standard Port (HTTPS/443)

T1571

Impact

Data Manipulation (payload
download)

T1565

37

Detection & Prevention
• Network Filtering: Block or monitor known malicious domains and IPs used by
Latrodectus affiliates (for example, agrahusrat[.]com or minrezviko[.]com have
been observed). Use SSL/TLS inspection if possible to spot unusual downloads.

• Filesystem Monitoring: Alert on processes using low-level file APIs to

manipulate ADS (e.g. calls to SetFileInformationByHandle with a stream name
like ":wtfbbq"). Detect and log hidden-window executions where a download
is immediately run.

• Registry/Startup: Monitor creation of new Run keys under
HKCU\Software\Microsoft\Windows\CurrentVersion\Run.

• YARA Rules: Use YARA signatures tailored for Latrodectus payloads or known

obfuscation artifacts.

• Sandbox Evasion: Encourage use of behavior-based EDR; since Latrodectus
uses sandbox checks, malicious samples might delay payload, so use longer
observation windows in dynamic analysis.

Usage & Targets
Latrodectus emerged strongly in Q1 2025. It is frequently used as an initial loader
for follow-on malware (ransomware, info-stealers). Reports indicate banking and
corporate networks are common targets. Its stealth features (ADS deletion) make
quick detection difficult, so organizations should watch for its characteristic
behaviors (ADS file operations, hidden MSI executables).

4.3. Emotet

Behavior and Capabilities
Emotet is a notorious modular trojan/loader active since 2014, originally a banking
trojan that evolved into a general-purpose loader. Emotet resurgence (post-2021)
continues into 2025. It primarily spreads via malicious Office documents (Word or
Excel) or even OneNote files. These documents contain macros or scripts that
launch VBS/PowerShell payloads. For example, one variant drops a VBS (click.wsf)
that runs a heavily obfuscated PowerShell to download an Emotet DLL into
C:\ProgramData\*.dll, then executes it with regsvr32.exe. Once active, Emotet
typically installs itself as a hidden Windows service (e.g. TnsZbP.dll) under
System32, and also copies its core DLL (named like E.dll) to %AppData%\Local. It
uses regsvr32.exe as a proxy (T1218.010) to sideload and execute its DLLs. Emotet
deletes Zone.Identifier marks to evade SmartScreen, and often deletes volume
shadow copies to prevent recovery. It uses elliptic-curve cryptography
(ECDH/ECDSA) to secure C2 communications. Emotet modules can enumerate
processes and network configuration, and even inject code into legitimate
Windows tools (e.g. hollowing certutil.exe) to harvest credentials

38

Attack Chain & Tactics -
Emotet’s chain is typically: Delivery via an email with an Office document (macro or
script enabled) (T1566/T1204). Execution: macro drops and runs a script
(VBS/WSF), which runs encoded PowerShell to fetch the Emotet payload Lateral
Movement: After initial infection, Emotet may use stolen credentials or exploit
SMB/RDP internally. Persistence: creates a new Windows service (T1050) and may
set Run keys. Privilege Escalation/Evasion: uses regsvr32.exe (T1218.010) to run
payloads invisibly, and can disable Defender or UAC if needed. Discovery: spawns
systeminfo.exe and ipconfig.exe to gather host details. C2/Exfiltration: uses
WinHTTP to connect to multiple hardcoded C2 servers over HTTPS (T1071). It
downloads additional modules (Keylogger, banking trojans, etc.) via HTTP GET.
Emotet’s activities map to many ATT&CK techniques (new service T1050, hidden
window T1143, process hollowing T1055.012, system/network discovery
T1082/T1016, encrypted C2 T1071.001).

TTPs (MITRE ATT&CK)

Tactic

Technique

MITRE ID

Persistence

New Service

Defense Evasion

Hidden Window

Defense Evasion

Software Packing

Discovery

Process Enumeration

C2 Communication

Application Layer Protocols
(HTTPS, custom ports)

T1050

T1143

T1045

T1057

T1071

Detection & Prevention -
• E-Mail Security: Filter inbound emails for malicious attachments, especially

Office files with macros. Sandboxed detonation of suspicious attachments can
catch the macro-initiated PowerShell.

• Blocklists: Block connections to known Emotet C2 IPs (e.g. 173.249.25.219,

212.83.184.188).

• Process Monitoring: Alert on unusual use of regsvr32.exe. For example, a Word
process spawning regsvr32 /s *.tmp.dll  is suspicious. Monitor for new services
being created by non-privileged users.

39

• Execution Control: Disable or restrict use of regsvr32.exe and wscript.exe unless
needed. Constrain Office macro execution policy (e.g. block or require user
approval).

• YARA/Signatures: Deploy YARA rules targeting Emotet (e.g. rules looking for

“EmotetFunctionStrings” used in its modules).

• Integrity Monitoring: Watch for changes to registry Run keys, hidden service DLLs, or

deletion of VSS snapshots (indicative of ransomware follow-on).

• Network Monitoring: Use EDR/NDR to detect beaconing or unusual TLS connections

to foreign IPs from regsvr32.exe.

Usage & Targets
Emotet remains among the most persistent loaders in 2025, rebuilding itself after
takedowns. It predominantly targets financial services, government agencies, and
education/healthcare. Global telemetry  has shown Emotet campaigns hitting diverse
industries worldwide. Its versatility (as a dropper for other payloads) makes it a
widespread threat.

4.4. AgentTesla

Behavior and Capabilities
AgentTesla is a .NET-based credential-stealer RAT (also called OriginLogger) that has
been continually updated through 2025. It’s commonly sold on underground forums
(subscription-based “MaaS”). Upon infection, it often installs itself as a Windows service
and may disable User Account Control by setting the registry EnableLUA = 0 (bypassing
UAC; MITRE T1088). AgentTesla hooks into processes by allocating large executable
memory regions (RWX) for code injection (observed in jsc.exe or explorer.exe), allowing it
to capture keystrokes and screenshots. It harvests stored credentials from browsers,
email clients, FTP clients, and files (Credential Access T1081). Notably, AgentTesla uses
multiple C2 channels for exfiltration: it frequently sends stolen data via SMTP (email), but
also supports HTTP POST and even Telegram-based exfil. For example, a recent sample
was observed sending data to finalrestingplace.net on port 587 (SMTP). Internally,
AgentTesla may also gather network info (T1016) to profile the host.

40

Attack Chain & Tactics - Commonly distributed via phishing emails with malicious
attachments (often malicious executables or PDFs). When run, it may drop files and
modify the registry for persistence. Execution: the service or injected process runs
AgentTesla’s payload (T1059). Persistence: often via a new Windows service entry.
Defense Evasion: bypasses UAC (T1088) and may elevate privileges (T1087). Discovery:
performs local network and system enumeration (T1016). Credential Access: scans
browser data and files for passwords (T1555.003/ T1081). Exfiltration: uses one-way
outbound channels like SMTP, FTP, HTTP POST, or even encrypted messaging APIs
(T1041). Because the data is typically exfiltrated to legitimate servers (e.g. mail providers
or Telegram APIs), network defenders must rely on content inspection or detection of the
AgentTesla message formats.

TTPs (MITRE ATT&CK)

Tactic

Technique

MITRE ID

Defense Evasion

Bypass UAC via Registry

Privilege Escalation

Enable Process Privileges

T1088

T1087

Discovery

Network Configuration Discovery

T1016

Credential Access

Credentials in Files

Execution

Windows Management
Instrumentation

T1081

T1047

Detection & Prevention -
• Network Monitoring: Block/monitor outbound SMTP on unusual mail servers. For
example, block traffic to finalrestingplace.net (108.179.232.90:587), a known
AgentTesla SMTP host. Use Zeek/Suricata rules to look for AgentTesla-specific email
patterns (Corelight’s blog shows regex for its SMTP format). For HTTP, search for
unusual POST to “*.php” endpoints carrying base64-encoded payloads. For Telegram
C2, it is very hard to distinguish from normal Telegram SSL traffic, but monitoring for
large encrypted uploads to Telegram might help.

• Registry/OS: Alert on changes to HKLM\...EnableLUA or similar UAC settings. Watch

for creation of new services by non-standard processes.

41

• Memory/Process: Detect large RWX allocations or injector behavior in processes like
jsc.exe or script hosts. Monitor for known AgentTesla strings (e.g. SMTP banner
patterns) in memory.

• YARA Rules: Deploy YARA rules for AgentTesla signatures (many variants share core

code).

• Email Gateway: As with others, block or sandbox suspicious attachments and disable

macros/scripting where possible.

• Password Hygiene: Since AgentTesla targets credentials, enforce strong credential

policies and use MFA to reduce impact.

Usage & Targets -
AgentTesla remains a daily active stealer in 2025. It’s been found in campaigns against
organizations of all sizes. Sector-wise, it often hits healthcare, manufacturing, and retail
entities (where stolen creds and internal data are valuable). A Bitsight study notes that
AgentTesla is prevalent worldwide and mainly spreads by email attachments. Its modular
builder and frequent updates mean defenders must stay vigilant to new variants.

4.5. LockBit

Behavior and Capabilities:  LockBit is a leading ransomware-as-a-service (RaaS) that
first appeared as “ABCD” in Sept 2019 and rebranded to LockBit in 2020. It has since
evolved (LockBit 2.0, 3.0/Black, 4.0, etc.) and remains highly prolific. LockBit’s payload
encrypts files system-wide with strong crypto (AES/RSA), appending randomized
extensions (e.g. .wxacdzitl) to encrypted files. Upon execution, LockBit often replaces
the desktop wallpaper and drops ransom notes (e.g. restore-my-files.txt). It aggressively
deletes backups by wiping volume shadow copies (VSS) on Windows (Inhibit System
Recovery, ATT&CK T1490). To spread in a network, affiliates frequently use stolen admin
credentials and tools like Cobalt Strike to move laterally (ATT&CK T1021.002). LockBit’s
affiliates will often inject into explorer.exe or svchost.exe to locate and encrypt network
shares. It also typically attempts to disable security software (e.g. forcibly terminating or
uninstalling Windows Defender)

Attack Chain & Tactics: The chain may begin with phishing or exploiting a public-facing
system to gain Initial Access. Privilege Escalation: stolen credentials grant domain admin
rights. Discovery: scanning for file servers and drives (T1135) to maximize encryption.
Lateral Movement: via SMB/Remote Services (T1021.002) as noted. Defense Evasion:
stops security services, and obfuscates file names by random extensions (T1027).
Impact: heavy data encryption (T1486) on local and mapped drives, effectively a
ransomware wiper when combined with shadow-copy deletion (T1490). Unlike pure
wipers, LockBit typically also exfiltrates data for double-extortion.

42

TTPs (MITRE ATT&CK)

Tactic

Impact

Technique

MITRE ID

Data Encryption

Discovery

Network Share Discovery

Defense Evasion

File Obfuscation (random
extensions)

Credential Access

Credentials in Files

T1486

T1135

T1027

T1081

Detection & Prevention -
• File Monitoring: Look for sudden mass file changes or the appearance of novel

extensions (e.g. many files renamed to *.wxacdzitl). Alert on large-volume file writes
or encryption patterns.

• EDR/Process: Detect the characteristic process injection into explorer.exe/svchost.exe
(LockBit often runs inside these processes) and scanning of network shares. Monitor
for high CPU or file I/O on these processes.

• Service & VSS Monitoring: Watch for VSSAdmin commands deleting shadows. Alert if

volume snapshot services stop.

• Access Controls: Strictly limit domain admin and service account privileges (principle

of least privilege). Use dedicated jump servers for admin tasks. Network
segmentation to prevent easy SMB lateral spread. Disable legacy protocols (SMBv1)
and block SMB traffic where not needed.

• Backups: Maintain offline, immutable backups. Since LockBit removes online backups,

offline copies are critical.

• Incident Response: If ransomware is detected (rapid encryption), isolate the affected

system immediately.

• Awareness: Train users to avoid phishing and ensure timely patching of external

systems (many LockBit infiltrations began with known exploits).

Usage & Targets -
LockBit has been the single most active ransomware group globally. In 2022 it was
responsible for ≈50% of all ransomware incidents observed (often quoted as ~44%). It
continues to dominate in 2025. The group targets healthcare and critical infrastructure
prominently, as well as financial services, manufacturing, and government organizations.
(LockBit’s own rules even forbid attacks on critical power and post-Soviet countries.)
Because of its scale and affiliate model, LockBit will remain a top threat into 2025.

43

4.6. Prilex POS Malware Variant

Description:  A Brazilian-origin POS malware family, Prilex, has evolved to perform
"ghost transactions." The installer (GB.exe) deploys multiple executables and scheduled
tasks, registers malicious DLLs, and later injects into POS software to intercept live card
transaction data. Upon detecting a transaction, it requests a fresh ARQC from the
victim's card, captures PAN/CVV/expiry, then exfiltrates via HTTP to dynamic-DNS
domains (amazoncrime-001-site1.htempurl[.]com).

Why It Matters
• Ghost transactions use legitimate cryptograms, evading authorization anomalies
• Physical installer vectors (social-engineered "POS update") bypass remote defense

Recommendations
• File Integrity Monitoring: Alert on unexpected new task-scheduler entries or

suspicious DLL registrations

• Network Egress Controls: Block HTTP/S to known dynamic-DNS providers
• Script/Batch-File Auditing: Investigate VBS and BAT files creating persistence under

%TEMP%

Latest Signatures / IoCs:
• File: GB.exe (v06.03.8080)
• AV Detection Name: HEUR:Trojan.Win32/64.Prilex
• C2 Domain: amazoncrime-001-site1.htempurl[.]com
• NFC Block String: "Contactless error, insert your card"

4.7. Cogui Phishing Kit

Description:  Cogui is a Phishing-as-a-Service offering that sent over 580 million
phishing emails between January and April 2025. It provides turnkey phishing kits, email
templates, and a dashboard parsing campaign emails. The operation primarily targets
Japan but also affects the United States, Canada, Australia, and New Zealand. Clients
purchase access on Telegram, send phishing lures to targeted domains (email providers,
banks), and harvest credentials for resale or immediate fraud.

Why It Matters
• Lowers operational barrier: no coding needed for large-scale credential theft
• Real-time dashboarding accelerates campaign optimization
• Volume represents the highest phishing campaign currently tracked by major security

firms

44

05

Top 5 Vulnerabilities of 2025

Major new vulnerabilities discovered in early 2025 have been rapidly weaponized by
attackers. Notably, an unauthenticated stack overflow in Ivanti Connect Secure
(CVE-2025-22457) and a zero-day in Chrome’s V8 engine (CVE-2025-5419) were both
exploited in the wild. This report highlights five CVEs (January–July 2025) that were
most frequently observed across threat intelligence sources and added to CISA’s Known
Exploited Vulnerabilities (KEV) catalog. Key risks include remote code execution bugs in
enterprise appliances, browser engines, and deserialization flaws, as well as a
security-bypass in a popular archiver. Immediate patching of affected products is
strongly recommended to counter active attacks.

• Remote RCE in enterprise VPN/gateway appliances: Ivanti Connect Secure/Policy
Secure/ZTA appliances have a critical stack-based overflow (CVE-2025-22457)
allowing unauthenticated RCE.

• Chrome/Chromium sandbox escapes: Two critical Chrome flaws (CVE-2025-2783,

CVE-2025-5419) enable remote code execution via malformed files or web content.
These high-severity zero-days were actively exploited (e.g. by the “TaxOff” group)
before patches were issued.

• SAP NetWeaver deserialization: A flaw in the Visual Composer uploader

(CVE-2025-42999, CVSS 9.1) lets privileged users trigger deserialization and RCE on
NetWeaver hosts. Onapsis reported it being chained with another SAP bug and
abused in the wild.

• Trusted tool bypass (Mark-of-Web): 7-Zip’s MotW protection was defeated

(CVE-2025-0411) so that malicious archives run code without warnings. Attackers
used this in phishing campaigns (e.g. delivering SmokeLoader malware via
spear-phish) to stealthily execute malware.

CVSS Vector Key

• AV (Attack Vector): N = Network
• AC (Attack Complexity): L = Low
• PR (Privileges Required): N = None
• UI (User Interaction): R = Required
• S  (Scope): U = Unchanged
• C  (Confidentiality): L = Low
• I  (Integrity): N = None
• A  (Availability): N = None

45

Rank

CVE ID

Date Added

Affected Product

Brief Description

01

CVE-2025-2
2457

2025-04-04

Ivanti Connect Secure,
Policy Secure, ZTA
Gateways

02

CVE-2025-2
783

2025-03-27

Google Chrome (Mojo
sandbox on Windows)

03

CVE-2025-5
419

2025-06-05

Google
Chrome/Edge (V8
JavaScript engine)

04

CVE-2025-4
2999

2025-05-15

SAP NetWeaver Visual
Composer Metadata
Uploader

05

CVE-2025-0
411

2025-02-06

7-Zip

Stack-based buffer
overflow allowing
unauthenticated RCE
(remote code
execution).

Sandbox escape via
bad handle in Mojo
(Chrome
<134.0.6998.177)
enabling remote code
execution.

Out-of-bounds
read/write in V8
(Chrome
<137.0.7151.68) leading
to heap corruption and
RCE.

Insecure
deserialization
(privileged user)
enabling RCE on
NetWeaver hosts.

Mark-of-the-Web
bypass (archive
handling flaw) allowing
execution of malicious
files.

46

5.1. CVE-2025-22457

• About: A stack-based buffer overflow in Ivanti Connect Secure (<22.7R2.6), Policy

Secure (<22.7R1.4) and ZTA Gateways (<22.8R2.2) permits remote, unauthenticated
attackers to execute arbitrary code. This critical flaw (CVSS 9.8) was quickly exploited
in the wild (Google/Mandiant ties it to China-linked actors). It was added to CISA’s
KEV on April 4, 2025.

• Risk Score: NVD 9.8 (Critical); Vector:

CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H.

• Exploit Status: Yes – active exploitation observed (CISA KEV, Mandiant). Full root RCE

PoC was later demonstrated.

• Recommendation: Patch immediately. Upgrade Ivanti Connect Secure to 22.7R2.6,
Policy Secure to 22.7R1.4, and ZTA Gateways to 22.8R2.2. CISA advises applying
these patches by the April 11, 2025 KEV deadline and performing threat-hunting on
any unpatched devices.

5.2. CVE-2025-2783

• About: A Chromium Mojo sandbox escape in Google Chrome on Windows (fixed in
Chrome 134.0.6998.177) allows remote attackers to escape the browser sandbox via
a crafted filen. The flaw arises from an incorrect handle being provided to Mojo,
leading to privilege escalation. It was a zero-day exploited by the TaxOff group in
March 2025 to deploy the Trinper backdoor. CISA added it to KEV on March 27, 2025
(due April 17).

• Risk Score: CVSS 8.3 (High).
• Exploit Status: Yes – used in active attacks (phishing>exploit chain) by APT (TaxOff).
• Recommendation: Update to Chrome/Chromium 134.0.6998.177 or later immediately
(patch was released March 25, 2025). Until patching, avoid loading untrusted files and
employ rigorous email/URL filtering to block the exploit.

47

5.3. CVE-2025-5419

• About: A critical out-of-bounds read/write flaw in Chrome’s V8 JavaScript engine

(affecting Chrome/Edge before 137.0.7151.68) enables remote heap corruption and
code execution via a malicious web page. Google issued an emergency patch on
June 5, 2025. This high-severity (CVSS 8.8) zero-day was actively weaponized in the
wild. CISA’s KEV lists it on June 5 (due June 26).

•  Risk Score: CVSS 8.8 (High).
•  Exploit Status: Yes – publicly confirmed in-the-wild exploitation (added to KEV). A

public PoC also exists.

•  Recommendation: Upgrade Chrome/Edge to version 137.0.7151.68 (or later) by

June 26, 2025. As an interim measure, restrict untrusted HTML content or enforce
strict Content Security Policies to mitigate exploitation.

5.4. CVE-2025-42999

• About: An insecure deserialization bug in SAP NetWeaver Visual Composer

Metadata Uploader (fixed by SAP Security Note 3604119 on May 13, 2025) can be
abused by a privileged user to execute arbitrary code on NetWeaver servers. This
flaw (CVSS 9.1) was observed chained with another SAP zero-day (CVE-2025-31324)
to give attackers unauthenticated RCE capability. CISA added CVE-2025-42999 to
the KEV on May 15, 2025 (due June 5).

•  Risk Score: CVSS 9.1 (Critical).
•  Exploit Status: Yes – actively exploited (confirmed by CISA/Onapsis; used by

ransomware/APT).

•  Recommendation: Apply SAP Security Note 3604119 immediately to patch the

deserialization flaw. Also review Visual Composer usage: disable it if not needed or
restrict uploads to trusted administrators to reduce attack surface

48

5.5. CVE-2025-0411

• About: A “Mark-of-the-Web” bypass in 7-Zip (patched in version 24.09) fails to tag
extracted files as untrusted. When a user opens a specially crafted archive, the
extracted files execute as if coming from a trusted source. This allows malicious
scripts or executables to run without warning, facilitating arbitrary code execution.
Attackers have leveraged this in phishing campaigns (using Spoofed filenames) to
deliver malware (e.g. SmokeLoader, ransomware). CISA added it to KEV on Feb 6,
2025 (due Feb 27).

•  Risk Score: CVSS 7.0 (High).
•  Exploit Status: Yes – actively exploited. Firms reported Spear-phish attachments

exploiting this flaw to deploy malware without user suspicion.

•  Recommendation: Update 7-Zip to v24.09 or later immediately (fix issued Feb 7,

2025). As a workaround, disable automatic MotW file extraction or enforce archive
scanning via endpoint protections to block malicious archives.

Recommendations
• Universal 2FA: Wherever possible, enforce FIDO2/WebAuthn over SMS-based OTPs
• Email Authentication: Strict DMARC, DKIM, SPF enforcement at the domain level
• Phishing-Simulation Training: Regularly unannounced tests to reinforce user

skepticism

5. Conclusion

The 2025 threat landscape makes clear that cyber resilience in the BFSI sector hinges on
three pillars: rapid vulnerability response, layered defense, and collaborative intelligence
sharing. As adversaries exploit everything from POS malware and phishing-as-a-service
to zero-day flaws in widely used appliances and applications, organizations can no
longer afford patch backlogs or siloed security teams. Proactive patch management,
applying fixes for Ivanti, Chrome/Edge, SAP NetWeaver, 7-Zip and similar software
within CISA’s KEV timeframes, must be institutionalized alongside multi-factor
authentication, network segmentation, immutable backups, and robust incident
response playbooks. Only by marrying relentless vulnerability hygiene with
threat-informed detection and cross-sector cooperation can financial institutions
withstand the sophisticated, fast-moving attacks that define today’s digital battlefield.

49

References

• https://www.trmlabs.com/resources/blog/lockbit-leak-provides-insight-into-raas-enter

prise

• https://icoholder.com/en/news/crypto-heist-lazarus-group-steals-1-4b-from-bybit
• Victoria’s Secret Security Incident Shuts Down Lingerie Giant’s Systems - CPO

Magazine

• https://threatprotect.qualys.com/2025/03/26/google-chrome-zero-day-vulnerability-e

xploited-in-the-wild-cve-2025-2783/

• https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/cve-2025-54

19-out-bounds-readwrite-vulnerability-v8

• https://www.dbtsupport.com/2025/05/15/sap-netweaver-zero-day-cve-2025-31324-4

2999-exploited/

• M&S cyber attack: What we know about it and its impact
• https://www.cvedetails.com/cve/CVE-2025-5419/
• https://nvd.nist.gov/vuln/detail/CVE-2025-22457
• https://onapsis.com/blog/active-exploitation-of-sap-vulnerability-cve-2025-31324/
• https://cybelangel.com/banking-cybercrime-2025/
• https://www.techtarget.com/searchSecurity/news/366619872/FBI-Lazarus-Group-beh

ind-15-billion-ByBit-heist

• https://www.quorumcyber.com/threat-intelligence/critical-chrome-zero-day-vulnerabil

ity-cve-2025-2783/

• https://cymulate.com/blog/akira-ransomware/
• https://www.picussecurity.com/resource/blog/akira-ransomware-analysis-simulation-a

nd-mitigation-cisa-alert-aa24-109a

• https://cyberint.com/blog/dark-web/cl0p-ransomware/
• https://cybersecuritynews.com/cl0p-ransomware-attacking-telecommunications/
• https://gbhackers.com/cl0p-ransomware-launches-large-scale-attacks/
• https://foresiet.com/blog/cl0p-ransomwares-reign-of-cyber-extortion-analyzing-the-re

cent-cleo-software-exploits

• https://www.s-rminform.com/cyber-intelligence-briefing/cyber-intelligence-briefing-2

1-march-2025

• https://gbhackers.com/akira-ransomware-dominates-january-2025/
• https://icoholder.com/en/news/lazarus-hack-targets-bybit-stealing-1-4-billion-in-crypt

o

• https://coinmarketcap.com/academy/article/bybit-ceo-declares-war-on-lazarus-group

-and-launches-dollar140-million-bounty-after-dollar14-billion-hack

• https://www.webasha.com/blog/unmasking-akira-the-global-impact-of-rising-cyber-th

reat

• https://www.linkedin.com/pulse/lockbit-ransomware-gang-announces-comeback-40-s

et-launch-amul-patel-n1uze

50

• https://en.wikipedia.org/wiki/LockBit
• https://www.bitcoininsider.org/article/268839/lazarus-group-heist-north-korean-hacke

rs-steal-14b-bybit-exchange

• https://ubuntu.com/security/CVE-2025-0411
• https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/cve-2025-27

83-google-chrome-sandbox-escape

• https://threatprotect.qualys.com/2025/06/03/google-fixes-third-zero-day-vulnerabilit

y-in-chrome-cve-2025-5419/

• https://www.rapid7.com/blog/post/2025/04/03/etr-ivanti-connect-secure-cve-2025-2

2457-exploited-in-the-wild/

• https://forums.ivanti.com/s/article/April-Security-Advisory-Ivanti-Connect-Secure-Poli

cy-Secure-ZTA-Gateways-CVE-2025-22457

• https://www.cisecurity.org/advisory/a-vulnerability-in-google-chrome-could-allow-for-

arbitrary-code-execution_2025-031

• https://arcticwolf.com/resources/blog/follow-up-cve-2025-42999/
• https://www.acaglobal.com/industry-insights/urgent-patching-required-address-7-zip

-mark-web-bypass-vulnerability/

• https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/43999109/

85e4cd3d-1034-417f-be87-3d45f5a230b0/paste.txt

• https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/43999109/

7e1058d9-ed8d-4893-a43f-183ad3e5fb94/paste.txt

• https://en.wikipedia.org/wiki/Akira_(ransomware)
• https://gbhackers.com/cl0p-ransomwares-exfiltration-process-exposes-rce-vulnerabili

ty/

• https://fieldeffect.com/blog/second-zero-day-in-sap-netweaver-actively-exploited
• https://digital.nhs.uk/cyber-alerts/2025/cc-4610
• https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-5419
• May 28 2025 Exploit Post-Mortem - Cork
• https://www.reuters.com/business/insurer-aflac-discloses-cybersecurity-incident-2025

-06-20/

• https://www.hipaajournal.com/erie-insurance-cyberattack/
• https://www.msdlegal.com/blog/2025/06/philadelphia-insurance-companies-cyberatt

ack-class-action-investigation/

• https://www.insurancejournal.com/news/east/2025/07/02/830032.htm
• https://news.trendmicro.com/2025/06/21/aflac-data-breach/
• https://www.hindustantimes.com/cities/pune-news/fir-in-connection-with-fake-shanes

hwar-devasthan-apps-duping-devotees-101752518765805.html

• https://www.businessinsider.com/return-fraud-amazon-shipping-retail-theft-wardrobin

g-online-shopping-2025-7

• Mastercard, VISA and American Express

51

SISA

SISA is a global forensics-driven cybersecurity solutions company, trusted by leading
organizations for securing their businesses with robust preventive, detective, and
correctivecybersecurity solutions. Our problem-first, human-centric approach helps
businesses strengthen their cybersecurity posture. We apply the power of forensic
intelligence and advanced technology to offer true security to 2,000+ customers in 40+
countries.

Compliance

Security Testing

Cyber Defense

Data Protection &
Governance

Trainings &
Certiﬁcations

Leading
Tech Security

Payment Data Security

Application Security

• Application Penetration

Testing

• CREST/CERT-in

Approved Security
Testing

• API Security Testing
• Secure Code Review

Network Security

• Vulnerability
Assessment

• Penetration Testing

• Configuration Review
• Firewall Rule Review

• PCI ASV Scan

Phishing Simulation

Red Teaming Exercise

• Layer Security Testing

• PCI DSS

• PCI PIN

• PCI 3DS
• PCI P2PE

• PCI S3
• PCI S-SLC

• PCI CP (Card Production)
• Facilitated PCI SAQ

• Quarterly Health

Check-ups

• Central Bank Compliance
• SWIFT

Strategy and Risk

• CCPA
• GDPR

• HIPAA
• ISO

• NIST
• SOC 1

• SOC 2
• Cloud Security

• HITRUST

Unified Audits

Managed Compliance

Managed Extended
Detection and Response
Solution - SISA ProACT

•

 24x7 Monitoring

• UEBA

•

Threat Intel

•

•

•

•

Advanced Threat Hunting

Breach &
Attack Simulation

SOAR

Use-case Factory

Digital Forensics and
Incident Response

• Incident Response /

Compromise
Assessment Services

• Forensic Readiness

Audit

• Forensic and Incident
Response Retainer
Service

• Payment Forensics

Investigation

• Internal Forensics

Investigation

• Ransomware Simulation

Payment Data Security
Training and ANSI
Accredited Certiﬁcation

•

•

•

•

•

CPISI ( 2 Day Program

CPISI ( 3 Day Program)

CPISI- Advanced (3 Day
Program)

CPISI-D (Developers)

CPISI Hybrid (4 Weeks)

Certiﬁcation Program
in Cybersecurity for
AI – CSPAI

•

•

CSPAI

CSPAI - Developers

Forensic Brieﬁng
Sessions for Senior
Management

AI PRISM

•
•

•
•

•
•

AI PRISM LLM
Vulnerability Scanner
Solution

AI Risk Management and
Governance Solution
Framework

AI Compliance and
Governance Consulting
Service

Hardware and IoT
Security Testing

•
•

•
•

•
•

•
•

Firmware Security
Testing

Hardware/Embedded
Security Testing

IoT Network Security
Testing

IoT/Embedded
Application and
Management Layer
Security Testing

•
•

MPOC/ PCI PTS

Quantum Security

•
•

•
•

•
•

Quantum Cryptographic
Consulting

Quantum Security Risk
Assessment

Quantum Security
Standards Compliance

Data Discovery and
Classification

•

•

•

•

•

PCI/PII/PHI Data
Discovery

Data Classification in
Endpoint (Windows,
Linux)

Data Classification in
O365, Metadata

Dynamic Masking,
Redact, Truncation

Integration to DRM, DLP,
SIEM

Data Privacy
Professional Services

•

•

•

•

•

Assessments (Unified
Privacy Maturity, DPIA,
3rd Party Risk)

Data Inventory, Mapping
and Process flow, RoPA

Data Privacy Framework -
Policy, Notice, SoPs

Consent and Notice
Management framework

Data Breach and
Management

•

Principal management

•

•

•

•

Privacy by Design
implementation guide

Define Data Retention
Guidelines and processes

Technical/Organization
measures

Privacy
Training/Awareness

For more Information visit us at www.sisainfosec.com
or
write to us at contact@sisainfosec.com

52