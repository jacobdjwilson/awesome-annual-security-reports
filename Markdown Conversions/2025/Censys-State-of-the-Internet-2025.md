# 2025 State of the Internet Report

## Table of Contents
- [Introduction](#introduction)
- [Malware Detection Trends](#malware-detection-trends)
- [C2 Time to Live](#c2-time-to-live)
- [Open Directories Time to Live](#open-directories-time-to-live)
- [Residential Proxy Infrastructure](#residential-proxy-infrastructure)
- [Conclusions](#conclusions)

---

## Introduction

Adversary infrastructure is the hidden scaffolding of modern cybercrime and espionage. From command-and-control (C2) services and malware loaders to proxy networks that route through trusted IP space, this infrastructure lets attackers scale campaigns, mask origins, and persist long after initial exploitation. For defenders, understanding this layer is critical: it’s often the best place to detect and disrupt attacks before they reach intended targets.

This report centers on adversary infrastructure—C2 and the surrounding tools threat actors use to establish control, move laterally, and exfiltrate data—and examines how that ecosystem behaves through real data. We examine the structural patterns of adversary infrastructure at Internet scale—where it resides, how long it persists, and how different signals reveal continuity even as individual services change. This view spans both traditional C2 ecosystems and emerging edge-based infrastructure like residential proxies and IoT botnets, highlighting the ways attackers build, sustain, and evolve the scaffolding behind modern threat operations.

### Data Accuracy and Historical Context

Censys enables organizations to see the Internet as it truly is and to secure it more effectively. Governments, enterprises, and insurers rely on Censys for attack surface management, supply-chain risk assessments, cyber-insurance underwriting, and monitoring of critical infrastructure.

Tracking adversary infrastructure requires breadth, freshness, and accuracy of Internet data to deliver insights that are both actionable and trustworthy. Censys provides the most complete map of global Internet infrastructure, tracking ~794 million IPv4 services[^1]—almost triple the 275 million observed a decade ago when we first started scanning the Internet.

While Censys emphasizes accuracy above all else, Censys also excels in speed. In controlled experiments, it discovered new services in a median of just 5.7 hours (12.3 hours on average), faster than all other platforms. This rapid detection empowers researchers to identify and monitor fast flux infrastructure designed to evade detection.

![Table comparing Censys, Shodan, Fofa, ZoomEye, and Netlas across metrics like estimated unique services and accuracy percentages.]

Over 92% of the services listed in Censys reflect live services, not stale or duplicate results, ensuring the best insights to track malicious infrastructure. Censys also provides historical context of every identified IP, Port, and services, providing insights to how infrastructure has changed over time.

![Table comparing service identification percentages across top 10, top 100, and all 65k ports for various platforms.]

With unmatched coverage, Censys identifies 96% of services on the top ten ports and 92% across the top hundred, while still capturing 82% of services across the entire 65k port space allowing security teams and researchers to track malicious services, open directories, and other adversary infrastructure running on non-standard or high ports that are often poorly unmonitored.

Censys is more than a dataset; it is a platform widely adopted across research and industry. Over 500 academic papers have used its data to study Internet security, public key infrastructure, IoT devices, industrial control systems, and more. Most relevantly, Censys has also been used to study malware infrastructure, the subject of this year’s State of the Internet Report.

---

## Malware Detection Trends

Let’s begin with a broad look at the malicious infrastructure landscape. We examined 80 of our malware detections over a period of 6 months, from December 2024 to May 2025.

During this study time frame, we observed an average of 2,906 malware detections for each snapshot date. Mid-December marked the greatest number we observed online during the period. Following the peak in December, we observed a 14% drop in detections in early January. This appears to be primarily driven by a drop in Cobalt Strike instances in China. Cobalt Strike was the most commonly observed malware family, and they are largely concentrated in China.

![Figure 1: Line graph showing total malware detections over time from December 2024 through May 2025.]

### Malware Families

Cobalt Strike originated as a pentesting and red teaming tool; however, it has been widely adopted by threat actors since its initial release over 10 years ago. In addition to C2 functionality, it offers extensible post-exploitation tooling attractive to security professionals and threat actors alike.

Despite the decline into January and takedown efforts spanning two years[^2], Cobalt Strike consistently had the greatest observed Internet presence of the detections we examined during the study period—it represents 34% of the C2s we observed as of May 2025.

The next largest families during this time frame were Viper (15% of total) and Sliver (13% of total). While Cobalt Strike is a commercial tool, Viper[^3] and Sliver[^4] are open source alternatives for adversary emulation. Viper and Sliver are slightly younger projects than Cobalt Strike, but their availability has likely contributed to their popularity.

> **Operation Morpheus & Other Notable Incidents**
> Read the story of a global disruption campaign against pirated versions of Cobalt Strike and other notable CVE investigations in our blog.
> [Read the Blog](URL)

![Figure 2: Stacked area chart showing top 10 malware detections over time.]

### Geography Trends

As of May, we observed detections in a total of 62 countries globally, with China and the U.S. topping the list and hosting 55% of malware collectively. Beyond the U.S. and China, we observe concentrations of malware in Asia, Europe, and North America.

It can be tempting to look for deeper meaning in geographic regions with high concentrations of malicious infrastructure, but rather than having geopolitical significance, concentrations of malware are more likely driven by hosting provider availability, pricing, and permissiveness.

![Figure 3: Bar chart showing global malware detection concentrations by country.]

### Network Trends

China-based providers Alibaba and Tencent top the list of where we observe the greatest volume of malware detections across the snapshot dates studied, and Huawei’s Cloud Service also makes the top 10. Rounding out the list are several U.S.-based providers, including Cologix, Digital Ocean, Colocrossing, Vultr, Amazon, and Microsoft.

![Figure 4: Line graph showing top 10 ASNs hosting malware over time.]

### Spotlight: PlugX

We can also find interesting exposure patterns when we look beyond the most common families shown above. Consider PlugX as an example.

PlugX[^5] is a remote access trojan (RAT) known since 2008[^6] and used by China-linked threat actors such as APT41 and Mustang Panda.

We generally observed a decline in PlugX instances over the study timeframe, apart from a slight and short-lived uptick in early April 2025. This decline follows news of a takedown[^7] from the U.S. Department of Justice in January 2025.

![Figure 5: Bar chart showing PlugX instances over time.]
![Figure 6: Bar chart showing all observed ASNs hosting PlugX over time.]

In examining all autonomous systems (AS) where we observe PlugX, we note minimal overlap with the global top autonomous systems where we observe C2 infrastructure. The only shared ASes are Vultr and Alibaba, which could point to more specific or discerning operations by PlugX operators.

XNNET, a U.S.-based provider, tops the list of networks where we observe PlugX, followed by Hong Kong-based Cloudie and CAT Telecom, based in Thailand.

> **Malware Case Files**
> Get the deep dive on some of our research team’s long-running malware investigations.
> [Read the Blog](URL)

---

## C2 Time to Live

A previously unexplored concept of threat infrastructure is their time to live, or TTL. Understanding how quickly threat infrastructure remains online, disappears, or moves is incredibly useful for defenders and researchers. Given the unique perspective of Censys, which is continuously scanning entities on the Internet, we are able with high confidence to examine TTLs, or the lifespans, of services and understand the repercussions of varying TTLs for defenders and researchers.

In this section, we will examine a C2 server’s TTL using two perspectives, network liveliness and content liveliness.

### Lifespans by Network Availability

TTL can traditionally be viewed from the network sense: how long is a specific service online before it disappears? We focus our analysis on the most common malware families we observed, Cobalt Strike and Viper.

![Figure 7: Bar chart comparing Cobalt Strike and Viper TTLs in days.]

This overarching view of the two C2 families exemplifies the huge variability in even these basic metrics. We next dive deeper and examine the most popular ports for Cobalt Strike and Viper services.

![Figure 8: Pie chart of top 5 Cobalt Strike ports and bar chart of their mean TTL.]
![Figure 9: Pie chart of top 5 Viper ports and bar chart of their mean TTL.]

### Lifespans by Content

Thus far we have examined TTLs in the context of network availability: when was the service online, and when did it go down? However, there is more to a service than just its network availability, as a service often has rich forms of content associated with it. We examine Cobalt Strike servers through observed watermarks for 32-bit copies of Beacon, and analyze their lifespans through a content-level perspective.

![Figure 10: Line graph showing service-level appearance for IPs with watermark 1359593325.]

Figure 10 shows the difference that comes with examining hosts at the watermark, or content, level. If you look at specific IPs, you can see that while the service may disappear, the watermark actually remains the same.

![Figure 11: Heatmap showing IPs that change a watermark at least once.]

To add to this nuance, we also check how many IPs have more than one watermark. We find 14 IPs (an incredibly small population) that have more than one watermark, and show how the service switches its watermark.

---

## Open Directories Time to Live

Open web directories are a cheap, simple, and stealthy way for attackers to host malicious payloads AND they’re hard to detect. OpenDirs are used by malware families such as AsyncRAT, SuperShell, Emotet, Mirai and many others.

We examine the lifespans of open web directories based on their HTTP bodies. We narrowed down our scope to look at only open web directories that are located on an HTTP service for the month of April. To compare the HTTP body of the open directory, we calculate the hash of the HTTP body using TLSH, a rolling hash algorithm.

![Figure 12: Comparison of observable lifespan and similar content lifespan.]

### Analysis

In Figure 12, we show the percentiles of network lifespans, or pure observability, vs lifespans based on content similarity:

- 50% vanish in <1 day
- 50% change contents within ~3 days

We find that open web directories have shorter network lifespans, meaning that almost half of open directories generally come online only to disappear a short while later. However, when we examine open directories through a content lens, we find their median lifespan is closer to 3 days.

---

## Residential Proxy Infrastructure

Beneath the hum of everyday Internet traffic, millions of home and small business devices quietly pull double duty, functioning for their legitimate owners while also relaying traffic for entirely separate purposes. These devices form the backbone of residential proxy networks, which route traffic through ordinary consumer equipment.

In this section, we explore Operational Relay Boxes (ORBs), a particularly stealthy type of malicious proxy, and examine one suspected ORB network, PolarEdge, to illustrate how they function.

### Spotlight: Pivoting on a PolarEdge Botnet C2

In February 2025, researchers uncovered PolarEdge, an IoT botnet that has been active since at least late 2023. It started out by exploiting CVE-2023-20118[^9], a command injection vulnerability in the web interfaces of Cisco Small Business routers, to implant base64-encoded webshells.

![Figure 13: Investigations of host 119.8.186[.]227.]

We can leverage historical scan data in Censys to go back in time to February 11[^10], around the time when Sekoia first observed attacker activity, and examine the attributes of this host to identify potentially adjacent infrastructure.

![Figure 14: learningrtc[.]cn mixed with a PolarSSL certificate.]

![Figure 15: The chance discovery of an open directory provides a rare view into possible botnet operation tooling.]

### The RPX Server

The x86-64 ELF binary (SHA256 Hash: 827797a9bff728ae6f46abd505e67a15e40b0ba69a8dc92a36fd90d9974c9593) appeared capable of coordinating (potentially compromised) nodes as proxy relays. The discovery of this component (dubbed “RPX” due to several debug statements referencing the source code path “/rpx”) offered the first glimpse into a potentially dedicated backend tool for managing large-scale proxy infrastructure.

> **Further Reading: the RPX Server**
> Full investigation details of the RPX proxy management binary, its function, purpose and the open directory that it was discovered on are available on the Censys blog.
> [Read the Blog](URL)

---

## Conclusions

This report examined adversary infrastructure from multiple angles: Internet-scale trends across malware families, geographies, and networks; the lifespans of C2 services measured both by network availability and content signals; the rise of perimeter-blurring infrastructure such as residential proxies and ORB-like botnets; and how these structural patterns play out in real incidents and disruption efforts. Across these lenses, a consistent lesson emerges: access to the most accurate, up-to-date data on Internet infrastructure is key to understanding and tracking threat actor operations and behavior.

---

[^1]: https://dl.acm.org/doi/10.1145/3718958.3754344
[^2]: https://therecord.media/malicious-cobalt-strike-use-down
[^3]: https://github.com/FunnyWolf/Viper
[^4]: https://github.com/BishopFox/sliver
[^5]: https://malpedia.caad.fkie.fraunhofer.de/details/win.plugx
[^6]: https://www.exabeam.com/blog/infosec-trends/take-a-deep-dive-into-plugx-malware/
[^7]: https://www.justice.gov/archives/opa/pr/justice-department-and-fbi-conduct-international-operation-delete-malware-used-china-backed
[^8]: https://blog.sekoia.io/polaredge-unveiling-an-uncovered-iot-botnet/
[^9]: https://nvd.nist.gov/vuln/detail/cve-2023-20118
[^10]: https://platform.censys.io/hosts/119.8.186.227?at_time=2025-02-11T09%3A25%3A58Z
[^11]: https://platform.censys.io/search?q=%28host.services.tls.fingerprint_sha256+%3D+%22e234e102cd8de90e258906d253157aeb7699a3c6df0c4e79e05d01801999dcb5%22%29
[^12]: https://platform.censys.io/hosts/8.219.153.173?at_time=2025-08-29T19%3A23%3A48Z
[^13]: https://web.archive.org/web/20250904121146/https://en.clash.wiki/
[^14]: https://www.virustotal.com/gui/file/827797a9bff728ae6f46abd505e67a15e40b0ba69a8dc92a36fd90d9974c9593
[^15]: https://platform.censys.io/search?q=host.services.tls.fingerprint_sha256+%3D+%22e234e102cd8de90e258906d253157aeb7699a3c6df0c4e79e05d01801999dcb5%22