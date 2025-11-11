# AI Instruction Set for Converting Technical PDFs to Markdown

## Purpose
Ensure technical PDFs are converted to Markdown with complete fidelity, preserving all content, structure, and formatting.

## Goals
1. **Full Conversion**: Include all text, quotations, footnotes, references, and technical terminology without omission or summarization.  
2. **TOC Format**: Include a fully functional Table of Contents with proper linking.  
3. **Markdown Conventions**: Use clear, consistent, and professional formatting.  
4. **Images**: Describe image contents without embedding.

## Conversion Instructions
### Content
- **Include All Text**: Retain all sections, preserving the original structure and content.  
- **Headings**: Format with `#` for main headings, `##` and `###` for subheadings.  
- **Lists**: Use `1.` for ordered lists, `-` for unordered lists.  
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and \`\`\` for code blocks.  
- **Links**: Format as `[text](URL)` and ensure accuracy.

### Images
- **Do Not Embed**: Replace with descriptive text: `![Image description]`.

### Table of Contents
- Place after the document title but before the main content:
  ## Table of Contents
  - [Section Title](#section-title)
  - [Subsection Title](#subsection-title)
- Ensure anchor links work and follow the format `(#section-title)`.

### Footnotes and References
- Use Markdown footnote syntax:  
  Content with a footnote[^1].  
  [^1]: Footnote content here.
- Retain all technical and academic terms exactly.

## Verification and Quality Assurance
1. **Accuracy**: Verify the entire document is converted without omissions.  
2. **TOC Functionality**: Check all links point to the correct headings.  
3. **Readability**: Ensure professional formatting and adherence to Markdown standards. DO NOT enclose the top and bottom of the content in ```markdown and ``` . 
4. **Fidelity**: Confirm the output matches the original PDF exactly.  
---
# Cyber Threat Landscape
Report 2025

Version 1.4 | 21 July 2025

## Table of Contents
- [Editorial Foreword](#editorial-foreword)
- [1. Executive Summary](#executive-summary)
- [2. Developments and Insights](#developments-and-insights)
- [3. Regional Incidents](#regional-incidents)
    - [a) ASEAN](#asean)
    - [b) East Asia](#east-asia)
    - [c) South Pacific](#south-pacific)
- [4. Territorial Insights](#territorial-insights)
    - [a) Singapore](#singapore)
    - [b) Malaysia](#malaysia)
    - [c) Indonesia](#indonesia)
    - [d) South Korea](#south-korea)
    - [e) Australia](#australia)
    - [f) Greater China Region](#greater-china-region)
- [5. Outlook of Cyber Threats for 2025](#outlook-of-cyber-threats-for-2025)
- [6. Defensive Actions for Cyber Defenders and Leaders](#defensive-actions-for-cyber-defenders-and-leaders)
- [7. Contributors](#contributors)
- [8. Appendices](#appendices)
    - [a. Techniques Heatmaps by Territory](#techniques-heatmaps-by-territory)
    - [b. Territorial Observed Top Exploited Vulnerabilities](#territorial-observed-top-exploited-vulnerabilities)
    - [c. ICS oriented Techniques Heatmaps](#ics-oriented-techniques-heatmaps)

## Editorial Foreword
<a name="editorial-foreword"></a>

The cyber threat landscape continues to evolve with geopolitical tensions, trade tensions, internal strife and the
evolving adversarial behaviours fuelling the changes. Across the Asia Pacific, we have seen threats becoming
more persistent, more targeted, and more difficult to defend against. We have developed this report to share our
observations on the key trends and developments shaping the region’s cyber threat landscape.

This year’s edition includes observations from across ASEAN, East Asia and the South Pacific. As our regional
presence grows, we remain committed to bring an Asia Pacific focussed view of the cybersecurity situation of
the  digital  environment  we  operate  in,  whether  through  the  threat  intelligence  we  gather,  the  incidents  we
respond to, or the platforms we contribute to.

The  environments  in  which  we  operate  are  complex.  From  geopolitical  flashpoints  and  trade  tensions,  to
localised unrest and cross-border criminal activity, each region presents its own unique cyber risk profile. Such
an  environment  has  proven  fertile  for  the  thriving  underground  economy,  which  we  observe  to  have  active
collaborations  and  subcontracting,  leading  to  increasing  capability  developments,  and  increased  scale  and
efficacy of cyber-attacks and campaigns.

The  widening  use  of  diverse  technologies,  including  those  from  established  Western  vendors,  open-source
solutions,  and  the  emerging  Eastern  technology  solutions,  have  led  to  increasingly  the  fragmented  digital
ecosystems.  This  complexity  makes  defending  against  Ransomware,  state-linked  cyber-attack  campaigns,
cybercrime, and hacktivism not only more challenging, but also more urgent.

Ransomware in particular, has become endemic in the region, if not globally. We are seeing variants that bypass
EDR and XDR systems with increasing success. Hacktivists are also becoming more tactically capable, moving
beyond surface-level disruption and website defacements, to leverage advanced exploit platforms. Meanwhile,
organised  cybercrime  groups  are  expanding  in  number  and  sophistication,  with  many  of  them  working  in
concert  with  larger  threat  actors.  These  collaborations  are  increasing  the  complexity  to  determine  the
motivation and “mastermind” behind attacks.

Ensign remains committed to monitor how these developments are reshaping the threat landscape. This report
outlines  key  defensive  considerations  and  offers  recommendations  that  security  leaders  can  act  on  to  stay
ahead of a threat environment that shows no sign of slowing down.

As  a  Research  Sponsor  to  the  MITRE  Center  for  Threat  Informed  Defense  and  an  advocate  for  the  threat-
informed defence concept, we continue to provide tactics, techniques and procedures (TTPs) for the observed
threats leveraging the MITRE ATT&CK framework, version 17 this year, with the MITRE ATT&CK Navigator JSON
files for cyber defenders to use in monitoring, threat hunting, red teaming, risk assessments, and other cyber
defence operations.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Ensign  InfoSecurity  is  the  largest
cybersecurity  service  provider
in
Asia.  Headquartered  in  Singapore,
Ensign  offers  bespoke  solutions
and services to address our clients’
cybersecurity needs.

assurance

Our  core  competencies  are  in  the
provision  of  cybersecurity  advisory
and
services,
architecture  design  and  systems
integration  services,  and  managed
for  advanced
security  services
threat  detection,  threat  hunting,
and incident response.

Underpinning  these  competencies
and
is
development in cybersecurity.

research

in-house

Ensign has more than two decades
of  proven  track  record  as  a  trusted
relevant  service  provider,
and
serving  clients  from  the  public  and
private  sectors  in  the  Asia  Pacific
region.

For more information, visit
www.ensigninfosecurity.com or
email
marketing@ensigninfosecurity.com

## 1. Executive Summary
<a name="executive-summary"></a>

Since the formation of Ensign in 2018, we have released these threat reports to help our clients and
the general community understand the state of the threat environment in Asia Pacific.  In 2025, we
note the growing geopolitical and trade tensions around the world and observed the growing cyber
activities by a number of threat groups.

For 2025, key insights to note:

1. State-sponsored  threat  groups  are  increasing  their  activities.  They  are  likely  to  be  pre-
positioning,  in  light  of  geopolitical  and  trade  tensions,  to  maintain  strategic  opportunities  for
future effects by compromising digital infrastructure and the cyber supply chain. Whether this is
for the purposes of staging for future attacks, espionage or disruption. The intentions are multi-
fold, but we suspect this will grow significantly, posing concerns for the public sector and critical
infrastructure operators.

2. Ransomware  continues  to  be  the  endemic  “digital  flu”  that  plagues  companies  across  the
world. Criminal groups are collaborating and competing in the underground economy for a larger
share of the prize. New capabilities are being developed and the efficacy of attacks will grow. We
note:

▪ Initial Access Brokers (IABs) pursuing a “breach once, sell to many” approach.

▪ Mastermind  threat  groups  subcontracting  cyber-attack  tasks  to  other  parties  to  create

multi-prong and distraction effects in their cyber campaign.

▪ Multiple income streams pursued for financial gain amongst organised crime groups.

3. Finally,  attacks  are  also  targeting  the  weaker  but  highly  important  links  in  our  economic
systems.  In  particular,  we  are  witnessing  attacks  on  our  business  and  professional  services
(BPS) firms, including legal firms, accounting companies and professional services firms. These
companies hold (or are custodians of) significant assets but are not large enough to mount deep
defences, and have come under increasing attacks from threat groups.

The cyber  space  is not  a benign place  and  as  digitisation grows, and the use  of  AI becomes  more
pervasive,  the  threats  will  commensurately  grow.  Ensign  remains  committed  to  defending  and
protecting our customers in this environment.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

## 2. Developments and Insights
<a name="developments-and-insights"></a>

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

Top Developments and Insights of 2024

![Image description: A table summarizing top developments and insights of 2024, including Ransomware adopting capabilities to circumvent defenses, state-sponsored threat groups adjusting pre-positioning, IABs adopting "breach once, sell to many" approaches, hacktivists evolving through collaboration, AI exploited for influence operations, and technology bifurcation creating fragmented attack surface.]

The  Asia  Pacific  region  experienced  a  high  intensity  of  cyber  threat  activity  in  2024,  fuelled  by
geopolitical  tensions  (e.g.,  South-China  Sea  disputes,  PRC-ROC  tensions,  PRC-DPRK-Russia
involved  activities),  increasing  economic  competition  (e.g.,  US  tariffs,  US-China  tensions),
challenges  (e.g.,  Myanmar  civil  unrest,  organised  crime  syndicates  operating  along  Thailand’s
border),  and  uneven  progress  made  in  digitalisation  and  cyber  defence  maturity  (laws  and
operations).

Across the territories, Ensign observed increasing variety of technologies implemented, from well-
established and familiar Western solutions, open source and open source adapted solutions, and
Eastern  (predominantly  driven  by  Chinese  companies)  solutions.  The  rising  diversification  of
technologies  used  in  the  organisations’  digital  attack  surface  elevates  the  complexity  and
challenges  organisations  face
increasingly
competent and sophisticated cyber threats.

in  maintaining  effective  defences  against  the

In the midst of the situation in 2024, the public sectors and organisations have been making steady
progress  in  bolstering  the  cyber  defences.  Governments  across  the  world  have  updating  their
regulations  to  provide  greater  guidance  on  how  to  lay  out  the  cyber  controls  for  businesses  and
critical infrastructure – the EU updated the NIS legislation to enhance cybersecurity resilience and
digital  defence,  Singapore  updated  the  Cybersecurity  Act,  Indonesia’s  Personal  Data  Protection
Law and Malaysia’s Cyber Security Act came into effect in 2024, just to name a few. Amidst these
regulatory developments, regional and international efforts are also underway to build up capacity
and  capability  through  collaborative  efforts  and  exercises  –  the  efforts  through  the  ASEAN-
Singapore  Cybersecurity  Centre  of  Excellence  (ASCCE)  in  Singapore,  and  the  ASEAN-Japan
Cybersecurity  Capacity  Building  Centre  (AJCCBC)  in  Thailand,  the  establishment  of  the  ASEAN-
CERT, the annual EU Locked Shields exercise, and continued dialogue and proliferation of the UN
cyber norms, just to name a few.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

RANSOMWARE,  with  (i)  the  leaks  of  Ransomware  platform  source  codes  (e.g.,
LockBit  and  Conti)  and  Ransomware-as-a-Service  (RaaS)  operations  playbooks,  (ii)
the  reorganisation  of  constituent  operators  (i.e.,  initial  access  brokers,  RaaS
operators, negotiators, crypto mixers and launderers), the barrier to entry for parties
with malicious intent to rapidly adopt Ransomware operations has been lowered.

Supported by the now commonplace pervasiveness of generative AI solutions, both
in  the  public  and  deep  and  dark  web  (DDW),  threat  actors  are  now  more  rapidly
evolving  their  exploits,  techniques,  playbooks  and  platforms  to  increase  their
success rates in penetrating organisations and extracting value from them, whether
that  be  (i)  information  and  monetary  value,  or  (ii)  to  cause  pain  through  disruption,
compromise of operations and destruction of technology services.

The  prevalent  RaaS  variants  in  2024  have  developed  novel  capabilities  which
advance the Ransomware groups’ financial gain objectives, notably, (i) the ability to
evade  endpoint  detection  &  response  (EDR)  and  extended  detection  &  response
(XDR)  solutions,  (ii)  having  the  ability  to  kill  processes  through  bring  your  own
vulnerable driver (BYOVD) – particularly to impair defences, and (iii) adopting unique
programming languages to enhance performance, target multi-platform and achieve
stealth objectives.

This situation in aggregate, has raised the profile of Ransomware as the new digital
endemic  “flu”.  Within  Ensign’s  operating
territories,  LockBit  Gang,  Kill
Ransomware,  RansomHub  and  Sarcoma  Ransomware  are  the  most  active,  in
ranking order.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

HACKTIVISM  related  activities  have  been  driven  by  the
troubled  times  we  live  in  today.  The  World  Economic  Forum
(WEF) and the United Nations (UN) have both acknowledged
that  we  are  in a  modern  period  of  a  confluence  of  conflicts,
disagreements and disruptions around the world, with some
stakeholders  taking  on  a  “might  is  right”  approach,  and
others  taking  a  more  insular  approach  towards  trade  and
international engagements.

conflicts  which  complicate  the  treatment  to  these  groups.
This also presents as a boon and a bane – the advantage of
increased  organisation  means  that  it  becomes  easier  for
defenders to profile and defend against these groups’ cyber-
attacks, with the knowledge that they will likely become more
competent  and  successful.  The  active  hacktivist  groups
observed targeting the territories include Bjorka, ETHERSEC
Team Cyber, R00TK1T and RipperSec.

the

increasingly  mature  underground
Enabled  by
collaboration  and  sharing  of  capabilities  and  services,  we
observed  the  evolution  of  some  hacktivists  taking  on
advanced  capabilities  beyond  the  conventional  distributed
denial  of  service  (DDoS)  attacks,  website  defacements,  and
data  breaches.  DragonForce  Ransomware  emerged,  with
some  connectivity  to  the  previously  reported  DragonForce
Malaysia  hacktivist  group,  which  most  recently  attacked
retail brands in the United Kingdom[^1] (i.e., Marks and Spencer,
Co-op, and Harrods). It first posted, in July 2022, the desire to
to  have
become  a  RaaS,  and  has  been  observed
refactored/forked  its  Ransomware  from  the  leaked  source
codes from LockBit and Conti.

We  are  also  rapidly  observing  Hacktivists  accelerating  their
development  of  exploit  platforms,  e.g.,  MegaMedusa  DDoS
platform  for  the  RipperSec  hacktivist  group,  and  the
increased  collaboration  with  other  hacktivist  or  organised
crime groups as seen in the collaboration between R00TK1T
and the Cyber Army of Russia. When hacktivists rally behind
in  grey  zone
state-linked  causes,  they  also  participate

(IABs)  active

INITIAL  ACCESS  BROKERS
the
territories  are  generally  observed  to  be  individual  or  small
groups  of  individuals  working  as  mercenaries  for  hire.  While
some of the IABs have affiliations with unique threat groups,
especially RaaS groups, others generally collaborate with any
other threat group as long as the price is right.

in

Increasingly,  IABs  have  adopted  a  “breach  once,  sell  to
many”  practice,  working  with  RaaS
groups  with
advantageous  affiliate  programs  for  prioritised  access,  but
subsequently  sell  access
the
to
“embargoed”  period.
opportunistically  collect/exfiltrate  data  assets  upon  breach
to be put up for sale as additional income streams; these are
commonly called infostealers.

to  other  parties  after
IABs  are  also  observed

IABs  are  observed  to  leverage  alternative  authentication
material’s such as session keys, OAuth tokens and the like to
gain  access  rather  than  directly  accessing  user  credentials,
although,  there  is  no  shortage  of  leaked  user  credentials
available on the region’s users.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

ORGANISED  CRIME  group  activities  have  been  steadily  rising  with  the  increased
digitalisation of the region with many territories having electronic public sector services,
and digital banking and payment ecosystems.

The  proliferating  collaborations  in  the  underground  community  have  also  given  rise  to
subcontracting  work  leading  to  more  (individual)  initial  access  brokers  (IABs)  supporting
other  “mastermind”  threat  actor  groups.  IABs  exploiting  the  use  of  AI,  are  now  more
effective  and  efficient  in  gathering  credentials,  performing  target  reconnaissance,  and
identifying vulnerabilities for exploitation.

Organised  crime  groups  have  been  observed  to  leverage  AI  most  with  enhancing  the
efficacy  of  phishing  attacks  by  enhancing  the  believability  of  the  phishing  content,  and
adapting  a  multi-channel  strategy  (e.g.,  initial  contact  on  one  communication  platform,
and  asking  the  victims  to  follow  through  payments  in  other  platforms)  towards  getting
their victims to execute actions triggering compromise. The multi-channel strategy aims to
throw  off  the  digital  trails  in  being  easy  to  identify  them,  but  also  to  confuse  victims  for
payments.

The past year saw a doubling of Organised Crime groups actively targeting the territories
(from  5  to  10).  This  is  despite  having  successful  law  enforcement  activities  taking  down
threat actors, e.g., the arrest of GhostR/0mid16B/DESORDEN in Thailand[^2].

Other than operating RaaS, some of these Organised Crime groups are observed to have
been  subcontracted  to  perform  data  breaches,  service  disruptions,  compromise  supply
chains, to help “mastermind” threat groups achieve their campaign objectives.

The  Organised  Crime  groups  observed  in  the  territories  include  BITTER,  Blackwood,
Bronze  Highland,  FIN11,  FIN7,  GhostR,  Pseudo  Hunter,  SharpPanda,  TIDRONE,  with
Void Arachne. BITTER, Blackwood, Bronze Highland, Pseudo Hunter, and Void Arachne
observed to pre-dominantly target the Greater China Region (GCR).

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

STATE-SPONSORED threat groups have been observed to represent close to 40% of cyber
activities  in  the  region  (39.8%),  with  deepening  significance  in  their  attacks.  Many  of  these
threat  groups  are  observed  to  be  well-resourced,  have  high-level  capabilities,  with  a
strategically  patient  approach  in  their  compromise.  These  observations  correlate  with  the
industry  term  of  advanced  persistent  threat  (APT)  where  the  threat  actor  breaches  an
environment and may not actively cause detrimental (and overtly observable) symptoms until it
is necessary for their interest or mission.

Some threat groups in this category was observed to have exploited vulnerabilities in a variety
of  network  devices,  ranging  from  widely  used  Ubiquiti  routers,  Cisco  and  Fortinet  network
devices,  and  VPN  solutions  with  the  intent  to  stage  their  capabilities.  Many  of  these  devices
typically provide trusted access between networks or are part of the unmanaged and “outside
of  perimeter”  infrastructure.  Such  efforts  can  then  enable  disruption  of  services  and/or
espionage.  We  note  that  these  threat  groups  leverage  the  challenges  organisations  face  in
managing  a  complete  inventory  of  assets  and  the  growing  vulnerability  patching  debt  to
maintain persistent access, aside from cyber hygiene issues.

Increasingly,  we  observed  higher  sophistication  attacks  targeting  hypervisors  and  container
infrastructure,  which  typically  have  no  security  defence  solutions,  to  provide  persistence,
stealth and deeper access into technology environments.

ADVERSARY  ECOSYSTEM is now observed to have matured to an underground economy
which
is  rich  with  subcontracting  work,  mutually  reinforced  evolution  and  capability
enhancements  due  to  competition  and  collaboration,  which  lead  to  material  growth  in  reach
and  sophistication.  The  ecosystem,  coupled  with  the  already  thriving  use  of  AI  (including
agentic  AI)  and  automation  can  make  the  adversaries  more  effective  in  their  exploits  of  their
targets and victims. The following illustrates our view of the interactions between threat actors
in the underground.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

![Image description: A diagram illustrating the observed interaction map of threat groups, including state-sponsored actors, hacktivists, organized crime groups, IABs, and RaaS operators, and their motivations.]

INDUSTRIAL  CONTROL  SYSTEMS  (ICS)  attacks  continue  to
evolve and deepen their impact into organisations which use or rely on
operational  technologies  (OT).  Other  than  the  specialised  targeting  of
unique  OT  such  as  field  controllers,  programmable  logic  controllers
(PLCs),  sensors  and  actuators,  specialised  threat  groups  are  also
targeting the IT equipment, such as networking devices, and operating
systems, which are connected to the OT to gain access to the industrial
operations – which can result in cyber-physical impact.

Often  state-sponsored  threat  groups  pre-position  their  capabilities  in
OT  environments  to  enable  the  opportunity  to  disrupt  operations  or
destroy  equipment,  especially  for  organisations  who  are  critical
information infrastructure operators, e.g., utilities and transportation.

We are also seeing the rapid prototyping of exploit tools and platforms
targeting  unique  OT  used  in  the  ICS  environments.  Notably,  there  are
observed exploit tools targeting commonplace industry solutions from
Siemens,  Unitronics,  Rockwell,  Honeywell,  amongst  others.  While
many of these exploits may not have the same sophistication as those
targeting IT environments, their rise in evolution and pervasiveness may
be  attributed  to  (i)  the  rising  industrialisation  of  the  exploit  making
industry,  and  (ii)  the  use  of  AI  to  prototype  and  develop  these  exploit
solutions.  Combined  by  the  fact  that  technology  refresh  and  patching
generally takes a longer duration of time compared to IT (e.g., 10 years
or  longer),  the  vulnerabilities  will  also  persist  for  the  same  (long)
duration, exposing organisations to cyber-attacks.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

INCIDENT-RESPONSE DWELL  time has significantly changed across the territories
increased  technology  sprawl,  variety  of
based  on  our  observations.  Given  the
technologies deployed (open source, Western and Eastern technology stacks), and rising
sophistication  of  cyber-attacks,  the  dwell  times  have  all  increased  compared  to  2023
statistics in our 2024 report.

![Image description: A table showing average, minimum, and maximum dwell times in days for different industry groups.]

The  maximum  dwell  observed  has  risen  from  49  to  201  days.  The  minimum  dwell
observed has risen from 3 to 7 days.  The average dwell has also risen:- Retail from 5 to
28 days, and the Others from 33 to 70 days.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

TOP TARGETED INDUSTRIES has also seen some reshuffling given the changing times.

![Image description: A table showing top targeted industries sorted alphabetically for different territories.]

The most common targeted industry groups were Technology, Media and Telecommunications (TMT), Banking, Finance and Insurance
(BFI), and Public Sector.

Both  TMT  and  BFI  industry  groups  saw  targeting  across  the  territories.  BFI  targeting  is  a  common  stay  with  the  processing  of  financial
transactions being attractive to threat groups for financial gain and to cause social unrest. TMT targeting is largely fuelled by the continued
adoption of Cloud services, also fuelled by AI solutions adoption.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

TOP  OBSERVED  EFFECTS  of cyber  incidents  in  the  territories saw  Data  Breach,  Denial  of  Service,
and Ransom dominate the rankings.

![Image description: A table showing the top observed effects of cyber incidents in different territories.]

Throughout this report, Ensign has provided key MITRE ATT&CK techniques for each relevant context for
readers to use for follow-on defensive actions such as Red Teaming, threat hunting, and to tune the
detection and mitigation measures.

Full versions of the techniques heatmaps can be found in Appendix A with links to download MITRE
ATT&CK Navigator JSON files for further review. Full versions of the vulnerabilities observed in the territories
can be found in Appendix B. Appendix C has the ICS oriented techniques heatmap with links to JSON files.

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

OBSERVED ACTIVE RANSOMWARE THREAT GROUPS ANALYSES (1/2)

![Image description: A table summarizing observed key characteristics and languages used by various ransomware threat groups.]

While it is generally observed that all the active Ransomware threat
groups in the territories operate a Data Leak Site (DLS) and practice
multi-extortion,  the  newer  capabilities  to  evade  anti-malware
solutions  and  escape  detections  vary  across  the  variants.  It  is
noteworthy that the newer Ransomware threat groups generally are
observed  to  have  forked  or  refactored  a  combination  of  LockBit,
Conti, and other leaked Ransomware source codes.

The  ability  for  EDR/XDR  Stealth  generally  stems  from  the
Ransomware (i) targeting the hypervisor, (ii) using containers and/or
virtual machine images, or (iii) leveraging hard to fingerprint binaries
created from RUST programming language.

We  also  observe  that  the  prevalence  in  sharing  or  acquiring
compromised drivers and modules with “EDR killing” capabilities to
be embedded as payload in the Ransomware through BYOVD. This
allows  for  the  Ransomware  to  kill  processes  relating  to  identified
anti-malware  solutions,  thereby  impairing  the  victim  endpoint’s
defences.

The use of Golang enhances the Ransomware with write-once, use
on many platforms capabilities. The conventional C/C++ languages
the  Ransomware,
enable  high  performance  and  speed
particularly
(ii)  exfiltration
purposes.

(i)  encryption/decryption,  and

for

for

Legend: Ma – Material  Im – Impending  Po – Potential  In – Insubstantial  BYOVD – Bring Your Own Vulnerable Driver

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

OBSERVED ACTIVE RANSOMWARE THREAT GROUPS ANALYSES (2/2)

These  developments  mean  that  organisations  need  to  redouble  efforts  in
bolstering their cyber defences. These include:

1. Performing  inventory  of  endpoints  (on  premise,  containerised,  virtualised,
or in the Cloud) and ensuring that security monitoring is as comprehensive
as possible across both the perimeter and the internal environment

2. Ensuring  that  anti-malware  solutions,  particularly  endpoint  detection  and
response  (EDR)  and  extended  detection  and  response  (XDR)  solutions,  are
competent  and  updated.  Organisations  can  review  MITRE  ATT&CK
Evaluations for reference on their capabilities.

3. Perform regular threat hunting informed by threat intelligence. Leveraging
threat  intelligence  advisories,  particularly  focussed  on  known  threat  actor
behaviours (or tactics, techniques and procedures) to uncover compromised
environments which may not have demonstrated symptoms.

4. Reviewing  backup  and  archival  processes,  ensuring  that  there

is
adherence  to  the  3-2-1-1  backup  and  archival  strategy  and  that  the
organisation is prepared  with  golden  images  for  critical  system rebuild in
the face of Ransomware.

▪ 3-2-1-1  generally  refers  to  having  3  copies  of  data,  stored  on  2
different types of media, keeping 1 copy offsite, and keeping 1 offline
copy.  Permutations  of  the  strategy  include  having  a  copy  online  for
fast  recovery,  and  having  one  kept  offsite  and  offline.  Having  the
offline  copy set  to  immutable  generally  enhances  the  opportunity  for
recovery.

▪ Preparing for system rebuild through golden images generally bolsters
the  organisation’s  confidence  in  having  a  fallback  option  to  recover
from the Ransomware-induced business disruptions.

It

requires

5. OPTION to consider planning for non-production “Third
Recovery  Site”.  This  option  should  be  considered  by
organisations  needing  high  resilience  outcomes  for
business.
the  minimal  planning  and
preparation for rebuilding critical systems and services to
enable  critical  business  operations  to  continue.  This
“Third Recovery Site” can be considered a cold site, with
no  connectivity  to  production  systems,  but  with  the
necessary  assets  to  allow  rapid  setup  to  operational
status.  Such  planning  and  preparation  will  often  rely  on
Cloud  services  to  leverage  on  demand  scaling  up  of
resources,  and  the  organisation  having  prepared  to
leverage  containerised  service  architectures  and  virtual
machines.

response  and  disaster

6. Drill and exercise processes and procedures relating to
recovery,
Ransomware
integrating  it  with  the  organisation’s  wider  business
continuity
crisis
communications  processes,  and  legal  and  regulatory
engagement processes.

management

practices,

ENSIGN INFOSECURITY | CYBER THREAT LANDSCAPE 2025

OBSERVED OPERATIONAL TECHNOLOGY (OT) THREATS ANALYSES (1/2)

There are two groups of threat actors typically targeting OT operators:

1. Organised Crime Groups, especially RaaS, who opportunistically exploit (i) the legacy technologies’

vulnerabilities, (ii) lower cyber hygiene, (iii) connected and exposed remote services.

2. State-sponsored  threat  groups
