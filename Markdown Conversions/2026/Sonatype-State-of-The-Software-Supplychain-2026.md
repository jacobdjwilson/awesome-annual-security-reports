# State-of-The-Software-Supplychain

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [Registries, Models, and the New Software Infrastructure Burden: When Growth Meets Gravity](#registries-models-and-the-new-software-infrastructure-burden-when-growth-meets-gravity)
- [The Evolving Software Supply Chain Attack Surface: Malware at The Gate](#the-evolving-software-supply-chain-attack-surface-malware-at-the-gate)
- [The Three Layers of Failure in Modern Vulnerability Management](#the-three-layers-of-failure-in-modern-vulnerability-management)

---

## Foreword

For most of my career, open source has run on a simple premise: shared building blocks make everyone faster. That is still true. What is not optional anymore is everything that comes with running that premise at a global, automated scale.

Open source is now the substrate of software delivery, pulled continuously by pipelines and rebuilt across fleets that rarely stop. At machine speed, small inefficiencies and small risks do not stay small. “Just one more build” becomes billions of requests, and then everyone acts surprised when the infrastructure starts to groan.

You see it again in the security reality. Attackers target open source because it is the fastest path to developers, and developers sit closest to credentials, tokens, and build systems. Malware is steady pressure on ecosystems designed for openness. At the same time, public vulnerability intelligence is too often incomplete, late, or wrong, which turns prioritization into guesswork. That’s not a tooling problem. It’s a signal problem.

And now AI is entering the loop. It can accelerate good engineering, but it can also scale mistakes when it’s operating from static training data instead of live reality. When a model doesn’t know what versions exist or what is newly risky, it predicts and fills in the blank. That’s how you end up with confident “upgrades” to versions that don’t exist and recommendations that look plausible right up until they break your build or your policy. AI should not guess. AI-driven velocity will overwhelm any governance model built on “we’ll review it later.”

You’ll see it first in the operational reality of the commons. The same CI/CD patterns that make teams productive can generate massive redundant load when caches are cold, runners are ephemeral, or pipelines are effectively configured to re-download the world. If your build environment forgets what it did last run, the ecosystem still pays the cost.

This report is about what happens when trust becomes a scaling problem. The takeaway isn’t that open source is unsafe or that teams should slow down. It is that the ecosystem has matured into critical infrastructure and we need to operate it like one. That means responsible consumption, security controls that match modern development, and transparency that is produced by the build, not assembled after the fact. Regulations and buyers are moving there because the world is demanding evidence, not assurances.

Open source will keep powering innovation. The question is whether we build the practices and infrastructure to sustain it at the scale we now depend on, or whether we keep acting like the bill is someone else’s problem.

> AI CAN ACCELERATE GOOD ENGINEERING, BUT IT CAN ALSO SCALE MISTAKES WHEN IT’S OPERATING FROM STATIC TRAINING DATA INSTEAD OF LIVE REALITY. GUARDRAILS FOR AI ARE NO LONGER A NICE-TO-HAVE.

**Brian Fox**
Co-founder and CTO, Sonatype

---

## Executive Summary

Software supply chains have hit machine scale. In 2025, the world did not just build more software. It reused more of it, more often. That scale is bending the ecosystem in predictable ways. Open source registries, now largely serving as the internet’s critical infrastructure, are under sustained strain. Synthetic traffic and redundant downloads inflate the commons, and attackers increasingly treat open source as a delivery channel, not an afterthought.

> IN 2025, THE WORLD DID NOT JUST BUILD MORE SOFTWARE. IT REUSED MORE OF IT, MORE OFTEN.

### The Key Takeaways

- **1,233,219**: Open source malware packages logged by Sonatype since 2019.
- **9.8 Trillion**: Downloads across Maven Central, PyPI, npm, and NuGet.
- **27.76%**: Recommended dependency upgrade hallucination rate observed with leading LLM.
- **65%**: Of open source CVEs were left without CVSS by the NVD.

Vulnerability intelligence is getting noisier and less complete just as teams need it to be faster. AI-assisted development is also introducing a new class of risk — automation can amplify bad inputs at machine speed. Against a backdrop of accelerating regulatory mandates for transparency, the message of this report is simple:

> TRUST AT SCALE IS NOW THE CENTRAL ENGINEERING AND BUSINESS CHALLENGE OF MODERN SOFTWARE.

---

## Registries, Models, and the New Software Infrastructure Burden: When Growth Meets Gravity

### Open Source Scale Has Become a Structural Risk

Open source has entered an era where scale itself has become a structural risk. Package registries that once measured growth in millions of downloads now routinely serve trillions of requests. But this growth does not map cleanly to innovation. 2025 saw 9.8 trillion downloads across Maven Central, PyPI, npm and NuGet, but the majority of registry traffic today is not driven by new applications or meaningful reuse. It’s driven by transitive dependency sprawl, unused or abandoned packages, and unsustainable tooling patterns.

![Yearly Downloads over Time chart]

Modern CI/CD systems and ML pipelines are optimized for speed and convenience, not efficiency. Once configured, they pull relentlessly, often blind to redundancy, cost, or downstream impact. The result is a structural burden that registries were never designed to carry alone.

---

## The Evolving Software Supply Chain Attack Surface: Malware at The Gate

### A Turning Point for Open Source Malware

Throughout 2025, Sonatype identified more than 454,600 new malicious packages, bringing the cumulative total of known and blocked malware to over 1.233 million packages across npm, PyPI, Maven Central, NuGet, and Hugging Face. This year, we observed that the evolution of open source malware crystallized, evolving from spam and stunts into sustained, industrialized campaigns against the people and tooling that build software.

![Annual Open Source Malware Growth chart]

This year, over 99% of open source malware occurred on npm. State-linked entities such as the Lazarus Group advanced from simple droppers and crypto miners to five-stage payload chains that combined droppers, credential theft, and persistent remote access inside developer environments.

---

## The Three Layers of Failure in Modern Vulnerability Management

### The Limits of Modern Vulnerability Management

Modern vulnerability management is struggling to keep up with the rapid evolution of the software it aims to protect. It’s not a single tool, team, or workflow that’s failing, but the entire system that allows open source vulnerabilities to exist.

Despite major investment in scanning tools, disclosure pipelines, and security automation, organizations continue to operate with blind spots large enough for systemic risk to take root. Our analysis shows this failure compounds across three breakpoints in the software ecosystem:

1. **The Data Layer**: Incomplete, inaccurate, and delayed public vulnerability intelligence.
2. **The Consumption Layer**: Developers, AI, and pipelines keep pulling vulnerable components.
3. **The Ecosystem Layer**: Dependence on EOL and abandoned components locks in permanent risk.

This problem is accelerating. In just five years, the global CVE count has doubled, yet the number of unscored CVEs has increased 37×, overwhelming a system built for manual processing and slower software cycles. As volume grows, the gap widens — leaving defenders without the baseline CVE data they rely on to triage risk effectively.

[^1]: Sonatype Security Research, 2025.

---

ulnerabilities last year could
effectively be triaged. When Sonatype assigned
scores to these unscored CVEs, 46% were
actually High or Critical, meaning many serious
vulnerabilities enter the ecosystem without any
meaningful prioritization signal.

I N   2 0 2 5 ,  E N T E R P R I S E S   C O U L D   O N LY
T R I AG E   3 5 %   O F   V U L N E R A B I L I T I E S
I F   R E LY I N G   O N   P U B L I C   C V E   DATA .

33

2026 STATE OF THE SOFTWARE SUPPLY CHAIN1 IN 7

NVD-scored CVEs differ from
Sonatype by 3+ CVSS points

20,362

false positives identified
by Sonatype

167,286

false negatives identified
by Sonatype

Sonatype identified 20,362 false positives, or
packages incorrectly marked as vulnerable, creat-
ing noise in vulnerability management workflows
and wasting developer time, and 167,286 false
negatives, meaning exploitable components went
unflagged entirely. The result is a vulnerability
intelligence ecosystem that misleads both devel-
opers and security teams, forcing organizations
to spend time on issues that don’t exist while
overlooking those that do. Inaccurate data also
biases AI-driven tools, which use this information
to determine dependency selection, upgrade
paths, and remediation recommendations.

AC C U R ACY  FA I LU R E S

Even when scores exist, they’re inconsistent
enough to drive different outcomes depending
on which feed you trust. Compared to Sonatype
scoring and analysis, exact CVSS score matches
are rare (4.4%), and severity categories align only
55.7% of the time. This means 44% of CVEs land
in a different bucket in NVD versus Sonatype.
The direction of the drift is usually upward in
NVD: 61.3% of NVD scores are higher than Sona-
type, compared with 34.3% that are lower.

FIGURE 3.2
Severity Score and
Category Adjustments

80%

60%

40%

20%

0

Score

Category

61.3%

55.7%

33.4%

34.3%

4.4%

10.8%

NVD Higher

Same

NVD Lower

Sonatype Adjustment

34

THE THREE-LAYERS OF FAILURE2026 STATE OF THE SOFTWARE SUPPLY CHAINE V E N   M I N O R   M E TA DATA
I N AC C U R AC I E S   C R E AT E
O U T Z I D E D   R E A L- W O R L D
C O N S E Q U E N C E S :

•  Incorrect vulnerable version ranges

generated thousands of false positives,
overwhelming downstream scanners.

•  Wrong component identifiers resulted
in silent false negatives — packages
with real vulnerabilities passed security
checks unflagged.

•  EOL versions omitted from advisories
gave organizations a false sense of
security, masking risks that upstream
maintainers no longer track.

•  These cases reveal a systemic issue:
the CVE system excels at naming vul-
nerabilities, but struggles to describe
them reliably enough for automated
decision-making.

D E L AYS  T H AT  B R E A K   D E F E N S E S

In 2025, the NVD’s median time-to-score for
open source CVEs was 41 days, with some taking
up to a year. Meanwhile, exploit proof-of-con-
cepts and maintainer patches frequently appear
within hours. This growing lag renders “official”
vulnerability information increasingly stale. By
the time a CVE receives a severity score, the
vulnerability may already be exploited in the wild,
patched upstream, or both. Organizations relying
exclusively on NVD data become effectively blind
during the period when fast action matters most.

35%

took more than 3 months to
receive a complete NVD record

FIGURE 3.3
NVD Time-to-Analysis of
2025 Open Source CVEs

64.8%

46.4%

35.2%

16.6%

5.6%

≤48 hours <7 days <30 days <90 days ≥90 days

Timeframe

s
E
V
C
f
o
e
r
a
h
S
e
v
i
t
a
u
m
u
C

l

80%

60%

40%

20%

0

35

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

A I   A S   A   F O R C E   M U LT I P L I E R
F O R   B A D   DATA

AI-assisted development tools — increasingly
embedded across coding, build, and remedia-
tion workflows — amplify the weaknesses of the
data layer. Large language models are trained on
public CVE and NVD data and treat it as author-
itative even when it is incomplete, outdated,
or incorrect. This impact is compounded when
using an older model. As a result, AI does not fix
bad data, but rather distributes it faster, which
is examined closer in the From Guesswork to
Grounded chapter.

The data layer is the foundation of threat and
vulnerability management, yet today it is the
least reliable part of the system. Incomplete
coverage, inaccurate metadata, long scoring
delays, AI amplification, and shadow download
blind spots collectively undermine the ability of
organizations to recognize and respond to real
risk. When the data layer fails, every subsequent
decision — what to fix, when to fix it, and how to
prioritize it — begins from the wrong premise.

Poor Consumption Patterns
Sustain Avoidable Risk
Even when vulnerability data is accurate and
patches are readily available, risk persists
because of how organizations actually consume
open source. Dependency pinning, transitive
pull-ins, outdated build images, and AI-gener-
ated manifests all keep vulnerable components
in circulation long after fixes exist. In practice,
a large share of modern vulnerability exposure
is not created by new flaws — it is sustained by
repeated reuse of old ones.

36

LO G 4 S H E L L :  T H E   C A S E  T H AT
S H O U L D   H AV E   C H A N G E D
E V E R Y T H I N G   —   B U T  D I D N ’ T

Log4Shell was expected to be the turning point:
the moment the industry collectively learned to
upgrade quickly, retire vulnerable components,
and modernize dependency practices. Four years
later, the data tells a different story: the remedi-
ation path is well-understood and non-breaking,
the open source vulnerability is universally rec-
ognized, and yet vulnerable versions continue to
circulate at scale.

I N   2 0 2 5   A LO N E ,  D E V E LO P E R S
D O W N LOA D E D   M O R E  T H A N   42
M I L L I O N   V U L N E R A B L E   V E R S I O N S   O F
LO G 4 J,  R E P R E S E N T I N G  1 3 %   O F   A L L
LO G 4 J   D O W N LOA D S   W O R L D W I D E .

Regional patterns make the problem even clearer.
While some markets have driven vulnerable Log4j
usage down to single digits, others continue to
pull 20–45% vulnerable versions, suggesting
deeply uneven adoption of safe releases and
persistent reliance on outdated build tem-
plates, pinned versions, or ungoverned transitive
dependencies.

Log4Shell should have eliminated any doubt
about the cost of running outdated open source.
Instead, it revealed how ingrained consumption
habits can be — and how long vulnerable code
can persist, even when every incentive exists to
move away from it.

THE THREE-LAYERS OF FAILURE2026 STATE OF THE SOFTWARE SUPPLY CHAIN
T H E   B R OA D E R   PAT T E R N :   JAVA’ S
TO P   U N N E C E S S A R Y  R I S KS

Log4Shell remains the most visible example of
“avoidable” vulnerability exposure, but it is not
the dominant driver. Taking a broader look at the
Java ecosystem, Sonatype analyzed the most
frequently downloaded components that con-
tained a vulnerability, despite a fix for that vulner-
ability already existing. The same consumption
pattern repeats across the ecosystem: the vast
majority of vulnerable components being down-
loaded already have a safer version available. The
10th Annual State of the Software Supply Chain
Report found that roughly 95% of vulnerable
component downloads had a fix on the shelf,
while only ~0.5% represented true edge cases
with no upstream path forward.

The most concerning signal is how frequently
well-known vulnerable releases persist years
after fixes are released. The Java ecosystem

provides clear examples: widely used libraries
with long-available patches still see substantial
(and in some cases overwhelming) consumption
of vulnerable versions. This is “unnecessary risk”
in its purest form: risk that organizations con-
tinue to import into new builds even when safer
versions are readily available.

Sonatype took a closer look at four vulnerable
component versions with released fixes that,
combined, represent a total of nearly 1.8 billion
avoidable vulnerable downloads in 2025.

These packages share three characteristics: (1) at
least one disclosed vulnerability, (2) a published
fix, and (3) low adoption of the fixed line. The
reasons are rarely dramatic. They’re structural:
pinned versions copied across services, transitive
dependency blind spots, upgrade friction (espe-
cially across major versions), and selection signals
that reward familiarity over maintainability.

F O U R   V U L N E R A B L E   C O M P O N E N T  V E R S I O N S   W I T H   R E L E A S E D   F I X E S

Vulnerable
version(s) still
widely consumed

Fixed
version
available

Component

% of 2025 avoidable
vulnerable downloads

Representative
CVE(s)

Why it persists
(consumption drivers)

commons-
compress

1.21

1.26
(Feb 2024)

46.32%

CVE-2012-2098,
CVE-2024-26308,
CVE-2020-1945,
CVE-2024-25710,
CVE-2021-36374

Deeply embedded in build/packaging
workflows; low “visibility” dependency;
upgrades deferred unless forced.

commons-
lang

2.6
(legacy major line)

3.18.0
(Jul 2025)

snappy

0.4

jdom2

2.0.6

0.5
(May 2024)

2.0.6.1
(Dec 2021)

99.88%

CVE-2025-48924 Major-version migration is non-trivial

99.58%

CVE-2024-36124

57.73%

CVE-2021-33813

(2.x → 3.x); older enterprise stacks remain
pinned to legacy APIs.

Common in distributed platforms
(e.g., Hadoop/Spark ecosystems) where
low-level compression deps are pinned
for stability/performance.

Widely reused XML utility; upgrade iner-
tia and “if it isn’t broken” maintenance
norms keep vulnerable lines circulating.

37
37

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

2026 STATE OF THE SOFTWARE SUPPLY CHAINW H Y T E A M S   K E E P   D O W N LOA D I N G   O P E N   S O U R C E   V U L N E R A B I L I T I E S

If patches exist and the risks are well-known, why do vulnerable components continue to
flow into modern software at such scale? The answer lies not in malicious intent, but in
the quiet, structural habits of software development. Collectively, these patterns mean
vulnerable components remain in circulation, not because teams are unaware of the risk,
but because the system makes unsafe choices easier than safe ones.

T H E   S YS T E M   M A K E S   U N S A F E   C H O I C E S   E A S I E R  T H A N   S A F E   O N E S .

SET-AND-FORGET DEPENDENCIES
A version gets pinned once and then copied forward across
services for years.

THE RESULT:
Changing dependencies
feels risky; leaving them
alone feels “safe.”

TRANSITIVE DEPENDENCIES + UNCLEAR OWNERSHIP
Vulnerabilities arrive via the dependency tree, not direct installs.

TOOLING THAT SHRIEKS BUT DOESN’T STEER
Scanners generate long CVE lists without clear
prioritization or safe upgrade paths.

INCENTIVES FAVOR FEATURES OVER HYGIENE
Maintenance work is deferred unless there’s a fire drill.

38
38

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

THE RESULT:
No single team feels
accountable for buried
upgrades.

THE RESULT:
Teams hit alert fatigue
and avoid “break the
build” upgrades.

THE RESULT:
Delivery is rewarded;
dependency upkeep is
invisible..

THE THREE-LAYERS OF FAILURE2026 STATE OF THE SOFTWARE SUPPLY CHAINA I   E X AC E R B AT E S   V U L N E R A B L E
C O N S U M P T I O N

AI-assisted development tools are increasingly
embedded across modern software workflows —
from code generation and dependency selection
to build configuration and remediation guidance.
While these tools can accelerate delivery, they
also inherit and amplify the same consumption
patterns that already sustain vulnerability risk. AI
amplifies vulnerable consumption in several pre-
dictable ways:

1.

2.

3.

4.

AI suggests “popular” (historically common)
versions, not secure ones.

AI generates manifests with outdated/vul-
nerable components.

Training data lags, so even after fixes exist,
AI keeps suggesting vulnerable versions.

Without governance, AI increases compo-
nent sprawl.

AI does not introduce new vulnerability classes,
but it accelerates existing consumption behav-
ior. When unsafe versions are already easier to
consume than safe ones, AI makes those unsafe
choices faster, more repeatable, and harder to
unwind. Most vulnerability risk is no longer a vul-
nerability discovery problem. It’s a consumption
behavior problem, and AI scales that behavior
by default.

39

When the Ecosystem Stops
Maintaining Your Software
Even with accurate vulnerability intelligence
and disciplined dependency practices, some
risks cannot be mitigated because the software
itself is no longer maintained. A growing share
of open source components now lives on EOL,
or abandoned release lines, where no patches
will ever be issued and new open source vulner-
abilities may never be disclosed. These depen-
dencies create permanent exposure: organiza-
tions inherit flaws that cannot be remediated
upstream, locking long-term risk into the foun-
dation of their software.

To analyze how End-of-life (EOL) dependencies
turn vulnerabilities into persistent risk, we part-
nered with HeroDevs to examine the security
impact of EOL software across modern software
supply chains.

A I   D O E S   N OT  I N T R O D U C E
N E W   V U L N E R A B I L I T Y
C L A S S E S ,  B U T  I T
AC C E L E R AT E S   E X I S T I N G
C O N S U M P T I O N   B E H AV I O R .

2026 STATE OF THE SOFTWARE SUPPLY CHAINE O L   S O F T WA R E   I S   N OT  A N   E D G E   C A S E

EOL software is often discussed as something a mature program will eventually “clean up.” But data
and analysis from HeroDevs suggests the opposite: EOL dependencies are a structural flaw of
modern enterprise stacks, showing up consistently across ecosystems and persisting over time.

EOL changes the risk model. A measurable share of open source vulnerabilities now fall into a cat-
egory that traditional remediation workflows cannot resolve. For these components, “scan → ticket
→ patch” stops being a workflow and becomes a backlog generator.

FIGURE 3.4
Breakdown of EOL
Components by Registry

25.7%

t
n
e
c
r
e
P

30%

20%

10%

0

18.5%

13.4%

11.6%

10.5%

npm

Maven
Central

PyPl

Cargo

NuGet

Registry

5–15%

of components in enterprise dependency
graphs are EOL, meaning EOL exposure is
present even when teams believe they are
only using supported top-level libraries.

81,000+

package versions with known CVEs are
both EOL and unpatchable. HeroDevs
estimates this number may actually be
400,000 across all registries.

ALL EXPOSED

EOL exposure appears across all major
ecosystems (Java, Python, npm), with little
variation in long-term persistence, sug-
gesting this is not limited to one language
community or a single package manager.

40

THE THREE-LAYERS OF FAILURE2026 STATE OF THE SOFTWARE SUPPLY CHAINW H Y  E O L   A L LO W S  “ F O R E V E R
V U L N E R A B I L I T I E S ”

Most vulnerability programs assume a predictable
lifecycle: issues are disclosed, fixes are released,
and risk declines as organizations patch and
upgrade. EOL status breaks that logic. Once a
release line is out of maintenance, upstream fixes
stop, and a vulnerability can persist indefinitely —
not simply because teams are slow to respond,
but because the ecosystem no longer provides a
patch path. At the same time, advisory coverage
often degrades for unsupported versions, cre-
ating blind spots where EOL exposure is under-
counted or missed entirely. And because aban-
doned code is reviewed less, fewer issues may be
found or disclosed, so “no CVE” can indicate low
scrutiny rather than safety.

In practice, EOL turns ordinary defects into “forever
vulnerabilities”: liabilities that cannot be resolved
through routine patching and instead require major
upgrades, replacements, or commercial backports.
AI-assisted development can amplify this effect

A I   R E I N F O R C E S   E O L   R I S K
I N   P R E D I C TA B L E   WAYS :

1.  AI models recommend EOL components
because training data reflects historical
prevalence, not current support status.

2. EOL packages often appear “popular” in
public code corpora, creating insecure
defaults in AI-generated manifests.

3. Once introduced, EOL dependencies
are self-replicating: AI reuses prior
code patterns, deepening organiza-
tional reliance on abandoned software.

41

by steering teams toward what is most common
in historical code rather than what is currently
supported. EOL components often appear “pop-
ular” in public corpora, making them more likely
to be suggested and adopted as defaults in
AI-generated manifests. Once introduced, those
patterns can replicate across services through
reuse, reinforcing dependence on software that
has no viable long-term remediation path.

E O L   I N  T H E   W I L D :   LO G 4 S H E L L
A N D   OT H E R S

EOL is not just a theoretical lifecycle concern. It
has measurable real-world impact during major
incidents. Log4Shell illustrates how EOL status
can prevent closure even when a fix exists in
maintained branches. Real-world cases show
how EOL obstructs remediation:

•  14% of Log4j artifacts affected by Log4Shell
are now EOL, representing more than 619
million downloads in 2025, preventing closure
even four years later.

•  Widely deployed major versions of Java, Node.
js, Python frameworks, and .NET libraries con-
tinue to see active download volume despite
being unsupported.

•  CVE coverage for these versions is often

incomplete or missing, reinforcing misleading
“clean” scan results, especially when advisories
and scanners focus on supported release lines.

This is how “known vulnerabilities” become
“persistent exposure.” Even if engineering teams
upgrade where they can, long-tail EOL usage
can keep a vulnerability class alive in produc-
tion fleets, especially in large enterprises with
diverse portfolios, legacy workloads, and inher-
ited dependency trees.

2026 STATE OF THE SOFTWARE SUPPLY CHAINT H E   B AC K P O R T  E C O S YS T E M

As EOL exposure becomes unavoidable, a sec-
ondary market has emerged to provide what
upstream maintainers no longer can: security
patches for unsupported release lines. This
ecosystem is both a pragmatic mitigation path
and a signal of structural fragility in open source
lifecycle guarantees.

These programs can reduce risk when modern-
ization is not immediately feasible. But they also
underscore a core shift: for a meaningful share of
enterprise dependencies, patchability is no longer
guaranteed by the open source ecosystem itself.
Organizations must plan for lifecycle continuity as
a security requirement, not a best practice.

A   G R O W I N G   R E S P O N S E
E C O S YS T E M   I N C LU D E S :

1.  Commercial extended-support

 providers that backport security
fixes (and sometimes ship compatible,
maintained forks).

2. Smaller specialist vendors and

consultancies that produce targeted
patches for older release branches.

3. Community-maintained forks that

temporarily sustain patching.

42

How the Three Layers
Compound Each Other
Together, these failures create structural vulnera-
bility debt, or risk that accumulates faster than it
can be identified, triaged, or patched. Traditional
“find and fix” workflows, centered on CVE identi-
fiers and remediation queues, cannot keep pace
with this reality. When the data is incomplete,
consumption is undisciplined, and the ecosystem
is aging, security becomes a reactive discipline
rather than a strategic one.

Modern vulnerability risk is not the product of a
single failure point. It is systemic, emerging from
the way multiple weaknesses interact across
the SDLC. When viewed in isolation, each layer
appears manageable. When combined, they
create a feedback loop that sustains risk even
in organizations with mature security programs.
The result is not a backlog problem but a struc-
tural one:

•  Long-term residual risk persists across soft-
ware lifecycles, surviving refactors, rebuilds,
and even organizational change.

•  Attack windows widen as vulnerable and EOL
components accumulate faster than teams
can identify, prioritize, and remove them.

•  Remediation pipelines fall behind depen-
dency sprawl, generating more work than
existing security and engineering capacity
can absorb.

•  Compliance artifacts drift from reality.
SBOMs, audit reports, and scan results
increasingly reflect what tools can see, not
what software actually runs, especially when
shadow downloads, or artifacts that are pulled
into development without the use of a reposi-
tory manager, bypass formal governance.

THE THREE-LAYERS OF FAILURE2026 STATE OF THE SOFTWARE SUPPLY CHAINH O W   V U L N E R A B I L I T Y  D E B T  AC C U M U L AT E S

DATA
Blind spots create false confidence.

CONSUMPTION
Old and unsafe versions keep flowing into builds,
often without anyone noticing.

ECOSYSTEM
Unsupported components turn “known issues” into permanent risk.

INCIDENT

Eventually, debt must be paid: exposure, exploit, breach.

This is why vulnerability management feels increasingly ineffective, even as tooling improves. The
system is optimized to find and fix individual vulnerabilities, while the risk itself is produced by how
software is sourced, reused, and aged over time. When bad data feeds unsafe consumption, and
unsafe consumption feeds unpatchable software, remediation alone cannot catch up. Organizations
accumulate vulnerability debt, not because teams are inattentive, but because the system allows risk
to enter faster than it can be retired.

43

2026 STATE OF THE SOFTWARE SUPPLY CHAINModernizing Vulnerability
Management
The issues outlined in this chapter are not the
result of insufficient effort or tooling, but the
product of workflows designed for a slower, sim-
pler software ecosystem. Addressing modern
vulnerability risk requires modernization, not
acceleration of legacy “find-and-fix” models.

To meaningfully reduce vulnerability debt, orga-
nizations need to move beyond CVE-by-CVE
remediation toward lifecycle-based modern-
ization and governance. In practice, reducing
risk increasingly means addressing structural
weaknesses: improving the fidelity of vulnerabil-
ity intelligence, making safe dependency intake
the default, and proactively migrating away from
EOL components that have no future patch path.

This shift is necessary because vulnerability risk
is now systemic rather than isolated. Modern vul-
nerability management often fails at the system
level, constrained by weak data quality, inefficient
consumption patterns, and the compounding
effects of aging software foundations. The data
layer, in particular, is increasingly misaligned with
real-world exposure: coverage gaps, inaccurate
metadata, and delayed scoring distort prioriti-
zation, waste remediation effort, and obscure
material risk.

At the same time, the ecosystem itself is aging
in ways that create durable exposure. EOL and
abandoned components transform open source
vulnerabilities into long-term liabilities that cannot
simply be patched away; they must be modern-
ized out of the environment or supported through
alternative maintenance models. AI increases the
urgency of this modernization agenda.

W I T H O U T  G OV E R N A N C E ,  A I   C A N   A M P L I F Y
E AC H   FA I LU R E   M O D E ,  M A K I N G   L I F E CYC L E
M O D E R N I Z AT I O N ,  N OT  C V E  T R AC K I N G   A LO N E ,
T H E   O N LY  S U S TA I N A B L E   PAT H   F O R WA R D.

44

THE THREE-LAYERS OF FAILURE2026 STATE OF THE SOFTWARE SUPPLY CHAINTo reduce structural vulnerability debt, organizations must correct weaknesses across all three layers
of the system: data, consumption, and ecosystem. And, with increasing integration of AI into software
pipelines, reducing this risk has never been more critical.

Layer

Key Actions

DATA
LAYER

•  Enrich CVE/NVD: leverage data from OSV.dev, GitHub Security

Advisories, upstream maintainers, and commercial intel.

•  Add decision context: accurate version ranges, exploitability

signals, and EOL status.

•

Improve identification: fingerprint shadow-downloaded arti-
facts and feed curated data into AI systems.

CONSUMPTION
LAYER

•  Block by default: repository firewall + policy controls for

known-vulnerable versions and shadow downloads.

•  Standardize safe inputs: golden images, dependency tem-

plates, internal catalogs/allowed versions.

•  Automate hygiene: PR bots + continuous refresh with compatibili-
ty-aware upgrades; govern build agents/AI to approved sources.

ECOSYSTEM
LAYER

•  Treat EOL as critical: detect, prioritize, and remove unsup-

ported components.

•  Define exit paths: major upgrades, framework transitions,

retirement plans.

•  Reduce provenance risk: eliminate unsupported shadow bina-
ries; use extended-support backports only as transitional con-
trols; surface lifecycle status in SBOM/risk scoring.

AI WITHIN
CONTROLS

•  Constrain recommendations: limit AI to approved catalogs

and sources.

•  Steer the model: retrain/condition on enriched, policy-aligned

metadata (not popularity).

•  Verify outputs: monitor AI-generated manifests for vulnerable/
EOL/shadow patterns and enforce dependency-aware guard-
rails in workflow.

Primary KPI

False negative
rate / coverage
gaps (missed
vulnerable or EOL
components due
to incomplete
intelligence).

Avoidable expo-
sure = % of down-
loads/builds using
vulnerable versions
when a fix exists.

EOL footprint =
% of compo-
nents (or builds)
on unsupported
release lines.

AI policy violation
rate = % of AI-gen-
erated depen-
dency changes
that introduce
vulnerable, EOL,
or unapproved
components.

45
45

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

2026 STATE OF THE SOFTWARE SUPPLY CHAINFrom Guesswork to Grounded:

AI AGENTS WITH REAL
WORLD INTELLIGENCE

As organizations increasingly delegate critical security decisions
to AI systems, we face a fundamental challenge: even state-of-
the-art language models lack access to real-time vulnerability
databases, supply chain intelligence, and breaking change data.
As a result, AI agents are confidently recommending nonexistent
versions, introducing known vulnerabilities, and even suggesting
malware-infected packages. The model is doing all of this while
appearing authoritative.

T H I S   I S N ’ T  A N
I N D I C T M E N T  O F   A I
C A PA B I L I T I E S .  I T ’ S   A
R E C O G N I T I O N  T H AT
AU TO M AT I O N   W I T H O U T
L I V E   I N T E L L I G E N C E   I S
DA N G E R O U S   AT  S C A L E .

Traditional upgrade strategies expose similar blind spots. Most Recently Published Version (Latest) heu-
ristics, which software developers simply upgrade open source components whenever a newer version
is available, assume newer means better, ignoring CVE disclosures, stability signals, and the cascade of
breaking changes that transform simple updates into multi-week migrations. Meanwhile, ungrounded
AI recommendations, regardless of the sophistication of the underlying model, operate on theoretical
patterns rather than live security intelligence. Both approaches share a critical flaw: they make decisions
without the data that actually matters and without the guardrails to guarantee code is compliant.

46

FROM GUESSWORK TO GROUNDED2026 STATE OF THE SOFTWARE SUPPLY CHAINPROMPT

You are helping a production engineering team decide on a dependency
upgrade path.

Based on your best knowledge, recommend the version they should target.
If newer releases may exist beyond your knowledge, still provide a specific
version and explain any uncertainty.

Dependency context:
- Package: {namespace}/{name}
- Current production version: {version}
- Ecosystem: {format}

Return JSON matching the schema.

In this research, Sonatype demonstrates a
different path: AI that is grounded in live
intelligence, validated against real registries,
and guided by breaking-change analytics
governed by policy. When AI operates with
this foundation, its capabilities shift from theo-
retical suggestion engines to trusted, produc-
tion-grade decision systems.

This chapter analyzes nearly 37,000 real depen-
dency upgrades across Maven, npm, PyPI, and
NuGet to quantify how ungrounded AI coding
agents behave in practice and how security-in-
telligent governance closes the gap.

LLMs Hallucinate Versions at Scale

27.76% of dependency upgrades

were hallucinations

Across 36,870 upgrade recommendations,
27.76% referenced non-existent versions includ-
ing over 10,000 hallucinated package releases
that would never resolve in a live repository.

47

FROM GUESSWORK TO GROUNDED2026 STATE OF THE SOFTWARE SUPPLY CHAINFIGURE 4.1
Hallucination Rates by Confidence Level

Confidence

Hallucinated

Valid

High

Medium

Low

23

4,504

5,708

1,336

18,959

6,340

Total

1,359

23,463

12,048

Hallucination Rate

Share of
Hallucinations

1.69%

19.20%

47.38%

0.22%

44.01%

55.77%

P E R F O R M A N C E   A N A LYS I S
O F  T H E   L L M   S T R AT E GY

The performance analysis of the LLM
strategy (detailed in the “Grounding AI
Agents In Real-World Intelligence” section
of the Appendix) reveals an interesting
finding regarding confidence:

•  GPT-5 was 98% accurate when it

expressed high confidence

•  It expressed high confidence in just

3.68% of recommendations

•  Nearly half of all “low confidence”

answers were incorrect

This confidence pattern was observed in a sam-
ple of real-world enterprise applications. While
production AI systems might decline to answer
when uncertain, the core issue remains: package
ecosystems evolve constantly. New versions ship
hourly. Security vulnerabilities are constantly
emerging. No training dataset, however com-
prehensive, can predict tomorrow’s CVE or
next week’s breaking change.

Sonatype’s approach doesn’t compete with
agentic AI — it completes it. By grounding recom-
mendations in live package registries, proprietary
vulnerability and malware data, and breaking
change calculations, we achieved zero AI hallu-
cinations across the same 36,870 components.
Every recommendation is verified against real
repositories. Every upgrade is assessed for
actual security impact.

The future isn’t choosing between AI and tradi-
tional tools. It’s AI agents operating with real-time
intelligence that teams can trust in production.

48

2026 STATE OF THE SOFTWARE SUPPLY CHAINFIGURE 4.2
Mean security score improvement per application by strategy

e
s
a
e
r
c
n

I

400%

300%

200%

100%

0

120.4%

267.1%

258.4%

306.7%

LLM

Latest

NBC

Best

Strategy

Security Improvement
by Upgrade Strategy
Software ages like milk, not wine. As new vul-
nerabilities are discovered and disclosed, older
package versions accumulate security debt
while newer releases incorporate patches. Every
day without upgrading increases exposure. Yet,
not all upgrade paths are created equal. We
compared four upgrade strategies across 856
enterprise applications. All strategies improved
security, but not equally.

Figure 4.2 outlines the mean security score
improvement for each application by strategy.
Percent improvement is calculated as (total
target security - total baseline security) / total
baseline security × 100, averaged across vulner-
able components from 856 enterprise applica-
tions. Security scores aggregate the severity and
count of known vulnerability types on a 0–100
scale. For example, an application with 450 base-
line points improving to 614 target points rep-
resents +36.4% security gain.

49

COMPARING FOUR UPGRADE STRATEGIES

We compared four upgrade strategies across
856 enterprise applications. All strategies
improved security, but not equally

•  LLM-generated versions (LLM)

Lowest improvement of the strategies ana-
lyzed; 345 components became less secure

•  Most Recently Published Version (Latest)

Results in strong security outcomes but with
extreme engineering costs

•  Sonatype ‘No Breaking Changes’ (NBC)
Chooses highest safe version without
breakage; high security gains with minimal
refactoring

•  Sonatype Best (Best) Chooses highest ver-
sion score regardless of breaking changes;
highest security improvement overall

FROM GUESSWORK TO GROUNDED2026 STATE OF THE SOFTWARE SUPPLY CHAINOverall, it is generally a good idea to remediate
vulnerabilities. All upgrade strategies improve
security outcomes, but not equally. LLM-gener-
ated (LLM) upgrade recommendations show the
smallest uplift, recommending generally newer
versions without proper guidance. Sonatype
‘No Breaking Changes’ (NBC) sees a significant
improvement while identifying versions that mini-
mize or eliminate breaking changes.

Then we have the Latest version strategy, with
a significant improvement in security, but with
a high engineering cost, as we will see later. The
overall best improvement comes from the Sona-
type Best (Best) strategy, which more holisti-
cally considers the security of the components
(severity in combination) when identifying the
best upgrade path.

LLM recommendations present a troubling par-
adox. While showing an improvement overall,
the model degraded security posture for 345
components, ecommending newer versions

that introduced more vulnerabilities than they
resolved. This occurred when the model unknow-
ingly chose versions that:

•  Were compromised after its training cutoff

•  Carried additional CVEs

•  Were newer, but were also riskier

M A LWA R E   A N D   P R OT E S T WA R E
R E C O M M E N DAT I O N S

The LLM strategy did more than hallucinate ver-
sions. It recommended sweetalert2 11.21.2,
which is confirmed protestware executing politi-
cal payloads, as well as  color 5.0.1 and
color-string 2.1.1,  which were compro-
mised in a major supply chain attack. These
packages were not obscure edge cases. They
were widely downloaded and part of a high-pro-
file security event that occurred after the mod-
el’s training data cutoff.

PROMPT

{
  “color”: {
    “recommended_version”: “5.0.3”,
    “confidence”: “high”,
    “rationale”: “Latest per Sonatype MCP; MIT licensed, no known vulnerabilities.”
  },
  “sweetalert2”: {
    “recommended_version”: “11.26.3”,
    “confidence”: “high”,
    “rationale”: “Latest stable; fixes prior malware flag and known CVE.”
  }
}

50

2026 STATE OF THE SOFTWARE SUPPLY CHAINT H I S   I S  T H E   C O R E   P R O B L E M :   A I
C A N N OT  D E T E C T T H R E AT S  T H AT
H A P P E N E D   A F T E R   I T  WA S  T R A I N E D.
A I   N E E D S   R E A L-T I M E   I N T E L L I G E N C E .

While security improvements justify upgrades,
the practical question remains: what does it
cost? Breaking changes drive developer effort,
transforming version bumps into multi-day
refactoring projects. The following analysis
quantifies these costs across strategies, reveal-
ing trade-offs between security gains and imple-
mentation burden.

B R E A K I N G   C H A N G E   C O S T  A N A LYS I S

Security improvements come at a price measured
in developer hours and refactoring effort. Across
856 enterprise applications with representative
dependency footprints, upgrade strategies impose
dramatically different implementation costs.

Figure 4.3 below compares median per-applica-
tion upgrade budgets across the four strategies.
NBC delivers the lowest-friction path: roughly
~1 engineer-week to modernize an entire app
while avoiding destabilizing work. Best still holds
the costs under $20K and under 200 hours per
app, yet it absorbs the additional change needed
to drive higher security scores.

FIGURE 4.3
Upgrade Cost & Effort per Application

$30,000

314 hours

)

D
S
U

(

$20,000

192 hours

196 hours

t
s
o
C
n
a
d
e
M

i

$10,000

0

58 hours

LLM

Latest

NBC

Best

Strategy

51
51

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

FROM GUESSWORK TO GROUNDED2026 STATE OF THE SOFTWARE SUPPLY CHAIN

FIGURE 4.4
At Enterprise Scale: Upgrade Cost & Effort

$50M

$40M

11,775 weeks

)

D
S
U

(

t
s
o
C
n
a
d
e
M

i

$30M

7,200 weeks

7,350 weeks

$20M

$10M

0

2,175 weeks

LLM

Latest

NBC

Best

Strategy

Both outclass the unmanaged options: uncon-
strained Latest upgrades result in nearly 5x
the median spend versus NBC, and LLM-only
selections land in the same cost bracket as Best
without the significant risk reduction.

Applying a generic ~8% copilot uplift to the same
per-app upgrade totals, NBC still modernizes
an app for a little over $5K and ~53 hours, while
chasing Latest upgrades soaks up nearly $27K
and 288 hours — over five times the spend and the
engineering time.

That gap isn’t just a bookkeeping line; it’s
opportunity cost. Every extra week poured into
unmanaged upgrades is a week not spent on
security hardening, paying down tech debt,
or feature delivery. LLM-only picks land in the
same budget band as Best yet lack its curated
risk reduction, reinforcing that disciplined Sona-
type strategies are the only way to keep upgrade

budgets predictable without cannibalizing road-
map work.

H O W   C O S T S   S C A L E :
O R GA N I Z AT I O N A L   I M PAC T

This projection scales each strategy’s median
per-application effort across a representative
large enterprise portfolio. It illustrates the cumu-
lative impact of decentralized upgrade decisions
over time.

In practice, organizations don’t upgrade every
dependency in every application all at once.
Instead, they perform ongoing dependency main-
tenance — small, continuous updates that, across
hundreds or thousands of applications, represent
a near-constant workload. Without a cohesive
strategy, these distributed efforts can quietly
accumulate into multimillion-dollar annual costs.

52

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

T H E  “ I N T E L L I G E N C E ”  GA P
I N   G E N E R AT I V E   A I

The most alarming finding is not merely that
ungrounded AI makes mistakes, but that it makes
dangerous ones with high confidence. The
observed 27.8% AI hallucination rate in GPT-5
recommendations confirms that language
models, when isolated from live repositories,
struggle to distinguish between existing and
non-existent software.

More critically, the “hallucinations” were not only
harmless version number errors, but also data
corruption, protestware, and hijacked packages.
This illustrates a fundamental limitation: training
data cuts off, but supply chain attacks operate in
real-time. A model trained before a package com-
promise cannot “know” a version is unsafe with-
out a live feed of vulnerability intelligence.

Furthermore, the LLM strategy delivered the
lowest security improvement (+120.4%) of all
methods tested. In 345 specific instances, fol-
lowing the AI’s advice actually degraded the com-
ponent’s security posture by introducing more
vulnerabilities than it resolved.

NBC automation keeps portfolio-level upgrade
effort roughly an order of magnitude lower than
unmanaged Latest adoption, while achieving
a similar security posture. Teams targeting the
most secure baseline can adopt Best selectively,
reserving deeper migrations for critical systems
where maximum vulnerability reduction warrants
the additional investment.

Our analysis of 36,870 dependency upgrade
recommendations exposes a critical divergence
between the promise of autonomous AI agents
and the reality of software supply chain security.
The data suggests that without access to real-
time package registry intelligence, both state-of-
the-art LLMs and traditional Latest heuristics fail
to balance security risk with engineering effort.

S W E E T A L E R T 2  V E R S I O N  1 1 . 2 1 . 2

Data corruption & protestware

This package creates a ‘noWarMessageFor-
Russians’  banner on any Russian website
using this component that is running in a
browser using Russian.

C O L O R  V E R S I O N  5 . 0 . 1   &
C O L O R - S T R I N G  V E R S I O N  2 . 1 . 1

Cryptostealer & hijack

Taken over as part of the chalk/debug
campaign, color and color-string
were manipulated to extract victims’
cryptocurrency from browser wallets.

53

FROM GUESSWORK TO GROUNDED2026 STATE OF THE SOFTWARE SUPPLY CHAINT H E   FA L S E   E C O N O M Y  O F
“ L AT E S T  V E R S I O N ”

While the industry often defaults to “always
upgrade to latest” as a best practice, our cost
analysis reveals this to be a financially inefficient
strategy. While Latest achieved strong security
gains (+267.1%), it did so at a brute-force cost:
approximately $29,516 and 314 developer hours
per application. When scaled to a portfolio of
1,500 applications, the Latest strategy demands
nearly $44.3 million in estimated labor costs.

H O W   W E   G E T TO   $ 4 4 M   AT
T H E   E N T E R P R I S E   S C A L E

•  180 dependencies per app × ~$161

per app = ~$29.5K per app

•  1,500 apps × $29K = ~$44.3M

This 5x cost multiplier, compared to intelligent
automation, represents a massive opportunity
cost; every hour spent resolving breaking changes
from an unnecessary major version jump is an hour
lost to feature development or debt reduction.

Grounding is the Missing Link
The high accuracy (98%) of GPT-5 in the rare
instances (3.68%) where it expressed “High Con-
fidence” suggests that the reasoning capabilities
of modern models are sound, but their context is
insufficient.

The path forward is not to choose between AI
and traditional tools, but to ground autonomous
AI agents in verified intelligence. By feeding the
model real-time data — including computed break-
ing changes and enhanced vulnerability and mal-
ware intelligence, Sonatype’s approach eliminates
AI hallucinations entirely while empowering teams
to choose the upgrade path (Best vs. No BC) that
aligns with their risk tolerance and budget.

SONATYPE SECURITY HYBRID
You can also take a hybrid approach that puts security first in the version scoring algorithm.
When a version has a perfect security score, it recommends NBC; otherwise, it defaults to
the Best recommendation. This results in:

327%

2.1X

security gain from remediating
vulnerable components

lower dependency upgrade cost and
effort compared to Latest Version

54
54

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

2026 STATE OF THE SOFTWARE SUPPLY CHAINThe 2025 Global Software Assurance Mandate:

TRANSPARENCY
AS THE NEW TRUST

Transparency has become the currency of software supply chain security.
Around the globe, policymakers and regulatory bodies have moved from rhetoric to regulation on that
principle. SBOMs (Software Bills of Materials), attestations, and provenance tracking are no longer
optional. They’re being elevated as expressions of transparency, codified in law, and embedded into how
organizations will be required to demonstrate security readiness. We estimate 90% of global organiza-
tions fall under one or more regulatory requirements to demonstrate evidence of software assurance.

In this chapter, we map the current regula-
tory landscape, identify key changes and
enforcement deadlines as of the end of
2025, and forecast how organizations should
prepare. We show how software compliance
is shifting from policy to code and why teams
that treat transparency as an engineering
challenge will win.

UP TO 90%

of organizations around the world will fall
under one or more regulatory requirements

55

TRANSPARENCY AS THE NEW TRUST2026 STATE OF THE SOFTWARE SUPPLY CHAINFrom Open Source Governance
to Regulatory Mandate
For years, SBOMs, consumption governance,
and software supply chain transparency were
treated as best-practice responses to technical
risk. What changed in 2025 is that transparency
moved from optional to required. Across regions,
regulations are converging on the same basics:
minimum SBOM elements, interoperable formats,
and proof of secure development practices. The
focus is no longer just what’s in the software, but
who delivered it and how it was built and shipped.

This shift is also changing how compliance
works. Manual checklists are giving way to
automation and “compliance as code,” because
procurement, audits, and enforcement increas-
ingly demand auditable evidence. Vendors are
expected to show, not just claim, that they gener-
ate SBOMs, track provenance, sign artifacts, and
provide attestations when asked.

As a result, open source governance is now
squarely in the regulatory spotlight. Policies that
once lived as internal guidelines are becoming
obligations, driven by frameworks such as the
EU Cyber Resilience Act and NIS2, alongside U.S.
Executive Order 14028. OSS components, forks,
transitive dependencies, and license ambiguity
can create exposure not only through security
risk, but through procurement breach, audit
failure, or product liability. The UK is moving
in the same direction. The Cyber Security and
Resilience Bill, recently introduced to Parliament,
signals expanded scope and faster incident
reporting, reinforcing that assurance has to be
operational, repeatable, and provable.

56

Sonatype sees this evolution as a positive forcing
function. The industry already knows what “good”
looks like: mapped dependencies, SBOMs, signed
provenance, and attestable secure practices.
The work now is making those outputs default by
embedding them directly into development and
release workflows.

GLOBAL REGULATORY TIMELINE

May 12, 2021

US Executive Order 14028 signed.

July 12, 2021

US NTIA publishes SBOM “Minimum Elements.”

January 16, 2023

NIS2 and DORA enter into force in the EU.

December 1, 2023

Australia’s ASD ISM first edition released.

October 18, 2024

NIS2 compliance measures apply in the EU.

December 10, 2024

EU Cyber Resilience Act (CRA) entered
into force.

January 17, 2025

DORA compliance measures apply in the EU.

July 25, 2025

CERT-in mandatory annual third-party
cybersecurity audits in India.

November 12, 2025

UK CSRB introduced to parliament.

TRANSPARENCY AS THE NEW TRUST2026 STATE OF THE SOFTWARE SUPPLY CHAINT H E   R E G U L ATO R Y  M A P :   W H E R E  T H I N G S   S TA N D   AT T H E   E N D   O F   2 0 2 5

US Federal Agencies
SSDF, CISA attestation
form, SBOM guidance

India
CERT-In / SEBI
expectations

US Commercial
EO 14028

United Kingdom
Cyber Resilience Bill

European Union
NIS2, CRA,
DORA, AI Act

Australia
ASD ISM and
continued
Essential 8
emphasis

M A N DAT E S   I N
F O R C E  /  D E TA I L E D
G U I DA N C E

•  European Union

•  United States

(Federal)

M A N DAT E S
A D O P T E D  /  I N
T R A N S I T I O N

•  United Kingtom

•  United States
(Commercial)

•  Australia

E M E R G I N G
R E Q U I R E M E N T S  /
G U I DA N C E   O N LY

•  India

Note: On January 23, 2026, OMB issued Memorandum M-26-05 rescinding the standardized secure software self-attestation
approach and directing agencies to use a risk-based model for software assurance, including requesting SBOMs when appropriate.

57
57

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

2026 STATE OF THE SOFTWARE SUPPLY CHAINUnited States Software
Regulations

In the U.S., the federal approach has matured into
a multi-layered regime. The foundation lies in the
NIST SP 800-218 (Secure Software Development
Framework, SSDF) and the self-attestation and
verification regime instituted under Executive
Order 14028 and related OMB memoranda (such
as M-22-18 and M-23-16). The Cybersecurity and
Infrastructure Security Agency (CISA) has pub-
lished the Secure Software Development Attesta-
tion Form, which vendors must submit to certify
adherence to secure development practices.

Federal procurement rules now condition soft-
ware eligibility on those attestations, and as
noted by the Government’s Software Acquisition

S O F T WA R E   V E N D O R S   S E E K I N G
F E D E R A L   C O N T R AC T S
M U S T  P R OV I D E :

☑ Attestation that their development

practices align with SSDF.

☑ Minimum Elements for SBOMs (in
one of the formats specified by the
National Telecommunications and
Information Administration (NTIA)
and supplemented by CISA.

☑ Evidence of component provenance,
vulnerability handling, and in some
cases third-party assessment.

58

Guide, procurement agencies are being guided
to require transparency via SBOMs, signed arti-
facts, and auditable supplier processes.

For federal agencies, this has broader implica-
tions: the procurement lifecycle now explicitly
links security software assurance to procurement
eligibility, renewal cadence, and supplier audits.
Vendors that cannot demonstrate attestations or
generate SBOMs may simply be disqualified.

In our view, organizations outside of federal
scope but working in critical verticals should view
this as indicative of what is coming in the private
sector: procurement leverage, audit readiness,
and transparency of supply chain footprint will
become table stakes.

European Union Software
Regulations
Europe has launched multiple landmark pieces of
legislation in the software supply chain and prod-
uct cybersecurity domain.

N I S 2   +   I M P L E M E N T I N G   R E G U L AT I O N

The NIS2 Directive (Directive (EU) 2022/2555)
entered into force in January 2023 and introduced
higher standards for cybersecurity risk manage-
ment, incident reporting, and software supply chain
security for “essential” and “important” entities.
The Commission Implementing  Regulation (EU
2024/2690) defines more specific technical and
methodological requirements. In June 2025, the
European Union Agency for Cybersecurity (ENISA)
published technical implementation guidance for
the software regulation, mapping each requirement
to evidence, frameworks, and standards.

TRANSPARENCY AS THE NEW TRUST2026 STATE OF THE SOFTWARE SUPPLY CHAIN
NIS2 explicitly requires organizations to manage
software supply chain security risks, incorpo-
rate secure-by-design and secure procurement
principles into system acquisition and devel-
opment, and demonstrate effective software
governance. Organizations in scope must main-
tain documented risk management policies,
implement incident detection and handling pro-
cesses, and assess and manage the cybersecu-
rity posture of suppliers.

CY B E R   R E S I L I E N C E   AC T  (C R A )

The CRA (Regulation (EU) 2024/2847) estab-
lishes a horizontal regulatory framework for
“products with digital elements” (PDEs). It
entered into force on December 10, 2024. Its
main obligations begin to apply in December
2027, after a three-year transition period. Certain
vulnerability handling and reporting obligations
start earlier, in September 2026.

Under the CRA, manufacturers must ensure that
products are designed, developed, and produced
in accordance with essential cybersecurity
requirements. This includes implementing Secure
by Design practices, performing and document-
ing risk assessments, and ensuring ongoing
vulnerability handling throughout the support
period they specify. When integrating third-party
components, including free and open source
software, manufacturers remain responsible
for assessing risks and maintaining appropriate
technical documentation.

The CRA requires manufacturers to maintain
detailed technical documentation about secu-
rity properties and supply chain dependencies.

59

While the software regulation anticipates greater
transparency of software components, it does
not explicitly prescribe an SBOM format; how-
ever, it does empower the Commission to adopt
delegated acts specifying additional elements or
procedures, which could include SBOM-related
requirements in the future.

A notable feature of the CRA is that it brings
certain actors in the open source ecosystem
into scope. Specifically, “open source software
stewards” are identified as individuals who play a
coordinating role in the development and distri-
bution of widely used OSS.

They may be subject to obligations such as
adopting documented cybersecurity processes,
providing attestations, and cooperating with
market surveillance authorities. These obli-
gations apply only where such stewards meet
the criteria defined by the regulation and are
not intended to cover individual volunteer
contributors.

In parallel, the revised EU Product Liabil-
ity framework (Regulation (EU) 2024/2853)
extends no-fault liability to software and dig-
ital products. Non-compliance with the CRA’s
cybersecurity obligations may therefore expose
manufacturers to strict product liability for
damage caused by vulnerabilities or security
defects in products with digital elements, irre-
spective of fault or negligence.

From our perspective at Sonatype, CRA and
NIS2 together represent a sea-change: software
and products containing digital elements are
regulated from design through maintenance;
transparency and SBOMs are wired in. The mes-
sage: software compliance requires end-to-end
visibility, not after-the-fact patching.

2026 STATE OF THE SOFTWARE SUPPLY CHAIN
Other Key Jurisdictions
Beyond the U.S. and EU, several jurisdictions are
aligning with this global transparency movement.

From Sonatype’s vantage point: while regulatory
maturity varies, the direction is consistent globally.
Firms that invest in transparency and software
assurance now will gain a competitive advantage.

Regulated Industries: From
Obligation to Opportunity
Historically, heavily regulated industries, includ-
ing financial services, healthcare, and critical
infrastructure, have been the earliest adopters
of software assurance and SBOM mandates. The
regulatory developments emerging in 2025 are
broadening that landscape.

Under DORA, financial institutions and their ICT
third-party providers must implement compre-
hensive ICT-risk-management frameworks, inci-
dent reporting processes, and supplier-
governance controls. Requirements for docu-
menting cyber resilience strategies and demon-
strating oversight of software supply chain risk
are now appearing in procurement cycles and
audit practices.

In 2025, multiple regulatory bodies began explic-
itly treating artificial intelligence components,
including models, training data, evaluation pipe-
lines, and automated decision systems, as soft-
ware artifacts subject to supply chain controls.

The AI-compliance landscape is rapidly matur-
ing, led by the EU AI Act’s staggered phase-in
schedule and U.S. federal guidance following
Executive Order 14110 (later replaced by Execu-
tive Order 14179).

In India, the Indian Computer Emergency
Response Team (CERT-In) and the
Securities and Exchange Board of India
(SEBI) have updated incident reporting
obligations and disclosure requirements.

While SBOM mandates are less mature than
in the U.S. or EU, regulated entities are being
required to establish software supply chain doc-
umentation and risk management programs as
an expectation.

In Australia, the Australian Signals
Directorate (ASD) Information Secu-
rity Manual (ISM) and the “Essential
8” framework have long influenced
cyber-maturity expectations.

In 2025, those frameworks began emphasizing
software supply chain transparency, SBOMs,
and supplier assurance as differentiators for
procurement in critical sectors.

60

TRANSPARENCY AS THE NEW TRUST2026 STATE OF THE SOFTWARE SUPPLY CHAINFormats and Interoperability
The two dominant SBOM schemas are SPDX and CycloneDX. SPDX has traditionally excelled in open
source license compliance and metadata governance; CycloneDX is particularly effective for vulnera-
bility/component dependency correlation and CI/CD integration. In practical terms, organizations must
evaluate when to use which schema: for licensing-governance pipelines SPDX may be the default; for live
software supply chain tools, vulnerability context and runtime telemetry, CycloneDX may be preferable.

Interoperability is increasingly mandated. For example, the CRA allows the European Commission
to specify by delegated acts the format and elements of SBOMs for products with digital elements.
“Attestation” too has become the currency of procurement and audit readiness. In the U.S., CISA’s
attestation form formalized vendor self-attestation to SSDF practices. Similarly, the EU regulatory
regimes expect documented evidence of risk assessments, vulnerability-handling procedures, and
software assurances.

The key operational lesson here is that transparency must be engineered: organizations must treat
SBOM generation, artifact signing, attestation capture, and publishing as part of the build-and-re-
lease pipeline — not as an afterthought. The enforcement regime is moving from “show us your pol-
icy” to “show us the artifact”.

S B O M   &   AT T E S TAT I O N   F O R M AT S

strong

mixed

Category

SPDX

CycloneDX Notes

Licensing &
IP metadata

Vulnerability /
Dependency
correlation

CI/CD
Friendliness

Ecosystem
Tooling &
Adoption

strong

mixed

SPDX is fundamentally license-first (SPDX expressions, compliance
lineage). CycloneDX carries license data well, but SPDX remains the
legal/compliance “gold standard.”

mixed

strong

CycloneDX was designed with security and dependency graphs in
mind. SPDX supports this, but it’s not the primary design center.

mixed

strong

CycloneDX is more commonly generated by modern build tools,
scanners, and CI jobs. SPDX is used in CI/CD, but more often post-
build or for compliance artifacts.

mixed

strong

CycloneDX has stronger momentum in AppSec, SCA, and cloud-na-
tive tooling. SPDX remains dominant in regulated, supplier-driven,
and government contexts — strong, but slower-moving.

61
61

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

capture accurate license data; and maintain audit
logs of intake decisions. Downstream, procure-
ment teams are beginning to require supplier
attestations that OSS intake and license gover-
nance policies are in place and followed.

Bringing Policy into Reality
Whether your discussion is around Compli-
ance-as-Code, Policy-as-Code, GRC Engineer-
ing, or some other umbrella term — the industry
is shifting toward automated governance to
keep pace with the exponential acceleration
in both software development speed and mal-
ware presence.

As we can see in the CNCF’s Automated Gover-
nance Maturity Model and OpenSSF’s Gemara,
software development lifecycles can be signifi-
cantly accelerated while improving compliance
outcomes by ensuring codification and automa-
tion at every opportunity:

•  Writing organizational policies in a

machine-optimized format reduces friction for
both human and AI interactions as tools inter-
face with structured data. Policies turn com-
pliance into a foundational design requirement
instead of being stapled on after development.

•  Selection of development tools can be done
with early feedback according to policy,
informed by supplier onboarding workflows:
standardized questionnaires, third-party
assessment checklists, attested secure devel-
opment practices.

Open Source License Compliance
in the New Regime
Key risk patterns include transitive copyleft
propagation (when combining or distributing
code with copyleft-licensed dependencies
can trigger downstream obligations), unclear
or missing license metadata, and forked com-
ponents that diverge from upstream develop-
ment, making provenance and patch-tracking
difficult. The compliance challenge is to define
meaningful metrics. For example, the percent-
age of components with approved licenses,
the number of license conflicts detected pre-
merge, and the mean remediation time for
license-non-compliant usage. While current
compliance regimes rarely specify exact thresh-
olds for these metrics, the trend is clear: orga-
nizations that cannot demonstrate open source
license compliance of intake and remediation
are increasingly disadvantaged in procurement,
audit, and regulatory contexts.

Under the CRA, for instance, open source soft-
ware stewards must put in place and document
in a verifiable manner a cybersecurity policy and
cooperate with market surveillance authorities
and CSIRTs/ENISA in certain circumstances.
They may also need to provide security docu-
mentation and, in some cases, attestations of
compliance. At Sonatype, we increasingly advise
clients that an open source intake policy is no
longer just software governance best practice —
it is rapidly becoming a compliance expectation.

The practical implication is that organizations
must operationalize OSS intake, contribution, and
remediation workflows; integrate open source
license compliance scanning and component
metadata tracking into CI/CD; ensure SBOMs

62

TRANSPARENCY AS THE NEW TRUST2026 STATE OF THE SOFTWARE SUPPLY CHAINC O M P L I A N C E -A S - C O D E

P O L I CY

D E V E LO P M E N T

D E P LOY M E N T

AU D I T

ACCEPTANCE
CRITERIA

AI, SAST, SCA,
& SBOMs

Capture compliance
requirements alongside
design documentation

Equip developers with
policy-informed tools

 VULN & COMPONENT
HEALTH GATES

Ensure deployments
meet CVE and other
requirements

EVIDENCE FOR PROCUREMENT
& REGULATORS

SBOM + attestations
accessible on demand

•  Development tools can provide early feedback
both in the IDE and at pull/merge time with
evaluation and enforcement of priorities such
as license requirements and trusted depen-
dency registries; blocking patterns if disallowed
licenses or untrusted sources are requested.

•  Audits become streamlined by using compiling
machine-readable policies, evaluation logs,
enforcement results, and relevant artifacts
(e.g., via a customer-accessible portal, or pub-
lic registry) to support audit, procurement, or
regulator review.

•  Deployment builds can automatically evaluate
code and enforce requirements such as gen-
eration of SBOMs (SPDX or CycloneDX) with
all dependencies, versions, metadata, and sig-
natures. At release time, attachment of signed
provenance data and attestation, artifacts to
the release package.

The question is not whether your organiza-
tion can produce an SBOM or attestation but
whether it has the automation, traceability, and
audit-readiness baked into the build workflow.
Compliance is not an add-on; it must be part of
the entire software development lifecycle.

63

2026 STATE OF THE SOFTWARE SUPPLY CHAINM E T R I C S   A N D   M AT U R I T Y
F O R   S E L F -A S S E S S M E N T

Transparency and software compliance readi-
ness must be measured. Sonatype recommends
organizations track four dimensions: Coverage,
Integrity, Responsiveness, and Assurance.

•  Coverage: What proportion of shipped arti-
facts include SBOMs? What percentage of
components have declared licenses and an
explicit policy decision?

•  Integrity: How deep is your SBOM (i.e., depen-
dency depth)? Are provenance records signed
and traceable? Is your rebuild reproducible?
What signal-to-noise ratio do your scans pro-
duce (i.e., real vulnerabilities vs false positives)?

SOFTWARE MATURITY ASSESSMENT

Control

Metric

Readiness

Transparency % of artifacts

with SBOM
provenance

% depen-
dencies with
approved
license

Mean time
to patch
vulnerabilities

90% =
Mature

90%+ =
mature

<15 days =
mature

Releases
meeting SSDF
standard

80%+ =
mature

Licensing

Security
Response

Attestation

64

•  Responsiveness: What is your mean time to
provide a customer or regulator an SBOM or
attestation? What is your mean time to resolve a
non-compliant license usage? What is the median
time to apply a post-release security update?

•  Assurance: What percentage of releases meet
SSDF-defined attestation? What percentage
of your suppliers provide verifiable artifacts
(SBOMs, signed provenance, secure develop-
ment attestation)?

Software Assurance as Currency
2025 marked the inflection point. In 2026, soft-
ware assurance becomes the standard by which
software earns trust. Transparency through
SBOMs, attestations, and provenance is moving
from policy to regulation, from a nice-to-have to
a procurement requirement, and from an audit
checkbox to a competitive differentiator.

Sonatype views these mandates as catalysts for
safer software. When compliance is built into the
delivery process, software becomes more mea-
surable, auditable, and secure.

Organizations that embed transparency into
build pipelines, integrate supplier attestations
into procurement, and treat SBOMs and prove-
nance as first-class artifacts will be ahead of the
curve. Everyone else risks procurement lockout,
audit disruption, and downstream liability.

I N   2 0 2 6 ,  C O M P L I A N C E   I S   N OT  J U S T
A B O U T  AVO I D I N G   P E N A LT I E S .  I T
I S   A B O U T  E A R N I N G  T R U S T,  A N D
T R U S T  I S  T H E   C O R E   A S S E T  O F
T H E   S O F T WA R E   S U P P LY  C H A I N .

TRANSPARENCY AS THE NEW TRUST2026 STATE OF THE SOFTWARE SUPPLY CHAINONE-YEAR SOFTWARE COMPLIANCE PLAYBOOK

Based on our experience across clients and regulatory developments, here is a recommended
playbook for organizations aiming to be fully compliant (and competitive) in a world of compliance
through governance.

Timeframe

Primary Goal

Key Actions

Outputs

0–3
MONTHS

E S TA B L I S H
O W N E R S H I P
A N D   B A S E L I N E

3–6
MONTHS

O P E R AT I O N A L I Z E
C O M P L I A N C E
I N   C I /C D

6–12
MONTHS

E X T E N D  TO
S U P P L I E R S   A N D
AU D I T  R E A D I N E S S

•  Name cross-functional compliance

•  Ownership

owners

•  Inventory SBOM coverage
•  Choose SPDX/CycloneDX
•  Validate toolchain
•  Run attestation gap analysis (signing,

pipeline evidence, vuln mgmt)

model
•  SBOM

baseline
•  Schema
decision
•  Gaps list

•  Require SBOM per release
•  Sign and (if needed) publish
•  Map obligations (CRA/NIS2/AI Act

as applicable)

•  Define required artifacts
•  Implement compliance-as-code
(license gate, SBOM at build,
provenance at release)

•  Start metrics

•  SBOM +

signed prov-
enance in
pipeline

•  Obligations/
artifact
catalog

•  Initial metrics

•  Standardize supplier onboarding
•  Require supplier attestations,
SBOMs, signed provenance
•  Quarterly reporting dashboards
•  License conflict + copyleft workflows
•  Make artifacts accessible and

auditable

•  Supplier

requirements
in place
•  Dashboards
•  Audit-ready
evidence
repository

By the end of the year, your goal should be: all major releases produce SBOMs, all software vendors/
suppliers have attested secure-development practices, all major components have approved licenses,
and compliance metrics are live in software governance dashboards.

65
65

2026 STATE OF THE SOFTWARE SUPPLY CHAIN

2026 STATE OF THE SOFTWARE SUPPLY CHAINMethodology

R E G I S T R I E S ,  M O D E L S ,  A N D  T H E   N E W   S O F T WA R E
I N F R A S T R U C T U R E   B U R D E N :   W H E N   G R O W T H   M E E T S   G R AV I T Y

This chapter is based on Sonatype’s analysis of registry consumption and infra-
structure load signals drawn from aggregated telemetry across major open source
ecosystems (with Maven Central used as a primary lens where noted). The study
examined download and re-download behavior over the report’s specified reporting
windows, focusing on how automated software delivery systems (CI/CD pipelines,
ephemeral build fleets, and dependency managers) amplify demand on shared regis-
try infrastructure.

Sonatype Security Research Team evaluated registry load and sustainability pres-
sure using four primary measures:

•  Growth and concentration: overall request volume trends and the degree to which

traffic is dominated by a small set of high-volume consumers.

•  Re-download intensity: repeat-fetch behavior for the same artifacts, used as a

proxy for cache inefficiency and rebuild amplification.

•  Burstiness and hotspots: peak download behavior (e.g., 95th percentile pat-

terns) to distinguish steady consumption from spiky traffic that strains shared
infrastructure.

•  Source footprint signals: directional indicators such as distinct IP counts and dis-

tribution patterns to infer automation characteristics (shared egress/NAT, central-
ized runners), without treating IPs as definitive identity.

While the chapter focuses on open source registry dynamics, the patterns identified
(automation-driven amplification, concentrated demand, and cache fragility) reflect
broader structural pressures affecting modern software supply chains. All quantita-
tive results reflect a point-in-time snapshot as of the report’s stated verification date,
and are reported in aggregate to avoid attribution to specific organizations or users.

66

APPENDIX2026 STATE OF THE SOFTWARE SUPPLY CHAINT H E   E VO LV I N G   S O F T WA R E   S U P P LY  C H A I N   AT TAC K   S U R FAC E :
M A LWA R E   AT T H E   GAT E

This chapter is based on Sonatype’s analysis of malicious open source packages iden-
tified through a mix of automated detection and expert review, using publicly observ-
able package metadata and Sonatype threat intelligence. We evaluated packages
observed within the report’s stated window using a consistent, multi-label threat tax-
onomy (one package may map to multiple behaviors), normalized duplicates/variants
to avoid inflating counts, and used clustering signals (payload and code reuse, naming
patterns, publisher behavior, dependency relationships, and shared infrastructure) to
identify coordinated campaigns. Findings are reported in aggregate as a point-in-time
snapshot as of the report’s verification date.

T H E  T H R E E   L AY E R S   O F   FA I LU R E   I N   M O D E R N
V U L N E R A B I L I T Y  M A N AG E M E N T

The Data Layer: This analysis evaluates the quality and usefulness of vulnerability
records for open source by comparing public advisory data with Sonatype’s enriched
vulnerability intelligence. We assembled a study set of 1,718 open source–relevant CVE
records disclosed within the report’s defined window (January 1, 2025 to December
31, 2025), drawing from publicly available sources (including NVD/CVE metadata and
CVSS where present) and Sonatype Security Research. For each CVE, the Sonatype
Security Research Team assessed five core dimensions that directly affect whether
teams can make consistent remediation decisions: (1) coverage (whether NVD provides
usable CVSS/severity and how often that aligns with Sonatype), (2) scoring consis-
tency (magnitude and direction of CVSS score drift between NVD and Sonatype, plus
resulting severity-category shifts), (3) false positives (records or affected-version
claims that would trigger remediation for non-impacted software), (4) false negatives
(missing, incomplete, or delayed records/metadata that would cause impacted soft-
ware to be missed), and (5) timeliness (time between public CVE disclosure and avail-
ability of NVD analysis/scoring). Results are reported at the CVE level using consistent
matching rules across sources, with percentages rounded for readability; all findings
reflect a point-in-time snapshot verified as of the report’s stated “as of” date.

67

2026 STATE OF THE SOFTWARE SUPPLY CHAINThe Consumption Layer: This section is based on Sonatype’s analysis of Maven
Central download telemetry to measure real-world consumption of known vulnerable
vs. fixed component versions. We constructed a dataset of components with publicly
disclosed vulnerabilities and an available remediated (fixed) release, then measured
how frequently vulnerable versions continued to be downloaded relative to their fixed
counterparts over the report’s stated time windows. Downloads are treated as a con-
sumption signal (what build systems actually pull), not as a proxy for unique users,
and results are reported in aggregate to quantify avoidable risk—cases where vulner-
able versions remain in active use even though safer versions exist.

The Ecosystem Layer:
Prevalence of EOL components
We analyzed a representative sample of more than 3,000 enterprise SBOMs. For
each SBOM, we examined the fully resolved dependency graph, including all transi-
tive dependencies, and identified the number of package versions that were end-of-
life. We calculated the percentage of EOL components per SBOM and then aggre-
gated these results across all enterprises to measure overall EOL prevalence.

Number of EOL components with unpatched CVEs
We analyzed a database of over 11 million package versions with known end-of-life
status and known, unpatched CVEs. This analysis identified approximately 81,000
EOL package versions with unpatched vulnerabilities. To estimate ecosystem-wide
impact, we weighted this dataset against the broader population of open-source
package versions, normalizing for selection bias introduced by database coverage
and sourcing constraints. This produced an estimated total of more than 400,000
end-of-life package versions with unpatched CVEs across open-source ecosystems.

Breakdown of EOL Components by Registry
We analyzed a database of over 11 million package versions with known end-of-life
status and grouped them by package registry. Within each ecosystem, we calculated
the percentage of package versions that are end-of-life versus those that are currently
supported. This resulted in a per-ecosystem end-of-life rate, as shown in the chart.

68

APPENDIX2026 STATE OF THE SOFTWARE SUPPLY CHAINF R O M   G U E S S W O R K  TO   G R O U N D E D :   A I   AG E N T S
W I T H   R E A L   W O R L D   I N T E L L I G E N C E

We analyzed a sample of enterprise applications scanned over a three-month window
(June–August 2025), filtering to valid scans (those with >10 components) to remove
setup/test/incomplete results. For apps with multiple stages, we selected the most
operationally mature snapshot using the hierarchy compliance > operate > release
> build > develop > proxy, and then took each app’s first valid scan within the period.
Analysis focused on four ecosystems (Maven, npm, PyPI, NuGet) and used direct
dependencies identified by Sonatype’s component recognition as upgrade candi-
dates; apps that migrated into/out of an ecosystem during the window were kept to
reflect real-world complexity.

We compared five upgrade strategies: No Breaking Changes (highest version score
without breaking changes), Latest (most recent by publication date), Sonatype Best
(highest version score regardless of breaking changes), Sonatype Security Hybrid
(use No Breaking Changes only if it achieves a perfect security score of 100, other-
wise fall back to Best), and an LLM strategy where GPT-5 (reasoning_effort=medium)
returned a JSON recommendation (version, confidence, short rationale) per depen-
dency (≈37,000 components, processed asynchronously with concurrency). Break-
ing-change effort was modeled using four buckets (0–5, 6–20, 21–100, 101+ changes)
mapped to estimated hours and cost at $94/hr (conservative lower bound), with
SemVer fallbacks when telemetry is unavailable (patch→L1, minor→L2, major→L3; L4
requires explicit data).

Security outcomes were measured via a 0–100 security score derived from Sona-
type vulnerability intelligence, combining the worst-severity issue with the count of
distinct vulnerability types (log-transformed to reflect diminishing marginal impact).
Strategy comparisons used Welch’s t-tests across primary outcomes (security score
change and breaking-change count) at  α=0.05.

69

2026 STATE OF THE SOFTWARE SUPPLY CHAINSonatype  is  the  leader  in  AI-driven  DevSecOps.  As  the  maintainers  of  Maven  Central  and  creators
of  Nexus  Repository,  Sonatype  has  spent  two  decades  pioneering  how  the  world  manages  and
secures open source software — making Sonatype the trusted authority for modern software supply
chains. With  unmatched  open  source visibility  and  a  unified  product  suite  built for  modern  software
development,  Sonatype  gives  enterprises  the  intelligence  and  automated  governance  they  need  to
harness the full potential of open source and AI. Sonatype handles the complexity behind the scenes:
guiding component and model selection, blocking harmful malicious code, automating dependency and
vulnerability management, and ensuring faster, more reliable builds — so developers spend more time
on  innovation  and  less  time  on  remediation  and  rework. Trusted  by  more  than 15  million  developers,
Sonatype  helps  power  secure,  modern  software  development  at  nearly  2,000  global  organizations
including 70% of the Fortune 100. To learn more about Sonatype, please visit www.sonatype.com.