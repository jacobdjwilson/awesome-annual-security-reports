2022

INTRUSION
DETECTION
& PREVENTION
REPORT

EXECUTIVE SUMMARY

Intrusion Detection & Prevention Systems (IDS/IPS) have long provided a critical last line
of defense against sophisticated cybersecurity attacks that have penetrated endpoint and
perimeter defenses. They also offer an important frontline defense in emerging networks that
do not really have fixed perimeters, and which often connect new kinds of devices that cannot
support conventional embedded endpoint security software.

However, conventional IDS/IPS have some weaknesses in usability (like generating high volumes
of false positive alerts) and in effectiveness (such as a blindness to many protocols and to
certain types of advanced threats – especially those using encryption to evade detection).
The latter is especially worrying as the use of encryption expands and standards become
more rigorous, making it impossible to use common current methods of analyzing traffic
without resorting to decryption.

To better understand these concerns, how IDS/IPS is currently being used, and what the
future might hold for this important technology, we conducted a comprehensive survey of
Cybersecurity Insiders 500,000-member information security community.

For a panel discussion about options and strategies for addressing the needs and concerns
raised in this survey, we invite you to watch our webinar 2022 State of IDS/IPS: Adapt or Die.

Many thanks to Enea Qosmos for supporting this important research project, and we hope
you find the information shared by respondents useful in strengthening your own
cybersecurity posture.

Thanks

Holger Schulze

Holger Schulze
CEO and Founder
Cybersecurity Insiders

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

2

2022 INTRUSION DETECTION & PREVENTION REPORT

KEY FINDINGS

IDS/IPS adoption is widely deployed

IDS/IPS remains one of the most widely deployed cybersecurity technologies. 80% of
respondents report having deployed one or more IDS/IPS systems. In addition, while
39%  of  respondents  use  standalone  systems,  IDS/IPS  functionality  is  increasingly
being integrated into solutions like Network Detection and Response (NDR) (21%),
Extended Detection and Response (XDR) (29%), and Cloud Firewalls (CFW) (26%).
This  indicates  that  network-based  threat  detection  remains  an  essential  tool  for
combatting advanced threats.

IDS/IPS cloud deployments increase
IDS/IPS  is  still  widely  deployed  on-premise  (65%),  but  significantly,  a  nearly  equal
number  (64%)  now  report  deploying  IDS/IPS  in  the  cloud,  including  both  private
(35%)  and  public  (29%)  clouds.  The  category  of  protocols  for  which  respondents
would most like to see improved coverage is business Software as a Service (SaaS)
applications. This indicates organizations are assuming much more responsibility for
cloud security.

IDS/IPS capabilities are improving
The survey indicates significant improvement has been made in Anomaly Detection
(AD) capabilities in IDS/IPS, with respondents citing anomaly detection as their 2nd
most relied upon IDS/IPS function (71%). However, the demand for more accurate
and  actionable  IDS/IPS  alerts  persists,  with  respondents  specifically  calling  out  a
need for more definitive attack declarations (45%) and automatic alert triage (42%).

Future prognosis is uncertain
While  IDS/IPS  use  seems  rock  solid  year  after  year,  responses  indicate  that  many
legacy  IDS/IPS  are  ill-equipped  to  meet  the  future  challenge  of  fully  encrypted
environments. Nearly half of all respondents also say they are unsure whether open
source IDS/IPS software like Suricata and Snort will still be playing an important role
in threat detection in the future. This could reflect concerns over specific issues like
encryption, or that techniques like Machine Learning/Artificial Intelligence (ML/AI)
will  replace  rather  than  complement  IDS/IPS.  It  could  also  simply  reflect  the  fact
that a large percentage of respondents are unaware that their commercial IDS/IPS
solution embeds open source components. This obfuscation is likely to increase as
IDS/IPS is embedded in umbrella solutions like XDR and Cloud Firewalls.

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

3

2022 INTRUSION DETECTION & PREVENTION REPORTIDS/IPS TYPES

IDS/IPS  remains  one  of  the  most  widely  deployed  cybersecurity  technologies.  At  least  80%  of
respondents report their organization has deployed one or more IDS/IPS platforms. Most respondents
use  commercial  IDS/IPS  (61%),  though  only  19%  know  for  sure  whether  their  commercial  IDS/IPS
embeds open source (in fact, most do). Twenty percent of respondents use open source to develop
custom versions.

What type of IDS/IPS do you use?

61%

of cybersecurity
professionals
use commercial
solutions

Commercial IDS/IPS, but uncertain if it

embeds open source components 42%

Commercial IDS/IPS solution
based on open source

(e.g., Corelight, Stamus) 19%

Custom IDS/IPS built
with open source tools

(e.g., Suricata, Snort) 20%

No IDS/IPS deployed

 at this time 12%

Not sure if IDS/IPS

deployed or not 7%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

4

2022 INTRUSION DETECTION & PREVENTION REPORTIDS/IPS DEPLOYMENT

IDS/IPS  deployments  are  evolving  in  step  with  changes  in  network  environments,  particularly  the
migration of IT assets and systems to the cloud. While IDS/IPS is still widely deployed on-premise (65%),
a nearly equal number (64%) now use IDS/IPS in the cloud, including 29% in public and 35% in private
clouds.  This  indicates  organizations  are  becoming  more  proactive  about  assuming  responsibility  for
cloud security.

Where have you deployed (or plan to deploy) IDS/IPS?  (Select all that apply)

65%

On-premises

35%
Private
cloud

29%
Public
cloud

10%
No plans
to deploy

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

5

2022 INTRUSION DETECTION & PREVENTION REPORTSTANDALONE VS.
INTEGRATED SOLUTIONS

While 39% of respondents still use IDS/IPS in standalone form, they are increasingly being integrated
into more comprehensive threat management solutions. The most popular integration is with Extended
Detection  &  Response  (XDR)  solutions  (29%),  which  combine  network-  and  endpoint-based  threat
detection and response to combat advanced attacks. IDS/IPS is also increasingly used to enhance the
capabilities  of  Cloud  Firewall  (CFW),  specifically  the  use  of  integrated  DPI  and  IDS/IPS  to  transform
simple cloud firewalls into Next Generation Firewalls (NGFW).

If you use IDS/IPS, is it standalone or integrated? (Select all that apply)

26%

Integrated into
a Cloud FW

29%

Integrated
into an XDR
solution

21%

Integrated into
an NDR solution

39%

Standalone

Other 14%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

6

2022 INTRUSION DETECTION & PREVENTION REPORTPOPULAR IDS/IPS FUNCTIONS

Three quarters of respondents report the most-used IDS/IPS functions are threat blocking (74%) and
anomaly detection (71%). The prominent second place showing for anomaly detection (AD) indicates
that this functionality within IDS/IPS is rapidly maturing; in last year’s survey on Network Detection &
Response  (NDR),  respondents  cited  anomaly  detection  (74%)  as  the  primary  advantage  of  NDR  over
standalone IDS/IPS, which was considered weak on AD.

What type of functions do you use IDS/IPS for? (Select all that apply)

74%

Threat blocking

71%

Anomaly detection

39%

25%

22%

Threat hunting

Forensics

Ofﬂine packet
capture (pcap)
processing

Other 7%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

7

2022 INTRUSION DETECTION & PREVENTION REPORTALERT ANALYSIS

Nearly half of cybersecurity professionals (47%) view and analyze IDS/IPS alerts within umbrella Security
Information  &  Event  Management  (SIEM)  or  Security  Orchestration,  Automation  &  Response  (SOAR)
platforms. A nearly equal number use more focused XDR or NDR (45%) for alert analysis and management.
Despite the broad use of these standard platforms, 31% of cybersecurity professionals still develop their
own  visualization  solutions,  which  might  be  a  strategy  for  addressing  some  of  the  reported  usability
issues with standard IDS/IPS alerting.

How do you visualize and analyze IDS/IPS alerts? (Select all that apply)

Use the tools
available in the
 NDR or XDR system

Send alerts to
commercial or proprietary
SIEM/SOAR

Visualize/analyze
alerts with custom
ELK stack

Other 11%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

8

2022 INTRUSION DETECTION & PREVENTION REPORT47%45%31%BIGGEST CHALLENGES

For 45% of cybersecurity professionals, inaccurate, ‘noisy’ alerts are the biggest headache with IDS/IPS
solutions. This could help explain why people continue to develop their own analysis and visualization
tools  for  IDS/IPS  alerts  even  when  using  commercial  systems.  The  other  four  primary  concerns  carry
nearly equal weight. All challenges noted, except performance challenges, are associated with network
traffic visibility issues which can be improved with strategies like DPI integration.

What are your greatest challenges with your IDS/IPS? (Select all that apply)

34%

35%

36%

45%

29%

Limited protocol
and application
coverage

Loss of
functionality for
encrypted ﬂows

Limited
visibility into
cloud workloads

Performance
(latency,
throughput, etc.)

More accurate &
actionable alerts
(less noise)

Other 10%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

9

2022 INTRUSION DETECTION & PREVENTION REPORTENCRYPTED TRAFFIC CHALLENGE

Many  IDS/IPS  solutions  are  not  prepared  for  the  challenge  of  fully  encrypted  environments.  Our
survey reveals that the most widely used strategy (38%) for detecting threats in encrypted flows is to
analyze the minimal data that remains clear in legacy encryption standards only. At least a quarter
however are adopting encrypted traffic classification (ETC) technology (26%), while an almost equal
number use proxy servers to decrypt and inspect traffic (25%). Using a threat intelligence database
is another popular workaround (28%), though this is often integrated into ETC solutions.

How does your IDS/IPS handle threat detection with encrypted flows?  (Select all that apply)

Analyze whatever information remains unencrypted in an
encrypted ﬂow (e.g., handshake data in non-TLS 1.3 environment)

Enrich with threat intelligence database

Extend IDS/IPS with an Encrypted Trafﬁc Classiﬁcation
(ETC) component (e.g., ETC-enabled DPI engine)

Use MITM/Proxy to decrypt trafﬁc, then inspect

38%

28%

26%

25%

Not sure/other 25%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

10

2022 INTRUSION DETECTION & PREVENTION REPORTNEEDED IMPROVEMENTS

Strengthening  anomaly  detection  tops  the  list  of  improvements  cybersecurity  professionals  would
most  like  to  see  in  IDS/IPS  technology  (51%).  The  next  two  desired  enhancements,  more  definitive
attack  declarations  (45%)  and  automatic  alert  triage  (42%),  underscore  respondent  complaints  about
noisy alerting. The desire for expanded protocol coverage and preservation of visibility in encrypted
environments points to the need to integrate IDS/IPS with advanced DPI.

What would you most like to improve about your IDS/IPS? (Select all that apply)

Improve detection of anomalous and
evasive trafﬁc

51%

45%

More deﬁnitive attack declarations
as opposed to simple alerts

42%

Automatic alert triage

32%

Expand protocol and
application coverage

Safeguard visibility in
encrypted environments

28%

Improve scaling and
management for the cloud

Other 6%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

11

2022 INTRUSION DETECTION & PREVENTION REPORT29%APPLICATION COVERAGE

Cybersecurity  professionals’  desires  related  to  improvements  in  IDS/IPS  protocol  coverage  reflect
the  growing  reliance  on  cloud  services  in  the  modern  enterprise.  When  asked  in  which  application
categories they would most like to see improved coverage, the number one response was business
SaaS apps (64%). Communications applications, which are cloud-based today, come in at third place
(40%), behind expanding coverage to proprietary or legacy applications (42%), which in the case of new
custom applications are almost all developed on cloud infrastructure. Nearly one third would also like
their IDS/IPS to do a better job with Internet of Things (IoT) and Operational Technology (OT) coverage
(30%), reflecting the interrelated trends of cloudification and IT/OT convergence.

If you could expand IDS/IPS protocol and application coverage, which application categories
would you choose?  (Select all that apply)

42%

Proprietary or
legacy applications

40%

Communication
(e.g., WhatsApp, Zoom)

64%

Business SaaS
applications
(Salesforce,
Ofﬁce 365, etc.)

Other 6%

30%

IoT and
ICS/Scada

21%

Social media
& gaming
(WOW, Facebook,
Twitter)

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

12

2022 INTRUSION DETECTION & PREVENTION REPORTFUTURE IMPACT OF
OPEN-SOURCE SOFTWARE

Despite a broad general reliance on IDS/IPS today, only half of respondents are fully confident that
open source IDS/IPS will still be playing an important role in threat detection five years from now. Forty
percent are unsure, while 10% think it will not. There are multiple possible explanations for this relatively
weak  level  of  confidence.  One  possibility  is  the  low-level  awareness  of  how  widespread  the  use  of
open  source  software  is  in  commercial  IDS/IPS.  Another  is  perhaps  a  belief  that  specific  challenges
like  encryption  will  limit  the  effectiveness  of  all  IDS/IPS,  or  that  emerging  techniques  like  machine
learning-based threat detection will replace (rather than enhance) IDS/IPS. Or, it may simply reflect an
assumption that standalone IDS/IPS (including open source systems like Suricata and Snort) will cease
to exist outside encompassing systems like next generation Cloud FWs, XDR and SIEM/SOAR.

Do you think open source software like Suricata and Snort will still be playing an important role
in threat detection five years from now?

No
10%

Not sure
40%

Yes

50%

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

13

2022 INTRUSION DETECTION & PREVENTION REPORTMETHODOLOGY & DEMOGRAPHICS

This  report  is  based  on  the  results  of  a  comprehensive  online  survey  of  388  cybersecurity
professionals, to gain more insight into the latest trends, key challenges, and solutions for IDS/
IPS. The respondents range from technical executives to managers and IT security practitioners,
representing a balanced cross-section of organizations of varying sizes across multiple industries.

PR I MARY   RO LE

35%

13%

9%

8%

6% 6%

6%

17%

IT Manager, Director or CIO             CSO, CISO, or VP of Security          Security Analyst            Security Manager or Director            Auditor
Security Administrator             Systems Administrator               Other

D EPARTM ENT

43%

30%

6% 5% 2% 2% 12%

IT Security          IT Operations            Security Operations Center (SOC)           Engineering              Product Management
Sales/Marketing             Other

CO M PAN Y   S IZE

28%

19%

15%

15%

5%

18%

Less than 100          100-499            500-999           1,000-4,999            5,000-9,999           +10,000

I N D U STRY

24%

20%

9%

8%

7%

6% 5%

21%

Technology            Financial Services, Banking or Insurance           Energy or Utilities           Manufacturing            Government             Healthcare
Retail or Ecommerce               Other

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved

14

2022 INTRUSION DETECTION & PREVENTION REPORTAbout Enea

Enea is a world-leading specialist in software for telecom and cybersecurity. The

company’s cloud-native solutions connect, optimize, and secure services for mobile

subscribers, enterprises, and the Internet of Things. More than 100 communication

service providers and 4.5 billion people rely on Enea technologies every day.

Enea’s  embedded  DPI-based  traffic  intelligence  software  classifies  traffic  in  real-

time  and  provides  granular  information  about  network  activities.  Enea’s  Qosmos

technology is trusted by 75% of cybersecurity and networking vendors who embed

commercial DPI technology in their solutions. Typical uses cases include SD-WAN,

SASE, SSE, ZTNA, NGFW, SWG, XDR.

enea.com/qosmos

Cybersecurity  Insiders  is  a  500,000+  member  online  community  for

information  security  professionals,  bringing  together  the  best  minds

dedicated  to  advancing  cybersecurity  and  protecting  organizations  across

all industries, company sizes, and security roles.

We provide cybersecurity marketers with unique marketing opportunities to

reach  this  qualified  audience  and  deliver  fact-based,  third-party  validation

thought  leadership  content,  demand-generation  programs,  and  brand

visibility in the cybersecurity market.

For more information please visit www.cybersecurity-insiders.com

GET THE MEDIA KIT
or contact us for more details at:
info@cybersecurity-insiders.com

Copyright © 2022 Cybersecurity Insiders. All Rights Reserved.

Report contents can be quoted by third parties with a source reference that the report was produced

by Cybersecurity Insiders, and adding a link to  www.cybersecurity-insiders.com.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-01", "model": "unknown"} -->
