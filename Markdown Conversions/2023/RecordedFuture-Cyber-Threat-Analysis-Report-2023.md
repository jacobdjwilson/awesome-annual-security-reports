# Cyber-Threat-Analysis-Report: 2023 Annual Report

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [2023 The Year of the Enterprise Software Hack](#2023-the-year-of-the-enterprise-software-hack)
- [Key Findings](#key-findings)
- [Section I: Setting the Stage: Technology, Geopolitics, Economics, and Policy](#section-i-setting-the-stage-technology-geopolitics-economics-and-policy)
- [Section II: Cyber Threat Intelligence](#section-ii-cyber-threat-intelligence)
- [Section III: Reflections on 2022 Predictions](#section-iii-reflections-on-2022-predictions)
- [Section IV: Outlook](#section-iv-outlook)
- [Appendix A: Top Exploited Vulnerabilities in 2023](#appendix-a-top-exploited-vulnerabilities-in-2023)

---

## Foreword

When creating this annual report, we had two goals: to give you insight into the adversary’s playbook and to assess future scenarios so that your organization can reasonably prepare for them. In 2023, attack surfaces expanded, software supply-chain vulnerabilities were widely exploited, and the expanded use of generative AI increased the velocity of malicious content at scale.

Get insights from the adversary’s playbook of tactics, techniques, and procedures (TTPs). The report presents the industry’s most comprehensive analysis of intelligence from 2023. It covers threat actors and their playbook of targets, methods, and attacks to help you eliminate blind spots in your current security posture. You’ll discover how:

- **Threat actors exploited enterprise software at scale**, as observed in CL0P ransomware group’s attack on third-party managed file transfer (MFT) services such as Fortra’s GoAnywhere and Progress Software’s MOVEit.
- **Offensive tooling is increasingly targeting Linux and macOS systems**: Ransomware kits continue to expand beyond Windows environments, facilitating an expanded range of victims.
- **Nation-states such as China-linked Spamouflage Dragon** (tracked by Insikt Group as Empire Dragon) are already using AI-generated images to improve information operations (IO).

Prepare for upcoming threats with a roadmap for 2024 and beyond. The report also offers our predictions regarding key vulnerabilities, third-party threats, extortion groups, and more for the year ahead. Wherever you are in your threat intelligence journey, you can use this report as a roadmap. It will help you strengthen your operations, create a forward-looking strategy, and protect your organization’s data, intellectual property, and brand reputation.

**Levi Gundert**
Chief Security Officer

---

## Executive Summary

2023 was a year of unrealized expectations. A rumored global recession failed to materialize. The Ukrainian counteroffensive did not decisively shift the tide of its war against an invading Russia. Any movement toward Israel-Saudi rapprochement was significantly set back following the October 7 Hamas terrorist attack in Israel and the launch of a new war in Gaza. Despite the initial hype around ChatGPT, disruptive applications of generative AI are likely still years off.

Nonetheless, Insikt Group continued to track cyber threat actors capitalizing on this chaos and uncertainty to steal data, conduct espionage, and disrupt their geopolitical rivals. Occasionally, these objectives converged. Chinese state-associated threat actors increasingly targeted Taiwanese semiconductor companies to gain both an economic and political advantage in that industry. At the same time, profit-minded actors took advantage of the surge in hacktivism to sell tools (such as DDoS-as-a-service) or monetize “hack-and-leak” operations.

## 2023 The Year of the Enterprise Software Hack

While “zero trust” may be a buzzword in enterprise security, the reality is that the internet relies on trust now more than ever. The work-from-home era accelerated the adoption of “as-a-service” enterprise software, shared cloud infrastructure, and virtualized workspaces. As a result, even the most security-focused companies rely on a vast array of third-party services and tools to get work done.

Cybercriminals are taking advantage of this increasingly interconnected environment to amplify their attacks. The number of weaponized vulnerabilities in enterprise software increased fourfold from the previous year. Some of the year’s most high-profile attacks targeting enterprise services, such as the MOVEit File Transfer Application exploit in May 2023, garnered attention due to the high volume of second- and third-party entities whose data was exposed. The ransomware gang behind MOVEit, CL0P, is estimated to have earned between $75 to $100 million in profit on that hack alone, suggesting these types of attacks will continue well into 2024.

Exploitation of enterprise software wasn’t the only way threat actors took advantage of trusted technologies and services. Abuse of legitimate internet services — such as messaging platforms and cloud services — was detected in almost 25% of malware families in one Recorded Future study, allowing threat actors to hide their command-and-control (C2) communications by blending in with ordinary traffic. Threat actors also increasingly incorporated exploits for Linux and macOS operating systems into their attack sequences, breaching the “walled garden” and allowing ransomware to be deployed on a wider variety of systems. Finally, threat actors compromised business process organizations (BPOs) to facilitate SIM swapping and other social engineering scams.

---

## Key Findings

- **Expanding attack surfaces increased the opportunity for mass exploitation of vulnerabilities**: Throughout 2023, threat actors increasingly favored vulnerabilities that would allow the exploitation of multiple victim enterprises through a single vulnerability in a third-party product.
- **Early malicious use of generative AI focused on social engineering and influence operations**: Initial use cases for malicious use of generative AI have facilitated the creation of large amounts of convincing, fraudulent content.
- **Software supply-chain attacks remain prevalent**: The increasingly interdependent nature of software has allowed threat actors to exploit third- and fourth-party dependencies in new ways.
- **Criminals targeted business process organizations to facilitate social engineering**: Social engineering scams run through business process outsourcing (BPO) made it easier for criminals to commit fraud.
- **Trusted tools are being abused through legitimate internet services**: Threat actors increasingly exploited trusted tools and services to gain access to an organization’s infrastructure and remain undetected.
- **Regulation abuse failed to take hold**: Ransomware and extortion campaigns experimented with new ways to coerce their victims into paying, including reporting their breach to regulators.
- **Offensive tooling is increasingly targeting Linux and macOS systems**: Ransomware kits continue to expand beyond Windows environments.
- **The war in Gaza increased hacktivist activity, capitalizing on chaos**: Hacktivists are increasingly taking advantage of growing “grassroots” interest in their cause by selling exploits, DDoS-for-hire, and other services.
- **Valid accounts are increasingly being used for initial access, while phishing tactics evolve**: Threat actors have adapted by adopting new phishing techniques and other initial access vectors, including valid accounts.
- **There is a convergence of influence narratives between ideological groups**: 2023 was characterized by an increasing convergence in narratives used in Chinese covert influence operations with narratives originating from the Russian disinformation ecosystem.

---

## Section I: Setting the Stage: Technology, Geopolitics, Economics, and Policy

### Major Technology Trends
It is nearly impossible to talk about trends in 2023 technology developments without acknowledging the ubiquitous discussions around generative artificial intelligence (AI). In 2023, increased demand for services like cloud computing and generative AI drove vendors to seek increased computing power. Another trend in technology products was increased offerings of passwordless authentication, such as through magic link logins.

### Geopolitical Events: Global Conflicts Reshape Strategic Partnerships
In its second year, Russia’s full-scale invasion of Ukraine entered a phase in which both sides wrestled to maintain their territorial gains. Exacerbating Ukraine’s struggle is the threat of another geopolitical conflict: the Israel-Hamas War, which began on October 7, 2023. United through anti-Western bloc sentiment, China’s strategic partnerships with both Russia and Iran played out in political, economic, and military areas throughout the year.

### Macroeconomic Trends
Entering 2023, the macroeconomy faced headwinds marked by an ongoing global health crisis, growth slowdowns, geopolitical uncertainty, and shifting trade alliances. A wave of mass layoffs hit the technology sector the hardest, with 260,000 jobs lost in 2023.

### Cyber Policy’s Uphill Battle
2023 was a major year of law enforcement takedowns against cybercriminal operations. Additionally, sector-specific cybersecurity regulations emerged, particularly in the US. One of the most anticipated developments was the finalization of the Securities and Exchange Commission’s (SEC) regulations for covered entities to report incidents of “materiality” within four business days.

---

## Section II: Cyber Threat Intelligence

### Evolution of Exploited Vulnerabilities
In 2023, threat groups successfully exploited several vulnerabilities at scale in singular third-party tools (GoAnywhere, MOVEit, and Citrix NetScaler devices) to inflict widespread damage.

### Evolution of Cyber Threats
Currently, the most tangible risks associated with generative AI are linked to influence operations, social engineering, data privacy breaches, and intellectual property violations.

### Third-Party Threats
Software supply-chain attacks remain prevalent. In 2023, Insikt Group identified an 11.8% increase in reported software supply-chain attacks.

### Extortion Trends
New cyberattack disclosure rules from regulators in the US and Europe in 2023 were feared to cause a widespread shift in tactics from extortion groups, but so far, such a shift has not materialized.

### Offensive Tooling Increasingly Targets Linux and macOS Systems
Reporting shows that cyberattacks and malware targeting Linux and macOS systems increased from 2022 to 2023.

### Gaza War Increases Hacktivist Activity: Capitalizing on Chaos
The latter half of 2023 saw an unprecedented rate of emergence of new hacktivist groups and alliances taking advantage of the chaos following the October 7 attack against Israel by Hamas.

### Valid Accounts Increasingly Used for Initial Access, While Phishing Tactics Evolve
Among the initial access methods Insikt Group observed in 2023, phishing, external remote services, and the use of valid accounts stood out for their high volume of reported attacks.

### Converging Influence Narratives Between Ideological Groups
2023 was the year of new records in covert influence operations. Both Russian and Chinese covert influence networks have illustrated a strong intent in manipulating audiences in connection with their respective governments’ geopolitical objectives.

---

## Section III: Reflections on 2022 Predictions

Assessing the accuracy of past predictions is a crucial part of the intelligence lifecycle. Insikt Group reflects on three major predictions from the 2022 Annual Report, which have globally stood true, although with several nuanced developments.

---

## Section IV: Outlook

### Cyber Threat Landscape
- **Vulnerabilities**: We predict that at least one ransomware group will carry out a successful compromise of hundreds of targets via exploiting vulnerabilities in an enterprise third-party file transfer service in 2024.
- **Third-party threats**: We expect to see software supply-chain attacks dominate the third-party threats landscape by number and severity of attacks.
- **Extortion groups**: We expect that extortion groups will increasingly target technologies supporting and securing hybrid and remote work.
- **Hacktivism**: We anticipate that shifts in the tides of the Russia-Ukraine war are likely to result in the strategic diversion of hacktivist activity toward the war in Gaza.
- **Initial access methods**: We expect that attackers are likely to increasingly focus on stealing credentials and identities using techniques like password spraying and credential stuffing.
- **Information operations**: We anticipate the public’s awareness of deepfakes and disinformation operations will be more disruptive than the aims or activity of adversary-driven campaigns.

### Contextual Landscape
- **Technology**: Companies are almost certain to increasingly offer passwordless logins to users in 2024.
- **Geopolitics**: Should China’s domestic economic performance worsen, it will likely use social surveillance and censorship to quell unrest. Iran will continue to rely on a mixture of proxy warfare and cyber influence operations.

---

## Appendix A: Top Exploited Vulnerabilities in 2023

![Figure 1: Metrics associated with key themes in the 2023 cyber threat landscape]
![Figure 2: The trilateral relationship between Russia, China, and Iran is based on converging goals]
![Figure 3: High-risk vulnerabilities actively exploited in 2022 and 2023 per the Recorded Future® Intelligence Cloud]
![Figure 4: References to macOS, Linux, or Unix-like OSs in TTP Instance notes over the last three years]
![Figure 5: Mentions of DDoS-as-a-service between 2022 and 2023 and the number of hacktivist groups active within the first eighteen days of the Ukraine/Gaza wars]
![Figure 6: Top five TTPs used to gain initial access in validated cyberattacks]
![Figure 7: Stolen credentials observed in Recorded Future malware logs]
![Figure 8: Generative AI uploaded by Empire Dragon accounts during the Hong Kong local elections]
![Figure 9: Reflections on three major predictions from our 2022 Annual Report]

---

resence in the region. Russia will very likelyexploit
perceived “war fatigue” among Western nations to influence public opinion ahead of elections in
the US and EU and will wait for election results to determine its next course of action in relation
to its war in Ukraine and its relationship with the West.
● Regulations:The increase in vulnerability exploits will drive lawmakers to shift from regulating
software safety to reforming software liability law. This would make it easier for consumers to
take legal action against software companies that produce insecure code; however,determining
what counts as coding negligence will be a significant challenge for policymakers. In response to
ongoing policies and regulations for AI, AI companies will likely shift toward synthetic data for
training their models to avoid privacy and copyright issues, speed up development, and reduce
the chances of data poisoning from threat actors.
25 TA 2024 0321 RecordedFuture®|www.recordedfuture.com

THREATANALYSIS
| Appendix      | A  Top          | Exploited | Vulnerabilities | in 2023 |      |      |
| ------------- | --------------- | --------- | --------------- | ------- | ---- | ---- |
| Vulnerability | AffectedProduct |           | Description     |         | Risk | CVSS |
Score
CVE-2023-44487 Anyproductthat TheHTTP/2protocolallowsa 89 7.5
|     | usestheHTTP/2 |     | denial-of-service(serverresource |     |     |     |
| --- | ------------- | --- | -------------------------------- | --- | --- | --- |
|     | protocol      |     | consumption)becauserequest       |     |     |     |
cancellationcanresetmanystreams
quickly.Fixesarevendor-specific.
CVE-2023-34362 ProgressSoftware ASQLinjectionvulnerabilityhasbeen 89 9.8
|     | MOVEitTransfer |     | foundintheMOVEitTransferweb |     |     |     |
| --- | -------------- | --- | --------------------------- | --- | --- | --- |
applicationthatcouldallowan
unauthenticatedattackertogainaccess
toMOVEitTransfer'sdatabase.
CVE-2023-23397 MicrosoftOutlook Elevationofprivilegevulnerability 89 9.8
CVE-2023-4966 CitrixNetScalerADC Asensitiveinformationdisclosure 89 9.8
|     | andNetScaler |     | vulnerabilitythatallowsanattackerto |     |     |     |
| --- | ------------ | --- | ----------------------------------- | --- | --- | --- |
|     | Gateway      |     | readlargeamountsofmemoryafterthe    |     |     |     |
endofabuffer
CVE-2023-21716 MicrosoftOffice MicrosoftWordremotecodeexecution 99 9.8
|     |  Word) |     | vulnerability |     |     |     |
| --- | ------ | --- | ------------- | --- | --- | --- |
CVE-2023-24932
|     | MicrosoftWindows |     | SecureBootsecurityfeaturebypass |     | 99  | 6.7 |
| --- | ---------------- | --- | ------------------------------- | --- | --- | --- |
|     | 10,11,Server     |     | vulnerability                   |     |     |     |
CVE-2023-28206 ApplemacOS,iPhone Anout-of-boundswriteissuewas 99 8.6
|     | OS,iPadOS |     | addressedwithimprovedinput |     |     |     |
| --- | --------- | --- | -------------------------- | --- | --- | --- |
validation.Anappmaybeableto
executearbitrarycodewithkernel
privileges.
| CVE-2023-2868 | BarracudaEmail  |     | Aremotecommandinjection          |     | 99  | 9.8 |
| ------------- | --------------- | --- | -------------------------------- | --- | --- | --- |
|               | SecurityGateway |     | vulnerabilitythatcanenableremote |     |     |     |
|               | Firmware        |     | codeexecution                    |     |     |     |
CVE-2023-38831 RARLABWinRAR RARLABWinRARbefore6.23allows 99 7.8
attackerstoexecutearbitrarycode
whenauserattemptstoviewabenign
filewithinaZIParchive.
CVE-2023-41990 ApplemacOS,iPhone Apple-onlyADJUSTTrueTypefont 99 7.8
|     | OS,iPadOS |     | vulnerabilitythatallowsremotecode |     |     |     |
| --- | --------- | --- | --------------------------------- | --- | --- | --- |
executionthroughamaliciousiMessage
attachment.ExploitedinOperation
Triangulation.
CVE-2023-43177 CrushFTP CrushFTPpriorto10.5.1isvulnerableto 99 9.8
ImproperlyControlledModificationof
|     |     |     | TA 2024 0321 | RecordedFuture®|www.recordedfuture.com |     |     |
| --- | --- | --- | ------------ | -------------------------------------- | --- | --- |
26

THREATANALYSIS
| Vulnerability | AffectedProduct | Description | Risk | CVSS |
| ------------- | --------------- | ----------- | ---- | ---- |
Score
Dynamically-DeterminedObject
Attributes.
CVE-2023-47565
|     | QNAPQVRFirmware | AnOScommandinjectionvulnerability | 99  | 8.8 |
| --- | --------------- | --------------------------------- | --- | --- |
|     | 4.0             | thatcanallowauthenticatedusersto  |     |     |
executecommandsviaanetwork
CVE-2023-4863 GoogleChrome, Heapbufferoverflowinlibwebpin 99 8.8
|     | MozillaFirefox | GoogleChromepriorto116.0.5845.187 |     |     |
| --- | -------------- | --------------------------------- | --- | --- |
andlibwebp1.3.2allowedaremote
attackertoperformanout-of-bounds
memorywriteviaacraftedHTMLpage.
CVE-2023-4911 GNUglibconx64 Bufferoverflowvulnerabilitythatcan 99 7.8
| (LooneyTunables) | Fedora | allowRCEwithelevatedprivileges |     |     |
| ---------------- | ------ | ------------------------------ | --- | --- |
RedHatEnterprise
Linux
CVE-2023-7024 GoogleChrome HeapbufferoverflowinWebRTCin 99 8.8
GoogleChromepriorto120.0.6099.129
allowedaremoteattackertopotentially
exploitheapcorruptionviaacrafted
HTMLpage.
Table1:Tophigh-riskvulnerabilitiesdisclosedin2023 Source:RecordedFuture)
|     |     | TA 2024 0321 RecordedFuture®|www.recordedfuture.com |     |     |
| --- | --- | --------------------------------------------------- | --- | --- |
27

THREATANALYSIS
AboutInsiktGroup®
RecordedFuture’sInsiktGroup,thecompany’sthreatresearchdivision,comprises
analystsandsecurityresearcherswithdeepgovernment,lawenforcement,military,and
intelligenceagencyexperience.Theirmissionistoproduceintelligencethatreducesrisk
forclients,enablestangibleoutcomes,andpreventsbusinessdisruption.
AboutRecordedFuture®
RecordedFutureistheworld’slargestthreatintelligencecompany.RecordedFuture’s
IntelligenceCloudprovidesend-to-endintelligenceacrossadversaries,infrastructure,
andtargets.Indexingtheinternetacrosstheopenweb,darkweb,andtechnical
sources,RecordedFutureprovidesreal-timevisibilityintoanexpandingattacksurface
andthreatlandscape,empoweringclientstoactwithspeedandconfidencetoreduce
riskandsecurelydrivebusinessforward.HeadquarteredinBostonwithofficesand
employeesaroundtheworld,RecordedFutureworkswithover1,700businessesand
governmentorganizationsacrossmorethan75countriestoprovidereal-time,unbiased,
andactionableintelligence.
Learnmoreatrecordedfuture.com
28 TA 2024 0321 RecordedFuture®|www.recordedfuture.com