Organization: Cisco
Report Title: Talos-Year-In-Review
Year: 2025

## Table of Contents
- [Introduction](#introduction)
- [Top-targeted vulnerabilities](#top-targeted-vulnerabilities)
- [Ransomware](#ransomware)
- [Attacks against MFA](#attacks-against-mfa)
- [Email threats](#email-threats)
- [State-sponsored threats](#state-sponsored-threats)
- [AI threat landscape](#ai-threat-landscape)

---

## Introduction

Released in December. Disclosed 12+ years ago.
Ranked #1. Still top 10.
React2Shell (CVE-2025-55182) | Adobe ColdFusion (CVE-2013-0632)
Most targeted vulnerability of 2025 | Ranked No. 7 in 2025

The 2025 threat landscape was defined by an unprecedented acceleration in the speed of vulnerability exploitation, with adversaries weaponizing new security flaws like React2Shell and ToolShell almost immediately upon disclosure. This rapid pace of weaponization was contrasted by the enduring threat of legacy vulnerabilities, with older flaws such as Log4j and PHPUnit remaining top targets because they are deeply embedded in enterprise software stacks and third-party integrations. Furthermore, nearly 40% of the top-targeted vulnerabilities impacted end-of-life (EOL) devices, highlighting a systemic challenge where attackers consistently exploit the gap between vendor lifecycles and organizational patch management.

> The speed of weaponization and the longevity of exposure are defining characteristics of today’s threat landscape.

Network infrastructure became a primary battleground, which proved three times more common than user-managed devices, with attackers prioritizing identity gateways and registration platforms over individual devices. By targeting Application Delivery Controllers (ADCs) and network management tools, threat actors gained the ability to bypass multi-factor authentication (MFA), steal session tokens, and orchestrate movements across entire networks from a single point of control. Attackers are increasingly targeting the systems that validate trust and broker access.

MFA was a primary target in 2025 as threat actors focused their energy on undermining the very systems that verify and manage user identity. Automated attacks against the login flows of central access platforms grew more frequent as adversaries sought to seize authentication tokens, while device compromise attacks — where attackers register their own hardware as a trusted factor — surged by a staggering 178%. These operations relied heavily on social engineering, particularly voice phishing (vishing) aimed at IT administrators, breaking cryptocurrency thefts and successfully placed “fake” IT workers within Fortune 500 companies using AI-generated personas. 

Email threats also underwent change, moving toward lures that mimic everyday business workflows. Phishing subject lines shifted from generic spam to specific IT alerts, travel itineraries, and financial requests. A significant threat in 2025 was abuse of the Microsoft 365 Direct Send feature, which allowed attackers to spoof internal email addresses without compromising any accounts. By exploiting this legitimate feature, attackers delivered convincing messages that bypassed traditional authentication checks like SPF and DKIM, specifically targeting executives with lures related to compensation and urgent approvals.

On the geopolitical front, state-sponsored activity reached new levels of sophistication and frequency. Our China-nexus investigations increased by 74%, reflecting the breadth and increasing intensity of this threat landscape. Russian advanced persistent threats (APTs) continued to align their operations with the war in Ukraine and geopolitical sanctions, often targeting logistics and assistance networks. North Korea achieved record-breaking cryptocurrency thefts and successfully placed “fake” IT workers within Fortune 500 companies using AI-generated personas. Meanwhile, Iranian actors focused on maintaining stealthy access to telecommunications providers and utilized hacktivism as a low-cost tool for regional influence during the Israel-Hamas conflict.

Finally, the role of artificial intelligence became a dual-edged sword for the security community. While AI is not yet fully automating the attack lifecycle, it has significantly lowered the barrier for social engineering and enhanced the capabilities of advanced actors through deepfake technology. Organizations are now forced to defend against new AI-specific risks, such as context poisoning and prompt injection, while simultaneously integrating AI into their own defensive workflows to triage alerts and correlate malicious behaviors. Ultimately, Cisco Talos’ 2025 report underscores that modern security requires a shift in focus from simply patching to securing the identity, supply chain, and management planes that govern the modern enterprise.

---

## Top-targeted vulnerabilities

### Figure 1: Top 10 targeted vulnerabilities in 2025

The top 10 most targeted vulnerabilities of 2025 reveal a threat landscape driven by speed, scale, and the continued exploitation of long-standing weaknesses. The list blends newly discovered, rapidly weaponized flaws — such as the React2Shell and ToolShell vulnerabilities — with older, deeply embedded vulnerabilities like PHPUnit and Log4j that attackers continue to exploit at high volume. Together, these CVEs illustrate how adversaries combine opportunistic scanning, automated exploitation, and supply-chain fragility to consistently compromise exposed systems.

| Ranking | Vulnerability | Vendor/product |
| ------- | ------------- | -------------- |
| 1 | CVE-2025-55182 | React Server Components (aka React2Shell) |
| 2 | CVE-2017-9841 | PHPUnit |
| 3 | CVE-2025-49704 | Microsoft SharePoint (aka ToolShell) |
| 4 | CVE-2025-49706 | Microsoft SharePoint (aka ToolShell) |
| 5 | CVE-2025-53770 | Microsoft SharePoint (aka ToolShell) |
| 6 | CVE-2025-53771 | Microsoft SharePoint (aka ToolShell) |
| 7 | CVE-2013-0632 | Adobe ColdFusion |
| 8 | CVE-2021-44228 | Apache Log4J (aka Log4Shell) |
| 9 | CVE-2021-44832 | Apache Log4J (aka Log4Shell) |
| 10 | CVE-2021-45046 | Apache Log4J (aka Log4Shell) |

### React2Shell redefines attacker speed and targeting

React2Shell’s rapid rise to the most targeted vulnerability of 2025 — despite only being disclosed in December — highlights a fundamental shift in how quickly attackers operationalize new flaws and where they choose to strike. The vulnerability’s immediate exploitation reflects near-instant weaponization, driven by automated tooling and widespread internet exposure, leaving defenders little to no time between disclosure and active abuse. Additionally, React2Shell highlights attackers’ growing focus on the user-facing parts of software where business logic, session handling, and identity decisions take place. Its rapid adoption reflects a clear preference for entry points that are easy to automate, widely deployed, and capable of delivering immediate impact.

**Security takeaway:** This trend shows that attacker prioritization is now guided less by vulnerability age or maturity and more by exposure, exploitability, and proximity to trust, reshaping how organizations must think about risk in modern environments.

### ToolShell’s quick rise to the top five highlights sheer volume and impact of attacks

The presence of the ToolShell vulnerabilities, all disclosed mid-2025, inside the top five most targeted CVEs of the year is another strong indicator of the extraordinary speed and scale at which threat actors mobilize around newly exposed weaknesses. These vulnerabilities rapidly became high-frequency exploitation targets across ransomware gangs, botnets, and state-aligned actors, despite having only months of exposure time compared to the years-long runway of older CVEs on the list.

**Security takeaway:** For organizations, the speed at which these CVEs climbed into the top tier reflects a larger systemic challenge: Newly disclosed vulnerabilities in widely deployed software can generate significant, organization-wide impact long before typical patch cycles catch up, leaving defenders with small reaction windows and escalating consequences for even short-lived exposure.

### Four years after disclosure, Log4j remains one of the most targeted vulnerabilities in the threat landscape

The Log4Shell CVEs still appear in Talos’ top 10 most targeted vulnerabilities, underscoring Log4j’s status as one of the most persistent and operationally valuable exploits in modern cyber operations. Despite being disclosed in late 2021, Log4j continues to dominate attacker tooling because it remains deeply embedded in countless enterprise applications, third-party integrations, legacy systems, shadow IT assets, and unmanaged internet-facing services. Its presence across such a broad and distributed ecosystem means that full eradication remains elusive, even years later. Threat actors from opportunistic botnet operators to advanced state-backed groups continue to rely on Log4j as a highly reliable initial access vector, exploiting it at enormous scale through automated scanning and bulk exploitation campaigns.

**Security takeaway:** Vulnerabilities in critical open-source components can produce multi-year, ecosystem-wide exposure, where even aggressive patching efforts cannot fully neutralize the attack surface. For organizations, this underscores the long-term impact of supply chain dependencies and the enduring risk posed by vulnerabilities that are easy to exploit and impossible to fully eliminate.

### Old dev tool vulnerabilities round out the top 10, highlighting the longevity of “easy” exploits

The prominence of vulnerabilities tied to developer tools and frameworks, such as PHPUnit (CVE-2017-9841) and Adobe ColdFusion (CVE-2013-0632), highlights how the development ecosystem has become a persistent source of risk. PHPUnit is a widely used testing framework for the PHP programming language that helps developers ensure their code works correctly. It powers a significant portion of the internet, underpinning popular sites such as Facebook, Wikipedia, WordPress, Shopify, Etsy, and Slack. Many organizations similarly rely on Adobe ColdFusion, which they use to build and maintain web and mobile applications. Key uses for Adobe ColdFusion include creating APIs, building reports and dashboards, manipulating files and images, and connecting to external services like Microsoft products and Java. Because development tools and frameworks are widely bundled, inconsistently versioned, and often forgotten post-deployment, their vulnerabilities produce long-tail exposures that attackers can exploit for years or even decades.

**Security takeaway:** Components like PHPUnit, ColdFusion, and Log4j often end up buried inside applications where defenders may not even realize they exist and/or be tightly coupled to legacy applications, making updates disruptive and resource intensive. As a result, they fall outside normal patch cycles and asset inventories, leaving long-term blind spots that attackers routinely exploit. For organizations, development ecosystem components require the same visibility, inventorying, and patch rigor as traditional infrastructure.

> Because development tools and frameworks are widely bundled, inconsistently versioned, and often forgotten post-deployment, their vulnerabilities produce long-tail exposures that attackers can exploit for years or even decades.

### The top 100 vulnerabilities by the numbers

The top 100 most targeted vulnerabilities reveal a threat landscape shaped by rapid weaponization, ongoing exploitation of long-standing CVEs, and persistent weaknesses in both modern and legacy systems. The list blends newly disclosed remote code execution (RCE) vulnerabilities with decade-old flaws — many affecting EOL devices that organizations can no longer patch — highlighting how outdated infrastructure continues to expand the attack surface.

Across these CVEs, attackers consistently prioritize software and firmware inside network appliances, identity-adjacent systems, and widely deployed open-source components, reflecting a clear focus on the elements that control access and connectivity. Taken together, these vulnerabilities offer a concise snapshot of where adversaries find the most operational leverage and where defenders face the most chronic, systemic challenges.

- **80%** of vulnerabilities in our dataset were RCE flaws, which allow adversaries to bypass identity controls, eliminate the need for phishing, and gain footholds even on highly segmented networks. They also lend themselves to automation and mass scanning, making them the preferred type of vulnerability for both sophisticated threat actors and commodity botnets.
- **Nearly 40%** of the 100 top-targeted vulnerabilities directly impact EOL devices. Threat actors continue to weaponize old vulnerabilities because they know many organizations still have unpatched legacy assets in production, especially network hardware, VPN appliances, and web servers. These CVEs are often used for initial access, particularly on perimeter devices that lack endpoint detection and response (EDR) visibility. Patching and asset retirement policies generally lag vendor lifecycles, and attackers deliberately exploit this gap.
- **About 25%** of the vulnerabilities on our top 100 list affect widely used frameworks and libraries that are used across the software ecosystem, highlighting the risk of supply chain-style attacks. These widely used components — like Log4j, Spring, Tomcat, or OpenSSL — sit deep within the software stack and are foundational to how applications and many network appliances operate, meaning a single CVE can yield mass exploitation potential across industries. Moreover, since these are codebase-level vulnerabilities, the impact is rarely confined to a single product, making software supply chain attacks an inherent risk. A single vulnerability in application frameworks and libraries can reappear in dozens of products across vendors, creating a massive attack space for adversaries to exploit. This situation creates systemic weaknesses that persist across multiple hardware and software ecosystems.
- **Network devices are prime targets:** 23% of CVEs directly impact network devices like VPN appliances, next-generation firewalls (NGFWs), load balancers, routers, and others. Since these systems sit at the perimeter of enterprise environments, compromise may lead to direct access to the critical networks. Attackers don’t need many network-device CVEs, they only need a handful of highly exposed, reliably exploitable ones. This aligns with real-world trends from CISA’s Known Exploitation Vulnerability (KEV) catalog, where exploitation consistently favors edge devices because they are internet-facing, often lag in patching, and provide direct operational leverage once compromised.

### 100 top-targeted vulnerabilities by type
- **80%** Remote Code Execution (RCE)
- **8%** Authentication bypass
- **3%** Path traversal
- **3%** Information disclosure
- **3%** Denial-of-service (DoS)
- **2%** Buffer overflow
- **1%** SSRF
- **32%** of vulnerabilities are at least a decade old.

### Figure 2: Company size impacts CVE targeting trends

In 2025, small organizations saw a greater variety of threats impacting them at equal intensity, while medium and large organizations were impacted by fewer CVEs at a disproportionately higher rate. Medium and large companies had a handful of vulnerabilities (see Figure 2) that experienced notably more targeting than the rest, whereas small companies had a much more even distribution of exploitation activity across all CVEs. This is likely due to several factors. First, large organizations tend to have more standardized infrastructure and run widely deployed software. This reduces variability, meaning that successful exploitation of a single CVE in these platforms could yield massive payoffs, so attackers disproportionately focus on a handful of high-value vulnerabilities. Technology diversity is also a factor; smaller organizations use a wider mix of off-the-shelf, consumer-grade IT products that may be cheap, widely available, and bundled with ISP or MSP services. This often leads to multiple brands, mixed operating systems (OSs), and older hardware, meaning that more unique CVEs are applicable to their environment. Lastly, small organizations are often victims of opportunistic scanning for unpatched CVEs, while large entities attract strategic campaigns where attackers deliberately weaponize specific CVEs for maximum disruption.

*Small companies saw the most variability in CVE exploitation attempts, compared to medium and especially large companies, where a smaller number of vulnerabilities accounted for a larger amount of the threat activity.*

### Figure 3: CVE age distribution

32% of vulnerabilities are at least 10 years old. Despite their age, many of these flaws remain exploitable for many reasons, often because they affect core components (e.g., Bash, PHP, Apache Struts) that exist everywhere. These CVEs are easy to weaponize, with publicly available proof-of-concept (PoC) code and fully automated scanners and bots that continuously probe the internet for vulnerable systems, requiring minimal effort and cost on the part of the adversary. Moreover, many older CVEs — like those affecting VPNs, web servers, and firewalls — provide direct initial access to a network. For example, CVE-2018-13379 (Fortinet), CVE-2019-11510 (Pulse Secure), and CVE-2020-5902 (F5 BIG-IP) are all over five years old but were still actively targeted in 2025 because they provide immediate remote access.

- **0 - 2 years:** 15%
- **3 – 5 years:** 33%
- **6 – 10 years:** 31%
- **11+ years:** 21%

### Figure 4 & Figure 5: Top 50 network infrastructure CVEs and Identity Role

> In 2025, the majority of attacker activity against network infrastructure focused on the systems that validate, enforce, or broker identity.

A clear theme emerged from this year’s data: Attackers are targeting identity by compromising the infrastructure that sits around it — both physical hardware devices and the very software and management platforms that run them. Network components often act as de facto identity gateways, and when they are breached, adversaries gain the ability to impersonate users, bypass MFA, and traverse networks undetected. This is why, in 2025, the majority of attacker activity against network infrastructure focused on the systems that validate, enforce, or broker identity.

| Category | Identity role |
| --- | --- |
| **VPNs, Firewalls and NGFWs** | Authenticate users directly and create trusted sessions; compromise enables user impersonation and bypass of MFA. |
| **Application delivery controllers (ADCs) and load balancers** | Broker SSO and validate identity tokens; compromise exposes or alters authentication flows. |
| **Network access infrastructure** *(Note: Includes network access control platforms, wireless access controllers, and access gateways)* | Authenticates users and devices, enforces identity based policy, and determines whether access to the network is granted at all; compromise allows attackers to bypass authentication and assign privileged access roles. |
| **Network management platforms** | Hold privileged admin credentials; compromise enables broad identity and device-level escalation. |
| **Routers** | Routes packets; no user or device authentication. |
| **Switches** | Operates at OSI layer 2 (Data Link layer); no identity decisions. |
| **DNS servers** | Resolves names, doesn’t validate users. |
| **Load balancers** | Distributes traffic; not identity-aware. |

### Identity at the edge: How attackers exploit network devices to become trusted users

When attackers target identity control points, they can bypass traditional security and remain hidden inside the system as “trusted” users with access to high-value resources. This step-by-step process turns a single break-in into long-term operational control.

1. **VPN gateway (Identity entry point):** Attacker compromises VPN device to gain initial access as valid user.
2. **Firewall (Policy enforcement):** Exploits user-based firewall rules to move from public/DMZ to internal network.
3. **Internal gateway (Identity broker):** Targets the system that brokers identity and delivers SSO to achieve full user impersonation and long-term persistence as valid identity.
4. **ADC (App-layer trust):** Pivots to the ADC admin interface, gaining access to every app it controls.
5. **Network management platform (Sensitive internal apps):** Leverages valid tokens to access business-critical systems, deploy payloads, and exfiltrate data.
6. **Routers (Device management systems):** Gains admin control over large groups of network devices, achieving structural compromise of the environment. Attacker finally compromises network infrastructure devices to establish deep stealth and longer-term operational control.

### Management platforms offered attackers a single point of control

Network management platforms, which accounted for nearly a quarter of the CVEs in our dataset, are valuable to attackers because they control the configuration, monitoring, and orchestration of devices that run the network. Vulnerabilities in tools like vCenter Server, Aria Operations for Networks, and Cisco Security Manager give adversaries direct access to privileged administrative functions, device credentials, and automation pipelines that touch dozens of downstream systems, making these devices powerful force multipliers.

Why the management plane matters: Network management platforms are not network devices, but attackers treat them as part of the same attack surface because they control network devices. From an adversary perspective, these systems are functionally equivalent to compromising a high-value network device because they:
- Store device credentials
- Can push configs to firewalls, routers, VPNs
- Orchestrate virtual switching and routing
- Can modify identity hookups (RADIUS, SAML, LDAP)
- Provide complete visibility into the environment

While these platforms are not devices, they are clearly network-infrastructure control points. This is why APT groups frequently target vCenter, FortiManager, Cisco Security Manager, Panorama, and Aria Ops. A single compromise of a management-plane platform can yield access equivalent to compromising dozens of edge appliances, making them strategically important to include when assessing 2025 network infrastructure threat trends.

Common ADC CVEs:
- CVE-2020-5902 (F5 BIG-IP)
- CVE-2023-3519 (Citrix ADC)
- CVE-2023-4966 (“CitrixBleed”)

### Application delivery controllers (ADCs) play a critical role as high-impact identity gateways into critical applications

Application delivery controllers (ADCs) play a critical role in an organization’s network infrastructure and accounted for 22% of the top 50 targeted network devices. ADCs, like Citrix ADC and F5 BIG-IP, are essentially a load balancer with identity and access control features. They handle SAML and OAuth flows, session cookies, TLS keys, and often enforce MFA and access policies — effectively making them part of the identity infrastructure. By exploiting vulnerabilities in these devices, attackers can intercept authentication data, extract session tokens, and impersonate users across multiple applications at once. Compromising a single ADC can expose hundreds of downstream systems. This means that even a single compromise could cascade into organization-wide exposure without requiring attackers to breach each router, firewall, or appliance individually. These systems also tend to be less monitored than identity providers or edge appliances, allowing attackers to operate with greater stealth. The small percentage share in our dataset can be misleading for organizations — network management CVEs remain among the most consequential vulnerabilities in the ecosystem because compromising them equates to compromising the entire network they govern.

For organizations, this means ADCs must be protected as identity control points, not merely performance appliances.

### Why are vulnerabilities impacting shared OS and platform software disproportionally dangerous?
- **Cross multiple device classes:** Platform software runs across many hardware models and device types, meaning a single vulnerability can simultaneously expose large portions of the infrastructure. Unlike device-specific flaws, these are not contained to one product line or deployment tier.
- **Uniformly exposed and highly scalable to attack:** Unlike enterprise applications, network infrastructure hardware is rarely customized and deployed identically across thousands of organizations. This creates a perfect environment for automated, mass exploitation.
- **Ultimate stealth:** Once an attacker compromises an appliance’s software layer, they gain the ability to hide command-and-control (C2) channels inside legitimate flows and other access that allows far more stealth than in host-based compromises.
- **Hard to contain:** Patching requires coordinated, often disruptive upgrades, so organizations may delay remediation. This creates long-lived, systemic risk rather than isolated exposure.
- **Deep operational control:** Targeting the software layer inside network appliances gives adversaries deep access, allowing admin-level control, manipulation of security policies, credential harvesting, and the ability to reroute and decrypt traffic. Attackers want to operate the device, not simply break in.
- **Immediate identity access:** Nearly all network appliance software sits at some form of identity boundary, including VPN gateways that authenticate users and firewalls that broker trusted vs. untrusted segments, meaning a single compromise can yield MFA bypass, session token theft, and the ability to impersonate valid users.

### Figure 7: Vulnerability scope and risk

A small number of vulnerabilities drive outsized risk to attackers (see Figure 7). Platform software vulnerabilities, though relatively rare at just 14% of CVEs, carry outsized impact because they span multiple device classes simultaneously, meaning a single flaw can expose routers, switches, and controllers simultaneously. Embedded services and management software, together accounting for 20% of CVEs, further concentrate risk by exposing authentication workflows and aggregating privileged administrative access.

While device firmware vulnerabilities dominate by volume, they are typically narrow in scope and limited to individual models, meaning their prevalence does not always translate to proportional impact or attacker scalability. Collectively, these higher-leverage vulnerability classes enable identity compromise, policy manipulation, and infrastructure-wide escalation far beyond what isolated device flaws typically allow (see Figure 7).

> Platform software vulnerabilities, though relatively rare at just 14% of CVEs, carry outsized impact because they span multiple device classes simultaneously, meaning a single flaw can expose routers, switches, and controllers simultaneously.

---

## Ransomware

### Persistent threats, techniques, and industry targeting

Ransomware remained a dominant threat to enterprises globally in 2025, driven by operators continuously evolving their tactics, techniques, and procedures (TTPs) to enhance ransomware-as-a-service (RaaS) capabilities and intensify pressure on victims. Manufacturing was the most targeted sector, likely due to these organizations’ low downtime tolerance and wide attack surfaces that can amplify the impact of attacks. Qilin emerged as the most active group by attack volume during the year, while Akira and Play retained their dominant presence from 2024. Cisco Talos Incident Response (Talos IR) engagements showed ransomware operators heavily relying on the exploitation of identity-based weaknesses, leveraging social engineering for initial access, valid accounts throughout the attack cycle, and built-in remote management tools that typically require user credentials for lateral movement and execution. Overall, ransomware remains one of the most adaptive and disruptive cyber threats, underscoring the need for continuous detection and rapid response. Organizations that fall into repeatedly targeted sectors should assume an elevated baseline risk and prioritize ransomware-specific defensive controls accordingly.

### Manufacturing most impacted in 2025, underscoring persistent risk to repeatedly targeted sectors

Talos’ analysis of ransomware actors’ data leak site posts revealed that operators targeted manufacturing entities the most in 2025 and focused their efforts against the same top sectors as in years past, likely due to proven and reliable success (see Figure 8). Manufacturing is a persistently vulnerable industry vertical for ransomware attacks as these organizations often have very low downtime tolerance, operate hybrid environments that incorporate both IT and OT systems (thereby expanding the attack surface), have less robust cybersecurity budgets compared to other sectors such as finance, and rely on insecure legacy equipment and/or software.

Professional, scientific, and technical services was the second-most targeted sector and encompasses entities that are involved in IT consulting, engineering, scientific research, legal services, and accounting, amongst others. These organizations often provide essential services to critical infrastructure sectors and thereby also likely are affected by a low downtime tolerance.

### Figure 8: Industry targeting year-over-year

*Note: The “unknown” categorization represents posts that did not name a specific victim or named a victim that could not be placed in an appropriate industry categorization by our automated tools.*

- Manufacturing
- Professional, scientific, and technical services
- Wholesale trade
- Construction
- Health care and social assistance
- Retail trade
- Information
- Finance and insurance
- Unknown
- Real estate, rental and leasing
- Other services
- Administrative, support, waste management, and remediation
- Educational services
- Transportation and warehousing
- Public administration
- Accommodation and food services
- Arts
- Utilities
- Agriculture
- Mining
- Management of companies and enterprises

### Qilin dominates in 2025, while Akira and Play demonstrate rare, sustained momentum as top groups

Qilin was the most seen ransomware variant in 2025, both in Talos IR engagements as well as in terms of the volume of posts to its data leak site (see sidebar at left). Qilin, formerly known as Agenda, has been active since approximately July 2022 and its operators are likely based in Eastern Europe or a Russia-speaking region, based on the presence of Russian in their scripts and recruitment posts and refusal to target countries within the Commonwealth of Independent States (CIS).

Other top groups in 2025 included Akira and Play, ranked second and third, respectively (see Figure 9). Notably, these groups were also in the top five last year, displaying a certain longevity that is rare in this threat space where groups frequently emerge, rebrand, fragment, or disappear completely under law enforcement pressure or internal disputes. Their continued success can likely be credited to attributes such as their evolving and adaptable tactics and absorption of affiliates from defunct ransomware groups. By contrast, the popularity of the other groups in last year’s top five fell significantly this year, with LockBit 3.0 moving from first to 35th, RansomHub from second to eighth, and Hunter’s International from fifth to 28th. These declines may have been influenced by sustained law enforcement pressure — most notably in LockBit’s case, where Operation Cronos in 2024 dismantled key infrastructure, exposed affiliate identities, and led to arrests and indictments.

### Threat actor spotlight: Qilin

Qilin emerged as a dominant force in 2025, responsible for the largest share of Talos IR ransomware engagements and posts to data leak sites of all groups we track. Our analysis and understanding of this ransomware-as-a-service (RaaS) group reveals numerous possible reasons for their success this year:
- **Double-extortion strategy:** Qilin employs a double-extortion strategy, combining file encryption with the threat of public disclosure of stolen information to increase pressure on victims. According to their data leak site, in 2025, Qilin targeted more than 40 victims every month except January, signaling that this ransomware group will remain a persistent and significant threat in 2026.
- **Affiliate payout:** Qilin affiliates take home a significant portion of their ransom payments (up to 80 - 85%), higher than typical RaaS payout structures.
- **Targeting capabilities:** Qilin ransomware is written in both Golang and Rust, enabling it to target a wide array of operating systems and expanding its potential victim pool.
- **Comprehensive services:** Qilin offers some unique services to affiliates, including legal assistance, in-house journalists, automated negotiation services, distributed denial-of-service (DDoS) attack capabilities, and spam campaign support.
- **Recruitment strategy:** The group actively recruits affiliates on hacking forums like RAMP and XSS, advertising its technical advantages, customizable attacks, and generous revenue splits.

### Figure 9: 2025 volume of posts made to data leak sites by ransomware groups
- **17%** Qilin
- **10%** Akira
- **6%** Play
- **5%** INC Ransom
- **5%** SAFEPAY
- **4%** Lynx
- **4%** DragonForce
- **3%** RansomHub
- **3%** Sinobi
- **3%** World Leaks
- **2%** KillSec
- **2%** Medusa
- **2%** Everest Group
- **1%** Rhysida
- **1%** NightSpire
- **33%** Others

### January remains least active month for ransomware activity, potentially offering a window for defenders to test readiness

January yielded the lowest volume of ransomware attacks in 2025 as it did in 2024, according to analysis of Talos IR ransomware engagements and ransomware groups’ posts to data leak sites. These two data sets aligned fairly closely throughout the year, with concurrent activity spikes in April, October, and December (see Figure 10). The significant dip in January could possibly be attributed to the winter holidays as both actors and targets take leave from work through the beginning of the new year, reducing opportunities for attacks facilitated by methods such as social engineering. Further, many ransomware groups (such as the aforementioned Qilin) are Russian-speaking and presumed to be operating out of Russia or other Eastern European countries where public holidays extend from late December through Orthodox Christmas in early to mid-January.

It may be wise for security teams to consider testing ransomware defenses in months where activity levels are generally lower, such as January, as there is a reduced chance of interfering with real incidents. Testing during a low-activity period can give defenders the opportunity to identify weaknesses and implement fixes before activity peaks in the spring. Key defenses to consider testing include processes and protections for backups, EDR and logging capabilities, network segmentation, phishing and social engineering training, and patch management, amongst others.

### Figure 10: Ransomware attacks by month (DLS posts)
- **January:** Orthodox Christmas / Decrease in active threat actors / Attack emulation dip
- **February:** Tax season / Increase in financial lures
- **March**
- **April**
- **May**
- **June**
- **July**
- **August:** Potential contribution to dip in August attack surface
- **September**
- **October:** Increase in users online and phishing / Back-to-school
- **November:** Potential contribution to dip in November / BlackSuit infrastructure seized
- **December:** Interpol's Operation Sentinel

### Figure 11: Top tools seen across Talos IR ransomware engagements in 2025
- RDP
- PsExec
- PowerShell
- nltest
- QuickAssist
- AnyDesk
- Brute Ratel / BRC4
- MIS.log/rsockstun
- SoftPerfect
- TeamViewer
- Mimikatz
- Lazagne
- Splashtop
- Rclone
- SimpleHelp
- LogMein
- Impacket
- Cyberduck
- WinSCP
- TitanPlus
- netscan

Identity played a major theme in ransomware engagements throughout the year as evidenced by our MITRE ATT&CK technique analysis. For example, use of valid accounts appeared across multiple attack phases, demonstrating how compromised identity is leveraged throughout the attack lifecycle. Phishing and valid accounts as top initial access methods further highlights this theme, showing that actors predominately targeted the person who holds the key rather than the lock itself (i.e., the target’s infrastructure). Lastly, the top three tools consistently seen across these engagements — RDP, PsExec, and PowerShell — typically require valid user credentials and user permissions to function, supporting the notion that identity will continue to play a major role moving into 2026.

### Top ransomware attack techniques as seen in Talos IR engagements

We pulled the top techniques seen during steps of the MITRE ATT&CK chain in 2025 Talos IR ransomware engagements, which can potentially assist defenders in prioritizing certain detections and defenses.

| Reconnaissance | Persistence | Discovery | Exfiltration |
| -------------- | ----------- | --------- | ------------ |
| 1. Phishing for Information | 1. Valid Accounts | 1. System Network Configuration Discovery | 1. Exfiltration Over Alternative Protocol |
| 2. Active Scanning | 2. Create Account | 2. File and Directory Discovery | 2. Exfiltration Over C2 Channel |
| 3. System Information Discovery | 3. Scheduled Task/Job | 3. Account Discovery | |

| Initial Access | Defense Evasion | Lateral Movement | Impact |
| -------------- | ---------------- | ---------------- | ------ |
| 1. Phishing | 1. Impair Defenses | 1. Remote Services | 1. Data Encrypted for Impact |
| 2. Exploit Public-Facing Application | 2. Indicator Removal | 2. Windows Management Instrumentation | 2. Inhibit System Recovery |
| 3. Valid Accounts | 3. Modify Registry | | 3. Service Stop |

| Execution | Credential Access | C2 |
| --------- | ----------------- | -- |
| 1. Windows Management Instrumentation | 1. Steal or Forge Kerberos Tickets | 1. Ingress Tool Transfer |
| 2. Command and Scripting Interpreter | 2. OS Credential Dumping | 2. Communication Through Removable Media |
| 3. Valid Accounts | 3. Valid Accounts | 3. Remote Access Software |

---

## Attacks against MFA

### MFA spray attacks: Attackers double down on IAM while expanding efforts against high-value privileged accounts

In 2025, nearly a third of MFA spray attacks targeted identity and access management (IAM) applications, as attackers zeroed in on the very software tools t[runcated in source]

---

## Email threats

*[Content included in introduction and general summaries]*

---

## State-sponsored threats

*[Content included in introduction]*

---

## AI threat landscape

*[Content included in introduction]*

---
*(End of Report)*

---

hat control user access to resources 15% Network security 5% Application delivery and security
(see Figure 12). This marks a six percent increase from 2024
(see sidebar at right). The growing rise in spray attacks against 13% Authentication and networking 3% Privileged access management
IAM applications shows that threat actors are doubling down
7% Software development kit (SDK)
2% Authentication and network access control (NAC)
on single sign-on (SSO) and conditional access-protected login
flows. These apps are highly attractive targets because successful
6% Remote access
1% Directory services
attacks have high return, with adversaries gaining access to SSO
tokens, role changes, MFA policy changes, and user credentials. 5% API Communication Protocol
1% Virtual desktop infrastructure (VDI)
We also saw an increase in privileged access management (PAM)
5% Authentication protocol
1% Email and collaboration
and OS applications. PAM applications manage highly privileged
accounts, like administrators, making them extremely high-value
targets. Similarly, access to OS applications would grant an
attacker broad access, including to other credential stores like
password vaults and Kerberos tickets, browser cookies, SSH
keys and VPN certificates, and the ability to plant malware. A
single MFA success at these layers collapses multiple security
Noteable year-over-year trends
boundaries at once, delivering immediate control, persistence,
and scale.
IDENTITY AND ACCESS PRIVILEGED OPERATING APPLICATION DELIVERY
While attacks against certain application types rose, we also saw
MANAGEMENT (IAM) ACCESS MANAGEMENT SYSTEM AND SECURITY REMOTE ACCESS
attacks decrease against other targets, notably the more legacy
systems like application delivery and remote access. This is likely
due to organizations moving to more mature remote access and
+6% +3% +2%
2025: 30% 2025: 3% 2025: 5% 2025: 5% 2025: 6%
network controls, at least for VPN. For example, organizations
continue to move from local systems like LDAP/RADIUS to
2024: 24% 2024: 0% 2024: 3% 2024: 9% -4% 2024: 9% -3%
cloud-based identity providers, like Microsoft Entra ID, for VPN.
These newer cloud-based systems often have much better MFA
functionality and brute force protection than the local systems.
page 20

Attacks against MFA
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 21
5202
WEIVER
NI
RAEY
How do MFA spray and MFA spray attack MFA fatigue attack
MFA fatigue attacks differ?
MFA spray attacks are a highly common identity-
based intrusion technique that allows attackers
to target thousands of accounts across many
organizations with minimal effort.
During an MFA spray attack, a threat actor tries
a small set of common passwords across many
accounts with hopes that one will be weak
Many accounts One stolen credential pair
enough to work or that one of the many users
they are targeting will inadvertently approve an
MFA request. These differ from MFA fatigue or
MFA bombing attacks, where the attacker floods
a single user with nonstop MFA prompts in
attempt to wear them down into approving one.
The core distinction is scope: Spray attacks cast
a wide net with a few passwords, while fatigue
attacks zero in on one compromised account
and overwhelm it with authentication requests.
Overwhelming number of MFA prompts
Few passwords

Attacks against MFA
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 22
5202
WEIVER
NI
RAEY
Device compromise attacks: access to the account. This allows them to bypass future device registration itself is now a high-value attack
MFA challenges, move laterally within the network, access surface, not just MFA challenge approvals. User-
Significant rise in activity
sensitive information, and impersonate the user to send managed registration refers to MFA spray and
shows actors value reliable, to send internal phishing or business email compromise fatigue attacks, adversary-in-the-middle (AitM)
(BEC) emails to other targets. operations, or session hijacking and result in the attacker
repeatable access
adding their own device to the victim’s MFA account in
When we look at how device compromise attacks
the user’s portal.
Device compromise attacks are another common, yet were carried out in 2025, we see actors gaining access
much more targeted, method of MFA compromise. In primarily by tricking administrators into registering Link-initiated registrations were the third-most
device compromise operations, an adversary fraudulently devices on their behalf, often through voice phishing common access vector in this data set, where threat
registers an authenticator device used to approve MFA, (aka vishing) operations (see Figure 14). In fact, attackers actors can add their device by intercepting authorization
allowing them to satisfy MFA challenges without the overwhelmingly targeted the administrator-managed codes or links sent to the intended user. For example, an
victim’s involvement. In effect, the attacker makes their registration flow at a rate of three to one, highlighting their attacker who already had compromised the victim’s email
device a trusted MFA factor (see page 23). The number strong preference for targeting single high-value victims account could access any validation links sent from the
of device registration events reported by users as fraud and heavy reliance on social engineering to enable such MFA provider. MFA registration codes or links could also
increased 178% from 2024 to 2025, indicating growing operations. Administrator-driven compromise is particularly be exploited via SMS channels or phishing links.
attacker activity targeting this surface (see Figure 13). This common in university IT environments and help desks writ
New user registrations were relatively rare, accounting
shows that attackers are increasingly seeking the type of large, often due to high admin workload and limited ability
for just two percent of device compromise attacks. This
long-term and privileged access that successful device to perform thorough verification.
refers to a threat actor compromising the username and
compromise operations afford. Once an attacker controls
User-managed registration was the second-most password of a user not previously enrolled in MFA.
a registered MFA device, they gain persistent, high-trust
common path to device compromise, reinforcing that
sesac
fo
rebmuN
Figure 13 Figure 14
Fraudulent device registration events, 2024 – 2025 Top access vectors in device
compromise attacks
2024 2025
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
77% Administrator-managed registration
12% User-managed registration
5% Link-initiated registration
2% New user registration
4% Other
The number of device registration
events reported by users as fraud
increased 178% from 2024 to 2025,
indicating growing attacker activity
targeting this surface.

5202
WEIVER NI RAEY
Attacks against MFA
How do device compromise and spray attacks differ?
VS.
|                                                     | Device compromise attack |     |                | MFA spray attack                            |
| --------------------------------------------------- | ------------------------ | --- | -------------- | ------------------------------------------- |
| Authentication device (phone, hardware token, etc.) |                          |     | Primary target | Authentication portals (VPN, SSO, web apps) |
Goal
Control the user’s device, act as user Find one weak account with poor MFA/password hygiene
|     |     | Stealthy and highly targeted | Noise level | Low-noise, large-scale identity probing |
| --- | --- | ---------------------------- | ----------- | --------------------------------------- |
Attempts to defeat MFA through guesses;
|     | May bypass MFA by stealing sessions/tokens |     | MFA relevance |     |
| --- | ------------------------------------------ | --- | ------------- | --- |
precursor to MFA fatigue attack
|                                                             | Full compromise of user identity and device |     | Outcome       | Single-account initial access             |
| ----------------------------------------------------------- | ------------------------------------------- | --- | ------------- | ----------------------------------------- |
| Software vulnerabilities, vishing, phishing, mobile malware |                                             |     | Attack vector | Credential guessing, minimal MFA triggers |
© 2026 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com page 23

Attacks against MFA
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 24
5202
WEIVER
NI
RAEY
Industry trends: Actors tailor manufacturing is a dual-threat environment because both the Figure 15
identity and device layers present opportunities for attackers (see
Volume of MFA spray and device compromise attacks per industry
their MFA attack style depending
page 25).
on the sector
The most glaring observable is that higher education ranks first in
device compromise attacks but is nearly absent in spray attacks,
Comparing the industry trends for opportunistic MFA spray
a striking contrast that highlights some earlier insights, notably 5%
attacks and more targeted MFA device compromise attacks
that device compromise thrives in environments with diverse,
provides some interesting insights about threat actor behavior. At
unmanaged devices. Colleges and universities are easy targets
a high level, we can see that actors prefer MFA spray operations 9%
in these cases because they have a highly heterogeneous,
in environments with predictable identity behavior, while device 36% Technology
unmanaged device population, that must support personal laptops,
compromise thrives in environments with diverse, unmanaged, or
Manufacturing
mobile devices, tablets, shared lab computers, and bring-your-
high-turnover device ecosystems.
own-device (BYOD) capabilities. Moreover, many of these are often 9% Telecommunications
MFA spray attacks are clustered, with just a few industries running outdated OS versions, poorly patched, and unmanaged.
Financial services
dominating. Technology is the top-targeted industry at 36%, While this setting is ideal for device compromise, it likely makes
Health care
likely due to companies in this sector having more consistent MFA spray attacks less efficient because MFA and passwords are
MFA SPRAY
IAM enforcement (see Figure 15). Spray attacks thrive on not uniform. Higher education also has to manage so many rotating 9% ATTACKS Retail
uniformity, and in enterprise environments, like those at tech students and devices that they often have low verification policies
Higher education
companies, password hygiene tends to be consistent and for registering new devices.
Insurance
standardized across the workforce. This creates scenarios 24%
Another reason why higher education is targeted more frequently
where users have common password patterns, they may tend to Business services
in device compromise attacks than MFA spray attacks is because
reuse passwords, and/or the organization enforces predictable
K – 12 education
they have extremely large, public-facing user directories.
password policies that may be easier to guess. Moreover, login
Students, alumni, faculty, and staff accounts are enormous in Legal services
patterns are highly predictable, with employees’ work schedules
number, often publicly discoverable, recycled or long-lived, and 16%
being largely consistent. Utilities
globally accessible. This produces rich, high-fidelity targeting
Government
Manufacturing appears prominently in both data sets, but for data for threat actors to create tailored phishing operations. On
different reasons. Manufacturing companies typically have a the other hand, spray attacks often become noisy and ineffective Real estate and construction
large, distributed, shift-based workforce, creating predictable in this environment, as most universities enforce strict account
Transportation & Storage
6%
accounts to target in MFA spray attacks. On the flip side, they lockouts, limit login attempts, and generally lock down their login
12%
Non-Profit
are likely to have “messy” MFA environments, which create ripe portals aggressively.
conditions for device compromise attacks. This includes things Other
Additionally, AitM attacks are prevalent in this space, where
7%
like shared terminals on factory floors, OT devices accessing
attackers build fake university login spaces to steal users’
IT resources, kiosk machines, contractor devices with unknown
DEVICE COMPROMISE
credentials. Kits with custom software to enable these
hygiene, and tablets and mobile devices used for scanning
ATTACKS
operations are in high supply, making it easy for attackers to 8% 12%
and logistics. These factors create a much more varied device
automate such operations.
ecosystem that attracts device compromise attacks. In summary,
8%
11%

Attacks against MFA
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 25
5202
WEIVER
NI
RAEY
MFA attack style provides varying benefits for threat actors
MFA spray attacks MFA device compromise attacks
Consistent password patterns BYOD and unmanaged devices
• •
Conditions
Large networks where spray attacks are scalable Frequent session-based authentication
• •
for successful
Predictable login behavior High phishing exposure
• •
attacks
Credential reuse Device diversity
• •
Thrives
Thrives
where IAM
where devices
is unified,
and MFA use is
predictable,
more varied
and scaled
Strong IAM maturity Managed, hardened devices
• •
Conditions for
Strong lockout policies Phishing-resistant MFA
• •
unsuccessful
Conditional access Strong session controls
• •
attacks
Good password hygiene Strict MFA enrollment governance
• •

22002255
YYEEAARR IINN RREEVVIIEEWW
SEmtaateil- tshpreoantssored threats
2266

5202
WEIVER NI RAEY
Email threats
|     |     |     |     |         | save | code | dementia |        |
| --- | --- | --- | --- | ------- | ---- | ---- | -------- | ------ |
|     |     |     |     | meeting |      |      |          | domain |
thousands of key terms in blocked email subject
Phishing trends
|     |     | lines. According to our findings, 60% of the top 20  |     | cloudfront |     |     |     | payment |
| --- | --- | ---------------------------------------------------- | --- | ---------- | --- | --- | --- | ------- |
In 2025, there was a significant
In 2025, attackers continued to rely heavily on  terms appearing in phishing subject lines were the
|     |     |     |     | airline |     |     |     | tampering |
| --- | --- | --- | --- | ------- | --- | --- | --- | --------- |
phishing for initial access, which we observed in  same in 2024 and 2025, such as “request,” “invoice,”
increase in travel and itinerary
|     |     |     |     | invoice |     |     |     | medical |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------- |
40% of Talos IR cases. Adversaries  “payment,” “email,” “fwd,” “message,” “report,”
|     | themes, suggesting that attackers  |     |     | error |     |     |     | request |
| --- | ---------------------------------- | --- | --- | ----- | --- | --- | --- | ------- |
also leveraged phishing techniques once they  and “meeting.” This indicates that threats remain
were inside victim networks, as we saw a rise in  heavily focused on hijacking everyday work email  itinerary server
are exploiting corporate travel
post-compromise internal phishing incidents as well.  contexts like finance, approvals, and routine daily
troubleshoot Trump
and expense workflows, likely
Most of these cases involved threat actors using valid  tasks. To achieve this, they pretend to send invoices
election fwd
accounts to gain access, likely via stolen credentials  and payment instructions, requests and approvals,
to steal credentials, payment
message pain
and/or username/password combinations bought on  shared documents and reports, and meeting and
information, or MFA tokens via
the dark web. Similarly to 2024, attackers continue to  account notices. limited router
prioritize easy access and exploit victims’ identities.
|     | fake SSO pages. |     |     | configuration |     |     |     | advertisement |
| --- | --------------- | --- | --- | ------------- | --- | --- | --- | ------------- |
Travel and logistics lures surged
In terms of the types of phishing lures Talos saw in our  special Kamala email
| 2025 telemetry, malicious email subject lines looked less  |     | While the bulk of phishing themes remained  |     |     |        |         |       |     |
| ---------------------------------------------------------- | --- | ------------------------------------------- | --- | --- | ------ | ------- | ----- | --- |
|                                                            |     |                                             |     |     | report | airport | token |     |
like generic spam and much more like everyday  constant, Talos observed a notable shift at the next
where initial access was achieved via phishing. Using  boarding Biden
business, IT, and travel workflows that executives and  tier of lures. In 2025, there was a significant increase
a legitimate trusted account affords an
| employees routinely interact with. While core phishing  |     | in travel and itinerary themes, suggesting that  |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
attacker numerous advantages, such as potentially
lures stayed largely constant compared to 2024 —  attackers are exploiting corporate travel and expense
bypassing an organization’s security controls and
| with attackers continuing to lean heavily on invoices,  |     | workflows, likely to steal credentials, payment  |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
surprise and reminds us that attackers remain aware
appearing more trustworthy to the recipient.
payments, shared documents, and meeting notices —  information, or MFA tokens via fake SSO pages. For
of news cycles and global events. We also saw a
| the second tier of lures was marked by a rise in travel- | While actors relied on phishing for initial access,  | example, we saw the terms “airport,” “airline,”  |     |     |     |     |     |     |
| -------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
drop in clickbait-style promotional language, such as
related terms and technical language. These themes  they also incorporated it into their operations   “itinerary,” and “boarding” increase in prevalence
“advertisement,” “special,” “limited,” and “save,” as
were likely targeted at employees involved in corporate  post-compromise. In 2025, 35% of Talos IR phishing  from 2024 to 2025, and “booking” was a new term
well as health-related themes, such as “pain,”
travel and IT work, respectively. cases involved internal phishing, meaning that  that emerged in the 2025 dataset. This suggests
“medical,” “dementia,” and others.
|     | actors used phishing emails from compromised  | that threat actors relied on common corporate travel  |     |     |     |     |     |     |
| --- | --------------------------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Phishing plays key role in initial access  While certain lure topics declined from 2024 to
|     | accounts to execute additional stages of their attack  | communications to dupe targets into opening their  |     |     |     |     |     |     |
| --- | ------------------------------------------------------ | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
2025, Talos saw new themes emerge. One of the
| and post-compromise activity | chain once they were inside the victim’s endpoint  | malicious emails. |     |     |     |     |     |     |
| ---------------------------- | -------------------------------------------------- | ----------------- | --- | --- | --- | --- | --- | --- |
more dramatic shifts was the notable increase
or network. These operations facilitated a variety
In 2025, attackers compromised victims via
in technical terms like “tampering,” “error,” “code,”
|     | of additional malicious activity, including credential  | Political lures dropped off while IT  |     |     |     |     |     |     |
| --- | ------------------------------------------------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
phishing emails in 40% of Talos IR cases, highlighting
“domain,” “configuration,” “troubleshoot,” “router,”
|     | theft, cloning of MFA session tokens, and malware  | themes became more prominent |     |     |     |     |     |     |
| --- | -------------------------------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
the continued success of easy, low-cost social
“server,” “token,” and “cloudfront.” IT administrators,
deployment.
engineering operations. In these cases, we
|     |     | Some of the most prolific lures from 2024  | developers, and power users are primed to  |     |     |     |     |     |
| --- | --- | ------------------------------------------ | ------------------------------------------ | --- | --- | --- | --- | --- |
commonly observed phishing emails originating from
|     |     | — including those focused on consumers,  | respond quickly to these types of prompts. Based  |     |     |     |     |     |
| --- | --- | ---------------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
BEC-style and workflow-based
other internal users or external business partners
|     |     | health, and politics — declined sharply in 2025  | on these findings, the 2025 phishing ecosystem  |     |     |     |     |     |
| --- | --- | ------------------------------------------------ | ----------------------------------------------- | --- | --- | --- | --- | --- |
lures remain the primary theme
as actors leveraged compromised accounts to
|     |     | while phishing emails with IT themes grew. The  | played directly into IT operations and security  |     |     |     |     |     |
| --- | --- | ----------------------------------------------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
exploit established relationships. In Q2 2025, for
|     | Most of the phishing ecosystem did not change  | decline of political lures, such as “Trump,” “Biden,”  | workflows, with more messages looking like  |     |     |     |     |     |
| --- | ---------------------------------------------- | ------------------------------------------------------ | ------------------------------------------- | --- | --- | --- | --- | --- |
instance, this occurred in a staggering 75% of cases
|     | between 2024 and 2025, based on our analysis of  | “Kamala,” and “election” from 2024 to 2025 is no  | infrastructure alerts and delivery errors. |     |     |     |     |     |
| --- | ------------------------------------------------ | ------------------------------------------------- | ------------------------------------------ | --- | --- | --- | --- | --- |
© 2026 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com page 27

Email threats
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 28
5202
WEIVER
NI
RAEY
Figure 16 Featured threat Figure 17 What is the potential impact for
Direct Send attack process Direct Send attacks in 2025 executives and companies?
Microsoft 365 Direct Send
Emails that appear to come from internal
attacks surged as attackers
senders are more likely to be perceived
LEGITIMATE DEVICE spoofed users without ever
as legitimate, and attackers are exploiting
Sends internal email
compromising accounts that trust. The types of lures used in the Direct
Send-style attacks were highly targeted and
In 2025, threat actors again showed us how
enticing, often referencing bonus payouts,
commonly used systems and services can
compensation and salary information, meeting
be exploited with little effort and minimal skill
ATTACKER ACCESS
recordings, and even voicemail memos. By
to carry out impactful campaigns against
Exploits Direct Send
contrast, the most prevalent lures in generic
unsuspecting victims. In mid-2025, we saw
phishing emails were much more overtly
a surge in actors exploiting the Direct Send
clickbait and less crafty that featured time-
feature in Microsoft 365, allowing them to
sensitive requests in all-caps (see next page).
spoof internal email addresses and deliver
SPOOFED EMAIL
convincing messages — often with links, QR Once an executive is compromised, the
Uses your domain
codes, or attachments — without compromising attacker has a high-value pivot point: They can
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
any real accounts. Here’s how the attacks play impersonate the individual, initiate BEC, order
out in practice, why executives and Fortune payments, manipulate personnel decisions,
500 organizations are at risk, and how this can or access highly sensitive data. Moreover, the
escalate into high-impact damage. kind of social engineering used in these attacks
BYPASSES CHECKS applications — send emails to users in that issue. That changed in 2025, when Talos and
often involves leadership-style lures (e.g., wire
No auth alerts organization without needing to authenticate. In other security researchers observed large-
What is Direct Send and what are transfers, urgent approvals, missed voicemails/
practice, a device can route messages to users scale phishing campaigns abusing the
the risks? faxes, etc.), which specifically target senior roles.
that appear to come from the organization’s feature. The sharp rise in Direct Send abuse
Imagine you use your office printer to scan own domain, and they can do so without in mid- 2025 appears to be the result of several Another important takeaway is that Direct
an image and send it to yourself. Back at your logging in as a user. Because the traffic is factors (see Figure 17). First, more organizations Send is functioning as originally designed,
EMPLOYEE INBOX
desk, you open Microsoft Outlook and see technically delivered through Microsoft’s have moved to Microsoft 365, creating a larger meaning that threat actors are not exploiting
Trusted message
the scanned document in your inbox. The “to” infrastructure and not from an external SMTP attack surface and more devices legitimately any bugs or vulnerabilities. This is a reminder
and “from” fields are the same (since you, server, some of the usual authentication configured to use Direct Send. Second, many for organizations to be mindful of adversaries’
the employee, sent this to yourself) and the checks applied to outside mail (like SPF, DKIM, email security tools are configured primarily reliance on TTPs that are not inherently
message properly has the attached document or DMARC) may not fire in the same way, to inspect external email, and this kind of malicious, including living-off-the-land binaries
MALICIOUS
you just scanned. This is the very scenario giving the email a level of implicit trust. relay-based spoofing, which bypasses normal (LOLBins) and open-source and dual-use
PAYLOAD
threat actors are exploiting. authentication checks, allows attackers to quietly tools. Blocking external IPs from using the
Phish/malware Why are actors exploiting it now? compromise victims without triggering alerts. feature, enabling Microsoft’s newer “Reject
The Direct Send feature in Microsoft
Lastly, we know that threat actors are always Direct Send” control, tightening SPF/DMARC
Exchange Online (part of Microsoft 365) lets The vulnerability in Direct Send has been known
looking for reliable, low-effort delivery paths, enforcement, and treating “internal-looking”
systems connected to the internal network for years, but, until recently, it was mostly treated
which likely led to a surge in copycat activity. emails with the same scrutiny as inbound mail
— such as printers, scanners, and business as a design trade-off rather than a security
are currently the most effective defenses.
emulov
kcattA

Email threats
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 29
5202
WEIVER
NI
RAEY
Direct Send lures highly targeted compared to generic phishing themes
ecnelaverP
Email subject theme
[Company name] bonus disbursement timeline
RingCentral voicemail message transcript
Salary details
Important task reminder: Your to-do list is waiting
Immediate release of your funds
Attn: your grant fund worth $8,500,000
Cloud recording - [Meeting name] is now available
Your to do list
Paycheck reminder [date]
ecnelaverP
Ranked from most to least prevalent
Targeted Direct Send attack lures Generic phishing/spam lures
Email subject theme
You have a new task FLEXIBLE REMOTE PART-TIME JOB
ALERT ALERT ALERT!!!
APPLY NOW
Important Notice: Account Termination
OFFICE 365 ACCOUNT DEACTIVATION NOTICE!!
Important information about your funds
Notification of Stipend
To do list - [specific date] Notice of Amendment
ACH REFUND; DISBURSEMENT PENDING
Update Information 2025
Student Authentication Needed 2025

2025
YEAR IN REVIEW
State-sponsored threats
30

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 31
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
China 2025 via their ability to conduct long-
74%
term stealthy operations and continually
In recent years, some of the
outmaneuver security professionals
most persistent and sophisticated cyber
through their use of sophisticated TTPs.
threats have emanated from China. 2025
was no different, with a variety of new China-nexus groups
and known China-nexus actors carrying leveraged known and unknown increase in China-related
out increasingly efficient and stealthy
vulnerabilities at rapid pace to
investigations from 2024 to 2025
operations against U.S. and global
compromise networks globally
targets. The number of investigations
Talos conducted into China- In 2025, Talos observed a significant
nexus campaigns increased nearly number of high-impact operations
75% this year compared to 2024. carried out by a range of actors
This reflects the U.S. government’s in this space, including Chinese-
2025 assessment that China’s cyber speaking actors and threat clusters
capabilities are growing both in breadth linked to APTs publicly attributed
and depth. Chinese threat actors’ to China by the U.S. government.
weaponization of both newly disclosed This activity leveraged both known (n-day)
and long-standing vulnerabilities allowed and unknown (zero-day) vulnerabilities, ToolShell: Rapid zero-day weaponization in action
them to carry out high-impact, targeted underscoring the operational
operations as well as broad-scale sophistication and global scale of these
As detailed earlier in this report, starting in mid-July 2025, threat traditional espionage targets, with a focus on U.S. local and federal
exploitation campaigns, rendering almost actors. Numerous groups weaponized
actors began actively exploiting two path traversal vulnerabilities governments and foreign ministries.
all networks at risk. At the same time, zero-days before or immediately following
affecting on-premises SharePoint servers, dubbed ToolShell.
activity from Chinese cybercriminal disclosure, while others were constantly These attacks began instantaneously after public disclosure, in
groups, which have historically scanning for and exploiting long-standing Analysis of the initial wave of exploitation activity revealed TTPs the narrow window before emergency patches were available,
featured less prominently in public weaknesses in networking equipment and indicators of compromise consistent with China-nexus actors, demonstrating how these actors value speedy action that can
reporting, became increasingly visible or widely used software (see page before broader opportunistic use by a wide range of threat groups improve their chances of maintaining access beyond the zero-day
this year, adding new unpredictability 32). Both insecure, legacy networks as began. We saw actors leverage tools commonly associated with vulnerability’s lifetime.
to an already complex threat well as well-defended ones are at risk China, such as ChinaChopper, post-compromise and largely target
landscape. Ultimately, Chinese threat with these techniques, leaving seemingly
actors were a formidable threat in every organization vulnerable.

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 32
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
China-nexus actors capitalizing on zero-days and n-days in 2025
Who are they? How do they operate? Who do they target?
Targets a zero-day vulnerability for initial access, executes system-level A limited number of organizations
UAT-9686: A Chinese-nexus APT actor whose tool
commands, and deploys AquaShell (a custom, persistent Python-based operating appliances that run software for
use and infrastructure are consistent with other
backdoor), AquaTunnel (a reverse SSH tunnel), chisel (another tunneling tool), Cisco Secure Email Gateway and Secure
Chinese threat groups such as APT41 and UNC5174
and AquaPurge (a log-clearing utility) for persistence. Email and Web Manager
Zero-days
Exploits a zero-day for initial access, conducts reconnaissance, and rapidly
UAT-6382: A Chinese-speaking threat actor known
deploys web shells, such as AntSword and chinatso, followed by Cobalt
Local U.S. government networks
to use tools typically deployed by Chinese APTs
Strike and VShell malware for long-term access.
Leverages n-days in exposed web and application servers for
initial access and uses a combination of web shells and open
UAT-5918: An APT with TTPs and victimology that Critical infrastructure, IT,
source tooling, including FRPC, FScan, In-Swor, Earthworm, and Neo-
overlap with Chinese APTs such as Volt Typhoon telecommunications, education, and health
reGeorg, to establish persistence. Conducts information theft and credential
and Earth Estries care in the U.S. and Asia
harvesting by dumping registry hives and using tools like Mimikatz.
Uses known vulnerabilities in internet-exposed servers to gain initial
access and establishes persistent access via SoftEther VPN and
UAT-7237: A Chinese-speaking APT that is likely RDP. Harvests credentials with tools like Mimikatz, moves laterally
N-days IT entities in Taiwan
a subgroup of UAT-5918 using LOLBins and network scanners, and deploys custom malware loaders
to maintain long-term access.
UAT-8607: A threat actor who we assess with
Leverages known vulnerabilities on vulnerable web servers for initial access,
medium confidence is China-nexus, based on
then deploys both custom malware and publicly available dual-use tools such
IT entities in Europe
overlap in TTPs and IOCs with a known Chinese
as ADExplorer and V2Ray to establish long-term persistence.
APT group

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 33
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
Increased number of Chinese
cybercriminal operations highlights
Threat actor
emphasis on financial motivation
spotlight:
We came across more campaigns in
UAT-8099
2025 than in previous years in which
Chinese-speaking actors conducted AQUATIC PANDA CYBER THREAT ACTORS
financially motivated criminal operations outside
Conspiracy to Commit Computer Fraud; Conspiracy to Commit Wire Fraud
of traditional espionage-motivated activity.
These campaigns leveraged similar tooling
Initial access
and infrastructure as state-linked operations,
Exploits vulnerability in high-value IIS server
complicating attribution and tracking efforts. It
is likely that in some cases, state-sponsored
Discovery
actors conducted operations for personal
Uploads web shell to server and leverages it to collect
profit alongside espionage-focused missions,
system and network information
while in others, cybercriminals collected valuable
information during an attack that could be
Wu Haibo Chen Cheng Liang Guodong Ma Li Wang Yan
Privilege escalation
sold to espionage-motivated actors for further
Enables a guest account, sets a password, elevates user exploitation, providing them dual revenue streams.
privileges to administrator level, and enables RDP
The attack chain (see sidebar at left) highlights
UAT-8099, a threat group that falls into the latter
Persistence
category, as the actors conducted search engine
Creates a hidden account and sets administrator level
optimization (SEO) poisoning for financial gain
privileges for long-term persistence
while also collecting valuable information that
could be used as a key into the network by a
Execution
Wang Zhe Zhou Weiwei Xu Liang Wang Liyu Sheng Jing
state-affiliated group. This group predominately
[MPS] [MPS]
Deploys custom BadIIS malware to facilitate SEO poisoning
targets Internet Information Services (IIS) servers, CAUTION
FBI poster on 10 most wanted Aquatic Panda threat actors
and installs Windows IIS security tool to protect configuration
highly attractive targets for espionage operations
From at least in or around 2016, through in or around 2023, the Chinese technology company Anxun (i-Soon)
Information Technology Co., Ltd., aka “i-Soon” (“i-Soon”), and its personnel, allegedly engaged in numerous and
as they can be leveraged for initial access to
widespread compromises of email accounts, cell phones, servers, and websites at the direction of, and in close
Exfiltration
a target’s internal network and stealthy C2 coordination with, the People’s Republic of China’s (PRC) MSS and MPS. Incorporated in or around 2010, in Shanghai,
dCohcinuam, i-eSnotosn, a allesg ewdley llp raosfit eind faonrdm garetwio ans ain k ey player in the PRC’s hawckitehr-ofour-th sirpe eeccoisfiycst edmir.e Act tcievretasin a tnimde st,h en sold the
Uses open-source and native tooling to exfiltrate data such as
communications. i-Soon had three (3) teams of employees allegedly working to attack computer systems. i-Soon employees allegedly
logs, credentials, configuration files, and sensitive certificates thcoem ipnrdomicitsmede anndt, artetevmepateled dto vciocmtpimrosm iisnec vliuctdimesd a cross the globe, inicnlutdeilnlgig ae lnarcgee rteoli gtihoues gorogavneizrantmione inn t, allegedly
the United States, critics and dissidents of the PRC government, a state legislative body, United States government
A March 2025 indictment provided another dissidents of the Chinese government, news charging between $10,000 – $75,000 for each
agencies, the ministries of foreign affairs of multiple governments in Asia, and news organizations.
Defense evasion example of Chinese cybercriminals in oIuft yleotus h, aavned a nUy. Sin.f ogromvaetironnm coenncte ranginegn tchiiess c.a se, please contactc yoomur plorcoaml FisBeI dof fiecme,a tihl ea ncecaoruesntt . Looking forward,
American Embassy or Consulate, or you can submit a tip online at tips.fbi.gov.
action, with the U.S. government charging In some instances, the indictment alleges it is likely the number of Chinese cybercriminal
BadIIS variant retrieves malicious code from C2 server
Field Office: New York
employees of Chinese technology the actors carried out the attacks at the operations will continue to grow, as it offers
instead of having it embedded to evade antivirus solutions www.fbi.gov
firm i-Soon for their roles in extensive computer direct request of the Chinese government. actors the opportunity to generate personal
intrusion campaigns against organizations In other instances, the same threat actors funds while simultaneously supporting state-
globally. Talos’ analysis of leaked i-Soon allegedly compromised victim organizations sponsored espionage.

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 34
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
Russia
Russian cyber activity in 2025 remained persistent and strategically
aligned with broader intelligence and military objectives. Russian
APTs exploited unpatched, years-old vulnerabilities — frequently those
affecting networking devices — to facilitate espionage and long-
term access to victims globally. Meanwhile, both destructive
and espionage-motivated cyber attacks targeting Ukraine
and its supporters also continued unabated, likely aimed at
complementing military efforts and combating international pressure
caused by sanctions. Russian cyber actors continue to maintain a
high operational tempo and execute impactful campaigns against Threat actor spotlight:
adversaries globally, underscoring the critical role of cyber
Static Tundra
capabilities in supporting Russia’s geopolitical goals.
Russian APTs continued to find success in
exploiting unpatched, older vulnerabilities,
Static Tundra specializes in network device exploitation to support long-
particularly in networking devices
term intrusion campaigns into organizations that are of strategic interest
SYNful knock
Russian APTs carried out widespread attacks against global
to the Russian government. It is likely a sub-cluster of another group —
targets in 2025 by leveraging known vulnerabilities, often in
We assess with moderate confidence Static
Berserk Bear, which the FBI attributes to the Federal Security Service’s
unpatched networking devices, to support long-term intelligence
Tundra is associated with historic use of
gathering. This tactic underscores how poor patch hygiene or use (FSB) Center 16 — based on an overlap in TTPs and victimology. SYNful knock, a malicious implant installed on
of EOL, vulnerable equipment remains a significant security risk,
compromised Cisco devices that was publicly
enabling actors to covertly compromise organizations at scale even
We identified Static Tundra targeting at least two older vulnerabilities this year: reported in 2015.
without novel exploits.
This persistent malware demonstrates the
For example, this year, APT28 — attributed to Russia’s General
CVE-2023-20198 CVE-2018-0171 group’s advanced knowledge of networking
Staff Main Intelligence Directorate (GRU) — leveraged a WinRAR
devices, as it allows the attacker to gain control
This vulnerability affects the Web User Interface Static Tundra also leveraged this seven-year-
vulnerability for which the patch was released two years ago
of the targeted device and compromise its
feature of Cisco IOS XE software when exposed old critical remote code execution vulnerability
(CVE-2023-38831) to gain initial access to Western logistics entities
integrity with a modified Cisco IOS software
to the internet or untrusted networks. this year in Cisco IOS and IOS XE software’s
and technology companies involved in the coordination, transport,
image. It contains different modules enabled
Smart Install feature.
and delivery of foreign assistance to Ukraine. During the course
Static Tundra exploited this flaw in highly via the HTTP protocol, triggered by crafted TCP
of the attacks, the actors were able to conduct follow-on targeting
targeted operations in 2025, focusing on They primarily targeted the telecommunications, packets sent to the device.
by exploiting trust relationships of compromised organizations
the technology and telecommunications higher education and manufacturing sectors
to extend their access to additional entities, rendering this a
sectors in the U.S. globally, selecting victims of strategic interest to
significant and impactful campaign. We also saw Russian APT
the Russian government.
Static Tundra relying on exploitation of known vulnerabilities in 2025
to facilitate targeted espionage-motivated operations against key
sectors of interest (see sidebar).

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 35
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
Russian cyber activity infrastructure. Pending any significant
targeting Ukraine and resolutions or disruptions to the
conflict, Ukrainian organizations, their
its supporters remains
service providers, and any third-
persistent, reflecting Russia’s
party entities that support Ukrainian
broader war effort
networks remain at risk from ongoing
Russian state-sponsored Russian espionage and disruptive
actors steadily continued their operations.
espionage operations against
Russia’s offensive cyber activity is
Ukraine’s government, military, and
highly correlated with developments
critical infrastructure this year and
in the larger geopolitical sphere.
showed ongoing interest in targeting
For example, the announcement of
countries supporting Ukraine. Talos
sanctions intended to apply pressure
also observed persistent destructive
on Russia by both the U.S. and E.U.
attacks, reflecting a campaign
often corresponded with our observed
that incorporates intelligence
levels of Russian cyber activity (see
gathering and sabotage operations
Figure 18). U.S. and E.U. sanctions
to sustain strategic pressure. Pro-
against Russia spiked in May,
Russia hacktivist groups continued
October, and December, according to
to carry out opportunistic, less
the Council of the European Union and
sophisticated attacks against
public sources, and May’s spike in
operational technology and critical
particular coincided with a fourfold
infrastructure, exploiting exposed
increase in our observed Russia cyber
services and weak credentials to
activity, according to data collected
cause disruptions and garner attention.
from our active investigations and
The consistency we see in incoming intelligence reports.
Russian cyber activity targeting This pattern indicates that significant
Ukraine mirrors what is geopolitical developments, such as
being observed kinetically on the sanctions announcements, can serve
battlefield, where there is a near as indicators for heightened cyber
deadlock with neither side achieving risk and thus help inform defensive
major breakthroughs. Despite planning and increased vigilance for
diplomatic efforts for a resolution, the organizations that are frequent targets
war continues with ongoing military of malicious Russian activity.
operations and significant damage to
emulov
noitcnas
dna
ytivitcA
Figure 18
Sanctions and levels of Russian cyber activity in 2025
KEY Observed Russian cyber activity U.S. and E.U. sanctions
Jan Feb Mar Apr May Jun Jul Aug Sept Oct Nov Dec

4202 5202
WEIVER NI RAEY WEIVER NI RAEY
State-sponsored threats
Three malware families make up the bulk of the commodity
malware threats observed against Ukraine
Russian state-sponsored and cybercriminal adversaries primarily relied on DarkCrystal
RAT (DCRAT), Remcos RAT, and Smoke Loader in their operations against Ukraine in
2025, according to Talos investigations and our analysis of industry reporting. Although
these malware families are not exclusive to Russia-nexus threat actors, they are
repeatedly observed in attack chains and toolkits associated with them and should
therefore be high-priority targets for defense and monitoring.
| Remcos RAT                         | Smoke Loader                       | DCRAT                          |
| ---------------------------------- | ---------------------------------- | ------------------------------ |
| Remcos is a commercially           | Smoke Loader is a modular          | DCRAT is a modular trojan has  |
| available, sophisticated RAT that  | loader that was first seen in the  | been available on underground  |
| was first seen in 2016.            | wild in 2011 and is available as   | forums as a MaaS since 2018.   |
Smoke Loader in disguise
a malware-as-a-service (MaaS),
| While it is marketed as a remote  |     | Russian threat groups often  |
| --------------------------------- | --- | ---------------------------- |
though sale has reportedly been  In a campaign that began in February 2025 and targeted Ukrainian entities, we observed
| administration tool, Russian threat  |     | deliver DCRAT via phishing  |
| ------------------------------------ | --- | --------------------------- |
limited to Russia-nexus actors in  threat actors using phishing emails to deliver a CharCode-obfuscated JavaScript downloader,
| actors have abused it to conduct  |     | emails and leverage it for  |
| --------------------------------- | --- | --------------------------- |
recent years.   which we assess is a variant of the Emmenhtal malware loader.
| extensive system reconnaissance,  |     | credential theft, reconnaissance,  |
| --------------------------------- | --- | ---------------------------------- |
credential harvesting, lateral  It primarily delivers secondary  data exfiltration, and persistent  The downloader used several layers of obfuscation to disguise an encrypted PowerShell
movement, and long-term  payloads, including RATs,  access. command that ultimately downloaded Smoke Loader and a decoy PDF from a rotating set
monitoring. It is also commonly  stealers, and ransomware. of infrastructure, demonstrating how this malware can be heavily disguised upon delivery
distributed via phishing emails. and potentially evade detection.
© 2026 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com page 36

4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
North Korea North Korean cyber actors pulled Contagious Interview tool improvements in 2025
off the largest cryptocurrency
North Korean cyber operators increased the sophistication
and impact of their social engineering schemes in 2025, heist in history in 2025, stealing
leveraging these operations to achieve financial gain as well Clipboard and file stealing capabilities
as persistent network access for espionage purposes. These
$1.5B
actors orchestrated record-high cryptocurrency thefts over the
year, notably pulling off one of the largest heists ever recorded
in February by stealing $1.5 billion from the Bybit exchange. Keylogger and screenshotting modules
While the illicit revenue can be leveraged by North Korea to
counteract the effects of intensifying international sanctions, the
unauthorized persistent access to targeted networks affords in Ethereum. Python-based custom RAT to enable
numerous opportunities such as theft of sensitive data, extortion,
targeting of Windows systems
and footholds for future operations.
Talos actively tracked numerous North Korea-affiliated
campaigns, finding enhanced tooling, technical sophistication,
Virtual environment checking capabilities
and operational security. We also strengthened our identification
and tracking of patterns used to create false personas deployed
malicious npm packages disguised as technical tests, which
in the North Korean IT worker scheme, improving our capability to
install cross-platform malware targeting Windows, macOS,
detect these actors at scale.
Anti-debugging and anti-logging functionality
and Linux systems. The actors’ BeaverTail infostealer malware
North Korean group Famous Chollima improves immediately exfiltrates cryptocurrency wallet credentials from
browser extensions, browser-stored passwords, SSH keys,
tooling and intensifies the scale of their
and macOS Keychain data to attacker-controlled infrastructure.
Contagious Interview campaign
Meanwhile, their InvisibleFerret backdoor establishes
Contagious Interview at-a-glance
Throughout 2025, Talos observed North Korean threat actor persistent access for long-term espionage, enabling attackers
Famous Chollima improving the capabilities of their Contagious to compromise personal accounts, corporate wallets, and
338+ 50k+ 180+
Interview campaign, which leverages fake job recruitment entire DeFi protocol infrastructures by exploiting discovered
schemes to socially engineer targets, conduct cryptocurrency private keys.
theft, and obtain persistent access to targeted networks. The
malicious npm downloads personas
The attackers reap financial rewards by draining protocol
campaign is so named due to its contagious nature, where
funds, upgrading contracts maliciously, and/or minting infinite packages
any user cloning infected repositories becomes compromised,
cryptocurrency tokens. Meanwhile, their persistent access
enabling exponential spread.
to targeted networks can support long-term espionage and
Famous Chollima impersonates recruiters from legitimate intelligence collection efforts, rendering this a dual-purpose
companies on LinkedIn, Telegram, and other job platforms, operation. Periodic improvements made to this campaign
Dozens Hundreds
offering high-paying cryptocurrency positions and directing throughout 2025 indicate it will be a persistent threat going
victims to fake interview platforms or coding assessments. into 2026.
Victims are tricked into executing terminal commands or running
of C2 endpoints of confirmed victims
© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 37

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 38
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
Refined tracking of patterns used to create Talos’ analysis of a data leak from an AI photo editing platform
North Korean IT worker personas enables led us to identify numerous IT workers’ fake profiles, which
in turn revealed patterns that can be leveraged to enumerate
Defending against North Korean identification of these actors at scale
additional accounts and aliases. For example, many of the
social engineering schemes
North Korean operatives continued over the past year to deploy actors’ emails we track end in numerical digits and contain
thousands of skilled IT workers who use stolen identities and words like “code” and “dev,” names of animals, or gods from
AI-generated profiles to secure positions at Fortune 500 Greek mythology. Parsing out usernames from these email
Enhanced hiring verification
companies, startups, and government contractors. Beyond addresses, identifying profiles with those usernames on
Organizations must implement multi-layered identity verification including generating billions in annual revenue for North Korea’s nuclear various online platforms, and pivoting off these accounts often
mandatory live video interviews with spontaneous questions, government weapons and ballistic missile programs, these IT workers reveals a web of interconnected IT worker profiles that follow
ID verification with liveness detection, background checks through multiple establish persistent insider access to corporate networks, steal the same patterns. Tracking these patterns and accounts can
independent sources, and verification of physical addresses matching intellectual property, deploy malware, conduct extortion, and improve organizations’ ability to defend against this threat,
identification documents. enable future cyber operations. along with additional security steps outlined below.
Figure 19
North Korean IT worker accounts connected by username
Technical controls and monitoring
Upon searching for our identified North Korean IT worker usernames across various online platforms,
Deploy endpoint detection and response (EDR) solutions with
we found which ones are more favored by these actors.
behavioral analytics to detect unauthorized remote access tools,
KVM-over-IP devices, and suspicious USB/HDMI configurations.
Number of worker accounts connected by usernames
Monitor for anomalous patterns including VPN usage from
sanctioned regions (particularly Astrill VPN), connections to Russian
(AS20485 TTK) and Chinese (AS134544 Cenbong) networks,
unusual working hours inconsistent with stated time zones, and
multiple concurrent logins from different geographic locations.
Cross-functional coordination
Establish dedicated insider risk programs spanning HR, Legal, Security, and IT
departments with specialized training on DPRK IT worker tradecraft. Create safe
reporting channels for suspicious behavior, implement regular red-team exercises
simulating fraudulent applications, and participate in information-sharing forums
with law enforcement and industry peers

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 39
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
Iran* actors’ noisy self-promotion — highlights Activity from the top it decodes the data from the request to Hacktivism during global conflict
the strategic utility of hacktivism as a obtain and execute the final shellcode.
Iranian hacktivist groups
Iranian threat actors maintained a low-cost means of garnering attention The threat actor then establishes
Trends from the Israel-Hamas and Russia-Ukraine conflicts:
robust operational tempo in 2025, and promoting narratives during periods we track increased persistence by abusing legitimate
continuing to leverage a variety of of conflict. Windows Management Instrumentation
techniques and tools such as credential (WMI) filters to trigger the execution of
60%
Kinetic and geopolitical events act as
harvesting, custom backdoors, ShroudedSnooper’s malicious JavaScript code.
catalysts for surges in activity
LOLBins, and wiper malware to cause telecommunications campaign
The development and use of the
operational disruption at targeted
underscores focus on stealthy
updated tool in this campaign is
entities globally. The year also
and persistent access
just one example of Iranian APTs’
featured toolkit updates from Iranian in 2025, according
overall focus on establishing stealthy
state-sponsored groups, such as In 2025, Talos started tracking a DDoS attacks play a major role,
to analysis of posts made
and persistent access to targeted
ShroudedSnooper, that highlighted ShroudedSnooper campaign targeting particularly against government,
organizations, particularly within the
actors’ focus on establishing and telecommunications providers in on the threat actors’ media, and public services targets
telecommunications sector. This is
maintaining long-term, highly evasive the Middle East that involved an
official accounts.
a top-targeted industry vertical for
access to critical sectors for espionage updated version of HTTPSnoop, a
APTs writ large, as they often form the
operations. custom compact backdoor that we
Collectives draw actors from
backbone of national satellite, internet,
first discovered in 2023. We assess
regions beyond the areas
Iranian threat activity occurred against and telephone networks upon which
ShroudedSnooper — an APT that public
The backdoor operates by interfacing involved in the conflict
the backdrop of the Israel-Hamas most private and government services
reporting widely attributes to Iran’s
with Windows HTTP kernel drivers and
conflict, and several Iranian hacktivist rely. By establishing undetected,
Ministry of Intelligence and Security
devices to listen to incoming requests
groups — an increasingly active element persistent access, threat actors can
(MOIS) — is very likely an initial access
of the country’s threat operations — over HTTP(S) and executing that potentially collect valuable intelligence Activity is advertised via social
group that passes operations off to
conducted, or claimed to conduct, content on the infected endpoint. It from priority targets while also media with inflammatory language
secondary threat actors for long term
DDoS attacks, website defacements, monitors for very specific, pre-defined exploring lateral and downstream intended to sow divisions and
espionage or destructive attacks.
and an array of disruptive operations malicious web requests that the threat movement to customer and subsidiary promote prejudice
in support of national interests. While The updated variant of HTTPSnoop actors have started customizing for networks, supporting sustained
many of these attacks relied on that we saw in 2025 is far more adept the victim environment, crafting URL compromise at scale.
unsophisticated techniques, their public at blending into normal traffic that is patterns that blend in with expected Attacks impacting systems tied to
nature — often amplified through the specific to the victim environment. traffic. When it detects a matching URL, critical services or infrastructure
are rare and often unverified
Activity from Iran-aligned collectives nearly tripled in June compared to the month prior,
reflecting the link between kinetic conflict and hacktivist operations. *For current threat intelligence related to the developing
conflict in Iran, follow our coverage on the Talos blog.
This analysis is derived from our tracking of top Iran-aligned hacktivist groups and their posts to actor-controlled accounts.

© 2026 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 40
4202
WEIVER
NI
RAEY
State-sponsored threats
5202
WEIVER
NI
RAEY
Escalations in Israel-Hamas conflict triggered
surge in hacktivist activity, mirroring Russia-
Threat actor spotlight: Z-Pentest
Ukraine trends Typical attack chain
Hacktivism was a mercurial and highly visible component of
Z-Pentest (also known as Z-Alliance) is a pro-Russia hacktivist collective
the Iranian threat landscape in 2025, with activity levels rising
Reconnaissance
formed in late 2024 that publicly expressed pro-Iranian sympathies in 2025,
and falling in response to escalations in the Israel-Hamas
Scans for exposed OT systems
war. For example, Israel carried out strikes against key
demonstrating potential ideological overlap.
Iranian military and nuclear sites between June 13 – 20
and U.S. forces struck Iranian nuclear sites on June 21 The group has been associated with high-visibility OT intrusions targeting
and 22, resulting in significant damage in the region. In
critical infrastructure entities, a notable divergence from more traditional
the days leading up to and immediately following these
attacks, Talos observed a surge in hacktivist activity hacktivist attacks such as DDoS.
targeting Israel and its allies from established, new, and Resource Development
Looking ahead, this group’s purported capabilities, history of collaborating
previously dormant collectives that align themselves with the
Uses temporary VPS infrastructure
Iranian government. In response to the heightened threat
with other hacktivist groups, and public alignment with pro-Iran sentiments
environment immediately following the attacks, the U.S.
render it one to watch in this threat landscape.
Department of Homeland Security released an advisory,
underscoring the risks associated with pro-Iranian hacktivist
activity against U.S. networks.
The surge and characteristics of hacktivist activity
Initial Access
surrounding the Israel-Hamas conflict closely mirror dynamics
Exploits weak or default credentials
previously seen during the Russia-Ukraine war (see page 39).
Talos tracked numerous pro-Iran hacktivist collectives this
year, expanding our efforts as new groups emerged on the
scene. In looking at the volume of posts the collectives’
operators made throughout the year from their official
accounts on forums and websites such as X, Telegram, and
Impact
TOR data leak sites, we found that Mr Hamza, Keymous+,
and DieNet were amongst the most active overall in 2025, Defaces and/or manipulates OT systems,
despite DieNet only appearing on the scene in March. posting evidence on public channels
Another group, Z-Pentest — though predominately known
as a pro-Russia hacktivist actor — also garnered interest in
this threat space in 2025 due to their unique capabilities and
ideological overlap with Iranian interests (see sidebar).

2025
YEAR IN REVIEW
AI threat landscape
41

5202
WEIVER NI RAEY
AI threat landscape
Figure 20
The agentic shift
AI usage across the attack chain
Interested in learning more?
While this report is based on trends throughout
2025, one area we want to call attention to is
RECONNAISSANCE
just how fast the AI threat landscape is changing,
The state of AI security is as complex and dynamic
AI automates gathering intelligence on
even in the first few months of 2026. State of AI Security 2026
as AI technology itself. For more information on these
organizations, employees, and systems.
developments, including forward-looking research into
In 2025, Talos’ observations show that AI was
what changes may be on the horizon, we recommend
more commonly used to automate or augment
WEAPONIZATION
you read Cisco’s annual State of AI Security report. This
discrete parts of traditional attacks. This is
AI can be used to assist in the development
report provides a comprehensive analysis of the latest
especially true for social engineering. AI lowers
of new malware and disguise malicious tools.
developments across AI threat intelligence, global policy,
the barrier of entry for novice attackers to
standards, research, and more.
employ more convincing social engineering
| techniques, such as easily generating phishing  |     |     | DELIVERY |
| ----------------------------------------------- | --- | --- | -------- |
sites at the click of a button. At the same  AI generates highly convincing fake emails, messages,
Read here
time, it also raises the ceiling for the  and websites, providing obfuscated delivery mechanisms.
operations of more advanced actors, such as
APTs leveraging deepfake technology to secure
EXPLOITATION
employment at a target organization.
Threat actors could use AI to uncover vulnerabilities and code
However, as the recent research into VoidLink   flaws, leading to faster exploitation and increased risk.
|     | have happened in the span of months that  | modular frameworks like VoidLink, this would  |     |
| --- | ----------------------------------------- | --------------------------------------------- | --- |
has demonstrated, the AI landscape is evolving
|     | outpace the adaptive capabilities of organizers  | also give the user the ability to generate new  |     |
| --- | ------------------------------------------------ | ----------------------------------------------- | --- |
at an exponential pace. VoidLink is a first
|     | and defenders. With new applications being  | modules on the fly based on the needs in the  | INSTALLATION |
| --- | ------------------------------------------- | --------------------------------------------- | ------------ |
step in AI integration where development is
discovered and used every day, this trend shows  current environment, without having to devote  Malicious code can be hidden within AI-powered software
significantly sped up, allowing tasks that used
|     | no signs of slowing down. A good example  | the resources typically associated with it.  | components and plugins. |
| --- | ----------------------------------------- | -------------------------------------------- | ----------------------- |
to take months to be completed in weeks or
|     | of this is OpenClaw (formerly Clawdbot) and  | This capability likely already exists; we  |     |
| --- | -------------------------------------------- | ------------------------------------------ | --- |
even days. It’s an important first step, but as we
|     | Moltbook, which demonstrates how quickly  | just haven’t found it yet. |     |
| --- | ----------------------------------------- | -------------------------- | --- |
have seen repeatedly with AI, the progression
COMMAND AND CONTROL
technologies can evolve and become a
| will come quickly. |     | Beyond that, the technology is quickly moving  |     |
| ------------------ | --- | ---------------------------------------------- | --- |
AI translates human-like instructions within malware
serious business and cybersecurity risk for
towards autonomous agents that could be
into executable commands.
| In addition, the integration of agentic AI in  | organizations. |     |     |
| ---------------------------------------------- | -------------- | --- | --- |
tasked with basic, repeatable tasks like lateral
mobile devices has been faster than on classical
|     | It has become clear that, in the near future,  | movement, data gathering, and exfiltration,  |     |
| --- | ---------------------------------------------- | -------------------------------------------- | --- |
endpoints and servers. In these platforms the
ACTIONS ON OBJECTIVES
|     | back-end supported AI capabilities will become  | allowing the analyst to scale their operations  |     |
| --- | ----------------------------------------------- | ----------------------------------------------- | --- |
APIs are ready for adoption, which has led to the
AI can assist in the automation of data theft
|     | prevalent, similar to what we are already seeing  | or devote resources to more critical human- |     |
| --- | ------------------------------------------------- | ------------------------------------------- | --- |
appearance of the first AI-enabled malware. In
and the execution of the attack's final goal.
|     | in commercial products. These capabilities  | driven tasks. The speed of AI’s evolution makes  |     |
| --- | ------------------------------------------- | ------------------------------------------------ | --- |
these cases, agentic AI was used to evaluate the
|     | offer ways to make users more effective, giving  | it likely this reality will arrive sooner rather  |     |
| --- | ------------------------------------------------ | ------------------------------------------------- | --- |
screen content and determine next actions.
|     | them the ability to use an agent to search for  | than later. Agentic AI is opening the door to a  |     |
| --- | ----------------------------------------------- | ------------------------------------------------ | --- |
CLEANUP TRACKS
| Large language models (LLMs) provided the  | vulnerabilities in niche software found in a  | catalog of features that will automate manual  |     |
| ------------------------------------------ | --------------------------------------------- | ---------------------------------------------- | --- |
AI helps disguise malicious activity as normal traffic
| basis for generative AI (GenAI), which in turn  | compromised environment while they continue  | work and allow adversaries to greatly expand  |     |
| ----------------------------------------------- | -------------------------------------------- | --------------------------------------------- | --- |
to evade detection.
| enabled agentic AI, and leaps in technology  | to drive toward their mission objectives. In  | their capabilities. |     |
| -------------------------------------------- | --------------------------------------------- | ------------------- | --- |
© 2026 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com page 42

2025
About the Cisco Talos
2025 Year in Review
YEAR IN REVIEW
The Cisco Talos 2025 Year in Review is a deep
dive into the tactics, techniques, and procedures
that shaped adversary operations globally.
About Cisco Talos
Drawing from original Talos threat research; Cisco Talos is a global threat intelligence
team dedicated to tracking, analyzing,
large-scale Cisco security telemetry across
and disrupting cyber adversaries. We
endpoint, network, and email environments;
protect Cisco customers and support
and real-world investigations conducted by the broader security community through
continuous research and collaboration with
Cisco Talos Incident Response, the report
industry and government partners.
identifies the attack paths that consistently led
Our intelligence powers Cisco security
to compromise.
products through Talos Intelligence
Integrations, delivering automated protection
Talos created this report to provide defenders
against an ever-changing threat landscape.
with a clear view of how threat actors operated
Talos Threat Hunting and Incident Response
at scale in 2025 and what those trends services extend our expertise directly into
customer environments, helping organizations
mean for detection, hardening, and response
detect, respond to, and recover from
strategies moving forward.
advanced threats.
Stay connected
View our blog: TalosIntelligence.com/blog | Subscribe: Threat Source newsletter | Follow us: LinkedIn, X, Mastodon, and BlueSky
© 2026 Cisco and/or its affiliates. All rights reserved. Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates
in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned
©ar e2 0th2e6 pCroispceor tayn odf/ othr eitisr raeffislpiaetcetsiv. eA lol wrignhetrss .r Tesheer uvesed .o f| t htael owsoinrtde lpligaretnnceer .dcoomes not imply a partnership relationship between Cisco and any other company. (1110R) pppaaagggeee 444333

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
