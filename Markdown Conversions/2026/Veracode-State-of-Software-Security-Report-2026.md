2026 STATE OF
PRIORITIZE, PROTECT, PROVE

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Contents
03 22
Executive Summary Comparative Analysis:
Key Findings Key Shifts from 2025 to 2026
06 25
Chapter 1: Actionable Insights
The Security Debt Crisis Intensifies and Recommendations
• For Organizations with
High Security Debt
10
• For Organizations with
Growing Application Portfolios
Chapter 2: • For Technology Leaders
The High-Risk Vulnerability Surge and Executives
13 28
Chapter 3: The Path Forward
Modest Progress in Detection,
Struggles in Remediation
32
16
Methodology
Chapter 4:
The Persistent Third-Party 33
Supply Chain Challenge
Appendix
20
Chapter 5:
The AI Era’s Double-Edged Impact
© Veracode 2026. All rights reserved. 2

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Executive
Summary
What happens
when keeping pace
isn’t an option?
© Veracode 2026. All rights reserved. 3

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Innovation and risk are inseparable. As organizations
build the future, they will inevitably create vulnerabilities.
The critical question is not how to eliminate all
risk, but which risks are you willing to accept?
The 2026 State of Software Security (SoSS) affects 60% of organizations, a stark 20%
report illuminates a difficult truth: the pace rise from the previous year, and high-risk
of flaw creation is decisively outstripping the vulnerabilities saw a 36% relative increase.
current capacity for remediation. Despite
marginal gains in fix rates, the tide of security When the velocity of development in the AI era
debt – known vulnerabilities left unresolved makes comprehensive security unattainable,
for more than a year – is rising. This is not the strategy must evolve. The path forward
a distant problem; it is a present reality for is not about running faster on a treadmill of
82% of organizations, an 11% increase in a endless flaws. It’s about making deliberate,
single year. Plus, the debt accumulating is intelligent choices about which risks to accept
not benign. Critical security debt (flaws that and which to neutralize. It’s about learning to
are both severe and highly exploitable) now prioritize, protect, prove, and, ultimately, prevail.
This summary analysis puts 2026 findings against the 2025 baseline to illuminate the primary
themes that will shape our understanding of software security maturity in an era where AI-
driven development, expanding attack surfaces, and accelerating release cycles collide with
finite remediation capacity. The following chart measures not just the absolute change, but the
percentage of change year-over-year (YoY). This captures, for example, how a shift from 50% to
60% critical debt reflects a 20% relative increase, not just a 10-point rise. This approach provides
a more nuanced view of the rate at which risk indicators are accelerating or improving over time.
Declines since 2025 Improvements since 2025
YoY % YoY %
change change
ORGANIZATIONS WITH SECURITY DEBT APPS WITH OPEN SOURCE FLAWS
2026 82%
+11
62%
-11
% %
2025 74% 70%
ORGANIZATIONS WITH CRITICAL DEBT FIX SPEED (HALF-LIFE)
60% +20 243 DAYS 1 YEAR -4
% %
50% 252 DAYS
APPS WITH SECURITY DEBT OVERALL FLAW PREVALENCE
49%
+17
78%
-3
% %
42% 80%
HIGH-RISK VULNERABILITIES
11.3%
+36
%
8.3%
© Veracode 2026. All rights reserved. 4

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Key themes
As we delved into the findings for this year’s report, we saw multiple themes arise:
The Security Debt The High-Risk
Crisis Intensifies Vulnerability Surge
With 82% of organizations now burdened A 36% YoY spike in flaws that are both
by security debt, the accumulation of highly severe and likely to be exploited
vulnerabilities older than a year is outpacing demands an urgent shift from generic
remediation capacity, signaling a severity scoring to prioritization based
critical need to rethink how on real-world attack potential.
we manage backlogs.
Modest Progress in Detection, The Persistent Third-Party
Struggles in Remediation Supply Chain Challenge
While organizations are successfully Despite improvements in general open-
finding fewer flaws and improving source hygiene, third-party components
detection rates, the data remain the primary source of critical,
reveals a persistent long-lived debt, underscoring
struggle to fix them the necessity of
quickly enough to rigorous supply
close the widening chain defenses.
exposure window.
The AI Era’s Double-Edged Impact
The rise of AI is reshaping the landscape by potentially
introducing new patterns of high-risk vulnerabilities
while simultaneously offering the automated
remediation capabilities needed to finally turn the tide.
© Veracode 2026. All rights reserved. 5

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
CHAPTER 1
The
Security Debt Crisis
Intensifies
© Veracode 2026. All rights reserved. 6

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Security debt—known vulnerabilities left unresolved for more than a
year—has surged dramatically, with organizational prevalence climbing
from 74% to 82% and rising from 50% to 60% of organizations in a
single year. This trend has continued year after year, with security
debt mounting and affecting more and more organizations.
Key Points
|     | Overall Security Debt:  |     |     | Critical Security Debt:  |     |     |     |
| --- | ----------------------- | --- | --- | ------------------------ | --- | --- | --- |
82%  of organizations affected   60%  of organizations affected
(up from 74%, an +11% YoY increase) (up from 50%, a +20% YoY increase)
FIGURE 1
Prevalence of
security debt and
critical debt and
|                     |                          | 74       | 82   |                      | 50       | 60   |     |
| ------------------- | ------------------------ | -------- | ---- | -------------------- | -------- | ---- | --- |
| among organizations |                          | %        | %    |                      | %        | %    |     |
|                     |                          | 2025 +11 | 2026 |                      | 2025 +20 | 2026 |     |
|                     |                          |          | %    |                      | %        |      |     |
|                     | Application-Level Debt:  |          |      | Apps with No Flaws:  |          |      |     |
49%  of apps now carry security debt  Increased slightly to  6.5%  from 6.1%
(up from 42%, a +17% YoY increase)
FIGURE 2
Prevalence of
|     | Apps with no flaws |     | Apps with flaws but no debt |     | Apps with security debt |     |     |
| --- | ------------------ | --- | --------------------------- | --- | ----------------------- | --- | --- |
security debt across
| all applications active  | 6.5% |     |     | 44.6% |     |     | 48.9% |
| ------------------------ | ---- | --- | --- | ----- | --- | --- | ----- |
for at least one year
| © Veracode 2026. All rights reserved. |     |     |     |     |     |     | 7   |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Effective prioritization allows
teams to focus on remediating the
most critical vulnerabilities first,
ensuring risk is minimized even
when resources are constrained.
The security debt crisis has reached an What makes this trend particularly concerning
inflection point. While 2025 celebrated a is the shift in critical security debt. The 20%
decade of progress in reducing flaw prevalence relative increase in organizations carrying high-
and improving Open Web Application Security severity, long-unresolved flaws suggests that
Project (OWASP) Top 10 pass rates in first- teams are increasingly forced to accept the risk
party code apps, 2026 confronts us with a or defer dangerous vulnerabilities, not because
sobering reality: the backlog is growing faster they’re low priority, but because capacity
than remediation capacity can eliminate it. constraints make comprehensive remediation
This represents more than a statistical blip. too challenging for most organizations.
It signals a fundamental mismatch between
the pace of software development, the Later in the report, in Figure 6, we see a 4%
complexity of modern applications, and the YoY decrease in the half-life of flaws (meaning
available resources for security remediation. we’re getting faster at fixing them), but it’s
still not enough to take on the number of flaws
The story behind these numbers reveals three being introduced. This is why prioritization
intersecting pressures. First, organizations must become a core focus for modern
are discovering more vulnerabilities as their development teams. Effective prioritization
testing programs mature and expand across allows teams to focus on remediating the
Static Application Security Testing (SAST), most critical vulnerabilities first, ensuring
Dynamic Application Security Testing (DAST), risk is minimized even when resources are
and Software Composition Analysis (SCA) constrained. By leveraging tools that provide
modalities. Second, the accelerating pace of context on vulnerability severity, exploitability,
software releases we see in DevOps and CI/ and business impact, organizations can
CD practices creates a continuous influx of make informed decisions about which
new code before existing vulnerabilities can issues to address immediately, and which
be addressed. Third, the growing technical can be scheduled for later remediation or a
complexity of applications, particularly those decision can be made not to remediate at all.
incorporating AI-generated code and extensive This approach not only mitigates risk more
third-party dependencies, makes remediation effectively, it also helps maintain a balance
more complex and resource-intensive. between security and development velocity.
© Veracode 2026. All rights reserved. 8

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Understanding which applications constitute By leveraging AI-driven solutions, organizations
your organization’s “crown jewels” is a critical can expedite the remediation process while
component of effective prioritization. These streamlining prioritization efforts. AI not only
are the systems and applications that hold helps identify vulnerabilities faster but also
the most significant value to your business – pinpoints the “crown jewels,” enabling teams
whether due to the sensitive data they process, to focus their efforts where it matters most.
their role in delivering core services, or their Additionally, AI can provide actionable insights
impact on overall operations. Prioritizing the and automated fixes tailored to an application’s
remediation of critical security debt within environment and criticality, significantly
these key assets ensures that your security reducing the manual workload for development
efforts are focused where they matter most. and security teams. Beyond remediation,
AI-driven solutions also play a pivotal role
in managing compliance by continuously
monitoring and aligning security practices
with regulatory requirements. This holistic
approach allows organizations to efficiently
AI not only helps identify vulnerabilities
reinforce their most important defenses while
faster but also pinpoints the “crown
ensuring adherence to compliance standards.
jewels,” enabling teams to focus their
efforts where it matters most.
© Veracode 2026. All rights reserved. 9

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
CHAPTER 2
The
High-Risk
Vulnerability Surge
© Veracode 2026. All rights reserved. 10

Vulnerabilities rated as both highly severe and highly exploitable—
the ‘high-risk region’—have increased by a relative 36%, representing
a concerning concentration of dangerous, weaponizable flaws.
Key Point
High-Risk Region Growth:
36%
relative increase in flaws with both high exploitability AND high severity (from 8.3% to 11.3%)
FIGURE 3
Breakdown of flaws
according to severity
LOW MEDIUM HIGH VERY HIGH
and exploitability
22.6% 57.8% 14.9% 4.6%
VERY LIKELY 22.2% 0.9% 11.3% 8.4% 1.5%
High risk
region
totaling
LIKELY 35.3% 1.2% 32.6% 1.1% 0.3%
11.3%
NEUTRAL 33.8% 13.7% 12.0% 5.3% 2.8%
UNLIKELY 8.6% 6.7% 1.8% 0.1% 0.0%
VERY UNLIKELY 0.1% 0.1% 0.0% 0.0% 0.0%
The 36% surge in high-risk vulnerabilities traditional scanning tools readily detect as
since 2025 represents one of 2026’s most high-severity issues. For example, a cross-site
critical findings, fundamentally challenging Scripting (XSS) attack can lead to severe data
the narrative of steady security improvement. breaches, and in 86% of tests, AI-generated
The concentration of flaws in the dangerous code failed security tests for XSS, according
intersection of high severity and high to the 2025 GenAI Code Security Report.
exploitability has accelerated dramatically.
There aren’t just more vulnerabilities; Meanwhile, the expanding attack surface
there’s more risk from vulnerabilities created by microservices architectures,
with real-world attack potential. Application Programming Interface
(API) proliferation, and cloud-native
This trend likely reflects the convergence applications creates more opportunities
of several market forces. The proliferation for exploitation, even as organizations
of AI-assisted code generation tools may improve their basic security hygiene.
be introducing security flaws that many
ytilibatiolpxE
2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Severity
© Veracode 2026. All rights reserved. 11

Proportion of Apps Affected by Critical Flaws
On the bright side, we see a favorable trend Fewer apps with high-severity flaws
in the number of applications affected by reiterates the importance of knowing which
these critical flaws. While there was a 36% applications are your prized possessions and
relative increase in flaws with both high then prioritizing their protection within your
exploitability AND high severity, the proportion security strategy. Identifying these critical
of applications affected by these critical flaws assets allows teams to allocate resources
decreased. We see this in the density of the effectively, focusing on remediation efforts
bars in Figure 4 shifting left from 2025 to 2026. that reduce organizational risk with the highest
impact. Furthermore, incorporating real-time
alerts and automated remediation processes
can enhance responsiveness and ensure that
vulnerabilities are addressed promptly.
FIGURE 4
High-severity flaw 2026 2025
prevalence among
5%
organizations
4%
3%
2%
1%
0%
10% 20% 30% 40% 50% 60% 70% 80% 90%
Proportion of applications with critical flaws
snoitazinagrO
fo
egatnecreP
2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
© Veracode 2026. All rights reserved. 12

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
CHAPTER 3
Modest Progress
in Detection,
Struggles
in Remediation
© Veracode 2026. All rights reserved. 13

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Organizations continue to improve their ability to find vulnerabilities
and introduce fewer flaws (overall flaw prevalence down from
80% to 78%), but remediation timelines show only incremental
improvement and fix capacity remains constrained.
Key Points
|     | Overall Flaw Prevalence in Apps  |     | OWASP Top 10 Failure Rate:     |     |     |     |
| --- | -------------------------------- | --- | ------------------------------ | --- | --- | --- |
|     | Across All Scan Types:           |     |                                |     | 50% |     |
|     |                                  |     | Increased from 48% failing to  |     |     |     |
78%
Decreased to   (down from  failing (a +4% YoY increase in failing apps)
80%, a -3% YoY improvement)
FIGURE 5
YoY %
| Percent of         |     |      |     |     | change |     |
| ------------------ | --- | ---- | --- | --- | ------ | --- |
| applications with  |     | 2026 |     | 78% |        |     |
-3%
| security flaws across  | ANY FLAWS    | 2025 |     | 80% |     |     |
| ---------------------- | ------------ | ---- | --- | --- | --- | --- |
| all scan types         |              |      | 50% |     |     |     |
|                        | OWASP TOP 10 |      |     |     | +4% |     |
48%
38%
|     | CWE TOP 25 |     |     |     | -3% |     |
| --- | ---------- | --- | --- | --- | --- | --- |
39%
|     |     |     | 51% |     | -9% |     |
| --- | --- | --- | --- | --- | --- | --- |
HIGH SEVERITY
56%
Fix Speed (Half-Life) Across All Scan Types:
243 days
 (down from 252 days, a -4% YoY  improvement)
FIGURE 6
Overall flaw
remediation
timeline of all scan
80%
types based on
| survival analysis |     | HALFLIFE  |     |     |     |     |
| ----------------- | --- | --------- | --- | --- | --- | --- |
OF 243 DAYS
nepo llits swafl fo egatnecreP
60%
About 42% of overall flaws
turn into security debt
40%
About 28% of overall flaws
extend beyond two years
Just 10% of overall flaws
|     | 20% |     |     |     | extend beyond five years |     |
| --- | --- | --- | --- | --- | ------------------------ | --- |
|     | 0   | 1   | 2   | 3   | 4                        | 5   |
 Age of open flaws (years)
| © Veracode 2026. All rights reserved. |     |     |     |     |     | 14  |
| ------------------------------------- | --- | --- | --- | --- | --- | --- |

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Monthly Fix Capacity:
16.2%
Top performers at of flaws (down slightly from 16.5%)
FIGURE 7
Average monthly APPLICATIONS PCT OF APPS AT OR BELOW CAPACITY
fix capacity across
applications
12k 100%
16.2% of flaws
10k 80%
10.6% of flaws
7.7% of flaws
7.5k 60%
5.8% of flaws
4.4% of flaws
5k 40%
3.3% of flaws
2.0% of flaws
2.5k 20%
0.9% of flaws
0.0% of flaws
0 0
0% 10% 20% 30% 40% 50% 60% 70% 80% 90%100% 0% 30% 60% 90%
Average monthly capacity Average monthly capacity
The 2026 data tells a story of incremental The math is unforgiving. If you’re finding
progress shadowed by persistent structural flaws faster than you’re fixing them, and
challenges. On detection, organizations are your fix capacity remains essentially
winning: flaw prevalence across all scan types flat (currently hovering around 10% of
continues its multi-year downward trajectory flaws monthly for median organizations),
and fix speed has improved by 4%, too. This the backlog inevitably grows.
reflects maturing AppSec programs, better
secure coding practices, expanded use of While we’re optimistic that AI-generated
automated testing, and likely the positive fixes are a potential solution to reverse the
impact of security training programs. tide, when we combine the high-severity
flaw surge in Chapter 2 with the current
Yet this improvement masks a profound rates of remediation, we can conclude that
prioritization and remediation failure. We prioritization is key. Teams won’t reduce more
see a 4% YoY increase in applications that risk by getting faster at fixing the low-severity,
have flaws ranked in the OWASP Top 10 as unlikely-to-be-exploited flaws. Organizations
the 10 most critical risks to applications need to focus on fixing the most critical and
(Figure 5). And while fix speed improved (by exploitable flaws in the most critical, “crown
just 9 days, from 252 to 243 days for half- jewel” applications. And where does most of
life), this rate pales against the mounting the critical debt reside—in first-party or third-
volume of vulnerabilities discovered. party code? That brings us to the next chapter.
© Veracode 2026. All rights reserved. 15

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
CHAPTER 4
The Persistent
Third-Party Supply
Chain Challenge
© Veracode 2026. All rights reserved. 16

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
While third-party code shows slight improvement in overall security
debt contribution, it continues to dominate critical security debt,
representing 66% of the most dangerous, long-lived vulnerabilities.
And since critical security debt rose a relative 20%, that slight
decrease is a modest step in the right direction but not nearly enough
to mitigate long-term risks associated with third-party code usage.
Key Points
|     | Third-Party Critical Debt: | Third-Party All Security Debt:  |                           |     |     |
| --- | -------------------------- | ------------------------------- | ------------------------- | --- | --- |
|     | 66%                        | 9%                              |                           |     |     |
|     |  (down from 70%, a         |                                 |  (down from 11%, an -18%  |     |     |
|     | -6% YoY improvement)       | YoY improvement)                |                           |     |     |
FIGURE 8
| Proportion of security  |      Third party code  | First party code |     |     |     |
| ----------------------- | ---------------------- | ---------------- | --- | --- | --- |
debt and critical
|     |     | 9.3% |     |     | 90.7% |
| --- | --- | ---- | --- | --- | ----- |
debt in first-party
| vs. third-party code | ALL SECURITY DEBT |     |       |     |       |
| -------------------- | ----------------- | --- | ----- | --- | ----- |
| Percentage of flaws  |                   |     | 65.5% |     | 34.5% |
CRITICAL SECURITY DEBT
Applications with First-Party Flaws:   Applications with Third-Party Flaws:
|     | 63% | 62% |     |     |     |
| --- | --- | --- | --- | --- | --- |
 have flaws in first-party code    have open-source vulnerabilities
(down from 64%, a -1.6% YoY improvement) (down from 70%, a -11% YoY improvement)
FIGURE 9
Prevalence of flaws
in first-party (left)
vs. third-party
| (right) code among  | 64 % | 63 % | 70 % | 62 % |     |
| ------------------- | ---- | ---- | ---- | ---- | --- |
applications
Percentage of flaws
|                                       |      | -1.6   |      | -11    |     |
| ------------------------------------- | ---- | ------ | ---- | ------ | --- |
|                                       | 2025 | % 2026 | 2025 | % 2026 |     |
| © Veracode 2026. All rights reserved. |      |        |      |        | 17  |

Remediation Half-Life for Third-Party Flaws:
358 days
FIGURE 10
Overall flaw
remediation
timeline based on
80%
survival analysis
for SCA findings HALFLIFE
OF 358 DAYS
60%
About 49% of overall flaws
turn into security debt
40% About 31% of overall flaws
extend beyond two years
Just 8% of overall flaws
20% extend beyond five years
0 1 2 3 4 5
The third-party security challenge presents Additionally, the proportion of applications
one of 2026’s most nuanced stories; it’s a containing third-party vulnerabilities decreased
tale of modest improvement overshadowed by a relative 11%, falling from 70% to 62% of
by persistent structural concerns. The applications. We are pleased to report that
decline in third-party critical debt from this reduction indicates an improved security
70% to 66% represents real progress, posture in open-source integration—especially
suggesting organizations are getting better at on the application level, which indicates
dependency hygiene, vulnerability scanning people may be taking supply chain action
in the software supply chain, and potentially focused on their “crown jewel” applications.
adopting package manager firewalls and
Software Bill of Materials (SBOM) practices.
nepo
llits
swafl
fo
egatnecreP
2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Age of open flaws (years)
© Veracode 2026. All rights reserved. 18

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
However, despite these gains, organizations Reliance on open-source libraries and
still face significant challenges when other third-party components introduces
addressing third-party code vulnerabilities. dependencies that, while accelerating
The half-life of third-party flaws found using development, often remain unchecked for
SCA is 358 days (Figure 10); that’s 115 days vulnerabilities over time. This lack of visibility
longer than the average of all scan types and accountability poses a significant
(Figure 6). That’s almost four months longer! challenge for organizations striving to
maintain secure software. The difficulty
One of the key hurdles to remediating of managing transitive dependencies
vulnerabilities in the supply chain is the exacerbates this issue, as teams must
complexity of these chains. This complexity navigate the delicate balance between fixing
is further compounded by the nature of vulnerabilities and preserving functionality.
open-source flaws, which come in two types
of dependencies: direct and transitive. To address this issue, organizations must
Direct dependencies, where a configuration prioritize strategies that include rigorous
file references a library, are relatively dependency management, frequent updates to
straightforward to fix. However, transitive third-party libraries, and proactive vulnerability
dependencies—where direct dependencies scanning. Leveraging tools that integrate
rely on other libraries—are far more seamlessly into CI/CD pipelines can help
challenging. Fixing transitive dependencies automate this process, ensuring that outdated
can risk breaking functionality in the direct or vulnerable components are identified and
library, often requiring code refactoring and remediated efficiently. Additionally, educating
significantly slowing the remediation process. development teams on the importance of
securing third-party code and adopting a
Organizations must prioritize strategies that include “shift-left” approach to security can foster
a culture of proactive risk mitigation.
rigorous dependency management, frequent updates
to third-party libraries, and proactive vulnerability
scanning. Leveraging tools that integrate seamlessly
into CI/CD pipelines can help automate this process.
© Veracode 2026. All rights reserved. 19

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
CHAPTER 5
The AI Era’s
Double-Edged
Impact
© Veracode 2026. All rights reserved. 20

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Though not explicitly measured in the data, it would be remiss not to
discuss AI’s expanding role in software development. AI presents us
with a double-edged sword: simultaneously creating new vulnerability
patterns and offering potential solutions for remediation at scale.
While it would be convenient for code On the other hand, the rapid adoption of
generated by AI to be tagged as such, that’s not AI also introduces new attack vectors
the reality we live in. While the 2026 analysis and raises concerns about the integrity of
doesn’t provide definitive AI impact metrics, generated code. For instance, malicious
the data patterns and analyst questions reveal actors can exploit vulnerabilities in AI-
growing awareness that AI represents the wild generated outputs or manipulate models
card reshaping software security dynamics. through adversarial attacks. There’s also risk
The 2025 SoSS report noted that ‘while many from attackers finding your latent unfixed
teams may not openly admit to using AI, vulnerabilities with AI penetration tools.
other indicators of its presence and impact Furthermore, reliance on AI tooling without
can be found’. 2026 trends suggest those proper oversight may yield inaccurate results,
indicators are becoming harder to ignore. such as false positives or missed threats,
potentially undermining developer trust.
AI’s rising integration into software To truly harness the potential of AI while
development processes has redefined both mitigating risks, organizations must establish
the opportunities and challenges faced by clear governance strategies, implement
AppSec teams. On one hand, AI-driven tools transparent model training processes, and
can enhance vulnerability detection, real- ensure human oversight remains a core element
time code analysis, and even automated of AI integration in security workflows.
remediation workflows. These advancements
enable organizations to address security risks
faster than ever, improving team efficiency
and reducing the likelihood of overlooked
flaws. AI models can analyze vast amounts
of code and identify patterns, allowing for a
proactive approach in mitigating risks early
within the software development lifecycle.
© Veracode 2026. All rights reserved. 21

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Comparitive
Analysis:
Key Shifts from
2025 to 2026
© Veracode 2026. All rights reserved. 22

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Consistencies
What Stayed the Same and Why It Matters
1
The Fundamental 78% of applications still contain Why It Matters:
flaws (78% in 2026 vs 80% in 2025), Despite technological advances
Challenge Persists
third-party code continues to drive and increased awareness, the
critical security debt (over 65% basic challenge of software
range maintained), and remediation security—ubiquitous vulnerabilities
capacity remained on par. and constrained remediation—
remains unchanged, leading to
mounting security debt, validating
the need for sustained focus.
2
Incremental Progress Flaw prevalence metrics continued Why It Matters:
trending positively year-over-year. The multi-year pattern of detection
Continues on Detection
improvement validates that secure
coding practices, training, and
automated testing are working—
the problem is remediation
capacity, not awareness.
© Veracode 2026. All rights reserved. 23

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Evolutions and Shifts
What Changed and What It Means
1
Security Debt Crisis From 74% of organizations Driver: Detection outpacing
with security debt (2025) to remediation capacity; DevOps velocity;
Accelerates (+11%
82% of organizations with application complexity.
organizational prevalence)
security debt (2026). Implication: The remediation gap
has reached crisis proportions;
incremental improvements insufficient;
transformational change required.
2
High-Risk Vulnerabilities From 8.3% of vulnerabilities Driver: Likely supply chain related;
concentrated in the high-severity expanding attack surfaces; remediation
Surge (+36%)
+ high-exploitability category not focused on severe flaws.
in 2025 to 11.3% in 2026. Implication: Prioritization frameworks
must urgently shift to exploitability-
weighted risk, not just severity;
traditional CVSS scoring is insufficient.
3
Application Security From 42% of applications Driver: Accumulation outpacing
carrying security debt (2025) elimination; long tail of hard-to-
Debt Grows (+17%)
to 49% of applications carrying remediate flaws; resource constraints.
security debt (2026). Implication: Nearly half of all
applications are now burdened
with year-old+ vulnerabilities,
representing massive attack
surface and technical debt.
© Veracode 2026. All rights reserved. 24

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Actionable Insights
and
Recommendations
© Veracode 2026. All rights reserved. 25

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
For Organizations with High Security Debt
(>50% of apps)
1
| Emergency Triage   | Immediately implement risk-       | Target:                           |
| ------------------ | --------------------------------- | --------------------------------- |
|                    | based prioritization focusing on  | Reduce critical security debt by  |
Protocol
|     | high-exploitability + high-severity  | 25% in 180 days through focused  |
| --- | ------------------------------------ | -------------------------------- |
|     | intersection. Use ASPM solutions to  | elimination of high-risk flaws.  |
correlate findings across tools and
add runtime/business context.
2
| AI-Assisted   | Deploy AI remediation tools for  | Target:  |
| ------------- | -------------------------------- | -------- |
Remediation Pilot  the ‘long tail’ of simple, repetitive  Increase monthly fix capacity from
|     | vulnerabilities. Allocate 10-15%  | <5% to >10% within two quarters. |
| --- | --------------------------------- | -------------------------------- |
of sprint capacity specifically to
security debt reduction using AI-
generated fixes with human review.
3
| Dependency   | Implement package manager firewalls  | Target:                      |
| ------------ | ------------------------------------ | ---------------------------- |
|              | to prevent vulnerable dependencies   | Reduce third-party critical  |
Management Overhaul
|     | entering the codebase. Establish  | debt contribution from 65%+  |
| --- | --------------------------------- | ---------------------------- |
|     | dependency review process with    | to <50% within one year.     |
security-weighted evaluation.
© Veracode 2026. All rights reserved. 26

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
For Organizations with
Growing Application Portfolios
1
Shift Left on Remediation Integrate automated fix suggestions Target:
directly into integrated development Prevent net new security debt in
environments (IDEs) workflows. a way that’s prioritized; keep debt
Implement ‘fix before close’ policies for prevalence at <20% of applications.
high-risk vulnerabilities in new code.
2
Security Champion Deploy security training focused Target:
on common vulnerability patterns Achieve fix half-lives of <90 days
Enablement
in AI-generated code. Establish for critical vulnerabilities.
dedicated sprint points (15-20%)
for security debt reduction.
For Technology Leaders
and Executives
1
Resource Reallocation Recognize remediation capacity Target:
as a strategic constraint worthy of Double fix capacity through tooling
investment. Allocate budget for AI- investment, not just headcount.
assisted remediation tools, ASPM
platforms, and security automation.
2
Metrics and Accountability Make security debt a board-level key Target:
performance indicator (KPI) alongside Organizational security debt
technical debt and SRE metrics. Tie is decreasing quarterly, with
security outcomes to development top-quartile performance
team Objectives and Key Results expected within 18 months.
(OKRs) and performance reviews.
© Veracode 2026. All rights reserved. 27

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
The
Path Forward
© Veracode 2026. All rights reserved. 28

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
The 2026 findings expose a glaring The themes analyzed here—debt
contradiction: improved detection masking intensification, high-risk vulnerability surge,
a remediation crisis, incremental gains detection-remediation gap, persistent
overshadowed by systemic debt accumulation, supply chain challenges, and AI’s double-
and pockets of excellence coexisting with edged impact—form a tale of transformation
widespread struggle. This isn’t a story of failure. imperative. Organizations have spent the last
It’s a story of transition, of an industry grappling decade learning to find vulnerabilities. The
with the implications of AI-accelerated next decade must be about learning to fix
development, cloud-native complexity, and the them in a prioritized way while simultaneously
unforgiving mathematics of finite remediation preventing their introduction in the first place.
capacity confronting an infinite attack surface.
The path is clear, the tools are available, and the examples exist. What remains to
prevail in 2026 and beyond is to adopt the “Protect, Prioritize, Prove” strategy:
Prioritize
Find Clarity in the Chaos by Knowing What You Have & What Matters Most
The pursuit of fixing every flaw is a race
Key questions to answer:
that cannot be won. Instead, organizations
must prioritize their efforts. This starts with • What apps do I have?
identifying your “crown jewel applications”:
• How many are there and
the applications and assets most critical
what do they do?
to your business operations with the most
• Which are public-facing vs. internal?
material impact. By concentrating security
resources on these critical areas and targeting • Which handle sensitive
the most severe, exploitable vulnerabilities, data, models, or IP?
you maximize impact where it matters most.
• What’s my AI attack surface?
Prioritization is about visibility and risk ranking,
because you can’t protect everything equally.
© Veracode 2026. All rights reserved. 29

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Protect
Enable Automation and Embrace DevSecOps to Secure Apps Continuously
With priorities in place, protection must
Key questions to answer:
become a strategic, continuous process
• What’s in my apps? How do I automate
focused on active risk reduction. Automation
knowing this continuously?
and DevSecOps practices are key to building
scalable, efficient defenses. By integrating • Where are the vulnerabilities—
security into the development lifecycle in models, data, prompts,
and automating vulnerability detection and pipelines, dependencies?
response, you reduce human error and keep
• How do I fix the risks in there at scale?
pace with the rapidly evolving threat landscape.
This ensures your critical applications remain
secure as they grow, adapt, and interact within
an ever-expanding software supply chain.
Prove
Software Assurance, Compliance, & Due Diligence
To prevail is to move beyond reacting to Transparency becomes a strategic
threats and toward assuring that your software advantage: verifiable evidence of compliance
and systems operate within a consistently reassures regulators, customers, and
compliant environment. Proving is not just stakeholders that security is not ad hoc, but
about preventing recurrence; it’s about systematically governed and enforced.
demonstrating, with evidence, that your
organization adheres to recognized security
Key questions to answer:
frameworks and regulatory requirements.
• How do I ensure my software and
Software assurance provides the foundation for
environments continuously meet
this proof by ensuring controls are designed,
required security frameworks
implemented, and continuously validated across
and regulatory standards?
the development and operational lifecycle.
A mature security posture makes • How can I provide clear, auditable
compliance measurable, repeatable, evidence that compliance
and defensible. By aligning security and assurance controls are
practices to established frameworks and operating effectively?
regulatory mandates, organizations can
clearly demonstrate reasonable care, audit
readiness, and operational discipline.
© Veracode 2026. All rights reserved. 30

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Taking control of your security landscape begins with a structured
approach that empowers teams and builds resilient systems. By
embedding proactive security measures into your workflows, you
not only meet compliance demands but also create a foundation for
innovation and trust. It’s time to turn challenges into opportunities
with a solution tailored to your organization’s evolving needs.
Start your security transformation today. Schedule a demo to
discover why organizations trust Veracode to reduce vulnerabilities,
enhance efficiency, and achieve compliance with confidence.
© Veracode 2026. All rights reserved. 31

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Methodology
The report contains findings about applications that were subjected to static analysis, dynamic
analysis, software composition analysis, and/or manual penetration testing through Veracode’s
cloud-based platform. Specifically, the data in this year’s report comes from:
• 1.6M unique applications with 141.3M raw findings
• 115.6M raw static findings
• 3.6M raw dynamic findings
• 22.1M raw SCA findings
This data represents companies of all sizes, commercial software suppliers, software outsourcers,
and open-source projects. In most analyses, an application was counted only once, even if it was
submitted multiple times as vulnerabilities were remediated and new versions were uploaded. For
software composition analysis, each application is examined for third-party library information and
dependencies. These are generally collected through the application’s build system. Any library
dependencies are checked against a database of known flaws.
The OWASP Top 10 was updated in November 2025 with minor changes. We used the prior version
(2021) of the OWASP Top 10 for this analysis.
A Note on Mass Closures
While preparing the data for our analysis, we noticed several large single-day closure events. While
it’s not strange for a scan to discover that dozens, or even hundreds, of findings have been fixed
(50% of scans closed fewer than 2 findings), we did find it strange to see some applications closing
thousands of findings in a single scan. Upon further exploration, we found many of these to be
invalid. These large collections of flaws were both added and removed in single scans: Developers
would scan entire filesystems, invalid branches, or previous branches, and when they would rescan
the valid code, every finding not found again would be marked as “fixed.”
These mistakes had a large effect: The top 0.01% accounted for over 1 out of 10 of all the closed
findings. These “mass closure” events have significant effects on measuring flaw persistence and
time to remediation and were ultimately excluded from the analysis.
© Veracode 2026. All rights reserved. 32

2026 STATE OF SOFTWARE SECURITY: PRIORITIZE, PROTECT, PROVE
Appendix
This report would not have been possible without the invaluable contributions of several individuals
and organizations. We extend our deepest gratitude to:
• David Severski and Wade Baker of the Cyentia Institute for their exceptional expertise in data
analysis and statistical modeling, which provided the foundation for the insights presented in
this report.
• Natalie Tischler and Joe Ariganello for their outstanding efforts in authoring and shaping the
narrative of this report.
• Karen Buffo, Niels Tanis, Chris Wysopal, Jens Wessling, Sohail Iqbal, and Katy Gwilliam
for their ideation on the right questions to ask, meticulous review and thoughtful feedback,
ensuring the accuracy, clarity, and impact of the findings.
Your dedication and expertise have been instrumental in delivering the 2026 State of Software
Security report. Thank you for your contributions to advancing the field of application security.
About Veracode
Veracode is a global leader in Application Risk Management for the AI era. Powered by
trillions of lines of code scans and a proprietary AI-assisted remediation engine, the Veracode
platform is trusted by organizations worldwide to build and maintain secure software from
code creation to cloud deployment. Thousands of the world’s leading development and
security teams use Veracode every second of every day to get accurate, actionable visibility
of exploitable risk, achieve real-time vulnerability remediation, and reduce their security
debt at scale. Veracode is a multi-award-winning company offering capabilities to secure
the entire software development life cycle, including Veracode Fix, Static Analysis, Dynamic
Analysis, Software Composition Analysis, Container Security, Application Security Posture
Management, Malicious Package Detection, Package Manager, and Penetration Testing.
Learn more at www.veracode.com, on the Veracode blog, and on LinkedIn and X.
© Veracode 2026. All rights reserved. 33

Copyright © 2026 Veracode, Inc. All rights reserved. Veracode is a registered
trademark of Veracode, Inc. in the United States and may be registered in certain
other jurisdictions. All other product names, brands or logos belong to their respective
holders. All other trademarks cited herein are property of their respective owners.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-23", "model": "gemini-3.5-flash-lite"} -->
