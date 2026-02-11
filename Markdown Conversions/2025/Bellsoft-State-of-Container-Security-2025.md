# The State of Container Security 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Security Leads, but Priorities Pull in Different Directions](#security-leads-but-priorities-pull-in-different-directions)
- [Performance Optimization Requires Expertise Most Teams Lack](#performance-optimization-requires-expertise-most-teams-lack)
- [Operational Convenience vs Security Best Practices](#operational-convenience-vs-security-best-practices)
- [Half Choose Bloated Distributions, Half Face Support Gaps](#half-choose-bloated-distributions-half-face-support-gaps)
- [Mainstream JDKs Carry Hidden Security & Cost Burdens](#mainstream-jdks-carry-hidden-security--cost-burdens)
- [Organizations Remain Stuck in Reactive Security Posture](#organizations-remain-stuck-in-reactive-security-posture)
- [Dangerous Update Delays Leave Known Vulnerabilities in Production](#dangerous-update-delays-leave-known-vulnerabilities-in-production)
- [One in Four Hit by Security Incidents](#one-in-four-hit-by-security-incidents)
- [Teams Drowning in Vulnerability Management Work](#teams-drowning-in-vulnerability-management-work)
- [Organizations Need Relief From Endless Vulnerability Management](#organizations-need-relief-from-endless-vulnerability-management)
- [Conclusion](#conclusion)

## Executive Summary
The container ecosystem has matured significantly over the past decade, yet fundamental questions about security practices remain unresolved. To better understand how teams manage container security today, we surveyed 427 professionals at Devoxx 2025 to examine:

- How organizations select and build container images,
- Which security practices they follow,
- What challenges they encounter, and
- Where current practices fall short of their stated priorities.

Across the responses, a clear pattern emerges: teams overwhelmingly value security, efficiency, and simplicity — yet their tools, OS choices, and JVMs directly undermine these goals.

## Key Findings
- **23%** experienced container-related security incidents in the past year.
- **33%** update monthly or less frequently. Meanwhile, exploitation windows have shrunk from weeks to days.
- **48%** want pre-hardened base images, indicating a shift toward outsourcing vulnerability management.
- **49%** cite time and resource constraints as a primary challenge in maintaining container security.
- **29%** of respondents prioritize security (minimal number of CVEs) when selecting base container images.
- **55%** use general-purpose Linux distributions with hundreds of unnecessary packages and unresolved CVEs.
- **2/3** of respondents want efficiency for Java applications in containers, measured by low memory usage, high throughput, and fast startup time.
- **69%** use general-purpose JDKs requiring manual optimization, consuming engineering time and inflating cloud bills.

Teams know what good security looks like, but current tooling, OS choices, and JDKs make it difficult to achieve without external support.

## Security Leads, but Priorities Pull in Different Directions
Security dominates at 29%, followed by performance at 21%, image size at 17%, and Java support at 17%. This split reveals the challenge: teams manage multiple concerns simultaneously.

Image size and memory efficiency directly impact cloud spending. Smaller containers mean lower storage costs, faster deployments, and reduced bandwidth. With hundreds or thousands of instances running, these differences compound quickly.

Java applications complicate this further. General-purpose JDKs weren't built for containers. Organizations either invest significant engineering time in manual tuning or accept higher cloud bills. Solutions like Liberica JDK Lite deliver 30% reduction in memory and disk space without complex configuration.

![Bar chart showing the most important factors when choosing a base container image: Security (minimal number of CVEs) at 29%, Performance at 21%, Image size at 17%, Java support at 17%, Ease of use at 11%, License compliance at 4%, and Other at 1%.]

## Performance Optimization Requires Expertise Most Teams Lack
Respondents overwhelmingly prioritize:
- **Efficient memory usage** (86%)
- **High throughput** (68%)
- **Fast startup** (66%)

But achieving these requires deep knowledge of container-aware GC tuning, heap sizing, CDS configuration, or advanced approaches like GraalVM and CRaC — complex and not always applicable.

Out-of-the-box optimized runtimes, such as lightweight Java distributions, eliminate this effort and deliver consistent performance gains without extra engineering overhead.

![Bar chart showing critical parameters for Java application performance: Efficient memory usage (86%), High throughput under load (68%), Fast startup time (66%), Minimal OS overhead (46%), and Compatibility with cloud-native tools (32%).]

## Operational Convenience vs Security Best Practices
Teams rely on tools like:
- **Shells** (54%)
- **Package managers** (39%)
- **curl/wget** (34%)

These are helpful for debugging but significantly expand the attack surface. Only 17% use minimal/distroless images in production. Organizations face a real conflict: operational convenience during development vs. minimal attack surface in production.

A practical approach is using hardened minimal runtime images, paired with fuller “debug builds” during development — allowing both security and diagnostics without compromise.

![Bar chart showing essential tools inside base containers: Shell (54%), package manager (39%), curl/wget (34%), Editor (25%), none/distroless (17%), openssh (28%), and binutils/coreutils (14%).]

## Half Choose Bloated Distributions, Half Face Support Gaps
The split is revealing: 41% use Alpine while 55% use Ubuntu/Debian or Red Hat-based systems. This represents fundamentally different approaches.

**Ubuntu/Debian and Red Hat** users (55%) rely on general-purpose distributions with hundreds of packages their applications never use. Each represents potential vulnerabilities requiring security patches. When a vulnerability emerges, security teams must evaluate impact and coordinate updates across thousands of instances — regardless of whether the application uses the affected package.

**Alpine Linux** users (41%) chose minimal distributions built for containers, reducing image size and vulnerability exposure. However, Alpine is community-driven with no commercial support, no SLAs, and no Long-Term Support releases. For enterprises under regulatory frameworks, this creates compliance concerns.

Alpaquita Linux addresses this gap — delivering minimal attack surface with enterprise-grade support guarantees.

![Donut chart showing Base Operating Systems: Alpine Linux (41%), Ubuntu/Debian (34%), Red Hat/Red Hat-based distributions (21%), Alpaquita Linux (2%), and other distributions (1%).]

## Mainstream JDKs Carry Hidden Security & Cost Burdens
Over 69% use Oracle/OpenJDK or Adoptium/Temurin — mainstream distributions aligned with what developers know. This familiarity has hidden costs.

These general-purpose JDKs weren't optimized for containers. They consume more memory, produce larger images, and require substantial tuning for acceptable performance. Standard distributions regularly ship with known CVEs requiring continuous tracking and patching. Oracle's commercial JDK adds licensing complexity that changes unpredictably.

Alternatives designed for containerized environments, like Liberica JDK Lite, deliver optimized performance without specialized tuning, maintain a minimal vulnerability profile, and provide clear licensing terms.

![Bar chart showing JDK usage inside containers: Oracle/OpenJDK (48%), Adoptium/Temurin (21%), Amazon Corretto (14%), I do not use JVM containers (8%), BellSoft’s Liberica JDK (7%), and Other (2%).]

## Organizations Remain Stuck in Reactive Security Posture
Responses reveal different security maturity stages. Trusted registries at 45% and vulnerability scanning at 43% represent basic hygiene — catching known vulnerabilities reactively. SBOM generation at 18% and image signing at 16% address supply chain visibility but remain challenging to implement. Only 6% use hardware isolation.

Ten percent report no additional security measures beyond standard tools.

The focus remains heavily weighted toward detection and monitoring rather than prevention. Most organizations are trapped in reactive security, constantly responding to newly discovered vulnerabilities rather than building on foundations that minimize exposure from day one.

![Bar chart showing applied container security mechanisms: Working only with trusted image registries (45%), Vulnerability scanning (43%), Only standard Docker/Kubernetes tools (36%), Software Bill of Materials (18%), Image signing (16%), No additional measures (10%), and Secure container isolation (6%).]

## Dangerous Update Delays Leave Known Vulnerabilities in Production
While 31% update with every release and 26% when critical vulnerabilities emerge, 33% update monthly, rarely, or only a few times yearly. In today's threat landscape, this represents substantial risk.

Time between vulnerability disclosure and exploitation continues shrinking. What once took weeks now happens in days. Organizations updating monthly or less operate with known vulnerabilities attackers actively exploit.

The reasons are understandable: updates require testing, validation, and coordination. But this creates a dangerous pattern. The longer you delay, the more changes accumulate, making each update riskier — a negative feedback loop that further discourages frequent updates.

![Bar chart showing container image update frequency: With every application release (31%), Only when critical vulnerabilities are found (26%), Monthly (19%), Rarely (14%), and Weekly (10%).]

## One in Four Hit by Security Incidents
Twenty-three percent reported security incidents — 18% minor and 5% major. The problem isn't detection — it's the gap between vulnerability disclosure and remediation. During this window, often weeks or months, organizations operate with known exposures.

The 60% reporting no incidents shouldn't breed complacency. Many haven't experienced attempted attacks yet or lack visibility to detect successful intrusions.

The data reinforces a critical point: reactive security measures aren't sufficient. Organizations need approaches that minimize risks of human mistakes and vulnerability exposure from the foundation.

![Pie chart showing security incidents in the past 12 months: No incidents (60%), Yes, minor incident(s) (18%), and Yes, major incident(s) (5%). Note: Remaining percentage represents "Unsure/No Answer".]

## Teams Drowning in Vulnerability Management Work
The challenges cluster into three related categories:

1.  **Human errors**: dominate at 62% — even with the best tools, implementation failures remain the primary vulnerability.
2.  **CVE management**: revolves around patching difficulties at 36%, gaps before patches at 32%, and false positives at 29%.
3.  **Human Resources & Support**: centers on time constraints at 49% and lack of organizational priority at 36%.

These clusters reinforce each other. Insufficient resources lead to rushed implementations, causing human errors. The overwhelming CVE workload consumes available time, leaving no capacity for proactive improvements.

![Bar chart showing main challenges in securing containers: Human errors (62%), Time and resource constraints (49%), Difficulties with regular patching (36%), Lack of organizational priority (36%), Gaps before patches become available (32%), False positives from scanning tools (29%), and Limitations of standard tools (27%).]

## Organizations Need Relief From Endless Vulnerability Management
The top three needs converge on the same requirement: relief from overwhelming vulnerability management. Pre-hardened images at 48%, better automation at 47%, and more resources at 36% are different approaches to the same problem.

Pre-hardened images shift from reactive to proactive security. The vendor handles all the firefighting — scanning, patching, and testing. Whenever you pull an image from the registry, it's free of known CVEs and stays that way. Patching becomes the vendor's responsibility, completely removing this workload from your teams.

![Bar chart showing what would help improve container security: Pre-hardened, security-focused base images (48%), Better/easier automated tools (43%), More time and resources (36%), Clearer best practices and guidelines (29%), Better integration with development workflows (21%), and Executive support and prioritization (19%).]

## Conclusion
Across every section of the survey, one message repeats consistently: Teams want security, efficiency, and simplicity, but their current tooling makes this difficult to achieve.

The 48% requesting pre-hardened images aren't just looking for a security tool. They're signaling a desire to build their platform engineering on a foundation that's secure by default. Hardened vendor-maintained images directly address the root causes of today's container security challenges, reducing vulnerability exposure, operational strain, cloud costs, and risk of human errors.

As the industry moves beyond reactive security, hardened images are emerging as the most effective path toward stable, low-maintenance, high-security container environments.

**48% want pre-hardened, security-focused images.**