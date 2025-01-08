# 2024 Education Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Shift Towards Online Education](#shift-towards-online-education)
- [Third-Party Security Risks](#third-party-security-risks)
- [Ransomware Attacks](#ransomware-attacks)
- [Dissecting the Attack Flow for the Education Sector](#dissecting-the-attack-flow-for-the-education-sector)
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
- [Akira:](#akira)
- [ALPHV aka BlackCat:](#alphv-aka-blackcat)
- [Bl00dy Ransomware:](#bl00dy-ransomware)
- [Clop or Cl0p:](#clop-or-cl0p)
- [LockBit 3.0:](#lockbit-30)
- [Medusa:](#medusa)
- [No Escape:](#no-escape)
- [Pirat-Networks:](#pirat-networks)
- [Rhysida:](#rhysida)
- [Royal:](#royal)
- [Vice Society:](#vice-society)

T R U S T W A V E  T H R E A T  I N T E L L I G E N C E 
B R I E F I N G  A N D  M I T I G A T I O N  S T R A T E G I E S 

## Executive Summary
“So many of our schools across the nation are, what we call, 
‘target rich, cyber poor’ in that they are often a frequent 
target for ransomware and other cyberattacks due to the 
extensive data kept on school networks, often without 
the proper protection,” stated the Cybersecurity and 
Infrastructure Security Agency (CISA), aptly summarizing 
the concerning state of cybersecurity in education.

Primary school systems handle sensitive data concerning minors, while 
higher education institutions must safeguard intellectual property data, 
making them prime targets for cyberattacks. These attacks not only threaten 
the safety and security of teachers and administrators, but they put the 
privacy of students, staff, and other associated entities at risk.

With millions of students now learning through technology in hybrid, remote, 
or in-class settings, device security is no longer optional. It's crucial to ensure 
a safe and secure learning environment for everyone. Strong cybersecurity 
measures not only protect student data but also enable teachers to do their 
jobs effectively without fear of disruptions or data breaches.

These disruptions directly contradict the sector's core mission of fostering 
knowledge and development. As a result, educators and administrators are 
facing heightened concerns about cyber resilience – and recent breaches 
illustrate the risks.

In May 2022, Illinois’ Lincoln College was forced to permanently shut down 
due to the impact of a ransomware attack. In March 2021, the Buffalo Public 
Schools District was hit by a ransomware attack and as a result, spent nearly 
$10 million on network security, fraud monitoring and other services. In June 
2023, The University of Manchester, which has over 10,000 staff and 45,000 
students, confirmed it had been successfully attacked, and data belonging to 
alumni and current students was accessed and removed.

There are a number of factors that make the education industry especially 
vulnerable to cyberattacks, including:
	
- **BYOD Dilemma:** The "Bring Your Own Device" culture poses security 
challenges by adding unmanaged devices to the network, straining 
IT resources.
	
- **Complex Infrastructure:** Diverse devices, decentralized IT management, 
and inconsistent security practices create a sprawling attack surface with 
vulnerabilities.
	
- **Data Trove:** Huge volumes of sensitive student data (PII, research, IP) 
attract attackers seeking data breaches and identity theft, amplified by 
online collaboration and open internet access.
	
- **Exposed Systems & Services:** Publicly accessible network devices like 
servers, building management systems, access systems, and cameras lack 
proper security, increasing risk.
	
- **Resource Scarcity:** Limited budgets hinder investments in cybersecurity 
software and staff, leaving critical systems under-protected.
	
- **Legacy Risks:** Outdated IT systems remain vulnerable to exploitation due 
to lack of updates and security patches.

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
industry: the shift towards online education, third-party security risks, 
and the rise of ransomware. Subsequently, we will analyze the attack flow 
specific to the education industry, offering insight on specific threat actors, 
actionable intelligence, and recommended mitigations for each stage to 
illustrate how organizations can proactively identify and prevent attacks to 
avoid lasting impact.

In this report, we will examine many of the most prevalent threat tactics and 
threat actors operating across education and throughout the attack chain, 
including:
  
**THREAT ACTORS** 
	
- LockBit 3.0
	
- Rhysida
	
- CLOP or Cl0p
	
- Akira
	
- ALPHV aka BlackCat
	
- Medusa
	
- Vice Society
	
- No Escape
	
- Royal
	
- Pirat-Networks
	
- Bl00dy Ransomware 

**THREAT TACTICS** 
	
- Phishing and Social Engineering
	
- Exploitation of Applications 
and Databases
	
- Drive-by Compromise
	
- Abuse of Valid Account 
Credentials and Password Attacks
	
- Access Brokers, Auctions, 
and WebShells
	
- BYOD and IoT Risks
	
- Third-Party Supplier Attacks
	
- Powershell and User 
Execution Techniques
	
- RDP, SMB, and DCOM Lateral 
Movement Techniques
	
- Ransomware and 
Cryptocurrency Miners

For additional information about the most prevalent threat actors, please go 
to the Appendix. 

## Emerging and Prominent Trends

### Shift Towards Online Education
The Threat
During the COVID-19 pandemic, the push towards online learning exposed 
educational institutions to a vast network of devices and systems. While this 
creates incredible opportunities for accessibility, flexibility, and personalized 
learning, it also presents significant challenges. Concerns range from 
cybersecurity and the digital divide to privacy, technical issues, and potential 
social isolation.

Effectively integrating online education requires careful consideration of these 
risks and benefits. This includes exploring specific technologies, analyzing 
successful case studies, staying informed about the evolving landscape, and 
addressing ethical considerations like algorithmic bias and data ownership. 
Ultimately, navigating this shift responsibly involves understanding its 
complexities and paving the way for a future where online and offline learning 
combine seamlessly to reach students everywhere. 

What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs found significant exposure of critical systems and 
devices such as public file servers, printers, collaboration systems, and 
systems storing sensitive data. 

Shodan analysis and scans revealed over 1.8 million devices related to the 
education industry being publicly exposed. As highlighted later in this report, 
this number significantly dwarfs the exposure in other sectors. Trustwave 
SpiderLabs also found instances of misconfigured and vulnerable devices, 
such as publicly accessible conferencing systems and collaboration tools, 
which could lead to unauthorized access and data breaches.

The operational disruptions caused by data breaches in education can be 
severe. An example is Lincoln College, which had to permanently close its 
operations due to a cyberattack. The ransomware attack blocked the college 
from accessing data used in its student recruitment and retention, as well as 
fundraising efforts.

Mitigations to Reduce Risk
	
- Implement strict access controls for critical systems, including file 
servers, printer management software, and collaboration tools. 
Strengthen access controls to minimum necessary levels for 
authorized users. 
	
- Place all servers behind the firewall and practice proper network 
segmentation for enhanced access control. Disable Internet 
access for servers that do not require it.
	
- Address misconfigurations in network devices and other IoT 
devices, ensuring firmware is updated and default passwords are 
changed. 
	
- Provide ongoing cybersecurity training and awareness programs 
for staff and students, emphasizing the importance of security 
best practices. 

### Third-Party Security Risks
The Threat
The education sector, like many others, relies heavily on third-party vendors 
such as software-as-a-service, hosting providers, storage, and IT services 
for various functions, including learning management systems, email, and 
communication and collaboration tools. 

These third parties pose a grave risk to the education sector because of 
undiscovered or un-remediated gaps in their cybersecurity controls or data 
breach protection.

Breaches not only impact the directly targeted institution, but can also have a 
ripple effect across numerous educational entities relying on the same third-
party services. 

What Trustwave SpiderLabs Is Seeing
Notable incidents include the breaches of Illuminate Education and 
Blackbaud. The Illuminate breach in early 2022 significantly impacted two 
of the largest US public school systems, compromising the information of 
approximately 820,000 students in New York City alone. 

The MOVEit RCE (CVE-2023-34362) vulnerability in a third-party file transfer 
service led to breaches at 13 major universities. These breaches had the 
highest prevalence from June to August 2023, most often facilitated by the 
ransomware threat actor Clop. 

![CVE-2023-34362 attack claims on notable universities (based on ransomware claims)]

Mitigations to Reduce Risk
	
- Know your supply chain. Keep inventory of all critical suppliers and 
conduct a comprehensive security assessment before any form of 
engagement is initiated with a third party. 
	
- Ensure that third-party vendor contracts have strict cybersecurity 
clauses. This could include mandating the conducting of regular 
security audits, immediate breach notification, and compliance 
with pertinent data protection regulations.
	
- Encrypt all sensitive data in transit and at rest. Restrict the 
access of sensitive data to the principle of least privilege. Carry 
out regular monitoring of the access logs so that activities of 
unauthorized or suspicious nature may be detected.
	
- Follow industry standards and regulations like GDPR, HIPAA, 
FERPA, etc. for compliance with geographical location and nature 
of data handled by third-party vendors.
	
- Participate actively in cybersecurity forums of the educational 
sector and other information sharing platforms. 

### Ransomware Attacks
The Threat
Ransomware attacks have become a dominant source of breaches in 
education. These attacks can lead to the loss of critical educational and 
personal data, disrupt educational processes, and cause substantial financial 
and reputational damage to institutions.

To facilitate their attacks, threat actors deploy a range of malware types, 
including loaders/downloaders, infostealers, and RATs, to maintain control, 
steal information, and to facilitate the end-to-end ransomware process. 
Attacks targeting universities and primary education schools have led to 
severe operational disruptions including temporary and even permanent 
closures. Please refer to our later section on Ransomware for additional 
details. 

What Trustwave SpiderLabs Is Seeing
Ransomware attacks striking the education industry are prominent and 
growing. For example, in 2023, Trustwave researchers monitored 352 
ransomware claims against educational institutions.

The top ten ransomware groups targeting the industry were LockBit 3.0, 
Rhysida, CLOP (aka CL0P, Cl0p), Akira, Medusa, ALPHV, Vice Society, 
NoEscape, Royal, and Pirat-Networks. These groups have targeted a wide 
range of educational entities across different countries, predominantly in 
the US, but also in Canada, the UK, Australia, France, Germany. The types of 
institutions compromised vary from universities and colleges to public school 
districts, technical schools, and specific training centers.

![Top ten ransomware groups in the education sector]

Mitigations to Reduce Risk
	
- Use host-based anti-malware tools that can assist in identifying 
and quarantining ransomware, but understand they have 
limitations and are often circumvented by custom malware 
packages.
	
- Enhance email security controls to protect against ransomware 
distributed via email. Educate users on the risks of malicious 
email attachments and phishing attempts. Enhance vigilance and 
implement email filtering and monitoring systems.
	
- Establish and regularly practice a formal Incident Response 
process. Ensure backups are available as a contingency to recover 
from a worst-case scenario.
	
- Enable system logs on critical systems and workstations and 
implement network logging through flows, Network Monitoring 
Solutions, or IDS devices on ingress and egress channels.
	
- Implement active monitoring. Merely enabling logs is insufficient; 
if logs are not monitored, they lose their effectiveness. Regular 
monitoring helps establish a baseline of regular activity, making 
abnormal behavior or traffic more conspicuous. 
	
- Perform ongoing underground and Dark Web monitoring for 
information leakage that may have been missed.

## Dissecting the Attack Flow for the Education Sector

### Attack Flow Overview
While the specifics and details of every breach and compromise may vary, 
there is typically a specific attack flow that occurs from the initial security 
bypass to escalation, compromise, followed by persistent home on your 
network, and exfiltration and/or destruction of valuable data. The following 
analysis presents an overview of the attack flow specific to the education 
sector, incorporating insights from the Trustwave SpiderLabs team and 
offering actionable mitigations for organizations to implement. 

At each stage of the attack flow, the recommended mitigations provide 
proactive guidance to minimize the potential risks of financial, reputational, 
regulatory, or physical impacts to an education institution. The typical 
sequence of events unfolds as follows:

### Attack Flow Steps
**Initial Foothold**
This is the step where the attacker successfully triggers a security bypass 
that will give them the ability to expand their access to suit their motives and 
goals. This initial foothold can take various forms, ranging from successful 
phishing attacks to vulnerability exploitation or even logging into public-
facing systems using previously acquired credentials.

In this section, we will explore the most common methods through 
which attackers gain this initial foothold into an education organization, 
like phishing, third party suppliers and exploitable vulnerabilities.

**Initial Payload**
Once the attackers have established a foothold on the network, they will 
proceed to download more sophisticated tools and malware.

In this section, we will specifically concentrate on real-world 
examples of the types of payloads that frequently target education.

**Expansion / Pivoting**
The initial foothold typically involves a low-value workstation, such as a 
phishing victim's laptop, or a network appliance like a VPN endpoint. 
In this section, we will showcase how once armed with the 
necessary tools, attackers can target higher-value accounts and 
systems, such as Domain Admins, root accounts, Active Directory 
Systems, and Database servers.

**Malware**
There are a variety of malware types with a myriad of uses, such as Remote 
Access Trojans (RATs), infostealers, ransomware, and many others. 
In this section, we will focus on the types of malware pervasive in 
the education industry.

**Exfiltration / Post Compromise**
In most cases, the primary motive behind compromises is data theft. 
In this section, we will explore the types of data that are targeted 
and exfiltrated in education-related compromises. Additionally, 
we will present real-world examples of data breaches to provide 
concrete illustrations.

### Initial Foothold: Phishing, Spam & Scams
The Threat
Phishing stands out as the most commonly exploited method for gaining 
an initial foothold in an organization. Instead of attempting to exploit 
vulnerabilities in the software or systems on the network, attackers target 
staff, faculty, or others who have access to systems within the institution that 
can be exploited, such as finances, databases, etc. 

In a typical scenario, the attacker crafts a compelling email, skillfully 
persuading the recipient to engage in certain actions. This could include 
opening an attachment, clicking a link, or executing specific instructions. 
Education-specific social engineering often involves sending fake university 
communications like offering enticing student job opportunities, which 
require the victim to perform certain tasks or provide sensitive information.

Typical phishing goals: 
	
- **Credential Theft:** An example of this would be an email that appears to be 
from the university's administration, containing a link. When the recipient 
clicks this link, they are prompted to enter their login details under the 
pretense of accessing important information or job opportunity details.
	
- **Malware Insertion:** This is often executed through embedding PowerShell 
scripts, JavaScript, or enabling Macros in a document, which is disguised 
as being related to the university or a student job offer.
	
- **Triggering Specific Actions:** This could involve convincing the recipient to 
provide confidential information or perform other actions under the guise 
of a necessary step for a student job application or a university-related 
process.

Trustwave SpiderLabs Insights
The Trustwave SpiderLabs team is committed to monitoring various email-
based threats, such as opportunistic phishing, spearphishing, spam-based 
malware, and scams. In the past year, our team has noted interesting 
developments in the tactics and delivery approaches used in email-based 
attacks within education. These advancements have played a role in 
sustaining the continuing significance and effectiveness of these types of 
attacks.

In the education sector, the most common types of email attachments 
used for phishing and malware distribution are HTML files, executables, 
and PDFs, a trend that echoes observations from other industries. Notably, 
HTML attachments make up 82% of malicious email attachments. These 
attachments are primarily used in two forms: as standalone HTML pages 
designed for credential phishing, often featuring sophisticated obfuscation 
techniques, or as HTML redirectors leading to malicious sites. Additionally, 
Trustwave original research has also seen a preference of the use of HTML 
attachments in Phishing Kits. 

Executable files, which make up the second most prevalent type, typically 
serve as either initial downloaders to facilitate further malware intrusion or 
act as the final payload, like Remote Access Trojans (RATs). Lastly, PDFs 
are commonly employed to host malicious links that initiate further malware 
downloads or contain deceptive text as part of a scam strategy, illustrating 
the diverse and evolving nature of email-based threats in education.

![Top malicious attachment filetypes for the education sector]

Trustwave researchers have observed that threat actors are frequently 
misusing specific services for these attacks. Decentralized InterPlanetary 
File System (IPFS) links, such as 'dweb.link,' are used to distribute phishing 
content, exploiting its network to avoid detection. Google Services, with 
domains like 'googleapis.com,' are abused for their trustworthiness to 
slip past security filters. Compromised WordPress sites, for example, 
'howtotender.co.za,' are hijacked to host fake login pages. Cloudflare 
Services, including 'workers.dev,' are manipulated for their credibility to host 
phishing material. Additionally, free web and app hosting platforms, such as 
'netlify.app,' are favored by phishers for cost-free malicious site creation.

In the education sector, Trustwave researchers have observed several 
notable phishing campaign themes: 

**RFQ-THEMED MALWARE SPAM**
In a recent phishing scheme targeting universities, Trustwave SpiderLabs 
researchers observed attackers sending emails masquerading as “requests 
for quotations” from various educational institutions. To enhance their 
authenticity, these emails featured the spoofed university's logo in the 
message body and incorporated the institution's name in the 'From' and 
'Subject' headers, as well as in the filenames of attachments. 

![Sample of malicious “request for quotations” impersonating various universities]

To further increase the authenticity of the attacks, the emails suggested that 
the quotations should align with the university’s annual budget, with more 
details purportedly in the attached file. However, these attachments were 
either malicious executables or archives containing them. The threats most 
delivered through this phishing theme included the Lokibot Infostealer, Agent 
Tesla RAT, and Downloader Guloader.

**FAKE UNIVERSITY COMMUNICATIONS**
In another common phishing campaign, university accounts of students, 
faculty, and staff were targeted with fraudulent emails purporting to be 
official university communications. 

![Sample of malicious email impersonating an official university communication that leads to a credential phishing site]

These messages impersonated the university's IT department and were 
crafted to look authentic. They bolster their credibility by integrating the 
university's branding and language style, often relating to current university 
events or settings. The emails typically include urgent calls to action, such 
as requests to verify accounts or update personal information, and direct 
recipients to fake websites designed to harvest their credentials. 

**STUDENT JOB OFFER SCAMS**
Trustwave researchers observed an uptick in scam messages targeting 
students with counterfeit job offers. These emails come unsolicited and 
usually present lucrative opportunities that promise high compensation for 
minimal effort and offer flexible working hours. 

Typically, these communications initiate with a request for personal details 
as part of the job application process. Scammers may also demand an 
advance payment under the pretext of covering training expenses. In some 
cases, students receive a fraudulent check with instructions to deposit it and 
forward a portion of the funds elsewhere, only to find out later that the check 
is fake, rendering the student responsible for the total amount.

![Sample of a “Job Offer Scam” targeting university students]

Students are prime targets for cybercriminals due to their relative 
inexperience with scams and eagerness for flexible, well-paying job 
opportunities. Their search for convenient employment can cloud judgment 
and makes them susceptible to offers that seem too good to be true.

**HR-THEMED SPAM**
Aside from the student population, the education sector has a significant 
workforce of personnel. Education has the 6th highest compounded rate of 
change in terms of employment projections out of 18 industries being tracked 
by the US Bureau of Labor Statistics. This high rate of increase in new staff 
could make the sector more attractive to threat actors. 

Throughout 2023, our researchers observed a surge in phishing campaigns 
exploiting the ubiquitous nature of HR communications. Cybercriminals 
capitalized on this situation which we have observed in our spam traps and 
reported by Trustwave SpiderLabs in a November 2023 blog post.

![Sample of an HR-themed spam targeting employees of a training academy]

HR-themed spam emails often lure recipients with subjects related to 
employee remuneration and benefits review. A notable tactic involves an 
HTML attachment in the email, purportedly from the organization’s HR staff, 
presenting itself as a document for employee benefits review. However, this 
attachment is a credential phishing page, with malicious code obfuscated 
within the 'onerror' attribute of an 'img' element. The invalid image source 
triggers this attribute upon opening the attachment, decoding, and displaying 
the phishing page, thus tricking the targeted staff members into divulging 
sensitive information.

**COMPROMISED EDUCATIONAL INSTITUTION SITES**
In our research involving cyberattacks targeting educational institutions, we've 
observed a notable trend involving the misuse of the '.edu' domain, commonly 
associated with educational entities. Our spam traps identified campaigns that 
frequently exploit this domain, either as a top-level or second-level domain, 
leading to compromised websites used to disseminate threats. 

![Sample PDF attachment leveraging an EDU domain that leads to an IcedID malware]

These compromised sites are often embedded as links within the body of an 
email or included within the PDF files. Clicking on these links leads users to 
malware such as IcedID, Pikabot, and DarkGate.

**WIRE TRANSFER SCAMS**
In a recent Business Email Compromise (BEC) scam targeting the education 
space, attackers used a cleverly disguised email asking recipients to urgently 
process a wire transfer, allegedly for research and market development 
purposes. This attempt to exploit the industry’s alignment with research 
activities is evident in the email's subject line. 

![Sample wire transfer email scam attempting to leverage a research-related requests]

However, the message contains several red flags: it artificially creates a 
sense of urgency by instructing the recipient to process the payment “right 
away,” and the sender's domain, “email.com,” is a generic free mail service, 
undermining the credibility of the supposed university communication. 

Finally, it is worth noting that Trustwave SpiderLabs has been continually 
monitoring the effect of AI and Large Language Models (LLMs) like ChatGPT 
on phishing attacks. Many of the red flags that we teach users to identify 
phishing emails include items like picking out misspellings, grammar 
mistakes, and general clumsiness of writing that may indicate that the 
author is not a native speaker. The quick maturity and expanded use of 
LLM technology is making the crafting of these emails even easier, more 
compelling, highly personalized, and harder to detect. 

Mitigations to Reduce Risk
	
- Conduct regular training and awareness programs for students, 
faculty, and staff, emphasizing the recognition of phishing emails, 
especially those mimicking university communications, HR 
communications, and job offers.
	
- Consistently conduct mock phishing tests to assess the effectiveness 
of anti-phishing training and retrain repeat offenders. If feasible, 
consider providing the same assessment to students as well.
	
- Implement robust anti-spoofing measures, including deploying 
technologies on email gateways.
	
- Deploy layered email scanning with a solution like MailMarshal to 
provide better detection and protection.
	
- Utilize techniques to detect domain misspellings, enabling the 
identification of phishing and BEC attacks.
	
- Regularly monitor for the misuse of '.edu' domains and take swift 
action against any detected compromises.
	
- Perform routine security audits of university websites and IT 
infrastructure to identify and rectify vulnerabilities that could be 
exploited in phishing campaigns.
	
- Be vigilant about the increasing sophistication of phishing emails 
due to AI and LLM technologies, which can create more convincing 
and error-free scam messages.
	
- Enable multi-factor authentication (MFA) to provide an additional 
layer of protection for accounts.
	
- Restrict the access of assets and sensitive data with the principle of 
least privilege in mind.

> When layered, captures up 
to 90% of malicious emails 
missed by other email 
security vendors.

### Initial Foothold: Logging in
The Threat
Threat actors can infiltrate an organization's network in various ways, 
including straightforward methods like using login credentials. This might 
happen if default device credentials remain unchanged, or if weak passwords 
are susceptible to brute-force attacks. But typically, threat actors gain access 
through methods like phishing, drive-by downloads, leveraging vulnerabilities 
in applications, or purchasing pre-established access to a target organization 
from various access brokers. 

Trustwave SpiderLabs Insights
As discussed in the previous section (Initial Foothold: Phishing, Spam 
& Scams), phishing is the most widespread tactic to gain initial access 
to organizations, with attackers focusing not on software or system 
vulnerabilities, but rather on manipulating the individuals. Other common 
techniques used by threat actors are: 

**ACCESS CREDENTIALS AND ACCESS BROKERS**
Trustwave researchers continually observe the trade of access credentials 
pertaining to data, networks, and systems on the Dark Web. Initial Access 
Brokers, which have been active in underground marketplaces and forums, 
were seen offering unauthorized access to various educational institutions. 
Threat actors targeting universities see the potential to leverage their 
extensive network infrastructures for various malicious activities, such as 
gathering sensitive data, turning them into botnets, orchestrating DDoS 
attacks, or deploying ransomware. In Figure 10, the threat actor is selling 
alleged root access to all EC2 machines, S2 buckets, and other AWS account 
services of a particularly well-known US university. 

![A threat actor selling alleged access to the AWS infrastructure of a well-known US university]

In Figure 11, a threat actor is selling alleged VPN access to a university in 
the US. The threat actor, while vague about the victim, referenced only the 
university's revenue. Prices for such illicit offers vary widely, ranging from a 
few hundred to tens of thousands of US dollars in cryptocurrency, influenced 
by factors like geographical location, network size, security measures, access 
type, information sensitivity, and the educational facility's privilege level.

![A threat actor selling alleged SSL / VPN access to a high revenue university in the US]

Figure 12 highlights a threat actor claiming to have domain-level access to 
Azure and Microsoft services within a US school's network. According to the 
post, this access potentially allows for the management of the entire network 
and its numerous devices, creating a significant risk for various malicious 
activities originating from this institution. The actor is reportedly asking for 
$10,000 for this level of access.

![A threat actor selling alleged access to various Microsoft and Azure services of a school in the US]

In another interesting finding, Trustwave researchers observed the "Russian 
Market," a marketplace known for selling data dumps, logs, and accounts, 
has listed over 82,000 logs mentioning the domain name mit.edu, associated 
with the prestigious Massachusetts Institute of Technology (MIT), in the past 
year. While the authenticity of these logs remains largely unverified, they 
predominantly contain login credentials for at least 90 subdomains of MIT. 
It's important to note that some of these samples might be fictitious or serve 
merely as examples of potential compromising methods rather than actual 
breaches.

**EDU EMAIL ACCOUNTS**
Threat actors often target education institution emails as an initial access 
vector due to their valuable content, including research, intellectual property, 
and personal and financial information of faculty and staff. The widespread 
use of university email addresses across various websites also makes them 
attractive for identity theft, phishing scams, and unauthorized access. With a 
large user base, these email accounts become appealing targets for hackers 
seeking to exploit them for malicious or financial gain. 

![A threat actor in a Vietnamese forum looking to purchase EDU emails every 1-2 weeks]

Email accounts from educational institutions are frequently exploited by 
hackers as initial access vectors to unlock various perks and benefits. This 
includes unauthorized access to purchasing platforms, acquiring restricted 
software, and taking advantage of software license discounts. The use of 
educational email credentials to gain entry to exclusive offers and services 
is a common strategy among cybercriminals. Below is an example of email 
access sellers:

![A threat actor in a Vietnamese forum selling various EDU Gmail accounts from a university]

**DRIVE-BY COMPROMISE**
In the education industry, marked by academic freedom, a diverse mix of 
unvetted users, including students and guests, and a prevalent BYOD policy, 
the risk of drive-by compromises is significantly heightened. 

Trustwave researchers have observed the use of drive-by compromise 
methods for initial network access, with SocGholish malware being a notable 
culprit. 

![Sample of a Compromised WordPress website used in SOCGholish campaign. Source: heimdalsecurity.com]

This malware typically disguises itself as a legitimate software browser 
update, exploiting the more "open" security measures in educational 
settings. It primarily functions as a javascript downloader, tricking users on 
compromised websites into downloading harmful files containing a JavaScript 
payload. These files, historically packaged within ZIP files, are misleadingly 
labeled as updates for widely used software like web browsers, or Microsoft 
Teams.

**EXPLOITING PUBLIC-FACING APPLICATIONS**
Educational institutions are exposed to public-facing exploits due to 
the nature of their operations, which involve many publicly accessible 
applications and systems processing information, such as student 
registration, enrollment, and personal information, as well as financial aid 
systems, crucial for storing sensitive personal details. Online collaboration 
sites and virtual learning platforms, which have become even more essential 
post-pandemic, are characterized by their vast data pools and decentralized 
management. 

Additionally, the multiple websites and web applications of an educational 
institution, which are often dynamic and involve student participation, 
present unique security challenges. The next section will expound on specific 
vulnerabilities and exploits that highlight these challenges. 

Mitigations to Reduce Risk
	
- Educate system users of the risks of phishing, drive-by downloads, 
and the importance of secure browsing habits.
	
- Update and patch all software regularly, including web browsers.
	
- Regularly monitor access points such as VPN and review logs for 
unusual activities. Educational institutions should also conduct 
periodic audits of their network infrastructure to identify and 
address vulnerabilities.
	
- Regular monitoring of Dark Web sites and underground 
marketplaces for possible breaches. 
	
- Implement password length requirements for at least 12 or more 
characters to enhance security.
	
- Enable multi-factor authentication (MFA) to provide an additional 
layer of protection for accounts.
	
- Restrict access to assets and sensitive data based on the principle 
of least privilege.
	
- Securely store credentials in password managers to prevent 
credential abuse.
	
- Encrypt credentials when used in scripts to safeguard sensitive 
information.
	
- Audit local administrative accounts regularly and obfuscate admin 
accounts by not using admin in the name.
	
- Use LAPS on Windows systems to manage local accounts.
	
- Implement Privileged Access Management (PAM) and Privileged 
Identity Management (PIM) solutions to deepen defense in depth 
strategy

### Initial Foothold: Vulnerability Exploitation
The Threat
When it comes to information security, vulnerability exploitation is often the 
first concept that comes to mind. This topic can encompass zero days, patch 
agility, proof-of-concept exploits, and vulnerability disclosure.

To put it simply, a vulnerability refers to a software bug that introduces 
security risks. Attackers develop specialized software or scripts to exploit 
the vulnerability and circumvent security controls, such as authorization, 
authentication, and audit controls. Once