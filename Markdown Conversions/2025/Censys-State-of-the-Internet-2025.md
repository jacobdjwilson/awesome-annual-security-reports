# 2025 State of the Internet Report

Understanding Adversary Infrastructure Through Real Investigations and Data

## Table of Contents
- [Introduction](#introduction)
- [Malware Detection Trends](#malware-detection-trends)
- [C2 Time to Live](#c2-time-to-live)
- [Open Directories Time to Live](#open-directories-time-to-live)
- [Residential Proxy Infrastructure](#residential-proxy-infrastructure)
- [Conclusions](#conclusions)
- [References](#references)

# Introduction

Adversary infrastructure is the hidden scaffolding of modern cybercrime and
espionage. From command-and-control (C2) services and malware loaders to
proxy networks that route through trusted IP space, this infrastructure lets attackers
scale campaigns, mask origins, and persist long after initial exploitation. For
defenders, understanding this layer is critical: it’s often the best place to detect
and disrupt attacks before they reach intended targets.

This report centers on adversary infrastructure—C2 and the surrounding tools threat
actors use to establish control, move laterally, and exfiltrate data—and examines how
that ecosystem behaves through real data. We examine the structural patterns of
adversary infrastructure at Internet scale—where it resides, how long it persists, and
how different signals reveal continuity even as individual services change. This view
spans both traditional C2 ecosystems and emerging edge-based infrastructure like
residential proxies and IoT botnets, highlighting the ways attackers build, sustain,
and evolve the scaffolding behind modern threat operations.

# Data Accuracy and Historical Context

Censys enables organizations to see the Internet as it truly is and to secure it more
effectively. Governments, enterprises, and insurers rely on Censys for attack surface
management, supply-chain risk assessments, cyber-insurance underwriting, and
monitoring of critical infrastructure.

Tracking adversary infrastructure requires breadth, freshness, and accuracy of Internet
data to deliver insights that are both actionable and trustworthy. Censys provides the
most complete map of global Internet infrastructure, tracking ~794 million IPv4
services[^1]—almost triple the 275 million observed a decade ago when we first started
scanning the Internet.

[^1]: https://dl.acm.org/doi/10.1145/3718958.3754344

While Censys emphasizes accuracy above all else, Censys also excels in speed. In
controlled experiments, it discovered new services in a median of just 5.7 hours (12.3
hours on average), faster than all other platforms. This rapid detection empowers
researchers to identify and monitor fast flux infrastructure designed to evade detection.

![Table showing Self-Report, Est % Accurate, Est % Unique, Est. # Accurate for Censys, Shodan, Fofa, ZoomEye, Netlas]

Over 92% of the services listed in Censys reflect live services, not stale or duplicate
results, ensuring the best insights to track malicious infrastructure. Censys also provides
historical context of every identified IP, Port, and services, providing insights to how
infrastructure has changed over time.

![Table showing Top 10, Top 100, All 65K for Censys, Shodan, Fofa, ZoomEye, Netlas]

With unmatched coverage, Censys identifies 96% of services on the top ten ports and
92% across the top hundred, while still capturing 82% of services across the entire 65k
port space allowing security teams and researchers to track malicious services, open
directories, and other adversary infrastructure running on non-standard or high ports
that are often poorly unmonitored.

Censys is more than a dataset; it is a platform widely adopted across research and
industry. Over 500 academic papers have used its data to study Internet security, public
key infrastructure, IoT devices, industrial control systems, and more. Most relevantly,
Censys has also been used to study malware infrastructure, the subject of this year’s
State of the Internet Report.

# Malware Detection Trends

Let’s begin with a broad look at the malicious infrastructure landscape. We examined
80 of our malware detections over a period of 6 months, from December 2024 to
May 2025.

During this study time frame, we observed an average of 2,906 malware detections
for each snapshot date. Mid-December marked the greatest number we observed
online during the period. Following the peak in December, we observed a 14% drop
in detections in early January. This appears to be primarily driven by a drop in Cobalt
Strike instances in China. Cobalt Strike was the most commonly observed malware
family, and they are largely concentrated in China.

![Graph showing Total Malware Detections Over Time from December 2024 to May 2025]

Note: The data shows detections as of May
2025, but Censys continuously updates and
adds detections over time.

## Malware Families

Cobalt Strike originated as a pentesting and red teaming tool; however, it has been
widely adopted by threat actors since its initial release over 10 years ago. In addition to
C2 functionality, it offers extensible post-exploitation tooling attractive to security
professionals and threat actors alike.

Despite the decline into January and takedown efforts spanning two years[^2], Cobalt
Strike consistently had the greatest observed Internet presence of the detections we
examined during the study period—it represents 34% of the C2s we observed as of
May 2025.

[^2]: https://therecord.media/malicious-cobalt-strike-use-down

The next largest families during this time frame were Viper (15% of total) and Sliver (13%
of total). While Cobalt Strike is a commercial tool, Viper[^3] and Sliver[^4] are open source
alternatives for adversary emulation. Viper and Sliver are slightly younger projects than
Cobalt Strike, but their availability has likely contributed to their popularity.

[^3]: https://github.com/FunnyWolf/Viper
[^4]: https://github.com/BishopFox/sliver

> Operation Morpheus & Other Notable Incidents
>
> Read the story of a global disruption campaign against pirated versions of
> Cobalt Strike and other notable CVE investigations in our blog.
>
> [Read the Blog](https://censys.com/blog/)

![Graph showing Top 10 Malware Detections Over Time from December 2024 to May 2025]

## Geography Trends

As of May, we observed detections in a total of 62 countries globally, with China and
the U.S. topping the list and hosting 55% of malware collectively. Beyond the U.S. and
China, we observe concentrations of malware in Asia, Europe, and North America.

It can be tempting to look for deeper meaning in geographic regions with high
concentrations of malicious infrastructure, but rather than having geopolitical
significance, concentrations of malware are more likely driven by hosting provider
availability, pricing, and permissiveness.

![Graph showing Global Malware Detection Concentrations by Country, May 2025]

Note: The legend depicts only the top 10
countries where we observe detections

## Network Trends

China-based providers Alibaba and Tencent top the list of where we observe the
greatest volume of malware detections across the snapshot dates studied, and Huawei’s
Cloud Service also makes the top 10. Rounding out the list are several U.S.-based
providers, including Cologix, Digital Ocean, Colocrossing, Vultr, Amazon, and Microsoft.

![Graph showing Top 10 ASNs Hosting Malware Over Time from December 2024 to May 2025]

### S P O T L I G H T

#### PlugX

We can also find interesting exposure patterns when we look beyond the most common
families shown above. Consider PlugX as an example.

PlugX[^5] is a remote access trojan (RAT) known since 2008[^6] and used by China-linked
threat actors such as APT41 and Mustang Panda.

[^5]: https://malpedia.caad.fkie.fraunhofer.de/details/win.plugx
[^6]: https://www.exabeam.com/blog/infosec-trends/take-a-deep-dive-into-plugx-malware/

We generally observed a decline in PlugX instances over the study timeframe, apart
from a slight and short-lived uptick in early April 2025. This decline follows news of a
takedown[^7] from the U.S. Department of Justice in January 2025.

[^7]: https://www.justice.gov/archives/opa/pr/justice-department-and-fbi-conduct-international-operation-delete-malware-used-china-backed

![Graph showing PlugX instances, December 2024 through May 2025]

![Graph showing All networks where we observed PlugX instances, December 2024 through May 2025]

In examining all autonomous systems (AS) where we observe PlugX, we note minimal
overlap with the global top autonomous systems where we observe C2 infrastructure.
The only shared ASes are Vultr and Alibaba, which could point to more specific or
discerning operations by PlugX operators.

XNNET, a U.S.-based provider, tops the list of networks where we observe PlugX,
followed by Hong Kong-based Cloudie and CAT Telecom, based in Thailand.

> Malware Case Files
>
> Get the deep dive on some of our research team’s
>
> [Read the Blog](https://censys.com/blog/)
>
> long-running malware investigations.

# C2 Time to Live

A previously unexplored concept of threat infrastructure is their time to live, or TTL.
Understanding how quickly threat infrastructure remains online, disappears, or
moves is incredibly useful for defenders and researchers. Given the unique
perspective of Censys, which is continuously scanning entities on the Internet, we
are able with high confidence to examine TTLs, or the lifespans, of services and
understand the repercussions of varying TTLs for defenders and researchers.

In this section, we will examine a C2 server’s TTL using two perspectives, network
liveliness and content liveliness.

## Lifespans by Network Availability

TTL can traditionally be viewed from
the network sense: how long is a specific
service online before it disappears?

We focus our analysis on the most
common malware families we observed,
Cobalt Strike and Viper.

Cobalt Strike and Viper services
act quite differently.

First, Cobalt Strike’s TeamServer, the part
controlled by a threat actor, services are
much shorter lived, with TTLs on average/
median of 11.2/5.0 days, whereas Viper
services exhibit TTLs of 17.4/18.5 days. We
hypothesize that this is because Cobalt
Strike is more well known and prevalent,
thus showing a much wider range of
behaviors than Viper services.

![Graph showing Most Common Malware Families Observed and their TTLs in days according to service/network availability]

This overarching view of the two C2
families exemplifies the huge variability in
even these basic metrics. We next dive
deeper and examine the most popular
ports for Cobalt Strike and Viper services.

Since there is a much longer tail for Cobalt
Strike than Viper services, we simply show
the five most prevalent ports and their
mean/median TTL in days, found in
Figures 8 and 9.

Even within a family, there can be a
variance of difference. With popular
Cobalt Strike ports, this variance is far
smaller, ranging from an average of 6.3
days to 11.8 days. However, for Viper we
see a much larger range, from an average
of 6.8 days to 30 days (the duration of our
data analysis period). This points to the
need to not only investigate specific
families and their behaviors, but also
specific sub-areas within those families.

![Graph showing Top 5 Observed Cobalt Strike Ports April 2025]

![Graph showing Top 5 Cobalt Strike TTL by Port April 2025]

![Graph showing Top 5 Observed Viper Ports April 2025]

![Graph showing Top 5 Viper TTL by Port April 2025]

## Lifespans by Content

Thus far we have examined TTLs in the
context of network availability: when was
the service online, and when did it go
down? However, there is more to a service
than just its network availability, as a
service often has rich forms of content
associated with it. We examine Cobalt
Strike servers through observed
watermarks for 32-bit copies of Beacon,
and analyze their lifespans through a
content-level perspective.

Watermarks in Cobalt Strike beacons are
an embedded value that are believed to
correlate to a purchaser’s software
license. We begin by examining x86_
watermarks in aggregate during the
month of April. We find a large variation
in the number of unique IPs per
watermark, which indicates that it is
feasible to track liveliness based on
this content-based watermark.

![Graph showing IP Presence for Watermark 1359593325]

Figure 10 shows the difference that
comes with examining hosts at the
watermark, or content, level. If you look
at specific IPs, you can see that while
the service may disappear, the
watermark actually remains the same.

When we use the watermark as an
indicator of liveliness, for these IPs that
have an x86_watermark, we find that the
average/median TTL for services is
9.5/4.0 days, while the average/median
TTL for services based on their
watermarks is actually 11.1/6.0 days. The
increase is slight, but belays the potential
importance of tracking services based on
their uptime or content.

![Graph showing Watermark Changes by IP Over Time]

To add to this nuance, we also check how many IPs have more than one watermark. We
find 14 IPs (an incredibly small population) that have more than one watermark, and
show how the service switches its watermark. In some cases, the switch is within a
single day, which would conflate service liveliness with content liveliness. While 14 hosts
is an incredibly small subpopulation, this points to some interesting takeaways, namely:

1.  We cannot always guarantee
    that service liveliness means
    the host is the same.
2.  These hosts exhibit strange,
    non-conformant behavior that
    is worth investigating further.

What does this mean for security defenders and researchers?

It means that tracking malware families requires both near real-time visibility to the
current state of Internet infrastructure AND also the ability to see historical changes over
time. Understanding the past provides us context for the current state of the Internet,
enriching investigations far more than a single snapshot allows.

Further, when analyzing C2 families, we need to understand both the base behavior of
that family as well as additional, more nuanced factors that can affect analysis
outcomes. For example, things like the port(s) in question, as well as service vs content
liveliness, deepened our analysis. We found that Cobalt Strike services are much shorter
lived than Viper services, which belays the importance of treating C2 families uniquely.

Moreover, this analysis showed how liveliness can be defined by the content of the C2
server itself, which can illustrate how a server is changing (or not changing) even in the
absence of network presence. Understanding these variations can help the security
community produce higher quality analysis.

# Open Directories Time to Live

Open web directories are a cheap,
simple, and stealthy way for attackers to
host malicious payloads AND they’re hard
to detect. OpenDirs are used by malware
families such as AsyncRAT, SuperShell,
Emotet, Mirai and many others.

These are another interesting avenue for
us to perform investigations as they are
literally open directories or filesystems,
often containing payloads and files used
for nefarious purposes. Open directories
are hosted on the public Internet, which
means that not only can attackers find
them, but so can we.

To do so, we need to approach the
problem differently. While we previously
had the benefit of being able to track
Cobalt Strike TeamServer via a distinctive
watermark, open web directories do not
have a specialized field that we can key
on. However, we consider the defining
characteristic of an open web directory to
be the HTTP body, as that is where all the
interesting content of the open directory
is typically found.

So, we examine the lifespans of open
web directories based on their HTTP
bodies. We narrowed down our scope to
look at only open web directories that are
located on an HTTP service for the month
of April. To compare the HTTP body of
the open directory, we calculate the hash
of the HTTP body using TLSH, a rolling
hash algorithm. In short, TLSH allows us
to compare HTTP content more easily.
We calculate the score between the
service’s current TLSH hash and the
service’s previous TLSH hash, where 0 is
not similar at all and 100 is the same, and
we compare the service lifespans of open
web directories based on their service
liveliness and their TLSH comparisons.

![Graph showing A comparison of observable lifespan and similar content lifespan]

Note: Observable Lifespan Q1 and Median both equal
1.0 days; the median line coincides with the box edge.

## Analysis

In Figure 12, we show the percentiles of network lifespans, or pure observability, vs
lifespans based on content similarity:

-   50% vanish in <1 day
-   50% change contents within ~3 days

We find that open web directories have shorter network lifespans, meaning that almost
half of open directories generally come online only to disappear a short while later.
However, when we examine open directories through a content lens, we find their
median lifespan is closer to 3 days. This means that even if a web directory blips in and
out in terms of network visibility, the content doesn’t necessarily change. This distinction
is important, as it allows us to understand how much an open directory has changed, a
critical component for actor investigations.

What does this mean for defenders?

Having up-to-date Internet visibility is crucial as it provides an accurate representation
of hosts and malicious infrastructure in a fast-moving environment. Moreover,
understanding what pieces of infrastructure are available, as well as how they change
are both equally as important. In other words, knowing the content of the infrastructure
and having the ability to see the files inside an open directory allows us to track how
they are changing and fluctuating over time, in addition to their mere presence.

# Residential Proxy Infrastructure

Beneath the hum of everyday Internet
traffic, millions of home and small
business devices quietly pull double
duty, functioning for their legitimate
owners while also relaying traffic for
entirely separate purposes. These
devices form the backbone of
residential proxy networks, which
route traffic through ordinary
consumer equipment.

Not all residential proxies are malicious.
Some operate with the full knowledge
and consent of their owners – for
example, those who rent out their home
router’s IP address to a commercial
proxy service. Owners are often
unaware of exactly how their IP will be
used, but have willingly placed it in a
pool that could serve both benign and
questionable purposes.

However, other devices are leveraged
without consent. In the cybercrime
ecosystem, threat actors commonly
compromise routers, smart speakers,
and other IoT devices to create
residential proxy networks that hide
malicious activity behind trusted,
geographically diverse IP addresses.
This makes them far more difficult to
detect or block than data center proxies
and gives attackers a layer of anonymity.

In this section, we explore Operational
Relay Boxes (ORBs), a particularly
stealthy type of malicious proxy, and
examine one suspected ORB network,
PolarEdge, to illustrate how they function.

## Historical C2 Excavations

As discussed earlier in this report, C2 servers are not always as short-lived as commonly
assumed. Our analysis of a few prominent malware families showed that, on average,
they remained active and responsive for just over a week. This is longer than the
anecdotal expectations of hours or days, but still far more short-lived than most other
types of infrastructure we track. The downside is that C2 IPs and indicators age quickly
– particularly delivery servers – and by the time they are investigated, they often no
longer lead to live infrastructure.

However, even when a known C2 IP is no longer active, we can still pivot off it in
Censys’s historical data to uncover valuable context about an operation. Examining
historical artifacts, such as certificates and services, on a single IP can shed light on
related infrastructure and provide a sense of the broader scale of an operation.

As our investigation revealed, what might appear at first glance to be an ordinary artifact
on a host can take on a very different meaning when analyzed in the context of the
services and networks where it is deployed over time. A normal-looking test certificate
can become a thread that unravels into a larger and more suspicious pattern.

To demonstrate this approach, we turn to “PolarEdge,” a suspected ORB network first
reported on by Sekoia[^8] researchers that resurfaced with new tactics earlier this year.
Starting from just one C2 server, we trace a trail of unusual test certificates and domains
that ultimately reveals an extensive network of proxy nodes.

[^8]: https://blog.sekoia.io/polaredge-unveiling-an-uncovered-iot-botnet/

### S P O T L I G H T

#### Pivoting on a PolarEdge Botnet C2

In February 2025, researchers uncovered PolarEdge, an IoT botnet that has been active
since at least late 2023. It started out by exploiting CVE-2023-20118[^9], a command
injection vulnerability in the web interfaces of Cisco Small Business routers, to implant
base64-encoded webshells. Its tactics have since evolved into a sophisticated operation
leveraging a custom Mbed TLS (formerly PolarSSL) backdoor for encrypted command-
and-control, log manipulation, and dynamic infrastructure updates.

[^9]: https://nvd.nist.gov/vuln/detail/cve-2023-20118

![Image showing Investigations of host 119.8.186[.]227.]

We honed in on a host that was identified by Sekoia as being used to deliver malware
payloads: 119.8.186[.]227, and pivoted to see what additional information we could
discover in Censys.

> The attacker used the IP address 119.8.186[.]227 to distribute these
> payloads via FTP. This address is located in Singapore and belongs to
> Huawei Cloud (ASN: 136907). Based on a Censys search, several non-
> standard TCP ports are open, exposing TLS services associated with
> either suspicious certificates or those linked to Polar.
>
> Sekoia Research Team

We can leverage historical scan data in Censys to go back in time to February 11[^10],
around the time when Sekoia first observed attacker activity, and examine the attributes
of this host to identify potentially adjacent infrastructure. At that time, this host was
exposing multiple services and certificates, including one tied to the domain “www[.]
learningrtc[.]cn” (3f00058448b8f7e9a296d0cdf6567ceb23895345eae39d472350a
27b24efe999) – a domain linked to a WebRTC development e-book. Tracing this
certificate on the web led to a GitHub repository containing an exact match that
appeared to be a test certificate from a legitimate project.

[^10]: https://platform.censys.io/hosts/119.8.186.227?at_time=2025-02-11T09%3A25%3A58Z

On its own, this overlap is not incredibly significant; a legitimate e-book’s test certificate
was reused on some attacker infrastructure. But when we began looking beyond this
specific host, a pattern began to emerge that made this seem less like a coincidence.

Over the past few years, the same e-book certificate has been observed across
numerous hosts, many of which expose other suspicious-looking certificates with a
“PolarSSL” subject and issuer, across seemingly random high ports above TCP/50000.

![Image showing learningrtc[.]cn mixed with a PolarSSL certificate]

The original attacker’s host (119.8.186[.]227) was also serving these strange PolarSSL
certificates on two ports: TCP/50000 and TCP/55555.

This raised the question: Were all these certificates originally legitimate, and only later
co-opted for malicious use? And how was the seemingly benign WebRTC e-book
certificate connected to the PolarSSL ones? To answer that, we traced the origins of the
PolarSSL certificate.

Our early efforts yielded little – unlike the WebRTC cert, there were no public code
repositories or documentation referencing its purpose. At first glance, examining its use
across the broader internet (and over time) suggested a very strong overlap with the
known PolarEdge botnet certificate. However, further review revealed that this cert
appears in older versions of Mbed TLS and is included in the project’s public test data
repository. This means that the overlap we observed does not, by itself, constitute
evidence of a direct PolarEdge connection. However, the continued recurrence of these
two specific certificates across different infrastructures indicated there might be
operational patterns worth investigating further.

We then shifted our focus to hosts currently serving[^11] these certificates, and at the time
of writing, there were plenty of them, but one host immediately stood out:
8.219.153[.]173[^12]. This server was located within the Alibaba Cloud ASN, exposed all of
the certificates we had been tracking, and, most importantly, was serving an open
directory on a high port (TCP/10000) with some extremely interesting filenames:

[^11]: https://platform.censys.io/search?q=%28host.services.tls.fingerprint_sha256+%3D+%22e234e102cd8de90e258906d253157aeb7699a3c6df0c4e79e05d01801999dcb5%22%29
[^12]: https://platform.censys.io/hosts/8.219.153.173?at_time=2025-08-29T19%3A23%3A48Z

![Image showing The chance discovery of an open directory provides a rare view into possible botnet operation tooling.]

This open directory would prove to be a
goldmine, bringing the broader picture into
sharper focus. The contents included
gigabytes of logs, numerous
administrative scripts and configuration
files, and a collection of binaries. From this
open directory, we found two leads that
set the rest of the investigation in motion.

The first was a configuration file, config/
clash.yaml, belonging to the Clash
Proxy[^13] service, and buried inside was a
single upstream SOCKS5 server pointing
to another host, 159.138.83[.]57:55556.

[^13]: https://web.archive.org/web/20250904121146/https://en.clash.wiki/

While that port was no longer active on
that host at the time of writing, it exposed
two very recognizable artifacts on other
ports: the “PolarSSL” test certificates and
the WebRTC certificate on port
TCP/19999. That overlap was too strange
to ignore.

The second, more surprising discovery
was a lone x86-64 ELF binary named
“server_multi” with no known ties to any
public project (it hadn’t even surfaced on
VirusTotal[^14]). Fortunately, it was compiled
with debug symbols intact, making reverse
engineering easier. It looked to be a
potential ORB (Operational Relay Box)
management system.

[^14]: https://www.virustotal.com/gui/file/827797a9bff728ae6f46abd505e67a15e40b0ba69a8dc92a36fd90d9974c9593

#### The RPX Server

The x86-64 ELF binary (SHA256 Hash:
827797a9bff728ae6f46abd505e67a15e
40b0ba69a8dc92a36fd90d9974c9593)
appeared capable of coordinating
(potentially compromised) nodes as proxy
relays. The discovery of this component
(dubbed “RPX” due to several debug
statements referencing the source code
path “/rpx”) offered the first glimpse into
a potentially dedicated backend tool for
managing large-scale proxy infrastructure.

A deeper analysis revealed that this
system was a reverse-connect proxy
server capable of handling SOCKS5 and
Trojan protocols, dynamically assigning
proxy nodes, and relaying traffic with
lightweight DES or XOR encryption.

One of the unusual Mbed TLS test
certificates with the “PolarSSL” subject/
issuer (e234e102cd8de90e258906d2531
57aeb7699a3c6df0c4e79e05d01801999
dcb5) was found embedded in the RPX
binary and used for TLS-encrypted
SOCKS5 communication. This certificate
can be found on thousands of other hosts[^15],
many of which are served on high ports.

[^15]: https://platform.censys.io/search?q=host.services.tls.fingerprint_sha256+%3D+%22e234e102cd8de90e258906d253157aeb7699a3c6df0c4e79e05d01801999dcb5%22

Since we were also able to retrieve a number of log files from this specific open
directory, we could see how many proxy nodes were connected to that specific server at
any given time by grepping for the string “online nodes”. At its peak, in August of 2025,
the system actively managed over 100 proxy nodes simultaneously, which is a clue as to
the scale of the operation.

```
2025-06-20 20:54:38 /root/project/rpx/server.c:1890 online nodes: 101,heart beat 60
2025-06-20 20:54:43 /root/project/rpx/server.c:1890 online nodes: 101,heart beat 60
2025-06-20 20:54:48 /root/project/rpx/server.c:1890 online nodes: 101,heart beat 60
2025-06-20 20:54:58 /root/project/rpx/server.c:1890 online nodes: 101,heart beat 60
```

#### Looking for ORBs

This investigation shows how benign-looking artifacts—such as reused test certificates—
can lead to broader insights into probable botnet infrastructure. While a direct link
between the RPX system and PolarEdge remains unproven, the recurring overlap in
certificates, services, and behavior is a phenomenon that’s likely more than a coincidence.
The chance discovery of an open directory provided a rare view into possible proxy
network management tooling, offering some perspective on how large-scale IoT botnets
may operate. Whether directly tied to PolarEdge or serving as auxiliary infrastructure,
these findings highlight the value of historical internet scan data to uncover hidden layers
of malicious ecosystems.

> Further Reading: the RPX Server
>
> Full investigation details of the RPX proxy management
> binary, its function, purpose and the open directory that
> it was discovered on are available on the Censys blog.
>
> [Read the Blog](https://censys.com/blog/)

# Conclusions

This report examined adversary
infrastructure from multiple angles:
Internet-scale trends across malware
families, geographies, and networks; the
lifespans of C2 services measured both
by network availability and content
signals; the rise of perimeter-blurring
infrastructure such as residential proxies
and ORB-like botnets; and how these
structural patterns play out in real
incidents and disruption efforts. Across
these lenses, a consistent lesson
emerges: access to the most accurate,
up-to-date data on Internet infrastructure
is key to understanding and tracking
threat actor operations and behavior.
Censys helps security practitioners gain
this visibility by maintaining the industry’s
most accurate, comprehensive, and
real-time map of Internet infrastructure.
Our best-in-class visibility empowers
security teams to uncover risks, identify
threats, and strengthen defenses.

Censys delivers real-time Internet
intelligence and actionable threat
insights to global governments, over
50% of the Fortune 500, and leading
threat intelligence providers worldwide.

> See Censys in Action
>
> To see how Censys can help you stay on top
> of emerging threats, request a demo.
>
> [Request a Demo](https://censys.com/get-a-demo/)

# References

1.  https://dl.acm.org/doi/10.1145/3718958.3754344
2.  https://therecord.media/malicious-cobalt-strike-use-down
3.  https://github.com/FunnyWolf/Viper
4.  https://github.com/BishopFox/sliver
5.  https://malpedia.caad.fkie.fraunhofer.de/details/win.plugx
6.  https://www.exabeam.com/blog/infosec-trends/take-a-deep-dive-into-plugx-malware/
7.  https://www.justice.gov/archives/opa/pr/justice-department-and-fbi-conduct-international-operation-delete-malware-used-china-backed
8.  https://blog.sekoia.io/polaredge-unveiling-an-uncovered-iot-botnet/
9.  https://nvd.nist.gov/vuln/detail/cve-2023-20118
10. https://platform.censys.io/hosts/119.8.186.227?at_time=2025-02-11T09%3A25%3A58Z
11. https://platform.censys.io/search?q=%28host.services.tls.fingerprint_sha256+%3D+%22e234e102cd8de90e258906d253157aeb7699a3c6df0c4e79e05d01801999dcb5%22%29
12. https://platform.censys.io/hosts/8.219.153.173?at_time=2025-08-29T19%3A23%3A48Z
13. https://web.archive.org