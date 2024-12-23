# 2022 Threat Detection Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Trends](#trends)
- [Ransomware](#ransomware)
- [Supply chain compromise](#supply-chain-compromise)
- [Vulnerabilities](#vulnerabilities)
- [Affiliates](#affiliates)
- [Crypters-as-a-service](#crypters-as-a-service)
- [Common web shells](#common-web-shells)
- [User-initiated initial access](#user-initiated-initial-access)
- [Malicious macOS installers](#malicious-macos-installers)
- [Remote monitoring and management abuse](#remote-monitoring-and-management-abuse)
- [Linux coinminers](#linux-coinminers)
- [Abusing remote procedure calls](#abusing-remote-procedure-calls)
- [Defense validation and testing](#defense-validation-and-testing)
- [Top threats](#top-threats)
- [Cobalt Strike](#cobalt-strike)
- [Impacket](#impacket)
- [SocGholish](#socgholish)
- [Yellow Cockatoo](#yellow-cockatoo)
- [Gootkit](#gootkit)
- [BloodHound](#bloodhound)
- [Rose Flamingo](#rose-flamingo)
- [Silver Sparrow](#silver-sparrow)
- [Bazar](#bazar)
- [Latent threats](#latent-threats)
- [Top techniques](#top-techniques)
- [Conclusion](#conclusion)

## Introduction
Welcome to Red Canary’s 2022 Threat Detection Report. Based on in-depth analysis of over 30,000 confirmed threats detected across our customers’ environments, this research arms security leaders and their teams with actionable insight into the threats we observe, techniques adversaries most commonly leverage, and trends that help you understand what is changing and why. This is our most expansive report to date, but our intention remains the same: The Threat Detection Report exists to help you understand and detect threats.

How to use the report:
- Start perusing the most prevalent techniques, trends, and threats to see what we’ve observed in our customers’ environments.
- Explore how to detect, mitigate, and simulate specific threats and techniques.
- Talk with your team about how the ideas, recommendations, and priorities map to your security controls and your overall strategy.

New trends section
Red Canary’s security operations team performs three primary activities:
- Our Intelligence team seeks to identify and understand distinct threats.
- Our Detection Enablement and Detection Engineering teams seek to understand these threats and engineer solutions that reliably detect them and enable timely investigation.
- Our Incident Handling team is charged with responding to threats before they harm customers.
In each of these areas, we’ve identified trends that help us understand how threats are evolving and how we as defenders must evolve in kind. From the continued scourge of ransomware to high-impact vulnerabilities and supply chain attacks, this section synthesizes intelligence with insights from the front lines of threat detection and response.

l Introduction

## ACKNOWLEDGEMENTS
Thanks to the 100+ security experts, writers, editors, designers, developers, and project managers who invested countless hours to produce this report. And a huge thanks to the MITRE ATT&CK® team, whose framework has helped the community take a giant leap forward in understanding and tracking adversary behaviors. Also a huge thanks to all the Canaries—past and present—who worked on the 2019, 2020, and 2021 Threat Detection Reports. The Threat Detection Report is iterative, and parts of the 2022 report are derived from previous years.

This report wouldn’t be possible without all of you!

## Methodology
Since 2013, Red Canary has delivered high-quality threat detection to organizations of all sizes. Our platform collects as much as a petabyte of security telemetry every day and leverages a library of roughly 3,000 detection analytics to surface potential threats that are analyzed by our Cyber Incident Response Team (CIRT). Confirmed threats are tied to corresponding MITRE ATT&CK® techniques and specific threats to help our customers clearly understand what is happening in their environments. A significant portion of this report is a summary of confirmed threats derived from this data.

Creating metrics around techniques and threats is a challenge for any organization. To help you better understand the data behind this report and to guide you as you create your own metrics, we wanted to share some details about our methodology.

Behind the data
To understand our data, you need to understand how we detect malicious and suspicious behavior in the first place. We gather telemetry from our customers’ environments and feed it through a constantly evolving library of detection analytics. Our detection analytics are mapped to one or more ATT&CK techniques and sub-techniques, as appropriate. When telemetry matches the logic in one of our detection analytics, an event is generated for review by our detection engineers.

When a detection engineer determines that one or more events for a specific endpoint surpasses the threshold of suspicious or malicious behavior, they
l Methodology

create a confirmed threat documenting the activity on that endpoint. These confirmed threats inherit the ATT&CK techniques that were mapped to the analytics that first alerted us to the malicious or suspicious behaviors.

It’s important to understand that the techniques and sub-techniques we’re counting are based on our analytics—and not on the individual review performed by our detection engineers, during which they add more context to detections. We’ve chosen this approach to maximize efficiency and consistency. However, the limitation of this approach is that context gleaned during the investigation of a threat does not inform its technique mapping, and by extension, some small percentage of threats may be mapped incorrectly or incompletely. That said, we continually review these confirmed threats, and we do not believe that there are a significant number of mapping errors in our dataset.

How do you count?
You may be wondering how we tally the scores for the Threat Detection Report. Our methodology for counting technique prevalence has largely remained consistent since our first Threat Detection Report in 2019. For each malicious or suspicious detection we published during the year, we incremented the count for each technique reflected by a detection analytic that contributed to that detection (excluding data from detections of unwanted software). If that detection was remediated and the host was reinfected at a later date, a new detection would be created, thus incrementing the counts again. While this method of counting tends to overemphasize techniques that get reused across multiple hosts in a single environment (such as when a laterally moving adversary generates multiple detections within a single environment), this gives appropriate weight to the techniques you are most likely to encounter as a defender.

For the purposes of this report, we decided to set our rankings based on techniques, even though the majority of our analysis and detection guidance will be based on sub-techniques. This seemed to be the most reasonable approach, considering the following:
- Sometimes we map to a technique that doesn’t have sub-techniques
- Sometimes we map to sub-techniques
- Sometimes we map generally to a technique but not to its sub-techniques
In cases where a parent technique has no subs or subs that we don’t map to, we will analyze the parent technique on its own and provide appropriate detection guidance. However, in cases where sub-technique detections are rampant for a given parent technique, we will focus our analysis and detection guidance
l Methodology

entirely on sub-techniques that meet our requirements for minimum detection volume. To that point, we decided to analyze sub-techniques that represented at least 20 percent of the total detection volume for a given technique. If no sub-technique reached the 20 percent mark, then we analyzed the parent.

What about threats?
Our Intelligence team seeks to provide additional context about threats to help improve decision-making. By understanding what threats are present in a detection, customers can better understand how they should respond. Throughout 2021, the Intelligence team sought to improve how we identified and associated threats in detections. We chose to define “threats” broadly as malware, tools, threat groups, or activity clusters. We took two main approaches to associating a detection to a threat: automatically associating them based on patterns identified for each specific threat and manually associating them based on analysts’ assessments conducted while reviewing each detection.

In contrast to our technique methodology, we counted threats by the unique environments affected. Whereas for techniques we counted multiple detections within the same customer environment as distinct tallies, for threats we decided to only count by the number of customers who encountered that threat during 2021. This is due to the heavy skew introduced by incident response engagements for laterally moving threats that affect nearly every endpoint in an environment (think ransomware).

Had we counted threats by individual detections, ransomware—and the laterally moving threats that lead up to it (e.g., Cobalt Strike)—would have been disproportionately represented in our data. We believe our approach to counting gives an appropriate measure of how likely each threat is to affect any given organization, absent more specific threat modeling details for that organization. It also serves as a check against the acknowledged bias in the way we count technique prevalence.

Limitations
There are a few limitations to our methodology for counting threats, as there are for any approach. Due to the nature of our visibility (i.e., that we predominantly leverage endpoint detection and response data), our perspective tends to weigh more heavily on threats that made it through the external defenses—such as email and firewall gateways—and were able to gain some level of execution on victim machines. As such, our results are likely different than what you may see from other vendors focused more on network or email-based detection.

While the top threats are worth focusing on, they are not the only threats to consider, since other impactful ones may be unidentified and therefore
l Methodology

underreported. The analysis and detection guidance in this report is reflective of the overall landscape, and, if implemented, offers a great deal of defense-in-depth against the threats that most organizations are likely to encounter.

Knowing the limitations of any methodology is important as you determine what threats your team should focus on. While we hope our top 10 threats and detection opportunities help you and your team prioritize, we recommend building your own threat model by comparing the top threats we share in our report with what other teams publish and what you observe in your own environment.

## Trends
Red Canary performed an analysis of emerging and significant trends that we’ve encountered in confirmed threats, intelligence reporting, and elsewhere over the past year. We’ve compiled the most prominent trends of 2021 in this report to show major themes that may continue into 2022.

The technique and threat sections of this report are focused on detection data and identifying prevalent ATT&CK techniques and threats in those detections. The trends section takes us one step beyond that data and allows us to narrate events that might not be prevalent but may be emergent or otherwise deserve your attention.

How to use our analysis
The next page highlights the most prevalent threats occurring in our customer environments, so we can assume they are prevalent elsewhere. We include advice for responding to each threat and offer detection opportunities so you can better defend your organization. Some defenders may be able to take our detection guidance and apply it directly, while others may not. Regardless, defenders without a detection engineering function can still make use of the actionable analysis of each threat written by our Intelligence team experts.
l Trends

Ransomware
Ransomware continued to dominate the 2021 threat landscape, and we observed operators take new approaches.

Affiliates
The threat landscape continued its trend toward a software-as-a-service (SaaS) economy, muddying the already murky waters of attribution.

User-initiated initial access
We observed an uptick in threats that occurred after users sought out content which, often unbeknownst to them, was malicious.

Linux coinminers
Coinminers once again dominated the Linux threat landscape.

Abusing remote procedure calls
Intrusions leveraging remote procedure calls (RPC) made waves, particularly PetitPotam and PrintNightmare.

Defense validation and testing
Confirmed testing comprised almost one quarter of our detections in 2021, with many coming from open source tools.

Malicious macOS installers
Malicious installers led to rotten Apples and adware, as macOS systems continued to be targeted.

Remote monitoring and management abuse
Adversaries continued to use and abuse legitimate remote monitoring and management (RMM) software to move data and control infected hosts.

Crypters-as-a-service
Crypters like HCrypt and Snip3 joined the ranks of other “as-a-service” threats.

Common web shells
Adversaries exploited web applications with help from web shells such as China Chopper, Godzilla, and Behinder.

Supply chain compromises
Supply chain compromises were a major theme, starting with SolarWinds, Kaseya and NPM package compromises mid-year, and ending with Log4j.

Vulnerabilities
Adversaries exploited vulnerabilities affecting popular enterprise platforms to drop web shells, spread ransomware, and more.

## Ransomware
Ransomware continued to dominate the 2021 threat landscape, with operators taking new approaches.

Throughout 2021, ransomware remained one of the top threats to every organization. While some groups focused on traditional encryption, 2021 also marked the rise of additional tactics such as double extortion, which amplifies an adversary’s leverage and further compels victims to pay up. Ransomware has become particularly challenging to track and prevent due to several trends we observed in 2021, discussed below.

The affiliate model
One challenge in responding to ransomware intrusions is that different adversaries are often involved at different phases of the intrusion. Ransomware groups usually rely on multiple affiliates to give them initial access to an environment before they encrypt files or take other actions. This makes tracking ransomware groups even more difficult, as intrusions can be a “mix and match” of different affiliates providing access to different ransomware groups.

Red Canary carefully tracks affiliates of ransomware groups and the malware they use, since these adversaries are the ones who sometimes gain initial access to an environment. These affiliates frequently use crimeware such as Bazar and Qbot to gain initial access to an environment, later passing off access to ransomware groups. A few common combinations of malware and ransomware we observed in 2021 include:

| TR END | MALWARE FAMILY (PRECURSOR) | RANSOMWARE GROUP |
|---|---|---|
|  | Qbot | Egregor |
|  | Qbot | Sodinokibi/REvil |
|  | Qbot | Conti |
|  | Bazar | Conti |
|  | IcedID | Conti |

Some things change, but some things stay the same
Challenges in understanding the ransomware landscape are not limited to tracking affiliates and payloads. Defenders must also contend with new groups emerging and others seemingly disappearing (often to be reincarnated in a different form as another group). Some of the ransomware families we bid farewell to in 2021 were Egregor, Sodinokibi/REvil, BlackMatter, and Doppelpaymer. While some seemed to fade away due to law enforcement actions, others disappeared for reasons that researchers haven’t pinned down.

Where one ransomware family disappeared, however, another was ready to step into its place. 2021 saw the dawn of many new ransomware families, including BlackByte, Grief, Hive, Yanluowang, Vice Society, and CryptoLocker/ Phoenix Locker. Many new ransomware families displayed close similarities to old families that “disappeared,” leading analysts to assess that known adversaries simply resurfaced using a new name. For example, Grief ransomware displayed many similarities to Doppelpaymer, including its deployment following Dridex malware.

Beyond encryption
A significant ransomware trend in 2021 was the increase in adversaries expanding their threats beyond data encryption. Multiple ransomware groups pivoted to stealing and exfiltrating data before encrypting it, then demanding payment to prevent the data from leaking publicly on a dark web site. While this practice isn’t new (it dates back to at least 2019), what was significant in 2021 was the number of groups who adopted this approach—to the point where it became the standard.

Adversaries realized they could demand payment for more than just the threat of a data leak or encryption. An adversary known as Fancy Lazarus (no affiliation with Fancy Bear or Lazarus Group) extorted victims by threatening to conduct a distributed denial of service (DDoS) intrusion if they didn’t pay.
l Ransomware

TAKE ACTION
There is no one simple way to prevent ransomware. The same security approaches you take to prevent any malware also should help prevent ransomware. It’s critical to regularly update software, as we often see ransomware after operators exploit a vulnerability in an internet-facing application. Additionally, internet-facing remote desktop protocol (RDP) connections without multi-factor authentication (MFA) are a common ransomware vector, making MFA for any accounts that can log in via RDP a high priority.

Ransomware also frequently gets into an environment as a follow-on payload for malware delivered via phishing emails. Looking for these malware families, such as Qbot, Bazar, and IcedID, can be an effective way to identify a potential ransomware intrusion chain early and stop it in its tracks. Robust detection for other common post-exploitation behaviors and tools like Cobalt Strike are also effective in limiting the impact of ransomware, as adversaries conduct multiple phases before data exfiltration and encryption.

It’s also important to remember that backups are no longer sufficient ransomware protection. While creating offline backups is an excellent security practice and may help restore an environment after a ransomware intrusion, organizations cannot rely on this entirely because adversaries regularly exfiltrate data before encryption, although this too offers potential opportunities for detection. Backups will allow an organization to get back up and running more easily, but will not protect you against leaked data.

While this report focuses on what security teams can do, when it comes to ransomware, it’s also important to remember that this problem is monumental and extends beyond defenders. Policymakers are also taking a close look at ransomware, and it’s necessary for the security community to help them better understand what we do so they can make better decisions.

## Supply chain compromise
Supply chain compromises were a major theme in 2021, starting with SolarWinds, Kaseya and NPM package compromises mid-year, and ending with Log4j.

Supply chain compromises were prevalent in 2021, and these incidents aren’t going away any time soon. It’s important to understand the different types of supply chain compromises. To state it simply, a supply chain compromise occurs when an adversary compromises a software developer, hardware manufacturer, or service provider and uses that access to target customers who use the affected software, hardware, or service. For example, the SolarWinds and Kaseya incidents involved an adversary compromising update servers to target customers of the companies’ IT management software. Separately, NPM package and Log4j incidents involved adversaries exploiting open source libraries in sweeping compromises that impacted products that use Log4j or NPM packages as a dependency—as well as anyone who uses those products directly. Each of these incidents made headlines in mainstream media as well as infosec publications.

SolarWinds
Adversaries compromised SolarWinds, accessed the update infrastructure for its Orion IT management software, and sent backdoored updates to the company’s thousands of customers in December 2020, affecting organizations well into 2021. The trojanized Orion platform updates included a legitimately signed dynamic link library (DLL) file, and some featured backdoor functionality that, after a dormancy period lasting as long as two weeks, initiated communication with command and control (C2) servers. Adversaries identified targets of interest for further exploitation and conducted follow-on activity such as installing additional malicious binaries. These malicious binaries were used to install a backdoor where adversaries could access the victim organizations’ accounts. SolarWinds had a massive impact across many networks, and it took months for enterprises to investigate and respond. This compromise initiated important discussions about supply chain risks that remain relevant in 2022 and beyond.

Kaseya
In July 2021, adversaries exploited vulnerabilities in Kaseya VSA IT Management software in a campaign ultimately designed to deploy Sodinokibi ransomware, also known as REvil. VSA is popular among managed service providers (MSP)
TR END
l Supply chain compromise

that use it to remotely administer IT systems. The adversaries exploited zero days to gain remote control over the MSPs’ VSA installations, which they used to infect the MSPs’ customers’ endpoints with ransomware. Kaseya estimated that about 50 direct customers who were running Kaseya VSA systems—and between 800 and 1,500 other businesses—were impacted by this breach. While the damage was not as bad as it could have been, this incident further highlights the importance of tracking supply chain threats. It also resulted in significant attention from the U.S. government, which later indicted the adversaries responsible for the intrusion. Read about how Red Canary responded to the compromises and protected several customers from ransomware infections.

NPM package compromises
Node Package Manager (NPM) is a repository for publishing node.js projects, including libraries that developers download and incorporate into their software to perform specific mathematical functions, process data in specific ways, visualize data, and more. In October 2021, adversaries compromised an open source JavaScript library with more than 7 million weekly downloads and used it to distribute password stealers and coinminers. At the time, the NPM registry did not require author accounts to use multifactor authentication (MFA), which led to an unknown adversary hijacking the registry accounts of multiple package authors. After hijacking, the adversary published malicious versions of the legitimate packages that contained malware. Victims included package authors and end users of applications relying on those packages. One package, ua-parser-js, was downloaded around 8 million times a week at the time and is used by Google, Amazon, Facebook, IBM, and Microsoft. The U.S. Cybersecurity and Infrastructure Agency (CISA) published a security alert about the incident, warning victims to update to a safe version.

There were many other NPM compromises throughout the year, most notably us-parser-js. Prior to this compromise, an adversary copied the legitimate ua-parser-js library and combined it with malicious code to publish a malicious library. Following this compromise, an adversary took control of two NPM packages, coa and rc. These incidents used a combination of XMRig coinminer on macOS and Danabot on Windows. Red Canary continues to track this activity.

Log4j
Log4j is a popular Java logging library underlying many third-party applications that was hit with a remote code execution vulnerability in December 2021. The primary threats initially exploiting this vulnerability were coinminers and botnets, though the community feared exploitation would expand because of Log4j’s massive intrusion surface. In some scenarios, the Log4j library was affected by a remote code execution vulnerability.
l Supply chain compromise

One reason the community didn’t observe a large volume of exploitation in the first few days may be that these vulnerabilities are highly application-specific, depending on how they’ve implemented Log4j. This means an adversary could not have crafted a single exploit that would have had a broad impact on many types of applications at once. Though it took adversaries a few weeks to ramp up targeting, in late December 2021 and early 2022, internet-facing VMware Horizon servers using vulnerable versions of Log4j became a target for multiple operators. Adversaries were likely attracted to VMware Horizon because it is widely used and often internet-facing. We anticipate the continued targeting of internet-facing applications using vulnerable versions of Log4j for months to come.

TAKE ACTION
One of the best ways organizations can be prepared is by accurately inventorying all of the hardware, software, and service providers they rely on and trust. This will assist in quick response when an inevitable supply chain concern arises. While it sounds commonplace, normal defense-in-depth strategies can also help prevent supply chain compromises from turning into impactful intrusions. Endpoint detection and response (EDR) tools coupled with network detection tools will help you detect malicious post-exploitation activity in the event an adversary gains access to your network through a trusted third party. While there may be nothing you can do to prevent a dependency or a vendor from being compromised, there is quite a lot you can do to detect and prevent follow-on compromise, including detection opportunities we’ve shared throughout the rest of this report.

## Vulnerabilities
In 2021, adversaries exploited vulnerabilities affecting popular enterprise platforms to drop web shells, spread ransomware, and more.

Several high-profile vulnerabilities made it into the collective consciousness of the security community in 2021. ProxyLogon and ProxyShell targeted Microsoft Exchange servers and affected a massive number of systems, sometimes leading to ransomware deployment. The exploitation of vulnerabilities in Kaseya’s VSA appliance software also led to ransomware deployment on some of the thousands of organizations that used Kaseya software for remote administration of endpoints. In the latter half of the year, adversaries exploited multiple vulnerabilities in Zoho’s ManageEngine suite of products. PrintNightmare and an MSHTML vulnerability caused a ruckus among the security community and media; however, their actual impact appears to have been limited.

An important nuance to call out is that vulnerabilities are just flaws in code—a threat must exploit that vulnerability. Given the frequency with which vulnerabilities are disclosed and the ease with which adversaries can exploit newly reported weaknesses, particularly in common applications, Red Canary focuses on identifying and detecting the behavior we observe surrounding exploitation of a vulnerability. We recommend other organizations do the same. Understanding the threats and the ways in which adversaries operate in compromised networks allows defenders to protect against malicious activity regardless of the means by which their environment is accessed.

ProxyLogon (CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065)
In March 2021, Microsoft released details of four Exchange Server vulnerabilities collectively known as “ProxyLogon.” If chained together, the vulnerabilities would allow an adversary remote code execution on a targeted Exchange server. Multiple adversaries, including the suspected Chinese state-sponsored group HAFNIUM, used the vulnerability chain to drop web shells and collect data from thousands of Exchange servers. Other adversaries used the DearCry ransomware to target unpatched servers as well. Microsoft released patches for these vulnerabilities at the time of initial reporting.
TR END
TAKE ACTION
We’ve outlined several of 2021’s major vulnerabilities below, along with some detection guidance. Detecting exploitation of a vulnerability from an endpoint perspective can be difficult and depends on how exploitation occurs in practice. We have tried to supply detection guidance as close to the point of exploitation as possible. In other cases, we provide detection opportunities that would most likely appear as follow-on behavior, such as suspicious child processes or registry modifications. The targeting of vulnerabilities in enterprise applications and platforms is unlikely to slow down in 2022, so it’s important to detect the threats that exploit them head-on.
l Vulnerabilities

Microsoft Exchange Mailbox Replication service writing Active Server pages
Adversaries exploited ProxyLogon to drop web shells on vulnerable systems, which manifested through the msexchangemailboxreplication.exe service writing an ASPX file to disk. Malicious web shells will likely be placed on the web server in a web-accessible directory. The following analytic looks for the Exchange mailbox replication service creating ASPX files.

```
process == msexchangemailboxreplication.exe
&&
filemod_extension == .aspx
```

ProxyShell (CVE-2021-31207, CVE-2021-34523, CVE-2021-34473)
Exchange servers remained a target throughout 2021. In July, Microsoft released details of three new vulnerabilities in the Exchange server, which were dubbed “ProxyShell.” ProxyShell exploitation allows an adversary to remotely execute code without authentication. Following the exploitation, adversaries dropped web shells to conduct reconnaissance, move laterally, and in some instances, deploy ransomware. Where ProxyLogon seemed to have a high impact over a short period of time, ProxyShell seemed to persist throughout the year; we detected exploitation as late as December. DetectingProxyShell exploitation is similar to ProxyLogon mentioned above, specifically msexchangemailboxreplication.exe writing an ASPX web shell to disk.

PrintNightmare (CVE-2021-34527)
On July 1, security researchers and Microsoft released details of a new vulnerability dubbed “PrintNightmare” (CVE-2021-34527). PrintNightmare permits an unprivileged user to remotely obtain elevated privileges on any system running the print spooler service, which is enabled by default. It abuses a vulnerability in how the print spooler service fails to properly authenticate users attempting to load a printer driver dynamic link library (DLL). This zero day affected all editions of Windows, allowing code execution with local SYSTEM-level privileges.

Though the vulnerability was concerning, there were not many reported campaigns exploiting it. That said, ransomware operators such as Vice Society and Magniber have exploited the vulnerability to gain initial access, and therefore it’s worth looking out for. We observed a single malicious instance of PrintNightmare exploitation leading to precursor ransomware behaviors.
l Vulnerabilities

Windows print spooler service spawning cmd.exe
PrintNightmare exploitation results in a shell being opened on the targeted system as a child process of the spooler service. This detection analytic identifies the Windows print spooler service spawning a shell on the system.

```
parent_process == spoolsv.exe
&&
process ==  cmd.exe
```

Kaseya VSA (CVE-2021-30116)
On July 2, adversaries leveraged multiple vulnerabilities in Kaseya Virtual Systems Administrator (VSA) to distribute Sodinokibi ransomware, also known as REvil. VSA allows IT administrators to remotely administer endpoints. By compromising this software, an adversary gains remote execution capability to a large subset of customer endpoints, especially if Kaseya is operated by a managed service provider (MSP).

Red Canary detected the initial behavioral activity using a preexisting analytic for identifying certutil.exe decoding content, as detailed below. Our Intelligence team had tracked Sodinokibi prior to this, which helped us identify the malicious registry modification of blacklivesmatter seen below and attribute it to Sodinokibi.

Certificate utility tool (certutil.exe ) decoding content
This detection analytic will detect certutil.exe running with the -decode option. Adversaries frequently leverage certutil to decode Base 64-encoded content.

```
process ==  certutil.exe
&&
command_line_includes (decode)
```
l Vulnerabilities

ManageEngine products (CVE-2021-40539, CVE-2021-44077, CVE-2021-44515)
In November and December, we observed likely exploitation of remote code execution vulnerabilities in two different Zoho ManageEngine products: ADSelfService Plus (CVE-2021-40539) and ServiceDesk Plus (CVE-2021-44077). In one case, an incident response partner determined that ADSelfService Plus was used for initial access prior to deploying ransomware. The FBI noted that advanced adversaries exploited a vulnerability in a third ManageEngine product, Desktop Central. ManageEngine products are widely used among IT departments to manage various services across the enterprise. As such, this presents adversaries with a wide attack surface. Organizations using ManageEngine products in their environment should update accordingly. Patches for all the vulnerabilities listed here are available via ManageEngine.

Keytool.exe spawning system shell or PowerShell
For the vulnerability in ADSelfService Plus (CVE-2021-40539), we observed adversaries use the Java utility Keytool to move a web shell from the initial directory it was dropped into. As such, keytool.exe spawning shells should be investigated, and the following detection analytic should surface related activity.

```
parent_process == keytool.exe
&&
process == (cmd.exe || powershell.exe)
```

## Affiliates
The threat landscape continued moving toward a software-as-a-service (SaaS) economy, muddying the already murky waters of attribution.

The term “affiliate” has been increasingly used to describe the cybercrime ecosystem’s evolution into a software-as-a-service (SaaS) economy. Borrowed from the subscription-based software specialization strategy, an “affiliate” refers to the provider-customer relationship of malicious services. In the cybercrime ecosystem, several SaaS variants have emerged, from phishing-as-a-service (PhaaS) to access-as-a-service to crypter-as-a-service to ransomware-as-a-service (Raas). It has never been easier to find an adversary for hire.

This service specialization across the phases of an intrusion has led to a proliferation of partnering, muddying the waters of what was once a relatively consistent collection of tactics across campaigns. As adversaries swap subscribers and pass off payloads, identifying and anticipating the progression of a compromise becomes more challenging. To meet this challenge, we need to distinguish the affiliate activity at each stage of the campaign.

Tracking threats at Red Canary
Tracking affiliates is tricky, and to help explain why we think it’s so important, we want to share some background on our threat tracking journey. At Red Canary, we primarily track threats by documenting their observable behaviors in the form of tactics, techniques and procedures (TTP). When we first set out on this intelligence mission, we began by clustering the most prominent and prevalent threats within our data. We often focused on the primary payload as a means of referring to the threat within a detection—think Qbot, TrickBot, or Cobalt Strike. Often we would see one or more of these threats progressing to another threat, especially in the wild west of active incident response engagements.

Throughout 2021, we realized that referring to activity as an Emotet phishing campaign or a Qbot phishing campaign was confusing. The activity we observed before and after Emotet or Qbot sometimes varied, while other times, we noticed the same patterns in how different malware families gained initial access. This realization helped us determine that patterns within filenames or infrastructure indicated that these characteristics likely belonged to their own initial access cluster—a delivery affiliate—rather than a simple malware payload as we had initially been referring to them. Understanding the relationships between these related threats enables us to better understand and respond to the overall ecosystem of the threat landscape.
TR END
l Affiliates

Prominent affiliates in 2021
The process of teasing out the distinguishing characteristics that allow us to separate distinct clusters into more granular components is constantly evolving, as are the threats themselves. While we’ve been tracking some affiliates, such as TA551 (named by Proofpoint), for quite some time, others came into focus more recently as our research progressed throughout the course of 2021. Breaking down intrusions into their component parts helps us better keep pace with the nature of the affiliate-based economy adversaries operate in today.

In 2021, we began identifying patterns in multiple phishing affiliates dropping variants of the Bazar family of malware, also referred to as “Baza.” Derived from the use of .bazar top-level domains for C2 when it was first observed in the wild, this family has lent its name to multiple initial access vectors, campaigns, and components, including BazarLoader, BazarCall, and BazarISO. The multiple components under the umbrella of the Bazar family highlight the importance of differentiating the initial access from the payload. We have seen BazarBackdoor delivered by other prominent phishing affiliates, such as TA551, and have even seen behavior echoing some of the earliest campaigns that delivered BazarBackdoor surface in the latter half of 2021, delivering a resurgent Emotet as its payload.

Incorporating findings from other researchers helped us test hypotheses and add context to our understanding of several other affiliated threats. The prominence of Qbot in our detections and as a ransomware precursor led us to further scrutinize the XLSX phishing lures that delivered it. As a result of this research, we created a distinct profile for the TR delivery affiliate (which we also observed delivering IcedID). Distinguishing these components would not have been possible without other researchers who shared their findings, such as Brad Duncan.

Shifting away from phishing affiliates, we appreciated Morphisec’s great reporting on HCrypt and Snip3 in the first half of the year, the first time crypter-as-a-service crossed our radar. This helped us better break down several other clusters of activity to distinguish the hallmarks of the crypter from the initial phishing campaigns, such as Aggah, or the myriad RAT payloads HCrypt typically delivered.
l Affiliates

TAKE ACTION
Analysts can better track affiliates by focusing on patterns in each phase of an intrusion and comparing similarities and differences to help distinguish when activity has passed from one affiliate to the next. To do this, you can ask questions of the data and compare answers across distinct incidents where you observed overlaps.

Here are some example questions to consider:
- Does the email that delivered this payload belong to a phishing affiliate, or is this entire campaign a cohesive cluster?
- What about the attachment or link within the email—is that a commodity maldoc? Is it part of access broker infrastructure, or does it belong to the adversary operating the later-stage payload?
- Is the download cradle and loader the beginning of the next-stage payload, or the last vestige of the delivery affiliate before handing off execution to the delivered payload?

By honing in on the handoff between one affiliate and the next, you gain better insight into the potential pivot points in the progression of an incident, hopefully detecting adversaries closer to the start of an intrusion. Distinguishing phishing affiliates such as TA551 or TR from the IcedID or Qbot payloads they deliver not only helps delineate the handoff between the affiliates, but allows you to dive deeper into delivery patterns to identify differences when the deployed payload changes. Anticipating the next stage of a threat’s progression based on early observables enables defenders and incident responders to implement mitigations before that initial access can progress to lateral movement, data exfiltration, or ransomware.

## Crypters-as-a-service
In 