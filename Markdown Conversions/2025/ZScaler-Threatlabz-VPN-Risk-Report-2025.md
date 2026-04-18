# Zscaler ThreatLabz 2025 VPN Risk Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [VPN Risks: Why 81% of Organizations Are Pivoting to Zero Trust by 2026](#vpn-risks-why-81-of-organizations-are-pivoting-to-zero-trust-by-2026)
- [VPN Security Concerns](#vpn-security-concerns)
- [Ransomware and VPNs: A Perfect Storm of Risk](#ransomware-and-vpns-a-perfect-storm-of-risk)
- [VPNs and Lateral Movement: Increasing the Blast Radius of Breaches](#vpns-and-lateral-movement-increasing-the-blast-radius-of-breaches)
- [VPN CVEs from 2020-2025: A Rising Wave of High-Severity Vulnerabilities](#vpn-cves-from-2020-2025-a-rising-wave-of-high-severity-vulnerabilities)
- [Key Trends: CVE Impact Types](#key-trends-cve-impact-types)
- [Key Trends: Critical VPN Vulnerabilities](#key-trends-critical-vpn-vulnerabilities)
- [The Challenges of Implementing Segmentation](#the-challenges-of-implementing-segmentation)
- [VPNs Increase M&A Cybersecurity Risks](#vpns-increase-ma-cybersecurity-risks)
- [Third-Party VPN Access: A Backdoor for Attackers](#third-party-vpn-access-a-backdoor-for-attackers)
- [Challenges and Gaps with Legacy Protective Measures](#challenges-and-gaps-with-legacy-protective-measures)
- [NAC Deployment in VPN Environments: A Limited Safeguard](#nac-deployment-in-vpn-environments-a-limited-safeguard)
- [VPN User Experience and Management Issues](#vpn-user-experience-and-management-issues)
- [VPN Replacement: A Shift Toward Secure Access](#vpn-replacement-a-shift-toward-secure-access)
- [Zero Trust Adoption](#zero-trust-adoption)
- [VPN Risk Predictions for 2025](#vpn-risk-predictions-for-2025)

---

## Executive Summary

The Zscaler ThreatLabz 2025 VPN Risk Report delivers an incisive look at the evolving risks associated with virtual private networks (VPNs) and underscores the urgent shift towards zero trust architectures as organizations strive to meet future-proofed security demands. Once heralded as the backbone of remote access, VPNs have increasingly become focal points for cyber threats, transitioning from essential tools to significant security risks for organizations worldwide. This report, drawing insights from over 600 IT and security professionals, reveals a critical pivot in the cybersecurity landscape: more than half of the organizations surveyed experienced attacks due to VPN vulnerabilities in the past year alone, highlighting the dire need for a new approach in today’s increasingly hybrid work environments.

In 2025, the dissatisfaction with traditional VPNs has catalyzed a shift, with enterprises overwhelmingly recognizing that patching these vulnerabilities is a race they can no longer win. This realization is driving the widespread adoption of zero trust models, which promise granular access control and significantly reduce security risks. Notably, 81% of organizations are now pivoting to implement zero trust strategies by 2026, with 65% planning to completely phase out VPNs within the same period. Moreover, operational frustrations such as slow connections, frequent disconnections, and complex authentication processes have only added to the urgency, propelling a surge in demand for zero trust solutions that ensure both seamless and secure access.

All of these shifts happen within the context of an AI-enabled threat landscape. Indeed, the rise of AI-driven cyberattacks will impact VPN security in unprecedented ways. Attackers will increasingly leverage AI for automated reconnaissance of VPN vulnerabilities, which are easily scanned over the public internet. Techniques like intelligent password spraying and rapid exploit development will allow threat actors to compromise VPN credentials at greater scale. Further down the attack chain, AI-powered evasion techniques will make it even more difficult to detect VPN-based intrusions before significant damage occurs. As such AI-driven threats grow, VPN risks will only magnify, driving enterprises to adopt proactive security measures and accelerating the already pronounced shift towards zero trust solutions.

Acknowledging these shifts, the ThreatLabz report not only charts the decline of VPNs from indispensable tools to liabilities but also provides actionable insights for enterprises navigating this transformative landscape.

---

## Key Findings

1. **Obsolescence of VPNs Accelerates**: A significant 65% of enterprises are set to replace their VPN services within the next year, marking a 23% increase from 2024. This trend is primarily driven by the inability of VPNs to meet the security and compliance demands of modern enterprises, highlighting their role in exacerbating risks rather than mitigating them.

2. **Escalation of VPN-Exploited Cyberattacks and Ransomware Concerns**: The past year saw a worrying increase in cyber incidents linked to VPN vulnerabilities, with 56% of organizations reporting such breaches, an alarming rise from previous figures. Meanwhile, 92% of respondents have concerns that unpatched VPN vulnerabilities will lead directly to ransomware attacks. These findings support the trend that, struggling to maintain the rapid pace of vulnerability patching, enterprises need a robust security overhaul to fill these critical security gaps and mitigate the ever-present risks of VPN exploitation.

3. **End-User Dissatisfaction Influences Security Redirection**: User frustrations over VPN inefficiencies—ranging from slow speeds to cumbersome, complex, or broken authentication—are increasingly influencing organizational strategies. This end-user discontent is driving the push towards zero trust architectures that offer uninterrupted, secure access without the traditional hassles associated with VPNs.

4. **The Zero Trust Shift from VPN: From Concept to Implementation**: Reflecting a major strategic shift, 81% of organizations are actively moving towards implementing zero trust frameworks within the next year. This marks a pivotal transition from viewing zero trust as a theoretical ideal to recognizing it as a practical necessity to replace VPNs while enhancing security in dynamic and distributed IT environments.

---

## VPN Risks: Why 81% of Organizations Are Pivoting to Zero Trust by 2026

VPNs were designed to provide remote access, but times have changed—and so have attackers. Today, VPNs often serve as entry points for ransomware attacks, credential theft, and cyber espionage due to vulnerabilities that are difficult to patch quickly; implicit trust models that provide complete network access; and widespread access permissions. In all, security vulnerabilities are the single largest challenge enterprises face with VPNs (according to 54% of respondents)—underscoring the fact that attackers routinely exploit unpatched flaws or bypass protections to infiltrate networks.

The risks become even more pronounced with third-party VPN access. A massive 93% of respondents express concerns over backdoor vulnerabilities introduced by external VPN connections, as attackers increasingly exploit third-party credentials to breach networks undetected. It’s not just about initial access, either—VPNs also make breaches more destructive. Unlike zero trust solutions that enforce granular policies to prevent movement within networks, VPNs provide broad access, allowing attackers to move laterally and escalate privileges. Overall, 71% of respondents identify lateral movement as a top concern, recognizing how it amplifies the scope and impact of a breach.

These challenges, paired with everyday concerns like slow performance, complex authentication, and frequent disconnections, make it clear why enterprises are moving away from VPNs in favor of zero trust models. The 2025 VPN Risk Report, based on insights from 632 IT and cybersecurity professionals, aims to shed light on the state of VPN usage in 2025 to better understand risks and challenges as well as offer enterprises best practice guidance to improve their cybersecurity posture and their approach to secure remote access.

---

## VPN Security Concerns

The top challenge—security and compliance risks, cited by 54% of respondents—reinforces the critical vulnerability of VPNs in the face of ransomware, privilege escalation, and lateral attack movement. Attackers view VPNs as weak links ripe for exploitation, while organizations struggle to patch these outdated systems fast enough to keep up with advanced threats.

User frustration has reached a boiling point: 51% of respondents identify poor VPN performance—including elements like sluggish connectivity, drop-offs, and cumbersome authentication protocols—as a roadblock to productivity. VPNs remain an operational burden, with 41% of survey respondents citing difficulties in management and 37% flagging high costs for continued maintenance.

![Figure 1: The biggest challenges with VPN solutions.]

---

## Ransomware and VPNs: A Perfect Storm of Risk

Overall, 92% of survey respondents expressed high levels of concern about ransomware targeting unpatched VPN vulnerabilities. This data underscores why VPNs are now seen as liabilities rather than reliable tools for mitigating modern cyber risks.

Real-world examples continue to validate these fears. In January 2023, multiple US healthcare organizations fell victim to a ransomware attack driven by an unpatched Citrix NetScaler vulnerability (CVE-2023-4966). This exploit enabled attackers to infiltrate systems, disrupt hospital operations, lock patient records, and force facilities to divert critical emergency care.

![Figure 2: Concerns about ransomware attacks.]

---

## VPNs and Lateral Movement: Increasing the Blast Radius of Breaches

In addition to enabling initial compromise through ransomware and other threats, VPNs facilitate lateral movement—a dangerous attack technique. A total of 71% of respondents expressed some level of concern for this risk.

In September 2024, attackers exploited multiple zero-day vulnerabilities in Ivanti’s Cloud Service Appliance (CSA), notably CVE-2024-8963 and CVE-2024-8190, to breach several organizations. Despite previous security incidents involving Ivanti VPNs, these new exploits demonstrate that patching or rearchitecting legacy VPN solutions still fails to address the fundamental security flaws inherent in network-based remote access models.

![Figure 3: Enterprise concerns that will move laterally across the network if a VPN is compromised.]

---

## VPN CVEs from 2020-2025: A Rising Wave of High-Severity Vulnerabilities

Zscaler ThreatLabz analyzed 411 VPN Common Vulnerabilities and Exposures (CVEs) from 2020-2025. The findings indicate a surge of VPN vulnerabilities that have gradually risen through the first half of this decade.

In 2024, 60% of the 83 VPN vulnerabilities reported by NIST indicated a high or critical CVSS score. Remote code execution (RCE) vulnerabilities were the most common VPN CVEs.

![Figure 4: Total VPN CVEs for each year, from 2020-2024.]

---

## Key Trends: CVE Impact Types

1. **RCE Remains the Top Threat**: RCE accounts for 149 CVEs including 2025 data, making it the most frequent and critical vulnerability type.
2. **Privilege Escalation is Steadily Growing Over Time**: Peaking in 2024 with 20 vulnerabilities.
3. **Denial-of-Service (DoS) Vulnerabilities Show a Sharp 200% Rise**: DoS-related CVEs tripled from 9 in 2020 to 27 in 2024.
4. **Sensitive Information Leakage is Rarer but Still Critical**: 41 CVEs total.
5. **Steady Growth in Authentication Bypass Vulnerabilities**: Totaling 30 CVEs over time.

![Figure 5: The impact type of VPN CVEs from 2020-2024.]

---

## Key Trends: Critical VPN Vulnerabilities

Overall, ThreatLabz found the CVEs with CVSS scores of HIGH or CRITICAL grew 38.9% from 2020 to 2024.

1. **Increasing Exploitation of Web-Based Management Interfaces**: Attackers see these management interfaces as attractive and accessible targets.
2. **Widespread Authentication and MFA Bypasses**: Evolved into more advanced, automated, and persistent attacks.
3. **Rise in Local Privilege Escalation Exploits**: Intensified by 2024–2025 into more sophisticated methods, such as DLL hijacking.
4. **Growing Sophistication of DoS and DDoS Attacks**: Transitioned from simple malformed packet-based disruptions to more advanced amplified attacks.
5. **Persistent and Intensifying Cryptographic Failures**: A noticeable spike in cryptographic vulnerabilities, peaking in 2024–2025.

![Figure 6: The volume of VPN CVEs with HIGH and CRITICAL CVSS scores from 2020-2024.]

---

## The Challenges of Implementing Segmentation

The survey highlights these challenges, with 51% of organizations anticipating or encountering configuration complexity. Additionally, 39% report a lack of expertise and resources, while 24% face performance bottlenecks.

![Figure 7: The top challenges enterprises face when implementing segmentation.]

---

## VPNs Increase M&A Cybersecurity Risks

Nearly two-thirds (64%) of respondents expressed concern about cyberthreats following M&A, acknowledging the security gaps that arise during IT integrations.

![Figure 8: Enterprises are concerned about cyber attacks after M&A.]

---

## Third-Party VPN Access: A Backdoor for Attackers

With 93% of respondents expressing critical concerns about backdoor vulnerabilities, third-party access represents a ticking time bomb for organizations reliant on static, trust-based access models.

![Figure 9: Enterprise concerns about third-party VPN access facilitating cyber attacks.]

---

## Challenges and Gaps with Legacy Protective Measures

According to the survey, firewalls (84%), web application firewalls (WAFs, 58%), and VPNs (43%) still dominate organizations’ web attack defenses. However, attackers are increasingly bypassing these tools.

![Figure 10: The security products in-use by enterprises to defend private applications from web-based threats.]

---

## NAC Deployment in VPN Environments: A Limited Safeguard

A notable 54% of surveyed organizations report using NAC to secure VPN access to private resources. However, these deployments have yet to prevent the breaches and exploits commonly associated with VPN vulnerabilities.

![Figure 11: Proportion of enterprises using NAC in between VPNs and private resources.]

---

## VPN User Experience and Management Issues

Slow connection speeds are the most common complaint (23%), underscoring VPNs’ reputation for latency, congestion, and poor performance.

![Figure 12: The most common complaints among VPN users.]

---

## VPN Replacement: A Shift Toward Secure Access

The survey confirms this momentum, with 65% of respondents saying their organizations are either replacing or planning to replace their VPNs within the next year.

![Figure 16: Enterprise plans to replace existing VPN services.]

---

## Zero Trust Adoption

Survey results underscore the growing momentum of this paradigm shift: 81% of respondents indicate plans to adopt zero trust slated within the year.

![Figure 17: Enterprise plans for implementing a zero trust strategy.]

---

## VPN Risk Predictions for 2025

- **Critical VPN Vulnerabilities Will Continue to Emerge**: The growing number of VPN exploits in recent years will accelerate in 2025.
- **Ransomware Groups Will Intensify VPN Exploits**: Ransomware-as-a-service (RaaS) groups frequently scan for exposed VPNs with unpatched vulnerabilities.
- **Lateral Movement via VPNs Will Drive More Destructive Attacks**: Attackers exploit the broad access VPNs provide to move laterally.
- **Third-Party VPN Access Will Remain a Key Threat Vector**: Third-party access remains a primary entry point for attacks.
- **Major VPN-Related Breaches Will Make Headlines**: Organizations will face greater pressure to disclose VPN-related cyber incidents.
- **Zero Trust Investments Will Surge as VPNs Decline**: Investment in zero trust security is accelerating, fundamentally reshaping the remote access landscape.

---

ing organizations
to move beyond VPNs as legacy solutions fail
to meet security, scalability, and compliance
demands. Zero trust adoption not only reduces
cyber risk, but also eliminates the high costs
of maintaining VPN concentrators, network
appliances, and continuous patching cycles. As a
result, VPNs are increasingly viewed as obsolete,
prompting an industry-wide shift toward zero
trust security models.

As 93% of respondents express concern over
third-party VPN vulnerabilities, attackers will
continue targeting weak external access points.
Stolen third-party credentials and misconfigured
VPN access remain among cybercriminals’ top
entry points. The 2024 Enterprise Financial
Group (EFG) breach demonstrated how attackers
exploit third-party VPN connections to infiltrate
corporate environments. Many organizations lack
visibility into third-party access permissions,
making it difficult to enforce security policies. To
mitigate these risks, organizations must transition
to a zero trust framework, enforcing strict least-
privileged access and continuous verification for
all external connections.

AI-Driven VPN Exploits
Will Increase

The rise of AI-driven cyberattacks will impact
VPN security in unprecedented ways. Attackers
will increasingly leverage AI for automated
reconnaissance, intelligent password spraying,
and rapid exploit development, allowing them
to compromise VPN credentials at scale.
AI-powered evasion techniques will make
it even more difficult to detect VPN-based
intrusions before significant damage occurs.
Meanwhile, AI-powered VPN security solutions
may introduce unforeseen security gaps, leading
to new attack vectors that cybercriminals will
exploit. As AI-driven threats grow, organizations
must adopt proactive security measures such
as continuous identity verification and zero trust
access controls.

Zscaler ThreatLabz 2025 VPN Risk Report

These predictions highlight a growing consensus: organizations that delay zero
trust adoption will remain highly vulnerable as VPN exploits increase. The future of
secure access depends on proactive risk mitigation, not reactive patching—making
now the time to move beyond VPNs.

27

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.

Best Practices for
Secure_Access

Reduce VPN Risks and
Strengthen Zero Trust Security

1.  Remove network-based access to minimize the attack surface
Prevent attackers from exploiting exposed network entry points
by phasing out VPNs and network-based access in favor of direct,
application-specific connectivity. Survey data shows that 54% of
organizations cite security risks as their top VPN challenge, reinforcing
the need to remove VPN dependencies and firewall-based security
models that expose enterprises to attack.

2.  Stop initial compromise with inline threat prevention

Inspect all encrypted and unencrypted traffic inline to block zero-day
exploits, malware, and ransomware payloads before they reach users.
As 92% of organizations worry about ransomware targeting VPN
vulnerabilities, real-time traffic inspection and policy-based blocking
are essential. A cloud native security model eliminates the need for
on-premises firewalls and reduces the attack surface.

3.  Strengthen authentication and identity security

Implement phishing-resistant multifactor authentication (MFA), such
as FIDO2 credentials, biometrics, or hardware tokens to verify user
access. Avoid legacy authentication methods like SMS-based MFA
and push notifications, which attackers frequently bypass. Integrate
identity-driven security with continuous verification instead of relying
on one-and-done authentication.

4.  Enforce least-privileged, context-based access with ZTNA

Replace broad VPN access with zero trust network access (ZTNA)
to ensure users only connect to authorized applications—never the
network itself. Granular, just-in-time (JIT) access controls based on
identity, device posture, and real-time risk analysis ensure users can
only access what they need, when they need it.

5.  Eliminate lateral movement with zero trust segmentation

Connect users directly to applications, not the network, to prevent
attackers from moving across systems if they gain initial access. Zero
trust segmentation and identity-aware microsegmentation ensure
that even if a user is compromised, an attacker cannot pivot to other
resources or escalate privileges. ZTNA eliminates VPN tunnels, which
are a major enabler of lateral movement.

6.  Secure third-party and external access with identity-based controls

Enforce least-privileged access for third parties, vendors, and
contractors, applying strict session controls, device health checks,
and continuous monitoring. Replacing VPN-based third-party access
with ZTNA significantly reduces risk exposure from compromised
vendor credentials—a welcome change for the 93% of organizations
concerned about third-party VPN risks.

Zscaler ThreatLabz 2025 VPN Risk Report

28

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.

By implementing these best practices,
organizations can eliminate the
security risks of VPNs with a resilient
zero trust security framework,
ensuring continuous verification,
least-privileged access, and proactive
threat mitigation.

7.  Enhance data protection with integrated zero trust policies

Deploy inline data loss prevention (DLP) and cloud access security broker
(CASB) controls to inspect, encrypt, and prevent unauthorized data
movement in real time. A zero trust security framework ensures that all
user traffic is inspected and controlled, even in SaaS applications and
cloud environments.

8.  Deploy AI-driven security and continuous monitoring
Use real-time AI-powered analytics, deception technology, and
automated behavioral detection to stop threats before they escalate.
ZTNA solutions provide real-time risk scoring, preventing compromised
accounts from accessing sensitive applications. Daily proactive
threat hunting and risk-based access controls significantly reduce
breach impact.

9.  Continuously assess and adapt security posture

Conduct automated risk assessments, penetration testing, and adversary
simulations to dynamically adjust zero trust security policies. Security
misconfigurations and lack of enforcement are key contributors to major
breaches, making automated, policy-driven enforcement critical for
reducing human error.

10.  Eliminate VPN infrastructure and automate security policy enforcement
Remove the need for VPN concentrators, firewall rule management,
and manual access control lists by adopting a cloud-delivered zero
trust model. ZTNA enables dynamic security policies that adapt in
real time to compliance changes, regulatory updates, and evolving
cyberthreats—without manual configuration or hardware dependencies.

To effectively secure private resources, organizations must eliminate
reliance on VPNs and adopt a zero trust model, in which users
connect directly to applications rather than the network itself. Unlike
NAC, zero trust continuously validates identity, context, and device
posture for each access request, preventing unauthorized access and
stopping lateral movement before attackers can escalate privileges or
exfiltrate data.

Zscaler ThreatLabz 2025 VPN Risk Report

29

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.

How Zscaler Transforms
Secure_Access

ZPA can be deployed in a matter of hours to
replace legacy VPNs and remote access tools
with a holistic zero trust platform. Powered by
the world’s largest security cloud, ZPA delivers
fast, reliable, and low-latency connectivity to
users anywhere in the world. Its cloud native
architecture ensures elastic scalability, seamlessly
supporting the needs of distributed and hybrid
workforces across various geographies.

With ZPA, enterprises can embrace cloud-first,
hybrid workforce models with confidence,
knowing their resources are protected, their
users are productive, and their IT operations
are future-proofed.

Traditional VPNs and firewalls significantly
expand an organization’s attack surface by
placing users directly on the network. This broad
access makes it easier for attackers to exploit
vulnerabilities, gain entry, and move laterally
within the environment. As threats continue
to evolve and hybrid work becomes the norm,
relying on these outdated technologies poses
critical security risks that demand more secure,
adaptive solutions.

Zscaler Private Access™ (ZPA) provides a
secure, scalable alternative to legacy remote
access solutions like VPNs. As a cloud native
solution, ZPA enables zero trust access for all
users by offering direct connectivity to private
applications. To minimize the attack surface,
applications are shielded behind the Zscaler
Zero Trust Exchange™ platform. This approach
eliminates lateral movement through AI-
powered user-to-application segmentation
and defends against sophisticated threats
with integrated traffic inspection, as well as
application and data protection.

30

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.Key Benefits of Zscaler
Private Access (ZPA)

Minimize the attack surface to
protect against ransomware attacks
VPN vulnerabilities expose organizations to
malicious users, leading to ransomware attacks
and credential theft. ZPA eliminates this risk
by hiding all applications behind the Zero Trust
Exchange and granting users direct, zero trust
access only to authorized applications. By
preventing unauthorized users, including third-
party vendors and contractors, from discovering
applications and moving laterally, ZPA effectively
protects against ransomware attacks. It enables
secure remote access for all applications,
including private apps, network-connected
applications like VoIP, and server-to-client
apps. Additionally, ZPA minimizes the impact
of disruption through a comprehensive business
continuity solution and helps organizations meet
strict compliance requirements.

Eliminate lateral threat movement
ZPA enforces least-privileged access by
connecting users directly to specific applications,
preventing access to other applications in
the network. It provides visual insights into
user-to-application access and policies applied,
enhancing visibility and control. ZPA AI-Powered
Segmentation automatically generates

recommendations for app segments and policies,
simplifying segmentation implementation while
ensuring scalability and robust security.

Gain granular visibility and analytics
ZPA provides detailed, real-time visibility into
application usage, user behavior, and access
patterns. IT teams can use this data to monitor,
audit, and quickly identify potential threats,
enhancing overall security posture. This can also
help in ensuring regulatory compliance.

Deliver clientless access to mitigate
third-party vulnerabilities

ZPA Clientless Access simplifies third-party
access by allowing contractors and partners to
securely connect to applications via any browser
without requiring a client. It isolates unmanaged
devices from the corporate network, protects
sensitive data, and integrates with Google
Chrome Enterprise Browser for enhanced BYOD
security. This modern approach reduces costs,
minimizes risks associated with third-party
access, and eliminates reliance on legacy
VDI management.

31

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2025 VPN Risk ReportPrevent private app compromise
ZPA minimizes the risk of private app
compromise and data loss by performing full
inline inspection of end-to-end private app
traffic. Robust data loss prevention capabilities
ensure sensitive information remains secure
while blocking unauthorized access. By hiding
applications from the public internet and enabling
secure user-to-app connections based on zero
trust principles, ZPA reduces the attack surface,
prevents lateral movement, and protects against
breaches, enhancing overall security.

Simplify policy management and
speed up deployment
ZPA streamlines IT operations by simplifying
remote access deployment, policy management,
and user-to-app segmentation. Previously time-
consuming tasks—such as user onboarding,
patching, and upgrades—can now be completed
in minutes, significantly reducing IT effort.
With centralized management and automated
policy recommendations, ZPA enables IT teams
to improve efficiency, minimize complexity,
and focus on strategic initiatives rather than
day-to-day operations.

Enforce device posture-driven
access control
ZPA integrates with endpoint posture
assessment tools to verify the security posture
of user devices before granting access. This
ensures that only compliant devices can

connect, mitigating risks from unmanaged or
compromised devices.

Deliver superior user experiences
ZPA ensures optimal user experiences by
providing fast, seamless, and secure connectivity
to business-critical applications. Unlike VPNs
that backhaul traffic through a centralized data
center, ZPA enables direct user-to-application
connections via the Zero Trust Exchange.
This drastically reduces latency and improves
application performance, whether users are on-
site, remote, or on the go. By minimizing multiple
logins and dependency on client-based software,
ZPA simplifies access and boosts productivity.
Additionally, ZPA’s proactive monitoring
capabilities streamline issue resolution, ensuring
uninterrupted, high-quality access for all users.

Reduce total cost of ownership
ZPA significantly reduces total cost of ownership
by eliminating the need for multiple point
products such as VPNs, firewalls, NACs, and
VPN concentrators. Built on a cloud native zero
trust architecture, ZPA removes infrastructure
costs related to hardware support, maintenance,
repairs, and updates. Its simplified management
and automated policy enforcement reduce
operational overhead, allowing IT teams to save
time and resources while improving security
and scalability.

©2025 Zscaler, Inc. All rights reserved.

32

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.Methodology_and
Demographics

This report is based on a comprehensive survey of 632 IT and cybersecurity professionals conducted
in early 2025, examining VPN security risks, enterprise access trends, and the adoption of zero trust
architectures. Respondents included executives, IT security practitioners, and network infrastructure
leaders across various industries. The findings in this report provide a data-driven perspective on the
decline of VPNs and the shift to zero trust, offering critical insights for organizations modernizing their
access security strategies.

Career Level

27%

19%

14%

10%

7%

6%

5%

12%

Manager/
Supervisor

Specialist/
Coordinator/
Analyst

Department

Director

Vice
President

CTO,CIO,CISO,
CMO,CFO,COO

Consultant

Founder/CEO/
President

Other

42%

21%

9%

7%

6%

3%

12%

IT Security

IT Operations

Infrastructure

Network

Engineering

Product
Management

Other

Company Size

1,000-5,000
employees

Industry

37%

34%

29%

5,001-20,000
employees

>20,000
employees

21%

13%

11%

10%

8%

7% 6% 5%

19%

Computers,
Software,
Technology

Healthcare,
Pharmaceuticals
& Biotech

Financial
Services

Government

Manufacturing

Telecommu-
nications

Education
& Research

Professional
Services

Other

Zscaler ThreatLabz 2025 VPN Risk Report

3333

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.About Zscaler

About Cybersecurity Insiders

Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can
be more agile, efficient, resilient, and secure. The Zscaler Zero Trust Exchange™
protects thousands of customers from cyberattacks and data loss by securely
connecting users, devices, and applications in any location. Distributed across more
than 150 data centers globally, the SASE-based Zero Trust Exchange is the world’s
largest inline cloud security platform. To learn more, visit www.zscaler.com.

About ThreatLabz

ThreatLabz is the security research arm of Zscaler. This world-class team
is responsible for hunting new threats and ensuring that the thousands of
organizations using the global Zscaler platform are always protected. In addition
to malware research and behavioral analysis, team members are involved in
the research and development of new prototype modules for advanced threat
protection on the Zscaler platform, and regularly conduct internal security audits to
ensure that Zscaler products and infrastructure meet security compliance standards.
ThreatLabz regularly publishes in-depth analyses of new and emerging threats on
its portal, research.zscaler.com.

C Y B E R S E C U R I T Y   I N S I D E R S  -   YO U R   T R U S T E D   S O U RC E   F O R

DATA- D R I V E N   C Y B E R S E C U R I T Y   I N S I G H T S

Cybersecurity Insiders delivers evidence-backed insights and third-party validation,
empowering cybersecurity leaders to make informed, strategic decisions. Built on
more than a decade of research with a global network of over 600,000 cybersecurity
professionals, we deliver actionable intelligence that helps leaders navigate evolving threats,
evaluate new technologies, and shape forward-looking strategies with confidence.

For cybersecurity vendors, we turn research insights into results — building credibility,
visibility, and trust through high-impact formats such as data-powered market reports
and webinars that establish thought leadership, CISO guides that showcase best practices,
product reviews that validate solutions, how-to articles that educate buyers, and award
recognition that elevates brand reputation.

By combining this content with built-in distribution, we help brands earn trust, amplify
awareness, and drive demand in a crowded cybersecurity market.

Learn more: cybersecurity-insiders.com

Holger Schulze
CEO & Founder
Cybersecurity Insiders

Zscaler ThreatLabz 2025 VPN Risk Report

©2025 Zscaler, Inc. All rights reserved.

3434

Zscaler ThreatLabz 2025 VPN Risk Report©2025 Zscaler, Inc. All rights reserved.

About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and
secure. The Zscaler Zero Trust Exchange™ platform protects thousands of customers from cyberattacks and data
loss by securely connecting users, devices, and applications in any location. Distributed across more than 150 data
centers globally, the SSE-based Zero Trust Exchange™ is the world’s largest in-line cloud security platform. Learn
more at zscaler.com or follow us on Twitter @zscaler.

© 2025 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks are either (i) registered
trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other countries. Any other
trademarks are the properties of their respective owners.

+1 408.533.0288

Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134

zscaler.com

Zero Trust Everywhere