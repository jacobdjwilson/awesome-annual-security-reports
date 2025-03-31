```markdown
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
3. **Readability**: Ensure professional formatting and adherence to Markdown standards. DO NOT enclose the top and bottom of the content in \`\`\`markdown and \`\`\` . 
4. **Fidelity**: Confirm the output matches the original PDF exactly.  

---
# Report Content Below

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Threat Landscape](#threat-landscape)
  - [The Threat Landscape in Charts](#the-threat-landscape-in-charts)
  - [Top Threats and Campaigns](#top-threats-and-campaigns)
  - [Mimecast Risk Radar](#mimecast-risk-radar)
  - [Major Event Timeline](#major-event-timeline)
- [Recommendations](#recommendations)
  - [Threat-Specific Countermeasures](#threat-specific-countermeasures)
  - [Best Practices and Advisories](#best-practices-and-advisories)
  - [Steps Specific to Mimecast Clients](#steps-specific-to-mimecast-clients)
- [Conclusion](#conclusion)
- [Resources](#resources)

## 1. Introduction <a name="introduction"></a>
Strong threat intelligence has become critical for 
companies and organizations to defend against 
attackers’ increasing agility. Organizations of 
every size should educate themselves on the 
latest trends, track the threats targeting their 
industry and suppliers, and harden defenses 
and update their processes to prevent their 
business communications and people from 
being used against them. 
 
In the second half of 2024, Mimecast processed 
more than 90- billion data points for its over 
42,000 customers, flagging more than 5- billion 
threats during the six-month period. The total 
number of protected interactions greatly 
exceeded that by many multiples. Email and 
collaboration tools continue to be the channels 
through which most attackers start their effort 
to compromise targeted organizations, allowing 
Mimecast to detect and analyze many threats 
before they become widely known. 
 
In our H2 2024 Global Threat Intelligence report, 
Mimecast has accumulated data from our 
systems protecting tens of millions of users, 
provided insights from our intelligence analysts, 
and added open-source intelligence on the latest 
threats. The report includes analysis of threat 
activity, statistics revealing attack trends, and a 
series of recommendations for small businesses 
and large enterprises to protect their employees 
and mitigate the impact of risky users. 
 
We invite you to explore our H2 2024 threat 
intelligence report and look forward to sharing 
more insights in the future. 
Introduction.
In the second half 
of 2024, Mimecast 
processed more than 
90- billion data points 
for its nearly 43,000 
customers, flagging 
more than 5- billion 
threats during the 
six-month period.
01

## 2. Executive Summary <a name="executive-summary"></a>
The trend of living off trusted services (LOTS) 
means that businesses will have to rely on more 
than just reputation and authentication systems to 
protect themselves from messaging and human-
centered attacks. In addition, threat actors are 
exploiting third-party suppliers — whether a 
service provider or a software product — to more 
easily slip into a targeted network.
 
 
 
 
Nation-state actors continued to resort to 
cyberattacks and cyber -espionage to pursue 
deniable actions against their rivals. China 
compromised US and Canadian[^1] infrastructure, 
Iran and Israel each targeted the other nation’s 
infrastructure[^2], and Russia continued to target 
European and US organizations[^3] after its invasion 
of Ukraine stalled.
[^1]: Tunney, Catharine. “China ‘compromised’ Canadian government networks and stole valuable info: spy agency.” CBC. 30 October 2024.  
https://www.cbc.ca/news/politics/cse-cyber-threats-china-1.7367719 
[^2]: Lemos, Robert. “As Geopolitical Tensions Mount, Iran’s Cyber Operations Grow.” Dark Reading. News article. 18 September 2024.  
https://www.darkreading.com/cyberattacks-data-breaches/geopolitical-tensions-mount-iran-cyber-operations-grow
[^3]: Eddy, Nathan. “Ukraine-Russia Cyber Battles Tip Over Into the Real World.” Dark Reading. News article. 3 October 2024. 
https://www.darkreading.com/cyberattacks-data-breaches/ukraine-russia-cyber-battles-tip-over-into-real-world
IN THE SECOND HALF OF 2024, THREAT 
ACTORS INCREASINGLY USED LEGITIMATE 
SERVICES AS A WAY TO OBSCURE THEIR 
ATTACKS AND ATTEMPT TO EVADE DEFENSES.

GEOPOLITICS HAVE GIVEN THREAT ACTORS 
BOTH MOTIVE FOR MORE FREQUENT 
ATTEMPTED COMPROMISES AND A FERTILE 
SUPPLY OF SUBJECT MATTER WITH WHICH TO 
CRAFT ATTACKS. 
02

## 3. Key Findings <a name="key-findings"></a>
AI TECHNOLOGIES CONTINUE TO OFFER 
UNIQUE BENEFITS TO BOTH DEFENDERS  
AND ATTACKERS.  
Cybersecurity analysts can more quickly analyze 
potential security events with the help of AI 
assistants, while incident responders can use AI 
to block and remediate an attack more quickly 
and completely. Attackers are benefiting as well: 
Mimecast research[^4] using linguistic analysis found 
that about 12% of emails — including phishing 
attacks — showed signs of being written by large 
language models (LLM). Deepfake audio and video 
have been effectively used to imitate CEOs and 
instruct employees to make fraudulent payments 
into cybercriminal accounts. 
  
 
 
ALL THESE TRENDS WILL CONTINUE IN 2025. 
The number of attacks that used the cloud to 
some degree more than doubled in 2024, while 
geopolitics continues to become more chaotic 
with France and Germany both facing elections 
in Europe, U.S. President Donald Trump seated 
for a second, non-consecutive term, and Russia 
and China continuing to flex their militaries on 
the world stage. Both security researchers and 
attackers are pioneering new ways to exploit 
AI systems, either taking advantage of security 
weaknesses or augmenting their own attack 
strategies. 
[^4]: Lee, Evonne. “New Mimecast Threat Intelligence: How ChatGPT Upended Email.” Mimecast Threat Intelligence Blog. 30 September 2024.  
    https://www.mimecast.com/blog/how-chatgpt-upended-email/.

ATTACKERS ARE 
INCREASINGLY LIVING  
OFF TRUSTED SERVICES 
(LOTS).
 Microsoft’s, Google’s, and 
Evernote’s cloud services 
commonly play hosts for 
threat actors’ payloads and 
landing pages. However, 
other cloud services are 
frequently being used for 
specific components of attack 
infrastructure: Cloudflare’s 
Turnstyle CAPTCHAs are 
regularly used to prevent 
threat analysis; DocuSign, 
TeamViewer, and Wave 
Compliance inadvertently 
host attackers’ content; and 
Google’s Gmail and Microsoft 
Outlook (formally Hotmail) are 
used to send  
phishing attacks.
Key
Findings.
ONE
K-
1
Masters of analysis 
with highly developed 
nervous system and 
large brain. They 
excel in adapting to 
their environment 
and overcoming 
challenges, making 
them a standout in 
threat intelligence. 
octo
SPECIES
Restore point
field flow control
p-34.34-3      fi
x
03
While threat actor activity has increased 
across almost all metrics, some trends 
stand out.  
-5  # T
5
MCS-51 #AT89S52
4897

GEOPOLITICS RAISES 
THE LIKELIHOOD OF 
CYBERATTACKS. 
The French and German 
elections, and the continued 
uncertainty of the Russia-
Ukraine war, will raise the 
tension of European Union 
politics. The departure of U.S. 
government from predictable 
norms could also result in 
greater activity in the cyber 
domain. Business, political, 
and cybersecurity experts 
have increasingly warned 
that geopolitical tensions and 
cybersecurity risks are linked. 
The top two risks identified for 
2025 in the annual Systemic 
Risk Barometer Survey 
conducted by the Depository 
Trust and Clearing Corporation 
were Geopolitical Risk and 
Cyber Risk.[^5]
[^5]: “Geopolitical and Cyber Risks Remain Top Threats to the Financial Services Sector in 2025.” DTCC. 4 December 2024.  
      https://www.dtcc.com/news/2024/december/04/geopolitical-and-cyber-risks-remain-top-threats-to-the-financial-services-sector-in-2025
TWO
K-2
KEY EMAIL 
AUTHENTICATION 
TECHNOLOGIES HAVE 
INCREASED CHALLENGES 
FOR ATTACKERS, WHILE AI 
HAS LOWERED THE BAR  
FOR CYBERCRIME. 
By using trusted services, 
attackers can meet the 
increasing authentication 
requirements of email 
technologies — such as 
SPF, DKIM, and DMARC — 
and appear to come from 
a trusted source. While the 
technologies make their 
attacks more complicated, 
the attackers continue to find 
services to pass authentication 
and alignment checks. In 
addition, the spread of AI chat 
bots allows even would-be 
cybercriminals to gain the skills 
necessary for hacking. 
 
THREE
K-3

MEDIA & PUBLISHING, 
ENTERTAINMENT & 
RECREATION, LEGAL 
SERVICES, AND THE ARTS 
INDUSTRIES SAW THE MOST 
THREATS PER USER IN  
H2 2024. 
Most industries saw a 
distinctive threat profile, 
including a greater proportion 
of malicious files targeting 
the Arts, Entertainment & 
Recreation sectors, while 
workers in the Media & 
Publishing sector encountered 
larger number of malicious 
links. Impersonation attacks 
dominated the threat profile 
for the software & SaaS sector.
FOUR
K-4
HUMANS CONTINUE TO 
HAVE A PRIMARY ROLE IN 
MOST BREACHES. 
Most breaches are enabled 
by an insider taking an action 
that allows attackers access 
to sensitive or protected 
resources. The 2024 version 
of the annual Data Breach 
Investigations Report (DBIR) 
found that more than two-
thirds (68%) of breaches that 
occurred in 2023[^6] had “a non-
malicious human element.” 
A 2024 survey of 1,000 
employees found that a third 
(34%) worried that they would 
be the vulnerability exploited 
by attackers, even though the 
vast majority (86%) considered 
themselves knowledgeable 
about cybersecurity[^7]. More 
than half of respondents fear 
they would lose their job if 
they left their organization 
open to a cyberattack.  
FIVE
K-5
[^6]: Verizon Data Breach Investigations Report, 2024  
     https://www.verizon.com/business/resources/reports/dbir/#takeaways
[^7]: Why AI fuels cybersecurity anxiety, particularly for younger employees 
     https://www.ey.com/en_us/consulting/human-risk-in-cybersecurity   

## 4. The Threat Landscape <a name="threat-landscape"></a>
Detecting threats 
is their craft. Using 
echolocation, they 
emit high-frequency 
sounds that bounce 
off objects, giving 
them a detailed map 
of their surroundings. 
This helps them avoid 
obstacles, even in 
complete darkness. 
BAT
SPECIES
04

### 4.1 The Threat Landscape in Charts <a name="the-threat-landscape-in-charts"></a>
![Chart titles: IN CHARTS, TOP THREATS & CAMPAIGNS, MIMECAST RISK RADAR, MAJOR EVENT TIMELINE.  Image contains text: F. d3 Senso R V2527-A5 V2527-A5 Restore point f ield flow contro l p-34.34-3 fix PPO-399.3 W 41°24'12.2" E 23°44'54.4" PE-3 Nvgt B]
 
 
The threat landscape in the second half of 2024 
showed increasing use of consumer and business 
cloud services as a way for attackers to avoid 
detection. As a result, several major cloud services 
are being used to host attackers’ content, and links 
continue to grow as a mechanism for delivering 
payloads.  
 
In the second half of 2024, attackers shifted to 
focus on Arts, Entertainment & Recreation, Legal 
Services, and Software & SaaS sectors, a shift 
from the first half of 2024, when the Banking, 
Travel & Hospitality, and Arts & Entertainment 
industries topped the list of targets. While every 
industry encountered a significant number of 
bulk email attacks from low reputation sources, 
attackers targeted the Arts & Entertainment 
sector with more attacks using malicious files, and 
Legal Services encountered more attacks using 
impersonation. 
 
Read on to explore how Mimecast data analysis 
illustrates the threat landscape. 
The Threat  
Landscape  
in Charts.

![Chart 1: Most initial domains map to similar final domains, such as most attacks using Evernote initially, also hosting a payload there. Yet, there are a number of standouts, where one platform hosts the initial redirect page — such as a large volume of spam coming from marketing service GetResponse.com — and a second platform hosting the landing page, such as the training and webinar service Wave Compliance.  Chart contains the following data: Initial Domain, Attack Type, Resolved Domain.  Initial Domain: publuu.com, documents.adobe.com, gamma.app, indd.adobe.com, forms.gle, 1drv.ms, docsend.com, docs.google.com, evernote.com, app.getresponse.com, Other.  Attack Type: Compromised, Malware, Phishing.  Resolved Domain: documents.adobe.com, indd.adobe.com, gamma.app, online.publuu.com, onedrive.live.com, imspublishergroup.com, wavecompliance.com, docsend.com, evernote.com, docs.google.com, Other.]
Attackers are increasingly living off trusted services (LOTS) in their efforts 
to bypass defenses that rely on identifying attacks by spotting untrusted 
code, resources, and online services. While some choices to host attackers’ 
infrastructure are obvious — such as Google Docs, Evernote, and Dropbox 
DocSend — other online services are less well-known, such as interactive 
publication site Publuu, online webinar host Wave Compliance, and slide-
deck presentation site Gamma. 
 
Attackers also used specific platforms to send phishing emails and different 
sites to host the payload, which is often just a web form or file with a link. 
All-in-one marketing site GetResponse, for example, was a significant 
source of phishing emails — although many of those may not be malicious, 
just unwanted. While Adobe sites are not top hosts of payloads, at least two 
sites are used by attackers to host initial landing pages used by attackers. 
01
CLOUD SERVICE ABUSE

While spam continues to account for the vast majority of messages blocked 
by Mimecast in H2 2024, the summer saw a surge in Unwanted email 
messages. While that surge abated by the end of the year, phishing attacks, 
which typically include a URL to an attacker-controlled site or service, saw 
slow growth through the half. 
Mimecast classifies malicious and unwanted activity by the 
stage at which detection occurs. 
 
SPAM catches mass emails from non-trusted domains and those 
containing widely encountered content.   
SUSPICIOUS MESSAGES are potentially malicious messages, files 
or URLs; harmful content has not been detected, but indicators 
demonstrate the message should be treated with caution, such 
as if the message originates from a commonly abused service or 
a source with a low reputation. 
 
UNWANTED includes messages blocked by the user.  
PHISHING are threats designed to trick victims into revealing 
sensitive information, such as credentials or payment 
information. This includes phishing links, BEC, impersonation, or 
html attachments designed to impersonate login pages.  
MALWARE are those messages with attachments that are 
detected as malicious or links that lead to malware.
The significant increase in spam between the first and second halves of 
2024 is due to Mimecast’s evolving detection system and data collection, 
not a trend in spam volume. The increase in spam detections occurs 
because Mimecast added spam that was held by the gateway to the 
detection data, which can be configured by the administrator, rather than 
just high-confidence rejections. 
02
TPUS BY ATTACK TYPE

![Chart 2a: The significant increase in spam detections follows the integration of spam held at the gateway, as opposed to solely relying on spam rejections; this change also introduces an element of admin configurability in managing spam holds.  Chart contains the following data: Month, TPUs.  Months: 2023-10, 2023-11, 2023-12, 2024-01, 2024-02, 2024-03, 2024-04, 2024-05, 2024-06, 2024-07, 2024-08, 2024-09, 2024-10, 2024-11, 2024-12.  TPUs: Malware, Phishing, Spam, Suspicious, Unwanted.]
![Chart 2b: Removing the overwhelming influence of the spam dataset shows that Phishing is on the rise, and a surge in Malware attacks late in the second half of 2024. In December 2024, malware detection in Sub-Saharan Africa surged by 42.14%, significantly higher than the previous year, driven by political instability and increased cyber activity. Additionally, the region is witnessing a rise in ransomware attacks, which are becoming more opportunistic, often exploiting vulnerabilities and delivered as secondary infections, indicating a concerning trend in the threat landscape. Chart contains the following data: Month, TPUs.  Months: 2023-10, 2023-11, 2023-12, 2024-01, 2024-02, 2024-03, 2024-04, 2024-05, 2024-06, 2024-07, 2024-08, 2024-09, 2024-10, 2024-11, 2024-12.  TPUs: Malware, Phishing, Suspicious, Unwanted.]
Attackers tend to use different 
types of attacks to target different 
industries, giving each industry a 
distinctive threat profile. The Arts, 
Entertainment & Recreation sector 
— the top attacked industry after 
removing the large volume of spam 
— encountered the greatest number 
of threats per user (TPUs), with most 
attacks consisting of emails and 
messages with malicious payloads.  
 
The Professional Services: Legal 
and Media & Publishing sectors 
saw the next highest threat 
intensity, with each encountering 
nearly 9 TPUs. Attackers targeted 
Professional Services: Legal with a 
greater number of impersonation 
attacks, while Media & Publishing 
encountered a high number of 
malicious URLs. 
  
Every industry encounters a 
significant volume of spam as 
well as threats that are detected 
because of the attackers’ use of low-
reputation infrastructure. As part 
of the analysis, Mimecast removed 
bulk email messages — detected as 
Spam or Low Reputation — which 
accounted for 17 TPUs and 5 TPUs, 
respectively. 
03
TOP TARGETED 
INDUSTRIES BY TPUS

![Chart 3:  The threat profile for the Top-10 industries, without the Spam and Low Reputation categories since that tends to overwhelm the data. The TPU counts (x-axis) are in log format.  Chart contains the following data: Threat Intensity, Industries.  Threats: Blocked URL, Impersonation, Malspam, Malicious File, Credential Harvesting, Suspicious Content.  Industries: Arts, Entertainment & Recreation, Prof. Services: Legal, Media & Publishing, IT: Software & SAAS, IT: Other, IT: Resellers, Financial Services: Other, Construction, Telecommunications, Finance: Insurance.]
THREAT GROUPS
Attributing cyber threats is inherently complex, 
especially with the blended tactics many threat 
actors employ and the rise of cybercrime-as-a-
service models like Ransomware-as-a-Service 
(RaaS), Phishing-as-a-Service (PhaaS), and Initial 
Access Brokers (IABs). These services allow 
multiple threat actors to reuse the same tools 
and infrastructure, resulting in similar campaigns 
being launched by entirely different groups. 
Threat actors often employ a combination of 
techniques from different attack vectors and 
frequently change their methods, making it 
difficult to pinpoint a single actor or motive. 
 
Traditional attribution methods, which rely 
on infrastructure or malware signatures, are 
increasingly unreliable. Instead, Mimecast 
focuses on analyzing Tactics, Techniques, and 
Procedures (TTPs) to categorize and reference 
threat operations systematically. By tracking how 
attackers operate, we group threats and identify 
patterns across campaigns, even when traditional 
attribution methods fail. This approach provides 
a clearer and more reliable understanding of 
their evolving capabilities. The most prolific 
threat operations with Mimecast internal 
attribution names are highlighted below with 
related campaigns to describe their behaviors 
and potential impact. 
04
![Image contains text: V2527-A 5 PPO-399.3]

![Chart 5: The Top 10 vulnerabilities detected in messages, compared by EPSS and CVSS scores.  Two popular vulnerabilities are at least 10 years old. EPSS data collected as of 15 January 2025. Chart contains the following data: CVSS Score, EPSS Score, Age of Vulnerability (Years).  Vulnerabilities: Microsoft Office (CVE-2017-0199), Apache Commons Text (CVE-2022-42889), Microsoft Outlook (CVE-2024-21413), Apache Log4J (CVE-2021-44228), Microsoft Outlook (CVE-2023-23397), Microsoft Windows Server (CVE-2024-38213), Microsoft Lync (CVE-2012-1858), Microsoft Office (CVE-2017-11882), Microsoft Office (CVE-2018-0802), Microsoft Word (CVE-2014-1761).]
While the vast majority of attacks attempting to exploit software issues 
focused on two popular vulnerabilities (CVE-2017-0199 and CVE-2022-
42889), attackers attempted to exploit 89 different issues in the second 
half of 2024. Comparing the Top 10 vulnerabilities detected by Mimecast as 
part of an email or delivered as a link, seven issues have an Exploitability 
Prediction Scoring System (EPSS) score of at least 0.88 which equates to an 
88% chance of exploitation within the next 30 days, while two vulnerabilities 
— both discovered in 2024 — have yet to be registered as exploited. 
 
The mapping also shows the divergence of the EPSS score and the Common 
Vulnerability Scoring System (CVSS) score, which tends to correlate with the 
eventual severity of exploitation.
05
TOP VULNERABILITIES 
OVER TIME

### 4.2 Top Threats and Campaigns <a name="top-threats-and-campaigns"></a>
![Image contains text: W 41°24'12.2" E 23°44'54.4" PE-3 Nvgt B PPO-399.3]
OPEN SPOOFING
COPYRIGHT INFRINGEMENT/SUBSCRIPTION NOTIFICATION 
USER LINK COPY AND PASTE - ACCOUNT PAYABLE SCAM
TARGETED BEC SCAM WITH AUDIO DEEPFAKE
MISSING A DELIVERY
FACEBOOK ACCOUNT TAKEOVER 
01
02
03
04
05
06

Threat actors are leveraging compromised 
consumer routers as proxies to send 
large scale credential phishing campaigns 
through ISP email services obscuring 
their infrastructure and bypassing email 
authentication. By taking advantage of 
ISPs with weak or absent outbound email 
authentication threat actors achieve 
high-volume distribution and unrestricted 
sender spoofing capabilities.  
 
The affected ISPs identified from our 
investigation use email solutions such 
as Zimbra and MagicMail, and appear 
to not have robust outbound anti-spam 
measures. The combination of inadequate 
authentication and relaxed security 
controls enables attackers to achieve high 
sending rates and sustain large-scale spam 
campaigns without significant disruption.
OPEN SPOOFING
01
Consumer ISP routers 
exploited through 
vulnerabilities or weak 
passwords
Threat actor
Router configured to be 
used as a proxy 
Malicious links hosted on 
various cloud services
Phishing emails relayed 
through ISP mail servers
Prompted for M365 
username and password
Credentials harvested 
and user redirected to 
genuine M365 login page
READ ARTICLE
TECHNIQUE   Compromised consumer routers proxying spoofed phishing emails through ISP services
SERVICES USED   Zimbra, MagicMail 
TARGETS   Global - all industries

Malicious emails sent through Gmail via 
a mail-merge service are impersonating 
reputable law firms and claiming that 
companies are infringing copyrights. 
The email contains a direct Dropbox link 
or a redirect to Dropbox, which results 
in a download of a zip file containing an 
executable. The goal of the campaigns 
is to use various infostealers to steal 
sensitive information from infected 
machines such as credentials and 
financial details.  
 
Phishing email through 
mail merge service
Threat actor
Links to content hosted 
on Dropbox
Executable file downloads 
infostealer from Github
Download zip file 
containing executable file
Exfiltrates sensitive data
EXE
02
COPYRIGHT INFRINGEMENT/SUBSCRIPTION NOTIFICATION
READ ARTICLE
TECHNIQUE   Impersonating law firms with copyright notice bait for info stealing 
SERVICES USED   Gmail, Mail Merge 
TARGETS   Global, but primarily UK-based - retail, wholesale, travel, and hospitality industries

In their efforts to evade technical 
detection software and services, threat 
actors have moved on to convincing users 
to copy malformed links from an email 
— typically, they are missing the prefix 
“http://” — and paste those links in their 
browsers. The lures Mimecast analyzed 
usually included a button with a broken 
link and text that has some variation on: 
“If the link does not work, please copy and 
paste the link below.” 
 
This technique is in addition to other 
approaches to obfuscation, such as using 
QR codes to make links unreadable by 
humans and using scare tactics paired 
with phone numbers to prompt victims to 
call an attacker-operated call center. The 
goal of the current campaigns using this 
attack typically are to gather credentials 
from the victim. 
03
USER LINK COPY AND PASTE - ACCOUNT PAYABLE SCAM
Phishing email through 
AWS using Python 
mailer
Threat actor
User prompted to paste 
malformed URL into 
browser
Prompted for M365 
username and password
Redirects to a shared 
file hosted on a fake 
SharePoint
Credit card used or 
sold in underground 
marketplaces 
READ ARTICLE
TECHNIQUE   Convincing users to copy and paste a link to evade defenses 
SERVICES USED   Amazon Simple Email Service, Python mailers 
TARGETS  Predominately U.S - manufacturing, retail and legal industries

Employees in the Banking, Insurance, 
and other financial sectors are targeted 
with spear phishing emails that claim 
to be from a law firm and sent using a 
trusted service such as DocuSign and 
Adobe Sign.  
 
The targeted messages ask the 
employee to sign the NDA and then call 
a number purportedly from a law firm, 
but the number is controlled by the 
attacker. The threat actor impersonates 
the law firm using deepfake audio 
techniques to disguise their voice 
and sends an email from an attacker-
controlled domain that appears close to 
the impersonated law firm.  
Finally, the attacker will send an invoice 
purportedly from the law firm  
and follow up with a deepfake call that 
poses as their company CEO or another 
executive. 
 
04
TARGETED BEC SCAM WITH AUDIO DEEPFAKE
BEC email through 
Docusign or AdobeSign
Threat actor
User signs digital NDA​
Interaction via email 
results in invoice for 
payment
User calls fake number for 
NDA verification
Deepfake audio from 
executive confirming 
payment
Payment made to threat 
actor bank account
READ ARTICLE
TECHNIQUE   Audio deepfake, business email compromise (BEC) 
SERVICES USED   Adobe Sign, DocuSign 
TAGETED   Global - predominately financial sectors 

Messages sent through BIGLOBE, a 
Japanese service that is often abused by 
threat actors, target not-for-profit and 
housing organizations in the UK with 
messages that indicate a delivery has 
been missed.  
 
Threat actors take advantage of this and 
other ISPs by purchasing authenticated 
accounts through underground 
marketplaces, granting them legitimate 
access to their infrastructure and  
enabling them to send malicious emails 
that bypass most email authentication 
protocols. 
 
05
MISSING A DELIVERY
Phishing email through 
Biglobe ISP
Threat actor
Redirected to HTML file 
hosted on AWS
PII and credit card 
Information provided for 
updated delivery
HTML file impersonates 
EVRI missed delivery page
Credit card used or 
sold in underground 
marketplaces 
READ ARTICLE
TECHNIQUE   Living off trusted services (LOTS)  
SERVICES USED   S3 buckets on AWS to host HTML files 
TARGETS  UK - not for profit and housing industries 

A recent phishing campaign leveraged 
Recruitee, a legitimate third-party 
recruitment CMS to send fraudulent 
job offer emails. Threat actors register 
lookalike domains impersonating 
well-known brands to add credibility 
to the scam. The phishing pages use 
CAPTCHAs and IP filtering to deter 
automated detection and aim to 
harvest Facebook credentials.  
 
06
FACEBOOK ACCOUNT TAKEOVER — BRAND IMPERSONATION
Phishing email sent 
through Recruitee CMS​
Threat actor
Signup page on 
lookalike domain of 
impersonated brand​
MFA codes are required to 
complete application
Login via fake Facebook 
page to submit application
Facebook credentials 
obtained and shared via 
a Telegram logger
READ ARTICLE
TECHNIQUE   Job lure impersonating brands such as Victoria’s Secret, Red Bull and Coca- Cola   
SERVICES USED    Recruitee 
TARGETS   UK and US largely - predominately media & publishing and retail industries 

### 4.3 Mimecast Risk Radar <a name="mimecast-risk-radar"></a>
ATTACKERS INCREASINGLY LIVE  
OFF TRUSTED SERVICES (LOTS)  
From legitimate email providers to file-sharing 
sites to webinar-hosting services, attackers have 
extended their use of trusted services to bypass 
defenses that rely on reputation and trust. Attacks 
commonly use major email providers, such as 
Google’s Gmail and Microsoft’s Outlook (formally 
Hotmail), while links in email messages commonly 
terminate on a legitimate hosting service, such as 
Google Docs, Evernote, or Microsoft’s OneDrive 
and SharePoint services. 
 
As legitimate services find ways to deter abuse, 
attackers are also branching out to smaller 
providers. Major campaigns tracked by Mimecast, 
for example, used providers, such as Airtable, 
Publuu, and Wave Compliance.  
mimecast 
Risk  
Radar.
04
.3
24 0

GEOPOLITICAL RISKS RISE  
As geopolitical tensions rise worldwide, the threat landscape is changing. 
Cyber attackers have become more active, using the cyber domain for 
intelligence