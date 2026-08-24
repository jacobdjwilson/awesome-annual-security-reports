2
0
2

6MSPTHREAT

REPORT

How Modern Attacks Abuse Trust and Identities
How Modern Attacks Abuse Trust and Identities
How Modern Attacks Abuse Trust and Identities
How Modern Attacks Abuse Trust and Identities

Contents

Foreword ................................................................................................................................. 3

Introduction ............................................................................................................................4

Key Findings ............................................................................................................................5

The 2025 Threat Landscape ...................................................................................................6

Ransomware in 2025: A Shift in Frequency and Strategy

Software Supply Chain Attacks

Potentially Unwanted Programs Trojanized for Higher Impact

SSL VPN Compromises

The Continued Rise of ClickFix in 2025

AI Cybersecurity Threats

From Insights to Action: How ConnectWise Can Help ....................................................... 21

Methodology: How We Build This Report  ..........................................................................22

2

Foreword

The most damaging incidents in 2025 didn’t rely on novel exploits or advanced malware. Instead,

attackers succeeded by abusing trust.

Attackers consistently exploited identities that were assumed to be legitimate, software that was

assumed to be safe, automation that was assumed to be reliable, and users who believed they were

following normal instructions. These attacks did not break systems; they blended into them.

For managed service providers (MSPs), this represents a fundamental shift in the nature of risk. MSPs

are no longer defending isolated endpoints or individual networks. They are defending interconnected

ecosystems where access, updates, tooling, and users are deeply interdependent. When trust fails

at any point in that ecosystem, the consequences extend quickly across clients, vendors, and shared

infrastructure.

The MSPs that succeed in the years ahead will be those that move beyond reactive security models and

rethink how trust is granted, monitored, and enforced across the environments they manage.

Patrick Beggs

Chief Information Security Officer, ConnectWise

3

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORT
Introduction

The 2026 MSP Threat Report analyzes the most significant threats observed throughout 2025, drawing

from real-world incident response investigations, ConnectWise partner intelligence, and industry

research. The findings focus specifically on attack patterns that materially impacted MSP-managed

environments and the small and midsized businesses (SMBs) they support.

Rather than cataloging every emerging tactic or malware family, this report concentrates on how

attackers consistently gained access, why defenses failed, and what those failures reveal about

modern MSP environments. Across investigations, adversaries favored techniques that were reliable

and repeatable.

Each section of this report examines a major threat category observed in 2025 and the growing

influence of artificial intelligence on threats and attacks. We analyze real incidents and translate those

findings into actionable guidance to strengthen defenses in the year ahead.

This report is a blueprint for enhancing security posture throughout the year. Share its insights with your

teams, integrate its findings into risk assessments, and prioritize recommended actions that best fit your

operational environment.

4

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORT
Key Findings

Initial access was rarely sophisticated,
but it was highly effective

 ▪ Software supply chains amplified blast radius

Compromises of upstream packages, installers, and

Most successful intrusions began with credential abuse,

update mechanisms allowed single intrusions to

misconfigured VPN infrastructure, or user-initiated

cascade across thousands of downstream environments,

execution. Attackers did not need zero-day exploits

often without immediate detection.

when valid access paths already existed.

 ▪ User-mediated execution became a

 ▪ Trust was the primary attack surface

dominant technique

Adversaries repeatedly abused trusted identities,

Techniques such as ClickFix demonstrated that

software updates, system utilities, and user behavior.

convincing users to manually execute commands is one

Security controls that assumed trust rather than verifying

of the most reliable ways to bypass traditional endpoint

it were routinely bypassed.

and email defenses.

 ▪ Ransomware surged to record levels with

faster, more disruptive attacks

Reactive security models consistently
failed MSP environments

Ransomware activity intensified in Q4 2025, making it

Detection after execution was often too late.

the most dangerous period of the year. Groups such as

Environments with limited identity monitoring, weak

Akira moved rapidly from access to impact, targeting

application controls, or poor visibility into execution

backup infrastructure, harvesting credentials, and

context suffered the greatest impact.

exfiltrating data before defenders could respond.

AI increased attacker scale, not visibility

While AI’s role is often invisible in incident telemetry

(sensor data collected from security incidents), its

impact was evident in phishing quality, fraud realism,

malware iteration speed, and operational efficiency.

5

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORT
The 2025 Threat Landscape

The cyberthreat landscape facing MSPs and their clients intensified throughout 2025, driven by a sharp increase in ransomware

activity and a broader shift in how attackers achieve scale and impact. Rather than relying on single exploits or isolated malware

campaigns, adversaries combined multiple access paths, including credential abuse, social engineering, software supply chain

compromise, and AI-assisted techniques, to move quickly from intrusion to monetization.

Ransomware was the most visible and damaging result of this convergence. Victim counts increased significantly year over year,

reversing prior declines and reinforcing ransomware as the preferred endgame for a wide range of threat actors. This growth was

not fueled by new encryption techniques, but by more reliable access methods. Attackers focused on stealing credentials, abusing

remote-access infrastructure, and exploiting trusted workflows to deploy ransomware faster and at greater scale.

Several factors contributed directly to the rise of ransomware:

 ▪ Supply chain attacks accelerated across public

inside, adversaries moved quickly, disabling defenses,

package registries, targeting maintainer accounts,

stealing data, and deploying ransomware with minimal

CI/CD pipelines, and upstream distribution channels.

dwell time. These incidents highlight the elevated risk

These incidents reinforced a critical reality: MSPs

MSPs face when remote access infrastructure is not

inherently inherit the security posture of their vendors

actively monitored and maintained.

and software ecosystems. Even trusted packages,

updates, and automation tools can become delivery

 ▪ 2025 marked a turning point in the practical

mechanisms for malicious code when upstream

maintainers are compromised.

 ▪ User-driven attacks such as ClickFix surged in

frequency and sophistication. These campaigns

persuade users to run commands manually under the

guise of browser verification, file repair, or system

troubleshooting. By shifting execution onto the user,

attackers bypass traditional security controls and

leverage built-in system utilities to initiate infection

chains. The increasing reliability of this technique has

made it a preferred initial access method across multiple

malware families.

use of AI within cybercrime. While AI often leaves

no direct artifacts in incident telemetry, its influence

is unmistakable: more convincing phishing lures, rapid

malware iteration, deepfake-enabled fraud, and

automated obfuscation techniques. AI has lowered

the barrier to entry for attackers while increasing

operational scale and precision.

MSPs must assume that attackers will use multiple avenues to

gain access: some technical, some human, some leveraging

trusted software itself. Building resilience requires a layered

approach, including stronger identity security, hardened

remote access, application control, behavioral monitoring,

 ▪ VPN abuse remained one of the most consequential

and user education that reflects modern attack patterns.

intrusion vectors. Weak credential hygiene, legacy

MFA implementations, and misconfigurations enabled

attackers—including ransomware groups such as Akira—

to obtain privileged access with little resistance. Once

While the landscape continues to evolve rapidly, MSPs can

stay ahead by adopting informed strategies and proactive

controls that protect their clients with confidence.

6

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTRansomware in 2025: A Shift in Frequency and Strategy

The 2025 ransomware environment underscored two realities: threats are increasing in quantity, and attackers are adapting

strategies that exploit existing trust relationships, human behavior, and pervasive access mechanisms.

According to recent industry reporting, overall ransomware victim counts surged sharply. One security firm observed a 58% year-

over-year increase in the number of victims added to data leak sites—the highest level on record. Other telemetry echoed this

trend, with incident counts rising significantly across geographies and sectors and fragmented extortion groups filling the void left

by high-profile law enforcement takedowns.

Volume and Reach

Impact and Resilience

Ransomware activity accelerated in both scale and visibility,

The growing sophistication and reach of ransomware

reshaping the overall threat landscape.

translated directly into real-world consequences.

 ▪ Ransomware incidents increased dramatically, outpacing

 ▪ High-impact ransomware events affected organizations

prior years and reversing earlier declines.

of all sizes, from local governments and hospitals to

 ▪ The number of active extortion groups grew, even as

some traditional ransomware-as-a-service (RaaS) gangs

major enterprises, often forcing extended downtime and

costly recovery.

dissolved, resulting in a highly fragmented but resilient

 ▪ Although some defensive measures gained traction,

threat ecosystem.

Tactics and Techniques

such as immutable backups and incident response

planning, the sheer volume and speed of attacks

strained detection and containment capabilities.

As ransomware volumes surged, attackers also refined how

they operated.

 ▪ Double extortion remained the dominant model,

combining file encryption with data theft and extortion

via public leak sites.

 ▪ Attackers increasingly leveraged AI-assisted tooling and

automation to scale phishing, credential abuse, and

lateral movement activity, making initial access faster

and more widespread.

 ▪ Established groups splintered into new variants or were

replaced by smaller, agile operators, complicating

attribution and response.

7

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTAkira Ransomware

Overview

Notable Incidents

Akira Operations

Akira was one of the most disruptive threats we tracked this

As a RaaS, Akira develops ransomware, maintains

year, with activity particularly focused on midsized businesses

infrastructure, and recruits affiliates to help carry out attacks.

across North America and Europe. The attack uses a double-

A large number of Akira ransomware events this year began

extortion model of data theft followed by file encryption.

with VPN compromises, followed by rapid lateral movement

The group’s affiliates leveraged stolen VPN credentials to

gain access to their victims’ networks. Once inside, Akira

operations followed a consistent lifecycle: scan, steal, encrypt.

There was little to no effort to dwell quietly. Operators moved

swiftly, often succeeding in their overall goals.

and ransomware deployment. In many cases, the attackers

used scanners such as Advanced IP Scanner or SoftPerfect

Network Scanner; dumped Active Directory and credential

information using tools such as Mimikatz and Ntdsutil; staged

archives of data using tools such as WinRar; and encrypted

files via the final akira.exe payload across multiple systems.

For SMBs, the risk isn’t that they’re being singled out; it’s

There was also notable exfiltration activity across some

that they’re part of a much larger pool of opportunistic

Akira=related incidents where we observed Rclone, WinSCP,

targets. They’re not picking specific targets, they’re following

and FileZilla being utilized in exfiltration attempts.

the easiest path in. For far too many SMBs, that path starts at

the VPN.

MFA Bypass

Key characteristics of Akira activity in 2025 included:

Multiple incident reports and vendor analyses indicate

that Akira operations were logging into SonicWall SSL VPN

 ▪ Rapid escalation from access to impact with minimal

accounts even when OTP-based MFA was enabled. The

dwell time between initial compromise and ransomware

cause was likely the use of previously stolen OTP seeds or

deployment

 ▪ Early disruption of backup infrastructure aimed at

preventing recovery and increasing operational pressure

 ▪ Consistent use of double extortion pairing encryption

appliance-resident secrets (credentials or seed material

migrated from older device configurations), allowing

attackers to generate or enroll OTP devices and bypass the

second factor.

with aggressive data theft and leak-site pressure

Defense Disabling Via Vulnerable/Legitimate Drivers

 ▪ A focus on SMB-centric environments where limited

(BYOVD)

visibility and weaker identity controls increased the

Observed post-compromise activity often focused on

likelihood of success

This combination of speed, opportunism, and operational

discipline made Akira particularly effective throughout 2025

and reinforced the broader trend of ransomware groups

prioritizing reliability over novelty.

interfering with backup platforms and disabling endpoint

protections. Akira affiliates have been observed harvesting

backup credentials, removing or corrupting restore points,

and using a bring-your-own-vulnerable-driver technique

(deploying a legitimate driver alongside a malicious helper

driver) to disable endpoint protection services prior to

exfiltration and encryption.

8

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTWhat This Means for MSPs

 ▪ Managed detection and response (MDR)

For MSPs and their clients, Akira’s activity highlights several

recurring weaknesses:

Modern ransomware campaigns intentionally blend into

normal activity, making signature-based detections

insufficient. MDR provides continuous, behavior-

 ▪ Privileged VPN access is a consistent starting point

based monitoring to identify early indicators such as

 ▪ Backup Infrastructure is being targeted directly

anomalous authentication, suspicious tool usage, and

 ▪ RDP is enabled far too often on critical systems

 ▪ Data staging and exfiltration happen fast

Strategies for mitigation

attempts to impair security controls. Rapid investigation

and containment at this stage are critical to stopping

attacks before encryption or extortion occurs.

 ▪ Security information and event management (SIEM)

 ▪ Early detection and access control

SIEM strengthens ransomware defense by centralizing

MSPs must prioritize detecting attackers during early

and correlating logs across identity, endpoint, network,

stages of an attack. If your clients rely on VPN based

and backup systems. By analyzing activity holistically,

access and centralized backup platforms, these are

SIEM helps surface coordinated attack behavior that may

the services that need network segmentation, MFA

appear benign in isolation, such as privilege escalation

hardening, and continuous active monitoring. The

combined with backup enumeration. Off-host log

encryption stage is too late. If you’re not catching them

retention also preserves visibility if attackers attempt to

at the VPN login or recon phase, you’re likely catching

delete or tamper with local logs.

them too late.

 ▪ Business continuity and disaster recovery (BCDR)

 ▪ Privileged access management

Even with strong prevention and detection, MSPs must

Ransomware operators depend on elevated privileges

assume some attacks will succeed. Immutable backups

to disable security controls, access backups, and

protect against ransomware operators who deliberately

deploy payloads at scale. Privileged access should

target backup infrastructure early in the attack lifecycle.

be governed by the principle of least privilege, with

Enforcing immutability, isolating backup access from

administrative rights being removed wherever possible.

production credentials, and routinely testing restoration

Enforcing just-in-time elevation and maintaining full

processes ensure recovery remains possible even when

auditability of privileged sessions helps limit blast radius

encryption and extortion attempts occur.

and reduces the likelihood that initial access escalates

into widespread compromise.

Related content
How to detect ransomware >>

How to prevent ransomware >>

9

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTSoftware Supply Chain Attacks

Overview

Modern software development relies heavily on the reuse of trusted components from public repositories. These repositories, and the

dependencies, packages, build tools, and distribution platforms that support them, collectively form the “software supply chain.”

Threat actors frequently target package maintainers or build pipelines because compromising these upstream sources enables

them to distribute malicious, signed updates that dependency managers automatically include in numerous downstream

applications. By exploiting the inherited trust across the supply chain, attackers can bypass security measures, maintain

persistence, and scale impact more efficiently than targeting individual entities directly.

In recent supply chain attacks, maintainers were compromised through phishing and credential theft techniques, such as token

theft or MFA fatigue, reinforcing that identity security remains a critical weakness in supply chain defense.

Notable Incidents

npm

Shai-Hulud 2.0: What happened

The default package manager and public registry for Node.

js and JavaScript, npm, was hit by a worm-style campaign in

September 2025 dubbed “Shai-Hulud.”

In late 2025, a second and even more aggressive campaign

emerged, which was dubbed “Shai-Hulud 2.0.” This variant

was among the fastest spreading npm supply chain attacks

Shai-Hulud: What happened

ever observed.

 ▪ Attackers used stolen maintainer credentials and tokens

to publish trojanized updates to hundreds of packages.

 ▪ These updates executed install-time scripts that

harvested additional secrets (including npm, GitHub,

and cloud keys) and planted hidden GitHub Actions

workflows to persist and spread to more projects.

 ▪ GitHub and npm maintainers removed hundreds

of compromised packages from the registry and

implemented several mitigation steps, including

blocking uploads matching campaign IOCs, rolling out

short-lived tokens, and enforcing phishing-resistant MFA.

The impact: While the total number of impacted downstream

vendors remains unknown, these attacks highlight the severe

 ▪ Unlike its predecessor, Shai-Hulud 2.0 leveraged

automation extensively, enabling rapid propagation

across thousands of packages in a short timeframe.

 ▪ The worm exploited compromised accounts and abused

npm’s ecosystem to inject malicious code at scale,

focusing on persistence and lateral movement.

 ▪ It introduced enhanced evasion techniques, including

dynamic payload delivery and more sophisticated

credential harvesting, targeting not only developer

secrets but also CI/CD environments.

The impact: The campaign’s velocity and automation amplified

its impact, forcing npm and GitHub to accelerate incident

response measures and expand detection capabilities.

implications for application security and public trust in

Shai-Hulud 2.0 underscores the growing trend of

open-source ecosystems.

weaponized automation in supply chain attacks, raising

urgent concerns about the resilience of package registries

and the need for stronger identity and integrity controls.

10

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTPyPI

NuGet

In another ongoing supply chain compromise campaign, PyPI,

Since 2023, NuGet, the public package registry many .NET

has continued to observe waves of phishing attempts where

apps use, have seen recurring waves of supply chain abuse.

attackers send out “verify your account” emails to lead to

Attackers routinely spin up new publisher accounts and

similarly named but spoofed domains designed to trick users

upload malicious packages with names similar to legitimate

into entering their credentials.

and popular packages that are introduced into projects

The campaign began as early as May 2023, but there have

been multiple reported large-scale attempts that persist to

through typos, name confusion or misplaced trust in an

unfamiliar publisher.

this day. Fortunately, PyPI has not had any confirmed cases of

Some campaigns also hijack existing accounts or smuggle

compromise where attackers published malicious packages

code into MSBuild .targets/.props so it runs during restore/

via phished accounts.

build, turning a normal dependency update into an execution

Ruby

path. Microsoft and security vendors routinely flag and

remove these packages and have tightened checks, but the

In mid-September 2025, the Ruby community was hit by

pattern persists, highlighting how a single upstream package

internal strife among the GitHub repo maintainers, wherein

can quietly cascade into many downstream applications

Ruby Central asserted control over key RubyGems and

through ordinary updates.

Whether it’s threat actors or disputes amongst maintainers,

it’s clear that the supply chain itself is delicate and at risk

and requires the same safeguards and scrutiny that a

company would place on its office environments, if not more

so. Considering a successful compromise of a supply chain

can turn one target into many, the importance of proper

security controls surrounding the supply chain should not be

taken lightly.

Bundler GitHub repos, removing or restricting several long-

term maintainers. Since the governance shakeup changed

who can publish, the speed at which fixes get pushed out,

and how keys and releases are managed, it has a potentially

significant impact on future supply chain trust.

Rust

In September of 2025, the Rust team and researchers

disclosed two malicious crates: faster_log and async_println.

These crates impersonated a popular logger and scanned

source trees to exfiltrate crypto wallet keys. They had been

live since late May with thousands of downloads before it was

resolved and the crates were removed, the accounts that

published the crates were suspended, and the rotation of any

exposed secrets were disabled.

11

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTWhat This Means for MSPs

Strategies for mitigation

DevOps who use these supply chains generally have their

own process in place, such as:

 ▪ Selecting reputable packages

 ▪ Reviewing maintainer reputation and release history

 ▪ Verifying signatures or checksums

 ▪ Locking versions

For MSPs, having a proper global application approval

process in place is important, but without proper controls,

it doesn’t necessarily prevent end users from installing

potentially unsafe apps on their work machines.

Industry best practices should be followed by those in charge

of approving and/or pushing applications in commercial

environments including:

 ▪ Implementing endpoint privilege management with

 ▪ Consuming through an approved internal repository,

application control

 ▪ Generating software bill of materials (SBOMs) to

record what is included

Combined, these are a solid layered approach to reducing

risk before code enters the CI/CD pipeline, but they do

not guarantee safety, and not every development team

implements them consistently.

 ▪ Safelisting apps that can be installed, while also

verifying the installers, using data such as file hash and

signer identity, will help prevent the local installation of

malicious applications

 ▪ Accepting installers from only official vendor

channels, verifying hashes and publisher signatures

for any application install, and testing in a controlled

environment before rolling out the application globally

 ▪ Small test rollouts to groups of users with lesser access

before pushing to higher-risk machines with access

to important company or user information can greatly

reduce risk

 ▪ Blocking suspicious download sites globally can

contribute to preventing the inadvertent download of

malicious programs

MSPs have very little control over upstream compromise,

especially updates to applications that have already been

installed. However, they can cut the risk, minimize impact,

and catch bad releases early by sourcing only from trusted

vendors, gating installs with application approval tools, and

staging updates in a safe test and small canary rollouts with a

ready rollback

12

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTPotentially Unwanted Programs Trojanized for Higher Impact

Overview

Not all threats carry the same weight. Potentially unwanted programs (PUPs) or potentially unwanted applications (PUAs)

traditionally sat near the bottom of the threat list. They typically include “free” software that may serve a legitimate purpose for

the victim, including PDF editing, file conversion, contact information lookups, or enabling dark mode on any website. Unlike other

forms of free software (e.g., open source), PUPs don’t have a monetary user cost; the “cost” comes in the form of ads, additional

software, hijacked search results, crypto mining, collection of data about your contacts, or even victim machines being enrolled as

residential proxies.

Historically, these behaviors were considered undesirable but tolerable. Excessive focus on PUPs risked distracting defenders from

higher-impact threats. However, that assumption no longer holds.

In 2025, attackers increasingly weaponized PUPs as a delivery mechanism for persistence, credential theft, and remote control.

What was once endpoint clutter has become a reliable entry point for more serious compromise.

Notable Incidents

Typical PUP behavior

In 2025, the ConnectWise Cyber Research Unit™ (CRU)

and other threat researchers worldwide observed multiple

campaigns distributing what would normally be classified

as traditional PUPs. It was later revealed that PUPs had more

malicious capabilities. Two prominent examples have been

tracked: TamperedChef and EvilAI.

TamperedChef

On their own, the trojanized applications already exhibit

undesirable behavior typical of many PUPs:

 ▪ Bundled adware

 ▪ Additional installers

 ▪ Enrolling the device as a residential proxy, often

presented during installation as a tradeoff for free access

TamperedChef has been distributed via apps for image

This enrolls them as an accessory to a service that makes

searching, recipe searching, AI assistants, PDF editors, calorie

traffic appear to come from a residential ISP ASN. It routes

counting, and product manual searching.

traffic from unknown users through that machine’s IP address

These trojanized apps are pushed via:

 ▪ Malvertising (ads purchased on platforms such as

Google)

rather than using well-known VPNs that can more easily be

tracked and filtered.

Affected application names observed include:

AllManualsReader, ManualReaderPro, JustAskJacky,

 ▪ SEO poisoning (gaming ranking algorithms to promote

OpenMyManual, TotalUserManuals, EffortlessPDF, AppSuite

malicious sites).

To further attempt legitimacy, code-signing certificates are

used to verify the installers, which are often promptly revoked

once abuse is discovered.

PDF Editor, RecipeLister, OneStart Browser, SodukuFunZone,

and multiple similarly branded variants, totaling dozens of

signed installers.

13

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORT
What This Means for MSPs

The resurgence of trojanized PUPs in 2025 highlights a core

challenge for MSPs: modern threat actors are increasingly

using channels that appear legitimate to both users and

security tools. These campaigns exploit gaps in application

hygiene, endpoint privilege, and user behavior, which

are areas that often receive less attention than perimeter

defenses or ransomware prevention.

Preventing these threats requires stronger guardrails around:

 ▪ What software can be installed

 ▪ How elevation is granted

Figure 1:AppSuite PDF Editor was one of several trojanized apps

used in the TamperedChef campaign

 ▪ How endpoints are monitored for unexpected

persistence mechanisms or credential harvesting

Escalation beyond traditional PUP behavior

TamperedChef, the malicious component of these

applications, executes as a JavaScript file using NodeJS.

It makes itself persistent through a scheduled task and in

a registry Run key. It will stop browser processes to copy

the “Web Data” and “Preferences” files containing cookies

that may permit session hijacking as well as theft of other

potentially sensitive data.

behavior.

Strategies for mitigation

 ▪ Application control, endpoint privilege management, and

policy-driven software sourcing should be considered

essential controls to prevent this class of threat.

 ▪ Behavioral monitoring, especially around script

interpreters, browser data access, and persistent

scheduling, plays a critical role in early detection. Since

installers rely heavily on user consent and legitimate

system utilities, traditional file-based detections may not

Trojan malware also operates as a backdoor enabling:

trigger until long after initial infection.

 ▪ Download of files on the victim machines

 ▪ MSPs should also reassess their processes for approving

 ▪ Registry manipulation

 ▪ Execution of arbitrary processes

These capabilities allow a wider range of attacks with

more potential impact than cookie theft or enrollment as a

residential proxy.

utilities and ensure that consumer-grade applications,

even when code-signed, undergo proper validation

before being allowed into managed environments.

Ultimately, 2025 demonstrated that PUPs are no longer

endpoint clutter. They have become a reliable entry point

for attackers seeking persistence, credential access, and

remote control, and MSP environments must treat them

accordingly.

14

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTSSL VPN Compromises

Overview

Throughout 2025, we observed widespread abuse of SSL VPN infrastructure as a primary entry point into SMB and MSP client

networks. Most successful compromises this year did not rely on new exploits; they stemmed from incomplete configuration

hygiene, credential reuse, and exposure of legacy infrastructure.

In many cases, the initial intrusion vector was not particularly advanced. Publicly exposed SSL VPN interfaces, especially those

from SonicWall and Fortinet, were routinely targeted by mass-scanning and credential-stuffing campaigns. Even environments with

MFA in place were not immune, especially those using appliance-based OTP implementations. Our team responded to numerous

incidents this year in which MFA was technically enabled, but attackers still managed to authenticate by enrolling their own device

or using credentials retained from prior firmware generations.

This trend reflects an uncomfortable reality for the MSPs and SMBs: SSL VPNS are often treated as a “set it and forget it”

infrastructure and rarely receive the same attention as endpoint or email security. However, this year made it clear, when these

devices are left exposed and unmanaged, they become the single easiest way into the network.

Notable Incidents

Ivanti (Pulse Connect Secure VPN)

Fortinet Brute Force Campaign

In early 2025, Ivanti Connect Secure SSL VPN appliances were

There was a spike in brute-force login attempts across

widely compromised through exploitation of CVE-2025-

Fortinet VPN portals in early August. These attacks were

0282, a critical pre-authentication remote code execution

confirmed to be part of a coordinated credential stuffing

vulnerability that allowed attackers to gain unauthorized

wave by threat actors. Several partners had login portals

access to VPN gateways without valid credentials. At least 17

exposed without proper perimeter defense mechanisms

organizations were confirmed breached, with investigations

in place, raising serious concern even in the absence of

attributing the campaign to a Chinese state-aligned threat

confirmed exploitation.

actor focused on long term access rather than immediate

monetization.

SonicWall VPN Intrusions

Multiple SMB organizations were compromised through

SonicWall Gen7 VPNs that had been upgraded from older

Gen6 hardware without properly resetting their inherited

credentials. This vulnerability (later tied to CVE-2024-40766)

allowed attackers to log in with valid credentials even when

MFA was enabled. Several of these incidents resulted in full

domain compromise in under two hours.

15

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTSonicWall Cloud Backup Breach

What This Means for MSPs

SonicWall disclosed that attackers had compromised its

VPN appliances are one of the few ways SMBs allow

MySonicWall cloud portal and accessed firewall configuration

persistent privileged access into their networks. While the

backups for a subset of customers. These backups included

intent is often for legitimate purposes, these devices become

hashed credentials, VPN group settings, and appliance

high-value targets for attackers and high-risk points of failure

secrets. For MSPs managing dozens of SonicWall clients

for MSPs. The activity observed in 2025 showed us:

through shared portals, this introduced a wider surface

area for compromise, especially for any clients that had not

rotated any credentials post migration.

Cisco ASA Zero Day Activity

While this campaign appeared to target larger orgs and

government entities, we note it here because many legacy

ASA appliances are still in use across SMB environments. Cisco

confirmed two zero days (CVE-2025-20362 and CVE-2025-

20333) were exploited in the wild to implant persistent malware

directly on the firewall OS. This reinforces that even “trusted”

edge devices should be monitored and routinely upgraded.

 ▪ Default and migrated credentials remain

dangerously common

 ▪ MFA is not enough if implemented poorly

 ▪ Monitoring VPN login telemetry must become standard

 ▪ Vendors aren’t immune to supply chain breaches

 ▪ Strategies for mitigation

MSPs relying on VPNs for remote access, or managing clients

who expose VPNs without proper hygiene, need to treat

these services as critical infrastructure, not background noise.

VPNs should be continuously monitored, regularly hardened,

and protected with strong authentication and access

controls.

16

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTThe Continued Rise of ClickFix in 2025

Overview

Throughout 2025, ClickFix-style social engineering emerged as one of the most reliable and repeatable initial access methods

observed across multiple intrusion campaigns. Rather than relying on exploitation or malicious attachments, ClickFix attacks

manipulate users into manually executing attacker-provided commands under the pretense of routine verification steps,

CAPTCHAs, browser prompts, or security-related actions. This execution model shifts the initial access burden onto the user,

allowing attackers to bypass many traditional security controls by operating entirely through legitimate system utilities and trusted

execution paths.

Target user is lured to
a ClickFix page using
phishing emails,
malvertisements, or
compromised sites

ClickFix page socially
engineers user into
copying/pasting and
running a command

Executed command
downloads and
launches a malicious
obfuscated code

Code delivers malware
like infostealers,
loaders, or remote
access tools (RATs)

Typical ClickFix Attack Chain

system error and BSOD-themed ClickFix lures (tracked by

This pattern has become prominent enough that it was

researchers at Securonix as PHALT#BLYX), designed to create

formalized within the MITRE ATT&CK Framework as Malicious

urgency and reduce hesitation by implying system instability

Copy and Paste (T1204.004), reflecting broader industry

or data loss. Despite differing themes, each of these variants

recognition that manual user execution represents a distinct

relied on the same core mechanic of convincing the user that

and recurring adversary behavior. In practice, ClickFix does

manually executing provided instructions was both safe and

not represent a single lure or campaign style, but a general

necessary.

execution pattern that can be adapted to different themes,

interfaces, and delivery contexts.

As the year progressed, attackers increasingly diversified

how this pattern was presented to users. Variants such as

FileFix reframed manual execution as a required step to

Over time, ClickFix has evolved from relatively simple copy-

and-paste lures into a flexible execution pattern used by

multiple threat actors and malware families. As defenders and

users became more familiar with earlier browser verification

and CAPTCHA-style lures, attackers adapted by introducing

open or repair a downloaded document, while ConsentFix

new narratives that aligned with common user expectations

extended the same copy-and-paste social engineering model

around file handling, system errors, and consent workflows.

into browser-based identity workflows by abusing legitimate

The underlying execution model remained unchanged, but

OAuth consent and authorization flows within the browser

the surrounding context continued to evolve, reinforcing

rather than delivering endpoint malware. Other campaigns

ClickFix’s effectiveness as a durable and adaptable initial

introduced more aggressive visual pressure, including fake

access method.

17

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORT
Notable Incidents

Early 2025: Establishing a Reliable Initial Access Pattern

At the start of the year, ClickFix activity was already present on a meaningful scale and was being actively operationalized by

multiple threat actors. Early campaigns favored consistency and reliability over technical complexity.

Common characteristics of early ClickFix campaigns included:

 ▪ Fake browser verification messages, update prompts,

 ▪ Initiation of the infection chain through legitimate

and security warnings used to convince users to

Windows utilities

manually execute short commands

 ▪ Simple download-and-execute chains that delivered

commodity malware

Figure 2: Clickfix lure pretending to be a Cloudflare CAPTCHA

Figure 3: What it looks like to victims when they paste the malicious command into the Run box

18

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORT
SmartApeSG campaigns

Moving beyond single actor campaigns at scale

Campaigns attributed to SmartApeSG exemplified this early

Early 2025 ClickFix activity also overlapped with a broader

operational model.  Payloads observed during this period

ecosystem of commodity stealers and remote access tools,

frequently included NetSupport Manager as a remote access

including Lumma, Vidar, and similar families frequently

tool, deployed with basic user-level persistence mechanisms.

observed in opportunistic intrusion activity. Telemetry from

Infrastructure rotated frequently, often using compromised

multiple incidents showed ClickFix lures being reused to

sites or short-lived domains, but the underlying lure

deliver these payloads with minimal modification, further

mechanics and execution flow remained stable, indicating

demonstrating that attackers did not need bespoke

early confidence in ClickFix as a dependable initial access

infrastructure or advanced tooling to benefit from the

method.

Filch Stealer campaigns

technique. In many cases, the same execution flow could

support a stealer, a RAT, or a loader with only minor backend

changes. These campaigns established the technique as a

Other early-year ClickFix campaigns demonstrated how

scalable and low-friction initial access method.

easily this execution pattern could support different malware

families without changing the user-facing lure. Campaigns

Later 2025: Refinement and Operational Maturity

delivering Filch Stealer used the same execution entry

By the latter half of the year, ClickFix campaigns demonstrated

point to stage multi-step PowerShell loaders that ultimately

clear signs of operational refinement rather than fundamental

deployed information-stealing payloads with limited

change. The core execution model of manual user execution

remote access capability. While Filch Stealer showed more

through trusted system utilities remained intact, but attackers

complexity than early SmartApeSG deliveries, the ClickFix

increasingly focused on reducing friction and improving

component itself remained minimal, serving only as a reliable

operational resilience. Compared to early-year activity, later

bootstrap mechanism.

Latrodectus campaigns

campaigns showed greater emphasis on infrastructure agility,

payload flexibility, and minimizing observable artifacts.

Similarly, Latrodectus campaigns observed during this period

Fake CAPTCHAs

reinforced the trend toward loader-based delivery while

One of the most visible shifts during this period was the

retaining the same social engineering foundation. In these

growing use of fake CAPTCHA and browser verification

cases, the user-executed step initiated a chain involving script

overlays embedded into otherwise legitimate websites.

execution and installer-based staging, ultimately leading

These pages closely mimicked trusted services and prompted

to reflective loading or sideloading techniques. Although

users to copy short commands into the Run dialog or a

the downstream tooling differed, the initial access method

command shell, maintaining the same ClickFix interaction

remained consistent, underscoring ClickFix’s flexibility across

pattern while improving visual credibility. In several incidents,

both stealer- and loader-centric campaigns.

this initial step triggered PowerShell-based loaders that

retrieved additional stages entirely in memory, leaving little

to no conventional executable footprint on disk. These

campaigns often culminated in stealer-style payloads or

loader frameworks capable of deploying follow-on malware.

19

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTMulti-stage archive-based delivery chains

MSHTA-based execution chains

Another prominent late-year pattern involved multi-stage

While many later campaigns favored PowerShell-centric

archive-based delivery chains, including the use of password-

loaders, others revisited MSHTA-based execution chains

protected archives paired with locally staged extraction

associated with broader ClearFake activity. In these cases,

utilities. In these incidents, the ClickFix prompt initiated a

ClickFix lures led users to execute commands that launched

short loader that fetched both an encrypted archive and the

remote HTA or HTML content, which then staged additional

tooling required to unpack it. The extracted contents typically

script-based execution. Although MSHTA is a well-known

included lightweight loader scripts or executables that

abuse vector, its continued use in ClickFix campaigns

established persistence and launched final payloads. Data

underscores the emphasis on leveraging legitimate, signed

and indicators from these campaigns aligned with information

binaries rather than introducing novel tooling. Some of

stealers such as Vidar, Lumma, StealC, and related families,

these chains also showed overlaps with reflective loaders

though the modular nature of the loaders allowed operators

and HijackLoader-style behavior, suggesting opportunistic

to change payloads without altering the user-facing lure.

blending of techniques rather than tightly coupled

Infrastructure abstraction

malware families.

Several campaigns observed during this period also

demonstrate deliberate infrastructure abstraction. Rather

than embedding full staging URLs in the initial command,

attackers relied on URL shorteners or redirect services to

The end result: CickFix emerged as a proven and
repeatable technique

keep the visible execution step minimal and static while

Across these varied campaigns, the unifying theme was

rotating backend hosts as needed. This approach reduced

efficiency. Commands became shorter, staging logic

the operational cost of infrastructure churn and allowed

moved off-host, and payload delivery became increasingly

the same ClickFix lure to remain effective even as payload

modular. The user-facing interaction changed little, even

locations changed.

as backend execution chains grew more flexible. ClickFix

matured into a delivery method that prioritizes reliability

and adaptability over stealth through obscurity. Attackers

did not abandon the technique as awareness grew; they

optimized it instead. The result was a consistent initial

access pattern capable of supporting a wide range of

malware families and operational goals.

20

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTWhat This Means for MSPs

ClickFix campaigns succeed not because of novel malware

or advanced exploitation, but because they exploit user

trust and legitimate system functionality. For MSPs managing

diverse client environments, this shifts the defensive

challenge away from blocking specific payloads and toward

identifying risky execution contexts and user-initiated

process chains.

Strategies for mitigation

Traditional perimeter controls and file-based detections offer

limited protection when users are convinced to manually

execute commands using built-in tools. As a result, visibility

into how processes are launched becomes more important

than the identity of the final payload. Execution chains that

originate from browsers, script hosts, or the Run dialog box

warrant closer scrutiny regardless of the malware family

involved, particularly when they rapidly transition into

scripting engines or command interpreters.

User awareness also plays a critical role, but it must reflect

modern attack patterns rather than legacy phishing models.

ClickFix lures do not rely solely on malicious links or

attachments. They depend on convincing users that manual

code execution is a legitimate verification or recovery step.

Effective training should explicitly address this behavior and

reinforce that legitimate services do not require users to

paste commands into the Run dialog box or a command shell.

Ultimately, ClickFix’s persistence and refinement

throughout 2025 demonstrate that social engineering-

driven execution remains a powerful and adaptable intrusion

method. MSPs that prioritize execution context, behavioral

telemetry, and user-initiated risk, rather than relying solely

on malware signatures or static indicators, will be best

positioned to detect and disrupt these campaigns early in

the attack chain.

21

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTAI Cybersecurity Threats

Overview

Artificial intelligence (AI) continued to reshape the cyber threat landscape throughout 2025, but not always in ways that are

directly observable from incident data alone. Supply-chain compromises or VPN intrusions include technical indicators that

provide clear evidence of how attackers gained access, but AI’s role in modern attacks often remains hidden behind the scenes.

Why AI activity is hard to observe

Why AI’s impact on the threat landscape still matters

Threat actors are increasingly using AI to accelerate

We include these broader findings in this report because

development, improve lures, automate decision-making,

AI is exerting a massive influence across every stage of the

or obfuscate their code, but these activities typically occur

threat landscape, even when that influence is not directly

before the payload ever reaches a victim environment. By the

measurable in the incidents we respond to. The evolution of

time an attack surfaces within an MSP-managed environment,

deepfake-enabled fraud, LLM-generated phishing content,

the components directly attributable to AI have usually been

prompt-manipulation attacks, and AI-assisted malware tooling

stripped away, leaving a significant visibility gap for incident

demonstrates a rapid acceleration that cannot be ignored.

responders.

While its fingerprints may not always be visible in the artifacts

As a result, it is difficult to determine whether generative AI

was used to craft phishing lures, produce malicious scripts,

automate payload delivery, or support operational planning.

Our visibility into AI-enabled activity depends heavily on

intelligence shared by external research organizations, cloud

providers, and security vendors who monitor upstream

development pipelines, large-scale phishing infrastructure,

and AI-tool abuse patterns that MSP-level incident data simply

cannot reveal.

we analyze, AI is undeniably shaping attacker capabilities,

lowering operational barriers, and expanding the scale and

speed at which threat actors can operate.

For MSPs, understanding this invisible dimension of

threat evolution is critical. The challenges ahead are not

only about detecting malware or blocking suspicious

scripts; they are about recognizing that the tools used

to create these threats are becoming more powerful,

accessible, and automated. AI is enabling attackers to

move faster, disguise intention more effectively, and iterate

through defenses with unprecedented agility. Even when

we cannot point to a specific indicator that “AI was used

here,” the impact is evident in the increasing volume

and adaptability of the threats we face.

22

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTNotable Incidents

Deepfake-enabled fraud and impersonation

allowing extensions with basic scripting access to read

One of the most alarming trends in 2025 was the rise of

and write prompts. Proof-of-concept attacks showed how

deepfake-enabled fraud. In July, a businessman in China lost

compromised extensions could silently alter user inputs,

over $622,000 in a Zoom call scam where attackers used

extract confidential information, and delete chat history to

real-time face-swapping technology to impersonate a trusted

cover tracks.

contact. The victim was convinced to authorize a wire transfer

during the call, only to discover later that the conversation

AI-assisted malware development

never occurred with the real individual. In the United States,

In the fourth quarter, threat intelligence researchers at

AI voice scams dubbed “Grandparent Scam 2.0” targeted

Google’s Threat Intelligence Group (GTIG) observed

seniors by cloning voices of loved ones and requesting

increasingly sophisticated uses of AI tools by malicious actors,

emergency funds. These scams often bypass traditional fraud

including the emergence of PROMPTFLUX, which leverages

detection due to their emotional manipulation and realism.

AI-generated phishing

Microsoft’s Threat Intelligence team flagged a phishing

large language models during execution to dynamically

generate malicious scripts, obfuscate code, and create

malicious functions on demand. Additional threats include

FRUITSHELL, a normal reverse shell that code comments to

campaign in August 2025 that used LLM-generated SVG files

evade LLM-based security scanning, and PROMPTSTEAL (also

to bypass email security filters. These files, disguised as PDF

known as LAMEHUG), a Hugging Face API utilization which

attachments, contained obfuscated JavaScript payloads that

enables the malware to use more than just public-facing

redirected victims to credential-harvesting sites. The attack

chatbots.

used business-related terminology and synthetic structures to

evade detection, suggesting the payloads were crafted using

Prompt injection

generative AI. SVG-based phishing attacks have become

According to GTIG, threat actors continue to employ

increasingly popular due to their ability to embed dynamic

prompt injection techniques to bypass AI safety guardrails

content and evade static analysis. In multiple documented

(e.g., claiming to be working on capture-the-flag exercises

cases, these files passed undetected through VirusTotal and

or cybersecurity research papers). Using LLMs in malware

other scanners, highlighting a significant blind spot in current

has also led to operational security failures on the part of

defenses.

Man-in-the-prompt attacks on AI tools

operators, inadvertently exposing hard-coded information

such as C2 domains and encryption keys to AI models. The

quarter also saw a growing marketplace for AI-enabled

A newly identified threat vector, Man-in-the-Prompt (MitP)

malicious services, including deepfakes, malware generation,

targeting browser-based AI tools like ChatGPT, Gemini, and

and phishing campaigns, that use several different models

Copilot. Researchers at LayerX demonstrated how malicious

that specialize in different areas of development and

browser extensions can intercept and manipulate prompts

exploitation (e.g., WormGPT and FraudGPT). Most of what is

in real time, injecting hidden instructions or exfiltrating

observed in the report is still experimental, but it highlights

sensitive data without user awareness. These attacks exploit

that we should expect to see more of over the next year.

the document object model (DOM) used by AI interfaces,

23

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTWhat This Means for MSPs

For MSPs, the rapid evolution of AI-driven cyberthreats

means that traditional playbooks focused on signature-

based detection and user awareness are no longer enough.

Attackers are using generative AI to automate phishing, create

deepfake-based social engineering, and develop polymorphic

malware that adapts faster than static defenses.

Strategies for mitigation

Reduce risk introduced by AI tooling

 ▪ Enforce browser extension allowlists and monitor for

unapproved data exfiltration.

 ▪ Disable auto-sync features that may expose chat history

or model interactions.

 ▪ Monitor AI usage itself as a potential attack surface

MSPs must now assume that every client organization could

Apply AI defensively with guardrails

face attacks engineered or enhanced by AI, even from

 ▪ Use AI for log correlation, phishing detection, and

relatively low-skilled actors. Mitigation requires adapting

anomaly detection under human oversight.

controls, training, and processes to reflect this shift.

Strengthen verification against impersonation
and fraud

 ▪ Protect against prompt injection and data leakage

through access controls, sanitization, and private or on-

prem AI deployments where possible.

 ▪ Implement stricter verification for financial and account

Translate AI risk into operational action

access requests.

 ▪ Proactively brief clients on AI-enabled threats and their

 ▪ Require multi-channel confirmation, such as verbal

business impact.

verification using known phone numbers.

 ▪ Demonstrate how controls such as dual verification and

 ▪ Expand training beyond email awareness to include AI-

extension policies reduce risk.

generated voice and video impersonation.

 ▪ Integrate these updates into security awareness

Harden software supply chain controls

programs and incident response plans.

 ▪ Treat software dependencies as potential intrusion

vectors, especially with AI-assisted code obfuscation.

 ▪ Encourage the use of signed packages, software bills

of materials (SBOMs), and integrity checks in CI/CD

pipelines.

 ▪ Discourage use of AI utilities from unknown GitHub

repositories, which have become common infection

carriers.

24

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTFrom Insights to Action:
How ConnectWise Can Help

The findings presented in this report underscore a critical truth: the threat landscape is not only expanding but also evolving in

ways that challenge traditional security models.

Defending against modern threats requires shifting security efforts earlier in the attack lifecycle. Identity must be protected as

a primary control plane, remote access must be tightly governed and continuously monitored, and execution behavior must be

visible, not just outcomes. And when prevention fails, recovery must be fast, reliable, and resistant to attacker interference.

ConnectWise delivers integrated Cybersecurity and Data Protection solutions to enforce the principle of least privilege, detect

suspicious behavior early, and ensure rapid recovery even in worst-case scenarios.

Privileged Access Management

Identity and access failures were at the center of many of

the most damaging incidents in 2025. ScreenConnect®

Privileged Access Management helps MSPs reduce this risk

by enforcing least-privileged access and controlling how

administrative sessions are initiated, elevated, and audited.

ConnectWise SIEM™ helps MSPs aggregate and correlate

telemetry across client environments, providing the context

needed to identify abnormal patterns and escalation paths.

SIEM enables faster investigation, supports proactive threat

hunting, and strengthens incident response by ensuring

critical events are not analyzed in isolation.

By removing standing privileges and tightly governing

For MSPs managing complex, multi-tenant environments,

remote access, MSPs can limit the blast radius of credential

SIEM provides the foundation required to move from reactive

compromise and reduce the likelihood that a single stolen

alerting to informed, intelligence-driven defense.

account leads to full domain compromise.

Managed Detection and Response (MDR)

Business Continuity and Disaster Recovery (BCDR)

Ransomware groups in 2025 increasingly targeted backup

Many of the attacks outlined in this report progressed rapidly

infrastructure early in attacks, attempting to delete, encrypt,

because early warning signs went unnoticed. ConnectWise

or corrupt recovery points before deploying ransomware.

MDR™ provides continuous monitoring and expert-led response

In these scenarios, traditional backup strategies often failed

across endpoints, identities, and network activity. By correlating

when they were needed most.

behavioral signals rather than relying solely on signatures, MDR

helps MSPs detect suspicious activity earlier in the intrusion

lifecycle, including techniques that bypass traditional defenses.

Security Information and Event Management (SIEM)

Immutable backup is no longer optional. It is a core resilience

requirement.

x360Recover from Axcient, a ConnectWise company,

provides immutable backups designed to resist tampering,

Modern attacks rarely leave a single, obvious indicator.

even when attackers gain administrative access. By

Instead, they generate weak signals spread across identity

protecting backup integrity and enabling rapid recovery,

systems, endpoints, network devices, and cloud platforms.

x360Recover ensures MSPs can restore systems confidently

Without centralized visibility, these signals are easy to miss.

when preventative and detective controls are bypassed.

25

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTMethodology: How We Build This Report

The ConnectWise MSP Threat Report was first introduced in 2020 to provide MSPs with practical, real-world insight into the

evolving cybersecurity landscape. The report highlights the threats, attack patterns, mitigations, and solutions most relevant to

environments MSPs manage every day.

Our annual MSP Threat Report is made possible by the research and findings from the ConnectWise Cyber Research Unit™ (CRU).

This elite team is composed of experienced threat hunters and cybersecurity professionals with deep expertise in engineering,

IT admin, security operations, incident analysis, and incident response. The team gathers threat intelligence 24/7 from a wide

range of sources, including real-world incident response investigations, telemetry from ConnectWise partner and SMB client

environments, ransomware leak sites, and malicious infrastructure such as botnets and command-and-control networks. By

correlating these data points, the CRU identifies emerging trends, common attack techniques, and recurring points of failure

across MSP-managed environments.

The goal of this report is not simply to document threats, but to translate complex threat intelligence into actionable insight

for MSPs.

About ConnectWise

ConnectWise powers IT businesses by simplifying operations, enhancing experiences, and driving growth. Trusted by IT solution

providers worldwide, ConnectWise sets the standard for innovation and service delivery. For more than 40 years, ConnectWise

has been committed to partner success, delivering software, services, and an open ecosystem of integrations. The ConnectWise

Platform provides unmatched scale and AI-driven automation across PSA, RMM, cybersecurity, and data protection, helping our

partners deliver and secure services more efficiently. Discover how ConnectWise is transforming the IT industry at connectwise.com.

26

<< BACK TO TABLE OF CONTENTS

connectwise.com

2026 MSP THREAT REPORT

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-21", "model": "gemini-3.5-flash-lite"} -->
