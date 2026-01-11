2024
2024

Trustwave
Risk Radar Report

Financial
Services Sector

2024 Trustwave Risk Radar Report: Financial Services Sector

Contents

Financial Services’ Unique Threat Landscape  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . . 6

Notable & Prominent Trends in Financial Services  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10

Growing Risk of Insider Threats    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 11

Phishing-as-a-Service Goes Mainstream   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14

Ransomware Groups Continue to Target Financial Services   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16

Evolution of Emerging Technology: Cryptocurrency and Deepfakes    .  .  .  .  .  .  .  .  . 20

Threat Actor Techniques by Attack Stage  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . . 24

Conclusion & Key Takeaways   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . . 28

3

In 2023, Trustwave released its Financial Services
Threat  Intelligence  Briefing  that  analyzed  the
attack flow specific to the financial services sector,
offering insight on specific threat actors, actionable
intelligence,  and  recommended  mitigations  for
each stage .

In  our  2024  report,  the  Trustwave  SpiderLabs  team  highlights  the
unique  factors  at  play  in  financial  services,  the  significant  trends
currently  affecting  the  industry,  and  an  overview  of  the  threat  actor
techniques by attack stage. Additionally, Trustwave SpiderLabs created
two complementary deep-dive writeups containing extensive research
and analysis on two looming threats: phishing-as-a-service and insider
threats.

Recent research by the Ponemon Institute identifies malicious insiders
as the costliest type of data breach, with phishing as the second most
expensive and the most prevalent. Our in-depth analysis explores why
these threats are particularly pervasive in the financial services sector.

2024 Trustwave Risk Radar Report: Financial Services Sector

$5.2

$5.0

$4.8

$4.6

$4.4

$4.2

$4.0

$3.8

Malicious insider, 4.99

Business email
compromise, 4.88

Phishing, 4.88

Social engineering, 4.77

Known unpatched
vulnerablity, 4.33

Unknown zero-day
vulnerablilty, 4.46

Stolen or compromised
credentials, 4.81

Accidental data loss and lost or stolen device, 4.28

Physical security compromise, 4.19

System error, 4.07

Clouds misconfiguration, 3.98

4%

6%

8%

10%

12%

14%

16%

18%

![Image description: A bar chart showing the cost and frequency of data breaches by initial attack vector. The cost is measured in USD millions and the frequency is represented as a percentage of all breaches. The highest cost is associated with malicious insiders at $4.99 million, followed by business email compromise and phishing at $4.88 million. The most frequent attack vector is phishing at 18%.](Image description: A bar chart showing the cost and frequency of data breaches by initial attack vector. The cost is measured in USD millions and the frequency is represented as a percentage of all breaches. The highest cost is associated with malicious insiders at $4.99 million, followed by business email compromise and phishing at $4.88 million. The most frequent attack vector is phishing at 18%.)

Financial services organizations are a goldmine for cybercriminals. With
their  abundance  of  sensitive  financial  data  and  large  sums  of  money,
these  institutions  are  highly  attractive  to  attackers.  Cyberattacks
on  this  sector  have  surged,  as  threat  actors  exploit  vulnerabilities  to
extort,  steal,  and  defraud  financial  institutions  and  their  customers.
The  potential  for  substantial  financial  gain  drives  a  relentless  pursuit
of these lucrative targets. According to Ponemon research, the cost of
a breach in the financial services sector is $6.08 million, making it the
second most expensive sector, just behind healthcare.

Key Report Findings for the
Financial Services Sector

24%

of ransomware
attacks were
ALPHV

49%

of attacks
originated from
phishing

20%

of ransomware
attacks were
against banking
institutions

65%

of ransomware
attacks were in
the US

37%

of phishing emails
contain HTML
attachments

73%

of credentials
access techniques
were brute-force
attempts

5

Financial Services’
Unique Threat Landscape

2024 Trustwave Risk Radar Report: Financial Services Sector

Expanded Regulatory Requirements

Cryptocurrency Evolution

 ▪ The  European  Union’s  Digital  Operational  Resilience  Act
(DORA)  represents  a  significant  shift  in  how  financial
institutions are expected to manage and respond to cyber
threats. This regulation mandates that organizations must
not  only  implement  robust  cybersecurity  measures  but
also continuously test their resilience to cyber incidents.

 ▪ DORA,  along  with  other  regulations  like  the  GDPR  and
institutions  to  maintain
PCI-DSS,  requires  financial
comprehensive  cybersecurity
frameworks,  conduct
regular  audits,  and  demonstrate  their  preparedness  for
potential cyberattacks. Compliance with these regulations
ensures that financial institutions maintain high standards
of security and operational resilience, directly influencing
their cybersecurity strategies.

 ▪ The  regulatory

landscape  extends  beyond  Europe.
Jurisdictions  like  the  United  States  and  Australia  have
also introduced stringent cybersecurity requirements for
financial  institutions.  In  the  US,  regulations  such  as  the
Gramm-Leach-Bliley  Act  (GLBA)  and  the  Cybersecurity
Framework (CSF) impose specific obligations on financial
firms.  Similarly,  Australia’s  Privacy  Act  and  the  Security
of  Critical  Infrastructure  Act  (SOCI)  mandate  robust
cybersecurity practices.

 ▪ Complying  with  multiple  overlapping  regulations,  often
with  varying  requirements  and  enforcement  mechanisms,
is extraordinarily intricate in nature.

 ▪ As  cryptocurrencies  gain

legitimacy  and

integration
into  traditional  banking  systems  increases,  the  financial
services industry faces new cybersecurity challenges. The
rise of digital wallets and crypto transactions introduces
potential  targets  for  cybercriminals,  such  as  infostealers
that focus on capturing private keys and wallet credentials.

 ▪ Financial  institutions  must  adapt  by  developing  robust
protection mechanisms for digital assets and ensuring the
security of their customers’ cryptocurrency holdings. This
includes  implementing  advanced  security  protocols  for
wallet protection, monitoring for suspicious activities, and
educating  consumers  about  best  practices  in  managing
their digital assets.

![Image description: A newspaper clipping with the headline "Jersey Financial Regulator Leaks Private Documents in Second Data Breach of 2024". The date is July 2024 and the source is Financial Times.](Image description: A newspaper clipping with the headline "Jersey Financial Regulator Leaks Private Documents in Second Data Breach of 2024". The date is July 2024 and the source is Financial Times.)

7

Consumer Protection Considerations

Heightened Risk Aversion

 ▪ The  financial  services  industry  is  a  prime  target  for
various forms of cyber threats aimed at stealing sensitive
consumer  information.  Banking  trojans,  for  instance,
can  capture  login  credentials  and  facilitate  unauthorized
transfers  of  funds.  Phishing  attacks  continue  to  evolve,
targeting individuals with sophisticated schemes designed
to extract personal and financial information. Additionally,
Magecart attacks, which involve injecting malicious code
into e-commerce sites to capture credit card data, pose a
significant risk.

 ▪ Financial  institutions  must  implement  advanced  threat
detection and response systems, educate their customers
on  recognizing  and  avoiding  scams,  and  ensure  robust
mechanisms are in place to protect consumer data.

 ▪ Financial  institutions  operate  under  a  high  level  of
risk  aversion  due  to  the  potential  impact  of  security
breaches  on  their  operations,  reputation,  and  regulatory
compliance.  This  heightened  risk  sensitivity  drives  a
proactive  approach  to  cybersecurity,  with  organizations
investing in advanced technologies and dedicated teams
to preemptively address vulnerabilities.

 ▪ The  financial  sector’s  emphasis  on  minimizing  risks
results  in  stringent  security  protocols,  frequent  updates
to  security  measures,  and  a  focus  on  incident  response
and recovery planning.

2024 Trustwave Risk Radar Report: Financial Services Sector

Franchise Model

 ▪ The  franchise  model  in  the  financial  services  industry  introduces
variability  in  cybersecurity  practices  across  different  branches
and  entities.  With  different  franchisers  and  franchisees  adopting
diverse business models, there can be significant disparities in the
consistency  and  effectiveness  of  cybersecurity  policies  and  their
implementation.

 ▪ This  fragmentation  can  lead  to  uneven  protection  levels  and
potential  vulnerabilities.  Standardizing  cybersecurity  practices
across franchises and ensuring uniform adherence to industry best
practices are crucial for maintaining a cohesive and resilient security
posture throughout the organization.

 ▪ Ensuring  compliance  with  regulatory  requirements  across  a
franchise  network  can  be  complex,  especially  when  dealing  with
different  jurisdictions  and  varying  local  regulations.  This  requires
a  coordinated  approach  to  maintain  consistent  security  and
compliance.

With  more  than  250  security  researchers  across
the  globe,  the  Trustwave  SpiderLabs  team  puts  its
resources to task in looking into what leads to these
breaches. We are uniquely positioned to do so, as we
perform over 200,000 hours of penetration tests and
uncover tens of thousands of vulnerabilities annually.
We  also  have  a  dedicated  email  security  team
analyzing  millions  of  phishing  URLs  validated  daily,
including 10k per day that are uniquely identified by
Trustwave SpiderLabs. Our diverse coverage of infosec
disciplines,  including  Advanced  Continuous  Threat
Hunting,  Digital  Forensics  and  Incident  Response,
Malware  Reversal,  and  Database  Security,  give  us
insight into identifying how these breaches occur as
well as mitigations and controls that your organization
can put in place to prevent these compromises.

industry.

This  report  examines  the  myriads  of  threats  facing
the  financial  services
In  addition  to
supplemental reports focused on insider threats and
phishing-as-a-service,  Trustwave  SpiderLabs  will
offer  recommendations  to  help  financial  institutions
mitigate risks and safeguard their customers and data.

9

Notable & Prominent Trends
in Financial Services

2024 Trustwave Risk Radar Report: Financial Services Sector

Growing Risk of Insider Threats

The Threat

We  explore  insider  threats  in-depth  in  our  accompanying
report. At a high level, here are some key points to consider:

Insider  threats  are  often  overlooked  in  an  organization’s
overall  security  posture.  While  news  outlets  frequently
highlight ransomware attacks and data breaches, they often
neglect the potential dangers posed by employees.

Unlike  external  attackers,  insiders  already  have  access  to
critical systems, making it easier for them to bypass traditional
security measures. Insider motives can vary widely, including
financial  gain,  personal  grievances,  or  coercion  by  external
threat actors.

Insider  threats  generally  fall  into  two  main  categories:
unintentional and intentional.

Unintentional Insider Threats:

 ▪ Unintentional insider threats can result from negligence or
accidents.  Negligent  threats  occur  when  employees  are
careless, such as by ignoring updates or security patches.

 ▪ Accidental  threats  arise  from  genuine  mistakes,  such  as
sending sensitive information to the wrong email address
or inadvertently opening a phishing email.

Intentional Insider Threats:

 ▪ Intentional  insider  threats  are  categorized  as  malicious
or collusive. Malicious insiders actively seek to harm the
organization, often for personal benefit or out of grievance.

 ▪ For instance, they might delete critical databases to create
operational issues if they feel wronged. Collusive insider
threats  involve  individuals  who  collaborate  with  external
threat actors or groups to compromise the organization.

11

What Trustwave Is Seeing

The  Trustwave  SpiderLabs  team  conducted  a  threat  hunt
to  identify  behaviors  indicative  of  insider  threats.  They
discovered  that  48%  of  the  risky  findings  were  related
to  T1219  Remote  Access  Software  and  T1572  Protocol
Tunneling.

Another notable threat vector observed during this campaign
was  T1052  Exfiltration  over  Physical  Medium,  specifically
the sub-technique Exfiltration over USB.

Then, the Trustwave SpiderLabs team took to the Dark Web
to  analyze  the  demand  for  malicious  insiders,  why  insiders
become malicious, and how threat actors are recruiting.

Several factors drive individuals to become malicious insiders.
Financial  gain  is  a  primary  motivator,  as  insiders  may  sell
sensitive information or facilitate breaches for profit. Personal
grievances, such as dissatisfaction with their employer, can
also lead insiders to engage in malicious activities.

![Image description: A screenshot from a dark web forum showing a threat actor offering a high salary for insider services at PayPal. The offer includes a base salary and additional payment. The user has a high reputation score, likes, and posts, indicating influence.](Image description: A screenshot from a dark web forum showing a threat actor offering a high salary for insider services at PayPal. The offer includes a base salary and additional payment. The user has a high reputation score, likes, and posts, indicating influence.)

The  above  threat  actor  offering  additional  payment  to  the
PayPal  employee  is  both  serious  and  knowledgeable,  as
evidenced by their salary offer. This individual is a respected
forum user with a high reputation score of 217, 139 likes, and
89 posts. The golden highlights on their nickname, status, and
rate suggest that they are a high-level, possibly paid account
with an escrow deposit, indicating their trustworthiness and
influence within the forum.

2024 Trustwave Risk Radar Report: Financial Services Sector

Mitigations to Reduce Risk

 ▪ Access  and  Usage  Controls:

 Reduce  RMM  (Remote
Monitoring and Management) usage to one tool, enforcing
restrictions on authorized accounts and their locations.

 ▪ Continuous Monitoring:  Implement continuous monitoring
of employee activities to detect unusual behavior or access
patterns.

 ▪ Access  Controls:

 Enforce  strict  access  controls  and
the  principle  of  least  privilege  to  limit  access  to  sensitive
information.

 ▪ Enhanced  Vetting  Processes:

 Strengthen  background

checks during the hiring process to identify potential risks.

 ▪ Anonymity  and  Reporting:   Create  anonymous  reporting
mechanisms  for  employees  to  report  suspicious  activities
without fear of retribution.

![Image description: A news headline stating "More Than 450K hit by JPMorgan Breach" dated May 2024 from SC Media.](Image description: A news headline stating "More Than 450K hit by JPMorgan Breach" dated May 2024 from SC Media.)

13

Phishing-as-a-Service Goes Mainstream

The Threat

What Trustwave Is Seeing

We cover phishing-as-a-service in-depth in our accompanying
report. At a high level, here are some key points to consider:

Phishing-as-a-Service  (PaaS)  has  emerged  as  a  major
cybersecurity threat to the financial sector. This “Cybercrime-
as-a-Service” model offers sophisticated phishing tools and
services that can be accessed through underground forums
and Telegram marketplaces.

Today,  many  phishing  emails  targeting  corporate  networks
are part of campaigns driven by PaaS platforms.

The  accompanying  report  provides  an  in-depth  analysis
of  how  PaaS  operates,  its  features,  and  various  platforms,
including a detailed case study of Tycoon PaaS.

Attackers  have
increasingly  adopted  HTML  and  PDF
attachments to transport, hide, and obfuscate phishing URLs.
These attachment types are common and often bypass email
scanning gateways.

 ▪ HTML attachments can serve as self-contained phishing
pages,  redirectors  to  phishing  sites,  or  use  HTML
smuggling techniques to deploy malware.

 ▪ PDF attachments may include links that redirect to phishing
pages  or  malware  downloads,  or  they  might  contain  QR
codes leading to malicious content.

2024 Trustwave Risk Radar Report: Financial Services Sector

Malicious Email Attachments

2
%

1
%

2
%

3
%

3%

3%

4%

16%

37%

%
9
2

![Image description: A pie chart showing the distribution of malicious email attachment types. HTML attachments are the most prevalent at 37%, followed by EXE at 29%.](Image description: A pie chart showing the distribution of malicious email attachment types. HTML attachments are the most prevalent at 37%, followed by EXE at 29%.)

Figure 3: Malicious email attachment types; June 2024

HTML

EXE

PDF

RTF

XLSX

DOCX

PDFCRYPT

VBS

XLSCRYPT

Other

Mitigations to Reduce Risk

 ▪ Advanced  Training

and  Awareness  Programs:
Continuously  update  training  to  educate  employees  on
the latest phishing tactics and prevention methods.

 ▪ Layered Email Security:  Tools like Trustwave MailMarshal
provide  layered  protection  against  email-based  threats,
capturing  all  forms  of  threats  to  protect  an  environment
and reduce the burden on security teams.

 ▪ Email Filtering and Analysis:  Use  advanced email filters
with  machine  learning  to  detect  anomalies,  analyze
headers, and assess sender reputation.

 ▪ Regular Audits and Simulations:  Perform regular security
audits  and  phishing  simulations  to  evaluate  and  improve
organizational readiness against phishing attacks.

 ▪ Collaboration  and

in
industry  collaborations  to  stay  updated  on  emerging
phishing trends and share critical security insights.

Intelligence  Sharing:

 Engage

 ▪ Hardware-based  Authentication:

 Implement  FIDO2
authentication with cryptographic keys stored on hardware
devices to prevent MFA bypass attacks and ensure secure
authentication.

15

Ransomware Groups Continue to
Target Financial Services

Threat

Ransomware  poses  a  significant  and  escalating  threat  to
financial  institutions  and  the  broader  financial  services
sector.  As  these  organizations  handle  vast  amounts  of
sensitive  data  and  financial  transactions,  they  are  prime
targets for cybercriminals seeking to disrupt operations and
extract  large  ransoms.  The  impact  of  a  ransomware  attack
on  a  financial  institution  can  be  catastrophic,  leading  to
operational paralysis, substantial financial losses, and severe
reputational  damage.  Attackers  often  deploy  sophisticated
encryption  methods  to  lock  access  to  critical  systems  and
data,  demanding  hefty  ransoms  in  cryptocurrency,  which
further complicates recovery efforts and legal responses.

The  financial  services  sector  is  particularly  vulnerable  due
to  its  interconnected  nature  and  the  reliance  on  complex
IT  infrastructures.  Institutions  such  as  banks,  investment
firms,  and  insurance  companies  manage  intricate  networks
of information systems that, if compromised, can have ripple
effects across the entire economy. The downtime caused by

individual  bank  accounts  to

ransomware  attacks  can  disrupt  not  only  daily  operations
but  also  critical  financial  transactions,  affecting  everything
from
international  market
stability.  Moreover,  the  regulatory  environment  around
financial  institutions  requires  them  to  adhere  to  stringent
data  protection  and  reporting  standards,  adding  layers  of
complexity to their response and recovery strategies.

In  addition  to  the  direct  financial  costs  and  operational
disruptions,  ransomware  attacks  on  financial  institutions
can lead to a loss of customer trust and regulatory scrutiny.
Customers  expect  high  levels  of  security  and  reliability
from  their  financial  service  providers,  and  any  breach  can
erode confidence and drive customers to seek more secure
alternatives. Regulatory bodies may impose hefty fines and
mandate enhanced security measures, further straining the
resources of affected institutions.

2024 Trustwave Risk Radar Report: Financial Services Sector

What Trustwave Is Seeing

Trustwave  SpiderLabs  analyzed  ransomware
incidents
targeting  the  financial  services  sector  and  identified  AlphV
and  LockBit  as  the  predominant  groups  operating  in  this
space.  Last  year,  AlphV  accounted  for  10%  of  attacks,  but
this year their share has increased to 24%. Similarly, LockBit’s
share was 24% last year, compared to 23% this year.

Though  threat  actors  target  companies  worldwide,  the
majority  of  reported  breaches  involve  organizations  from
the  US,  with  Brazil  and  Canada  coming  in  second  and
third,  respectively.  The  proportion  of  breaches  affecting
US  companies  has  increased  from  51%  last  year  to  65%
this year.

Top Ransomware Groups

Top Countries Impacted

AlphV

LockBit3

Ransomhub

Play

Medusa

Akira

Inc Ransomware

Qilin

Everst

Dispossessor

0%

7%

6%

5%

5%

4%

4%

5%

13%

9%

24%

23%

USA

Brazil

Canada

UK

India

Australia

Indonesia

Italy

France

6%

6%

5%

4%

4%

3%

3%

3%

El Salvador

2%

65%

10%

15%

20%

25%

0%

10%

20%

30%

40%

50%

60%

70%

![Image description: A bar chart showing the top ransomware groups targeting financial services. AlphV accounts for 24% of attacks, followed by LockBit3 at 23%.](Image description: A bar chart showing the top ransomware groups targeting financial services. AlphV accounts for 24% of attacks, followed by LockBit3 at 23%.)

Figure 4: Top ransomware groups targeting financial services

![Image description: A bar chart showing the top countries impacted by ransomware in the financial services sector. The USA is the most impacted at 65%, followed by Brazil at 10%.](Image description: A bar chart showing the top countries impacted by ransomware in the financial services sector. The USA is the most impacted at 65%, followed by Brazil at 10%.)

Figure 5: Financial services organizations affected by ransomware
by country

17

is  the  top  target  for
Perhaps  unsurprisingly,  banking
ransomware  attacks,  accounting  for  20%  of
incidents,
followed closely by the insurance sector at 18%. It’s important
to  note  that  no  subsector  is  immune  from  these  attacks.
Credit unions are targeted 8% of the time, while loan and legal
services, as well as wealth management firms, each face a 6%
attack rate. This distribution underscores the need for robust
cybersecurity measures across all financial services sectors.

Top Industry Types Impacted

Banking

Insurance

Financial Management

Accounting

Credit Union

Investment Management

Credit and Loan Services

Financial Legal Services

Wealth Management

Payment Solutions

20%

18%

13%

11%

8%

8%

6%

6%

6%

4%

5%

0%

10%

15%

20%

25%

![Image description: A bar chart showing ransomware attacks by financial services type. Banking is the top target at 20%, followed by Insurance at 18%.](Image description: A bar chart showing ransomware attacks by financial services type. Banking is the top target at 20%, followed by Insurance at 18%.)

Figure 6: Ransomware attacks by financial services type

![Image description: A news headline stating "Data Breach Affects 57,000 Bank of America Accounts" dated February 2024 from American Banker.](Image description: A news headline stating "Data Breach Affects 57,000 Bank of America Accounts" dated February 2024 from American Banker.)

2024 Trustwave Risk Radar Report: Financial Services Sector

Mitigations to Reduce Risk

 ▪ Use  Host-Based  Anti-Malware  Tools:
individual  hosts  to

 Deploy  anti-
identify  and
malware  tools  on
quarantine  specific  malware.  Be  aware  that  these  tools
have  limitations  and  may  be  circumvented  by  custom
malware packages.

 ▪ Enable  and  Audit  System  Logs:   Activate  logging  on
valuable  systems  and  workstations.  Implement  network
logging  through  flows,  Network  Monitoring  Solutions,  or
IDS devices on ingress and egress channels. These logs
are crucial for identifying potential compromises.

 ▪ Active  Monitoring  of  Logs:   Regularly  monitor  logs  to
detect  abnormal  behavior  or  traffic.  Establish  a  baseline
of normal activity to make deviations more noticeable, as
merely enabling logs without active monitoring diminishes
their effectiveness.

 ▪ Establish a Formal Incident Response Process:  Develop
and routinely practice a formal incident response plan to
ensure  a  swift  and  coordinated  reaction  to  ransomware
attacks.

 ▪ Ongoing  Underground  and  Dark  Web  Monitoring:
Continuously monitor the underground and dark web for
information  leakage  that  might  have  been  overlooked.
This can provide early warnings about potential threats or
data exposure.

![Image description: A news headline stating "Prudential Financial Data Breach Impacts 2.5 Million" dated February 2024 from SecurityWeek.](Image description: A news headline stating "Prudential Financial Data Breach Impacts 2.5 Million" dated February 2024 from SecurityWeek.)

19

Evolution of Emerging Technology:
Cryptocurrency and Deepfakes

Threat

As  emerging  technologies  advance  rapidly,  they  bring  both
transformative opportunities and new challenges, particularly
in cybersecurity.

the

financial  services  sector,

For
the  evolution  of
cryptocurrencies  and  the  rise  of  deepfake  technology
represents  a  double-edged  sword.  While  these  innovations
offer enhanced efficiency and new avenues for growth, they
also introduce significant security risks that require proactive
and sophisticated responses.

Deepfake  technology,  meanwhile,  presents  an  emerging
threat in the form of highly convincing but fabricated digital
content.  These  synthetic  media  can  be  used  to  deceive
individuals  and  organizations,  undermining
trust  and
facilitating fraud.

Earlier  this  year,  a  finance  worker  at  a  multinational  firm
was  tricked  into  paying  out  $25  million  to  fraudsters  using
deepfake technology to pose as the company’s chief financial
officer in a video conference call.

Cryptocurrency, once a niche financial product, has become
a  mainstream  asset  class,  increasingly  integrated  into
traditional  financial  systems.  This  integration  opens  up
new attack vectors, including the theft of digital assets and
hacking  of  cryptocurrency  exchanges.  The  EU’s  Markets  in
Crypto-Assets Regulation (MiCA) aims to mitigate these risks
by  establishing  a  comprehensive  regulatory  framework  for
the crypto-asset market.

2024 Trustwave Risk Radar Report: Financial Services Sector

What Trustwave Is Seeing

Cryptocurrency Risks: The surge in cryptocurrency adoption
has created several new security challenges:

Deepfake Threats: The proliferation of deepfake technology
has introduced several cybersecurity concerns:

 ▪ Wallet  Theft:

 Digital  wallets,  essential

for  storing
cryptocurrencies,  are  prime  targets  for  cybercriminals.
Successful  attacks  can  result  in  the  irreversible  loss  of
funds.

 ▪ Exchange  Hacks:

 Cryptocurrency  exchanges,  where
users  trade  digital  assets,  are  increasingly  targeted  by
hackers seeking to exploit vulnerabilities and steal assets
on a large scale.

 ▪ Cryptojacking:  Malicious actors may use infected systems
to  mine  cryptocurrencies  without  the  user’s  consent,
leading to significant operational disruptions and financial
losses.

In  February  2024,  Trustwave  SpiderLabs  discovered  Ov3r_
Stealer, a malware designed to steal credentials and crypto
wallets through Facebook job advertisements.

The  observed  Ov3r_Stealer  malware  is  designed  to  collect
and exfiltrate the following data:

Data Type

Location

Crypto

Wallets

C:\Users\IEUser\AppData\Roaming\wallet.dat

C:\Users\IEUser\AppData\Roaming\Coinomi\Coinomi\wallets

C:\Users\IEUser\AppData\Roaming\bytecoin

C:\Users\IEUser\AppData\Roaming\Electrum\wallets

C:\Users\IEUser\AppData\Roaming\Exodus\exodus.wallet

C:\Users\IEUser\AppData\Roaming\com.liberty.jaxx\IndexedDB\file_0.indexeddb.leveldb

C:\Users\IEUser\AppData\Roaming\Guarda\Local Storage\leveldb

![Image description: A table listing the data types and locations that the Ov3r_Stealer malware is designed to exfiltrate. The data type is "Crypto Wallets" and the locations are various file