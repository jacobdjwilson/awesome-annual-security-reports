# THREAT ACTOR STUDY: TRENDS, INSIGHTS AND LESSONS LEARNED OVER 2024

## Table of Contents
- [A Year In Summary](#a-year-in-summary)
- [1. Introduction](#1-introduction)
- [2. The Ever-Evolving Threat Landscape](#2-the-ever-evolving-threat-landscape)
- [3. Advanced Persistent Threats (APTs)](#3-advanced-persistent-threats-apts)
- [4. Financially-Motivated Threat Actors](#4-financially-motivated-threat-actors)
- [5. Malware and Threat Actor Infrastructure Trends](#5-malware-and-threat-actor-infrastructure-trends)
- [6. Silent Push Highlights & App Improvements](#6-silent-push-highlights--app-improvements)
- [7. Strategic Recommendations](#7-strategic-recommendations)
- [8. Predictions For 2025](#8-predictions-for-2025)
- [9. Pushing The Boundaries of Modern Threat Intelligence](#9-pushing-the-boundaries-of-modern-threat-intelligence)

---

## A Year In Summary
2024 marked a transformative year in cyber threat intelligence. Rapidly evolving adversary tactics, increasingly novel malware proliferation techniques, and the widespread availability of artificial intelligence (AI) enabled malicious infrastructure scaling methods have made the jobs of security teams exponentially more challenging worldwide.

Dealing with these threats thus requires a transformative approach. Reactive defense measures are no longer effective, and Indicators of Compromise (IOCs) are stale at best. The industry is turning toward Indicators of Future Attack (IOFAs) to gain actionable threat intelligence that can stop attacks before they are weaponized.

In pursuit of that goal, the preemptive cybersecurity intelligence company Silent Push spent 2024 tracking millions of hidden malicious domains and IP addresses, fingerprinting attacker infrastructure—both at scale and as it was built—mapping the impact of critical vulnerabilities spread across the web and working closely with partners to disrupt global threat actor operations.

We delivered world-first, in-depth technical reporting to our customers and produced IOFA feeds setting the gold standard for preemptive threat intelligence. We continue to perfect our rigorously curated, first-party dataset and intuitive threat-hunting platform. At Silent Push, when we say, “We Know First,” – we mean it.

---

## 1. Introduction
From C-suite leaders to hands-on keyboard analysts, Silent Push strives to ensure that the information we provide benefits all our readers. This “Year in Review” white paper contains a mix of technical information and analysis alongside high-level overviews and key trends regarding cyber attackers who have swiftly embraced the rise of AI to scale their operations and become more sophisticated by the minute.

We report the threat landscape as we see and experience it. Delving into some of the technical details behind Advanced Persistent Threats (APTs) pursuing nation-state objectives and major crimeware families focused purely on extracting financial gain, we objectively explore some of the latest emerging threats the security industry is facing. Examining the various malware and malicious infrastructure trends we have observed, we cover our own improvements and contributions in the fight against these threats and provide strategic recommendations for cyber-conscious organizations alongside our predictions for 2025.

The insights powering this paper are built on our proprietary dataset, which represents the most comprehensive view of the internet available anywhere in the world, to map attacker tactics, techniques, and procedures (TTPs) and infrastructure in real time. Our technology enables the tracking and analysis of adversaries’ network changes as they occur, stopping them at the gates – before they can get in.

_Note: Operational security requirements prevent us from revealing certain technical details in this and the rest of our public-facing publications. For in-depth analysis of the threats listed herein (as well as many others), access to our industry-defining data, IOFA feeds, and more, please contact our Sales team to see about becoming an enterprise customer._

---

## 2. The Ever-Evolving Threat Landscape

### Silent Push Key Statistics
We enable organizations to stay one step ahead of emerging threats:
- Hundreds of thousands of Indicators of Future Attack (IOFAs) provided on a constantly recurring basis to organizations worldwide alongside a similar number of indicators in our Bulk Data Feeds.
- Published dozens of blogs and technical reports detailing analysis and mitigation needed to stop activities of multiple APTs and major crimeware groups.
- Collaborated with worldwide partners in law enforcement and the security industry, leading to the disruption and/or takedown of numerous networks and the blocking of countless cyber attacks.
- Continuously expanded our data collection, processing, and fingerprinting capabilities.

### Top Threat Trends
The cybersecurity environment in 2024 experienced rapid escalation in both volume and complexity of cyber threats. Silent Push analysts noted considerable increases in activity driven by both state-sponsored APTs and financially-motivated cybercriminal groups, including a dramatic increase in the sophistication of phishing kits – with new iterations appearing faster than ever before to shift targeting across industry verticals (financial, retail, technology, and energy).

Another trend, one of the most significant in 2024, was the proliferation of AI-powered infrastructure scaling. Threat actors harnessed AI to enhance their spear-phishing campaigns, automate malware development, and obfuscate their infrastructure. The use of generative AI tools has made it easier for adversaries to scale operations and create convincing lures, complicating traditional detection and response efforts.

"Infrastructure Laundering" is a term we coined to describe the growing criminal practice our analysts observed of threat actors intentionally hiding their infrastructure behind large, mainstream providers hosting many otherwise legitimate subscribers. We see it as an increasingly pressing issue.

Our research into Triad Nexus, combined with insights driven by our unparalleled DNS data, has revealed troubling associations between cybercrime and real-world criminal gangs, most notably Chinese Triad groups.

Exemplified by actors like Raspberry Robin, that facilitated human-operated ransomware campaigns by providing compromised infrastructure to other threat groups, “Access-as-a-Service” models have continued to grow in prominence. These services streamlined the ability of less sophisticated actors to execute high-profile attacks, further diversifying the threat landscape. They also have worrisome ties to Russian threats that the industry should keep in mind when defending against them.

Threat actors increasingly exploited Cloudflare’s proxying services to obscure their infrastructure, effectively concealing the true IP addresses behind their malicious campaigns. This tactic allowed adversaries to add a layer of anonymity and resilience to their operations, complicating efforts to identify and disrupt their hosting environments. Silent Push’s research utilized advanced unmasking techniques to reveal the real IPs behind proxied domains, enabling organizations to uncover hidden infrastructures and preemptively defend against these sophisticated threats.

---

## 3. Advanced Persistent Threats (APTs)

### State-Sponsored APT Groups
The primary point of concern for governments, organizations, and critical infrastructure managers is state-sponsored APT groups that continue to pose a significant challenge to global cybersecurity. APTs remain a driving force behind the evolution and innovation of cyber threats. Their actions often pave the way for less sophisticated threats to imitate.

Collaboration across organizations, governments, and security providers is essential to mitigate APT groups’ impact. Silent Push’s focus on mapping adversary infrastructure before weaponization and sharing actionable intelligence underscores the critical need for preemptive threat intelligence in combating these persistent, sophisticated actors.

This section covers a few groups we tracked in 2024, namely APT 28 (Fancy Bear), APT 43 (Kimsuky), and Sapphire Sleet, that have operated with surgical precision throughout the year, targeting individuals and organizations involved in finance, technology, and government across multiple regions.

_Note: For the same operational security concerns mentioned before, which are only enhanced for high-profile threats backed with significant state resource pools, technical details and analysis of our reach into most APT groups are restricted to reports only available to our enterprise customers._

### APT28 (Fancy Bear)
APT28 is a long-running APT group linked to Russia’s military intelligence agency GRU. The group continues to be active, with public reporting discussing campaigns targeting countries in Europe and Central Asia using the HATVIBE HTML loader and CHERRYSPY custom python backdoor. Silent Push was able to pivot on and generate fingerprints from publicly-mentioned CHERRYSPY domains within our platform.

### Kimsuky (APT43)
Kimsuky is an APT group originating from North Korea that has been active for more than a decade. They are known for cyber espionage and targeting victims in countries including Japan, South Korea, and the U.S. Considerable effort and persistent analysis led Silent Push Threat Researchers to find hundreds of Kimsuky domains that aligned closely with those involved in previous attacks.

### Sapphire Sleet
Sapphire Sleet is a sub-group of the North Korean-affiliated and state-sponsored Lazarus group, active since the first quarter of 2020. Specializing in financial heists and cyber espionage, Sapphire Sleet primarily targets individuals and organizations operating in cryptocurrency exchanges, venture capital, blockchain, and other next-generation technology sectors.

![Screenshot warning of Sapphire Sleet fake Fenbushi Capital post on LinkedIn]
![Second screenshot alerting of the scam]

---

## 4. Financially-Motivated Threat Actors
For the majority of organizations, financially-motivated threat actors (also known as major crimeware groups) dominated the cyber threat landscape during 2024. Employing increasingly complex tactics against their targets, groups including FIN7, Scattered Spider, CryptoChameleon, and others exemplified the evolution of crimeware.

### FIN7
In 2024, Silent Push analysts received a valuable lead from one of our partners about FIN7 using shell websites to age domains. Since our initial FIN7 public report, we tracked over 5,000 domains and focused considerable efforts on finding new campaigns being launched through these websites.

![escueladeletrados.com as an Alliant phishing page on June 9, 2024]
![escueladeletrados.com as a shell domain on June 9, 2024]

### The Comm - Scattered Spider & CryptoChameleon
Scattered Spider and CryptoChameleon are both part of “The Comm” – a loosely organized group of threat actors, with many based in the West and the U.S. Throughout 2024, Silent Push analysts received private briefings and sensitive details from our research-sharing partners about The Comm.

### Scattered Spider
Since the second quarter of 2022, Scattered Spider has been an active, financially-motivated hacker collective known for launching hundreds of sophisticated social engineering attacks. In 2024, Silent Push analysts discovered over 350+ new high-confidence indicators attributed to this threat actor.

![Scattered Spider’s attack methodology]
![Phishing page 1]
![Phishing page 2]
![Phishing page 3]
![Phishing page 4]
![Phishing page 5]

### CryptoChameleon
CryptoChameleon is a phishing kit first discovered in February 2024. Our research discovered CryptoChameleon makes almost exclusive use of DNSPod nameservers.

![Kraken phishing page]
![Ledger phishing page]
![Apple phishing page]

---

## 5. Malware and Threat Actor Infrastructure Trends
Trends observed by our analysts in malware and across all malicious infrastructure we tracked throughout 2024 underscored the growing sophistication and adaptability of threat actors. Silent Push’s research revealed the increasing use of custom encryption algorithms, indirect API calls, and AI-enhanced evasion tactics in malware like the BlackMoon Trojan and Lumma Stealer.

Meanwhile, infrastructure trends highlighted the reliance on bulletproof registrar services, such as NiceNIC and BitLaunch, and the reuse of aged domains to obscure malicious operations. The rise of infrastructure laundering is particularly troubling. Attackers leverage reputable cloud providers like Microsoft and Amazon to add legitimacy to their campaigns while remaining seemingly unnoticed by their hosting providers and the security world.

---

proactively address these challenges. As malware continues to
evolve and threat actor infrastructure becomes more robust, the
cybersecurity industry must prioritize innovative detection methods
and global collaboration to stay ahead of these persistent threats.
Note: For more information on how your organization can leverage
Silent Push to defeat the rising number of cyber threats it faces,
please contact our Sales team.
silentpush.com 51

FIN7 MALWARE CAMPAIGNS MALWARE IDENTIFIED ON OPEN
DIRECTORIES
In late Summer 2024, Silent Push analysts discovered a
new FIN7 campaign that used a series of AI “deepfake nude
BLACKMOON TROJAN
generator” websites that were actually honeypots serving
The BlackMoon Trojan, first identified in 2014, is a banking
malware to unsuspecting visitors. The public details of that
malware known for targeting users in South Korea, using
report can be found here.
phishing tactics and malicious redirects to compromise
One interesting tactic observed in our analysis of the campaign credentials and facilitate unauthorized access to
was FIN7’s use of SEO tactics to spread their malware. All financial accounts.
FIN7 AI deepfake honeypots we found contained a footer link
Our team identified a new malware variant currently under
for “Best Porn Sites,” which redirected users to aipornsites[.]
development, showcasing advanced evasion techniques.
ai – a website that promotes the domain “ainude[.]ai” – that
Developed in MFC C++, the malware employs encrypted
is currently down – but appeared to be the same website
strings and indirect API calls to significantly complicate analysis.
template used on the FIN7 honeypots. Additional details,
analysis, and IOFAs found from this campaign and its malware
A standout feature is its custom Base64 encoding algorithm,
can be found in our enterprise-only TLP: Amber report and
specifically designed to bypass standard decoding methods.
FIN7 intelligence feeds.
Additionally, the presence of debug logs and several
unimplemented functions suggests this malware is still in its
early stages. These findings highlight the potential for further
sophistication as development continues.
LUMMA STEALER
Our team observed the emergence of a new tactic utilized by
the Lumma Stealer malware in 2024. This variation of the threat
builds its own HTTPS connections independently, circumventing
conventional Windows APIs and making detection and analysis
significantly more challenging. Our investigation also revealed
this variant leverages Steam-related elements in its
communications, further emphasizing its evolving sophistication.
CHROME APPBOUND ENCRYPTION
During 2024, our team observed some pushback against
malware stealers with protection enhancements in Chrome
for users, but later discoveries have since shown that newer
threats, like the Glove Infostealer, have managed to bypass
these safeguards.
silentpush.com 52

BULLETPROOF HOSTS THE RISE OF THE BULLET PROOF REGISTRAR
The practice of bulletproof hosting (BPH) is described as NiceNIC International is an ICANN-accredited registrar and
a service provided by an internet hosting operator that hosting provider founded in 2012 in Hong Kong by Zheng Wang.
is resistant to takedown efforts and is usually located in
The main website, nicenic.net, has the HTML title: “Register
jurisdictions with more lenient regulations and/or countries
Domain by Bitcoin | Buy Domain with Crypto Payment | Buy
where law enforcement has fewer resources to monitor and
Web Domain,” which emphasizes this service’s acceptance
control. Hosting service providers involved in BPH support
of digital currencies. Reviewing their documentation and
all types of unwanted activities, including but not limited to
knowledge base reveals *.my-ndns[.]com are this service’s
the abuse of copywritten materials, hosting of malware and
default name servers.
botnet command and control (C2) servers, hate speech and
misinformation support, illegal gambling, pornography,
During 2024, Silent Push identified an increasing number
and spam.
of threat actors resorting to NiceNIC for registering their
malicious infrastructure, including Scattered Spider, FIN7,
Our team put considerable effort into researching bulletproof
CryptoChameleon, and Hunters International.
hosts throughout 2024 by a wide array of threat actors, and
while covering the full extent of our research is unfortunately
The ratio of malicious domains registered on this service
beyond the scope of this paper, we have several releases
from the total of new registrations is out of proportion for
currently planned to fill this gap. We encourage readers to look
an innocuous service, as the vast majority has been serving
forward to our BPH-focused publications coming later
campaigns ranging from phishing, malware C2, crypto scams,
this year!
and underground markets, among others.
Silent Push analysts were also able to confirm in 2024 that
NiceNIC continues to have a process for requesting the
takedown of domains that is nearly impossible to accomplish –
they require having a “Power of Attorney” over a victim and a
letter to prove that relationship.
As you can see in the screenshot below, the third requirement
from NiceNIC to get infrastructure taken down is, “Please send
us your latest POA issued by the targeting website/brand.”
Screenshot of an email from the NiceNIC Dispute Team
silentpush.com 53

BITLAUNCH PROLIFIC PUMA
Throughout 2024, our team observed various threat actors Prolific Puma provides URL shortening services to
(Scattered Spider, Gamaredon, and Prolific Puma) acquiring cybercriminals, allowing threat actors to hide their
servers on Vultr and DigitalOcean through BitLaunch, a infrastructure during the initial distribution hop, having served
company that provides “anonymous cloud VPS hosting from almost every type of malicious campaign, from phishing and
DigitalOcean, Vultr, Linode and on their own hardware, payable spam to malware.
with Bitcoin and 10+ other cryptocurrencies.”
Similar to popular, legitimate URL shortening services,
the URLs generated by Prolific Puma follow the pattern:
http(s|)://<prolific_puma_controlled_domain>/<encoded_string>
If the correct path is provided, the string will be decoded, and
the victim redirected to the attacker-controlled malicious page.
Silent Push identified thousands of new domains created by
Prolific Puma operators in 2024, as this network consistently
had hundreds of redirects active simultaneously.
silentpush.com 54

SILENT PUSH
HIGHLIGHTS & APP
6
IMPROVEMENTS
CLOUDFLARE UNMASKING
Throughout 2024, Silent Push researchers noted a trend among
several malicious campaigns where threat actors used Cloudflare
services to proxy their infrastructure, thus hiding the real IP
addresses the campaigns were being served from.
Analyzing DNS records of the domains registered on NiceNIC during
a one-week period revealed about 1,000 of the domains used
Cloudflare to proxy their web pages within the first 48 hours of
creation. This accounted for about 68% of the total infrastructure
registered on that service during the timeframe.
The Silent Push app offers many Cloudflare unmasking techniques
using PADNS and Webscan datasets.
One threat actor that consistently uses this technique is
CryptoChameleon.
Advanced domain query showing part of the CryptoChameleon infrastructure
silentpush.com 55

NEW DATA SOURCES
Ad tech data | Telegram URLs | ICP License Numbers
In 2024, we continued our bulk scanning and resolving of content on the internet, capturing DNS
changes, certificates, and WHOIS data to empower organizations with over 100 metadata fields
available for search. We never delete data, and now have over three years of data available for
searching.
We’ve also been able to add several requested fields of data, which provides unique opportunities
for pivots.
In April 2024, we started scanning for ads.txt, app-ads.txt, and sellers.json data, which are public
files hosted on domains that contain “authorized advertising partners” and use a specific schema
introduced by the IAB[.]com. We captured this data across the internet and found a series of UK
government websites that were sending user data to a controversial Chinese ad tech vendor. Hours
after our piece had been published, the Chinese vendor was purged from the Government websites,
preventing them from collecting data on visitors of those sites and monetizing their visits.
Since starting this collection of advertising data, we now have SHA256 hashes available for search in
our Web Scanner for these fields:
adtech.ads_txt adtech.app-ads_txt_sha256
adtech.ads_txt_sha256 adtech.sellers_json
adtech.app_ads_txt adtech.sellers_json_sha256
About halfway through 2024, we started to collect a new, valuable field of data from our web
scanning: Telegram URLs. This feature makes it possible to search for exact Telegram URLs that
we’ve seen on various homepages, often included by specific threat actors and some
corporate organizations.
Combining this Telegram feature with our source of dark web data allows us to quickly parse the
approximately 6,000 results in our Web Scanner that embed specific Telegram URLs. This offers a
great source for finding potentially problematic Telegram channels.
Here’s a query to see these results:
silentpush.com 56

Datasource = “torscan” AND body_analysis.telegram = “*t.me*”
Across both the dark and clear webs, we currently have over 3.1 million results in our Web Scanner
that contain this body_analysis.telegram field – creating numerous opportunities for new pivots.
In the Spring of 2024, our team quietly started collecting Chinese Internet License Numbers known
as “ICP Licenses.” These are consistently structured IDs embedded into the footer of some Chinese
websites that are needed to apply for a license to send data through the Great Firewall. An example
of one of these ICP License IDs can be seen in our recent research into the AIZ Retail and Crypto
phishing network:
ssrchat[.]com ICP license
silentpush.com 57

Since starting our ICP scanning earlier this year, we now have over 15 million records available in
Web Scanner with this field.
Web Scanner query for body_analysis.ICP_license = “*”
Moving into 2025, we look forward to adding new fields to our collections and appreciate any
suggestions – please share them with info@silentpush.com or through your Silent Push representative.
silentpush.com 58

STRATEGIC
RECOMMENDATIONS
7
As the prevalence and complexity of 2024’s cyber threats
showed, preemptive threat intelligence is the evolution necessary
for proactive defense over prior, stale methodologies. Mapping
malicious infrastructure from a global rather than a limited field
of view is the optimum way to combat the scaling capacity and
effectiveness of AI-enabled cyber threats.
Silent Push’s approach, which involves providing organizations with
IOFAs to enable detection of threats before they are weaponized,
is the most effective means of securing an organization’s threat
surface. By consuming our actionable intelligence reports and
utilizing our first-party data, organizations can empower their
security teams to appropriately challenge and defend against
cyber threats.
silentpush.com 59

UTILIZING SILENT PUSH OFFERINGS
• IOFAs for Proactive Defense: Silent Push IOFA feeds enable organizations to detect adversary
infrastructure early, providing a critical advantage in the prevention of attacks when every
second matters.
• Enriched DNS Data: Silent Push’s world-renowned platform enables threat hunters to pivot
through unparalleled datasets with surgical precision, uncovering hidden connections and creating
expansive fingerprints to continuously track malicious infrastructure even as more is spun up.
• Threat Intelligence Reports: Silent Push provides in-depth TLP: Amber reports, detailing threat
actors’ activities in step-by-step analytical breakdowns complete with examples and immediately
useable (and actor-transferrable) pivots in-platform.
ACTIONABLE STEPS FOR ORGANIZATIONS
1. Integrate IOFAs: Incorporate Silent Push feeds into existing monitoring tools to mitigate threats
before they can strike.
2. Leverage DNS Data: Access our enriched DNS datasets and “Total View” breakdowns of domains
and IP addresses to proactively hunt for threats and discover new attack patterns.
3. Digest Gold Standard Intelligence Reports: Consume Silent Push’s reports as an upskill
opportunity for your organization’s defenders as well as critical awareness of threat actor trends
and capabilities.
By adopting a pivotal shift in focus, security teams can move from providing reactive threat
intelligence to preemptive threat intelligence. As seen in this report, that insight has allowed Silent
Push to “open the aperture” and shine our light on previously unknown, unseen, and unmitigated
attacker infrastructure. Adopting our methods will enable organizations to better position themselves
to proactively mitigate cyber threats – stopping adversaries not just at the gates but before their
attacks are ever launched.
silentpush.com 60

PREDICTIONS
FOR 2025
8
As threat actors continue to evolve, 2025 is poised to bring both
new challenges and novel strains for organizations striving to
secure their environments. The wide-ranging growth in malicious
activity observed in 2024 highlights the urgent, industry-wide need
for preemptive threat intelligence.
Silent Push expects to see threat actors leveraging AI even
more aggressively in the coming years, using it to deploy ever-
more-scalable malicious infrastructure, automate their phishing
campaigns, and obfuscate malware packages in many ways.
This trend is likely to exacerbate the complexity of cyber attacks,
forcing organizations to change their security approaches and
adopt the use of more sophisticated tools to stay ahead.
The growing reliance on advanced infrastructure management
tactics, such as bulletproof hosting, Fast Flux DNS, and proxying
malicious infrastructure via Cloudflare after aging it, is likely to
become more prevalent in 2025. Threat actors’ ability to adapt
quickly to takedowns and pivot into alternate infrastructure will
demand continuous monitoring and the application of purpose-
driven detection methods. Collaboration between cybersecurity
providers, enterprise organizations, and law enforcement the
world over will be more essential to disrupting and mitigating
adversaries’ operations.
silentpush.com 61

PUSHING THE
BOUNDARIES OF
9
MODERN THREAT
INTELLIGENCE
Silent Push’s preemptive approach to threat intelligence and
continuously expanding observation of global internet architecture,
backed by game-changing first-party data, are critical in helping
organizations navigate and mitigate the advanced threats facing
them now and in the future. As our industry shifts to combat
increasingly resourced and sophisticated cyber threats, the ability
to preemptively ruin adversaries’ plans by mitigating attacks
before they are launched will define the success of cybersecurity
strategies in 2025 and beyond.
silentpush.com 62

PREEMPTIVE CYBER INTELLIGENCE WITH
INDICATORS OF FUTURE ATTACK
Silent Push provides preemptive cyber intelligence exposing threat actor infrastructure as it’s being set up.
Our Indicators of Future Attack (IOFA) act as an early warning system to defend against threats. We go beyond
stale IOCs and create a unique digital fingerprint of adversary behavior enabling you to proactively block
hidden attacks before they’re launched.
Get started today.
© 2025 Silent Push. All rights reserved. 031225 silentpush.com