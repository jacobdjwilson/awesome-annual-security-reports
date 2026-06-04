# CrowdStrike 2026 Global Threat Report

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Threat Landscape Overview](#threat-landscape-overview)
- [Key Adversary Themes](#key-adversary-themes)
  - [Adversaries Leverage AI to Enhance and Accelerate Operations](#adversaries-leverage-ai-to-enhance-and-accelerate-operations)
  - [Ransomware Adversaries Expand Cross-Domain Tradecraft](#ransomware-adversaries-expand-cross-domain-tradecraft)
  - [China-Nexus Threat Actors Target Network Perimeter Devices for Initial Intrusions](#china-nexus-threat-actors-target-network-perimeter-devices-for-initial-intrusions)
  - [Supply Chain Attacks Enable Evasion of Traditional Security Controls](#supply-chain-attacks-enable-evasion-of-traditional-security-controls)
  - [Adversary Objectives Shape Zero-Day Exploit Selection](#adversary-objectives-shape-zero-day-exploit-selection)
  - [Adversaries Subvert Trust in Cloud Platforms and Services](#adversaries-subvert-trust-in-cloud-platforms-and-services)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [CrowdStrike Falcon Platform, Products, and Services](#crowdstrike-falcon-platform-products-and-services)

---

## Foreword
### The Age of the AI Adversary Begins
The world is operating in the agentic era. Artificial intelligence is embedded across the modern enterprise. Agents write code, analyze data, orchestrate workflows, and make decisions at machine speed. Every layer of the enterprise is becoming faster and more automated.

The adversary is operating in the agentic era as well. In 2025, AI-enabled adversaries increased attacks by 89% year-over-year. AI accelerated phishing and automated reconnaissance, shortening the time from initial access to impact. It elevated less sophisticated threat actors and amplified the most advanced ones. It compressed the time between intent and execution.

AI has also introduced a new dimension of risk: adversaries targeting the very AI systems underpinning the modern enterprise. As AI is embedded into development pipelines, SaaS platforms, and operational workflows, AI systems themselves become part of the attack surface. Adversaries exploited legitimate AI tools by injecting malicious prompts that generated unauthorized commands. As innovation accelerates, exploitation follows. Security must parallel the slope of innovation. In the agentic era, cybersecurity is the foundational infrastructure required to protect AI itself.

The data in this year’s Global Threat Report makes clear that speed is now the defining characteristic of intrusion, and it has fundamentally reshaped how adversaries evade detection.

The average eCrime breakout time fell to 29 minutes in 2025, a 65% increase in speed from the prior year. The fastest breakout took just 27 seconds. In one intrusion, data exfiltration began within four minutes of initial access. The window to detect, decide, and respond has narrowed dramatically.

In 2025, evasion was defined by the speed at which adversaries exploit trust. Adversaries operated through valid credentials, trusted identity flows, approved SaaS integrations, and inherited software supply chains. Notably, 82% of detections were malware-free. Intrusions moved through authorized pathways and trusted systems, blending into normal activity.

This evasive model extended across multiple domains. Adversaries exploit visibility gaps created by fragmented security controls (across identity, SaaS, cloud, and unmanaged devices), chaining together access paths to stay off well-protected endpoints.

Cloud-conscious intrusions rose 37% in 2025, including a 266% increase among state-nexus threat actors. Valid account abuse accounted for 35% of cloud incidents, reinforcing that identity has become central to intrusion. Zero-day exploitation prior to public disclosure increased 42%, compressing the time between vulnerability discovery and active exploitation.

China-nexus activity increased 38% in 2025. In 67% of the vulnerabilities China-nexus adversaries exploited, the flaw provided immediate system access. Of those exploited vulnerabilities, 40% targeted internet-facing edge devices. Newly disclosed vulnerabilities were weaponized within days.

Together, these trends show how modern adversaries operate: gain legitimate access through identity, move rapidly through cloud and edge infrastructure, and weaponize vulnerabilities before defenders can respond. Speed, legitimacy, and low-visibility access paths now define evasive tradecraft.

At CrowdStrike, we built our platform on the understanding that data is the foundation of both AI and cybersecurity. We process trillions of real-time events across endpoints, cloud workloads, identities, and networks. We correlate that telemetry with adversary intelligence and years of labeled tradecraft to detect and disrupt threats at scale. This data advantage allows us to connect signals across domains, identify evasive behavior early, and act decisively before adversaries achieve their objectives.

In the agentic era, defending against AI-accelerated adversaries, and securing AI systems themselves, requires operating at machine speed.

The CrowdStrike 2026 Global Threat Report reflects this reality. It provides the intelligence defenders need to understand how adversaries exploit trust, accelerate with AI, and move across domains to remain evasive.

Our mission remains unchanged. We stop breaches. In the agentic era, that mission requires a single platform with the architecture to reason and act at the speed of the adversary, while securing the AI-powered enterprise.

![CrowdStrike CEO and Founder]

---

## Introduction
Throughout 2025, adversaries grew more evasive than ever before. As defenses became more sophisticated, threat actors increasingly exploited the inherent trust in supply chain partners, legitimate software, internal systems, and employees to gain initial access and move undetected. This relentless targeting of trusted relationships defines 2025 as the year of the evasive adversary.

Adversaries of all motivations exploited AI technology throughout 2025 to accelerate, optimize, and troubleshoot their existing techniques. Demonstrating increasing fluency with AI tools, adversaries used the technology for attack types such as social engineering and information operations (IO). Most that integrated AI increased their attack volume compared to 2024; there was an 89% increase in the number of attacks by AI-enabled adversaries year-over-year.

Throughout 2025, big game hunting (BGH) adversaries continued to dominate the eCrime landscape by driving high-impact ransomware operations while tailoring tradecraft to exploit security blind spots and evade detection. Highly evasive threat actors such as SCATTERED SPIDER and BLOCKADE SPIDER challenged defenders by rapidly moving laterally across traditional servers, hypervisors, cloud environments, unmanaged hosts, and SaaS applications, underscoring the growing threat of cross-domain attacks.

Supply chain attacks also emerged as a defining tactic. Rather than targeting victims directly, threat actors increasingly compromised upstream providers, development ecosystems, and public code repositories to gain broad, stealthy access across downstream organizations. In February 2025, PRESSURE CHOLLIMA executed the largest single financial theft ever reported when they stole 1.46 billion USD worth of cryptocurrency through trojanized software delivered via a supply chain compromise.[^1] This demonstrates how abuse of trusted technology relationships can rapidly translate into large-scale financial and operational damage.

[^1]: https://www.ic3.gov/psa/2025/psa250226; https://www.elliptic.co/blog/bybit-hack-largest-in-history

Other Democratic People's Republic of Korea (DPRK)-nexus adversaries’ activity also surged in 2025; FAMOUS CHOLLIMA’s 2025 activity doubled compared to 2024, and STARDUST CHOLLIMA significantly increased their operational tempo over the year. These brazen and prolific operations comprise a cluster of DPRK-nexus adversaries acting undeterred by global law enforcement actions. CrowdStrike Intelligence assesses that DPRK-nexus adversaries will pose an acute threat to fintech, technology, and Western defense entities in 2026.

Zero-day exploitation increased significantly in 2025 as adversaries weaponized dozens of these vulnerabilities for initial access, remote code execution (RCE), and privilege escalation. CrowdStrike observed a 42% year-over-year increase in the number of zero-day vulnerabilities exploited prior to public disclosure, continuing a multi-year trend of rising zero-day abuse.

Cloud-conscious threat actors employed new techniques throughout 2025, favoring speed and broad access across environments. eCrime adversaries targeted hybrid identity technologies to gain privileged access to cloud and on-premises identities, while state-nexus threat actors favored stealthier initial access vectors. MURKY PANDA gained access to various victim environments via compromised trust relationships, while COZY BEAR abused legitimate Entra ID authentication flows through targeted phishing.

In parallel with these broader trends, China-nexus adversaries continued dominating the global threat landscape with attacks on nearly every region and sector. Compared to 2024, CrowdStrike observed a 38% increase in overall China-nexus targeted intrusion activity; in particular, attacks targeting logistics increased by 85%, telecommunications by 30%, and financial services by 20%. China-nexus adversaries systematically exploited vulnerabilities in network edge devices (including VPN appliances, firewalls, and gateways) to establish long-term access for intelligence collection. And 67% of the vulnerabilities they exploited in 2025 were RCE flaws that provided immediate system access. In several cases, China-nexus adversaries weaponized newly disclosed vulnerabilities within days of their public release.

These themes illustrate a threat environment defined by speed, scale, and sustained evasion. Adversaries increasingly combine trusted access paths, AI-enabled acceleration, and cross-domain movement to operate below traditional detection thresholds. Human-only analysis struggles to keep pace, and effective defense depends on the ability to rapidly connect intelligence, telemetry, and context into decisive action.

Identifying and stopping the evasive adversary is challenging, but it’s not impossible. CrowdStrike Counter Adversary Operations combines threat intelligence, managed threat hunting, and trillions of telemetry events from the AI-powered CrowdStrike Falcon® platform to detect, disrupt, and stop evasive adversaries.

Counter Adversary Operations comprises two closely integrated teams. The CrowdStrike Intelligence team identifies new adversaries, tracks malicious activity, and captures emerging cyber threat developments in real time. The CrowdStrike OverWatch team applies this intelligence through proactive threat hunting across customer telemetry to detect and address malicious activity. Together, these teams help protect organizations from sophisticated adversaries by delivering intelligence and threat hunting capabilities that most organizations cannot replicate internally.

This was the Counter Adversary Operations team’s most ambitious year yet for both vision and product innovation. CrowdStrike advanced its Threat AI vision to help scale analysis and reduce the time required to investigate complex activity. AI agent-based techniques now support tasks such as malware analysis and threat hunting, enabling analysts to more quickly assess activity, correlate intelligence, and determine appropriate responses. These capabilities are designed to support human analysts by automating time-intensive steps and revealing relevant context during investigations.

This vision also influences how intelligence is delivered and consumed. Enhancements such as personalized views, organization-specific context, expanded investigation tooling, and the CrowdStrike Threat Intelligence Browser Extension make intelligence immediately usable in operational workflows where decision-makers must act with speed and confidence.

Recognizing that adversaries pivot to unmanaged entry points to bypass defenses, CrowdStrike expanded the CrowdStrike Falcon® Adversary OverWatch™ managed threat hunting service to third-party CrowdStrike Falcon® Next-Gen SIEM data, extending visibility across the full attack surface beyond endpoint, identity, and cloud.

Together, these innovations reflect CrowdStrike’s commitment to outpacing adversaries, empowering security teams with actionable intelligence, and dramatically reducing the time between detection and effective response.

![24 new adversaries named in 2025, including Belarus adversary UMBRAL BISON; 281 total adversaries now tracked by CrowdStrike; 150 active malicious activity clusters and emerging threat groups tracked]

---

## Threat Landscape Overview
CrowdStrike named 24 new adversaries in 2025, bringing the total tracked to 281, signifying a larger and more complex threat landscape. Adversaries continue to become faster, stealthier, and more effective as they adapt to navigate larger environments and bypass stronger security controls. The below trends define 2025 as the year of the evasive adversary.

- **89% increase** in attacks by AI-enabled adversaries.
- **00:27**: Average eCrime breakout time dropped to 29 minutes, a 65% increase in speed from 2024, and the fastest breakout time was only 27 seconds.
- **82% of detections** in 2025 were malware-free, up from 51% in 2020.
- **281 total adversaries**: 24 new adversaries tracked by CrowdStrike.
- **China-nexus activity increased 38%** across all sectors, with an 85% increase in logistics.
- **42% increase** in zero-day vulnerabilities exploited prior to public disclosure.
- **Valid account abuse** accounted for 35% of cloud incidents.
- **37% rise** in cloud-conscious intrusions, with 266% increase among state-nexus threat actors.

### The Growing Dominance of Interactive Intrusions
Interactive intrusions continued to expand in 2025 as adversaries increasingly favored direct human-driven attacks over traditional malware-based attacks. In these intrusions, threat actors engage directly with victim environments, using legitimate credentials, native tools, and administrative functions to move laterally and achieve objectives while blending into normal user behavior.

![Interactive intrusions by region chart]
![Top 10 industries targeted by interactive intrusions chart]

### Breakout Time: The Race Against Adversaries
Once adversaries gain initial access, their next objective is to “break out” and move laterally from the initial foothold to high-value assets. The speed of this “breakout time” determines how fast a defender must respond to reduce the costs and damages associated with an intrusion.

![Average eCrime breakout time chart 2021-2025]

### CHATTY SPIDER: Initial Access to Exfiltration in Four Minutes
CHATTY SPIDER continued to primarily target law firms in 2025, leveraging voice phishing (vishing) campaigns to persuade targeted employees to download and install remote monitoring and management (RMM) tooling. After gaining access via the RMM tooling, CHATTY SPIDER typically downloaded the file transfer tool WinSCP and used it in an attempt to exfiltrate data to adversary-controlled infrastructure.

![Timeline of CHATTY SPIDER intrusion]

### Fake CAPTCHA Campaigns Surge in Popularity During 2025
In 2025, many criminal actors shifted from malicious browser update-related lures to fake CAPTCHA lures to entice victims to download and execute malware.

![Criminal use of malicious browser update lures and fake CAPTCHA lures chart]

---

## Key Adversary Themes

### Adversaries Leverage AI to Enhance and Accelerate Operations
Throughout 2025, adversaries increasingly targeted AI systems and incorporated the technology into their intrusion tradecraft, social engineering activity, and IO campaigns.

![AI model mentions in forums in 2025 chart]

By misusing these AI models, threat actors can enhance their capabilities and adopt techniques beyond their existing areas of expertise. Moderately resourced threat actors, such as PUNK SPIDER, highly likely benefit the most from using AI in their operations.

#### AI-Enhanced Threats
In 2025, there was an 89% increase in attacks by AI-enabled adversaries year-over-year.

![AI threats across the kill chain chart]

#### Technical Operations
Threat actors use AI to accelerate malware development, generate code, and create exploits. In an example of threat actors evading AI model safeguards to accelerate malware development, CrowdStrike Intelligence has identified two ransomware variants, FunkLocker and RALord, that share encryption flaws specific to templates generated by the unrestricted AI model WormGPT.

### Ransomware Adversaries Expand Cross-Domain Tradecraft
In 2025, ransomware disrupted organizations’ operations, inflicted financial losses, and caused reputational damage. Sophisticated adversaries such as SCATTERED SPIDER appeared in mainstream news headlines for high-impact attacks against aviation, insurance, and retail targets.

![SCATTERED SPIDER leverages unmanaged VMs to dump credentials diagram]

### China-Nexus Threat Actors Target Network Perimeter Devices for Initial Intrusions
Throughout 2025, China-nexus adversaries demonstrated a systematic preference for targeting network perimeter and edge devices as initial access vectors.

![Summary of 2025 trends in China-nexus targeted intrusion activity diagram]

#### Rapid Exploit Weaponization Defines 2025 Operations
In 2025, China-nexus adversaries demonstrated they can consistently operationalize publicly disclosed exploits within days of an exploit’s release.

![Rapid exploit weaponization by China-nexus adversaries chart]

---

## Conclusion
The 2025 threat landscape was defined by the evasive adversary—a threat actor that leverages speed, legitimacy, and cross-domain movement to bypass traditional security controls. As adversaries continue to integrate AI into their operations and exploit the inherent trust in modern enterprise infrastructure, the window for detection and response will continue to narrow. Organizations must prioritize visibility across all domains, including identity, cloud, and unmanaged assets, to effectively counter these sophisticated threats.

---

## Recommendations
1. **Adopt a Unified Security Platform**: Consolidate security tooling to eliminate visibility gaps across endpoints, cloud, identity, and network.
2. **Prioritize Identity Security**: Implement robust multi-factor authentication and monitor for anomalous identity behavior, as valid account abuse is a primary vector for intrusion.
3. **Secure the AI Pipeline**: Treat AI systems as critical infrastructure; implement rigorous access controls and monitoring for AI-specific components, models, and agents.
4. **Accelerate Patch Management**: Given the rapid weaponization of vulnerabilities, prioritize patching for internet-facing edge devices and critical infrastructure.
5. **Leverage Managed Threat Hunting**: Utilize proactive threat hunting services to identify and disrupt adversaries that operate below traditional detection thresholds.

---

## CrowdStrike Falcon Platform, Products, and Services
The CrowdStrike Falcon® platform provides the comprehensive visibility and intelligence required to stop breaches in the agentic era. By combining real-time telemetry, AI-powered analytics, and expert-led threat hunting, CrowdStrike empowers organizations to outpace the adversary and secure the modern enterprise.

---

hina’s business
hours. These adversaries’ deployment of custom malware families and maintenance of global infrastructure indicate
state-level resource allocation to support intelligence collection activities.
TARGETING PRIORITIES ALIGN WITH
STRATEGIC INTELLIGENCE REQUIREMENTS
China-nexus adversary targeting throughout 2025 reflected intelligence collection priorities aligned with Chinese
Communist Party strategic objectives, including telecommunications surveillance, economic espionage, and technology
transfer.
Consistent with previous years, specialized China-nexus threat actors primarily focused on telecom entities. OPERATOR
PANDA, for example, consistently targeted telecom providers between 2021 and July 2025. GENESIS PANDA also
targeted telecom entities in this time frame, focusing on East Asia, East Africa, and North America and likely seeking call
data records and network infrastructure access. China-nexus threat actors’ persistent telecom targeting indicates China
likely prioritizes communication interception capabilities.
WARP PANDA targeted U.S.-based legal, technology, and manufacturing entities, focusing on sectors containing valuable
intellectual property and trade secrets. HOLLOW PANDA’s operations targeted logistics, government, financial services,
energy, maritime, technology, and biomedical sectors across 10 countries. Targeting patterns align with the priorities
detailed in China’s 14th Five-Year Plan.
Geographically, China-nexus threat actors continued to heavily focus their operations on the Asia Pacific region, with
multiple adversaries targeting organizations in Australia, India, Indonesia, the Philippines, and Southeast Asia. VEILED
PANDA targeted a U.S.-based aviation entity in late 2025, exploiting a Windows Server Update Services (WSUS) RCE
vulnerability (CVE-2025-59287) before deploying ShadowPad.
6 An ORB network is a traffic relay system (generally composed of a mix of compromised devices and leased servers) used to obfuscate the
origin and destination of malicious traffic.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 30
CVE-2025-59287
On October 23, 2025, Microsoft issued an out-of-band patch
for CVE-2025-59287, which the company originally disclosed on
October 14, 2025. A remote, unauthenticated attacker can exploit
this vulnerability by sending a crafted event that triggers unsafe
object deserialization, which enables RCE on the targeted instance.
Only Windows servers with the WSUS server role enabled are
vulnerable to CVE-2025-59287 exploitation; by default, the WSUS
server role is disabled for Windows servers.
OUTLOOK
CrowdStrike Intelligence assesses that China-nexus adversaries will continue
targeting internet-facing appliances and edge devices for initial access operations
throughout 2026. This assessment is made with high confidence based on the
trend’s longevity in China-nexus targeted intrusion activity, the demonstrated
effectiveness of edge device exploitation for establishing persistent access, and
the continued availability of exploitable vulnerabilities in perimeter infrastructure.
As new vulnerabilities are disclosed, China-nexus adversaries will almost certainly
rapidly incorporate associated exploits, attempting both mass exploitation and
selective intrusion operations. These adversaries’ observed ability to consistently
begin exploitation rapidly after vulnerability disclosure throughout 2025 will likely
continue in 2026, placing organizations at significant risk in the brief time between
disclosure and patching.
This assessment assumes adversaries will continue using their current TTPs
rather than significantly alter their approaches. However, increased organizational
focus on edge device security could drive adversaries to explore alternative initial
access vectors.
»
Edge devices were targeted in 40% of cases in which a China-nexus adversary
exploited a vulnerability during an intrusion in 2025. Organizations in the telecom,
EDGE DEVICES WERE TARGETED
technology, legal, government, academic, and critical infrastructure sectors will
IN 40% OF CASES IN WHICH
likely continue to face elevated risk from China-nexus edge device targeting, as
A CHINA-NEXUS ADVERSARY
China-nexus activity targeting these sectors collectively increased 34% from EXPLOITED A VULNERABILITY
2024 to 2025. Given the rapid weaponization of vulnerabilities by China-nexus DURING AN INTRUSION IN 2025.
adversaries, defenders should prioritize patching edge devices within 72 hours of ORGANIZATIONS IN THE TELECOM,
TECHNOLOGY, LEGAL, GOVERNMENT,
critical vulnerability disclosure, implementing enhanced monitoring for edge device
ACADEMIC, AND CRITICAL
compromise indicators, and establishing network segmentation to limit lateral
INFRASTRUCTURE SECTORS
movement from compromised perimeter systems.
WILL LIKELY CONTINUE TO FACE
ELEVATED RISK FROM CHINA-NEXUS
By systematically compromising network perimeter infrastructure, China-nexus EDGE DEVICE TARGETING,
threat actors can continuously collect intelligence that supports China’s strategic AS CHINA-NEXUS ACTIVITY
TARGETING THESE SECTORS
objectives, including economic espionage, technology transfer, and telecom
COLLECTIVELY INCREASED 34%
surveillance. Edge device security is critical not only for individual organizations
FROM 2024 TO 2025.
but for national security, as compromised perimeter infrastructure can potentially
enable adversary access for months or years before detection.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 31
Supply Chain Attacks Enable Evasion of
Traditional Security Controls
Supply chain attacks represent a distinct security challenge. Because users trust that legitimate software
will not include malicious code and organizational patching policies will not inadvertently infect machines with
malware, adversaries can adopt methods that exploit this trust. Adversaries’ increased use of such methods in
2025 marks a shift in initial access techniques to focus on evading traditional security controls.
In supply chain attacks, threat actors modify software provider infrastructure or code bases in ways that obscure
threat activity, making them stealthy and challenging to detect. In some cases, supply chain attacks cause further
damage when untrusted code is incorporated into wider software ecosystems, infecting additional organizations
beyond the original target.
In 2025, CrowdStrike Intelligence detailed several supply chain attacks in which threat actors either compromised
software providers and manipulated their existing update mechanisms or obtained credentials for individual accounts
and then modified legitimate software packages in public code repositories.
Ultimately, both methods allow threat actors to execute code for deploying malware or executing malicious commands
that leak credentials. The threat actors can then exfiltrate sensitive data, compromise external systems, or steal
cryptocurrency. Several DPRK-nexus adversaries regularly use supply chain attacks in currency generation operations
and target software developers to enable subsequent campaigns.
COMPROMISED SOFTWARE PROVIDERS
Adversaries continued compromising software providers to enable supply chain attacks throughout 2025, typically
in highly targeted operations with significant impacts. Depending on their initial access vector and lateral movement
abilities, threat actors can leverage these operations for wide-ranging follow-on options. Such options include modifying
customer-facing SaaS environments to inject malicious code, altering software update mechanisms to deliver alternative
payloads, and accessing continuous integration and continuous delivery (CI/CD) systems that can be used to infect
legitimate software builds.
PRESSURE Safe{Wallet} Bybit
CHOLLIMA
1 Compromises
2 Exfiltrates credentials
OPERATOR DEVELOPER
3 Deploys malicious code
4 Performs transfer
Safe{Wallet}
5 Funds redirected to attacker CRYPTOCURRENCY Bybit
WALLET SERVICE EXCHANGE
Figure 16. PRESSURE CHOLLIMA supply chain attack targeting Bybit

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 32
In late February 2025, PRESSURE CHOLLIMA executed the largest cryptocurrency
theft in history by compromising Safe{Wallet}, a digital asset management
platform supporting cryptocurrency exchanges, to target funds held by the
centralized cryptocurrency exchange Bybit. The adversary initially gained access
to Safe{Wallet} systems by compromising a software developer’s machine via a
trojanized Python project (likely delivered using social engineering tactics) and
exfiltrating development-related credentials.
From this foothold in the victim system, PRESSURE CHOLLIMA pivoted to
Safe{Wallet}’s cloud infrastructure, where they inserted two elements into the
frontend: malicious JavaScript code for Bybit transactions and a smart contract
containing customized transfer logic that executed exclusively during transactions
between Bybit’s contract address and an adversary-controlled address. This
logic modified a subsequent routine transaction between Bybit wallets managed
using Safe{Wallet}, redirecting cryptocurrency then valued at 1.46 billion USD
to an adversary-controlled wallet. To evade detection, immediately following
the transaction, the adversary restored the malicious JavaScript hosted on
Safe{Wallet}’s cloud instance to its original version.
Threat actors also compromised software update mechanisms to deliver
malicious code in 2025. For example, in late October 2025, CrowdStrike
OverWatch identified a legitimate Notepad++ update process delivering malicious
reconnaissance and remote access tool (RAT) payloads to organizations in Central
America and South Asia. This highly targeted activity delivered malware to only
approximately 0.1% of organizations conducting Notepad++ client updates in the
operational time period.
Further payload analysis indicates technical overlaps with malware families
employed for likely China-nexus operations using multiple deployment methods,
indicating further diversification in supply chain attack distribution methods.
THIRD-PARTY SOFTWARE
DEPENDENCY COMPROMISE
Today’s complex software ecosystems frequently integrate third-party packages
into commercial and open-source software to provide additional functionality.
Because developers who use third-party dependencies trust that the package
maintainers securely verify their code and software build process over successive
updates, adversaries can abuse this trust to introduce their own malicious
code into otherwise legitimate projects. Organizations then unknowingly
execute untrusted code after installing or updating software that includes these
dependencies.
Throughout 2025, threat actors frequently used supply chain attack methods
to target npm repositories that offer JavaScript-based libraries for the Node.js
runtime environment. For example, FAMOUS CHOLLIMA combined malicious
npm packages with social engineering techniques to deliver BeaverTail malware
to software developers. Between January 2025 and May 2025, the adversary
deployed more than 30 malicious packages to npm.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 33
FAMOUS CHOLLIMA operators then masquerade as legitimate job recruiters
and ask targeted developers to review or improve a project as part of an
employment assessment. To complete the purported assessment, the developers
download and execute the malicious packages that deploy malware payloads.
Adversary-linked packages were downloaded more than 8,000 times, likely because
they were incorporated as dependencies in other software and therefore caused
collateral infections.
In September 2025, the new malware family ShaiHulud began circulating
via a supply chain attack on the npm ecosystem. An information stealer
capable of collecting many credential types from infected machines, ShaiHulud
can self-propagate by infecting further npm packages if the malware finds the
appropriate authentication tokens on the host. Though the initially affected
package was downloaded more than 2 million times by mid-September 2025,
ShaiHulud’s self-propagation capability likely posed an infection risk to many
more users as the attack progressed.
In November 2025, ShaiHulud’s developer expanded the malware’s capabilities to
include remote execution and destructive payload delivery. The updated malware
increases stealth by removing evidence of the attack’s initial phases, which use
malicious GitHub pull requests. This enhanced initial phase indicates the threat
actor attempted to maximize infection rates across a large number of
compromised packages in their second campaign iteration.
»
Threat actors also used npm-based supply chain attacks to hijack
THOUGH THE INITIALLY
cryptocurrency transactions via cryptocurrency wallet credential stealers
AFFECTED PACKAGE WAS DOWNLOADED
in 2025. Because trojanized npm packages are typically downloaded several
MORE THAN 2 MILLION TIMES BY
million times per week, threat actors using this technique have high chances MID-SEPTEMBER 2025, ShaiHulud’s
of successfully capturing credentials. SELF-PROPAGATION CAPABILITY
LIKELY POSED AN INFECTION RISK TO
MANY MORE USERS AS THE ATTACK
In September 2025, multiple npm packages maintained by a single developer,
PROGRESSED.
accounting for over 2 billion downloads per week, were compromised after threat
actors phished administrative credentials with a credential stealer masquerading
as an npm login page. In this case, malicious code incorporated into the packages
could monitor network data and hijack cryptocurrency transactions, replacing the
destination wallet with an attacker-controlled address.
As this campaign illustrates, attackers can use a single vulnerability point,
such as a prolific npm package developer, to spread malicious code across
projects with very high install rates.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 34
DETECTING ANOMALOUS SaaS ACTIVITY
WITH CROWDSTRIKE FALCON SHIELD
SaaS providers are an attractive target for adversaries aiming to execute supply chain attacks
and pivot to subscriber networks. Attackers can steal SaaS authentication tokens from a centralized
repository and use them to access many customer data stores.
In September 2025, Salesloft disclosed an intrusion that occurred between March 2025 and June 2025
in which a threat actor gained access to the company’s GitHub and cloud environments. The intrusion
enabled OAuth token theft for Salesloft customers’ Drift integrations with third-party SaaS applications.
The majority of observed incidents impacted IT services organizations, and several high-value IT and
information security companies publicly disclosed incidents related to the campaign.
In several subsequent incidents that CrowdStrike Falcon® Shield identified and CrowdStrike Services
responded to, a threat actor leveraged stolen Salesloft OAuth tokens to access and exfiltrate data from
customers’ Drift-integrated SaaS applications. In one incident, the threat actor also attempted to pivot
to the customers’ identity and access management (IAM) user accounts via exposed credentials.
The threat actor likely obtained these credentials from compromised SaaS instances using TruffleHog,
an open-source tool that can identify exposed credentials in source-code repositories.
CrowdStrike Intelligence cannot currently assess the threat actor’s origin or motivation but has not
observed attempts to monetize this campaign to date. The long time period the threat actor spent in
Salesloft’s environment is atypical for eCrime activity and more consistent with state-nexus intrusions.
Additionally, the threat actor’s focus on targeting IT and information security organizations indicates
they likely intend to target downstream organizations, another pattern consistent with state-nexus
threat actors.
Falcon Next-Gen SIEM customers can use Falcon Shield to detect anomalous SaaS activity, including
access from stale accounts, connections originating from unexpected autonomous system numbers
(ASNs), and actions that are atypical for the current user and other non-human identities.
OUTLOOK
CrowdStrike Intelligence anticipates that supply chain attacks will continue to pose a significant threat to organizations
throughout 2026. Attackers value this method because it offers a wide potential scope and allows them to hijack trusted
update mechanisms intended to improve software security.
Campaigns exploiting public code repositories demonstrate that attackers are refining their techniques in two important
ways: evading early detection by deleting evidence of initial infection from public view and expanding reach by
incorporating self-replication procedures into their malicious code. These changes have already yielded considerable
success, despite efforts by developers and code-hosting platforms to remove malicious code from circulation. As these
attacks often compromise packages created by developers who have full-time jobs outside of maintaining the code,
threat actors can often gather prerequisite credentials and initiate campaigns before a developer realizes their package
has been compromised.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 35
Attackers will likely continue adapting their techniques to maximize infection rates.
For example, threat actors may find opportunities to add malicious code more
subtly or trigger behavior that users do not intend through indirect code changes
(e.g., modifying cryptocurrency smart contracts executed by targeted software).
Targeting of SaaS applications will likely increase further in 2026 based on the
continued trend of enterprise organizations migrating data from on-premises to
cloud-based systems and the numerous 2025 campaigns in which threat actors
targeted SaaS instances. eCrime and targeted intrusion adversaries continued to
target SaaS platforms for data discovery, exfiltration, and monetization.
Compromising software development companies to access their internal build
chains and update mechanisms remains a more complex supply chain attack
option, although this methodology is still likely to be used for highly targeted
attacks that can evade detection unless updates are specifically tested for
malicious code.
Adversary Objectives Shape
Zero-Day Exploit Selection
Zero-day exploits allow adversaries to evade detection and countermeasures
for identified exploit vectors. Throughout 2025, threat actors used dozens of
zero-day exploits to enable initial access, RCE, and privilege escalation.
CrowdStrike Intelligence observed a 42% year-over-year increase in the
number of zero-day vulnerabilities exploited prior to public disclosure.
This aligns with the gradual increase industry sources have reported in
zero-day exploitation over the past four years.7
Adversaries’ objectives and preferences highly likely influence the zero-day
they choose to exploit. A subset of targeted intrusion threat actors, often driven
by their mandates to stealthily gain persistent access and collect intelligence,
prioritize targeting zero-days in internet-exposed endpoints. They frequently use
such exploits to gain initial access to unmanaged assets in high-value networks. In
at least one case, one targeted intrusion adversary repeatedly attacked the same
vendor and product with multiple zero-days disclosed in 2025, suggesting the
threat actor may be focusing their efforts on this product.
In contrast, financially motivated adversary GRACEFUL SPIDER targets
vulnerabilities in internet-facing enterprise products in widespread campaigns.
Therefore, they highly likely select exploits based on speed and reliability at scale.
Similarly, reliability requirements likely motivate eCrime adversaries’ selection
of a given zero-day exploit for local privilege escalation (LPE) against operating
systems (OSs). However, reliability is likely a less important criterion to these
adversaries than the ease with which they can obtain a given exploit, either
directly or indirectly.
7 https://cloud.google.com/blog/topics/threat-intelligence/2024-zero-day-trends

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 36
TARGETED INTRUSION THREAT ACTORS
EXPLOIT EDGE DEVICES VIA ZERO-DAY
VULNERABILITIES
Throughout 2025, targeted intrusion adversaries gained access to networks by
exploiting zero-day vulnerabilities in edge devices such as VPN servers, mail
servers, firewalls, and routers. Many targeted intrusion adversaries value edge
device attacks due to these devices’ security shortcomings and often deliberate
internet exposure.
Moreover, EDR solutions often achieve only limited visibility of edge devices.
Targeted intrusion threat actors’ continued efforts to leverage zero-day
vulnerabilities against these devices likely signal that they have experienced
success and have invested significant resources into such methods.
Since at least 2023, Russian targeted intrusion adversary FANCY BEAR has
targeted various webmail services via multiple methods, including zero-day
and n-day vulnerability exploitation impacting Zimbra and Roundcube webmail
services. The adversary likely uses these methods for access development and
intelligence collection. Targeted intrusion adversaries have conducted similar
exploitation campaigns against webmail products. In 2025, Russia-aligned threat
actors, including FANCY BEAR and Belarus-nexus adversary UMBRAL BISON,
increasingly exploited cross-site scripting (XSS) vulnerabilities in Roundcube and
Zimbra to exfiltrate valid credentials, email communications, and contact lists.
Threat actors also value mail servers because they are inherently exposed,
often via an easily enumerated login portal, and are associated with prolonged
patching periods. While CrowdStrike Intelligence has observed numerous threat
actors compromising and/or exploiting mail servers for several years, some
adversaries appear to particularly focus on these applications and target
multiple vendors across a broad spectrum of products and versions.
In addition to webmail servers, targeted intrusion threat actors frequently
exploit VPN servers, which are also commonly unmanaged and exposed.
Multiple vulnerabilities disclosed in 2025 that impact network devices, including
CVE-2025-22457 and CVE-2025-0282, were previously exploited as zero-days.
Though the malware and target sectors differed between incidents, a technique
often used in these operations aligns with a well-established China-nexus
technique: rapidly deploying a network remote code exploit against perimeter
devices as part of initial access operations.

| CROWDSTRIKE 2026 GLOBAL THREAT REPORT |     |     |     |     |     |     | 37  |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
GRACEFUL SPIDER’S OPPORTUNISTIC USE
OF ZERO-DAY VULNERABILITIES

eCrime adversary GRACEFUL SPIDER differentiates themselves from other BGH adversaries by repeatedly exploiting
zero-day vulnerabilities. Since late 2020, GRACEFUL SPIDER has primarily exploited internet-exposed network assets
with multiple remote zero-day vulnerabilities. Whether GRACEFUL SPIDER develops or merely acquires these zero-day
exploits remains unclear.
Beginning as early as August 2025, GRACEFUL SPIDER conducted data exfiltration operations by exploiting a novel
zero-day vulnerability now tracked as CVE-2025-61882.
Though this campaign diverges from GRACEFUL SPIDER’s historical pattern of targeting file transfer applications,
the tactical shift remains consistent with the adversary’s overarching strategy: targeting internet-exposed,
enterprise-level web applications to achieve initial access and, ultimately, exfiltrate data. This strategy will
almost certainly drive GRACEFUL SPIDER’s choice of exploit targets in the future.
Product: Accellion FTA
CVE-2021-27101
CVE-2021-27102
CVE-2021-27103
CVE-2021-27104
|     |     | Product: GoAnywhere MFT |     | Products:     |     |     |     |
| --- | --- | ----------------------- | --- | ------------- | --- | --- | --- |
|     |     | CVE-2023-0669           |     | Cleo Harmony  |     |     |     |
|     |     | Product: MOVEit         |     | Cleo VLTrader |     |     |     |
Cleo LexiCom
Transfer
|     |     |     | CVE-2023-34362 | CVE-2024-55956 |     |     |     |
| --- | --- | --- | -------------- | -------------- | --- | --- | --- |
Product:
Product: SysAid
|     |      |         | On-Premises    |      | E-Business Suite (EBS) |     |     |
| --- | ---- | ------- | -------------- | ---- | ---------------------- | --- | --- |
|     |      |         | CVE-2023-47246 |      | CVE-2025-61882         |     |     |
|     | DEC  | FEB MAY | NOV            | DEC  | AUG                    |     |     |
|     | 2020 | 2023    |                | 2024 | 2025                   |     |     |
Product Type: File Transfer  IT Service Management Business Integration
Figure 17. Zero-day vulnerabilities exploited by GRACEFUL SPIDER
eCRIME THREAT ACTORS’ APPROACH TO ZERO-DAY
EXPLOITATION FOR PRIVILEGE ESCALATION

Zero-day exploits used on common OSs are far more effective for achieving LPE at scale than alternative exploit types.
However, because OS patching cycles are relatively narrow, threat actors have limited opportunity to capitalize on
zero-day exploits following disclosure. Other exploit types, particularly network RCE, may impact platforms that are
more difficult to patch and may therefore remain effective for longer periods.
In late April 2025, eCrime adversary VICE SPIDER highly likely exploited a zero-day LPE vulnerability (CVE-2025-32706)
affecting the Microsoft Windows Common Log File System (CLFS) driver. Though VICE SPIDER previously leveraged
n-day LPE vulnerabilities against various Windows services and protocols (such as the Windows Error Reporting service
via CVE-2023-36874, CLFS via CVE-2022-24521, and Netlogon via CVE-2020-1472), the April 2025 activity marked the
first observed instance of VICE SPIDER using a zero-day LPE vulnerability for the Windows CLFS driver.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 38
VICE SPIDER’s transition to novel zero-day use is a logical progression in the adversary’s increasingly effective privilege
escalation techniques. Initially, the adversary frequently escalated privileges through compromised credentials.
However, since at least 2023, VICE SPIDER has repeatedly used a series of Windows LPE exploits targeting disclosed
vulnerabilities.
Other eCrime threat actors have also used exploits to target vulnerabilities affecting multiple Windows drivers, services,
and protocols, including the following:
• CVE-2025-59230, which affects the NetMan service
• CVE-2023-29360, which affects the Microsoft Streaming Service
• CVE-2024-35250, which affects Windows kernel-mode drivers
• CVE-2024-26169, which affects the Windows Error Reporting service
eCrime adversaries highly likely choose specific Windows drivers, services, or protocols to target for LPE
opportunistically rather than based on a specific preference or targeting requirement. These choices likely depend on
the target component’s prevalence, the exploit’s reliability, and the exploit’s availability, whether through purchase from
exploit brokers, free postings on public repositories, or in-house development.
OUTLOOK
CrowdStrike Intelligence assesses that the zero-day exploit trends addressed in this section will highly likely persist
into 2026 in various ways, including a direct repetition of the 2025 trends. Nevertheless, sophisticated adversaries are
expected to further evolve their exploitation abilities.
Though adversaries will likely approach this evolution in different ways, some may attempt to discover and operationalize
zero-day defense evasion-related vulnerabilities that could enable them to maintain long-term persistent access. While
such vulnerabilities may not receive critical ratings, facilitate mass exploitation, or garner widespread press coverage,
they would permit threat actors to remain undetected in victim networks, thereby complicating defense and remediation
efforts for network defenders.
Furthermore, GRACEFUL SPIDER's sustained, multi-year success in exploiting zero-day vulnerabilities will likely
motivate other BGH threat actors to adopt similar tactics in 2026. BGH threat actors aiming to execute rapid, extensive
exploitation against well-protected entities, appear highly skilled, or distinguish themselves from competitors are the
eCrime groups most likely to incorporate zero-day exploits into future operations.
CrowdStrike Intelligence recommends a comprehensive, in-depth defense strategy to mitigate the potential risk of
zero-day vulnerabilities. Proactive planning and preparation can help organizations understand their exposure and yield
actionable recommendations to minimize the probability and impact of a security event. This can include penetration
testing, establishing a robust vulnerability management program, conducting red teaming exercises, and executing
tabletop drills.
CrowdStrike Intelligence additionally recommends using Falcon Next-Gen SIEM. This helps organizations gather and
leverage cross-domain data (such as real-time indicators of attack, adversary intelligence, exposure data, Falcon sensor
data, and third-party data) to deliver highly accurate detections and automated protection and remediation. Many of
these automated detection features are designed to identify and block post-exploitation activities before an adversary
can achieve their objectives, reducing the overall impact of zero-day exploitation.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 39
Adversaries Subvert Trust in
Cloud Platforms and Services
»
Throughout 2025, both targeted intrusion adversaries and eCrime adversaries A 37% RISE IN CLOUD-CONSCIOUS
evolved their cloud-targeting techniques, successfully subverting the implicit INTRUSIONS YEAR-OVER-YEAR
trust users place in cloud entities and technologies to achieve persistence, DEMONSTRATES WIDESPREAD
ADVERSARY INTEREST, WHILE THE
lateral movement, and data exfiltration.
266% INCREASE IN SUCH INTRUSIONS
BY NAMED STATE-NEXUS THREAT
Adversaries’ continued efforts, alongside CrowdStrike OverWatch’s cloud hunting ACTORS SIGNALS THAT ADVANCED,
PERSISTENT THREAT GROUPS ARE
efforts, led to substantial increases in identified cloud-targeting activity in 2025.
PRIORITIZING CLOUD ENVIRONMENTS.
A 37% rise in cloud-conscious intrusions year-over-year demonstrates widespread
adversary interest, while the 266% increase in such intrusions by named
state-nexus threat actors signals that advanced, persistent threat groups are
prioritizing cloud environments.
CrowdStrike Intelligence assesses that multiple targeted intrusion threat actors,
the majority of whom conduct China- or Russia-nexus operations, significantly
increased their investment in cloud targeting in 2025, primarily by funding research
and supporting infrastructure.
China-nexus adversary MURKY PANDA continued to abuse trust relationships
in Entra ID to compromise downstream victims while also using the newly created
ORB network ORB28 for anonymity. In addition, Russia-nexus adversary
COZY BEAR has combined various Entra ID authentication flow abuse
techniques with social engineering tactics to compromise victim accounts.
Both eCrime and targeted intrusion threat actors have leveraged
adversary-in-the-middle (AiTM) phishing pages to enable credential collection
and to access Microsoft 365 SaaS services for data collection. eCrime threat
actor ShinyHunters used this access to search for data related to a victim entity’s
customer relationship management (CRM) SaaS instance. In November 2025,
Iran-nexus threat actor IMPERIAL KITTEN made their first observed attempt at
targeting cloud identities when they deployed the EvilGinx2 phishing kit to target
Hebrew- and English-speaking Microsoft 365 users in Israel.
Emerging eCrime threat actors also advanced their tactics to abuse trusted
relationships. While SCATTERED SPIDER primarily drove cloud-targeting
techniques in 2023 and 2024, cloud-conscious adversary BLOCKADE SPIDER
also targeted Entra ID services in 2025. Notably, BLOCKADE SPIDER used many
cloud-based techniques previously employed by SCATTERED SPIDER, particularly
those involving abuse of users’ trust in hybrid identity configurations.

| CROWDSTRIKE 2026 GLOBAL THREAT REPORT |                     |                           |               |     | 40  |
| ------------------------------------- | ------------------- | ------------------------- | ------------- | --- | --- |
|                                       | TRUST LAYER         | TRUST MECHANISM EXPLOITED | IMPACT RADIUS |     |     |
|                                       | ORGANIZATION-LEVEL  |                           | EXPONENTIAL   |     |     |
Partner tenant connections in Entra ID
TRUST
SaaS provider application secrets
Multiple downstream organizations
|     | Exploiting B2B relationships  |     | per compromised provider |     |     |
| --- | ----------------------------- | --- | ------------------------ | --- | --- |
and partner ecosystems
MURKY PANDA
|     | TENANT          | Hybrid identity sync services  | HIGH                   |     |     |
| --- | --------------- | ------------------------------ | ---------------------- | --- | --- |
|     | IDENTITY-LEVEL  | (Entra Connect Sync)           |                        |     |     |
|     | TRUST           |                                | Enterprise-wide access |     |     |
SCATTERED SPIDER
|     |     | Federation trust (AD FS) | Complete Entra ID user base at risk |     |     |
| --- | --- | ------------------------ | ----------------------------------- | --- | --- |
Exploiting identity
Third-party IAM (AD agent)
|     | synchronization  |     | Admin privilege escalation |     |     |
| --- | ---------------- | --- | -------------------------- | --- | --- |
Password hash synchronization
|     | and federation |     | Persistent access via federation |     |     |
| --- | -------------- | --- | -------------------------------- | --- | --- |
Token-signing certificates
BLOCKADE SPIDER
|     | USER-LEVEL TRUST | Legitimate Microsoft  | TARGETED |     |     |
| --- | ---------------- | --------------------- | -------- | --- | --- |
authentication endpoints
|     | Exploiting  |     | Individual accounts |     |     |
| --- | ----------- | --- | ------------------- | --- | --- |
OAuth 2.0 authorization flows
| COZY BEAR | authentication flows  |     |                            |     |     |
| --------- | --------------------- | --- | -------------------------- | --- | --- |
|           | and familiar login    |     | Email/Microsoft 365 access |     |     |
Device code authentication
|     | experiences |     | Initial access vector |     |     |
| --- | ----------- | --- | --------------------- | --- | --- |
Trusted domains/SSL certificates
Established relationships
(email, instant messaging,
video conferencing)
IMPERIAL KITTEN
Figure 18. Layers of trust targeted by cloud-conscious threat actors
BLOCKADE SPIDER AND SCATTERED SPIDER
USE PARALLEL HYBRID IDENTITY ABUSE TECHNIQUES

One of the trust abuse mechanisms that eCrime threat actors leveraged most effectively throughout 2025 was
hybrid identity targeting. This set of techniques subverts users’ trust in the technologies that bridge on-premises
and cloud-based identity solutions. SCATTERED SPIDER and BLOCKADE SPIDER, the adversaries that targeted
hybrid identity solutions most frequently throughout 2025, used many of the same cloud-conscious techniques.
SCATTERED SPIDER led the eCrime community in using hybrid identity-targeting techniques in 2025. The adversary
employed many of the most effective techniques observed throughout 2024 and 2025, especially those targeting Entra
ID or Azure environments. The adversary particularly favored vishing and abusing SSO services for lateral movement.
BLOCKADE SPIDER also used many techniques targeting Entra ID, often with only minor variations from SCATTERED
SPIDER’s techniques. Both adversaries used hybrid identity targeting, Entra ID account creation, device registration,
alternate multifactor authentication (MFA) registration, conditional access policy bypassing, and indicator removal via
email hiding. While BGH-based ransomware deployment remained the objective for both SCATTERED SPIDER and
BLOCKADE SPIDER, each used distinct methods to achieve this goal.
Both adversaries conducted multiple novel attacks against hybrid identity solutions, which primarily allow organizations
to synchronize users’ accounts and authentication mechanisms between on-premises and cloud-based identity systems.
Targeting this link, whether by compromising the hybrid identity solution itself or by compromising associated identities
that have privileged access, provides threat actors with exceptional access levels.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 41
These techniques can facilitate persistence and privilege escalation. Both SCATTERED SPIDER and BLOCKADE SPIDER
have targeted the hybrid Entra ID solutions Entra Connect Sync and Active Directory Federation Services (AD FS). They
used different tooling and, in some cases, different techniques to elevate privileges and control authentication in the
environment.
Additionally, BLOCKADE SPIDER targeted a hybrid identity solution to control authentication across environments.
Although these techniques may require administrative changes and anomalous account usage and are therefore less
subtle than some used by targeted intrusion threat actors, they are effective for eCrime threat actors, whose operations
often require speed in the cloud and quick lateral movement mechanisms with short access periods.
TARGETED INTRUSION THREAT ACTORS
INVEST IN CLOUD TARGETING
MURKY PANDA and Other China-Nexus Threat Actors Abuse
Partner Connections and Leverage ORB Networks
Cloud-conscious China-nexus threat actors significantly increased their intrusions in 2025, often using specialized tools,
techniques, and infrastructure. Many of these techniques involved trust abuse, e.g., targeting an upstream technology
service to enable later pivoting to downstream targets, leveraging ORB networks to evade detection by obfuscating
access, and conducting password spraying behind inconspicuous, residential IP spaces.
China-nexus adversary MURKY PANDA has specialized in targeting Entra ID since at least Q3 2024. The adversary has
compromised multiple IT services organizations using trusted relationship connections between Entra ID tenants. By
targeting upstream service providers rather than individual victims, MURKY PANDA can compromise other organizations
that have a trusted relationship with the targeted technology partner. This initial access vector is less monitored than
many others and therefore allows for prolonged, undetected access to downstream victims’ data, including emails.
In one mid-2025 incident, MURKY PANDA used the newly identified ORB28 network for delegated email access to
a Microsoft 365 environment. ORB28 has also been used in high-volume password spraying attacks against Entra ID
accounts, although whether the network is exclusively used by MURKY PANDA or is instead used by multiple
cloud-focused China-nexus threat actors remains undetermined.
COZY BEAR Implements Trust Abuse Social Engineering and Phishing Methods
Throughout 2025, Russia-nexus adversary COZY BEAR systematically exploited interpersonal trust, organizational
credibility, and platform legitimacy to compromise U.S.-based targets. The adversary successfully weaponized
established professional relationships by impersonating trusted contacts, then leveraged victims’ inherent trust in
Microsoft’s authentication infrastructure to complete the compromise. This activity was difficult for victims to identify as
malicious, as the adversary prompted victims to enter credentials only on legitimate Microsoft login pages.
CrowdStrike OverWatch and CrowdStrike Services responded to multiple COZY BEAR phishing attempts at U.S.-based
nongovernmental organizations (NGOs) and a U.S.-based legal entity. The adversary’s multi-layered trust exploitation
unfolded through three distinct vectors (Figure 19).

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 42
INTERPERSONAL TRUST EXPLOITATION
COZY BEAR successfully compromised or impersonated individuals with whom targeted users
maintained trusting professional relationships. Impersonated individuals included employees from
international NGO branches and pro-Ukraine organizations. The adversary heavily invested in
substantiating these impersonations, using compromised individuals' legitimate email accounts alongside
burner communication channels to reinforce authenticity.
MULTI-CHANNEL SOCIAL ENGINEERING
COZY BEAR orchestrated sophisticated, multi-day conversations across instant messaging, email, and
video conferencing to build rapport and establish credibility. This persistent, cross-platform engagement
created multiple opportunities for the adversary to lend the impersonation credence and lower the
target's defenses before introducing malicious links.
PLATFORM TRUST ABUSE
COZY BEAR delivered Entra ID OAuth 2.0 authorization code- and device code-based phishing links
that redirected to authentic Microsoft login pages. This technique removed the traditional phishing
warning sign: suspicious domains. Victims saw only legitimate Microsoft infrastructure throughout
the authentication process.
Figure 19. COZY BEAR’s multi-layered trust exploitation techniques
This layered approach to trust relationship abuse provides COZY BEAR with several operational advantages. First, it
ensures more reliable initial access by exploiting preexisting trust between the victim and the impersonated individual,
thereby increasing the likelihood that victims will comply with requests to click links or provide authentication codes.
Second, critically, the technique allows malicious authentication activity to blend seamlessly with legitimate user
behavior, thereby increasing the probability that malicious access eludes detection. By directing victims to authentic
Microsoft infrastructure rather than adversary-controlled domains, the phishing attempts further evade traditional
URL-based detections and leverage the inherent trust organizations place in Microsoft’s authentication services.
COZY BEAR used each of these techniques and attempted to evade multiple conditional access policies in an
August 2025 intrusion targeting a U.S.-based NGO.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 43
DAY 1
07:00:00
07:56:00
Threat actor makes initial contact with target user via an instant message
13:00:00
13:25:00
Threat actor sends target user phishing link initiating authorization code OAuth 2.0 flow to access device
registration app
14:00:00
14:26:21
Target user logs in with threat actor-provided device registration URL
14:28:00
Target user sends threat actor URL with authorization code
14:29:09
Threat actor logs in with target user-provided authorization code 14:29:43
Threat actor establishes persistence with Windows
Hello for Business credential and passwordless
14:33:49
phone sign-in
Threat actor tries and fails to access Outlook due to
conditional access policy requiring Intune enrollment
14:39:00
Threat actor sends follow-up authorization code URL to access the Outlook mobile
app, likely in hope that Intune enrollment is not required for mobile
14:44:00
Target user does not click link but requests email-based verification of the threat actor's presumed identity
14:45:00
Threat actor responds, indicating they do not currently have access to their PC but would like to reschedule
DAY 2
07:00:00 7:39:00
Threat actor replies, indicating they now have access to their email
14:00:00
14:31:28-15:17:59
Threat actor spends multiple hours throughout three days attempting to bypass the conditional access
DAY 4 policy by registering devices with various mobile and PC naming conventions and attempting to
authenticate to various applications and resources using multiple authentication flows
15:00:00
DAY 5
10:00:00 10:14:00
Threat actor responds to victim from the impersonated individual's legitimate email, prompting further
dialogue with the victim via instant message
13:00:00 13:31:00 13:37:00 13:37:49
Threat actor sends a third authorization Victim responds with a URL containing Threat actor logs in with user-provided
code URL to access Microsoft Intune the authorization code authorization code, likely failing to
Company Portal app, likely in hope of enroll in Intune due to a conditional
enrolling a malicious device in Intune access policy requiring enrollment
from an on-premises IP address
DAY 31
10:00:00 10:11:00
Threat actor contacts another user at the organization impersonating a pro-Ukrainian NGO and delivering
multiple auth code URLs, including one targeting the Microsoft Power Platform application
Figure 20. COZY BEAR phishing attempt targeting a U.S.-based NGO

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 44
AiTM ATTACKS ENABLE SaaS INTRUSIONS
Consistent with CrowdStrike Intelligence’s prediction in the CrowdStrike 2025 Global Threat Report, both
eCrime and targeted intrusion adversaries continued to target cloud-based SaaS applications throughout 2025.
Performing exfiltration from SaaS applications is an effective technique, as these platforms host high volumes
of critical data but are often not subject to the same heavy security monitoring as on-premises systems.
Moreover, threat actors face a low technical barrier to navigating SaaS platforms, as users typically access these
applications using a browser graphical user interface.
In 2025, adversaries continued targeting document management and storage suites, data warehousing platforms,
and payroll and expense reimbursement applications. CRM instances emerged as a key target: In multiple eCrime
and likely targeted intrusion campaigns, adversaries abused non-human identities, such as service accounts and
API keys, to facilitate access to database instances.
Throughout 2025, CrowdStrike Intelligence also observed eCrime and targeted intrusion threat actors leveraging
AiTM phishing kits to gain access to Microsoft 365 accounts. In contrast to traditional phishing attacks that
end at credential capture, AiTM phishing kits exploit the trust relationship between users and Microsoft’s
authentication ecosystem by acting as a real-time reverse proxy.
When a victim enters credentials on the adversary’s spoofed login page, the phishing kit transparently forwards
the authentication request to legitimate Microsoft login services and relays responses back to the victim in real
time. eCrime threat actors primarily use this access to identify data that can allow them to pivot to other services,
while nation-state threat actors primarily target data relevant to their intelligence collection priorities in Microsoft
Outlook and SharePoint.
Between January 2025 and August 2025, CrowdStrike Intelligence observed an eCrime threat actor that identifies
themselves in extortion communications as ShinyHunters conducting social engineering campaigns that targeted
access to CRM instances.
In an early 2025 campaign, the threat actor collected victims’ Microsoft Entra ID credentials by directing them to
access AiTM phishing pages on their personal mobile devices. The threat actor leveraged these credentials to
search Microsoft SharePoint for documentation relating to access to the victim’s CRM instance.
In November 2025, Iran-nexus adversary IMPERIAL KITTEN conducted credential phishing operations against
Israeli Microsoft 365 users via an AiTM phishing toolkit named EvilGinx2. The adversary used Israel-themed
phishing infrastructure with English- and Hebrew-language lures to establish credibility and urgency with targets.
Post-compromise, IMPERIAL KITTEN conducted basic enumeration of Microsoft 365 accounts, accessing
Microsoft App Access Panel, Office Home, and the Microsoft Authenticator app to map available services
and privileges.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 45
OUTLOOK
Throughout 2025, SCATTERED SPIDER and BLOCKADE SPIDER debuted multiple
hybrid identity-targeting techniques. These new methods enabled the adversaries to
obtain broad privileged access across target environments, effectively progressing
the threat actors toward their primary objective: BGH ransomware deployment.
CrowdStrike Intelligence assesses that additional eCrime threat actors will likely
target hybrid identity solutions in 2026. This assessment is made with moderate
confidence based on this strategy’s observed effectiveness as well as the steps
required to operationalize some implementations of this technique.
Targeted intrusion threat actors also grew more active in conducting
cloud-targeted operations in 2025, heavily investing in research, development,
and personnel. Multiple cloud-conscious targeted intrusion threat actors emerged
in 2025, including threat actors from Russia, China, Iran, and the DPRK.
CrowdStrike Intelligence further assesses that threat actors from these countries
and other state-aligned threat actors will maintain or expand their investment
in cloud capability development in 2026. This assessment is made with high
confidence based on these threat actors’ focus on increasing cloud-targeting
capabilities and infrastructure in 2025.
Both eCrime and targeted intrusion adversaries continued to target SaaS platforms
for data discovery, exfiltration, and monetization in 2025. CRM instances emerged
as a target in several campaigns, with multiple threat actors leveraging non-human
identity types such as OAuth tokens to gain access to these platforms.
CrowdStrike Intelligence assesses that SaaS application targeting will again
increase in 2026. This assessment is made with high confidence based on the
continued trend of enterprise organizations migrating data from on-premises to
cloud-based systems and widely reported 2025 campaigns targeting
SaaS instances.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 46
Conclusion
As 2026 begins, the cybersecurity threat landscape grows increasingly
sophisticated, demanding that organizations in all sectors and geographies
strengthen and adapt their defenses. As adversaries become more evasive,
agile, and innovative, understanding their motivations and anticipating their
actions is critical to an effective defense.
Threat actors of all skill levels will continue adopting AI for social engineering, IO,
and technical activity. Less sophisticated threat actors will use AI to offset limited
expertise, enabling more complex attacks but often introducing errors due to poor
implementation and limited ability to validate output. More advanced threat actors
will increasingly leverage AI for malware development, social engineering, and
post-exploitation activities, accelerating attack speed, scale, and effectiveness.
With greater resources and maturity, these threat actors are positioned to
operationalize agentic AI for minimally supervised or autonomous operations.
As organizations embed AI into core business processes, the attack surface
will expand to include AI models, training data, agents, and supply chains.
Limited visibility into AI operations will amplify risk and create exploitable gaps.
Despite improved detection and prevention capabilities, BGH adversaries
remained 2025’s primary eCrime threat. These adversaries caused significant
business disruptions in 2025, resulting in substantial recovery costs and lost
revenue for victims.
The ransomware ecosystem was remarkably resilient despite law enforcement
disruptions and internal criminal strife, confirming ransomware remains an attractive
business model. This trend is projected to persist in 2026. Fast-paced vishing
campaigns targeting SaaS applications for initial access and data exfiltration will
almost certainly continue, as opportunistic ransomware adversaries and targeted
data theft operators employ techniques that continue to evade even advanced
security solutions.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 47
Targeted intrusion adversaries remained persistent and adaptive in 2025,
incorporating stealth tactics, cloud-conscious techniques, and AI-enhanced
capabilities to achieve their geopolitical and strategic objectives while evading
defensive measures:
• Russia-nexus adversaries are expected to continue conducting aggressive
operations, primarily to collect intelligence from Ukrainian targets and NATO
member states.
• China-nexus adversaries are expected to maintain their high operational tempo
while increasingly incorporating stealth tactics and targeting edge devices and
internet-facing appliances. These adversaries will almost certainly continue
targeting telecom, financial services, and logistics entities to support the
Chinese Communist Party’s strategic intelligence collection objectives.
• DPRK-nexus adversaries will highly likely continue to prioritize operations
focused on military intelligence collection, cryptocurrency theft, and revenue
generation.
In the vulnerability exploitation landscape, threat actors will continue to leverage
their evasion capabilities and use zero-day exploits to bypass security controls.
Exploitation will almost certainly continue to transition from zero-day activity to
widespread campaigns, enabled by publicly available technical details and POC
exploits, which facilitate broader threat actor participation and widespread n-day
exploitation.
Cloud-conscious threat actors are now leveraging various techniques to
undermine victims’ trust. State-nexus adversaries are leveraging stealthy initial
access methods, while eCrime adversaries are prioritizing persistence and
privileged access. The prevalence of cloud-targeting adversaries will likely
increase in 2026, with additional state-nexus threat actors primarily targeting
cloud environments and eCrime threat actors employing techniques to target
broad cloud identity access.
As these complex threats continue evolving throughout 2026, the CrowdStrike
Counter Adversary Operations team remains committed to identifying, tracking,
and disrupting threat actors at every possible opportunity while providing
organizations with the intelligence and capabilities necessary to defend against
an increasingly sophisticated and persistent adversary landscape.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 4488
RReeccoommmmeennddaattiioonnss
Secure AI to reduce emerging business
and operational risk
As AI becomes embedded in core business processes, it introduces a rapidly expanding attack
surface that adversaries are already exploiting. Organizations should employ comprehensive
AI security and governance measures to address threats to AI systems as well as threats
posed by threat actors using AI. These should include monitoring employees’ use of AI tools,
enforcing access controls, and using data classification rules to prevent sensitive data leaks.
These measures should also include securing homegrown AI workloads from runtime attacks
(such as prompt injection), assessing the security of external vendors, and requiring secure
configurations and vulnerability assessments for new AI products and their dependencies.
To defend against AI-enabled threats, organizations should develop clear incident response
responsibilities and business continuity plans. Organizations can further secure their
environments with strong identity verification procedures, AI-focused security awareness
training, and continuous threat hunting.
Treat identity and SaaS as primary attack surfaces
Identity and SaaS platforms sit at the center of enterprise access, data, and business
operations, making them prime targets. Adversaries increasingly weaponize vishing, phishing,
and stolen OAuth tokens to pivot through cloud and SaaS identities. Organizations must
strengthen phishing-resistant MFA, enforce least-privilege access for service and non-human
accounts, and monitor anomalous SaaS and token activity to detect and contain intrusions
before attackers access sensitive data or critical systems.
Eliminate cross-domain blind spots to stop
high-impact attacks
Today’s most disruptive intrusions succeed by exploiting gaps between security domains, tools,
and teams rather than weaknesses in any single control. BGH and cloud-conscious adversaries
chain activity across endpoints, cloud environments, SaaS applications, and unmanaged hosts
to evade detection. Organizations should consolidate telemetry, apply cross-domain correlation
through extended detection and response (XDR) and next-generation security information and
event management (SIEM) workflows, and automate enrichment with threat intelligence to view
full attack paths and accelerate response.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 49
Secure the software supply chain and
developer workflows
Trust in software updates, open-source dependencies, and development pipelines has become a critical
business dependency and a prime target for adversaries. Malicious packages and compromised CI/
CD pipelines enabled high-impact supply chain attacks in 2025. Organizations should harden developer
environments, enforce code signing and dependency validation, scan repositories and packages for
anomalies, and assess third-party risk to reduce the likelihood that trusted software becomes a vehicle for
malware or credential theft.
Prioritize edge device and perimeter patching
and monitoring
Internet-facing and perimeter systems are among the most consistently exploited, and least visible,
paths into enterprise environments. State-nexus threat actors rapidly weaponize vulnerabilities in
edge and perimeter devices, which often lack EDR coverage and timely patching. Organizations
should prioritize rapid triage and patching of internet-facing appliances; enable logging and
monitoring for VPNs, firewalls, and virtualization platforms; and apply network segmentation
to limit lateral movement from compromised perimeter systems.
Prioritize proactive threat intelligence and hunting
When attacks unfold in minutes or seconds, reactive defense is no longer enough. An intelligence-driven
approach enables organizations to stop boiling the ocean and understand which adversaries are targeting
them, how they operate, and where they are likely to strike next. By applying threat intelligence and
adversary tradecraft analysis through proactive hunting, teams can identify stealthy footholds (such as
unmanaged VMs, AiTM activity, and supply chain anomalies) before attacks escalate. To operate at the
speed and scale of AI-accelerated adversaries, organizations must augment analysts with specialized AI
agents that accelerate intelligence analysis, hunting, triage, and response, turning insight into decisive
action earlier in the attack life cycle.
Strengthen human resilience against social engineering
and rapid intrusions
As adversaries increasingly rely on phishing, vishing, and trust abuse to bypass technical controls, human
decision-making remains a critical factor in preventing breaches. Organizations should reinforce user
awareness programs that reflect real-world adversary tactics to help employees recognize and resist social
engineering attempts that enable initial access.
For security teams, preparedness under pressure is essential. Regular tabletop exercises
and red/blue team operations help organizations identify gaps in detection, decision-making, and response,
ensuring teams can act quickly and effectively when attacks unfold. Continuous rehearsal strengthens
organizational resilience and reduces the likelihood that minor failures escalate into major incidents.

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 5500
CrowdStrike
Falcon Platform
AI and Cloud-Native
Leverages the network effect of crowdsourced security data while eliminating the management
burden of cumbersome on-premises solutions
Single Lightweight Sensor
Provides frictionless and scalable deployment and stops all types of attacks while eliminating
sensor bloat and scheduled scans
Charlotte AI
Powers the CrowdStrike portfolio of agentic and GenAI capabilities across the Falcon platform
(including natural-language chat, specialized agents, and embedded AI-powered features across
modules), tapping into the petabyte scale of CrowdStrike’s automated intelligence and further
enriched by security experts to accelerate analyst workflows
Falcon Fusion SOAR
Provides native security orchestration, automation, and response (SOAR) capabilities within the
Falcon platform to automate security workflows, reduce manual effort, and enable faster, more consistent
threat response
CrowdStrike Enterprise Graph
Unifies and contextualizes security telemetry across domains, connecting users, assets, behaviors, and
adversary activity into a single shared view of the enterprise to give humans and AI agents the context to see
attack paths, reason over complexity, and act faster; specialized graphs include:
• Asset Graph: Solves one of the most complex customer problems today: identifying assets, identities,
and configurations accurately across all systems (including cloud, on-premises, mobile, internet of things,
and more) and connecting them together in a graph form
• Intel Graph: Enables security teams to proactively defend against emerging threats with intelligence-driven
insights by mapping relationships between threat actors, tactics, vulnerabilities, and real-world attacks
• Threat Graph: Uses cloud-scale AI to correlate trillions of data points from multiple telemetry sources to
identify shifts in adversarial tactics and map tradecraft to automatically predict and prevent threats in real
time across CrowdStrike’s global customer base
Falcon Foundry
Allows customers and partners to easily build custom, low-code applications that harness
the data, automation, and cloud-scale infrastructure of the Falcon platform to solve your toughest
cybersecurity challenges
CrowdStrike Marketplace
Offers an enterprise marketplace of technology partners where you can discover, try, buy, and deploy
trusted CrowdStrike and partner applications that extend the CrowdStrike Falcon platform, without adding
agents or increasing complexity

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 5511
CrowdStrike Products
Endpoint Security
FALCON PREVENT | NEXT-GENERATION ANTIVIRUS
Protects against all types of threats, from malware and ransomware to sophisticated attacks, and deploys in minutes,
immediately protecting your endpoints
FALCON INSIGHT XDR | DETECTION AND RESPONSE FOR ENDPOINT AND BEYOND
Offers industry-leading, unified EDR and XDR with enterprise-wide visibility to automatically detect adversary activity
and respond across endpoints and all key attack surfaces
FALCON FIREWALL MANAGEMENT | HOST-BASED FIREWALL
Delivers simple, centralized host firewall management, making it easy to manage and control host firewall policies
FALCON DEVICE CONTROL | USB SECURITY
Provides the visibility and precise control required to enable safe usage of USB devices across your organization
FALCON FOR MOBILE | MOBILE THREAT DETECTION
Protects against threats to iOS and Android devices, extending endpoint security to your mobile devices,
with advanced threat protection and real-time visibility into app and network activity
FALCON FORENSICS | FORENSIC CYBERSECURITY
Allows you to quickly respond and recover with automated forensic data collection, enrichment, and correlation
FALCON FOR XIoT | XIoT ASSET PROTECTION
Delivers real-time threat prevention and detection for extended internet of things (XIoT) assets, backed by XIoT-specific
indicators of attack and indicators of compromise from CrowdStrike’s industry-leading threat intelligence
FALCON INSIGHT FOR ChromeOS | ChromeOS PROTECTION
Delivers industry-first native detection and response for ChromeOS devices without requiring additional agents or mobile
device management (MDM) solutions, providing unified visibility through the Falcon console
FALCON FOR LEGACY SYSTEMS | PROTECTION FOR LEGACY OPERATING SYSTEMS
Delivers anti-malware protection for Windows XP, Server 2003, Vista, and more while minimizing impact on
resource-constrained systems and integrating with the Falcon platform
FALCON ADVERSARY OVERWATCH: ENDPOINT | THREAT HUNTING
Provides 24/7 managed endpoint threat hunting, proactively monitoring your environment to identify novel attacks,
misuse of legitimate tools, credential compromise, insider threats, and adversary pivots from endpoint activity into
other domains

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 52
Threat Intelligence and Hunting
FALCON ADVERSARY OVERWATCH | THREAT HUNTING
Provides 24/7 protection across endpoints, identities, cloud workloads, and next-gen SIEM, delivered by expert
threat hunters powered by AI and threat intelligence to detect advanced intrusions and expose adversary
tradecraft, credential misuse, and vulnerability exploitation
FALCON ADVERSARY INTELLIGENCE | SOC AUTOMATION
Cuts investigation time from days to minutes across the SOC with personalized, real-time threat intelligence,
automating malware analysis and response through workflows and integrations while continuously monitoring the
open, deep, and dark web for fraud and emerging threats
FALCON ADVERSARY INTELLIGENCE PREMIUM | ADVERSARY INTELLIGENCE
Delivers industry-leading intelligence reporting on 281 adversaries globally and enables you to defend against
AI-powered adversaries with agentic AI built to reason across data, hunt for threats, and act decisively to
automate and accelerate complex analyst workflows
FALCON COUNTER ADVERSARY OPERATIONS ELITE | ON-DEMAND ANALYST
Provides an assigned analyst who leverages AI-powered investigative and threat hunting tools, enhanced by
deep adversary intelligence, to detect and disrupt adversaries across your IT environment and beyond
Cloud Security
FALCON CLOUD SECURITY: PROACTIVE SECURITY
Provides unified security posture management (USPM) and business context across cloud layers, leveraging
industry-leading threat intelligence, end-to-end attack paths, and ExPRT.AI so cloud teams can swiftly prioritize
their work, neutralize critical risks, and leave adversaries no room to strike
FALCON CLOUD SECURITY: CLOUD RUNTIME PROTECTION
Delivers leading cloud workload protection (CWP) and cloud detection and response (CDR), allowing SOC teams
to detect and respond to active threats across hybrid clouds so adversaries are stopped in their tracks
FALCON CLOUD SECURITY: CNAPP
Includes the features and capabilities of both Proactive Security and Cloud Runtime Protection for Falcon
Cloud Security
FALCON ADVERSARY OVERWATCH: CLOUD | THREAT HUNTING
Offers both proactive and protective security as a managed service through Falcon Adversary OverWatch
cross-domain threat hunting and Falcon Complete Next-Gen MDR, powered by integrated threat intelligence
to protect the cloud control plane, host OS, and data plane

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 53
SaaS Security
FALCON SHIELD | SaaS SECURITY
Unifies SaaS security posture management (SSPM) and SaaS-focused identity threat detection and response
(ITDR), delivering a modern approach to SaaS security with comprehensive visibility, continuous control over
SaaS security configurations, and real-time detection of active threats
AI Detection and Response
FALCON AI DETECTION AND RESPONSE | AIDR
Protects employee AI adoption and AI development at runtime by securing the prompt and agentic interaction
layer with unified visibility, real-time threat detection, data protection, access controls, and automated response
across endpoints, applications, AI agents, AI/API gateways, and cloud environments
Next-Gen Identity Security
FALCON NEXT-GEN IDENTITY SECURITY
Secures human, non-human, and AI identities by combining initial access prevention, modern secure privileged
access, ITDR, SaaS identity security, and agentic identity protection to stop identity-driven breaches across
domains
FALCON IDENTITY THREAT DETECTION
Provides unified visibility across hybrid identities and AI-driven threat detection to expose identity-based
threats before they escalate
FALCON IDENTITY THREAT PROTECTION
Secures hybrid identities with AI-driven threat detection and response to stop identity-based attacks in real time
FALCON PRIVILEGED ACCESS
Eliminates standing privileges by enforcing just-in-time access based on real-time risk, removing the complexity
of traditional privileged access management (PAM) solutions
FALCON ADVERSARY OVERWATCH: IDENTITY | THREAT HUNTING
Provides 24/7 managed identity threat hunting, proactively detecting identity-based attacks, monitoring
criminal forums for stolen credentials, and enforcing MFA challenges to prevent unauthorized access
Next-Gen SIEM
FALCON NEXT-GEN SIEM | SIEM
Empowers you to stop breaches and get unified visibility across your security ecosystem by delivering
industry-best detection, world-class threat intelligence, blazing-fast search, and AI-led investigation in
one platform

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 54
FALCON ONUM | HIGH-PERFORMANCE DATA PIPELINE
Simplifies complex telemetry pipelines and enables precise, real-time control over how telemetry
is collected, enriched, and routed in motion to deliver clean, high-quality signal for security and
analytic workflows
FALCON ADVERSARY OVERWATCH: NEXT-GEN SIEM | THREAT HUNTING
Delivers end-to-end threat disruption by correlating first- and third-party Falcon Next-Gen SIEM data and
proactively hunting advanced threats across network edge devices, SaaS applications, email security,
operating systems, and more
Data Protection
FALCON DATA PROTECTION FOR ENDPOINT | REAL-TIME ENDPOINT
DATA PROTECTION
Delivers real-time visibility, encryption detection, and behavioral analysis to stop unauthorized data
exfiltration across Windows and macOS devices
FALCON DATA PROTECTION FOR CLOUD | RUNTIME CLOUD
DATA PROTECTION
Provides real-time monitoring and classification of sensitive data in motion across cloud environments
using eBPF, enabling organizations to detect and respond to data risks without added complexity and
with minimal performance impact
Security and IT Operations
FALCON EXPOSURE MANAGEMENT | EXPOSURE MANAGEMENT
Provides full attack surface visibility, prioritizes vulnerabilities with AI, and automates remediation
to proactively reduce cyber risk and prevent breaches
FALCON EXPOSURE MANAGEMENT: CAASM
Allows you to discover and monitor managed and unmanaged assets in real time and visually
map assets and their relationships, revealing deep host insights into applications, browsers, CVEs,
and misconfigurations
FALCON FOR IT | IT AUTOMATION
Delivers AI-powered endpoint visibility, scalable response automation, and secure baseline
enforcement as a native capability of the Falcon platform
FALCON DISCOVER for XIoT | EXTENDED XIoT ASSET VISIBILITY
Delivers real-time visibility into unmanaged and adjacent XIoT assets to reduce security, safety,
and operational blind spots

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 55
FALCON EXPOSURE MANAGEMENT FOR XIoT | XIoT RISK MITIGATION
Provides contextual risk visibility and remediation guidance tailored to the operational complexity
of XIoT environments
FALCON FILEVANTAGE | FILE INTEGRITY MONITORING
Provides real-time, comprehensive, and centralized visibility that boosts compliance and offers
relevant contextual data
Managed Services
FALCON COMPLETE NEXT-GEN MDR | MANAGED DETECTION AND RESPONSE
Provides 24/7 expert-driven protection across endpoints, identities, cloud workloads, and third-party
Falcon Next-Gen SIEM data, combining elite security expertise, AI-powered technology, and proactive
threat hunting to detect, disrupt, and remediate sophisticated threats at machine speed

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 56
CrowdStrike Services
INCIDENT RESPONSE
Provides 24/7/365 elite incident response to contain threats, restore order, and mitigate breach impact
Incident Response Services | Provides comprehensive breach response and recovery, from triage and
investigation to cross-domain remediation and restoration, backed by world-class threat intelligence
and delivered by a highly experienced incident response team
Services Retainer | Provides prearranged, on-demand access to CrowdStrike experts for rapid incident
response and proactive consulting services that strengthen defenses over time
STRATEGIC ADVISORY SERVICES
Develops and matures the security program to improve defenses
Tabletop Exercise | Simulates incident response scenarios that expose process gaps and improve
coordination across the full team, from hands-on-keyboard analysts to executive stakeholders
Maturity Assessment | Comprehensively evaluates your organization’s security posture, identifying
gaps, benchmarking capabilities, and providing a prioritized roadmap to strengthen defenses against
evolving threats
Regulation Readiness and CXO Advisory | Helps you understand and prepare for cyber-related
regulation mandates, including the evolving risk and governance responsibilities of the board of
executives
Insider Risk Program Review | Strengthens your insider risk strategy by assessing and optimizing your
current detection, prevention, and response capabilities
RED TEAM SERVICES
Tests and validates defenses through emulated attacks that expose weaknesses
Penetration Testing | Provides attack emulations that test the detection and response capabilities of
your people, processes, and technology to identify vulnerabilities
Red Team/Blue Team Exercise | Increases response readiness under expert guidance, as a red team
attacks systems in a simulated exercise and a blue team mounts the defense
Cloud Breach Emulation and Response Exercise | Helps organizations test and enhance their CDR
capabilities through real-world adversary simulation
Adversary Emulation Exercise | Gauges readiness to defend against a sophisticated adversary
infiltration that employs advanced tradecraft

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 57
AI SECURITY SERVICES
Secures the AI powering your organization and uses AI to defend with scale, precision, and speed
AI Red Team Services | Exposes vulnerabilities in the GenAI stack that could be exploited by testing
LLM integrations for sensitive data exposure and adversarial manipulation
AI Systems Security Assessment | Provides Falcon-powered discovery and threat-informed testing to
uncover shadow AI, risky integrations, and governance gaps, delivering clear visibility and actionable
guidance
AI for SecOps Readiness | Provides expert guidance on integrating AI into detection and response
workflows with tailored use cases, architectural guidance, and a roadmap to increase response speed,
precision, and scale
TECHNICAL ASSESSMENT SERVICES
Audits and addresses security gaps across endpoints, cloud, and SaaS applications to tangibly
reduce risk
Technical Risk Assessment | Highlights security vulnerabilities, weaknesses, and gaps in the IT
environment across endpoint devices, applications, and user identities
Identity Security Assessment | Audits identity security practices and defense posture for weaknesses,
including Active Directory domain configuration, account configuration, privilege delegation, and
potential attack paths
Cloud Security Assessment | Identifies misconfigurations and vulnerabilities in the cloud estate that
could be exploited by adversaries
Compromise Assessment | Exposes and addresses undetected threat activity through a one-time
threat hunt available for endpoint, cloud, and SaaS applications
SaaS Security Assessment | Assesses SaaS environments for security gaps across configurations,
access controls, data policies, and third-party integrations
PLATFORM PROFESSIONAL SERVICES
Helps ensure your CrowdStrike Falcon deployment is expertly configured, optimized, and aligned
to your security needs; specialists provide best-practice implementation and deep module expertise
to maximize protection, improve efficiency, and achieve security outcomes faster
TRAINING AND SECURITY UPSKILLING
Builds security acumen and closes the skills gap through CrowdStrike University, offering on-demand
training, personalized learning paths, and five certifications for deep Falcon module expertise
CROWDSTRIKE PULSE SERVICES
Provides continuous consulting engagements via focused sessions on a recurring cadence (biweekly,
monthly, or every two months) tailored to your needs, aligned with your priorities, and adapted as needed,
enabling consistent progress, improved resilience, and strategic maturity that evolves at the speed of
the adversary

CROWDSTRIKE 2026 GLOBAL THREAT REPORT 5588
About
CrowdStrike
CrowdStrike (NASDAQ: CRWD), a global cybersecurity leader,
has redefined modern security with the world’s most advanced
cloud-native platform for protecting critical areas of enterprise
risk – endpoints and cloud workloads, identity and data.
Powered by the CrowdStrike Security Cloud and world-class AI,
the CrowdStrike Falcon® platform leverages real-time indicators of
attack, threat intelligence, evolving adversary tradecraft, and enriched
telemetry from across the enterprise to deliver hyper-accurate
detections, automated protection and remediation, elite threat
hunting, and prioritized observability of vulnerabilities.
Purpose-built in the cloud with a single lightweight-agent architecture,
the Falcon platform delivers rapid and scalable deployment, superior
protection and performance, reduced complexity, and immediate
time-to-value.
CrowdStrike: We stop breaches.
Learn more: www.crowdstrike.com
Follow us: Blog | X | LinkedIn | Facebook | Instagram | YouTube
Start a free trial today: https://www.crowdstrike.com/trial
© 2026 CrowdStrike, Inc. All rights reserved. CrowdStrike and CrowdStrike Falcon are marks owned by CrowdStrike, Inc. and are
registered in the United States and other countries. CrowdStrike owns other trademarks and service marks and may use the brands
of third parties to identify their products and services.