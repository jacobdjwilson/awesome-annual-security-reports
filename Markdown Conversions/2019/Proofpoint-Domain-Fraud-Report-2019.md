REPORT
2019
PROOFPOINT
DOMAIN
FRAUD
REPORT
proofpoint.com

2 DOMAIN FRAUD REPORT | 2019
TABLE OF CONTENTS
EXECUTIVE SUMMARY ..............................................................................................................................................3
METHODOLOGY ............................................................................................................................................................4
DOMAIN TRENDS .........................................................................................................................................................4
Registrations ..............................................................................................................................................4
Characteristics ...........................................................................................................................................5
Top-Level Domain Trends ...........................................................................................................................6
Registrars ...................................................................................................................................................7
Profile of a Fast-Growing TLD ....................................................................................................................7
Keyword Pairs ............................................................................................................................................8
FRAUDULENT DOMAINS ...........................................................................................................................................9
TLD Trends .................................................................................................................................................9
Registrars .................................................................................................................................................10
IDN Attacks ..............................................................................................................................................10
Lookalike Domains ...................................................................................................................................11
TLD Attacks ..............................................................................................................................................12
Domains Selling Counterfeit Goods ........................................................................................................13
FRAUDULENT DOMAINS AND SECURITY CERTIFICATES .............................................................................15
EMAIL TRENDS ...........................................................................................................................................................16
PARKED DOMAINS .....................................................................................................................................................17

3 DOMAIN FRAUD REPORT | 2019
EXECUTIVE SUMMARY
Domain fraud is an attractive attack method used by Most businesses are affected by fraudulent domains. Our
cyber criminals. Cheap and easy domain registrations research found that businesses across industries and geographies
are at risk from fraudulent domains. 76% of Proofpoint Digital Risk
create a low barrier to entry. Privacy features offered
Protection customers found “lookalike” domains posing as their
by most registrars and regulations like European Union
brand. In retail, domains devoted to selling counterfeit goods are
General Data Protection Regulation (GDPR) have made a compelling threat. More than 85% of top retail brands found
it easy to remain anonymous. And, most important, domains selling knockoff versions of their products. In fact, the
average retail brand had more than 200 such detections.
fraudulent domains provide the basis for a wide range of
attacks such as wire transfer fraud, phishing, counterfeit Fraudulent domains are active and positioned for an attack.
Most fraudulent domains detected are active, with more than 90%
good sales, scams and other new attacks.
associated with a live server. More than 15% have mail exchanger
Like many of today’s most pressing cyber threats, domain fraud targets (MX) records, indicating that they send and/or receive email. And 1
people rather than infrastructure. Bad actors use social engineering to in 4 have security certificates, which many internet users mistakenly
trick people into believing their domains are legitimate. And often, they equate with legitimacy and security.
are effective.
Fraudulent domains are using email for highly targeted
This Domain Fraud report outlines our latest research on domain attacks. For 94% of Digital Risk Protection customers, we found
trends, including the tactics and activity of the domains defrauding at least one fraudulent domain posing as their brand and sending
top global businesses and their customers. Here are our key findings. email. We also saw fraudulent domains sending low volumes
of email, behavior typically associated with highly targeted and
As the domain universe grows, so do fraudulent domains.
socially engineered attacks.
Quarterly domain registrations grew 44% between Q1 and Q4 2018.
Registrations of fraudulent domains also increased 11% during Market factors, such as the introduction of new TLDs, create
the same period. Threat actors register millions of new fraudulent opportunity for threat actors. In 2018, the introduction of new
domains each year, targeting customers and employees of top TLDs, such as .app and .icu, provided new opportunities for the
enterprises. Fraudulent domains use many of the same top-level registration of fraudulent domains. Our research suggests that
domains (or TLDs—common internet address suffixes such as attackers rushed to register domain names with the new TLDs.
“.com” and “.org”)—as legitimate domains do. And fraudsters are These fraudulent domains resembled “.com” domains already
registering these domains using many of the same registrars, too. owned by top brands. Google’s .app TLD, for example, was an
especially attractive target.

4   DOMAIN FRAUD REPORT | 2019
METHODOLOGY
Proofpoint’s Active Domains Database leverages multiple WHOIS data sources, Proofpoint email visibility and other proprietary Proofpoint
data sources to create the most comprehensive and accurate record of global domains daily. Unless indicated, all data represents the
period between January 1, 2018 and December 31, 2018. Additionally, the domain “created date” is not always available in WHOIS records,
which means some domains, TLDs or registrars may not be accounted for in sections related to 2018 registrations. To identify registrars,
Proofpoint researchers used IANA identification numbers, which are not always available in WHOIS responses.
DOMAIN TRENDS
Our research team uses a highly scalable detection system
to continually analyze over 350 million domains—virtually all
New Registrations Outpace Expirations
domains on the web—in the Proofpoint Active Domain Database.
This analysis helps us identify domain trends on a global and
189,032
regional scale.
REGISTRATIONS
Average number of domains registered each day in 2018
The domain universe grew substantially in 2018. New registrations
outpaced domain expirations, drops and deletes. On a month-
to-month basis, growth ebbed and flowed. These changes reflect
the dynamic nature of the domain market, continuously fluctuating  159,124
prices, the launch of new TLDs and other factors.
Average daily number of domains dropped, deleted or
allowed to expire in 2018
IN 2018
Total Active Domains Total Active IDNs Newly Registered Domains
| 360M |     | 250K |     | 25M |     |
| ---- | --- | ---- | --- | --- | --- |
|      |     |      |     |     | 44% |
11%
| 340M |     | 225K |     | 20M |     |
| ---- | --- | ---- | --- | --- | --- |
|      |     |      |     |     |     |
| 320M |     | 200K |     | 15M |     |
|      |     |      |     |     |     |
|      |     | 175K |     | 10M |     |
300M
| Q1 Q2 | Q3 Q4 | Q1 Q2 | Q3 Q4 |       |       |
| ----- | ----- | ----- | ----- | ----- | ----- |
|       |       |       |       | Q1 Q2 | Q3 Q4 |
Figure 1. The total number of domains increased  Figure 2. Internationalized domain names (IDN),  Figure 3. New domain registrations fluctuated
by 11% between Q1 and Q4. which utilize non-ASCII characters, decreased  from quarter to quarter, but increased by 44%
|     |     | between Q1 and Q3 before rising again in Q4.  |     | between Q1 and Q4.  |     |
| --- | --- | --------------------------------------------- | --- | ------------------- | --- |

5 DOMAIN FRAUD REPORT | 2019
CHARACTERISTICS But a number of these shared IP addresses are also likely controlled
by “parking groups.” These can represent a threat. (See the section
“PARKED DOMAINS” on page 17 for more on this trend.)
Because so many domains use shared IP addresses (often for
innocuous reasons), condemning or validating a domain based on
IP address alone can be impossible. One fraudulent domain using
an IP address does not necessarily mean that all other domains
using that address are fraudulent. Determining the trustworthiness
of a domain requires a broader analysis.
Domains with MX records use MX servers to send and/or receive
email. Domain owners may host such servers themselves or use
shared servers, frequently offered by hosting providers. A typical
domain uses between one and five MX servers. Figure 5 and Table 1
show the breakdown of MX servers across domains with MX
records. Note that No. 19 on the list of shared MX servers does not
point to an actual server, indicating that the domain can not receive
email. Domains using shared MX servers are more likely to use
There are more than 14 million unique IP addresses associated multiple servers than those using self-hosted MX servers.
with the observed domains. Most of these IP addresses host just
one domain or a handful of domains. But a small percentage
(less than 2%) host significantly more. In fact, more than 40% of
resolved domains (120 million) are hosted by just 406 unique IP
addresses (Figure 4).
This lopsided concentration may have several causes. Speculative
domain purchasers often leave such domains resolving to a
common default “under construction” page provided by the
registrar or web hosting provider, for instance. Businesses that
manage many domains may also use a single IP address to
conserve resources.
70% 45%
60%
35%
50%
40%
25%
30%
20%
10%
10%
0% 0%
1 2-100 101-500 501-1K 1K-10K 10K-50K 50K+
Domains per IP Address
sesserddA
PI
euqinU
fo
tnecreP
sniamoD
devloseR
fo
tnecreP
A cross all domains
66% resolve to an IP address, indicating that they
are associated with a live server
have an HTTP response, indicating that the
53%
domain is hosting web content and responds
to an HTTP request
have an MX record, meaning that the
42%
domains are configured to send and/or
receive email
have a security certificate, meaning that
6%
communications between the browser and
the web server are encrypted
Top Shared MX Servers Used by Domains
1. secureserver.net 11. 123-reg.co.uk
2. google.com 12. rzone.de
3. registrar-servers.com 13. 1and1.co.uk
4. googlemail.com 14. ctmail.com
5. outlook.com 15. mailspamprotection.com
6. kundenserver.de 16. hostedemail.com
7. ovh.net 17. gandi.net
8. b-io.co 18. qq.com
9. 1and1.com 19. localhost.
10. one.com 20. zoho.com
Table 1
Shared IP Addresses Type of MX Server Used by Domains
Self-Hosted
45%
Shared
55%
Figure 4 Figure 5

6   DOMAIN FRAUD REPORT | 2019
TOP-LEVEL DOMAIN TRENDS
As an example, note the surge of “.app” registrations in May.
There are now more than 1500 TLDs available for registration,1
For other TLDs, registrations spike in response to discounts
including more than 300 country-code TLDs (ccTLDs) and a growing
by registrars. This trend may explain the increase in “.ooo”
list of more than 1200 generic TLDs (gTLDs).2 Figure 6 and Figure 7
registrations in June and August, when flash sales brought the
show the top TLDs for new domain registrations in 2018.3
cheapest available price for that TLD from $24 to $2. Conversely,
On a monthly basis, “.com” held a consistent position as the
registrations with “.loan” dropped significantly in August, when
most popular TLD for new registrations. The rest of the TLD
the cheapest registration price climbed from under $1 to more
landscape shows pronounced fluidity from month to month.
than $10. The “.biz” TLD experienced a huge spike in registrations
Popularity also appears to be heavily influenced by factors
in May, nearly all of them through Chinese internet giant Alibaba
such as pricing and availability. When new TLDs are launched,
Group, perhaps prompted by a flash sale.4
speculators and businesses often rush to register new domains
For some TLDs, registration growth was especially rapid over the
with them.
course of 2018 (Figure 8).
Top-Level Domains Registered by Month
| RANK JAN | FEB   | MAR   | APR   | MAY   | JUN   | JUL   | AUG   | SEP   | OCT   | NOV  | DEC    |
| -------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- | ------ |
| 1 com    | com   | com   | com   | com   | com   | com   | com   | com   | com   | com  | com    |
| 2 top    | top   | loan  | loan  | biz   | loan  | top   | top   | top   | net   | net  | net    |
| 3 net    | loan  | xyz   | top   | top   | cn    | cn    | club  | cn    | top   | xyz  | site   |
| 4 org    | net   | net   | net   | cn    | top   | net   | cn    | net   | xyz   | top  | top    |
| 5 cn     | org   | org   | cn    | org   | net   | org   | net   | org   | site  | ltd  | online |
| 6 club   | ru    | cn    | org   | app   | org   | co.uk | org   | xyz   | org   | org  | org    |
| 7 info   | co.uk | ru    | co.uk | net   | club  | loan  | info  | co.uk | info  | site | xyz    |
| 8 xyz    | info  | top   | ru    | co.uk | ooo   | info  | co.uk | info  | us    | club | info   |
| 9 co.uk  | cn    | co.uk | info  | ru    | co.uk | xyz   | ooo   | work  | co.uk | ru   | icu    |
| 10 ru    | xyz   | info  | xyz   | info  | info  | ru    | xyz   | club  | ru    | info | ru     |

Figure 7
Top 10 TLDs by New Registrations Top 10 Fastest Growing TLDs by New Registrations
| com   |         |     |     |         |     | world     |     |     |     |     |     |
| ----- | ------- | --- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- |
| top   |         |     |     |         |     | services  |     |     |     |     |     |
| net   |         |     |     |         |     | asia      |     |     |     |     |     |
| loan  |         |     |     |         |     | rocks     |     |     |     |     |     |
| cn    |         |     |     |         |     | fun       |     |     |     |     |     |
| org   |         |     |     |         |     | live      |     |     |     |     |     |
| xyz   |         |     |     |         |     | tel       |     |     |     |     |     |
| co.uk |         |     |     |         |     | life      |     |     |     |     |     |
| info  |         |     |     |         |     | ltd       |     |     |     |     |     |
| ru    |         |     |     |         |     | site      |     |     |     |     |     |
| 0M 5M | 10M 15M | 20M | 25M | 30M 35M |     | 0         | 10x | 20x | 30x | 40x | 50x |
Rate of Growth
| Figure 6 |     |     |     |     |     | Figure 8 |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
1 ICAAN. “List of Top-Level Domains.” Accessed April 2019. 3 Some TLDs do not report the “created date” for their domains, so they may not be
2 ICAAN. “Program Statistics: Current Statistics.” Accessed April 2019.  represented in this analysis.
4 Historical price trends sourced from: https://tld-list.com

7   DOMAIN FRAUD REPORT | 2019
| REGISTRARS |     | PROFILE OF A FAST-GROWING TLD |     |     |     |
| ---------- | --- | ----------------------------- | --- | --- | --- |
A domain-name registrar manages the registration of domain names  For many of the fastest-growing TLDs, growth in new registrations
and must be accredited by a generic top-level-domain (gTLD)  correlated with an increase in registrars offering those TLDs. For
registry or a country-code top-level-domain (ccTLD) registry.  example, monthly registrations of “.services” increased from
A business must be accredited by the Internet Corporation for  123 to 4,911 between January and December. During the same
Assigned Names and Numbers (ICANN) before they can become  period, the number of registrars selling “.services” domains more
a domain registrar for the “.com,” “.net” and “.name” TLDs.   than doubled from 24 to 55. The cheapest price for the TLD
also fell from nearly $8 to less than $2 during this time. A similar
pattern occurs for many of the fastest-growing TLDs.
Top Registrars Across All Domain Registrations
Registrars for “.services”
1.  GoDaddy.com, LLC. . . . . . . . . . . . . . . . . . . . . . . . . 24%
| 2.  NameCheap, Inc. ........................... | 8%  |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- |
80
3.  Alibaba Cloud Computing Ltd.
| d/b/a HiChina (www.net.cn) ................... | 5%  | 60  |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- |
4.  Alibaba Cloud Computing (Beijing)
40
| Co., Ltd. ...................................    | 5%  |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- |
| 5.  Tucows Domains Inc. ........................ | 4%  |     |     |     |     |
20
| 6.  GMO Internet, Inc. d/b/a Onamae.com ..........  | 4%  |         |             |             |                 |
| --------------------------------------------------- | --- | ------- | ----------- | ----------- | --------------- |
| 7.  Chengdu West Dimension Digital                  |     | 0       |             |             |                 |
|                                                     |     | Jan Feb | Mar Apr May | Jun Jul Aug | Sep Oct Nov Dec |
| Technology Co., Ltd. .........................      | 3%  |         |             |             |                 |
| 8.  Xin Net Technology Corporation  ............... | 3%  |         |             |             |                 |
| 9.  PDR Ltd. d/b/a PublicDomainRegistry.com  ...... | 3%  |         |             |             |                 |
| 10.  Network Solutions, LLC ....................... | 2%  |         |             |             |                 |
Registrations for “.services”
| 11.  NameSilo, LLC .............................. | 2%  |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- |
12.  Alibaba.com Singapore E-Commerce
6K
| Private Limited ..............................   | 2%  |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- |
| 13.  Google LLC ................................ | 2%  |     |     |     |     |
4K
| 14.  1&1 Internet SE  ............................. | 2%  |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- |
| 15.  eNom, LLC ................................     | 2%  |     |     |     |     |
2K
| 16.  West263 International Limited  ................. | 1%  |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- |
| 17.  OVH sas ...................................      | 1%  |     |     |     |     |
0
18.  Dynadot, LLC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1%
|                                                    |     | Jan Feb | Mar Apr May | Jun Jul Aug | Sep Oct Nov Dec |
| -------------------------------------------------- | --- | ------- | ----------- | ----------- | --------------- |
| 19.  FastDomain Inc.  ............................ | 1%  |         |             |             |                 |
| 20.  Name.com, Inc. .............................  | 1%  |         |             |             |                 |
Table 2

8   DOMAIN FRAUD REPORT | 2019
KEYWORD PAIRS
Top Keyword Pairs in 2018
Domains feature a variety of words and phrases. We tracked
|     |     |     |     |     | 1.  real estate |     |     | 11.  for you |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | ------------ | --- |
the most common English-language word pairs in 2018 domain
registrations. Some pairs consistently appeared in the top  2.  for sale 12. we are
thirty rankings, including “real estate,” U.S. city names, and  3.  i am 13. las vegas
cryptocurrency-related terms.
|     |     |     |     |     | 4.  new york |     |     | 14. to do |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --------- | --- |
Even so, keyword pair trends also demonstrated the same fluidity  5.  bit coin 15. san diego
as other domain elements such as TLDs. In April, for example,
|     |     |     |     |     | 6.  how to |     |     | 16. house of |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ------------ | --- |
vacation-themed keyword pairs were registered in high quantities.
|     |     |     |     |     | 7.  i love |     |     | 17.  the best |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ------------- | --- |
Car-related keyword pairs also surged during the spring.
|     |     |     |     |     | 8.  make up |     |     | 18. the world |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | ------------- | --- |
We also observed a range of technology-related keyword pairs
|     |     |     |     |     | 9.  block chain |     |     | 19. move is |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | ----------- | --- |
throughout the year, though exact phrases varied from month
|     |     |     |     |     | 10. web design |     |     | 20. los angeles |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --------------- | --- |
to month.  These pairs often included terms such as “server,”
“security,” and “system.”
Table 3
Top Keyword Pairs by Month
| RANK JAN | FEB MAR  | APR   | MAY | JUN | JUL | AUG  | SEP | OCT NOV | DEC |
| -------- | -------- | ----- | --- | --- | --- | ---- | --- | ------- | --- |
|          | instant  | all   |     |     |     |      |     |         |     |
1 scoop to real estate zen desk real estate real estate real estate real estate real estate real estate real estate
|     | winner | inclusive  |           |       |     |        |     |         |     |
| --- | ------ | ---------- | --------- | ----- | --- | ------ | --- | ------- | --- |
|     |        | inclusive  | intercom  | for   |     | block  |     | casual  |     |
2 facts to i love info to apple id for sale bit coin for sale
|     |     | vacation | mail    | registration |     | chain     |     | meetings |     |
| --- | --- | -------- | ------- | ------------ | --- | --------- | --- | -------- | --- |
|     |     |          | secure  |              |     | security  |     |          |     |
3 info to real estate facts to real estate the queue bit coin how to go out i am i am
|     |     |     | server |            |     | check  |     |       |     |
| --- | --- | --- | ------ | ---------- | --- | ------ | --- | ----- | --- |
| 4   |     |     | femme  | available  |     | check  |     | out   |     |
wisdom to star games scoop to new car cougar for for sale version i am together a flash new york
|              |                  | inclusive  | sexe  | release  |        |      |          | block   block   |          |
| ------------ | ---------------- | ---------- | ----- | -------- | ------ | ---- | -------- | --------------- | -------- |
| 5 insight to | how to wisdom to |            |       |          | how to | i am | bit coin |                 | bit coin |
|              |                  | vacations  | femme | from     |        |      |          | chain chain     |          |
| going        | applicatio       |            |       | queue    |        |      |          |                 |          |
6 insight to new cars new car i am bit coin new york i am for sale how to
| ahead | and |     |     | available |     |     |     |     |     |
| ----- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
7 moving  i phone for sale to own car   after   resort  server not make for sale new york block
| ahead |     |     | spanish | release | living |     | up  |     | chain |
| ----- | --- | --- | ------- | ------- | ------ | --- | --- | --- | ----- |
not
8 to save my best new york rent to us courts to do for you  responding i love bit coin how to i love
|     | safe  |     |     |     |     |     |     |     | make |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | ---- |
9 to own how to how to a host for sale new york for sale for you a flash we are
|     | systems |     |        |     |     |     |     |     | up   |
| --- | ------- | --- | ------ | --- | --- | --- | --- | --- | ---- |
|     |         |     | cyber  |     |     |     |     |     | web  |
10 to have bit coin for you walk in how to make up apple id las vegas how to for you
|     |     |     | monday |     |     |     |     |     | design |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | ------ |
Figure 9

9   DOMAIN FRAUD REPORT | 2019
FRAUDULENT DOMAINS We classify domains as fraudulent using a proprietary classification
engine that analyzes domain records, website content, email activity,
reputation and other dynamic factors.
A  cross the fraudulent domains registered in 2018
Fraudulent domains resolve to IP addresses and have HTTP
responses at a much higher rate than domains overall. They are
95%
resolve to an IP address also more likely to have a security certificate.
94%
|     | have an HTTP response |     |     |     |     | TLD TRENDS |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
16%
have an MX record Figure 10 shows the top TLDs used in fraudulent domain registrations.
Research by Spamhaus recently highlighted several TLDs as “shady,”
26%
have a security certificate based on the percentage of websites with specific TLDs conducting
spam operations.5 Several of these “shady” TLDs appear in the list
of top TLDs for fraudulent domain registrations as well.
Most domains are registered by businesses and individuals for
For example, “.top” is No. 2, “.men” is No. 19, and “.work” is No. 50.
legitimate purposes. But fraudsters also register millions of domains
But threat actors are using more “innocuous” TLDs than “shady”
each year. These include fraudulent domains used to launch phishing
TLDs. This includes several European country code TLDs. In
attacks, lookalike or “typosquatting” domains that capitalize on
the wake of GDPR, some of the European country code TLDs
unintentional traffic intended for other sites, and domains used to sell
were the first to redact WHOIS information, which may have made
knockoff goods or scam customers. In addition to registering new
them attractive to fraudsters.
domains for fraudulent purposes, fraudsters often exploit existing
Because the success of fraudulent domains depends on tricking
legitimate domains. Points of transition in a legitimate domain’s
people, hiding in plain sight can prove effective. As with suspicious
life cycle, including expiration and deletion, present an opportunity
IP addresses, this ambiguity makes identifying fraudulent domains
for fraudsters to take over, often undetected. Businesses across
difficult based on one factor alone.
industries are undermined by fraudulent domains.
Top TLDs for Fraudulent Domains
11%
Between Q1 and Q4, our data indicates that
|     |     |     |     |     |     |     | 1.  .com ............38% |     |     | 6.  .РФ ..............3% |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------ | --- | --- |
registrations of fraudulent domains rose 2.  .top .............12% 7.  .xyz ..............2%
|                              |       |       |       |     |     |         | 3.  .fr ...............8% |       |       | 8.  .us ..............2%   |     |     |
| ---------------------------- | ----- | ----- | ----- | --- | --- | ------- | ------------------------- | ----- | ----- | -------------------------- | --- | --- |
|                              |       |       |       |     |     |         | 4.  .co.uk ............6% |       |       | 9.  .org ..............1%  |     |     |
|                              |       |       |       |     |     |         | 5.  .it ...............5% |       |       | 10.  .net ..............1% |     |     |
| Top TLDs Registered by Month |       |       |       |     |     | Table 4 |                           |       |       |                            |     |     |
| RANK                         | JAN   | FEB   | MAR   | APR | MAY | JUN     | JUL                       | AUG   | SEP   | OCT                        | NOV | DEC |
| 1                            | com   | com   | com   | com | com | com     | top                       | com   | com   | com                        | com | com |
| 2                            | fr    | fr    | fr    | fr  | top | top     | com                       | top   | top   | fr                         | xyz | top |
| 3                            | it    | РФ    | it    | it  | fr  | fr      | co.uk                     | co.uk | co.uk | РФ                         | fr  | fr  |
| 4                            | co.uk | co.uk | co.uk | xyz | it  | it      | fr                        | fr    | fr    | xyz                        | РФ  | РФ  |
5
|     | РФ  | it  | РФ  | top   | co.uk | co.uk | it   | it     | it     | co.uk  | site   | xyz   |
| --- | --- | --- | --- | ----- | ----- | ----- | ---- | ------ | ------ | ------ | ------ | ----- |
| 6   | org | org | org | co.uk | us    | ooo   | РФ   | xyz    | xyz    | site   | online | co.uk |
| 7   | top | us  | ca  |       | app   |       | net  | us     |        | top    | club   | club  |
|     |     |     |     | РФ    |       | РФ    |      |        | РФ     |        |        |       |
| 8   | se  | net | ru  | org   | org   | net   | ca   | РФ     | online | online | ru     | ru    |
| 9   | xyz | xyz | net | net   | men   | us    | club | online | ca     | se     | se     | net   |
| 10  | ru  | ru  | se  | pl    | РФ    | org   | us   | club   | us     | club   | net    | se    |
Figure 10
5 Spamhaus. “The World’s Most Abused TLDs.” Accessed April 2019.

10   DOMAIN FRAUD REPORT | 2019
REGISTRARS
Fraudulent domains used many of the same registrars as legitimate ones. Some registrars, however, are more popular for fraudulent domain
registrations. NameSilo, which appears as No. 2 in Table 5, accepts payment in Bitcoin and offers free WHOIS privacy for registrants. This
anonymity likely makes the registrar an attractive choice for fraudsters.
Top Registrars for Fraudulent Domains
1.  Chengdu west dimension digital ................. 14% 12.  DYNADOT, LLC ................................2%
2.  NameSilo, LLC ................................ 11% 13.  West263 International Limited .....................2%
3.  PDR Ltd. d/b/a PublicDomainRegistry.com ..........9% 14.  Netim ........................................2%
4.  GoDaddy.com, LLC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8% 15.  Alibaba Cloud Computing Ltd. d/b/a HiChina
5.  HOSTING CONCEPTS B.V.  ......................6% (www.net.cn) ..................................2%
6.  NameCheap, Inc. ..............................5% 16.  1&1 Internet SE ................................ 1%
7.  Gransy s.r.o d/b/a subreg.cz ......................5% 17.  Xin Net Technology Corporation ................... 1%
8.  Alibaba Cloud Computing (Beijing) Co., Ltd. .........4% 18.  Bizcn.com, Inc. ................................ 1%
9.  Limited Liability Company “Registrar of domain   19.  Regional Network Information Center,
names REG.RU” ...............................3% JSC dba RU-CENTER ........................... 1%
10.  Hosting Concepts B.V. d/b/a Openprovider ..........3% 20.  GMO ........................................ 1%
11.  1API GmbH ...................................2%
IDN ATTACKS
Top Registrars for IDN Attacks
F raudulent IDN domains are poised for an attack 1.  Registrar of Domain Names REG.RU, LLC ...... 21%
2.  GoDaddy.com, LLC. . . . . . . . . . . . . . . . . . . . . . . . . 13%
|     | 3.  1&1 Internet SE ............................ | 12% |
| --- | ------------------------------------------------ | --- |
|     | 4.  GMO .....................................    | 6%  |
79% resolve to an IP address
|     | 5.  Google Inc. ................................ | 4%  |
| --- | ------------------------------------------------ | --- |
6.  Regional Network Information Center,
75%
have an HTTP response JSC dba RU-CENTER ........................ 4%
7.  Alibaba Cloud Computing Ltd.
| 49% | d/b/a HiChina (www.net.cn) ................... | 3%  |
| --- | ---------------------------------------------- | --- |
have an MX record
|     | 8.  R01-RF .................................... | 2%  |
| --- | ----------------------------------------------- | --- |
|     | 9.  OVH ......................................  | 2%  |
16%
have a security certificate 10.  Gandi SAS ................................. 2%
|     | 11.  NameCheap Inc. ............................ | 2%  |
| --- | ------------------------------------------------ | --- |
12.  Regtime Ltd ................................ 2%
|     | 13.  Loopia AB ................................. | 1%  |
| --- | ------------------------------------------------ | --- |
Internationalized domain names (IDN) allow people to use domain  14.  BEGET-RF ................................. 1%
|     | 15.  TIMEWEB-RF .............................. | 1%  |
| --- | ---------------------------------------------- | --- |
names in local, non-Latin languages and scripts. They are also are a
|     | 16.  Internet Domain Service BS Corp ............... | 1%  |
| --- | ---------------------------------------------------- | --- |
common vehicle that threat actors use to create fraudulent domains.  17.  Mesh Digital Limited ......................... 1%
|     | 18.  NETHOUSE-RF ............................. | 1%  |
| --- | ---------------------------------------------- | --- |
Many characters in alphabets such as Cyrillic look identical or nearly
|     | 19.  Cronon AG ................................. | 1%  |
| --- | ------------------------------------------------ | --- |
identical to characters in the Latin alphabet. By substituting them in  20.  Nics Telekomunikasyon Tic Ltd. Sti. ............. 1%
place of corresponding Latin characters, attackers can create fake
| domains resembling popular brand domains. Table 6 |     |     |
| ------------------------------------------------- | --- | --- |
Fraudulent IDN domains are a widespread problem. In 2018, nearly
NEARLY
66% of Proofpoint Digital Risk Protection customers had at least one
66% of Proofpoint Digital Risk Protection
detection for an active fraudulent IDN domain that uses their brand
customers had at least one detection
name. And for more than 1 in 5 of those customers, the fraudulent
for a fraudulent IDN in 2018
domains are almost an exact match for their brand-owned domain,
with just one or two characters swapped.

11 DOMAIN FRAUD REPORT | 2019
LOOKALIKE DOMAINS
Top TLDs for Lookalike Domains
L ookalike domains, too, are poised for an attack
1. .com ............42% 6. .xyz ..............3%
2. .net ..............5% 7. .top ..............3%
79% resolve to an IP address 3. .ru ...............5% 8. .online ...........2%
4. .org ..............3% 9. .cn ..............2%
73%
have an HTTP response 5. .info .............3% 10. .club .............2%
34%
have an MX record
Table 7
17%
have a security certificate
Top Registrars for Lookalike Domains
To create a lookalike domain, fraudsters add or change as few
characters as possible in the company’s brand domain. These 1. GoDaddy.com, LLC. . . . . . . . . . . . . . . . . . . . . . . . . 23%
changes are often so subtle that they are difficult for visitors to detect. 2. NameCheap, Inc. ........................... 9%
For example, the letter “m” can be replaced by the letters “r” and “n” 3. Alibaba Cloud Computing (Beijing) Co., Ltd. ...... 5%
to give the appearance of “m.” In the case of acmeanvils.com, the 4. Registrar of Domain Names REG.RU, LLC ....... 4%
lookalike domain would appear as in acrneanvils.com. 5. PDR Ltd. d/b/a PublicDomainRegistry.com ....... 4%
6. Tucows Domains Inc. ........................ 3%
Our code-cracking brains naturally “autocorrect” these lookalike
7. GMO Internet, Inc. dba Onamae.com ........... 3%
spellings to make sense of them. Attackers know this and exploit
8. Xin Net Technology Corporation ................ 2%
this tendency regularly.
9. NameSilo, LLC .............................. 2%
Our data indicates that lookalike domain registrations increased 18% 10. Name.com, Inc. ............................. 2%
between Q1 and Q4 2018. And like IDN attacks, they represent a 11. Google Inc. ................................ 2%
widespread concern. 12. DYNADOT, LLC ............................. 2%
13. eNom, Inc. ................................. 2%
Like fraudulent domains overall, lookalike domains hide in plain
14. Network Solutions, LLC. ...................... 2%
sight when it comes to TLDs and registrars:
15. Chengdu West Dimension Digital Technology
Co., Ltd. ................................... 2%
16. Regional Network Information Center, JSC
dba RU-CENTER ............................ 1%
76%
of Proofpoint Digital Risk Protection
17. OVH ...................................... 1%
customers had at least one detection
18. 1&1 Internet SE ............................. 1%
for a lookalike domain in 2018
19. 123-Reg Limited ............................ 1%
20. Domain.com, LLC ........................... 1%
Table 8

12 DOMAIN FRAUD REPORT | 2019
TLD ATTACKS frequently cited as one of the most egregious examples of TLD
domain misuse.
Because the most popular TLDs (“.com” and “.net”) are
75%
resolve to an IP address unavailable, TLD attacks use a more broadly distributed set of TLDs
than other types of fraudulent domains. In the chart below, note
70%
have an HTTP response
the appearance of .app and .icu, which are new TLDs launched
37% have an MX record in 2018. Fraudsters pay attention to new TLD releases and rush to
register brand names with them as quickly as possible.
13%
have a security certificate
TLD attack domain characteristics also show higher active
resolutions than we see in the broader domain universe
TLD attacks are exact matches of the brand domain with different
endings after the “dot.” For example, if the brand-owned domain
was acmeanvils.com, threat actors might register acmeanvils.gq TLD attacks affect nearly all enterprises:
or acmeanvils.work.
96%
Whitehouse.com is a famous example of this domain type. In + of Proofpoint Digital Risk Protection
customers had at least one TLD
1997, Dan Parisi seized on this TLD opportunity and purchased the
“whitehouse.com” domain. He then turned it into a pornography attacks detection in 2018.
site that generated $1 million in revenue per year.
The official domain of the White House is whitehouse.gov. Although 23% TLD attack registrations
.gov as a TLD is only available to official government sites, it is increased between Q1
more common for people to type the .com TLD. In this case, that
and Q4 of 2018
simple “com” typo would land users on an adult site by mistake.
Because of the explicit and commercial content of the site, it is
Top TLDs for TLD Attacks Top Registrars for TLD Attacks
1. .app ....................6% 1. GoDaddy.com, LLC. . . . . . . . . 17% 11. Uniregistrar Corp ............ 2%
2. NameCheap, Inc. .......... 12% 12. Network Solutions, LLC ....... 2%
2. .ooo ....................3%
3. Alibaba Cloud Computing 13. OVH ...................... 2%
3. .xyz .....................3%
(Beijing) Co., Ltd. ........... 10%
14. GMO Internet, Inc.
4. .online ..................2% 4. PDR Ltd. d/b/a d/b/a Onamae.com .......... 2%
PublicDomainRegistry.com. . . . 5%
15. Gandi SAS ................. 1%
5. .site ....................2%
5. Tucows Domains Inc. ........ 3%
16. Registrar of Domain Names
6. .club ....................2%
6. Google Inc. ................ 3% REG.RU, LLC ............... 1%
7. .top .....................2% 7. Name.com, Inc ............. 3% 17. 1&1 Internet SE ............. 1%
8. Dynadot LLC ............... 2% 18. 1API GmbH ................ 1%
8. .info ....................2%
9. Key-Systems LLC ........... 2% 19. NameSilo, LLC .............. 1%
9. .icu .....................2%
10. Chengdu West Dimension 20. Regional Network Information
10. .website .................1% Digital Technology Co., Ltd .... 2% Center, JSC dba RU-CENTER ....1%
Table 9 Table 10

13   DOMAIN FRAUD REPORT | 2019
DOMAINS SELLING COUNTERFEIT GOODS
Top Registrars
Some domains use a brand name and append words like “online,”  For Domains Selling Counterfeit Goods
“sale” or “outlet.” These domains lead to websites that entice
customers with deep discounts and special pricing. Users are  1.  Chengdu west dimension digital .............. 18%
then tricked into providing their personal information and credit  2.  NameSilo, LLC ............................. 14%
card numbers. If they actually receive an item purchased on these  3.  PDR Ltd. d/b/a PublicDomainRegistry.com
sites, the items are usually cheap knockoffs of the brand’s goods.  [Tag = PDR-IN] ............................ 10%
In many cases, attackers simply steal the personal and payment  4.  HOSTING CONCEPTS B.V. .................... 8%
information without ever shipping anything.  5.  Alibaba Cloud Computing (Beijing) Co., Ltd. ...... 7%
|     | 6.  Gransy s.r.o d/b/a subreg.cz ................... | 6%  |
| --- | ---------------------------------------------------- | --- |
7.  GoDaddy.com, LLC. . . . . . . . . . . . . . . . . . . . . . . . . . 5%
of retail brands had at
| 78% | 8.  NameCheap, Inc ............................ | 5%  |
| --- | ----------------------------------------------- | --- |
least one detection in
|     | 9.  Hosting Concepts B.V. d/b/a Openprovider ....... | 3%  |
| --- | ---------------------------------------------------- | --- |
2018 for domains selling
|     | 10.  1API GmbH ................................ | 3%  |
| --- | ----------------------------------------------- | --- |
counterfeit goods 11.  DYNADOT, LLC ............................. 2%
|     | 12.  West263 International Limited .................. | 2%  |
| --- | ----------------------------------------------------- | --- |
|     | 13.  Netim .....................................      | 2%  |
On average, each of these customers had more than 200
|     | 14.  Bizcn.com, Inc. ............................. | 1%  |
| --- | -------------------------------------------------- | --- |
detections. Businesses that sell high-value goods—for example,
|     | 15.  Xin Net Technology Corporation ................ | 1%  |
| --- | ---------------------------------------------------- | --- |
luxury fashion, watches or sneakers—experienced a much higher
|     | 16.  Xiamen 35.Com Technology Co., Ltd. ........... | 1%  |
| --- | --------------------------------------------------- | --- |
rate. Registrations of counterfeit domains increased 11% between
|     | 17.  Registrar.eu ................................ | 1%  |
| --- | -------------------------------------------------- | --- |
Q1 and Q4 of 2018, spiking in Q3, likely in preparation for Q4
18.  Web Commerce Communications Limited
holiday shopping.
|     | dba WebNic.cc .............................       | 1%  |
| --- | ------------------------------------------------- | --- |
|     | 19.  InterNetX GmbH ............................  | 1%  |
|     | 20.  HEXONET Services Inc. ...................... | 1%  |
30%
have security
Table 11
certificates
Domains selling counterfeit goods have security certificates at a
significantly higher rate than other types of fraudulent domains.
This likely reflects an effort to make their transactions appear
more legitimate.
On the other hand, only 8% of counterfeit domains have MX
records. This suggests that they mainly use other channels such
as social media and sites with public comments enabled to drive
traffic to their sites rather than email.

14 DOMAIN FRAUD REPORT | 2019
Top TLDs Top Countries Hosting
For Domains Selling Counterfeit Goods For Domains Selling Counterfeit Goods
1. .com ............41% 6. .xyz ..............2% 1. United States ..............................56%
2. .top .............16% 7. .us ..............2% 2. Netherlands ............................... 15%
3. .fr ...............9% 8. .org ..............1% 3. Turkey .................................... 8%
4. .co.uk ............8% 9. .ru ...............1% 4. Great Britain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6%
5. .it ...............6% 10. .net ..............1% 5. Sweden ................................... 5%
6. Estonia .................................... 3%
Table 12
7. Russia .................................... 1%
8. France ...................................0.6%
Top Security Certificate Issuers
9. Germany .................................0.6%
For Domains Selling Counterfeit Goods
10. Romania .................................0.4%
1. COMODO CA Limited .......................43%
Table 15
2. Let’s Encrypt .............................. 21%
3. CloudFlare ............................... 20%*
Top Autonomous System Numbers (ASN)
4. cPanel ................................... 14%
For Domains Selling Counterfeit Goods
5. TrustAsia Technologies ....................... 1%
1. 13335-CLOUDFLARENET: Cloudflare, Inc., US ...23%*
Table 13
2. 41204-HOSTCOOL, NL ...................... 12%
3. 18779-EGIHOSTING: EGIHosting, US ........... 7%
Top Web Servers
4. 36352-AS-COLOCROSSING: ColoCrossing, US .. 6%
For Domains Selling Counterfeit Goods
5. 204353-GLOBALOFFSHORE, GB .............. 5%
1. apache ...................................67% 6. 59447-SAYFANET, TR ........................ 5%
2. cloudflare ................................ 23%* 7. 33387-NOCIX - DataShack, LC, US ............. 4%
3. nginx ..................................... 7% 8. 64435-GREENBEI, SE ....................... 3%
4. litespeed .................................0.7% 9. 197328-INETLTD, TR ......................... 3%
5. wcsflareplus ...............................0.7% 10. 29073-QUASINETWORKS, NL ................. 2%
Table 14 Table 16
* Cloudflare is an anti-DDoS product (likely included by default by some hosting providers) and masks the name of the actual hosting provider and web server for some of
these domains.

15 DOMAIN FRAUD REPORT | 2019
FRAUDULENT DOMAINS AND SECURITY CERTIFICATES
Websites with a security certificate start with “HTTPS” rather than
“HTTP” and feature some type of padlock icon, depending on the
web browser.
Not long ago, security awareness training taught users to look for
the padlock symbol at the beginning of a URL to ensure a website
was safe. But a security certificate does not mean the site has
been validated as trusted or legitimate. It only signifies that the data
transmitted between the user’s browser and the site is encrypted
and third parties cannot intercept and read the information in real time.
Fraudulent Domains with Security Certificates
50
40
30
20
10
Our research found that cyber criminals use security certificates
0
in 26% of their fraudulent domains. This finding is especially
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
concerning because all those years of “trust the padlock” training
have led many internet users to perceive these sites as legitimate. Figure 11
deretsigeR
sniamoD
fo
tnecreP
Top Issuers of Security Certificates for Fraudulent Domains
1. COMODO CA Limited .......................39%
2. Let’s Encrypt ..............................27%
3. CloudFlare ................................ 18%
4. cPanel ................................... 13%
5. DigiCert Inc ................................ 1%
Table 17
As Figure 11 shows, the percent of newly registered fraudulent
Our research found that cyber criminals domains with security certificates increased over the course of 2018
from just over 12% to more than 27%. This increase (and the spike in
use security certificates in
July) was likely a response to Google’s announcement that Chrome
26% would begin warning users that sites without security certificates are
of their
“not secure.” We expect the rate to continue climbing in 2019.
domains
Security certificates increased 27%
over the course of 2018 from
just over 12% to more than

16 DOMAIN FRAUD REPORT | 2019
EMAIL TRENDS
FRAUDULENT DOMAINS: TIME TO EMAIL ACTIVITY
Registration
Proofpoint email security products give our domain fraud analysts Date 14 Days 30 Days 90 Days
unique insight into enterprise email activity. This includes email
41.7%
traffic from fraudulent domains.
51.5%
Fraudulent domains sending email were generally quick to act, with
over 50% observed sending email within 30 days of registration. 71.8% 28.2%
The full breakdown appears in Figure 12.
Figure 12
For most fraudulent domains sending email, we saw a low volume
of activity. This points to highly targeted and socially engineered
attacks such as a form of wire fraud known as business email
For 96% of fraudulent domains sending email, we saw fewer than
compromise (BEC).
100 emails on the first date of email activity. For some fraudulent
domains impersonating highly recognizable retail brands (especially
those with complex supply chains), we observed much higher
94% of Proofpoint Digital Risk volumes of email, suggesting more broad-based attacks against
Protection customers customers and partners.
observed at least one of their Some companies have successfully gained ownership of domains
fraudulent domain detections that were fraudulently impersonating them through the Uniform
sending email in 2018.
Domain-Name Dispute-Resolution Policy (UDRP). But we have
also seen many fail to implement Domain-Based Message
Authentication, Reporting and Conformance (DMARC) on those
50% observed sending acquired domains. The lack of a strict DMARC policy published
email within 30 days by a domain allows fraudsters to spoof that domain and continue
sending fraudulent email as if they still owned it.
of registration day

17 DOMAIN FRAUD REPORT | 2019
PARKED DOMAINS
91% of Digital Risk Protection customers
had at least one detection for a
“Parked” domains incorporate brand names and resolve to an “parking group” domain in 2018
“under construction” page or a page with advertisements. These
domains are often owned and managed in bulk by “parking groups”
and are not always used for malicious purposes such as phishing.
The trend of “parked” domains appears to be on the rise.
Still, “parked” domains are not harmless, either. At the very Registrations of “parking group” domains more than doubled
least, they monetize traffic intended for other businesses. At the between Q1 and Q4.
worst, they may serve as indirect channels to malicious sites by
redirecting traffic or may serve malicious ads.

To learn how Proofpoint Digital Risk Protection can help you detect
threats at scale and protect your business and customers from
domain fraud, visit proofpoint.com/domain-monitoring.
ABOUT PROOFPOINT
Proofpoint, Inc. (NASDAQ:PFPT) is a leading cybersecurity company that protects organizations’ greatest assets and biggest risks: their people. With an integrated suite of cloud-based solutions,
Proofpoint helps companies around the world stop targeted threats, safeguard their data, and make their users more resilient against cyber attacks. Leading organizations of all sizes, including
more than half of the Fortune 1000, rely on Proofpoint to mitigate their most critical security and compliance risks across email, the cloud, social media, and the web. No one protects people, the
data they create, and the digital channels they use more effectively than Proofpoint.
©Proofpoint, Inc. Proofpoint is a trademark of Proofpoint, Inc. in the United States and other countries. All other trademarks contained herein are property of their respective owners.
proofpoint.com 0519-004

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-07", "model": "gemini-3.7-flash"} -->
