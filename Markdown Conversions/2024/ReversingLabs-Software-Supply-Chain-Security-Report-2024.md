# State of Software Supply Chain Security 2024

The official report URL is: https://www.reversinglabs.com/sscs-report

## Table of Contents
- [Foreword](#foreword)
- [Highlights](#highlights)
- [Executive Summary](#executive-summary)
- [Discussion: A Shifting Terrain](#discussion-a-shifting-terrain)
- [Key Trends](#key-trends)
  - [A Supply Chain Visibility Gap](#a-supply-chain-visibility-gap)
  - [More Malicious Open-Source Packages](#more-malicious-open-source-packages)
  - [Malware in the Supply Chain](#malware-in-the-supply-chain)
  - [Attackers Go High and Low with Supply Chain Campaigns](#attackers-go-high-and-low-with-supply-chain-campaigns)
  - [PyPI Overtakes npm as Host for Malicious Packages](#pypi-overtakes-npm-as-host-for-malicious-packages)
  - [A Shift in the Types of Malware Encountered on OSS Package Managers](#a-shift-in-the-types-of-malware-encountered-on-oss-package-managers)
  - [PUA and Protestware Proliferate](#pua-and-protestware-proliferate)
  - [Developer Secrets Leaks Persist](#developer-secrets-leaks-persist)
  - [Open Your AIs!](#open-your-ais)
  - [Private Keys, Web Service Credentials Top Leaked Secrets List](#private-keys-web-service-credentials-top-leaked-secrets-list)
  - [Developers: Mind Those Shortcuts!](#developers-mind-those-shortcuts)
- [State of SSCS Report: Timeline](#state-of-sscs-report-timeline)
- [What Comes Next: The Post-Trust Supply Chain](#what-comes-next-the-post-trust-supply-chain)
  - [Change Is Constant](#change-is-constant)
  - [Regulators Rush In](#regulators-rush-in)
  - [Mind the Guidance](#mind-the-guidance)
- [Recap: Federal Guidance](#recap-federal-guidance)
  - [The NIS2 Directive](#the-nis2-directive)
  - [National Cybersecurity Strategy](#national-cybersecurity-strategy)
  - [Secure by Design, Secure by Default](#secure-by-design-secure-by-default)
  - [Cybersecurity Information Sheet on Defending CI/CD Environments](#cybersecurity-information-sheet-on-defending-ci/cd-environments)
  - [SEC Rules for Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure](#sec-rules-for-cybersecurity-risk-management-strategy-governance-and-incident-disclosure)
  - [Cybersecurity in Medical Devices](#cybersecurity-in-medical-devices)
  - [The Digital Operational Resilience Act (DORA)](#the-digital-operational-resilience-act-dora)
  - [Software Identification Ecosystem Option Analysis](#software-identification-ecosystem-option-analysis)
  - [Recommended Practices for SBOM Consumption](#recommended-practices-for-sbom-consumption)
- [Recap: Industry Initiatives](#recap-industry-initiatives)
  - [Open Software Supply Chain Attack Reference (OSC&R)](#open-software-supply-chain-attack-reference-osc&r)
  - [Exploit Prediction Scoring System (EPSS), v.3.0](#exploit-prediction-scoring-system-epss-v.3.0)
  - [Supply Chain Levels for Software Artifacts, v.1.0](#supply-chain-levels-for-software-artifacts-v.1.0)
  - [SPDX, 3.0 Release Candidate](#spdx-3.0-release-candidate)
  - [CycloneDX, v.1.5](#cyclonedx-v.1.5)
  - [OWASP Top 10 for Large Language Model Applications](#owasp-top-10-for-large-language-model-applications)
- [State of SSCS 2024 Methodology](#state-of-sscs-2024-methodology)
- [About ReversingLabs](#about-reversinglabs)

# Foreword
<a name="foreword"></a>

Mario Vuksan
CEO AND CO-FOUNDER,
REVERSINGLABS

If there were any questions that software supply
chains are the new frontier in cybersecurity, 2023
put them to rest. The past year witnessed more
than a dozen high-profile, targeted attacks on
software supply chains, the impacts of which
were felt across the globe. Those incidents
include the hack of Voice over IP vendor 3CX
and the attacks on Progress Software’s MOVEit
managed file transfer application. The MOVEit
attacks, carried out by the Clop cybercriminal
group, are estimated to have affected 62 million
people around the world whose healthcare data
was stolen.

The lesson of these incidents is clear:
Software supply chains represent the largest
unaddressed attack surface lurking within
businesses today, regardless of whether you are
building or deploying software. And the threats
are not limited to third-party code such as
MOVEit. Recent history shows that proprietary,
commercial, and open-source software all pose
risks to the integrity of IT environments. In 2023
alone, ReversingLabs researchers uncovered
a string of malicious software supply chain
campaigns leveraging open-source repositories
such as npm, Python Package Index (PyPI),
and NuGet. In at least one case, the campaign
we uncovered contained links that suggested
the involvement of the Lazarus Group, a North
Korean state-sponsored threat actor.

As the threats to the software supply chain
grow, they expose holes in the defenses used
by software producers and consumers that
are focused on open-source vulnerabilities.
Today, traditional application security testing
and code-scanning solutions struggle to detect
compromises of development pipelines that
result in malicious modifications to otherwise
sanctioned code, regardless of who wrote it or
where it has been obtained from.

And scrutiny isn’t limited to federal regulators.
Customers will also be looking to hold their
software suppliers to a higher standard. In its
research paper “Mitigate Enterprise Software
Supply Chain Security Risks,” for example,
Gartner states that “A vendor’s inability or
unwillingness to accommodate requests
for attestations or information about secure
software development practices is an adverse
signal of risk and should be disqualifying.”[^1]

We hope with this report to give readers a
map with which to navigate the rapidly shifting
landscape of software supply chain security. We
look at some of the high-level trends in software
supply chain threats and attacks witnessed
in the last year and consider what lies ahead
for both software firms and their customers
in 2024. Throughout this report, we leverage
insights produced by ReversingLabs Software
Supply Chain Security platform, which is
designed to identify critical malware, tampering,
vulnerabilities, exposed secrets, and more
across proprietary, commercial, and open-source
software. Whether you build software or manage
vendor application security, the information
contained in this annual report — and revealed
by our SSCS platform — should be of great
interest. We hope you find this report both
informative and beneficial.

At the same time, end-user organizations that
purchase and deploy software are used to
simply accepting the integrity of signed updates
received from reputable vendors without being
able to interrogate them for unexplained or
malicious features or behavior. Existing tools and
platforms can’t provide an in-depth review of a
vendor’s [software] application or software supply
chain security measures. As Gartner® noted in its
report “Mitigate Enterprise Software Supply Chain
Security Risks,” “Traditional application security
testing tools do not typically attempt to detect
malicious code.”[^1]

Today, both software publishers and buyers
are under pressure to answer a fundamental
question: “Are there any material risks inside
my software?” The ability to conclusively and
confidently answer that question is only going
to grow more important as both software supply
chain threats and scrutiny of development
practices grow. The lawsuit filed in October by
the Security and Exchange Commission (SEC)
against the Austin, Texas-based company
SolarWinds suggests mounting regulatory
scrutiny of companies’ management of cyber
risks and vulnerabilities, including risks facing
software supply chains.

The SEC’s action against SolarWinds
emphatically expresses the regulator’s desire
to not only investigate but also to prosecute
deficiencies in application security programs.
Failure to detect security lapses will no longer be
seen as mere deficiencies; they will be treated
as criminal negligence and fraud. That is an
ominous sign for software producers. The loss
of enterprise value for public investors in the
wake of incidents such as those at SolarWinds,
Okta, MOVEit, and other firms serve as warnings.
SEC rulemaking will likely be reinforced by
other U.S. and global bodies. There are already
calls on Capitol Hill for more supply chain
transparency and security. At the same time, we
can expect that the current AppSec tools will not
be sufficient to provide control of material risk.
Expect the requirements on software producers
to rise in line with NIST guidance reports such as
Cybersecurity Supply Chain Risk Management
(C-SCRM). Exceeding expectations will be a valid
protective measure for many CISOs that seek to
avoid criminal prosecutions or other sanctions.

# Highlights
<a name="highlights"></a>

ReversingLabs analysis of software supply chain attacks and data from its industry-leading software risk
analysis platform reveal important trends related to software supply chain security. Among them:

The Software
Supply Chain Is
a Blind Spot:

Software Supply
Chain Attacks Are
Getting Easier:

Change Is
Coming... and
More of the Same:

Attacks such as the
compromise of VoIP vendor
3CX laid bare a yawning visibility
gap that hampers the ability of
both software makers and their
customers to detect software
supply chain compromises and
defend their organizations from
malicious actors.

ReversingLabs analysis of the
compromised 3CX Desktop App
showed how the inability
to track the evolution of
compiled binaries and spot
unexplained changes exposed
both software publishers and
their customers to attacks and
security compromises.

2023 saw software supply
chain attacks become both
easier to carry out and
ubiquitous.

Once the pinnacle of
cyber-offensive campaigns,
software supply chain
attacks in 2023 became just
another variety of malicious
online activity.

For example, Operation
Brainleeches, identified by
ReversingLabs in July, showed
elements of software supply
chain attacks supporting
commodity phishing attacks
that use malicious email
attachments to harvest
Microsoft.com logins.

ReversingLabs observed
substantial changes in both the
quantity and kinds of malicious
code turning up on open-source
platforms such as npm, PyPI,
and NuGet.

Take a step back, however,
and the root causes of supply
chain risks and attacks were
unchanged in 2023. So-called
typosquatting attacks designed
to fool developers into grabbing
malicious or compromised
code were common. At
the same time, developers
continued to leak sensitive
information such as API keys,
security tokens, and credentials
for popular services such as
AWS, Google, and Microsoft via
published code.

# Executive Summary
<a name="executive-summary"></a>

The barrier to software supply chain attacks was lowered in 2023, and it is likely to continue to come
down in 2024. Less sophisticated cyber actors are in search of unobstructed pathways into sensitive IT
environments to steal sensitive data, deploy ransomware and other malware, or cause disruptions. The
abuse of weak links in software supply chains supported both targeted- and indiscriminate campaigns
in the last year. That is according to an analysis of software supply chain threats to proprietary,
commercial, and open source code by ReversingLabs.

The proliferation of supply chain attacks in 2023 comes amid steady growth in the number of malicious
packages detected on popular, open-source platforms such as npm and the PyPI. ReversingLabs saw
a 28% increase in malicious packages spread across those two open-source repositories through the
first nine months of 2023 compared with all of 2022. That growth is the latest evidence for a multiyear
explosion in software based threats facing development organizations.

For example, leveraging its Software Supply Chain Security and malware analysis platforms,
ReversingLabs detected a more than 1,300% increase in threats circulating via open-source package
repositories between 2020 and 2023. That includes a 400% increase in threats found on the PyPI
platform in 2023 alone. ReversingLabs discovered more than 7,000 instances of malicious PyPI
packages in the first 9 months of 2023, the vast majority of which were classified as ‘infostealers’.

The landscape of supply chain threats and attacks also broadened and shifted in 2023. The year saw
continued evidence that nation-state actors are targeting weak software supply chains to infiltrate
targeted organizations. For example, ReversingLabs published research on “VMConnect,” a campaign of
two dozen malicious Python packages posted to PyPI, with links to North Korea’s Lazarus Group.

But 2023 also saw evidence that even script kiddies that use automated tools for phishing and
ransomware attacks were leveraging open-source platforms such as npm and PyPI to host malicious
wares and to launch attacks. ReversingLabs’ discovery of the Operation Brainleeches campaign in July
revealed attackers using packages published to npm to support turnkey email phishing campaigns
targeting Microsoft 365 users.

Finally, 2023 brought more evidence that development organizations continue to struggle to manage
their growing software supply chain risks, even as governments in the United States and elsewhere
sought to raise the bar for secure software development. For example, ReversingLabs analysis of
open-source repositories such as npm, PyPI, NuGet, and RubyGems shows that the leaking of sensitive
information such as web service access tokens and API keys is common across major platforms
including Google, Amazon, GitHub, and Slack. A new source of secrets leaks? OpenAI, the maker
of ChatGPT, which ranked just behind Google as the source of secrets leaks on both the PyPI and
RubyGems platforms.

Federal efforts to raise the bar for software security are still in their infancy — and remain confined to
federal contractors. Nevertheless, the pressure is building on software makers to clean up their acts, as
shown by the SEC’s legal action against SolarWinds. And private-sector insurers are increasingly attuned
to the security of software supply chains as they evaluate both compliance and overall cyber risk.

That means the hard work of securing software supply chains will fall to the private-sector and individual
software makers. In this report, we hope to help you understand the dimensions and landscape of
software supply chain risk in 2023 and how that is likely to play out in 2024.

# Discussion: A Shifting Terrain
<a name="discussion-a-shifting-terrain"></a>

Attacks on software supply chains and development pipelines were an extreme rarity not that long ago.
Incidents such as NotPetya, the 2017 compromise of the Ukrainian software firm Intellect Service’s M.E.
Doc software; or the 2019 campaign targeting SolarWinds Orion were cyber-offensive outliers: top-tier
attacks carried out by sophisticated and persistent actors, often with links to nation-states and using
never-before-seen techniques.

Today, in 2024, such attacks are far more common. The last 12 months have seen software supply chain
attacks shed complexity and boost accessibility. Data compiled by ReversingLabs shows that the barrier
to entry for supply chain attacks has lowered steadily in the last year, and everything indicates that it will
continue to do so in 2024.

These malicious actors hope to take advantage of pronounced monitoring and detection gaps that leave
both software producers and their customers incapable of spotting signs of code tampering and abuse
within development pipelines or of threats hiding in compiled software artifacts. For example, for the
first time, ReversingLabs this year found strong evidence connecting software supply chain campaigns
to the spread of malicious code, including incidents in which attackers pushed malware such as rootkits
directly via open-source packages[^2], embraced code obfuscation and non-mainstream languages, and hid
malware inside compiled binaries[^3] to make it harder for victim organizations to detect.

# Key Trends
<a name="key-trends"></a>

Here are some of the key trends ReversingLabs identified in 2023 and expects to continue to track
into 2024.

## A Supply Chain Visibility Gap
<a name="a-supply-chain-visibility-gap"></a>

Focusing on big, headline-grabbing
attacks is often a good way to highlight
the cutting-edge tools in an attacker’s tool
belt, connect the dots between seemingly
obscure challenges in securing development
pipelines, and recognizing the high stakes of a
successful supply chain compromise.

That was the case with the hack of 3CX’s
desktop client application. As ReversingLabs
researcher Karlo Zanki wrote in March, the
successful compromise of a 3CX Desktop App
software update left clear indicators that could
have tipped off 3CX to the attackers’ presence and their successful tampering with the client update
before it was distributed to 3CX customer environments.

Running the 3CX MIS installer packages through the ReversingLabs Software Supply Chain Security
platform triggered warnings on two files: d3dcompiler_47.dll, a standard library used with OpenJS
Electron applications such as 3CX Desktop App, and another Electron file, ffmpeg, which ReversingLabs
saw referencing d3dcompiler, the tampered file. The initial alert was related to the detection of a
Microsoft digitally signed binary that was modified post-signing so as not to alter or break the
signature’s integrity. While not malicious, per se, this technique has been seen by ReversingLabs being
used by malicious actors to ferry malicious code onto a system under the cover of a legitimate, digitally
signed binary.

Upon closer investigation, Zanki discovered the smoking gun: a combination of RC4 encrypted shellcode
inserted into the signature appendix of d3dcompiler, coupled with a reference to the d3dcompiler library
added to the ffmpeg library. When invoked, the altered ffmpeg file extracts RC4 encrypted malicious
content from the signature appendix of d3dcompiler.

In the end, ReversingLabs research into the hack suggested that the 3CX supply chain incident was
caused by the compromise of the repository from which the Electron application binaries were fetched
during the build process, with attackers swapping legitimate versions of the ffmpeg and d3dcompiler
libraries in the compromised repository with malicious versions compiled by the attackers after
modifying publicly available ffmpeg source code.

The lesson for software makers is clear: Cyberthreats to organizations today extend well beyond
software vulnerabilities and insecure code. Software makers and their customers increasingly need the
ability to scan both raw code and compiled binaries for behaviors and unexplained changes that may
indicate they have been tampered with. As threats such as malicious open-source modules and
software dependencies, CI/CD compromises, and code tampering proliferate, organizations will need the
tools and know-how to close the visibility gap and detect such threats during development and before
the software ships.

## More Malicious Open-Source Packages
<a name="more-malicious-open-source-packages"></a>

One of the most basic measurements of supply chain insecurity is the quantity of malicious packages
circulating on commonly used platforms, such as open-source repositories. By that measure, 2023
saw an increase in software supply chain risks.

npm, PyPI, and RubyGems

RubyGems

PyPI

npm

![Malicious Package Detection 2023: npm, PyPI, and RubyGems]

According to data collected by ReversingLabs, more than 11,000 malicious packages were detected
across three major open-source software platforms in 2023: npm, PyPI, and RubyGems. That marks an
increase of 28% over 2022, when a little more than 8,700 malicious packages were detected.

Multiple large-scale spam campaigns during 2023 affected monitored open-source repositories.
Since these were quickly taken down and posed no significant risk to the development community,
ReversingLabs has opted to exclude them from its statistics.

Additionally, ReversingLabs observed an increase in the number of packages that contained malicious
functionality that is obfuscated or encrypted, making it harder for conventional security tools to detect.
For example, in February, ReversingLabs reported on the discovery of aabquerys, a malicious npm
package that downloaded second- and third-stage malware payloads to systems that have downloaded
and run the npm package.

![Deobfuscated Content of jquery.js File]

As with other examples of malicious open-source packages, aabquerys sent up a number of red
flags, including the similarity of the package name to another, legitimate npm module: abquery. That
suggested a “typosquatting” attack, in which malicious actors try to sow confusion and fool developers
into downloading a malicious package that they mistake for a legitimate one.

More important was the discovery of obfuscated code within one of the aabquerys files. Code
obfuscation in modules published in public, open-source repositories usually correlates with suspicious
activity - as it did with aabquerys[^4] and malicious campaigns like IconBurst and Material Tailwind, which
preceded it.

To be sure: malicious software supply chain campaigns such as aabquerys are often primitive and
gain little traction in the open-source community. However, even primitive or unsuccessful campaigns
may be harbingers of larger operations. And they are a warning to development organizations of the
growing risks lurking on open-source repositories. The same techniques employed by malicious actors
— typosquatting, code obfuscation, implanted malicious functions — in the hands of sophisticated cyber
adversaries can power successful attacks on development teams.

## Malware in the Supply Chain
<a name="malware-in-the-supply-chain"></a>

As ReversingLabs noted: open-source platforms such-as npm are increasingly being used to support
malicious campaigns. The form that support takes has been pretty consistent in recent years. For
example, open-source modules might perform a kind of phishing function: pushing links to malicious
downloads in the hope that developers will click them. Or they might harvest sensitive user or system
data or fetch commands that execute scheduled tasks or cronjobs that increase attackers’ control over
the target system.

But in 2023, ReversingLabs witnessed increasingly bold software supply chain attacks, with an
open-source package on the npm platform, node-hide-console-windows, that directly facilitated the
planting of a rootkit, r77, on developer systems.

As ReversingLabs wrote at the time, the npm malicious campaign shared many similarities with previous
software supply chain attacks. Those included the application of typosquatting that had the malicious
package mimicking the legitimate and popular npm package, node-hide-console-window. Digging deeper,
however, ReversingLabs found malicious code inside of the file index.js, which is specified as the main
software component inside the package manifest. When index.js ran, it fetched an executable that was
detonated immediately thereafter and which ReversingLabs quickly identified as a copy of DiscordRAT
2.0, an open-source malware. With the help of a !rootkit command, DiscordRAT launched the r77 rootkit
and spawned two registry subkeys to hide the rootkit’s presence.

That’s not unusual. In May, for example, ReversingLabs observed a malicious npm package that
contained a copy of TurkoRat, an open-source infostealer. A similar campaign observed this year
delivered Luna Grabber, another open-source infostealer. However, foisting a rootkit directly from within
a malicious open-source package was a first for ReversingLabs researchers and further complicates the
software supply chain risk landscape. Expect to see more incidents like this in 2024.

## Attackers Go High and Low with Supply Chain Campaigns
<a name="attackers-go-high-and-low-with-supply-chain-campaigns"></a>

For more than a decade, “software supply chain attacks’’ have been a hallmark of sophisticated,
nation-state cyber actors. The NotPetya attacks on Ukrainian public- and private-sector firms followed
a compromise of a M.E. Docs financial software update. The hack of the SolarWinds Orion software
application opened the doors to both U.S. government agencies and Fortune 50 firms. These campaigns
set compromises of development pipelines and signed software artifacts from reputable publishers
as the gold standard for sophisticated cyber offensive campaigns conducted by the most capable of
cyber adversaries.

But the barrier to successful supply chain attacks has been dropping steadily in recent years, as more
and more malicious actors saw green fields of opportunity sprouting on open-source platforms like npm,
Python Package Index, and others. And 2023 finally saw aspects of software supply chain attacks crop
up at the bottom of the cyber offensive barrel: turnkey, automated attacks associated with a packaged
“phishing kit” sold and marketed on the cyber underground.

Specifically, Operation Brainleeches which ReversingLabs wrote about in July, documented a campaign
that began in May 2023 and saw npm packages used to host files used in widespread phishing
campaigns. Analysis by ReversingLabs researcher Lucija Valentić found that the files were likely derived
from turnkey phishing kits sold on the cyber underground and targeting Microsoft 365 customers in an
effort to obtain their login credentials.

![Flow of the Activity When Malicious Attachment is Opened in Web Browser]

Files contained in the npm package standforusz contained the raw components of the malicious
phishing campaign. That included the files DEMO.txt, jquery.js, jquery.min.js, and package.json.

The DEMO.txt file contained HTML code that mimicked the login for Microsoft.com and the URL of a
remote server, hxxp://ourwhite.brainleeches.xyz, which harvested credentials from the phishing login
form that are sent. The diagram above shows the flow of the activity once the malicious attachment is
opened in their web browser.

Interestingly, another branch of the same campaign was found to be more in line with traditional supply
chain attacks. A second group of seven packages linked to the Operation Brainleeches campaign could
be used both for hosting files used in email phishing campaigns and also for performing supply chain
attacks targeted at application end users, based on ReversingLabs analysis.

The npm open-source repository, in Operation Brainleeches, functioned mostly as the host of one stage
of a malicious campaign, rather than as a platform to target application developers with malicious or
tampered with open-source modules.

Expect to see more of this in 2024, as well. ReversingLabs open-source research uncovered the
remnants of a very large number of similar email phishing attachments spawned by slightly different, but
closely related phishing kits to the one used in Operation Brainleeches. That suggests that the modules
ReversingLabs identified were likely part of a broader wave of attacks orchestrated by actors outfitted
with powerful and automated tooling.

## PyPI Overtakes npm as Host for Malicious Packages
<a name="pypi-overtakes-npm-as-host-for-malicious-packages"></a>

One of the most notable changes in 2023 was the emergence of PyPI as a platform for distributing
malware. The number of malicious packages detected by ReversingLabs researchers on PyPI was
7,207 in the first nine months of 2023. That is a 400% increase over the number of malicious PyPI wares
detected in all of 2022 (1,741). At one point, new submissions to PyPI were even halted (temporarily)
amid a spike in malicious, typosquatting packages pushed via automated attacks.

Package repo threats: npm, PyPI, and RubyGems

RubyGems

PyPI

npm

npm

![Package repo threats: npm, PyPI, and RubyGems]

During the same time period, ReversingLabs
observed a marked decrease in malicious
packages hosted on the npm repository from
6,979 malicious packages detected during 2022
to just 3,961 detected through the first nine
months of 2023 — a 43% decrease.

This is a curious development. The historical
preference of malicious actors to post their
wares on npm made sense: JavaScript is the
most popular coding language for the web, and
npm is a far larger repository with more than 2.5
million packages, compared to 499,000 on PyPI.
That larger repository of packages attracts more
developers. Choosing to drop your lures on npm
was simply abiding by the old adage to “fish
where the fish are.”

400%

increase in
malicious PyPI

So what changed? The shift to PyPI may simply reflect the growing popularity and use of the Python
programming language. IEEE Spectrum’s 2023 ranking of development languages put Python squarely
on top of the pack, ahead of Java and C++. And Python has even overtaken the Java and C languages in
popularity among enterprise developers, according to reports.

But other factors may also be at play. Python offers some unique advantages for malware authors not
found in other languages. For example, in June, ReversingLabs researchers encountered a novel attack
that used compiled Python byte code (PYC) to evade detection by most AppSec testing tools, which can
scan Python source code (PY) files but not PYC files.

New Python exploits
evade detection by
traditional application
security tools.

The malicious package, named fshec2, marked
the first time ReversingLabs researchers
observed a compiled Python file (full.pyc) inside
the PyPI package that contained malicious
functionality. The design of the package
suggested that its primary purpose was to use
strategies that enabled the malicious actors to
evade detection by common AppSec tools, which
resulted in the execution of a malicious package
that collects usernames, hostnames, directory
listings, and so on.

As the use and popularity of Python grows — driven in part by the embrace of machine learning and
artificial intelligence — ReversingLabs expects to see this trend toward more Python Package Index
threats and attacks continue in 2024.

## A Shift in the Types of Malware Encountered on OSS Package Managers
<a name="a-shift-in-the-types-of-malware-encountered-on-oss-package-managers"></a>

The past year also brought shifts in the kinds of threats that are prevalent on leading open-source
repositories. For example: the number of malware samples identified as “downloaders” that
ReversingLabs encountered on the PyPI platform exploded, jumping more than 20-fold, from 272 in all of
2022 to 5,500 in the first 10 months of 2023.

That growth reflects the larger shift to PyPI for hosting open-source malware and the preference
among malware authors to distribute malware using downloaders, said Zanki. But the full scope of these
attacks stretches beyond PyPI and the Python language.

> Usually the Stage 2 malware isn’t even written in Python.
> It’s a native binary, or compiled in some non-mainstream
> language like Rust or GO. That may reflect the development
> preferences of the malware authors — or it may be an attempt
> to evade detection by using languages that are harder to
> parse and, therefore, spot malicious functions.

Karlo Zanki, Reverse Engineer at ReversingLabs

In contrast to what happened on PyPI, incidents of downloaders decreased significantly on the npm
platform between 2022 and 2023. On that platform, which saw an overall reduction in the number of
malicious packages, there was a slight (10%) increase in the number of infostealer packages detected in
2023. Similarly, incidents of spam and potentially unwanted applications (PUA) also jumped.

As all that suggests, the picture on npm is complicated. ReversingLabs analysis shows that much of the
malware discovered on npm and labeled as “infostealers” is not being used in active campaigns. Rather,
many of the malicious packages ReversingLabs discovered can be classified as “proof of concept
malware” or, alternatively, as tooling used in red team assessments of organizations’ cyber defenses.

Spam

PUA

Downloader

Trojan

Infostealer

Backdoor

![npm Malicious Packages by Type - 2020-2023]

## PUA and Protestware Proliferate
<a name="pua-and-protestware-proliferate"></a>

Similarly, the packages marked as “spam” and “Potentially Unwanted Applications (PUA)” are not
explicitly malicious but still warrant attention from development and security organizations. In many
cases, ReversingLabs found that these packages were precursors of malicious campaigns on npm. They
include test packages and malware in the earliest stages of development. In other cases, ReversingLabs
came across the work of bug bounty hunters who were leveraging customized open-source packages
to facilitate their probes of other platforms. Whether they contain malicious functionality or not, these
spam and PUA packages need to get flagged by developers so that they are not integrated into projects,
Zanki said.

With an increasingly volatile political landscape globally, “protestware” also turned up in ReversingLabs
scans of open-source repositories such as npm. That included ReversingLabs discovery, in
November 2023, of an npm package, e2eakarev version: 7.1.0, that was published in late October and
describes itself as a “free Palestine protest package.” Lucija Valentić, a software threat researcher
at ReversingLabs, also detected another application, sweater-comb, version 2.1.1, which was first
published in August 2023 by the firm Snyk, that used es5-ext, a previously identified and well-known
piece of protestware targeting Russian developers and protesting that country’s invasion of its neighbor
Ukraine. That package has been detected in 179 different npm packages just since July.

Protestware is typically not malicious, but its existence is still a reason for developers to be concerned,
said ReversingLabs Chief Software Architect Tomislav Peričin.

> The risks that developers and software consumers face have
> never been higher, and that includes political messages. Having
> software perform random acts of political activism does little
> for the specific cause. But it does decrease the