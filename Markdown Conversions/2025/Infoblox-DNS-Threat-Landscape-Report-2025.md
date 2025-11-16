# 2025 DNS THREAT LANDSCAPE REPORT

## Table of Contents
- [The Untapped Potential of DNS Intelligence](#the-untapped-potential-of-dns-intelligence)
- [Section 1: Top DNS Threat Observations](#section-1-top-dns-threat-observations)
  - [Ephemeral Nature of Domains](#ephemeral-nature-of-domains)
  - [Control Evasion Via One-Time-Use Domains](#control-evasion-via-one-time-use-domains)
  - [Malicious Versus Suspicious Domains](#malicious-versus-suspicious-domains)
  - [Cloaking Via Domains Part of Traffic Distribution Systems](#cloaking-via-domains-part-of-traffic-distribution-systems)
  - [Domains Linked to Diverse Threat Types](#domains-linked-to-diverse-threat-types)
  - [Domain Popularity](#domain-popularity)
- [Section 2: Threat Actors and Research](#section-2-threat-actors-and-research)
  - [Actor Case Study: Coordination Between WordPress Hackers and VexTrio Viper Cabal](#actor-case-study-coordination-between-wordpress-hackers-and-vextrio-viper-cabal)
- [Section 3: Malicious DNS Techniques](#section-3-malicious-dns-techniques)
  - [Traffic Distribution Systems Provide a Dangerous Level of Evasion](#traffic-distribution-systems-provide-a-dangerous-level-of-evasion)
  - [Malicious Adtech Is a Fast-Growing, Underreported Threat Vector](#malicious-adtech-is-a-fast-growing-underreported-threat-vector)
  - [Large Scale Infrastructures, Hard to Disrupt](#large-scale-infrastructures-hard-to-disrupt)
  - [Malicious Adtech Serves as a Gateway to Enterprise Risk](#malicious-adtech-serves-as-a-gateway-to-enterprise-risk)
  - [Example of TDS at Work:](#example-of-tds-at-work)
  - [Domains Used by Traffic Distribution Systems](#domains-used-by-traffic-distribution-systems)
  - [Domain Hijacking to Steal Trust](#domain-hijacking-to-steal-trust)
  - [Sitting Ducks Attacks](#sitting-ducks-attacks)
  - [Dangling CNAMEs](#dangling-cnames)
  - [Lookalike and Typosquatted Domains Deceive Users](#lookalike-and-typosquatted-domains-deceive-users)
  - [DNS Tunneling Used by Threat Actors, Pentester and Legit Security Tools](#dns-tunneling-used-by-threat-actors-pentester-and-legit-security-tools)
  - [Security Teams Need a Scalpel to Stop DNS Tunneling](#security-teams-need-a-scalpel-to-stop-dns-tunneling)
- [Section 4: Challenges for Defenders](#section-4-challenges-for-defenders)
  - [Adversarial AI Bypasses Existing Security Controls](#adversarial-ai-bypasses-existing-security-controls)
  - [Case Study: Reckless Rabbit Usage of Deepfakes to Target Japanese-Speaking Victims](#case-study-reckless-rabbit-usage-of-deepfakes-to-target-japanese-speaking-victims)
  - [AI-Powered Chatbots](#ai-powered-chatbots)
  - [Code Obfuscation and Evasion](#code-obfuscation-and-evasion)
  - [Protecting Brand and Organizational Reputation](#protecting-brand-and-organizational-reputation)
  - [Compliance Pressures and DNS Challenges for Security Teams](#compliance-pressures-and-dns-challenges-for-security-teams)
- [Next Steps](#next-steps)
- [Terminology Used](#terminology-used)

The Cyberthreat Fog:
How Malicious Actors
Use DNS to Deceive
and Evade

Over the past year, threat actors have rapidly advanced their
use of deception—scaling operations and leveraging AI to target
individuals, organizations, and evade threat research. Infoblox
Threat Intel has observed a new level of professionalism and
speed in the way actors launch Domain Name System (DNS)-
sourced cyberattacks, which affect consumers, businesses, and
government agencies alike.

To defend effectively, security teams must understand the threats
they face. Gaining insight into adversarial DNS techniques,
the actors behind them, and the risks they pose is essential to
strengthening defense strategies.

This report draws on vast volumes of real-time DNS telemetry,
cutting-edge analytics, and decades of threat expertise to provide
a unique perspective on how attackers exploit DNS. It also
outlines the business implications and highlights DNS-based
intelligence as a critical layer of modern cyberdefense.

## THE UNTAPPED POTENTIAL OF DNS INTELLIGENCE

People often refer to DNS as the phonebook of the internet because it translates
domain names into IP addresses. Every digital interaction begins with a DNS
request, making it a high-fidelity source of telemetry for network operations by
providing in-depth visibility into which digital assets are initiating connections
over the internet.

DNS is also utilized by malicious actors when phishing, scamming, for detection
evasion, and during data extraction. Consequently, analyzing DNS traffic and
domain usage is foundational for security analysts. DNS data can be reshaped
into predictive threat intelligence by holistically collecting pre-attack telemetry,
enriching the data, analyzing it against baselines, and executing deep threat
hunts. These insights offer defenders a comprehensive view of adversarial
infrastructures, targeted victims, and tactics—before the attacker strikes.

> “DNS unlocks a unique vantage
point into past threat activity,
which in turn serves as a crystal
ball—revealing the precursors to
future cyberthreats.”

As a result, DNS offers much more than just name resolution
and has become both an enforcement point for enterprise
security policy and an indicator of potential malicious activity on a
network. Organizations like the National Institute of Standards and
Technology (NIST) and the Cybersecurity & Infrastructure Security
Agency (CISA) have recognized this critical—and early—role that
DNS plays in cybersecurity and have highlighted its preemptive
security potential in the recently proposed NIST Special Publication
(SP) 800-81 Rev. 3.[^1]

This report addresses four key questions:

What are the key DNS observations from the past 12 months?

— Dr. Renée Burton
Head of Infoblox Threat Intel

Who are the DNS threat actors and what recent activities have
been discovered?

What are the main malicious tactics behind DNS techniques and
why are they dangerous?

What are the key challenges for defenders, and what opportunities
does DNS-based threat intelligence offer?

[^1]: Secure Domain Name System (DNS) Deployment Guide, National Institute of
Standards and Technology (NIST), April 10, 2025.

## SECTION 1: TOP DNS THREAT OBSERVATIONS

![image](https://i.imgur.com/missing.png)

100.8 million newly observed domains in one year

25.1% of newly observed domains are malicious or suspicious

### Ephemeral Nature of Domains

As of the end of May 2025, Infoblox was processing and analyzing 70 billion DNS queries
daily from over 13,000 Infoblox environments, covering millions of IP addresses across all
types of devices.

The fully anonymized data from 1,300+ Infoblox Threat Defense™ customers provides
global as well as in-depth visibility into millions of internet interactions, spanning multiple
client types, geographies, and industry verticals. Year over year, this DNS telemetry volume
increased by 21 percent.

Within all collected data, Infoblox Threat Intel identified 100.8 million newly observed
domains (second-level domains) in the past 12 months. This high volume of new domains
is often a result of fast-changing infrastructures, short-term advertising campaigns, and
branding initiatives.

### Control Evasion Via One-Time-Use Domains

More than one-quarter of the newly
observed domains (over 25 million) were
classified by Infoblox as malicious or
suspicious. Threat actors continuously
register, activate, and deploy massive
numbers of new domains to evade detection
controls. Because it is difficult to identify
and classify such large volumes of domains,
attackers are able to fly under the radar,
bypass blocking mechanisms, and leave
minimal forensic evidence.

The isolated usage of identified threat-
related domains—both malicious and
suspicious—is also significant. Infoblox
Threat Intel found that 95 percent of all
threat-related domains were observed within
a single network environment.

The objective behind this tactic is simple:
bypass forensic-based defenses that rely
on “patient zero” data by leveraging
throwaway domains—of which attackers
have unlimited supply.

![image](https://i.imgur.com/missing.png)

95% of threat-related domains were observed in only one customer environment.

### Malicious Versus Suspicious Domains

- **Malicious domains** are confirmed threats supported by strong evidence. They do not
age out and account for 1.6 percent of over 100 million newly observed domains.

- **Suspicious domains** are potential threats that lack conclusive evidence and account
for 23.5 percent of all newly observed domains. If not confirmed, these indicators expire
after a few months. Infoblox Threat Intel analysts continuously monitor these domains for
new evidence. When additional indicators are discovered, the scores are updated, and
suspicious domains may be reclassified as malicious.

### Cloaking Via Domains Part of Traffic Distribution Systems

Adtech (short for advertising technology) refers
to the tools, software, and platforms used to
automate, manage, target, deliver, and analyze digital
advertising. Traffic distribution systems (TDSs) are
the platforms or mechanisms used—legitimately or
maliciously—to redirect incoming internet traffic to
different destinations based on predefined rules.
Threat actors also adopted this technology, often
referred to as malicious adtech.

![image](https://i.imgur.com/missing.png)

82% of customers queried a domain part of a traffic distribution system.

Over the past 12 months, 82 percent of all customer
environments queried domains that were part
of TDS, much of which are operated by malicious
adtech operators known for concealing harmful content, such as tailored phishing sites,
scareware, scams, and infostealers.

These TDSs often consist of tens of thousands of domains, which are rapidly rotated to
evade detection, delivering targeted malicious content to the ideal victims while cloaking that
content from threat researchers.

Over time, Infoblox Threat Intel discovered over 1 million domains used by 168 malicious
adtech operators within their TDS infrastructure. These indicators span multiple DNS
techniques, like hijacked domains, lookalikes, redirections, and algorithmically preregistered
domain sets (registered domain name algorithms, or RDGAs). More on TDSs, how they work,
and why they are dangerous in Section 3.

### Domains Linked to Diverse Threat Types

As new threat-related domains are discovered, Infoblox threat researchers investigate
the actors behind them and their underlying intent. The table on the next page presents a
prioritized list of how actors use their domains for various malicious purposes.

![image](https://i.imgur.com/missing.png)

**Table 1. Actors’ purpose for newly observed domains.**

Top 7 List: How Threat Actors Utilize New Domains

1. Engage in fraudulent activities and scams, such as fake cryptocurrency investment sites.

2. Host illegal content, including gambling (particularly in regions like China) and adult material.

3. Create phishing pages designed to steal personal information or credit card data.

4. Deploy malware. Common examples include infostealers (e.g., Lumma Stealer), loaders via drive-by downloads (e.g., SocGholish), botnets, and ransomware (e.g., BlackBasta).

5. Cloak their activities via TDS and deliver various payloads or trick users into allowing unwanted browser notifications.

6. Distribute potentially unwanted programs (PUPs), such as scareware or unnecessary browser extensions.

7. Conduct spam campaigns and distribute malicious emails.

### Domain Popularity

Infoblox DNS telemetry also provides insights
into domain type usage, offering clues about
application popularity and the speed at
which threat actors are becoming proficient
at successfully pushing large volumes of
weaponized domains in front of victims.

Key Observations:

![image](https://i.imgur.com/missing.png)

19 DAYS Time needed for a TDS domain to become popular

- Eight domain categories—such as content delivery networks (CDNs), technology
providers, security vendors, business productivity tools, search engines, storage, cloud
services, and net conferencing—account for the majority (approximately 70 percent
on a given day) of all domains within customer DNS queries.

- In May 2025, domain queries related to personal internet usage—such as online
shopping, gaming, and social media (e.g., TikTok and Facebook)—reached parity with
those associated with professional collaboration platforms (e.g., Microsoft Teams,
Slack). This illustrates the growing overlap between professional and personal
internet use—an overlap that threat actors are acutely aware of.

- Adversaries continuously seek out weak attack surfaces—such as bring-your-own-
device (BYOD) and mobile devices—and deceive users into performing high-risk actions
aimed at extracting business-related data, including credentials. This trend was also
highlighted in Verizon’s 2025 Data Breach Investigations Report,[^2] which affirms that no
device is off limits and notes that 46 percent of stolen corporate credentials originated
from unmanaged or personal devices.

[^2]: 2025 Data Breach Investigations Report, Verizon.

- Infoblox Threat Intel observed domains part of TDSs becoming popular[^3] in as few
as 19 days, 2.35 times faster than in 2024 and 39 times faster than in 2020.
The speed at which TDS domains gain popularity—comparable to legitimate sites like
panerabread[.]com or draftkings[.]com—illustrates how effectively weaponized
domains are propagated and accessed by victims. Threat actors rapidly deploy
large volumes of these domains in front of their targets, maximizing the impact of
their campaigns while outpacing slower intelligence sources, such as open-source
intelligence (OSINT) and forensic-based analysis.

[^3]: A domain is considered popular when it belongs to the subset of domains that account for the majority of customer
traffic during a specific timeframe. It can range anywhere between 6,000 to 10,000 domains on a given day. For more
information, see https://blogs.infoblox.com/wp-content/uploads/infoblox-whitelists-that-work.pdf.

## SECTION 2: THREAT ACTORS AND RESEARCH

![image](https://i.imgur.com/missing.png)

204K total identified suspicious domain clusters

662 total identified DNS threat actors

10 new actors publicly disclosed in the past 12 months

The 100 million new domains discovered over the past year are not forces of nature—they
are always caused by human actions and initiated for specific purposes. Infoblox Threat
Intel continuously analyzes and investigates the actors behind threat-related domains by
enriching collected telemetry and correlating common patterns

Since the start of its research, Infoblox Threat Intel discovered a total of 204,000 suspicious
domain clusters, each sharing common threat elements, and has identified 662 unique
threat actors. In the past 12 months alone, Infoblox researchers have publicly disclosed
10 new actors through various research reports and blog posts.

The following list highlights key threat actors identified and publicly disclosed by Infoblox
Threat Intel between July 1, 2024, and July 1, 2025.

| Actor | Description |
|---|---|
| Enable Scam Actor | This actor operates a malicious TDS that hijacks legitimate web traffic—primarily from compromised WordPress sites—and redirects it to scams, malware, and phishing content. |
| VexTrio | VexTrio is considered one of the most pervasive and evasive actors in the threat landscape. Over the past 12 months, the actor was named in several reports for their relationship with affiliate hackers and is known for hijacking domains to supply their attack infrastructure.  Recently published reports:  • The Vexing and Vicious: The Eerie Relationship between WordPress Hackers and an Adtech Cabal  • Pushed Down the Rabbit Hole |
| Hazy Hawk | This sophisticated DNS threat actor group specializes in hijacking abandoned cloud resources—such as Amazon S3 buckets and Azure endpoints—by exploiting misconfigured or forgotten DNS records, particularly dangling Canonical Name (CNAME) entries.  Once Hazy Hawk gains control over these subdomains, it leverages the inherent trust of legitimate domains to host malicious content. Its operations often involve redirecting users through TDSs to deliver scams, malware, and deceptive push notifications.  Recently published reports:  • Cloudy with a Chance of Hijacking Forgotten DNS Records |
| Enable Scam Actor | This financially motivated threat actor has used hijacked domains for investment scams since February 2023. They embed these domains in short-lived Facebook ads across multiple continents, targeting victims in over 30 languages, including English, Italian, Polish, Turkish, and Spanish.  The actor employs the Sitting Ducks attack vector to hijack reputable domains, which they use to protect their fraudulent sites from security researchers. As of October 2024, Infoblox has identified nearly 5,000 hijacked domains tied to this actor.  Recently published reports:  • Uncovering Actor TTP Patterns and the Role of DNS in Investment Scams  • DNS Predators Hijack Domains to Supply Their Attack Infrastructure |
| Reckless Rabbit | Reckless Rabbit is an investment scam actor that lures victims through malicious Facebook ads. It employs dictionary-based RDGAs and targets individuals in multiple countries, including Austria, Belgium, Denmark, France, Poland, Sweden, the United Kingdom, and others. The actor uses RDGAs and fake endorsements.  Recently published reports:  • Uncovering Actor TTP Patterns and the Role of DNS in Investment Scams |
| Phishing Actor | This phishing actor runs investment scam campaigns that leverage dictionary-based RDGAs and spoof popular services. The actor operates their own domain cloaking service to perform user validation checks and targets Eastern European countries such as Romania, Russia, Poland, and others.  Recently published reports:  • Uncovering Actor TTP Patterns and the Role of DNS in Investment Scams |
| Hasty Hawk | This actor identifies abandoned cloud resources and repurposes them for various malicious activities. Hasty Hawk is known for hijacking domains that are used in charity-themed and DHL-themed campaigns distributed via Google ads. Hasty Hawk primarily uses “bulletproof” hosting networks such as Proton66 along with a TDS to direct users to the content.  Recently published reports:  • DNS Predators Hijack Domains to Supply Their Attack Infrastructure |
| Vacant Viper | Vacant Viper operates the 404TDS, using it to deliver malware and other malicious content. Vacant Viper hijacks domains that are left vulnerable due to misconfigured DNS name servers—a flaw named “Sitting Ducks” by Infoblox researchers—and incorporates them into its malicious TDS infrastructure.  Recently published reports:  • Who Knew? Domain Hijacking Is So Easy |
| Malicious Adtech Actor | This malicious adtech actor leverages WordPress vulnerabilities and distributes malware, phishing pages, fake apps, and unwanted content. They run an extensive TDS that incorporates push notifications, pop-ups, and redirects within a browser, serving ads even after the user leaves the initial page.  Recently published reports:  • The Vexing and Vicious: The Eerie Relationship between WordPress Hackers and an Adtech Cabal |
| Morphing Meerkat | Morphing Meerkat is global spam actor behind an advanced phishing-as-a-service (PhaaS) platform. This actor uses DNS MX records to identify the victim’s email service provider and dynamically serve fake login pages. Morphing Meerkat exploits compromised WordPress websites as well as open redirect vulnerabilities on adtech servers.  Recently published reports:  • A Phishing Tale of DOH and DNS MX Abuse |

### ACTOR CASE STUDY: COORDINATION BETWEEN WORDPRESS HACKERS AND VEXTRIO VIPER CABAL

Infoblox recently uncovered a complex alliance between WordPress hackers and a network
of malicious adtech companies, notably VexTrio’s TDS.

![image](https://i.imgur.com/missing.png)

Figure 1. Relationship between WordPress hackers and commercial adtech industry

What Happened?

- **Quick Migration**: When VexTrio’s TDS was disrupted in fall of 2024, multiple malware
actors simultaneously shifted to a seemingly new TDS named “Help TDS.” Further
analysis revealed that Help TDS is not independent but closely linked to VexTrio, sharing
infrastructure and software components.

- **Coordinated Operation**: Infoblox analyzed 4.5 million DNS TXT record responses from
compromised websites over six months. This revealed two distinct command-and-
control (C2) servers, both hosted on Russian-connected infrastructure, indicating a
coordinated operation between WordPress hackers and the VexTrio cabal.

- **Involvement of Commercial Adtech Firms**: Several adtech companies, including
Los Pollos, Partners House, BroPush, and RichAds, were found to be intertwined with
VexTrio’s operations. These firms facilitated the distribution of malicious content via
smartlinks and push notifications.

The investigation highlights the sophisticated and adaptive nature of cybercriminal networks
leveraging compromised WordPress sites and commercial adtech infrastructures. It
underscores the importance of DNS telemetry and collaborative efforts in uncovering and
mitigating such threats.

## SECTION 3: MALICIOUS DNS TECHNIQUES

Threat actors mentioned in Section 2 use DNS in various ways and with specific objectives
in mind. Once Infoblox discovers a threat-related domain, analytics processes and expert
reviews assign known malicious techniques to the domain. The table below provides an
overview of the most common DNS techniques assigned by Infoblox Threat Intel to threat-
related domains.

![image](https://i.imgur.com/missing.png)

**Table 2. DNS techniques assigned to threat-related domains**

| DNS Techniques and Threat-Related Domains Time frame: January 2025 through June 2025 | Percentage |
|---|---|
| Domains generated by machines algorithms (RDGA, DDGA and DGA) | 54.7% |
| Domains used to redirect traffic | 11% |
| CNAME or alias domains | 5.8% |
| Lookalikes | 5.1% |
| Hijacked domains | 5.1% |
| Domains used in malicious SMS | 4.2% |
| Domains created as part of a TDS | 1.8% |
| Domains used for C2 and exfiltration | < 0.4% |

Many of these techniques overlap during a threat campaign and become part of larger actor
tactics to achieve their objectives. In this report, we dive deeper into four common DNS
techniques, how they are used, and why they are dangerous:

- Usage of domains within TDSs
- Hijacking domains to steal trust
- Lookalike domains to deceive victims
- DNS tunneling for C2 and exfiltration

### TRAFFIC DISTRIBUTION SYSTEMS PROVIDE A DANGEROUS LEVEL OF EVASION

DNS plays a central role in TDS by covertly redirecting users through multiple intermediary
layers—often without their knowledge—based on various attributes like geolocation, device
type, or security posture. DNS plays a foundational role in determining how and where
network traffic is routed. Legit operators of TDS are mostly found in digital advertising or
adtech. The name adtech (short for advertising technology) refers to the tools, platforms, and
software used to manage, deliver, and analyze digital advertising campaigns.

Just like known legal advertising technology (e.g., Google AdSense), malicious adtech
delivers the right content to the right audience at the right moment to increase the
effectiveness of their campaigns. This type of cyberthreat is carried out by specialized
organizations with many affiliates and deep pockets.

![image](https://i.imgur.com/missing.png)

**Table 3: TDS operators and the percentage of customer connection attempts they received**

| Top TDS Operators by Connection Share | Connection Share |
|---|---|
| Actor Name |  |
| VexTrio Viper | 72.8% |
| Vane Viper | 68.4% |
| Venal Viper | 72.5% |
| Undisclosed actor | 64.8% |
| Vero Viper | 60.5% |
| Tiano Gambling | 50.9% |

At the heart of these activities is a TDS that profiles victims and routes them to malicious
advertisers while pointing threat researchers to a decoy site.

![image](https://i.imgur.com/missing.png)

Figure 2: A high-level picture of the three players in malicious adtech; affiliates, operators, and
malicious advertisers

### How Malicious Adtech Works

There are multiple reasons why malicious adtech is harmful and should be an important area
of focus for enterprise security teams:

### Malicious Adtech Is a Fast-Growing, Underreported Threat Vector

Attackers are increasingly leveraging malicious ad networks as a low-cost service to deliver
malware and other malicious content. These ads can lead to various types of attacks,
including drive-by downloads, phishing sites, credential stealers, and exploit kits
(see Table 4: TDS operators and delivered malicious content).

Because most of the security industry relies on a patient-zero approach—collecting
telemetry during (e.g., sandboxing) or after (e.g., forensic-based intelligence) an attack—
the resulting countermeasures are limited to artifacts discovered from that initial point of
compromise. This limitation makes TDSs effective tools for evading detection, as actors
continuously alter the malicious content they deliver and redirect threat researchers to
decoy sites. Consequently, TDSs have become one of the most underreported threats in the
cybersecurity industry.

### Large Scale Infrastructures, Hard to Disrupt

Organizations operating malicious adtech often build infrastructure at considerable
scale, including tens of thousands of fast-changing domains designed to redirect users
and lure them into accepting browser push notifications. These operations are frequently
compartmentalized into multiple entities to carry out cybercrime while avoiding legal
scrutiny. Some operators, such as VexTrio Viper, have persisted for years, becoming highly
profitable—and their activities show no signs of stopping.

### Malicious Adtech Serves as a Gateway to Enterprise Risk

Malicious adtech deceives victims by mimicking popular brands or offering content they are
eager to access, encouraging them to drop their guard and engage in high-risk interactions.
Although these threats typically originate on consumer-facing sites, they can easily infiltrate
corporate environments—exposing employees’ personal devices to weaponized content.
This allows threat actors to perform reconnaissance or impersonate enterprise notifications,
elevating the risk to organizational networks.

![image](https://i.imgur.com/missing.png)

**Table 4. TDS operators and delivered malicious content**

| DNS Operators | Malware | Scams | Phishing | Hijacked Domain |
|---|---|---|---|---|
| Vacant Viper | X | X | X | X |
| Vane Viper | X | X | X |  |
| Vextrio Viper | X | X | X |  |
| Hasty Hawk | X | X |  |  |
| Sophisticated Chickens |  |  | X |  |
| Black TDS |  |  | X |  |
| Parrot TDS |  |  | X |  |
| R0bl0ch0n TDS |  |  | X |  |

### Example of TDS at Work:

When a victim visits a compromised site from a mobile device or endpoint, the operator may
present a fake CAPTCHA to trick the victim into accepting browser push notifications from
a malicious advertiser. These notifications can then deliver additional fraudulent content,
such as prompts to download unverified software, share personal information, or enter
organizational credentials.

As the TDS profiles incoming victims, SOC analysts or threat researchers using common
security tools may not detect these notifications or malicious content—they may instead be
redirected to a decoy site displaying legitimate material.

Because of the overlap between professional and personal internet usage, malicious
advertising technology has become a significant contributor to cybercrime, especially to
mobile devices, tablets, BYOD and unprotected assets.

![image](https://i.imgur.com/missing.png)

Figure 3: Examples of VexTrio Viper’s landing page that leads the user to accept push notifications on their
device; these were both seen when browsing to germannautica[.]com

### Domains Used by Traffic Distribution Systems

Over the past 12 months, Infoblox Threat Intel discovered over 1 million indicators used by
168 malicious adtech operators within their TDS. These indicators span multiple techniques,
including RDGAs, redirections, hijacked domains, lookalikes, and others.

TDSs used by malicious adtech operators can be quite large. Many include over 10,000
domains, with some exceeding 100,000. However, the size of a TDS does not necessarily
correlate with its pervasiveness or threat level. Vigorish Viper operates a vast and growing
network of 170,000 active domains but primarily targets victims in China, Hong Kong, and
Macau. Venal Viper, though not among the top five in size, is one of the most frequently
queried in customer networks—65 percent of all Infoblox customers have queried a Venal
Viper domain in the past 12 months.

### Disrupting TDS

Harmful adtech using TDSs thrives because it masquerades as legitimate advertising,
deceives victims, and evades detection by security tools that rely on identifying known
malicious behaviors through simulations or patient-zero data. In contrast, DNS records can
reveal when and how new malicious infrastructure is configured.

Researchers who leverage real-time and historical DNS data—combined with innovative
data science—can identify suspicious or malicious domains before any payload is delivered,
including those used in malicious adtech.

DNS-derived intelligence sheds light on the infrastructure behind the threat, such as how the
TDS operates and redirects traffic. Unlike other security methodologies, DNS-based security
implementations can proactively uncover malicious adtech and prevent internet-connected
endpoints from interacting with it.

Put simply, by focusing on attacker infrastructure, DNS-based protection breaks the supply
chain between malicious advertisers and victims—offering long-term protection rather than
merely reacting to the latest payloads.

### DOMAIN HIJACKING TO STEAL TRUST

Threat actors hijack existing domains primarily to exploit the credibility and trust associated
with legitimate domains. Once under control of the adversary, hijacked domains can be used
to create convincing phishing sites, get prioritized by search engines, bypass spam filters, or
execute fraud.

Infoblox Threat Intel discovered multiple ways actors hijack domains and the tools they use
to deceive users.

### Sitting Ducks Attacks

Sitting Ducks attacks gained prevalence over the past years. In 2024, Infoblox Threat Intel
estimated that more than 1 million domains are vulnerable to this attack. During a deep
research exercise in the second half of 2024, 70,000 domains were discovered hijacked
out of a pool of 800,000 vulnerable domains. This highlights the scale of the problem and
the need for robust security measures.

Multiple threat actors use these techniques systematically. The ease with which these
attacks can be executed—combined with the difficulty security teams face in detecting
them—makes them particularly dangerous.

Actors known to be exploiting this attack include VexTrio Viper, Vigorish Viper, Horrid Hawk,
and Hasty Hawk. These groups have demonstrated the effectiveness of Sitting Ducks
attacks, underscoring the need for heightened vigilance and improved security practices to
counter these threats.

### Dangling CNAMEs

In early 2025, threat actors exploited redirection configurations on high-reputation domains
such as cdc[.]gov and several U.S.-based universities. This was possible because
organizations had decommissioned cloud applications (e.g., CDNs) hosted by third-party
providers (such as Microsoft Azure) while leaving their DNS aliases (CNAME records) active.

Malicious actors like Hazy Hawk exploited this lapse in DNS hygiene by creating new content
on the same CDN. The motive was simple: by leveraging the reputation of the original domain
alias, they were able to trick Google and other search engines into indexing the malicious
content and including it in search results.

### LOOKALIKE AND TYPOSQUATTED DOMAINS DECEIVE USERS

Lookalike domains are slightly altered domain names
registered to deceive users. They often impersonate
legitimate brands, employee communications, supply
chains, or other trusted partners, causing significant
issues.

Attackers used lookalike domains in SMS messages,
phone calls, direct messages on social media,
emails, and QR codes. Recently, they targeted
multi-factor authentication (MFA) due to its growing
adoption by everyone from gamers to digital currency
marketplaces. Other examples include bypassing
enterprise MFA or abusing domain names from
popular identity access platforms.

![image](https://i.imgur.com/missing.png)

Figure 4. MFA message from lookalike domain

Lookalike domains have become a significantly larger problem as there are over 1,500
top-level domains, increasing costs for most organizations to monitor all variations.

Additionally, organizations may have multiple groups registering domains and lack visibility
into who is doing what. Security teams may think a similar-looking domain was created by
the helpdesk or cloud application team, but the new domain may actually be configured by
an actor to phish customers.

A lack of expertise within security teams often creates an appetite for quick fixes through
managed services. Unfortunately, lookalike domains are not an easy problem to solve.
Even mature security teams continue to encounter them, and effective monitoring requires
significant diligence.

### Infoblox: Identified Lookalike Techniques

- **Homographs or homoglyphs** use visually similar characters from different character sets, such as Cyrillic or Greek (e.g., substituting “o” with “0”). The technique is effective because the inserted characters are not always clearly distinguishable.

- **Typosquats** include sneaky typing errors by registering domains that closely resemble popular websites (e.g., substituting “amazonn[.] com” for “amazon[.]com”) to take users to a fraudulent website.

- **Combosquats** combine well-known brand or company names with other keywords, such as “mail”, “security”, or “support”. Combosquatting is around 100 times more prevalent than typosquatting.

- **Soundsquats** are the most recent form of lookalike threats, using domain names that sound similar when spoken aloud (e.g., “hsbsee[.]com” instead of “hsbc[.]com”). It deceives users when using smart devices, such as Google Home, Siri, and Alexa.

### DNS TUNNELING USED BY THREAT ACTORS, PENTESTERS AND LEGIT SECURITY TOOLS

DNS tunneling encodes data within DNS queries
and responses, enabling covert communication
that is often exploited for C2 operations and
data exfiltration.

While Infoblox observed over 480 unique DNS
tunneling domains in some months, an average
of more than 100 unique domains related to
DNS tunneling were discovered per month
between June 2024 and June 2025. In addition to
cybercriminal use, DNS tunneling is also employed
in legitimate penetration testing and security tools.
The following list provides an overview of prevalent
DNS tunneling tools with C2 capabilities.

![image](https://i.imgur.com/missing.png)

+100 unique DNS tunneling domains found monthly—benign and malicious

- Cobalt Strike is a widely used pentest tool featuring a DNS C2 module. Utilized by red
teams and threat actors, it employs Hex-encoded queries with optional customizable
prefixes like “post”, “api”, or “dx”.

- Dnscat2 is a tool used for creating encrypted DNS tunnels. It is included within
METASPLOIT, an open-source penetration testing tool.

- DNS Exfiltrator is a tool that encodes data into DNS queries for exfiltration, illustrating
the potential misuse of DNS in practical scenarios. It uses TXT records, allows only one-
directional communication, and is initiated via the command-line. Infoblox has
not observed its use by a threat actor and considers it impractical due to the
one-directional mechanism.

- Sliver is a cross-platform C2 framework with DNS tunneling capabilities, frequently
utilized in adversary simulations and malicious campaigns.

- Weasel is a less-documented DNS tunneling tool developed by Facebook’s Red Team
that supports stealthy