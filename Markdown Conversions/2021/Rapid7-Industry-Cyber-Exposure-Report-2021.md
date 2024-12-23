# Industry Cyber Exposure Report (ICER): Nikkei 225

## Table of Contents
- [Executive Summary](#executive-summary)
- [Email Security Among The Nikkei 225](#email-security-among-the-nikkei-225)
- [Web Service Security Among the Nikkei 225](#web-service-security-among-the-nikkei-225)
- [Version Complexity Among the Nikkei 225](#version-complexity-among-the-nikkei-225)
- [High-Risk Services Among the Nikkei 225](#high-risk-services-among-the-nikkei-225)
- [Vulnerability Disclosure Programs Among the Nikkei 225](#vulnerability-disclosure-programs-among-the-nikkei-225)
- [Conclusion](#conclusion)
- [Appendix: Prioritization in Times of Crisis](#appendix-prioritization-in-times-of-crisis)
- [Key Takeaways](#key-takeaways)
- [Results](#results)
- [HTTPS Support](#https-support)
- [Findings: RDP, SMB, and Telnet](#findings-rdp-smb-and-telnet)
- [Version Dispersion Among Web Servers](#version-dispersion-among-web-servers)
- [By Industry](#by-industry)
- [HSTS Adoption](#hsts-adoption)
- [Windows Remote Desktop Protocol (RDP)](#windows-remote-desktop-protocol-rdp)
- [Version Dispersion: Focus on Microsoft Exchange](#version-dispersion-focus-on-microsoft-exchange)
- [CISO Takeaways](#ciso-takeaways)
- [Summary](#summary)
- [Windows Server Message Block (SMB)](#windows-server-message-block-smb)
- [Telnet](#telnet)
- [Exposure Overview](#exposure-overview)
- [Results: Prevalence of VDP Adoption](#results-prevalence-of-vdp-adoption)
- [CISO Actions at a Glance](#ciso-actions-at-a-glance)

RESEARCH
©RAPID7 2021
Industry Cyber Exposure 
Report (ICER): Nikkei 225

## Executive Summary
As the world’s knowledge workers were driven home amid a pandemic and cases of ransomware ran rampant 
across the internet, measuring the world’s most critical businesses’ internet exposure has become more import­
ant than ever. In this round of Internet Cyber-Exposure Reports (ICERs), researchers at Rapid7 evaluate 5 areas 
of cybersecurity that are both critical to secure to continue doing business on and across the internet, and are 
squarely in the power of CISOs, their IT security staffs, and their internal business partners to address.
In this report, we examine the internet-facing cyber-exposure of the top companies listed on Japan’s Nikkei 225[^1]. 
Each section is accompanied by real-world, practical advice that practitioners can start implementing today. 
Note that this advice is not only for those CISOs who are privileged to hold positions in Nikkei 225 companies, 
but also for those security experts who find themselves in business and regulatory relationships with members 
of this prestigious collection of corporations.
Through the first half of 2021, Rapid7 will be releasing reports measuring these five critical areas of 
cybersecurity fundamentals across five of the most advanced economies of the world: 
1. The United States Fortune 500[^2]
2. The United Kingdom’s FTSE 350[^3]
3. Australia’s ASX 200[^4]
4. Germany’s Deutsche Börse Prime Standard 314[^5]
5. Japan’s Nikkei 225 (this report)
These five facets of internet-facing cyber-exposure and risk include:
1. Authenticated email origination and handling (DMARC)
2. Encryption standards for public web applications (HTTPS & HSTS)
3. Version management for web servers and email servers (focusing 
on IIS, nginx, Apache, and Exchange)
4. Risky protocols unsuitable for the internet (RDP, SMB, and Telnet)
5. The proliferation of vulnerability disclosure programs (VDPs)

[^1]: https://indexes.nikkei.co.jp/en/nkave/index?type=index
[^2]: https://www.rapid7.com/research/report/2021-industry-cyber-exposure-report/
[^3]: https://www.rapid7.com/research/reports/2021-industry-cyber-exposure-report-uk
[^4]: https://www.rapid7.com/research/report/2021-industry-cyber-exposure-report-anz/
[^5]: https://www.rapid7.com/research/report/icer-germany-2021/

The paper is divided into five detailed sections covering the areas mentioned above, and the overall takeaways 
of this research are as follows:
With these key findings in mind, the remainder of this report explores each of the 5 areas of cybersecurity mea­
surable in the Nikkei 225.
Before you dive in, we want to note that if your organization was and/or still is impacted by those events, you 
may be feeling like you are spending most of your time and energy dealing with emergencies rather than being 
able to focus on some of the more chronic issues outlined in this report. Since our goal is to help organizations 
become (and remain) safe and resilient, we have an appendix just for you. Consider jumping there first before 
tackling the sections below.
- Nikkei 225 email security posture is lagging behind the US and UK. At the beginning of 2021, email 
security among the Nikkei 225 isn’t keeping pace with its peers in the US and UK. While DMARC 
adoption in the US and UK hovers around 50%, only about 13% of all the surveyed companies op­
erating in Japan have any DMARC records configured, and of those, 25 out of 29 (about 86%) are 
set with a p=none (or passthrough) policy. In other words, only 4 (under 2%) of the Nikkei 225-listed 
companies are taking active measures to protect their brands, employees, and customers through 
DMARC p=quarantine or p=reject policies.
- Exposed, dangerous services are less of a concern in Japan. While dangerous protocol exposures of 
Windows Remote Desktop (RDP) file-sharing (SMB), and Telnet continue to be an issue across the 
surveyed companies, it does not appear to be nearly as much of a problem as we’ve seen among 
the U.S.-based Fortune 500: For RDP and SMB, over 90% of the Nikkei 225 had no exposure.
- Telnet and HSTS remain concerning, however. Telnet is a different story; about 27% of the Nikkei 
225 has some legacy telnet exposed to the internet. Additionally, when we looked at secure HTTP 
(HTTPS) deployment, we found that while HTTPS is standard for 100% of the Nikkei 225 companies, 
very few listed companies (18%) have implemented HSTS directives to ensure that HTTPS infrastruc­
ture is actually being used all the time.
- Version dispersion is on the right track in Japan. Only 16 companies in the Nikkei are running their 
own Exchange servers (rather than managed cloud instances), and of these, about 75% are running 
at least 1 instance of the latest supported version. That said, we did count 93 distinct versions of 
Apache, 75 distinct versions of Nginx, and 17 distinct versions of IIS in the Nikkei 225.
- The Japanese Technology sector stands alone in vulnerability disclosure. Nearly all of the 16 VDPs 
we found across the 225 surveyed companies are either in the Technology sector proper, or in tech-
heavy Consumer Goods companies. So, while this is pretty good for Japanese tech, it’s not great for 
the rest of the Japanese businesses that have not normalized VDPs for their products and infra­
structure.

## Key Takeaways
Industry Cyber-Exposure Report (ICER): Nikei 225

## Email Security Among 
the Nikkei 225
Industry Cyber-Exposure Report (ICER): Nikei 225
7
We all know and love—or at least begrudgingly rely upon—email. It is a pillar of modern communications, 
but is unfortunately also highly susceptible to being leveraged as a mechanism for malicious actions, such as 
spoofing or phishing.
A core concern regarding email is the authenticity of the source, and in recent years, DMARC has arisen as 
the preeminent email validation system. DMARC builds upon the foundations of 2 older email authentication 
systems: Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM), which respectively check 
for mail-server authorization (“Is the sender authorized?”) and email integrity based on key signatures (“Was 
the content altered?”). The various components of DMARC can serve to mitigate direct threats as well as po­
tential reputational damage, such as spoofed emails intended to mislead partners, suppliers, or customers.
A properly implemented DMARC system can identify illegitimate emails and define how they should be han­
dled. DMARC can be configured to handle emails of suspect provenance with different degrees of severity, 
depending on the aggressiveness of IT administrators. The DMARC policy options include:
By virtue of its efficacy in mitigating malicious messaging via email, we consider DMARC a significant risk 
mitigator and highly recommend its implementation.  Unfortunately, while the benefits of DMARC are 
profound, its implementation is not global. DMARC’s implementations are tracked in public Domain Name 
System (DNS) records. To determine whether an organization utilizes DMARC only requires the examination 
of the organization’s published DMARC record. We are able to discern the scale and types of DMARC imple­
mentations by comparing the primary, well-known domains of the Nikkei organizations against their corre­
sponding DMARC records that appear alongside DNS.
Note that for the scope of this study, we focus primarily on the apex domains of organizations, and do not 
explore additional domains owned by particular organizations. We elected this approach because there can 
be significant variation in domain set ownership by organization. By focusing on apex domains, we are in 
effect treating it as a bellwether indicator of an organization’s overall email security posture. After all, if an 
organization fails to implement DMARC on a primary domain, how confident should we be that the organi­
zation practices healthy email hygiene across far less-prominent domains?
These published DMARC records are intended to be highly accessible. They are the means through which 
email recipients determine how to validate emails using DMARC, what email address to notify when receiv­
ing emails that fail DMARC validation, and what DMARC policy to apply in handling invalid emails.
- None, where suspect emails are reported to a designated email address that serves to monitor DMARC 
notifications.
- Quarantine, where suspect emails are punted to the spam folder and a report of its receipt is delivered 
to the monitoring email address.
- Reject, where in addition to notifying the monitoring email address, suspect emails are not delivered at 
all.

Industry Cyber-Exposure Report (ICER): Nikei 225
8
We found that 29 (or approximately 13%) of the Nikkei 225 set of organizations had implementations of DMARC 
for their primary domains, all of which were validly formatted. Of the set of national indexes that we have exam­
ined so far in the ICER series, this is a remarkably low level of DMARC coverage in comparison.
When we examine the DMARC policies in a bit more detail, we find that most valid DMARC policies are set to 
“none”, or simply to monitor and inform, followed by “reject”, which is the most aggressive approach. The least 
prominent policy implementation is “quarantine”, a policy to isolate suspect emails. That being said, the num­
bers are all fairly small, so attempts to draw any sort of pattern would be meaningless.
Somewhat disheartening is the lack of any DMARC implementations across all other industries to some extent. 
## Results
No Valid Policy
196 (87%)
Valid
29 (13%)
All instances of DMARC policies found were properly formed and valid.
2020: Nikkei 225 DMARC Coverage
Updated May 2021
![Figure 1: 2020 Nikkei DMARC Coverage]
No valid policy - 87.11% (196)
none - 11.11% (25)
quarantine - 0.44% (1)
reject - 1.33% (3)
All instances of DMARC policies found were properly formed and valid.
2020: Nikkei 225 DMARC Policies
Updated May 2021
![Figure 2: 2020 Nikkei DMARC Polices]
none
quarantine
reject
No valid policy
0
10
20
30
40
50
0
10
20
30
40
50
0
10
20
30
40
50
0
10
20
30
40
50
Transportation and Utilities (n = 20)
Financials (n = 21)
Consumer Goods (n = 33)
Capital Goods/Others (n = 35)
Materials (n = 58)
Technology (n = 58)
Count
none
quarantine
reject
No valid policy
n is the count of distinct organisations by sector. Sectors are organized by n.
2020: Nikkei 225 DMARC Policies for Apex Domains
Updated: May 2021
Industry Cyber-Exposure Report (ICER): Nikei 225
9
If DMARC has not already been implemented in your organization, take proactive measures to get it set up. 
Nowadays, DMARC can be thought of as a foundational fixture of email hygiene, and it broadly signals an orga­
nization’s commitment to modern information security norms. Furthermore, lacking a DMARC implementation 
leaves an organization potentially blind to malicious email campaigns that are not captured through some form 
of DMARC monitoring that can be informative in terms of scale, source, and severity.
Once the decision has been made to implement DMARC, it’s time to consider the policy implementation in a 
more nuanced manner. An aggressive reject policy is highly secure but might result in legitimate emails being 
blocked. A more forgiving quarantine policy could strike a balance between preventing aggravation and allow­
ing for some form of recourse. At the very minimum, a DMARC implementation of some form should be in place 
to monitor for illegitimate or poorly configured email traffic.
![Figure 3: 2020 Nikkei DMARC Polices for Apex Domains]
We can also separate the organizations by industry to get a better sense of DMARC variations across the sec­
tors. The most prominently featured industries in the Nikkei 225 include technology and materials.
## By Industry
## CISO Takeaways
Web Service Security 
Among the Nikkei 225
Industry Cyber-Exposure Report (ICER): Fortune 500
11
The vast majority of the interactions an average person has with technology is through some form of a web 
application, but what constitutes a “web app” can be considered quite nebulous, and the security controls for 
hardening these applications are equally broad. APIs, distributed authentication schemes, single-page appli­
cations, and static websites all might fall under the general category of “web application.” There are very few 
security measures that should be applied to all web applications across the board without further subdividing 
what specific type of application we are referring to. However, there are a couple that we will examine here.
All web applications should require strong encryption, with a vanishingly small number of exceptions. While 
this is most critical for applications serving up critical or sensitive information, such as personally identifiable 
information (PII), it is important even if you serve only static informational content. There is a common miscon­
ception that the only risk of using an insecure connection is a loss of confidentiality—that the information a 
user is browsing could be observed by a malicious third party. While this certainly is a risk, it is often overlooked 
that a lack of encryption makes the connection vulnerable to modification (a loss of integrity). This means that 
malicious third parties could not only observe potentially confidential information, but that they could alter that 
information or inject their own content that could potentially compromise your users.
The risk of malicious content injection exists regardless of whether your web application serves sensitive infor­
mation or just cute pictures of cats[^6]. Due to this universal risk to a site’s users and to the overarching brand 
reputation of the site owner, we will consider the support of strong encryption (in our case, TLS) and the en­
forcement of its usage via HTTP Strict Transport Security (HSTS). For the purposes of this section, we will look 
at the primary domain for each company, as it is the domain that is most responsible for a company’s brand 
reputation.
HTTPS is the protocol that ensures web traffic is encrypted and secure. There are a few ways that HTTPS could 
be configured in an environment. 
Supporting HTTPS for your site is table stakes for having a web presence at all, with requiring encryption follow­
ing very closely behind. HSTS preloading does carry some technological challenges, but they are challenges that 
a web security program should be working to proactively address. 
With all this said, let’s share some good news right off the bat: Among the sites we examined in the Nikkei 225, 
100% of them supported HTTPS.
- Not available (HTTP only)
- Required (HTTP “Strict Transport Security”, or HSTS, configured)
- Available and optional
- Required with HSTS preloading

[^6]: https://www.sanrio.co.jp/

## HTTPS Support
No HSTS Policy - 184 (81.78%)
HSTS Enabled & Preload Enabled & Include Subdomains Enabled - 5 (2.22%)
HSTS Enabled & Include Subdomains Enabled - 6 (2.67%)
HSTS Enabled & Preload Enabled - 2 (0.89%)
HSTS Enabled - 28 (12.44%)
Percentage calculated based on the total set of domains (225)
2020: Nikkei 225 HSTS Policy
Industry Cyber-Exposure Report (ICER): Nikei 225
12
The outlook for HSTS adoption was unfortunately a bit grim.
As you can see, only about 18% of the sites examined supported HSTS at all. This is substantially less than what 
we have observed in other reports. If the site already fully supports HTTPS (and these sites all do), it should be 
relatively simple to implement HSTS to guarantee your users visit the secure version of your site. Most of these 
sites do provide a redirect from the insecure version of their homepage—however, that will not mitigate a man-
in-the-middle (MiTM) attack.
None of the observed domains have HSTS manually disabled. The percentage of domains with this configuration 
tends to be low, so this observation is likely due to the low total number of HSTS supporting domains in this list. 
27% of sites that support HSTS also support the “includeSubDomains” directive, protecting the entire domain 
and all subdomains. This is a fantastic security feature, but it can be difficult to implement in certain situations.
17% of sites with HSTS also support the “preload” directive. This directive will cause crawlers to automatically 
add your site to a global list of known sites that support HSTS. If a supporting browser is directed to a site with 
HSTS preload enabled, it will guarantee that the first connection is always conducted over HTTPS, meaning it 
eliminates the one, single place where your site’s users are vulnerable to MiTM attacks—the first connection to 
your site before an HSTS header has ever been encountered. This configuration option is a simple way to add an 
extra layer of protection for your users, and if you bother to enable HSTS, you should certainly add this option. 
While it’s a somewhat newer directive with less browser support, there is no downside to including it (browsers 
that do not support HSTS will simply ignore it). 
## HSTS Adoption
![Figure 4: 2020 Nikkei 225 HSTS Policy]
Industry Cyber-Exposure Report (ICER): Nikei 225
13
Securing and encrypting traffic to your user-facing domains is not only good practice, but it also protects your 
corporate brand. Securing HTTP with TLS has been a major point of focus for the web-security community for 
the past several years, and for good reason. All of the Nikkei 225 companies provided a secure version of their 
primary website, but they have a long way to go before they come up to snuff in terms of best practices. 
The especially poor adoption of HSTS across the Nikkei 225 could be an indicator that their application security 
programmes are falling behind, especially since other, more sophisticated, mitigations can be significantly more 
complicated to implement. While the standards certainly move quickly, it’s important to keep up to speed, espe­
cially when your brand reputation is on the line.
If you haven’t thought about your site’s encryption for a while, now might be the time to revisit it.  A compa­
ny’s brand reputation is on the line when consumer-facing web applications suffer from security failures, and 
it’s important to consider this fact when making investment decisions in various security programmes. 
If your company’s website is not supporting HSTS, it might be worthwhile to find out why. Is it a technical, 
organizational, or budgetary constraint? Finding the cause could be a great springboard for re-evaluating 
your entire application security program.
## Summary
## CISO Takeaways
Version Complexity 
Among the Nikkei 225
Industry Cyber-Exposure Report (ICER): Nikei 225
15
Complexity is the enemy when it comes to successful security outcomes in an organization. Diversity in sys­
tems, technologies, and business processes present real, daily challenges for even the most mature security 
teams, especially when it comes to patch and vulnerability management. 
Patching even 1 major vulnerability can be a Herculean task in many places. Diversity compounds complex­
ity within each technology component. That is to say, an organization may have many different web server 
technologies in use. Each technology, in turn, may have its own hodgepodge of versions, which directly (neg­
atively) impacts configuration management and patch management.
To get a feel for how these well-resourced organizations are performing in this area, we looked at 3 separate 
factors:
We used Project Sonar[^7] and Recog[^8] to identify internet-facing technologies—e.g., web servers, file servers, 
DNS, SSH, etc.—that were in use for each organization in the Nikkei 225. We then mapped them to available 
Common Platform Enumeration[^9] (CPE) strings. This methodology has some limitations in that the results are 
constrained by:

[^7]: https://www.rapid7.com/research/project-sonar
[^8]: https://github.com/rapid7/recog
[^9]: Common Platform Enumeration definition and database: https://nvd.nist.gov/products/cpe

Our findings show that:
- Within a single technology stack (web servers), organizations in some key industries—Capital Goods/
Others, Consumer Goods, Technology, and Transportation and Utilities—expose 9 or more different 
versions of Apache and/or Nginx. Capital Goods/Others, Consumer Goods, Financials, Materials, Tech­
nology, and Transportation and Utilities have 1 or more members exposing 3 or more different versions 
of IIS. This increases their respective attack surfaces and makes it difficult to deploy patches (when 
they bother to apply patches) due to testing and quality assurance complexity. 
- Some organizations have serious difficulty keeping critical IT infrastructure—such as Microsoft Ex­
change—current. Impressively, around 75% (12 out of 16) of Nikkei 225 that still run self-hosted Mic­
rosoft Exchange are running at least 1 current/supported version of Exchange. On the flip side, about 
56% (9 out of 16) are running at least one end-of-life version of Exchange 2010, putting them at risk of 
future vulnerability exploitation.[^10]
1.  The diversity of the portfolio of a selected technology—web servers—in use by each organization
2.  How well maintained this portfolio is
3.  How well organizations maintain critical services, such as email gateways
- The fingerprints available to Recog
- How promiscuous each fingerprintable service is (i.e., whether Recog can extract version information)

[^10]: This adds up to over 100%, because it’s possible to run both a current and EOL’ed Exchange installation in the same organization.
![Figure 5: Web Server Version Dispersion in 2021 Nikkei 225 Members]
Industry Cyber-Exposure Report (ICER): Nikei 225
16
These constraints, if anything, generally result in underreporting of the magnitude of the findings.  
A higher density of points toward “1” on the X-axis means that each of the organizations those points represent 
are running with a low version dispersion. This means they have better control over server/service deployments 
and configurations, have fewer versions to test patches against, and can make changes faster and with more 
confidence than others. It also likely means they have a more rigorous “you must be this tall to deploy a server 
on the internet” rules than organizations that are further to the right on the X-axis.
Back in 2018, when we began our first foray into analysing the cyber-exposure of the Nikkei 225, we created the 
term “version dispersion” to refer to the diversity of versions within a service component an individual organiza­
tion was exposing to the internet. With the dramatic rise[^11] in enterprise use of tooling such as Kubernetes[^12], we 
expected to see a reduction in version dispersion of the 3 web servers—IIS, Apache, and Nginx—that we 
previously measured.
There are at least more than 93 distinct versions of Apache, 75 distinct versions of Nginx[^13], and 17—yes, 17—
versions of IIS[^14] running across the entire set of Nikkei 225 members. Let’s see how that stacks up by industry.

[^11]: A Cloud Native Computing Foundation 2019 survey notes 78% of respondents are using Kubernetes in production, a huge jump 
from 58% in 2018
[^12]: Kubernetes main site: https://kubernetes.io
[^13]: Some organizations announce they use a particular server type but redact the discrete version number.
[^14]: We frequently see leaking of IIS build strings in announced Server header banners in IIS deployments.
- The ports and protocols Project Sonar studies
- Our measurement of only IPv4-space
- Sonar honouring IPv4 opt-out requests

## Version Dispersion Among Web Servers
Apache
IIS
Nginx
0
20
40
60
80
0
20
40
60
80
0
20
40
60
80
0
20
40
60
80
0
20
40
60
80
0
20
40
60
80
Transportation and Utilities (n=10)
Technology (n=40)
Materials (n=30)
Financials (n=7)
Consumer Goods (n=20)
Capital Goods/Others (n=27)
# of web server versions identiﬁed
Each dot is one organisation. Placement on the X-axis denotes how many different versions are in-use by a single organisation
Web Server Version Dispersion in 2021 Nikkei 225 Members
Industry Cyber-Exposure Report (ICER): Nikei 225
17
0
5
10
15
20
25
30
35
XSS
DoS
Overﬂow
Code
Execution
Info
Leak
Memory
Corruption
Barrier
Bypass
Gain
Privileges
Directory
Traversal
CSRF
# CVEs
Exchange CVEs by Type
Attackers and cyber-insurance assessors alike notice such things and may be more likely to target organizations 
that exhibit a more “wild, wild west” stature. There is a striking difference between web server version disper­
sion in the Nikkei 225 vs what we’ve reported in the FTSE 350 and Fortune 500 ICERs. One reason for this is that 
companies listed in the Nikkei seem to have a preference for “the cloud,” possibly to ensure faster global con­
nectivity to the information or services provided by the web services they expose. We do not measure “cloud” 
assets in the ICERs, so these positive results come with said additional caveat.
Some internet-facing services are more important than others. It’s one thing to have a crusty old Apache HTTPD 
server attached to the internet, which may only have a denial-of-service weakness. It is quite another thing to 
run old versions of what most organizations would (or should) deem critical infrastructure, such as Microsoft 
Exchange servers or VPN/gateway/remote-access services.
To get a feel for how well these organizations maintain critical services, we’ll take a peek at Microsoft Exchange 
hygiene. Unlike their Fortune 500 counterparts, only 6% of Nikkei 225 organizations still[^15] have at least 1 inter­
net-facing Exchange server handling business-critical email, and Exchange has had a fair number of weakness­
es—of varying criticality—uncovered over the years:
16 organizations (excluding 2 ISPs that allow general service hosting) have chosen to go it on their own 
when it comes to email hosting, so surely they know the dangers facing self-hosted Exchange and take care 
to ensure this vital service is at peak resiliency, at least when it comes to security patches. Right?

[^15]: Microsoft 365/Office 365 adoption continues to grow at a significant clip, with 70% of the Fortune 500 using one or more services, 
including hosted Exchange. Source: https://www.thexyz.com/blog/microsoft-office-365-usage-statistics/

## Version Dispersion: Focus on Microsoft Exchange
![Figure 6: Exchange CVEs by Type]
Industry Cyber-Exposure Report (ICER): Nikei 225
18
The above figure paints a fairly disturbing picture of the state of Microsoft Exchange in the Nikkei 225 in both 
currency (i.e., age of some server versions) and whether the deployed version is supported[^16] by standard Micro­
soft support contracts[^17]. On the plus side, just over 50% of discovered, precise-version fingerprinted instances 
are 2020/2021 releases. 
We were hoping to see a repeat of our ASX 200 ICER findings with zero presence of Exchange 2007 (which has 
been at end-of-life status for a while). Sadly, our hopes were crushed as we spotted a single instance at a major 
Technology company. Additionally, a few handfuls of the Nikkei 225 did not seem to get the memo[^18] about Ex­
change 2010 reaching end-of-life status in October 2020.

[^16]: https://docs.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates
[^17]: This does not take into account the fact that an organization may have a custom or extended support agreement with Microsoft, 
though that matters little when it comes to vulnerability exploitation.
[^18]: https://docs.microsoft.com/en-us/microsoft-365/enterprise/exchange-2010-end-of-support?view=o365-worldwide
0
10
20
30
40
Jan
2011
Jan
2012
Jan
2013
Jan
2014
Jan
2015
Jan
2016
Jan
2017
Jan
2018
Jan
2019
Jan
2020
Jan
2021
Discovered Exchange Server Release Date
# Servers
Latest Version
Older Version
Exchange Server Age/Up-to-Date Status of the Nikkei 225
![Figure 8: Exchange Server Age/Up-to-date Status of the Nikkei 225]
Industry Cyber-Exposure Report (ICER): Nikei 225
19
If your organization is struggling to keep up with Exchange patching, you may have a bit of wiggle room 
when it comes to excuses since Microsoft does keep you busy, as seen in the volume of in-year updates for 
at least modern versions of Exchange:
![Figure 10: Exchange Server Releases Per Year]
![Figure 9: Nikkei 225 Exchange Server Distribution Major Version]
0
10
20
30
2007
2010
2013
2016
2019
Nikkei 225 Exchange Server Distribution by Major Version
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2012
2013 2014
2015
2016
2017
2018 2019
2015
2016
2017
2018
2019
2020
2021
2018
2019
2020
2021
0
5
10
15
20
2007
2010
2013
2016
2019
0
5
10
15
20
In-Year Release Count
Exchange Major Version Number
Position of each label on the X axis shows how many releases the associated version of
Microsoft Exchange had that year. 2021 has been brutal on already overwhelmed IT teams.
Exchange Server Releases Per Year
Industry Cyber-Exposure Report (ICER): Nikei 225
20
Jan
2010
Jan
2011
Jan
2012
Jan
2013
Jan
2014
Jan
2015
Jan
2016
Jan
2017
Jan
2018
Jan
2019
Jan
2020
Jan
2021
Transportation and Utilities
Technology
Materials
Consumer Goods
Capital Goods/Others
Jan
2010
Jan
2011
Jan
2012
Jan
2013
Jan
20