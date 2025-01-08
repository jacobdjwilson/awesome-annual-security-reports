# 2024 Technology Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Third-Party Supplier Risk](#third-party-supplier-risk)
- [Speed vs. Security](#speed-vs-security)
- [Rise of Ransomware](#rise-of-ransomware)
- [Dissecting the Attack Flow for the Technology Sector](#dissecting-the-attack-flow-for-the-technology-sector)
- [Attack Flow Overview](#attack-flow-overview)
- [Attack Flow Steps](#attack-flow-steps)
- [Initial Foothold: Phishing, Spam & Scams](#initial-foothold-phishing-spam--scams)
- [Initial Foothold: Logging in](#initial-foothold-logging-in)
- [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
- [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
- [Initial Payload](#initial-payload)
- [Expansion / Pivoting](#expansion--pivoting)
- [Malware: Loaders, Infostealers and RATs](#malware-loaders-infostealers-and-rats)
- [Malware: Ransomware](#malware-ransomware)
- [Exfiltration / Post Compromise/Impact](#exfiltration--post-compromiseimpact)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
- [Threat Groups](#threat-groups)
- [8BASE](#8base)
- [ALPHV / BlackCat](#alphv--blackcat)
- [Akira](#akira)
- [BlackBasta](#blackbasta)
- [CLOP/Cl0p](#clopcl0p)
- [LockBit 3.0](#lockbit-30)
- [Medusa](#medusa)
- [Play](#play)
- [STORMOUS](#stormous)

T R U S T W A V E  T H R E A T  I N T E L L I G E N C E 
B R I E F I N G  A N D  M I T I G A T I O N  S T R A T E G I E S 

MARCH 2024

## Executive Summary
The technology industry is synonymous with innovation, 
harboring a wealth of intellectual property and invaluable 
user data. Yet, amidst the promise of progress, lurks the 
menacing threat of cyberattacks.

These attacks can be devastating. Beyond disrupting core operations and 
causing financial losses, they can expose sensitive user data, intellectual 
property, and trade secrets. This not only damages a company's reputation 
but also erodes user trust, a critical component in today's tech-driven world.

Recent breaches illustrate the severity of the threat. In December 2022, a 
cyberattack on LastPass, a password management company, compromised 
the password vaults of millions of users. In October 2023, hackers stole data 
from US access and identity management giant Okta on its entire client base 
during a breach of its support systems.

There are a number of factors that make the technology industry especially 
vulnerable to cyberattacks, including:
	
- **Large Attack Surface**: 
The rapid digital transformation and technological 
progress within the technology sector have notably enlarged the attack 
surface for companies operating in this space. As the sector evolves, 
the proliferation of Software-as-a-Service (SaaS) providers, cloud 
infrastructure, and internet-connected systems and devices continues 
to grow. This growth often occurs at a rate that outstrips the deployment 
of adequate security measures, such as the inability to keep track of and 
remediate vulnerabilities, which not only exposes the company but also 
their clients.
	
- **Complex Supply Chains**:
 In most cases, technology companies are the 
third parties and possibly the root cause of most supply chain attacks. 
Additionally, certain technology sub-sectors like software companies and 
infrastructure providers have complex supply chains, making it difficult to 
ensure the security of all components and services.
	
- **High-Value Data**: 
Technology companies such as Telcos, SaaS providers, 
and hosting companies are prime targets for cyber threats due to their 
possession of large volumes of sensitive and valuable data. This high-
value data is attractive to threat actors for financial gain, espionage, or 
other malicious motivations.
	
- **Communications Backbone**: 
Telcos and Internet Service Providers (ISPs) 
are prime targets for cyber threats due to their importance in providing 
access and connectivity services. This exposure significantly increases 
their risk of being targeted by Distributed Denial of Service (DDoS) and 
other forms of disruptive attacks by nation-state threat actors.
	
- **Technology Savvy and Mobile/Remote Workforces**: 
The shift towards 
mobile and remote workforces in the technology sector introduces unique 
challenges, notably the use of personal devices for work and insecure 
home networks. The nature of the workforce also tends to expose 
personnel to more specific technology-oriented phishing and social 
engineering attacks.

The technology industry is incredibly broad. Therefore, for this research, 
we focused on two key areas: technology infrastructure and software 
technology.
	
- Technology infrastructure includes Internet Service Providers (ISPs), 
telecommunications companies (telcos), and cloud services. These 
elements provide the foundation for the digital world, enabling 
communication and data storage. 
	
- Software technology encompasses the development, creation, 
deployment, maintenance, and support of software applications. This 
includes everything from the operating systems that power our devices to 
the apps we use daily.

With hundreds of security researchers across the globe, the Trustwave 
SpiderLabs team puts its resources to task in looking into what leads to these 
breaches. We are uniquely positioned to do so, as we perform over 200,000 
hours of penetration tests and uncover tens of thousands of vulnerabilities 
annually. We also have a dedicated email security team analyzing millions 
of phishing URLs validated daily, including 4,000 to 10,000 per day that are 
uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec 
disciplines, including Continuous Threat Hunting, Forensics and Incident 
Response, Malware Reversal, and Database Security, gives us insight into 
identifying how these breaches occur as well as mitigations and controls that 
your organization can put in place to prevent these compromises. 

We will begin by highlighting the significant trends currently affecting the 
industry: third-party supplier risk, innovation speed versus security, and the 
rise of ransomware. Subsequently, we will analyze the attack flow specific to 
the technology industry, offering insight on specific threat actors, actionable 
intelligence, and recommended mitigations for each stage to illustrate how 
organizations can proactively identify and prevent attacks to avoid lasting impact. 

In this report, we will examine many of the most prevalent threat tactics and 
threat actors operating across technology and throughout the attack chain, 
including:  

**THREAT ACTORS** 
	
- LockBit 3.0
	
- CLOP/Cl0p
	
- ALPHV / BlackCat
	
- Play
	
- Akira
	
- 8BASE
	
- Medusa
	
- Mont4na
	
- STORMOUS
	
- BlackBasta 

**THREAT TACTICS** 
	
- Phishing and Business Email 
Compromise (BEC)
	
- AI-Driven Malicious Email 
Campaigns
	
- Special Phishing Themes (IOT – 
Ring Phishing, Cryptocurrency 
Phishing)
	
- Scam Campaigns
	
- Data Brokers and Access Brokers
	
- Malware
	
- Exploitable Vulnerabilities
	
- Misconfigured Applications and 
Services
	
- DDOS Attacks
	
- Third-Party Supplier Risk

For additional information about the most prevalent threat actors, please go 
to the Appendix. 

## Emerging and Prominent Trends
## Third-Party Supplier Risk
The Threat

Supply chain attacks are on the rise, but instead of brute-forcing their way into 
major companies, attackers are targeting a weaker link: the trusted third-party 
vendors these companies rely on. This tactic is like a domino effect, where 
compromising one vendor can bring down a cascade of businesses. 

These third-party vendors are attractive targets because they might have 
weaker cybersecurity defenses. Attackers can exploit these gaps to gain 
access to the data of the larger companies that use them. Unpatched 
vulnerabilities and lax data breach protocols leave these vendors wide open, 
posing a significant threat to the entire tech industry. 

The recent surge in supply chain attacks and the high-profile breaches 
they've caused highlight the significant potential rewards for attackers. This 
trend underscores the need for stricter security measures across the entire 
technology supply chain. 

**What Trustwave SpiderLabs Is Seeing**

What makes supply chain attacks especially risky in tech is that unlike other 
industries, many tech companies are both suppliers and consumers. Their 
products and services become building blocks for even larger systems, which 
can introduce security vulnerabilities. This gets even trickier because tech 
companies themselves often rely on numerous third-party technologies. 

This interconnectedness is particularly worrisome for subsectors with 
complex supply chains, like software publishers and infrastructure providers. 
Recent attacks on Kaseya, MOVEit, SolarWinds, and 3CX show how a single 
compromised vendor can disrupt entire industries. In our later supply chain 
section, we analyze notable examples of supply chain attacks and root 
causes. 

**Mitigations to Reduce Risk**
	
- Conduct security assessments before working with vendors and 
provide accurate security information if you're a vendor. 
	
- Include strict security clauses in contracts, requiring regular audits, 
breach notifications, and data protection compliance. 
	
- Regularly audit vendor security practices and conduct vulnerability 
assessments and penetration testing. 
	
- Enforce access controls, change control, and security checks 
throughout development pipelines. 
	
- Encrypt sensitive data at rest and in transit, implement least 
privilege access, and monitor access logs. 
	
- Ensure both parties comply with relevant data privacy regulations 
based on location and data type. 
	
- Provide regular training on cybersecurity hygiene to empower 
employees to defend against attacks. 

## Speed vs. Security
The Threat

The tech industry's relentless pursuit of innovation can sometimes come at 
the expense of security. The rush to market with new features, like Artificial 
Intelligence (AI), can lead to shortcuts, like integrating untested components. 
These components haven't been rigorously evaluated for vulnerabilities, 
leaving potential backdoors for attackers. Imagine a new car with a powerful 
engine, but faulty brakes. It might be fast, but it's also incredibly dangerous. 

Strong security shouldn't be an afterthought. It needs to be integrated 
throughout the entire software development lifecycle. Patching vulnerabilities 
later is a much more difficult and expensive process, like trying to reinforce a 
house with a shaky foundation. 

**What Trustwave SpiderLabs Is Seeing**

For example, SpiderLabs identified a case where an AI chatbot exposed 
sensitive data due to incomplete testing. This highlights a broader issue: AI 
is being integrated into software without thorough analysis of its security 
implications. 

Strong security practices throughout the development lifecycle are crucial. 
Catching vulnerabilities during coding and testing is much easier than fixing 
them later. Patching a product built on insecure components is a major 
challenge, as shown by the continued use of outdated and vulnerable 
packages in software repositories like npm. 

While AI offers tremendous potential, security concerns remain. Another 
example involves users exploiting a car dealership's AI chatbot to access 
irrelevant information. These "business logic flaws" are often undetectable by 
traditional security testing tools and require specialized testing approaches 
that consider the specific logic behind the AI component. 

**Mitigations to Reduce Risk**
	
- Integrate security practices into every stage of the Software 
Development Lifecycle (SDLC), from initial design through coding, 
testing, deployment, and maintenance. 
	
- Identify and assess potential security threats early in the 
development process. 
	
- Train developers in secure coding practices to minimize 
vulnerabilities introduced during coding. 
	
- Utilize automated tools to scan code for vulnerabilities throughout 
development. 
	
- Conduct regular penetration testing to identify and exploit 
vulnerabilities before attackers do. 

## Rise of Ransomware
The Threat

Tech firms are prime targets for a particularly nasty breed of ransomware. 
This malware not only encrypts or locks data, demanding a ransom for 
access, but also actively tries to erase backups and shadow copies, 
hindering recovery efforts.

Modern ransomware gangs have upped the extortion game. They steal 
sensitive data before deploying the ransomware, then publicly expose it to 
pressure victims into paying.  Even if the ransom isn't paid, these attackers 
hold onto the data, potentially selling it on the Dark Web. This "double 
extortion" tactic adds another layer of pressure on tech companies.

**What Trustwave SpiderLabs Is Seeing**

Ransomware attacks surged in the tech industry in 2023, with Trustwave 
tracking over 1,000 claims. LockBit 3.0, ALPHV, and CLOP (CL0P, Cl0p) were 
among the top culprits, targeting a wide range of tech companies across 
North America, Europe, and Asia. These attacks spanned various sectors 
within tech, including telecommunications, software, cybersecurity, media 
and broadcasting, and IT services. 

![Figure 1: Top 10 ransomware groups in the technology sector]

While activity fluctuated throughout the year, a significant spike occurred 
in June-July 2023, likely linked to the exploited MOVEit vulnerability (CVE-
2023-34362). We’ll go into more depth on these ransomware groups and 
their activity in a later section dedicated to ransomware. 

**Mitigations to Reduce Risk**
	
- Combine host-based anti-malware with strong email security 
(filtering, user training) to block common attack vectors. 
	
- Create and test an incident response plan for responding to 
ransomware attacks, including data backups for recovery. 
	
- Enable and monitor logs on critical systems and networks to 
detect suspicious activity. 
	
- Actively monitor underground sources to identify potential data 
leaks. 
	
- Restrict user access to only the data they need to perform their 
jobs. 
	
- Utilize multiple security tools and strategies from different vendors 
to create a multi-layered defense. 

## Dissecting the Attack Flow for the Technology Sector
## Attack Flow Overview
While the specifics and details of every breach and compromise may vary, 
there is typically a specific attack flow that occurs from the initial security 
bypass to escalation, compromise, followed by persistent home on your 
network and exfiltration and/or destruction of valuable data. The following 
analysis presents an overview of the attack flow specific to the technology 
sector, incorporating insights from the Trustwave SpiderLabs team and 
offering actionable mitigations for organizations to implement. 

At each stage of the attack flow, the recommended mitigations provide 
proactive guidance to minimize the potential risks of financial, reputational, 
regulatory, or physical impacts to a technology-oriented organization. The 
typical sequence of events unfolds as follows:

## Attack Flow Steps
**Initial Foothold**

This is the step where the attacker successfully triggers a security bypass 
that will give them the ability to expand their access to suit their motives and 
goals. This initial foothold can take various forms, ranging from successful 
phishing attacks to vulnerability exploitation or even logging into public-
facing systems using previously acquired credentials.

In this section, we will explore the most common methods through 
which attackers gain this initial foothold into a technology organization, 
like phishing, third-party suppliers, and exploitable vulnerabilities.

**Initial Payload**

Once the attackers have established a foothold on the network, they will 
proceed to download more sophisticated tools and malware.

In this section, we will specifically concentrate on real-world 
examples of the types of payloads that frequently target 
technology companies.

![Attack Flow Diagram]

**Expansion / Pivoting**

The initial foothold typically involves a low-value workstation, such as a 
phishing victim's laptop, or a network appliance like a VPN endpoint.  

In this section, we will showcase how once armed with the 
necessary tools, attackers can target higher-value accounts and 
systems, such as domain admins, root accounts, active directory 
systems, and database servers.

**Malware**

There are a variety of malware types with a myriad of uses, such as Remote 
Access Trojans (RATs), infostealers, ransomware, and many others. 

In this section, we will focus on the types of malware pervasive in 
the technology sector.

**Exfiltration / Post Compromise**

In most cases, the primary motive behind compromises is data theft. 

In this section, we will explore the types of data that are targeted 
and exfiltrated in technology sector compromises. Additionally, 
we will present real-world examples of technology-related data 
breaches to provide concrete illustrations.

## Initial Foothold: Phishing, Spam & Scams
The Threat

Like many industries, phishing is the most exploited method for gaining 
an initial foothold in organizations in the technology sector. Instead of 
attempting to exploit vulnerabilities in the software or systems on the 
network, attackers target staff, contractors, or others who have access to 
systems within the organization that can be exploited, such as financial 
databases, customer databases, etc.

In a typical scenario, the attacker crafts a compelling email, skillfully 
persuading the recipient to engage in certain actions. This could include 
opening an attachment, clicking a link, or executing specific instructions. 
Typical phishing goals: 
	
- **Credential Theft**: 
An example of this would be an email that appears to be 
from the company's admin, containing a link. When the recipient clicks this 
link, they are prompted to enter their login details under the pretense of 
accessing important information or job opportunity details.
	
- **Malware Insertion**: 
This is often executed through embedding PowerShell 
scripts, JavaScript, or enabling Macros in a document.
	
- **Triggering Specific Actions**: 
This could involve convincing the recipient to 
provide confidential information or perform other actions under the guise 
of a necessary step for a certain request.

**Trustwave SpiderLabs Insights**

The Trustwave SpiderLabs team is committed to monitoring various email-
based threats, such as opportunistic phishing, spearphishing, spam-based 
malware, and scams. In the past year, our team has noted interesting 
developments in the tactics and delivery approaches used in email-based 
attacks within the technology sector. These advancements have played 
a role in sustaining the continuing significance and effectiveness of these 
types of attacks.

In the technology sector, the top three email attachment file types (Fig 2) 
commonly received by clients are HTML, Executables, and PDFs similar to 
other sectors. Around 60% of HTML attachments contain credential phishing 
pages or malware downloaders, while 25% are executables containing RATs 
concealed in archive containers. PDFs often disguise scams, with about 37% 
impersonating brands like Geek Squad, PayPal, and Mcafee. 

![Figure 2: Top malicious attachment filetypes for the technology sector]

Phishing campaigns targeting technology-related customers frequently 
abuse URL categories such as InterPlanetary File System, Google Services, 
Cloudflare Services, compromised WordPress sites, and free web/app 
hosting services, leveraging trusted domains to distribute malicious content 
or set up fake login pages. This vector is further exacerbated by making 
phishing infrastructure readily available to threat actors as highlighted in 
original Trustwave SpiderLabs research about the Greatness Phishing Kit and 
the Tycoon Phishing-as-a-Service System. 

In the technology sector, Trustwave researchers have observed several 
notable phishing campaign themes, including: 

**ARTIFICIAL INTELLIGENCE-DRIVEN BEC AND PHISHING CAMPAIGNS**

2023 marked the breakout year for generative artificial intelligence (Gen AI), 
a form of artificial intelligence capable of generating new text, media, and 
source codes. With tools like ChatGPT, DALL-E, Synthesia, and others, Gen AI 
experienced explosive growth in both creative and malicious applications. 
There's a growing concern over Gen AI's ability to craft sophisticated email 
attacks highlighted by the emergence of WormGPT and FraudGPT which 
are Large Language Models (LLMs) similar to ChatGPT, but lacking security 
constraints. For example, Trustwave SpiderLabs researchers have been 
observing the growing frequency of potentially AI-generated (BEC) emails 
(Fig 3) to our clients’ inboxes such as these:

![Figure 3: Example of a possible AI-generated BEC email]

Our researchers tested this email against multiple AI text content detectors 
and tools (GPTZero, Copyleaks, ZeroGPT, Quillbot) to identify AI content (Fig 
4) in the message. Below is the result from ZeroGPT:

![Figure 4: Highlighted in yellow is ZeroGPT’s prediction of what were the AI-generated text 
from the message body of the BEC email]

Based on the result, almost the entire BEC message is most likely AI 
generated. In another example, this time from a Human Resources (HR)-
themed phishing and malware spam campaign (Fig 5) targeting a technology 
company, our researchers tested if the phishing campaign was AI generated: 

![Figure 5: An HR-themed phishing campaign suspected of being AI generated]

As suspected, the results show that the text used for this phishing campaign 
is predominantly AI generated. Traditionally, tech-savvy personnel, especially 
those in the technology sector, have been more cognizant of the indicators 
for identifying phishing attempts such as grammatical errors and spelling 
mistakes. With the advent of AI-generated text, phishing emails have the 
potential to significantly enhance the effectiveness of phishing campaigns. 

![Figure 6: Analysis of the text of the HR phishing campaign shows the text being 
predominantly AI generated]

Aside from AI-generated phishing text, our researchers also observed 
the increasing frequency of using AI services as lures. This is particularly 
important considering the tech savvy nature of the targets in the technology 
sector. One such example is this malicious email written in Dutch (Fig 7) that 
our team has recently observed:

![Figure 7: Scam email written in Dutch using an AI service as a lure]

Translation of the email (Fig 8) reveals that it is a scam that offers recipients 
the opportunity to make easy money through "Quantum AI," an alleged stock 
trading platform associated with Elon Musk. This scam extends beyond 
emails, as a deep fake video of Musk promoting the platform circulated on 
social media, falsely claiming high returns with minimal risk. These fabricated 
emails and videos attempt to trick individuals into investing in a financial 
scam.

![Figure 8: Translated email enticing recipients to invest in ”Quantum AI”]

Lastly, our researchers also noted the increasing use of AI-Powered SaaS 
Marketing Platforms for sending unsolicited marketing emails. One example 
that our team has observed lately is Kalendar AI, a Software-as-a-Service 
(SaaS) platform that automates sales outreach on behalf of companies. 
Their AI technology can write personalized invitations (Fig 9) to prospective 
customers as seen in this example:

![Figure 9: Sample of an unsolicited marketing email crafted through Kalendar AI]

Though not necessarily malicious, this could easily progress from unsolicited 
marketing emails to full blown malicious email campaigns due to the ease in 
creating and distributing personalized email campaigns through AI-driven 
services such as these.

**SOFTWARE DEVELOPMENT AND CODING PLATFORMS AS PHISHING URLS**

In the technology sector, platforms like Codesandbox.io provide developers 
with a convenient way to create and collaborate on web projects in the 
cloud. However, our researchers have observed that these platforms are also 
targeted by threat actors who abuse them for malicious purposes. In the 
example below (Fig 10), we can see that threat actors utilize these services 
such as Code Sandbox to host phishing login pages or redirection scripts:

![Figure 10: Phishing attack leveraging Code Sandbox URL]

Additionally, platforms like Replit and GitHub, which provide collaborative 
coding environments, have also been leveraged by threat actors to conduct 
phishing attacks. Replit (Fig 12) offers an online IDE for coding projects, while 
GitHub (Fig 11) serves as a platform for version control and collaboration 
in software development. Our team has seen both platforms vulnerable to 
abuse by threat actors who host phishing login pages or redirection scripts in 
their environment.

![Figure 11: Phishing attack leveraging Github URL]

![Figure 12: Phishing attack leveraging Replit URL]

**FAKE ORDER OR TECH SUPPORT SCAM**

During this research, our researchers noted a preponderance of lures 
attempting to leverage technology-related services to steal data or trick 
victims into installing malware on their devices. 

Fake order or tech support scams are fraudulent emails about product or 
service purchases that were never initiated by the recipient. These aim 
to trick recipients into cancelling the supposed order by clicking a link or 
contacting a provided phone number. A new variant of this type of scam uses 
the Google Groups platform to send malicious messages to the target inbox. 
Figure 13 is a legitimate Google Groups notification stating that the recipient 
has been added to a bogus Geek Squad group.

![Figure 13: A legitimate Google Groups notification for a purported client support service 
for Geek Squad]

These scams exploit Google Groups' Conversations feature, where members 
can interact through posts and replies. Threat actors automatically add email 
addresses to groups and then initiate spamming by creating conversation 
posts containing counterfeit order confirmation (Fig 14) receipts from entities 
like Geek Squad. A more in-depth look into these types of scams can be 
referenced in Trustwave SpiderLabs original research about the rise of 
Google Group Fake Order Fraud. 

![Figure 14: A Geek Squad-themed fake order scam]

**SINGLE EURO PAYMENTS AREA (SEPA) TRANSFER THEMED BEC**

The Single Euro Payments Area (SEPA) serves as an important payment 
integration system for cross-border bank transfers denominated in Euros. 
As the global nature of the technology sector requires global financial 
transactions, SEPA offers a streamlined mechanism for digital payments 
across European borders. 

However, the sector is not immune to exploitation by threat actors seeking 
to leverage these payment systems. Our researchers observed a recent 
string of BEC attacks targeting European users within the technology sector 
leveraging SEPA to orchestrate fraudulent transactions. These attacks involve 
the use of templated content written in multiple languages (Fig 15) which 
indicates a targeted and sophisticated approach. 

![Figure 15: SEPA-themed BEC written in multiple languages]

All three samples translate to the same English paragraph (Fig 16):

![Figure 16: Original English text of the SEPA-themed BEC]

The threat actors who crafted these emails most likely wrote the original 
email in English and translated it to the respective languages of their targeted 
institutions to make the emails look more legitimate.

**QUISHING - PHISHING WITH QR CODES**

Personnel in the technology sector are generally more tech savvy and are 
more likely to use technologies such as QR codes. Of note are attack vectors 
like "Quishing," which is a type of phishing attack that leverages these QR 
codes. This technique involves embedding a malicious URL within a QR code 
which when scanned, redirects the target to a phishing site. 

Trustwave SpiderLabs researchers have observed a notable increase in 
phishing campaigns utilizing this method in 2023. These “weaponized” QR 
codes are commonly found embedded within email message bodies or 
enclosed within PDF files. This attack is investigated in depth in Trustwave's 
SpiderLabs original research tackling the rise of QR codes in phishing.

![Figure 17: Examples of “Quishing” attacks]

**CRYPTOCURRENCY PHISHING CAMPAIGNS**

While there is no universal rule, it has often been observed that individuals 
working in the technology sector are more likely to use cryptocurrencies 
compared to those in other industries. Phishing attacks have increasingly 
targeted crypto users to obtain critical information about their digital wallets. 
One particularly important piece of information that threat actors attempt 
to obtain is the recovery phrase, which is a sequence of words essential for 
accessing cryptocurrency stored in a wallet. 

Trustwave SpiderLabs researchers have observed a trend in recent phishing 
campaigns where phishing messages (Fig 18 and Fig 19) specifically try to 
obtain these recovery phrases from targeted users. These phishing attempts 
often take the form of emails containing HTML attachments designed to 
replicate pages of legitimate cryptocurrency providers. 

![Figure 18: Cryptocurrency phishing example targeting Coinbase users' recovery phrases]

![Figure 19: Cryptocurrency users targeting Blockchain.com users recovery phrases]

Aside from recovery phrases, other common themes that were observed by 
our team in these phishing messages include promises of Bitcoin refunds, 
prompts for wallet recovery, and fraudulent claims of Bitcoin fund transfers. 

**INTERNET OF THINGS (IOT) – RING PHISHING CAMPAIGN**

Trustwave SpiderLabs researchers have noted that threat actors have 
recently launched an email phishing campaign impersonating Ring Doorbell, 
a home security system owned by Amazon. This is particularly interesting as 
this leverages an IoT alert to trick targets into providing sensitive information. 
The email warns recipients of an impending suspension of their Ring account, 
citing outdated membership information. An example email received by 
one of our clients showcases this fraudulent tactic. The phishing message 
includes an HTML file attachment housing a malicious link. Upon clicking, 
recipients are directed to a counterfeit Ring login page designed to illicitly 
harvest sensitive information, including credentials, social security numbers, 
and credit card details.

![Figure 20: Phishing sample mimicking a Ring email notification]

![Figure 21: Malicious HTML attachment included in the ring notification]

**CREDENTIAL PHISHING UTILIZING FORM SERVICES**

Trustwave SpiderLabs researchers have observed threat actors using online 
form services for credential phishing in our technology sector clients. These 
threat actors craft phishing pages and direct form submissions to services 
like ActionForms, FormBackend, Formspark, Formspree, and Formester (Fig 
22).

![Figure 22: Credential phishing example using Formester]

**Mitigations to Reduce Risk**
	
- Conduct security awareness sessions to educate employees about 
the latest phishing tactics and techniques. This should include 
"Quishing," IoT alert phishing, and online form services phishing. 
	
- Be vigilant about the increasing sophistication of phishing emails 
due to AI and LLM technologies, which can create more convincing 
and error-free scam messages. Consider utilizing artificial 
intelligence and machine learning-based tools to detect AI-
generated phishing emails and content. 
	
- Educate personnel on the importance of protecting cryptocurrency 
digital wallets, particularly the safekeeping of recovery phrases.
	
- Consistently conduct mock phishing tests to assess the 
effectiveness of anti-phishing training and retrain repeat offenders. 
	
- Implement robust anti-spoofing measures, including deploying 
technologies on email gateways. Deploy layered email scanning 
with a solution like MailMarshal to provide better detection and 
protection.
	
- Leverage web filtering and categorization technologies to block 
access to malicious websites, particularly compromised WordPress 
sites, and free web and app hosting services that are frequently 
used for distributing phishing content.
	
- Utilize techniques to detect domain misspellings, enabling the 
identification of phishing and BEC attacks.
	
- Perform routine security audits of IT applications and infrastructure 
to identify and rectify vulnerabilities that could be exploited in 
phishing campaigns.
	
- Enable multi-factor authentication (MFA) to provide an additional 
layer of protection for accounts.
	
- Restrict the access of assets and sensitive data with the principle of 
least privilege in mind.
	
- Establish strict verification processes for financial transactions such 
as cross-border payments like SEPA transfers that was mentioned in 
this section that could lead to BEC attacks.

> When layered, captures up 
> to 90% of malicious emails 
> missed by other email 
> security vendors.

## Initial Foothold: Logging in
The Threat

Threat actors can infiltrate an organization's network in various ways, 
including straightforward methods like using login credentials. This might 
happen if default device credentials remain unchanged, or if weak passwords 
are susceptible to brute-force attacks. But typically, threat actors gain access 
through methods like phishing, drive-by downloads, leveraging vulnerabilities 
in applications, or purchasing pre-established access to a target organization 
from various access brokers. 

**Trustwave SpiderLabs Insights**

As discussed in the previous section (Initial Foothold: Phishing, Spam 
& Scams), phishing is the most widespread tactic to gain initial access 
to organizations, with attackers focusing not on software or system 
vulnerabilities, but rather on manipulating the individuals. Other common 
techniques used by threat actors are leveraging valid accounts such as 
through access brokers and exploiting vulnerabilities (Fig 23).  

![Figure 23: Initial access techniques observed by Trustwave in our technology client base]

**VALID ACCOUNTS AND ACCESS BROKERS**

Trustwave researchers continually observe the trade of valid accounts 
and access credentials pertaining to data, networks, and systems on the 
Dark Web. Initial Access Brokers, which have been active in underground 
marketplaces and forums, were seen offering unauthorized access to various 
technology-related companies. In the example below (Fig 24), a threat actor 
is claiming that they have SSH access to the subdomains and CI/CD tools of 
an American ISP that has a net worth of $180 billion. 

![Figure 24: Threat actor claiming to SSH/administrator access to an American ISP]

Another post from a threat actor (Fig 25) in an underground forum shows 
access being sold to an ISP in Brazil. The threat actor claims that they have 
access to the backup infrastructure of the organization. 

![Figure 25: Threat actor claiming to have access to a Brazilian ISP]

Based on Trustwave threat hunting engagements for technology 
organizations, our researchers also observed that threat actors are often able 
to obtain valid accounts due to a company's inadequate management of user 
accounts, including local and default administrative accounts, as well as local 
administrator groups and default guest accounts.

Additionally, our threat hunts have also discovered that a significant portion 
of our cases involve unsecured credentials. Aside from custom scripts, we 
noted in our engagements that third-party remote access tools such as 
mRemoteNG and Tera Term Pro contain extractable credentials that can be 
used for initial access or for further lateral movement. 

**EXPLOITING PUBLIC-FACING APPLICATIONS**

The technology sector has a high exposure to public-facing exploits due to 
the nature of their operations as these organizations host and manage vast 
amounts of sensitive data across cloud services, data centers, and network 
infrastructure. 

With the ongoing shift towards remote management, automation, and 
the widespread use of IoT devices and SaaS platforms, the sector's 
attack surface has dramatically increased. In a recent Shodan review, 
our researchers noted over 12 million exposed devices (Fig 26) under the 
technology category. Note that this number does not include major cloud 
servers hosted by Microsoft, Amazon, Google etc.

![Figure 26: Publicly accessible devices in the technology sector]

In the next section, we will explore the implications of this exposure and 
how threat actors might use this attack surface to gain initial access through 
vulnerabilities and exploits. 

**Mitigations to Reduce Risk**
	
- Ensure that proper security controls are in place