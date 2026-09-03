No.87

December 2025

HardenStance Briefing

Trusted research, analysis & insight in IT & telecom security                  PUBLIC/SPONSORED

Allot Doubles Down on DDoS Defence
Sponsored by Allot

▪

▪

▪

Cybersecurity is well established as Allot’s long-term growth engine. While Security
as a Service (SECaaS) is the primary focus, the company is also augmenting its DDoS
protection capabilities to grow its share in network protection services for telcos.

Allot is augmenting the inline DDoS defence capabilities of Allot Smart NetProtect with
out-of-band detection. New mitigation options allow telcos to mix and match between
BGP Flowspec and a new off-ramp mitigation solution according to their requirements.

Augmenting the high accuracy/high cost of Allot’s traffic inspection technology with
the lower accuracy/lower cost of sampling traffic out-of-band at L4 makes Allot Smart
NetProtect a lot more compelling for telcos when they issue DDoS protection RFPs.

Cybersecurity is Allot’s long-term growth engine
Before IT systems and digital business processes began to be plagued by cyber threats,
Communications  Service  Providers  (CSPs)  tended  to  view  traffic  visibility,  traffic
management  and  performance  assurance  as  discrete  requirements  they  bought  from
specialist vendors. As malicious traffic has grown, some vendors in the traffic visibility,
traffic management and performance assurance space have pivoted to cybersecurity.

Allot is one such vendor. Nowadays, the company’s CEO, Eyal Harari, routinely refers to
cybersecurity  as  Allot’s  “long-term  growth  engine.”  As  shown  in  Figure  1,  Allot  has
strong  momentum  in  Security  as  a  Service  (SECaaS)  with  revenues  of  $16.5  million
reaching 18% of Allot’s total revenues in 2024. But while SECaaS is the largest part of
Allot’s cybersecurity business, the company also offers network protection solutions for
telecom operators such as DDoS protection services.

Figure 1: SECaaS revenues as a share of Allot’s total revenues

CEO, Eyal Harari,
routinely refers to
cybersecurity as
Allot’s “long-term
growth engine.”

Source: HardenStance/Allot

December 2025 | Allot Doubles Down on DDoS Defence

1

DDoS defence is top of mind for telcos and ISPs
Recent evidence points to the nature of DDoS threats markedly increasing the risk to
the availability and performance of telco networks, services and applications:

▪  DDoS attacks are the #1 cause of cybersecurity incidents. ENISA reports that
DDoS attacks accounted for 77% of all cyber incidents in the EU in the 12 months
to June 2025 – up from 41% in the 12 months to June 2024.

▪

The  telecom  sector  tends  to  suffer  more  DDoS  attacks  than  any  other.
Cloudflare’s  data  does  show  some  variation  quarter  on  quarter,  but  the  telecom
sector overtook gambling and casinos to become the sector of industry that’s most
targeted by DDoS attacks according to the company’s Q2 2025 DDoS threat report.

▪  Nation-state cyber threat actors are expressly targeting the availability of
telco  networks.  Submarine  cable  cuts  in  the  Baltic  sea  have  been  attributed  to
Russian and Chinese state operations. Ukraine’s Kyivstar saw its entire mobile core
wiped by a cyber-attack carried out by the Russian state. Volt Typhoon is a Chinese
state threat actor pre-positioning itself in western critical infrastructure, intent on
disrupting  service  availability.  Recent  years  have  seen  a  marked  uptick  in  DDoS
attacks being attributed to politically motivated ‘hacktivists’. Although they all claim
independence, nation-states direct and fund some of these hacktivist groups.

Botnets drive larger attacks despite high profile take-downs
Perhaps the most notable DDoS incidents of 2025 have been those launched  from the
Aisuru botnet, ramping up in September 2025. As shown below, the size of the attacks
made  media  headlines  but  the  underlying  features  of  Aisuru’s  composition  and
capabilities  are  just  as  important.  Aisuru  is  made  up  of  compromised  smart  home
devices in the homes of Tier 1 U.S carriers. Made worse by faster fixed and fixed wireless
last  mile  connections,  Aisuru  has  been  generating  very  high  volumes  of  outbound  as
well as cross-bound DDoS traffic, causing material disruption to a number of carriers.
Ironically the increased scale and capability of Aisuru has been enhanced by the much-
celebrated  takedown  of  the  RapperBot  in  August.  Once  the  enslaved  devices  were
disconnected from RapperBot, they were re-compromised almost immediately by Aisuru
and other botnets. Some key DDoS threat data points for 2025 are shown below:

▪

▪

▪

Strong  growth  in  overall  DDoS  threat  volumes:  For  the  first  half  of  2025,
Cloudflare reported blocking a total of 27.8 million DDoS attacks of all types. This
compared with just 21.3 million for the whole of 2024.

A new record for the largest ever DDoS attack: In September 2025, multiple
sources reported the Aisuru botnet launching a DDoS attack that peaked at a world
record 22.2 terabits per second (Tbps) and 10.6 billion packets per second (Bpps).

Strong growth in smaller DDoS attacks. Nokia reports that 78% of DDoS attacks
seen in the 12 months to June 2025 lasted less than 5 minutes, up from 44% in the
12 months to June 2024.

Figure 2: Recent threat reports point to higher risk from DDoS attacks

In September,
multiple sources
reported the
Aisuru botnet
launching a DDoS
attack that
peaked at 22.2
terabits per
second (Tbps).

Source: HardenStance

December 2025 |        Allot Doubles Down on DDoS Defence

2

There is some
merit in an all-
inline approaches
to DDoS defence.
The trouble with it
is, however, that it
doesn’t scale well.

New vulnerabilities in a telco’s own attack surface
As demonstrated by the Tactics, Techniques and Procedures (TTPs) used by the Aisuru
botnet, attackers are exploiting new vulnerabilities arising in a telco’s attack surface:

▪

5G Non Stand Alone (NSA) has introduced much faster speeds to 5G devices that
are already being exploited for much harder hitting outbound DDoS attacks.

▪  Where  DDoS  threats  from  botnet-enslaved  IoT  ‘things’  in  the  home  were  once
confined  to  fixed  line  ISPs,  5G  Fixed  Wireless  Access  (FWA)  is  introducing  those
exact same threats into mobile networks.

▪

▪

Now that 5G Standalone (5G SA) is finally starting to roll out a scale, the dynamism
and automation of cloud native network operations creates new risks as well as new
opportunities from a security perspective.

5G network slices – and the SLAs attached to them – are more sensitive to DDoS
attacks  triggering  service  and  quality  of  experience  (QoE)  degradations  than  the
one-size-fits-all, best effort, model of 4G and 5G NSA mobile network operations.

The long inline heritage of Smart NetProtect
Allot has been in the DDoS protection space since 2019. Its solution provides near real-
time DDoS detection and mitigation of  inbound and outbound  volumetric attacks that
still comprise a large majority of all DDoS attacks.

Over the last six years, this solution has relied on sensors deployed inline throughout a
telco network to learn its traffic baseline. A centralized behavioural analytics server that
uses machine learning ingests all the feeds and drives  DDoS detection and mitigation
decisions. In a mobile network, mitigation actions can either be executed via the telco
security team itself or automated via an interface between Allot Smart NetProtect and
the Policy Control Function (PCF) or Policy Control Resource Function (PCRF). Most telco
and ISP customers run it as an additional software license on the same Allot platform
they use for traffic visibility, traffic management, and performance assurance.

An all-inline approach to DDoS defence does have some merit. Inspecting all the traffic
up  through  L7  is  certainly  effective  from  a  detection  perspective.  The  application  of
behavioural analytics and machine learning to threat detection can help compensate for
the loss of visibility arising from the growing share of network traffic that’s encrypted.
Where inline deployments can allow detection of DDoS threats in seconds, out-of-band
traffic sampling up to L4 as widely used in DDoS defence, can take minutes.

The trouble with an all-inline approach, however, is that it doesn’t scale well. It depends
on sensors widely deployed throughout the network. As traffic scales up, more agents
are needed and/or more costs are incurred in inspecting all the traffic.

A new direction in DDoS features from 1H 2026
With  a  new  release  due  in  the  first  half  of  2026,  Allot  is  taking  its  DDoS  protection
capabilities in a new direction. Telco security operations teams will welcome it because
of  how  it  conforms  to  the  DDoS  defence  architecture  that  they  are  used  to.  It  also
maintains its differentiating inline features, albeit more cost-effectively.

The new release of Smart NetProtect will remain dependent on Allot’s packet inspection,
behavioural analytics and machine learning technologies. Inline options are still part of
the  offer,  but  the  exclusively  inline  approach  is  gone.  A  new  hybrid  architecture  still
leverages Allot’s technology, but sensors can now be deployed out-of-band. This is the
architecture that the telecom sector has aligned on over many years as optimal for DDoS
defence.  Behavioural  analysis  powered  by  neural  networks  allows  optimal  anomaly
detection in both inbound and outbound traffic.

December 2025 |        Allot Doubles Down on DDoS Defence

3

Figure 3: Inline and out-of-band DDoS mitigations with Allot’s Smart NetProtect

It's likely that the
first BGP Flowspec
option is all that
many tier 2
carriers will want.
The more
expensive, more
accurate, off-ramp
option will appeal
mostly to tier 1
carriers.

Source: HardenStance

The new release is depicted in Figure 3 and will be Generally Available (GA) in the first
half of 2026. The approach supports two out-of-band mitigation options:

1.  BGP Flowspec: out-of-band detection and mitigation will be supported at L3 and
L4.  The  sensors  will  be  deployed  as  flow-based  sensors  for  detection  based  on
Netflow, IPFix, and S-Flow. Mitigation is via BGP Flowspec. A supporting element of
this architecture is the reuse of the same third-party, cloud-based scrubbing center
used with current inline deployments.

2.  A new off-ramp scrubbing centre leveraging Allot technology: An alternative
approach will also be made available. With this on-demand architecture, suspicious
traffic is redirected to what amounts to a new scrubbing centre. Unlike the current
one, this leverages Allot’s own core technology and is hosted in the telco customer’s
own data centre. This approach can allow telcos to detect and mitigate DDoS attacks
more  accurately  for  superior  network  and  service  KPIs.  One  example  is  enabling
more accurate discrimination between actual DDoS traffic and flash events that look
malicious but are actually benign.

It's likely that the first BGP Flowspec option is all that many tier 2 carriers will want. The
more expensive, more accurate, off-ramp option will appeal more to tier 1 carriers. Telco
security  teams  will  have  the  option  to  mix  and  match  across  the  lower-cost/lower-
accuracy and higher-cost/higher-accuracy mitigation modes. They will do so according
to the unique risk profile associated with different traffic types and their own unique risk
appetite  relative  to  each  one.  A  potential  choice  operators  could  make  is  for  all  TCP
traffic to be redirected to the off-ramp scrubbing center, whereas UDP traffic will only
be redirected according to a threshold or other profile set by the operator.

By enabling Allot’s core technology to be applied in a more targeted, surgical way, rather
than uniformly, telco customers now have a way of deriving the benefits of applying it
to DDoS protection but without overpaying for it. Moreover, the operational model will
be dynamic, allowing mitigation choices to be adjusted with changes in security policy.

Allot  has  recently  introduced  an  optional  ‘Security  Community’  feature  to  Smart
NetProtect. Available to customers whether their deployments are inline or out-of-band,
the security community allows threat intelligence sharing among those telcos and ISPs
that are willing to accept a set of mutual obligations to share and enforce notifications
around known threats as well as recommendations for protecting against them.

The DDoS solutions space has had too little effective competition for far too long.  For
that reason, the reboot of Allot’s DDoS protection suite is very welcome. By embracing
the out-of-band model that telcos know and love, while also sharpening the competitive
differentiation it gets from its core technology, Allot is making a significant contribution
to changing that.

December 2025 |        Allot Doubles Down on DDoS Defence

4

“Allot Doubles Down on DDoS Defence”, Copyright: Patrick Donegan, HardenStance Ltd,
2025

More Information
▪

Allot's "Cyber Threat Report 2H 2024"

▪

▪

Cloudflare's "DDoS Threat Report Q2 2025"

ENISA’s “Threat Landscape 2025”

About Allot
Allot Ltd. (NASDAQ: ALLT, TASE: ALLT) is a provider of leading innovative converged
cybersecurity  solutions  and  network  intelligence  for  service  providers  and  enterprises
worldwide, enhancing value to their customers. Our solutions are deployed globally for
network-native cybersecurity services, network and application analytics, traffic control
and shaping, and more. Allot’s multi-service platforms are deployed by over 500 mobile,
fixed  and  cloud  service  providers  and  over  1000  enterprises.  Our  industry-leading
network-native  security-as-a-service  solution  is  already  used  by  many  millions  of
subscribers globally. www.allot.com

About HardenStance
HardenStance provides trusted research, analysis and insight in IT and telecom security.
HardenStance  is  a  leader  in  custom  cyber  security  research  and  leading  publisher  of
cyber security reports. HardenStance is also a strong advocate of industry collaboration
in  cyber  security  and  is  the  organizer  and  host  of  the  Telecom  Threat  Intelligence
Summit.  HardenStance  openly  supports  the  work  of  key  industry  associations,
organizations  and  SDOs  including  NetSecOPEN,  AMTSO,  The  GSM  Association,  MEF,
OASIS, ETSI. The Cyber Threat Alliance. HardenStance is also a recognized Cyber Threat
Alliance ‘Champion’. www.hardenstance.com

HardenStance Disclaimer
HardenStance  Ltd  has  used  its  best  efforts  in  collecting  and  preparing  this  report.
HardenStance  Ltd  does  not  warrant  the  accuracy,  completeness,  currentness,
noninfringement,  merchantability  or  fitness  for  a  particular  purpose  of  any  material
covered by this report.

HardenStance  Ltd  shall  not  be  liable  for  losses  or  injury  caused  in  whole  or  part  by
HardenStance Ltd’s negligence or by contingencies beyond HardenStance Ltd’s control
in compiling, preparing or disseminating this report, or for any decision made or action
taken by user of this report in reliance on such information, or for any consequential,
special,  indirect  or  similar  damages  (including  lost profits),  even  if  HardenStance  Ltd
was advised of the possibility of the same.

The  user  of  this  report  agrees  that  there is  zero  liability  of  HardenStance  Ltd  and  its
employees arising out of any kind of legal claim (whether in contract, tort or otherwise)
arising in relation to the contents of this report.

December 2025 |        Allot Doubles Down on DDoS Defence

5

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-03", "model": "gemini-3.5-flash-lite"} -->
