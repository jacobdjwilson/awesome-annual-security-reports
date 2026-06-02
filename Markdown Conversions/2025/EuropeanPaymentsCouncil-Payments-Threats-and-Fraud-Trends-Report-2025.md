# 2025 Payment Threats and Fraud Trends Report

EPC162-24
Version 2.0
Date issued: 19/11/2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Conclusions](#conclusions)
- [1 Document Information](#1-document-information)
  - [1.1 Scope and Objectives](#11-scope-and-objectives)
  - [1.2 Audience](#12-audience)
  - [1.3 Contributors](#13-contributors)
  - [1.4 References](#14-references)
  - [1.5 Definitions and Abbreviations](#15-definitions-and-abbreviations)
- [2 Focus on Recent Fraud and Attack Trends](#2-focus-on-recent-fraud-and-attack-trends)
- [3 Payment Threats and Fraud Landscape](#3-payment-threats-and-fraud-landscape)
  - [3.1 Cyber threats, attack techniques and fraud enablers](#31-cyber-threats-attack-techniques-and-fraud-enablers)
    - [3.1.1 Social Engineering](#311-social-engineering)
    - [3.1.2 Malware](#312-malware)
    - [3.1.3 Advanced Persistent Threats (APT)](#313-advanced-persistent-threats-apt)
    - [3.1.4 Distributed Denial of Service (DDoS)](#314-distributed-denial-of-service-ddos)
    - [3.1.5 Botnets](#315-botnets)
    - [3.1.6 Third-party compromise, supply chain attacks and IT outages](#316-third-party-compromise-supply-chain-attacks-and-it-outages)
    - [3.1.7 Monetisation Channels](#317-monetisation-channels)
  - [3.2 Fraud per Payment-Relevant Process](#32-fraud-per-payment-relevant-process)
    - [3.2.1 Introduction](#321-introduction)
    - [3.2.2 On-boarding and Provisioning](#322-on-boarding-and-provisioning)
    - [3.2.3 Payment request and invoicing processes](#323-payment-request-and-invoicing-processes)
    - [3.2.4 Payment Initiation & Authentication](#324-payment-initiation--authentication)
    - [3.2.5 Payment Execution](#325-payment-execution)
    - [3.2.6 Mobile Wallets for Identification and Authentication](#326-mobile-wallets-for-identification-and-authentication)
  - [3.3 Fraud unique to Specific Payment Instruments](#33-fraud-unique-to-specific-payment-instruments)
    - [3.3.1 SEPA Schemes](#331-sepa-schemes)
    - [3.3.2 Card Scheme](#332-card-scheme)
    - [3.3.3 Mobile Wallets for Card Payments](#333-mobile-wallets-for-card-payments)
- [4 Liability Shift Discussions related to Specific Fraud Types](#4-liability-shift-discussions-related-to-specific-fraud-types)
- [5 Annex I – Summary Threats versus Controls and Mitigations](#5-annex-i--summary-threats-versus-controls-and-mitigations)

---

## Executive Summary

### About this document
The overall purpose of the European Payment Council (EPC) is to support and promote European payments integration and development, notably the Single Euro Payments Area (SEPA). The EPC is committed to contribute to safe, reliable, efficient, convenient, economically balanced, and sustainable payments, which meet the needs of payment service users while supporting the goals of competitiveness and innovation in an integrated European economy.

Since security is one of the cornerstones of customer trust in payment systems, the EPC has decided to dedicate an annual report to the latest trends in security threats impacting payments while also giving an insight on how these threats may lead to payment fraud and how to mitigate related risks.

This document is maintained by the EPC Payment Security Support Group (PSSG). The EPC Fraud Information Distribution Arrangement Task Force (FRIDA TF) contributed to this update by providing information on relevant and recent attacks and fraud cases.

### Conclusions
The report provides the following main conclusions concerning payment threats and fraud enablers:

- **Social engineering attacks and phishing attempts** are still increasing, and they remain instrumental, often in combination with malware. A shift in targets has been observed from consumers, retailers and SMEs to company executives, employees (through ‘CEO fraud’), payment service providers (PSPs) and payment infrastructures.
- **AI-tools** make it easier for fraudsters to generate realistic-looking phishing and spear-phishing emails and deepfakes. AI is fundamentally reshaping the payment threats and fraud landscape.
- **Malware** in its various forms remains a major threat, in particular ransomware.
- **Advanced Persistent Threat (APT)** is presently one of the most sophisticated and lucrative types of attacks.
- **DDoS attacks** on the financial sector have increased in both volume and sophistication in recent years, fuelled by geopolitical tensions.
- **Botnets** continue to act as a force multiplier for malicious activity.
- **Third-party vendor risks** are increasingly critical for PSPs and they can introduce new challenges, in particular supply chain risks.
- **Monetisation channels**, such as ‘money muling’ or the use of crypto currencies, often follow a fraudulent payment transaction.

## 1 Document Information

### 1.1 Scope and Objectives
The present document aims to provide an insight in the latest developments on threats affecting payments, including cybercrime, and provides an insight into the payments fraud resulting from criminal attacks.

### 1.2 Audience
The document is intended for PSPs as well as interested parties involved in payments, such as:
- Third Party Service Providers
- Equipment manufacturers (POIs, consumer devices, etc.)
- Merchants and merchant organisations
- Regulators
- Standardisation and industry bodies
- Payment schemes
- Other interested stakeholders.

### 1.3 Contributors
The contributors to the 2025 update are:
Ioannis Tzanos (Eurobank, Greece), Alain Hiltgen (UBS Business Solutions AG, Switzerland), Laurens Messing (Dutch Banking Association, The Netherlands), Mika Linna (Finance Finland), Simone Coltellese (CERTFin, Italy), Valentim Oliveira (SIBS, Portugal), Dirk De bruyn (EPC Secretariat), Valentin Vlad (EPC Secretariat), Romano Ramanti (Zurich Cantonal Bank), Mats Ideström (Swedbank), Željko Čuljak (Zagrebačka banka).

### 1.4 References
| Ref nr | Document | Author |
| :--- | :--- | :--- |
| [1] | Payment Services Directive (PSD2) | EC |
| [2] | Commission Delegated Regulation (EU) 2018/189 | EC |
| [3] | Directive (EU) 2022/2555 (NIS 2 Directive) | EC |
| [4] | General Data Protection Regulation (GDPR) | EC |
| [5] | Digital operational resilience act (DORA) | EC |

### 1.5 Definitions and Abbreviations
*(Definitions and Abbreviations tables omitted for brevity, see original document for full list)*

## 2 Focus on Recent Fraud and Attack Trends
The payments threat landscape continues to evolve rapidly, with attackers leveraging increasingly sophisticated tools and techniques. Artificial Intelligence (AI) has emerged as a major enabler of both traditional and novel fraud schemes.

**Observed fraud types include:**
- **Bank employee impersonation:** Fraudsters impersonate law enforcement or bank support desk agents to trick victims into sharing credentials or installing remote support tools.
- **‘Safe account’ fraud:** A specific case of Bank Employee Impersonation where victims are convinced to transfer money to a ‘safe’ account controlled by the fraudster.
- **Remote support scam:** Fraudsters convince customers to install remote support software to take control of the customer device.
- **Call forwarding scam:** Perpetrators manipulate a victim’s phone settings to reroute calls to numbers under their control.
- **Ghost Tap:** Combines social engineering, malware, and NFC relay technology to enable unauthorized transactions.
- **Recovery Scam / Refund Scam:** A secondary scam targeting individuals who have already fallen victim to another fraud scheme, promising to recover lost funds for an advance fee.

## 3 Payment Threats and Fraud Landscape

### 3.1 Cyber threats, attack techniques and fraud enablers

#### 3.1.1 Social Engineering
Social engineering is an attack vector that exploits human error to gain private information, access, or valuables. In a corporate context, social engineering attacks often seek to gather and exploit information about the target organisation’s business processes.

**Suggested Controls and Mitigation:**
- Awareness campaigns are essential.
- Implement technical solutions that verify the authenticity of websites, emails, voice calls, and SMS messages.
- Ensure login screens only occur in https sessions using certificates with Extended Validation.
- Support HSTS on websites.

*(Remaining sections 3.1.2 through 5 follow the structure of the original document, detailing specific technical threats, payment processes, and liability discussions.)*

[^1]: https://www.europol.europa.eu/media-press/newsroom/news/fake-number-real-damage-europol-urges-action-against-caller-id-spoofing

---

EPC162-24/ Version 1.4

The sender of phishing emails will typically like to spoof the domain name of a PSP or other
trustworthy entity. Such organisations may try to prevent this by implementing the following
countermeasures:

•  Sender Policy Framework (SPF): an email-validation system designed to detect email

spoofing.

•  Domain Keys Identified Mail (DKIM)2: an email authentication method designed to detect
email spoofing by having receiving mail exchangers check that the incoming mail from a
domain is authorised to be sent by that domain’s administrators.

•  Domain-based Message Authentication, Reporting and Conformance (DMARC)3 is an email-
validation system designed to detect and prevent email spoofing. DMARC is built on top of
the mechanisms mentioned before, SPF and DKIM, and enables the blocking of spoofed
mails.

An inherent countermeasure against phishing is to provide an authenticator to users/customers:
this does not expose any information of users; hence, they do not expose any credentials. Social
engineering may still be used to trick the user in unintentionally authorising third-party access.

Private companies – working in close cooperation with telecom operators – offer takedown of
phishing websites as a service. Such companies might be able to limit access to and finally stop
phishing sites. In addition, it might also be possible sometimes to collect stolen data from phishing
servers. The victim’s PSP might then be able to reduce the consequences by contacting the
customer and blocking the card or compromised authenticator.

3.1.2  Malware
Malware, short for malicious software, is an umbrella term used to refer to a variety of forms of
hostile or intrusive software. Cybercriminals design malware to compromise computing functions,
to steal data, to bypass access controls, and to cause harm to host computers, customer devices
and their applications or data.

One of the major threats against cyber security today is malware. Malware comes in a wide range
of flavours, such as viruses, worms, remote access tools, rootkits, Trojans, spyware and adware.
Malware exploits software vulnerabilities in browsers, third party software and operating systems
to gain access to the device and its information and resources. To spread, malware uses also social
engineering techniques to trick users into installing and running the malicious code.

•  Trojan horse: This is probably the largest category of the malware family. It consists of a
large variety of exotic names. However, they all have one thing in common; they bypass
the security measure on the system to infect it. Their main purpose is stealing valuable
information from the system and gaining control of the system itself. Trojans are also used
to get an initial foothold and download other malware.

•  Spyware, Adware & Banking Trojans: Spyware and adware, which are categorised as

malware, are less dangerous for the users. Spyware is often classified into the following
categories, browser hijackers, tracking cookies and system monitors (key-logging, take
screenshots, record voice). In some cases adware is seen as the fourth category of
spyware. These types of malware are all trying to track and store the usage and behaviour

2 see for instance: https://www.gov.uk/government/publications/email-security-standards/domainkeys-identified-
mail-dkim
3 see for instance: https://www.gov.uk/government/publications/email-security-standards/domain-based-message-
authentication-reporting-and-conformance-dmarc

www.epc-cep.eu

23 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

of users, serving them with pop-up ads when connected to the Internet. Based on the
same approach, attackers are installing malware (Banking Trojan) targeting the victim
while using electronic or mobile banking services (e-banking / m-banking). Banking Trojans
are capable of hijacking the browser and tampering financial transactions or stealing user
credentials during the use of e- or m-banking services. Banking Trojan can also be sent
through weaponised attachments in an e-mail or infected software.

•  Ransomware: Is a type of malicious software designed to encrypt files on the device or

deny access to the device, which is the reason for it to be also known as cryptoware. Users
are blackmailed into paying a certain amount to receive a decryption key to regain access
to the data or device once payment has been made. A surprising fact is that this kind of
attacks seems to be more profitable to the attackers than the traditional banking Trojans.

•  Remote Access Trojans (RATs): This is a piece of malware that allows a remote actor to
control a system as if they have physical access to it. It may provide cybercriminals with
unlimited access to the victim’s computer. Using the victim’s access privileges, the RAT can
perform critical functions or steal sensitive data. RAT technology is also commonly used by
APTs (see Section 3.1.3) to bypass strong authentication and get access to important data.

•  RATs for Mobile: RATs in the mobile space have also emerged, exploiting Android’s
accessibility services in combination with standard remote access functionality. By
leveraging a dropper or tricking the user into installing such an app and granting it
accessibility rights, fraudsters get full remote control over the mobile’s user interfaces, i.e.,
they can easily spy on input/output to gather credentials but can also easily reinject
captured data or push buttons upon request by a specific service or authentication app
they would like to remote control. No mobile rooting is required for this to work.
•  Fileless malware (also known as non-malware): Fileless malware is malicious code that

does not need a file or script to operate; it takes advantage of existing vulnerabilities of the
Operating System. It exists exclusively in a computer’s RAM and uses system tools to inject
malicious code into trusted processes. It is more difficult to prevent, detect and remove, as
it does not leave a file for an antivirus software to detect. Hackers can steal data or install
other forms of malware to give it persistence or hide it in some other trusted processes or
internal persistent data. This way, it can set up scripts that run when the system restarts to
continue the attack.

•  AI-Enhanced Malware: Attackers use AI to develop polymorphic malware that can evade
traditional detection methods. AI can also automate the adaptation of malware to exploit
new vulnerabilities or bypass security controls.

•  Mobile Threats: AI is used to create malware that targets mobile devices, leveraging

accessibility features or mimicking legitimate app behaviour.

As organisations continue to migrate on-premise services and applications to the cloud or to
externalise them to third parties, it is reasonable to deduce that these external resources will also
suffer fraud threats and risks and become new targets of exposure to malwares and APTs.

3.1.2.1  Impact and Consequences
Whether the infection is targeting a private user, an SME or a multinational company, the effects
of a successful malware attack can cause significant damage, and every prevention and mitigating
method should be utilised.

Recent ransomware attacks have been attributed to various notable groups, including LockBit,
RansomHub, ALPHV (aka BlackCat), Clop, PLAY, Hunters International, and Akira.

www.epc-cep.eu

24 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

In the case of PSPs, all necessary steps to prevent ransomware attacks should be taken.
Ransomware attacks could involve encrypting of payment information, PANs and other
information necessary for PSP business execution.

Ransomware has typically no impact on the users’ banking credentials. Instead, by making use of
banking Trojans, fraudsters have managed to extort a significant amount of money from users.

For private users, spyware and adware are a large threat towards their privacy, as this type of
malware looks for patterns of the users and tries to profile their individual behaviour for
monetisation purposes. Similar things might happen for companies, but normally this type of
malware targets individual behaviour, in fact it is their goal to group the individual by their own
definitions, it is therefore not a direct threat towards corporate users.

Malwares normally search the infected machine for all information that can be monetised; for
private users this is typically credentials related to e- or m-banking (mobile and web). Credit card
credentials are of similarly high value. For private users the amount of information that can be
sold to other parties is relatively small. Such information is easier to find in companies as customer
information or intellectual property information can be used to blackmail or give an advance in a
competitive market. The above case has a significant impact in larger organisations or
governmental organisations where information is one of the most valuable assets.

3.1.2.2  Suggested Controls and Mitigation

User Controls and Mitigation
To prevent malware attacks, users should:

•  First minimise the number of installed programs on their device (and from trusted

resources only), as the number of vulnerabilities will decrease accordingly.

•  Secondly, one of the best ways to ensure that the systems or devices do not become
infected with malware is to regularly update the installed software – especially the
Operating System, which often release new versions to mitigate newly found
vulnerabilities– and to remove software that does no longer have any use.

•  An advice would however be to utilise specialised software to remove and protect against

adware, as the latter also could use resources on the computer.

Related specifically to Mobile devices, users should implement some measures to mitigate the
threats related to mobile devices, these include:

•  Update the software running on your mobile device with the latest security patches and
upgrades, these should be sent to you by your network / operating system provider.

•  Use a secure lock screen, set a password, PIN or fingerprint to unlock your device.
•  Do not allow applications to be installed from unknown / untrusted sources.
•  Do not jailbreak or root your devices.
•  Add a PIN or passcode to the voicemail on your mobile device.
•  Do not use a PIN code which is part of well-known information (e.g. date of birth).
•

Install anti-virus software on your mobile device.

PSP Controls and Mitigation
PSPs’ departments dealing with customer relations should use every opportunity to inform their
customers that it is very important to keep their software updated, and hence reduce the risk for
malware infection significantly.

www.epc-cep.eu

25 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Mobile payment service providers should:

•  Create awareness campaigns to educate consumers on how to avoid the previous

explained fraud scenarios.

Implement anti-tampering and integrity controls in app.

•  Monitor app stores and Internet for fake applications.
•
•  Associate jailbroken or rooted devices with a higher fraud score.
•  Protect app code with code signing and obfuscation.
•
•  Perform application penetration testing.
•  Do not consider frequently used third-party libraries as secure and validate them before

Implement strong sensitive data encryption on device.

using them.

•

•

Implement controls to protect communication channel (such as certificate pinning) to
ensure an app will only communicate with a trusted party.

Implement the app as personalised and prevent transfer of a personalised app to another
device.

Implement device owner/user verification as well as mobile device verification.

•
•  Use always two-factor authentication, which should be implemented in a user-friendly

way.

•  Establish secure mobile payment app enrolment procedures, which cannot be

circumvented by vishing and/or other social engineering scams.

•  Check vulnerabilities based on the OWASP MASVS list.

Service Providers or PSP IT departments Controls and Mitigation
Service providers’ or PSPs’ internal IT departments should implement measures such as:

•  Script blockers, so that the device becomes less exposed to the risk, and therefore the risks

of infections are smaller.

•  All critical files should be regularly backed up so that they can be recovered in the case of

unauthorised alteration, encryption, or destruction.

•  Monitoring of files/software (executables) behaviour can help to block certain threats such

as ransomware. This is generally referred to as ‘malware behaviour blocking’.

•  Limited use of administrative rights; this is mostly applied by companies and security aware
users, as most users would not see the benefit of it in their everyday needs. Firewall and
antivirus on consumer devices should be regularly updated. It is also strongly
recommended to enable further controls provided by the endpoint security mechanisms,
such as the IPS/IDS capability on the device4, when applicable.

•  Ensure that macros cannot run on the systems while opening attachments or documents in
general. This is typically the case for most large companies, however smaller companies
and private users largely depend on the patches that are automatically installed by the

4 Intrusion Prevention Systems / Intrusion Defence Systems are security mechanisms deployed on servers or devices
which monitor in real-time for entries representing a security violation. Some common abilities of such mechanisms
include integrity checking, policy enforcement, rootkit detection, detection of variations in system configuration. They
offer the ability to identify intrusion attempts and actively prevent malicious or anomaly activity on the host system.
IPS/IDS could be deployed at the network level too.

www.epc-cep.eu

26 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

office suite software provider as they do not understand the threat. Allowing the execution
of only signed macros can be the solution to securely exclude malware without losing
functionality or breaking business needs.

•  Consider the use of Web isolation technologies in order to let potential threats run in a

secure environment (sandbox).

Controls and Mitigation specific for the usage of Cloud services
Before using a cloud service, a PSP must identify assets (data, applications, infrastructure) and
evaluate them (criticality, classification) and define the appropriate security controls. Then they
should choose an appropriate cloud deployment model and define whether and how the data can
move in and out of the cloud. Finally, there should be a due-diligence process to evaluate the
service provider regarding security, privacy, availability and their SLA.

Cloud governance including a risk-based analysis approach, must be based on international
standards such as NIST, ISO 2700x, COBIT or PCI-DSS as well as continuous monitoring of the
implemented controls are first steps to mitigating or reducing the fraud risks.

Equally important is the regular execution of a security audit to verify the cloud provider’s
conformity to the security requirements through the whole lifecycle of the application.

PSPs must always have the control over their data, security included. For example, when
encryption is used for data privacy, PSPs must have control over the key management and not the
cloud provider. Also, where technically possible, the authentication mechanism should always be
controlled by the company and not by the cloud provider.

Controls and Mitigation for the usage of multi-purpose authentication means
Multi-purpose authentication means, as exemplified by the currently developed EUDI-Wallet5,
confront a form of exposure not encountered by authentication means dedicated to a specific
purpose (e.g. an online banking service from a PSP). Malware can trick end-users into granting
authorization for the use of their securely guarded credentials, ostensibly for an uncritical activity
(e.g. accessing an exclusive shopping opportunity), while effectively misusing these authorized
credentials for illicit access to the end-user’s online banking account. This exposure notably exists
irrespective of the level of credential protections (e.g. hardware keystore, strong biometric access)
against credential theft or unauthorized usage. To counter this threat:

•  Multi-purpose authentication means must incorporate a secure execution environment
that supports authentication with linking through a trusted user interface  (c.f. also EUDI
Wallet ARF Issue List6). Such feature is necessary to effectively confine an end-user’s
authentication to a service that can be clearly displayed and agreed upon by the end-user,
as additionally required for user sole control.

•  For PSPs that support multi-purpose authentication means for the access to their online
banking services it is imperative that they grant access only when they can unequivocally
verify, via a robust linking mechanism, that the use of the multi-purpose authentication
means was genuinely authorized by the end-user for access to their specific service.

5 https://digital-strategy.ec.europa.eu/en/library/european-digital-identity-architecture-and-reference-framework-
outline
6  FIDO  for  User  Sole  Contol  in  the  EUDI  Wallet  ·  Issue  #302  ·  eu-digital-identity-wallet/eudi-doc-architecture-and-
reference-framework · GitHub

www.epc-cep.eu

27 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

3.1.3  Advanced Persistent Threats (APT)
An Advanced Persistent Threat is a sophisticated, targeted, malicious attack aimed at a specific
individual, company, system or software, based on some specific knowledge regarding the target.
It pursues its objectives repeatedly over an extended period of time, adapts to defenders’ efforts
to resist and is determined to maintain the level of interaction needed to execute its objectives7.

The term APT originated in the U.S. Department of Defense late in the first decade of the 21st
century to describe cyberespionage efforts by China against American national security interests.8

APTs are different from other targeted attacks in the following ways:

•  Customised attacks – In addition to more common attack methods, APTs often use highly
customised tools and intrusion techniques, developed specifically for the campaign. These
tools include zero-day vulnerability exploits, viruses, worms, and rootkits. In addition, APTs
often launch multiple threats or ‘kill chains’ simultaneously to breach their targets and
ensure ongoing access to targeted systems, sometimes including a ‘sacrificial’ threat to
trick the target into thinking the attack has been successfully repelled.

•  Low and slow – APT attacks occur over long periods of time during which the attackers

move slowly and quietly to avoid detection.

•  Higher aspirations – Unlike the fast-money schemes typical for more common targeted
attacks, APTs are designed to satisfy the requirements of international espionage and/or
sabotage, usually involving covert state actors. The groups behind APTs are well funded
and staffed; they may operate with the support of military or state intelligence.
•  Specific targets – Widely reported APT attacks have been launched at government

agencies and facilities, defence contractors, and manufacturers of products that are highly
competitive on global markets. In addition, APTs may attack vendor or partner
organisations that do business with their primary targets. Regular companies with valuable
technology or intellectual property and financial institutions managing their clients’
valuable assets are now being targeted by nation states.

APTs can often be seen as an outstanding category of malware. Attackers demonstrate a
continuously improving set of skills, in bypassing security mechanisms, providing often a state-of-
the-art attack that changes the roadmap and trends of the security industry. This is also known as
zero-day attacks, since no normal signatures exist from the antivirus / antimalware tools.

The APT attacks are often executed following a structured approach. Experts have identified
typical stages of an attack starting with the selection of the target, going through the information
gathering, gaining access to the target, exploitation and operation, and terminating with data
discovery, collection and exfiltration.9

APT attacks can further be recognised by special signs that hackers leave behind. Over the
past two decades, Roger Grimes discovered the following five signs most likely to indicate
that a company has been compromised by an APT10:

7 National Institute of Standards and Technology (NIST), Special Publication 800-39, Managing Information Security
Risk, Organization, Mission, and Information System View, USA, 2011
8 https://www.britannica.com/topic/advanced-persistent-threat
9 See international Journal of Information Security Science, Evaluating Advanced Persistent Threats Mitigation

Effects: A Review, Article – February 2019, Oluwasegun Adelaiye, Aminat Ajibola, Silas Faki

10 https://www.csoonline.com/article/2615666/security/security-5-signs-you-ve-been-hit-with-an-advanced-
persistent-threat.html Parts of this article are presented verbatim above.

www.epc-cep.eu

28 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Increase in elevated logons late at night

•
•  Widespread backdoor Trojans
•  Unexpected information flows
•  Unexpected data bundles
•  Focused spear-phishing campaigns

APT attacks may target financial institutions with the aim to compromise the network or
payment system e.g., to perform unauthorised transactions and steal money.

More details on fraud caused by APT on payment processes and specific payment
instruments, may be found in the Section 3 and 4.

3.1.3.1  Impact and Consequences
The APT’s single-minded persistence on pursuing its target and repeated efforts to complete the
job for which it has been created with malicious intent, makes that the attack will not go away
after one failed attempt. It will continually attempt to penetrate the desired target until it meets
its objective.

Advanced Persistent Threats (APTs) continue to evolve, becoming more sophisticated and
challenging to detect. Here are some of the most recent developments:

•

Increased Use of AI and Machine Learning: APT groups are leveraging AI and ML to
automate reconnaissance, lateral movement, and data exfiltration, making attacks more
stealthy and persistent. For example, AI can be used to learn and mimic user behaviour,
bypassing traditional security measures.

•  Targeting Cloud and ‘Internet of Things’ (IoT) Environments: with the growing adoption of
cloud services and IoT devices, APTs are increasingly targeting these environments. This
shift requires organisations to enhance their security measures for these platforms.
•  Supply Chain Attacks: AI can be used to identify weak links in supply chains and automate
APT attacks on third-party vendors. APTs are focusing on supply chain attacks, where they
compromise a trusted third-party vendor to infiltrate their target. This method was notably
used in the SolarWinds attack, which affected numerous organisations globally.

•  Polymorphic Malware11: APT groups are using polymorphic malware that changes its code
to evade detection by traditional antivirus software. This makes it more challenging for
security systems to identify and block these threats.

Some notable APT Groups have also emerged are:

•  Lazarus Group (Hidden Cobra – North Korea)

Targets: Banks, cryptocurrency exchanges, payment systems, ATMs.
Notable operations:

o  Bangladesh Bank Heist (2016): Stole $81M via SWIFT network manipulation.
o  FASTCash campaigns: Attacked ATM networks in Africa and Asia to dispense

fraudulent cash.

o  Crypto thefts (2020–2024): Billions stolen from exchanges and DeFi platforms.

Relevance: the most active and dangerous financially motivated APT in the world.

11 A polymorphic malware is programmed to repeatedly mutate its appearance or signature files which makes many
traditional cybersecurity tools, such as antivirus or anti-malware solutions, which rely on signature based detection, fail
to recognize and block the threat.

www.epc-cep.eu

29 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

•  APT38 (North Korea – subset of Lazarus)

Targets: Banks and interbank payment systems.
Notable operations:

o  Attacked over 16 banks worldwide between 2014–2018.
o  Known for long dwell times (up to 18 months) before cashing out.

Relevance: focused purely on financial gain rather than espionage; deeply familiar with
SWIFT and interbank messaging systems.

•  Carbanak / FIN7 (Eastern Europe / Russia-linked)

Targets: Commercial banks, POS systems, payment processors, hospitality sector.
Notable operations:

o  Carbanak malware enabled theft of over $1B from 100+ banks globally.
o  Compromised internal systems to trigger unauthorized bank transfers.

Relevance: pioneer in bank network infiltration and supply chain compromise of financial
institutions.

•  Cobalt Group (Cobalt Spider / FIN7 offshoot)

Targets: Financial institutions, ATMs, card payment processors.
Notable operations:

o  Used spear-phishing to distribute Cobalt Strike payloads.
o  Attacked more than 100 banks in 40+ countries.

Relevance: highly technical group that overlaps with criminal and APT tactics.

These examples highlight the need for continuous advancements in cybersecurity measures to
counteract the evolving tactics of APTs.

3.1.3.2  Suggested Controls and Mitigation
APT is deemed a serious threat because of its nature to stay undetected for a long duration. APT
malware is designed to evade detection from conventional perimeter security defences (firewalls,
IDS, IPS, endpoint protection platforms and secure Web gateways) used by most organisations.
APT mitigation and detection capabilities need to be incorporated in a security defence-in-depth
strategy and architecture, to protect enterprises from attacks of this complexity. The traditional
defence-in-depth components are still necessary but are no longer sufficient in protecting against
advanced targeted attacks and advanced malware.

Gartner, an IT research and advisory firm, noting that Advanced Targeted Attacks (ATAs) and
advanced malware continue to plague enterprises, states clearly no single security control is able
to provide effective, efficient protection. An APT defiance strategy needs to include real-time
advanced security data analytics that can identify patterns of invasive behaviour and threat
intelligence for detection-remediation-prosecution or attribution to stop attacks in an early stage.

Today’s APTs are well coordinated, organised, methodical, and sometimes state-sponsored which
makes them particularly difficult to detect by network security administrators, as many APTs use
custom-developed code and/or target zero-day vulnerabilities. Nonetheless, by using technologies
of early detection with real-time reporting and visualisation, network security administrators can
try to perceive penetration as it happens before it disappears through the components of the
system. Also, incorporating security threat intelligence into infrastructures and utilising best-
practice mechanisms and procedures may help find the malware carefully hidden by
cybercriminals inside enterprise networks.

www.epc-cep.eu

30 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

To confront such cyber-attacks will require system users to evaluate weak links in their
infrastructure and employ defence controls that may recognise signs that something appears out
of place. IT security managers need to look for patterns of events characteristic of APT
methodologies. There are many proposed methods for mitigating APT, a few common methods
not in order of effectiveness are highlighted in the following table:

No.

Mitigation Techniques

1
2
3
4
5
6
7
8
9
10
11
12

Traffic/ Data analysis
Pattern Recognition
Anomaly Detection
Awareness
Whitelists
Cryptography
Multi-layer security
Blacklists
Deception
SIEM
Intrusion Detection System (IDS)
Risk assessment

Table 4 Overview mitigation techniques used against APT attacks

Tools such as a SIEM solution try through security logs to detect any unauthorised or suspicious
object access, or else FIM (File Integrity Monitoring) tools and honeypots can detect host-based
attacks on computers and allow early detection of APT behaviour. Also, they can find any cyber-
attacks that bypass signature-based tools and common sandboxes.

Turning the table on attackers, deception technology lures attackers into attacking fake servers,
services and many other networked IT resources that are found in the typical enterprise network.
When attackers waste time and energy attempting to exfiltrate valuable data, security researchers
gather valuable information about the methods they use, including insights into an attacker’s kill
chain, and adjust their network defences accordingly.

To be able to effectively defend against today’s new breed of cyber adversaries, and be able to
counter APT and protect data from inappropriate access, it requires – apart from taking standard
security countermeasures like security hardening and patching of systems, and minimising the
attack surface – strengthening existing authentication flaws (password weaknesses) and properly
utilising proprietary security hardware/software. An advanced IP scanner application, for example,
can help clean any form of malware, including spyware; whereas an APT scanner device that
focuses on detection of attacker activity can be of use should antivirus software and firewalls fail.

Furthermore, to test existing defences and prepare advanced security readiness, security
professionals use the Red Team / Blue Team approach (used also by the military to test force-
readiness) to identify vulnerabilities as part of the offensive attack activities, determine areas for
improvement in the defensive incident response processes, identify opportunities to improve
prevention and detection capabilities and develop response and remediation activities to return
the IT landscape to a secure status. The Red Team is an independent internal or third-party group
that assesses the organisation security readiness, tests active controls and countermeasures
within a given operational environment and validate security defences as well as the ability of
internal security resources to detect and respond to advanced security threats. The Blue Team
consists of internal security resources with the mission to defend the operating environment
against real or simulated cyberattacks over a significant period of time by the Red Team. This is

www.epc-cep.eu

31 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

accomplished by emulating the behaviours and techniques of likely attackers in the most realistic
way possible. Based on the simulation findings, recommendations are provided to increase the
organisation’s cybersecurity readiness posture.

To support the cybersecurity professionals in their fight against Advanced Targeted Attacks,
known as ATAs, Gartner has developed the ‘Five Styles of Advanced Threat Defense Framework’12.
These styles are: network traffic analysis, network forensics, payload analysis, endpoint behaviour
analysis, endpoint forensics, and can be used in combinations for a more effective approach.

3.1.4  Distributed Denial of Service (DDoS)
Distributed Denial of Service, or DDoS, involves crippling the systems of an organisation usually
customer facing websites by flooding the website systems with large amounts of malicious digital
traffic. These attacks are usually carried out by low tier threat actors as they are widely available
for purchase on the internet dark web. Although the impact on the stability of a targeted financial
institution is limited, it can result in reputational damage for the institution and/or may hinder
customer service. DDoS is deployed by actors across the entire actor spectrum, ranging from a
low-skill threat actor using a DDoS attack, to advanced threat actors using DDoS as a smoke screen
for other stages of their attack.

DDoS attacks are one of the oldest internet cyberweapons used today by everyone from
hacktivists and governments to disgruntled video game players and thrill-seekers purely for
personal enjoyment. At the end of the last century, DDoS attacks were performed as a form of
vandalism and without a clear strategy. This changed at the beginning of this century, and DDoS
attacks now have specific objectives. They are used, for instance, to blackmail organisations for
money or to protest against a country or organisation based on ideological motives. DDoS attacks
are more and more often a modern form of protest. The attacks disrupt access to web sites and
servers or take them offline completely by using co-opted online resources such as zombie PCs
and servers or Internet of Things (IoT) bot networks that flood and overwhelm victims with online
traffic. DDoS attacks are performed by many – sometimes hundreds of thousands – nodes at the
same time, grouped in ‘botnets’. In 2016 malware was released to incorporate IoT (Internet of
Things) devices in DDoS botnets. IoT will dramatically increase the number of connected devices
which are poorly patched. Therefore, IoT could give DDoS attackers an unpreceded bandwidth.

The ease for criminals, even low-skill threat actors, to prepare and execute a DoS attack is
increasing. It is relatively easy and not expensive to buy or rent attack capabilities on the Internet.
Two categories of perpetrators may be distinguished: ‘old school hackers’ or ‘hacktivists’ who just
want to have a name or defend an ideology and the ‘hackers that essentially pursue financial gain’.
The latter ones use all means, human or technical failure, available to create blackmail or massive
fraud. Moreover, DoS attacks are also used to conceal other attacks and distract the defenders.

DDoS attacks have been steadily increasing in frequency over the past few years. In its annual
Distributed Denial of Service Insights Report13, which analysed DDoS attack activity and its impact
across industries in the first half of 2023, Zayo Group Holdings, Inc. found that DDoS attacks in the
first part of 2023 were up 200% from 2022. Activity had increased nearly four-fold from Q1 to Q2
in 2023 which Zayo insinuates has been caused by increased automation in the digital world. In a
world of increasing digitisation, political unrest and the emergence of widespread hybrid/remote

12 https://www.gartner.com/en/documents/2576720/five-styles-of-advanced-threat-defense
13 https://go.zayo.com/resources/truth-and-trends-of-ddos-attacks/

www.epc-cep.eu

32 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

working patterns, the need for stringent cybersecurity measures has never been more urgent.
Zayo states that these have all contributed to an increase in DDoS attacks.

Zayo highlights that DDoS has fast become the most common cyberattack against an
organisation’s online presence. They are deliberate attacks to prevent true user traffic from
passing. The scale of these attacks often causes hours of downtime, resulting in immense costs for
businesses, and loss of money, time, customers and reputation. These types of attacks also have
the potential to severely impact key infrastructure and citizens.

Furthermore, in its annual Threat Landscape (ETL) reports, the European Union Agency for
Cybersecurity (ENISA) has consistently highlighted that DDoS attacks are becoming larger and
more complex, increasingly targeting mobile networks and IoT systems, and are often used in
conjunction with other methods as part of broader conflict-related activities.

Largely dormant for years, it has been observed the return of DDoS attacks based on political
motivations. Targets have consisted of government websites, private networks, education
facilities, and critical infrastructure – including financial institutions – of entities that directly or
indirectly have taken sides in the Russia-Ukraine war or other geopolitical tensions between China
and Taiwan, as well as between the US, Israel, and Iran14.

Distinction can be made between four basic types of DDoS attacks:

•  The flooding attack: the term ‘flood’ is a collective term used to describe the most basic
form of DDoS attacks, namely those attacks that focus on making it impossible to gain
access to a system or service, by exceeding the maximum bandwidth available. Exceeding
the maximum available bandwidth means there is not enough bandwidth left for the
legitimate data traffic.
A special form of a flooding attack is the so-called amplification attack, for example a DNS-
amplification attack. In an DNS-amplification attack, the attacker spoofs look-up requests
to domain name system (DNS) servers to hide the source of the exploit and direct the
response to the target. Through various techniques, the attacker turns a small DNS query
into a much larger payload directed at the target network.
The size of attacks is increasing, caused by the number of infected end points. Moreover,
the possibility to increase the size of an attack by combining it with an amplification attack
is worrying.

•  The protocol attack: another way of causing a DDoS attack is to send data packets that

take advantage of weaknesses in the communication protocols and other protocols used
mainly by network devices such as routers and firewalls. These devices receive packets for
processing that lead to unexpected results. For example, a large number of communication
sessions are opened without being properly closed in due time, this way consuming the
resources of the network device. As a result, they can no longer accept any new sessions.
Well-known examples of protocol-attacks are SYN floods, fragmented packet attacks, Ping
of Death and Smurf-attacks. The number of SYN-flooding attacks is increasing. In many
cases the botnets used contain so called Internet of Things (IoT) devices. Examples of these
devices are consumer electronics like home-routers, IP-cameras and smart-TV’s. There are
a lot of these devices nowadays and most of them are badly administered, resulting in non-
patched systems and default administrator credentials.

14 https://www.akamai.com/site/en/documents/research-paper/the-evolution-of-ddos-return-of-the-
hacktivists.pdf?utm_campaign=F-MC-59113

www.epc-cep.eu

33 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

•  The application-layer attack: an application layer DDoS attack is named after the OSI-

layers’ Application Layer (layer 7). The attacker is aiming at a specific function of a layer 7
protocol like http and misuses that function to exhaust the service. An example is the
misuse of the GET/POST-function of http, performing a so-called slow attack which causes
the web server to wait for a long time before answering the request of a web browser. An
attack is disguised to look like legitimate traffic, except that it targets a specific function of
the protocol it attacks. There is often not much bandwidth consumed and the e.g. web
server just crashes. Application-layer attacks cannot be recognised as a DoS-attack during
the encrypted transport. Only after decryption an application-layer attack can be
recognised and mitigated.

•  Combined attacks: at present combined attacks are becoming more frequent, using for

example floodings and application-layer attacks at the same time, making mitigation of the
attacks more complex.

DDoS attacks can also be used as an extortion-scheme. In this case, the victim receives an e-mail
from an attack group asking for a (large) sum of money to prevent a (much larger) DDoS attack.
Sometimes the email is preceded by the DDoS, as a proof of competence. The extortion message
often refers to ‘vivid’ scenarios that are attributed to this offender group.

3.1.4.1  Impact and Consequences
Akamai’s annual threat intelligence reports highlight continuing growth and evolution in DDoS
activity, particularly against the financial services sector, which has emerged as one of the primary
targets. The rise is driven by increasingly powerful botnets and hacktivist operations often linked
to geopolitical tensions. The Europe, Middle East, and Africa (EMEA) region has seen a significant
rise in DDoS attacks, particularly against financial services, gambling, and manufacturing sectors.
This trend is expected to continue due to ongoing geopolitical issues. Furthermore attackers are
combining DDoS attacks with ransomware and web application zero-day exploits to create more
complex and damaging threats. This method, known as triple extortion, is becoming more
prevalent.

When people think of DDoS attacks, they focus on the outliers, the massive Terabit attacks that
generate headlines. But the smaller, more focused attacks can do just as much damage. More
importantly, these smaller attacks are actually more common than their larger-scale counterparts.
Sometimes, criminals will attempt credential stuffing attacks side by side with distractions, such as
DDoS attacks, or they will skip the credentials and attempt to exploit applications or website
vulnerabilities on the target’s domain.

DDoS attacks are a problem for any organisation, but they are especially a problem for the
financial services industry. The financial services sector is still a prime target for cyber criminals.
According to Boston Consulting Group research, financial service firms are up to 300 times more
likely to experience a cyber-attack per year compared to companies in other industries. With the
global pandemic and remote working driving significant increases in DDoS attacks on financial
services in the first half of 2020 this appears to be a trend that is set to continue. A successful
DDoS in the financial world could mean millions of euros lost for each minute of downtime. As
mentioned, sometimes criminals will launch DDoS attacks as a distraction, either to conduct
credential stuffing attacks or to exploit a web-based vulnerability. The banking, financial services
and insurance (BFSI) sector continues to rank among the industry’s most frequently targeted by
DDoS attacks, consistently accounting for a significant share of global attack volume. This reflects
an ongoing trend of rising threat activity against financial institutions, while sectors such as
telecommunications, technology, and education also remain prominent targets. Collectively, these

www.epc-cep.eu

34 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

industries represent the majority of recorded DDoS incidents, whereas sectors like energy, retail,
healthcare, transportation, and legal experience comparatively lower levels of activity. The
potential impact of a DDoS attack is twofold. On the one hand it can lead to the temporary
unavailability of a PSP, including all its services, e.g. Internet banking, mobile banking, but also
non-payment related services. And that can again lead to a form of blackmail (see next paragraph)
by the attacker and/or – caused by a focus of many on re-establishing the service – a potential
increase in successful fraud attempts. On the other hand, a consequence can be damage to the
reputation of the attacked PSP, where e.g. the Internet banking service is ‘again’ not available.

A group calling themselves ‘Cozy Bear’ has been emailing various companies with an extortion
letter, demanding payment and threatening targeted DDoS attacks if their demands are not met.
Cozy Bear, also known as APT29, is known for its customized malware and attacks on commercial
entities and government organisations across the globe. Akamai believes the letter is from a
copycat group leveraging the Cozy Bear name as a means to invoke fear and panic. Their extortion
letter actually suggests victims perform a Google search on their name, which immediately returns
results related to the infamous group. So far, multiple companies have reported receiving an email
demanding a sum of about $17,500 in Bitcoin, or 2 BTC, at the time this advisory was written. If
the payments are not made before the deadline expires (usually 6 days), the price increases by 1
BTC each day the demand is not met, and the targeted DDoS attack will start. This is not the first
time that DDoS extortion demands have circulated across the Internet. In 2015, Akamai published
research concerning a group calling itself DD4BC (DDoS 4 Bitcoin), which was responsible for a
number of DDoS attacks. Apparently clinging to the hope of a major Bitcoin payout, criminal actors
have started to ramp up their efforts and their attack bandwidth, which puts to rest any notion
that DDoS extortion was old news. Extortion or ransom DDoS (RDDoS) attacks started to become a
new threat in 2020 and grew bigger and more complex since then. They started around 200Gbps
and then flexed to more than 500Gbps in mid-September. In February 2021, internet security
services company Akamai saw its share of a challenge dealing with an 800Gbps RDDoS that
targeted a gambling company in Europe. Last September, a threat actor deployed an RDDoS
against VoIP.ms voice-over-Internet provider, disrupting phone services as the company’s DNS
servers became unreachable.

It is clear that DDoS attacks are not a PSP specific issue, but it is also a threat to the whole financial
sector. The threat is well known now in the sector and most PSPs have taken mitigating measures
against these kinds of threats (see below).

3.1.4.2  Suggested Controls and Mitigation
PSPs should preferably set up a (DDoS) security control framework. In general terms they should
be able to identify, protect, detect, respond, recover, assess and adjust possible DDoS attacks. The
table below gives a high-level description of these controls 47F

15.

Level

Identify

Protect

Description

Develop the organisational understanding to manage DDoS risk to systems,
assets, data and capabilities

Develop  and  implement  the  appropriate  safeguards  to  ensure  delivery  of
critical infrastructure services

15 more details may be found in Chapter 5 in http://www.vurore.nl/images/vurore/downloads/scripties/2040-

Def.scriptie_LarsDrost.pdf

www.epc-cep.eu

35 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Detect

Respond

Recover

Assess

Adjust

Develop and implement the appropriate activities to identify the occurrence
of a DDoS attack

Develop and implement the appropriate activities to take action regarding a
detected cybersecurity event

Develop  and  implement  the  appropriate  activities  to  maintain  plans  for
resilience to restore any capabilities or services that were impaired due to a
DDoS event

Determine whether the previous functions performed/functioned effectively

Determine which changes need to be made, based on the assessment made

Table 5 High-level dynamic DDoS security control framework

The Internet Engineering Task Force (IETF) established a new working group called DDoS Open
Threat Signalling (DOTS). The aim of DOTS is to develop a standard based approach for the real
time signalling of DDoS related telemetry and threat handling requests and data between
elements concerned with DDoS attack detection, classification, trace-back, and mitigation.

In general, PSPs are expected to have implemented a so-called ‘DDoS mitigation scrubbing
service’. This is a service to filter the fraudulent traffic of the DDoS attacks. Scrubbing is more
specifically a good mitigating measure against flooding attacks and sometimes mitigating protocol-
attacks. Scrubbing services are provided by third party service providers.

Since protocol- and application attacks comply with the standard for the protocol in question, it is
more difficult to counteract such attacks. PSPs have implemented or should implement mitigating
measures against application level attacks including for instance application-level security
products, application level key completion indicators, filtering capabilities, etc.

PSPs can simulate attacks on their environment in order to prove that mitigating measures
(including organisation and personnel) are adequate. Moreover, every entity should also test
periodically their anti DDoS measures (e.g. through DDoS simulations). This testing should cover
both the technical and the organisational aspects (e.g. procedures).

One additional set of countermeasures is to organise security intelligence. It is important to know
what types of DDoS and what type of actors and motivations are around; it helps to take accurate
measures and to determine the (residual) risk of the organisation of getting hit by DDoS-attacks.
Security intelligence can be received from a commercial organisation and/or a governmental or
industry specific Computer Emergency Response Team (CERT), which are a good answer to deter
the effects of DDoS activities.

PSPs should consult their upstream ECSP and the local Law Enforcement Agency to check whether
the logging capabilities of the PSP and the monitoring solutions of the PSP offer sufficient
capabilities for the PSP to be ‘forensic ready’ for law enforcement.

3.1.5  Botnets
A botnet is a collection of internet-connected devices compromised by an attacker who
orchestrates through a C&C, without the knowledge of the victim.

Botnets act as a force multiplier for malicious activity. Commonly used for DDoS attacks, attackers
also make use of the botnets’ collective power to scale attacks such as spamming, credential
compromise, delivering malware or cryptocurrency mining. The word ‘botnet’ is a combination of
the words ‘robot’ and ‘network’.

www.epc-cep.eu

36 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Botnets have two main objectives:

•  Herding more devices into the botnet and;
•  Performing malicious activity.

The malicious activity performed by a botnet can be of a wide variety, namely:

Distributed  Denial  of  Service  (DDoS):  Botnets  usually  consist  of  such  large  numbers  of  remote
machines that their cumulative bandwidth can reach hundreds of gigabytes of upstream traffic per
second. This enables botmasters to start targeted sabotage attacks against websites. The usage of
botnets that are becoming more and more intelligent will create flexible tools for the execution of
DDoS attacks.

Spam email: One of the most popular uses of botnets was spamming: the ability of botnets to use
bots’ IP addresses to hide the true originator of the spam email complicates countermeasures such
as the blacklisting of suspicious IP addresses. Nowadays phishing is done less by botnets as more
SIM cards are being used (‘smishing’) for this purpose.

Credential harvesting: A major use of botnets, with the intention of gaining financial benefits, is for
the automated extraction of user data and credentials from infected hosts.
Man-in-the browser malware to intercept online banking credentials is one of the attack vectors
that can achieve a large-scale attack through the use of a botnet.

Account testing fraud: Cybercriminals can scan a range of IP addresses to find a specific port, and
then bombard the service – FTP, Telnet, RDP or others – with rapid-fire authentication credentials
from a list they have developed or bought in the underground market. In the electronic payments
sector this can be used to test credit card numbers or online banking accounts.

Cryptocurrency mining: Cryptocurrency mining requires intensive computing power. Botnets are a
preferred  means  to  mine  crypto-currency  drawing  on  the  victim’s  system  computing  power  and
electricity.
Many other malicious activities may be performed benefitting from the large scale offered by
botnets, such as:

•  Click and pay-per-install fraud;
•  Manipulation of online polls;
•  Denial of inventory;
•  CAPCHA solving;
•  Hosting illegal downloads.

AI is also used to coordinate large-scale botnets, optimize attack timing, and evade mitigation
efforts. AI enables botnets to self-organize, adapt to takedown attempts, and maximize the impact
of attacks such as credential stuffing, spam, and crypto-mining.

Nowadays, botnets seem to focus more and more on ransomware and not on fraud related
activities. Notorious banking malware botnets such as Emotet are an example.

Emotet has been one of the most professional and long lasting cybercrime services out there. First
discovered as a banking Trojan in 2014, the malware evolved into the go-to solution for
cybercriminals over the years. The EMOTET infrastructure essentially acted as a primary door
opener for computer systems on a global scale. Once this unauthorised access was established,
these were sold to other top-level criminal groups to deploy further illicit activities such data theft
and extortion through ransomware. However, the Emotet botnet was successfully taken down in

www.epc-cep.eu

37 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

January 2021; Europol announced in a Press Release16 that Emotet had been disrupted and
investigators had taken control of its infrastructure. More than 500 servers from different tiers
were taken down of the criminal infrastructure. A database containing e-mail addresses,
usernames and passwords stolen by Emotet was compiled by analysing all the seized
infrastructure. This operation is the result of a collaborative effort between authorities in the
Netherlands, Germany, the United States, the United Kingdom, France, Lithuania, Canada and
Ukraine, with international activity coordinated by Europol and Eurojust. This operation was
carried out in the framework of the European Multidisciplinary Platform Against Criminal Threats
(EMPACT).

Law enforcement agencies worldwide have made significant efforts to disrupt these criminal
networks. Collaborative operations involving multiple countries have successfully dismantled
major botnet infrastructures, seizing servers, freezing illegal proceeds, and preventing further
harm. These actions often require international coordination and advanced technical strategies to
effectively neutralize the threat.

3.1.5.1  Impact and Consequences
A few evolutions have occurred to botnets in the last years, in respect to their C&C strategy, to the
types of infected devices, to the malicious activity and to the commercial model of botnets.

C&C strategy – Centralised to decentralised
The most important part of a botnet is the so-called C&C infrastructure from where the attacker
can control the botnet giving instructions to the bots and receiving collected data from them.

The first botnets would have a centralised approach comparable to the classic client-server
network model. Newer botnets use a decentralised, i.e. peer-to-peer, model in order to try and
evade detection and to be more resilient in face of takedown attempts.

The bots maintain connectivity to other bots and issue requests for new commands to the botnet.
Because there is no single set of command servers that can serve as a single point of failure, and
the botmaster can hide inside the network of bots when giving commands, this approach is harder
to mitigate.

Types of infected devices – Computers to IoT
The compromised systems in traditional botnets were almost exclusively computers, recent
botnets compromise IoT devices such as cameras, routers, Digital Video Recorders (DVRs),
wearables and other embedded technologies. IoT botnets tend to be larger in scale due to a set of
characteristics of the compromised systems:

•

IoT devices are usually designed with lowering costs as a major driver and security interests
tend to be neglected. As a result, these embedded devices are easily exploited (e.g.,
default credentials, exposed services).

•  These devices are in many cases not subject to patching or firmware upgrades leaving large

numbers of devices subject to exploitation of already published vulnerabilities.

•  Many of these devices are permanently online and available 24x365, resulting in a larger

exposure surface from the beginning of an exploit.

•  Devices are rarely monitored, preventing timely detection.

16  https://www.europol.europa.eu/newsroom/news/world%E2%80%99s-most-dangerous-malware-emotet-disrupted-
through-global-action

www.epc-cep.eu

38 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Botnet malicious activity – Crypto-currency mining
Botnets are the basis for certain types of attacks such as DDoS and spam mailing; and are a way to
enlarge the scale of other attack types.

Using botnets for crypto-currency mining, perfectly fits the objective of the attackers. It offers the
vast computing capacity, managed through the compromised devices, and the tremendous usage
of electricity power, both unknowingly supported by the victims, required for crypto-currency
mining. The fact that victims sense no apparent harm makes detection less probable and turns the
botnet even more profitable.

Commercial model of botnets – Botnet kits
For some years, botnets have been offered as a commodity either through selling subparts of the
botnet or by leasing botnets. More recently botnet kits have been behind some major botnets. .

3.1.5.2  Suggested Controls and Mitigation
The Council to Secure the Digital Economy (CSDE) provides international guidance on securing
networks and connected devices against botnet threats. Its published framework outlines a
comprehensive set of mechanisms and processes to mitigate attacks originating from botnets.
These measures are organized across key domains, including infrastructure, software
development, and IoT device security, with additional recommendations tailored to home and
small business systems as well as enterprise environments.

Authorities should collaborate with Internet Service Providers (ISPs) to restrict or temporarily limit
Internet access for customers identified or suspected as part of a botnet. Such users should be
isolated within a controlled quarantine network until the threat is neutralized. These cooperative
procedures should be formalized within the ISPs’ Service Level Agreements (SLAs).

 The European Union Agency for Cybersecurity (ENISA) also offers comprehensive guidance on
botnet detection, measurement, disinfection, and defence. Its reference materials encompass
technical, organisational, and regulatory measures supporting long-term mitigation strategies.

Technical countermeasures

•  Blacklisting
•  Sinkholing
•  Orchestration of controls at host and network level
•  Vulnerability management in combination with regular updates
•  Distribution of fake/traceable credentials
•  DNS-based countermeasures
•  Direct takedown of C&C server
•  Packet filtering on network and application level
•  Walled gardens
•  Peer-to-peer countermeasures
•  Quarantine Infected Computers
•

Infiltration and remote disinfection.

Regulatory and social countermeasures
•  Dedicated laws on cybercrime
•  User awareness raising and special training

www.epc-cep.eu

39 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

•  Central incident help desk
•  Enhance cooperation between stakeholders.

3.1.6  Third-party compromise, supply chain attacks and IT outages
It is quite common that banks, and in general PSPs, rely on third-party vendors to provide services
and products to their customers. For example, processes outsourced by banks may include
customer service, credit cards, data entry operations, ATM services or even entire business
functions such as risk management and IT support.

AI is also used to analyze software supply chains, identify vulnerabilities, and automate
exploitation.

It is clear that third party vendors are critical for every organisation’s business, especially for PSPs.
But they also introduce cyber risk. Because of the inherent trust relationships, unsecure suppliers
in the PSPs’ chain can become the entry point for attackers. This kind of attack is known under the
name ‘supply chain attack’. According to ENISA17, a supply chain attack is a combination of at least
two attacks: the first attack is on a supplier that is then used to attack the actual target. The target
can be the final customer or another supplier. Therefore, to classify an attack as a ‘supply chain
attack’, both the supplier and the customer have to be targets.

A distinction can be made between two basic types of supply chain attacks:

•

•

In software supply chain attacks malicious actors exploit the software vendor of their
targets. It is accomplished by compromising staged of the software development lifecycle.
Most of the times, attackers target software updates. Threat actors first gain access to the
software’s update server and then inject malicious code into the update packages. Once
that the target organisation downloads and installs the malicious packages from its
suppliers, malicious actors can gain access to the organisation’s network.

In hardware supply chain attacks, physical components are tampered with. For example, a
manufacturer can install a malicious microchip on a circuit board used to build servers and
other network components. These kinds of supply attacks are very rare as they require the
cooperation of manufacturers and vendors.

Although not always present in the literature, it is worth to mention also the risks introduced by
using open-source software libraries as they are widely used due to decrease development time
and costs. Should a third-party library developer inject malicious code into the product, any
software developer that incorporates the infected library would be vulnerable.

Even though supply chain attacks have been a security concern for many years, they increased in
number and sophistication. Among the most important and recent incidents it is worth to mention
Solarwinds, Accellion, Kaseya, and Log4j that affected many organisations from all over the world.

Furthermore, it is also worth highlighting the risks arising from any IT outages of third-party
organisations. Similarly, such events can cause the shutdown of critical services such as payment
systems, ATMs, and branch operations.

As financial institutions increasingly rely on CSPs, it is worth noting that the industry is facing new
security challenges such as:

17 https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks

www.epc-cep.eu

40 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

•  Systemic risk from provider concentration: high reliance on a small number of CSPs can
create financial stability concerns. An outage at one provider could trigger simultaneous
service disruptions for many financial institutions.

•  Cloud specific cyber-attacks: traditional attacks still target cloud platform providers but
ultimately impact end users. Techniques like hyperjacking can be used to steal sensitive
data, including financial information.

•  Data loss from inadequate backup/recovery: poor backup and disaster recovery

capabilities in cloud environments can result in permanent data loss.

•  Credential compromise: weak or stolen cloud computing credentials are the leading cause

of data breaches.

The above list represents only a subset of the potential cyber risks and threats and does not
address important compliance-related challenges, which also require careful consideration.

In the light of a such strong interconnectivity among systems and processes across network and
organisations, PSPs need to manage such risks in order to prevent data breaches, financial losses,
and operational failures.

3.1.6.1  Impact and Consequences
Unfortunately, due to the lack of visibility on third-party vendors, supply chain attacks are hard to
detect for any organisation: once a threat actor bypasses the security perimeter of the target
through a software vendor, it can maintain persistent access for a long time. In addition, if the
threat actor loses the access to the victim’s network, he can re-gain access through the
compromised software vendor.

Such kind of attacks have severe impacts which can devastate corporate revenue, brand
reputation, and vendor relationships. The main impacts from supply chain attacks are:

•  Data breaches and data disclosure: Any data that passes through a system infected with
the malicious code could be breached, including potentially stealing high-privileged
account credentials for future compromises, corporate information and financial
information.

•  Malware installation: Ransomware, rootkits, keyloggers, viruses, and other malware could

be installed using injected supply chain attack code.

•  Reputational damage: loss of customers, loss of sales, reduction in profit can be some of

the negative effects caused by supply chain attacks.

•  Unavailability: Critical systems and services, such as payment systems and ATMs, may go

offline causing significant disruption.

Furthermore, most of the data breaches experienced by financial organisations and third-parties
result in the loss of customers and employees’ sensitive data increasing the risk of identity theft,
fraud, or other malicious activity against citizens.

Fortunately, no incident has yet significantly impaired PSPs. It is nevertheless useful to provide
some examples to illustrate how a cyber incident may have impact on PSPs and the financial
system.

Among the most sophisticated and disruptive attacks seen in the past, we highlight the incident
happened in 2020 that affected SolarWinds and its customers. SolarWinds customers, which
included large financial institutions, were infected by the malware when they installed the
software update. The attack opened a backdoor through which attackers could have exploited the
customers’ computer systems. As previously mentioned, no PSPs appeared to have been the

www.epc-cep.eu

41 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

intended targets of such attacks. However, if they had been, the consequences for the interested
PSPs and the whole financial sector could have been devastating.

Worth mentioning are also the risks associated with digital operations when providers experience
long outages. For example, in 2019, Google experienced a network outage that impacted services
hosted on Google Cloud Platform in some US regions. The outage lasted for more than four hours
and affected access to various services. If PSPs had transitioned their business activities to the
cloud, the outage could have disrupted their payment services. Another example is that of a major
bank that in 2016, due to an outage cause by a technological issue inside one of the platforms
hosted by the bank itself, was unable to process payment instructions sent over the Swift network
from clients for 19 hours18. Finally, we report the case of an outage of a bank’s data centre caused
by a smoke condition19. It caused an automatic shut off of power resulting in the unavailability of
some customer accounts through online/mobile banking applications and ATMs.

In July 2024, a global outage affected about 8.5 million Windows devices. This outage was caused
by un update that pushed a faulty "sensor configuration update" to the millions of PCs worldwide
running Falcon Sensor software20. Such outage impacted also the Banking sector causing in some
cases the unavailability of payment systems, ATMs and bank’s internal servers.

In august 2024, a ransomware attacks experienced by C-Edge Technologies, a technology service
provider, forced nearly 300 Indian banks to go offline causing the temporary disruption of all
online transactions, including RTGS and UPI payments21.

The previous examples show in what measure the PSPs physical and digital operations are heavily
interconnected, and problems in either can affect the other.

3.1.6.2  Suggested Controls and Mitigation
The management of relations with suppliers – and consequently with any sub-suppliers – is of
crucial importance in banking and financial legislation. Until now, however, this importance was
reserved only for IT service providers to whom financial entities outsource essential or important
services or functions, providing for mostly general rules. Furthermore, the regulation of relations
with these service providers was given by monitoring and control obligations incumbent solely on
banks and financial institutions, which therefore included these obligations in the contracts with
their ICT service providers, without however there being a clear system of rules which specifically,
clearly and targeted regulated the contractual provisions stipulated with these subjects.

As a result, the effectiveness of such contractual clauses often depend on the negotiating power
of the service provider.

The DORA [6] Regulation, which applies since January 2025, establishes in Chapter V, the
fundamental principles that guide the management, by financial entities, of IT risks deriving from
third parties, which are considered as an integral part of their own risks.

To this end, it should be noted that DORA does not only deal with outsourcers of ICT services, but
speaks in general of ‘ICT service providers’, which means that the spectrum of subjects with whom

18 https://www.pymnts.com/bank-regulation/2016/bny-mellon-unable-to-run-payments-for-19-hours/
19 https://www.cnbc.com/2019/02/08/wells-fargo-says-working-to-fully-restore-system-as-outage-spills-into-day-
2.html
20 Falcon Sensor is produced by a trusted software developer firm called CrowdStrike Holdings
21 https://www.reuters.com/technology/cybersecurity/small-indian-banks-back-online-after-ransomware-attack-
payments-authority-says-2024-08-01/

www.epc-cep.eu

42 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

financial institutions must adequately regulate their relationships is broadened, extending it to all
types of ICT service provision (for example, the supplier of hardware devices that carries out
maintenance and assistance on them will also be the recipient of the legislation). The following
points provide some provisions aimed to strengthen the digital resilience financial operators
involving third-parties services providers:

•

In order to understand the complex interconnection and any vulnerabilities, DORA requires
the mapping of all ICT systems and assets of financial institutions. Third-party services
providers are included in such mapping.

•  DORA enables regulators and financial institutions to perform audits throughout the supply

chain in the financial industry.

•  DORA requires the definition of a third-party management framework such as the

nomination of executives responsible for operational resilience.

•  DORA requires firms to set specific requirements for outsourcing ICT systems and services
to third parties. In addition, critical third-party providers are obliged to comply with the
same rules as financial institutions.

Therefore, it should be highlighted that as best practice, each PSPs should apply a risks assessment
process able to identify dependencies on third-party suppliers of these services and assets. Such
analysis should identify critical IT supplier dependencies, customer dependencies, the mapping of
critical software and single point of failure22.

To conclude, it is worth to mention also the eight key practices suggested by NIST for establishing
a Cyber Supply Chain Risk Management (C-SCRM) approach that can be applied to software23:

1.  Integrate C-SCRM across the organisation.
2.  Establish a formal C-SCRM program.
3.  Know and manage critical components and suppliers.
4.  Understand the organisation’s supply chain.
5.  Closely collaborate with key suppliers.
6.  Include key suppliers in resilience and improvement activities.
7.  Assess and monitor throughout the supplier relationship.
8.  Plan for the full lifecycle.

These practices can assist PSPs in preventing, mitigating and responding to software vulnerabilities
that may be introduced through the cyber supply chain and exploited by malicious actors.

3.1.7  Monetisation Channels
A fraudster who succeeded to establish a fraudulent payment transaction (whether authorised or
unauthorised), knows that investigators soon will follow the trace and that the transaction amount
may be frozen or returned. He therefore aims at immediately leveraging a monetisation channel: a
cash withdrawal, a purchase (that leaves no trace), a money transfer or a transfer to another bank
account from which again a withdrawal, purchase or transfer may be initiated. Purchases that
leave no trace may include buying crypto currencies or acquiring gambling credits or goods that
can easily be cashed in over the internet. Common examples of such goods include airline tickets

22 https://www.enisa.europa.eu/publications/good-practices-for-supply-chain-cybersecurity
23 Jon Boyens, et al., ‘Key Practices in Cyber Supply Chain Risk Management: Observations from Industry’, NISTIR 8276
(February 2021), https://doi.org/10.6028/NIST.IR.8276

www.epc-cep.eu

43 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

and any type of vouchers or gift cards but may also include more expensive items such as
jewellery or electronic equipment.

However, especially in a corporate context the fraudster’s monetisation options are not limited
only to the immediate use of liquid funds available via the victim’s payment account, credit card,
etc. but may include also cover acts such as brokering access to breached systems, data or user
accounts, modification or encryption of data for subsequent extortion purposes, etc.

AI can also help fraudsters automate the movement of funds through mule accounts,
cryptocurrencies, and other channels, making detection and investigation more challenging.

3.1.7.1  Impact and Consequences
To stay in the shadows, the fraudster hires ‘money mules’ and uses their bank accounts to receive
the fraudulent transfers and the mules themselves – according to the fraudster’s instructions – to
bring the spoils to the fraudster in a way it cannot be tracked. The mule is, willingly or unwillingly,
knowingly or unknowingly, covering the fraudster’s tracks. The emergence and rapid expansion of
crime-as-a-service made money muling services readily available via darknet marketplaces and
instead of recruiting them, the fraudster can choose to hire money mules as, and when, needed.

Most mules will eventually be subject to investigations and reported to the police. If there are any
funds left on a mule’s account after paying the fraudster, the mule will likely be forced to return
the amount that was stolen from the original victim. Hence, it seems that a mule is bound to lose,
but nevertheless new recruits are constantly being persuaded to act as such24.

When a fraudster has established the necessary mule(s), the fraudster will orchestrate the
combination of conducting one or more fraudulent transactions and using the mule(s) to get the
money out of sight. The actual flow may depend on the size of the amount(s) and the needed level
of complexity to escape investigators. Especially cross-border transfers and more in particular
instant payments make investigations and fund recovery more difficult and complex.

Two examples of flows involving money mules are provided below. While complexity makes it
harder for investigators, it also increases significantly the fraudsters’ effort and risks. Most cases
are therefore not very complex and do not involve more than one or two levels of mules. When
needed professional mules can be sourced ‘as a service’ to make things easier for a fraudster.

Figure 1: Classic money mule flow

24 See a comprehensive description of ‘The money mule trap’ at FINTRAIL

www.epc-cep.eu

44 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Figure 2: Classic upscaled money mule flow

A critical step is when the money finally leaves the banking system through any kind of transaction
that covers the tracks sufficiently for the criminals. In the flows above the mule withdraws cash
and often sends it to the fraudster via money transfer service to preserve anonymity. However
other modi operandi may be employed in which money mules can be avoided or digitised:

•  By directly purchasing valuable assets (ideally digital) which can easily be cashed-in over

the internet.

•  By directly initiating a fraudulent payment to a money transfer service account (such

service supporting withdrawal around the globe with varying levels of identity verification).

•  By directly buying hard-to-investigate or hard-to-trace crypto currencies.

Anonymity of crypto currencies exploited as a replacement for mules
While money transfer services have always played a key role in enabling fraudsters to hide behind
the money mules, anonymous virtual currencies have been identified as an often much more
efficient replacement for both. Virtual currencies are defined by the European Banking Authority
(EBA) as ‘a digital representation of value that is neither issued by a central bank or public
authority nor necessarily attached to a fiat currency but is used by natural or legal persons as a
means of exchange and can be transferred, stored or traded electronically’25.7

Over the last few years, popularity of virtual currencies has skyrocketed, due to the surge of
decentralised digital currencies, like Bitcoin, the first to appear in 2009 and still the most
important of them. Decentralisation means that one person can pay directly to another without
using a third party as an intermediary, something that before was only possible using cash. It is for
this reason that decentralised digital currencies are commonly considered ‘digital cash’ and
currently achieve a market capitalisation of more than 3000 billion euros7

26.

In Bitcoin-like schemes, trust is provided by a mix of technologies that include primarily
cryptography, instead of being provided by a trusted third party. Therefore, these kinds of
decentralised currencies are also referred to as cryptocurrencies. As such they allow for reliable,
fast and irreversible online transactions, are not centrally controlled, have no built-in know-your-
customer (KYC) mechanism, and are relatively difficult to trace. Therefore, they have also become
a magnet for criminals. Indeed, their illicit use is increasingly happening as criminals are gradually
accepting it as a currency of choice for trade in the darknet.

25 https://www.eba.europa.eu/documents/10180/657547/EBA-Op-2014-08+Opinion+on+Virtual+Currencies.pdf
26 Cryptocurrency market capitalisation is available at https://coinmarketcap.com/

www.epc-cep.eu

45 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Although all crypto currency transactions are stored publicly and permanently on the network by
means of blockchain technology, the identity of a user behind an address can remain unknown.
Moreover, Bitcoin mixer services have appeared, with the aim to provide obfuscation of the flow
of funds in exchange for a fee, allowing fraudsters to move and cash-out the stolen funds
anonymously.

3.1.7.2  Suggested Controls and Mitigation
Money mules, anonymous or non-traceable money transfers, crypto currency services, but also
instant payments make it easier for fraudsters and harder for fraud investigators.

Raise Awareness
It is not generally understood that when a person receives some money (e.g. via a mobile P2P or
banking app), withdraws the same amount from an ATM and passes on the cash to some friendly
person they just met, they might have in reality helped to cover up a crime. Awareness is
especially necessary towards youngsters, who due to natural lack of experience, low income,
willingness to-help-out and sometimes some ‘peer pressure’, seem more prone to become mules.
PSPs should be careful to give easy-to-understand warnings against ‘becoming a mule’ when they
provide access to on-line banking services or issue payment cards. Awareness must also target
other identified ‘vulnerable’ groups (such as low-income persons, addicts, etc.) tempted by
seemingly easy money and unaware of law and consequences27.

Register/ share identified mules
For those mules who know what they are doing and do it for gains, awareness is not relevant.
Instead, PSPs should cooperate to achieve that the same person cannot act as colluding mule
again and again by shifting to a new PSP. It should be possible to register in a common database if
a person repeatedly has acted as a mule, subject to respect of data protection laws (e.g.,
GDPR[4]). This should not necessarily hinder this person to open a payment account, but it should
enable monitoring to detect possible new mule activity by this person at a very early stage.

Monitor, detect and stop mule-like behaviour at PSP and regulator level
Regulators and PSPs should consider having mechanisms in place to react and stop supporting
service practices or to put related transactions on hold, until further investigated, if transaction
patterns indicate ‘mule activity’ – e.g., if larger amounts arrive from or flow to new (unknown)
sources, followed by attempts to cash out or pass on these amounts via other ways.

Detect complex mule and money laundering schemes
For a single PSP it may end up being very difficult to ‘follow the track’ if there are many mule-
levels and cross-border payments are involved. However, if PSPs cooperate and pool their
payment data (in a secure and lawful way), it may be possible to use strong analysis tools and
much more efficiently detect mule accounts and money laundering rings. Whereas the first mule
level has a short lifetime, subsequent mule-levels may re-use accounts over a longer period if they
can stay undetected. Analysis on pooled data can put a significant pressure on money mule
schemes. To be effective in the long run such cooperation must be cross-border and will become
even more important in view of instant payments, which are gradually becoming the new normal.

27 See ‘The money mule trap’ at FINTRAIL

www.epc-cep.eu

46 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

3.2  Fraud per Payment-Relevant Process

Introduction

3.2.1
This section describes various attacks that may lead to fraud, occurring in all payment-relevant
processes of a business transaction. Often attacks are caused by exploiting a combination of
several threats. Multi-vector attacks are becoming commonplace and have been targeting a
number of financial institutions (e.g. recent examples of multi-vector attacks include cyberattacks
using the SWIFT-related banking infrastructure, ATM infections, remote banking systems and POS
28, making changes in PSP’ databases to ‘play’ with account balances, as well as
terminal networks83F
supply-chain attacks, i.e. attacks on vendors supplying financial organisations 84F

).).

29

The table below provides a non-exhaustive view on possible impact of threats and fraud enablers
on payment-relevant processes.

Social engineering  Malware

APT

DoS

On-boarding/ Provisioning
Payment request / Invoicing
Initiation/ Authentication
Execution

X
X
X
X
Table 6 Possible impact of threats and fraud enablers on payment-relevant processes

X
X
X
X

X

X

3.2.2  On-boarding and Provisioning
The different types of attacks against on-boarding or provisioning processes, are:

•  Manipulation of identity-relevant information in an authoritative registry e.g., change the
surface mailing address for hardware credentials (authenticator or payment cards) or the
mobile number for SMS one time passwords (OTP) and then trigger a delivery to the
modified destination.

•  Exploit oversimplified ordering of credentials to a registered address, with the intention to
physically steal the credentials from the client’s mailbox upon delivery by the post services.

•  Fake enrolment with stolen credentials to a payment app, mobile bank app or general
authenticator app. If login credentials can also be used for activation this is very
convenient, as it allows the fraudster to delay payment execution until a later time that
better suits the attack.

•  Deepfake and other AI-enabled scams to exploit/fool digital onboarding and other digital
verification processes by creating deepfake (cloned/fictitious) videos, audios, images or
documents, using, easily and cheaply available, generative Artificial Intelligence (AI)
software tools. The capabilities of these AI software tools, which could be used for
fraudulent purposes, are continuously evolving.

•  SIM swapping or duplicate SIM attacks in case the bank uses SMS OTP and the network
operator’s client authentication procedure is easier to overcome than any of the bank’s
procedures.

28 See for example: https://www.tripwire.com/state-of-security/security-data-protection/hackers-indian-bank-attack/
29 https://securelist.com/cybercriminals-vs-financial-institutions/83370/

www.epc-cep.eu

47 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Manipulation of identity-relevant information
Already in the on-boarding process a fraudster could be involved. The purpose for the fraudster
can be e.g., to obtain tax returns intended for the victim, take out loans in victim’s name, establish
a mule account, get a credit card with a spendable limit and others. KYC and AML laws and
regulations oblige banks and other account servicing institutions to apply a thorough scrutiny,
when opening new customer relationships.

‘Verifying the identity of a new account holder’ and ‘providing a new account holder with an
authenticator for payments’, may seem two independent procedures, but the quality of the first
largely impacts the second. There is a certain point in the onboarding dialogue – whether face-to-
face or online/digital – where the new account holder is identified and sensitive information is
securely exchanged. During onboarding, all information that is relevant for a secure provisioning
of authenticators or for later secure authentication, e.g. with Q&A over the phone, must be
collected in a reliable way. This may include:

•  Home address (verified by authoritative registry),
•  Telephone number, email address,
•  Copy of passport, driver license or other types of id documents
•  Activation code for an authenticator
•  Control questions with a set of answers only account holder should know
•  Biometrics (e.g. Pictures, fingerprints or other)

Exploitation of oversimplified ordering of credentials
Often triggering a surface mailing to a preregistered address is deemed insensitive and can be
initiated without any strong authentication. However, If the client is known not to be at home
during delivery or has a mailbox that is easily accessible to a fraudster, the fraudster may exploit
the oversimplification of the ordering / reordering process to get hold of a spare set of credentials.

Fake enrolment with stolen credentials
Whereas a secure and correctly enrolled mobile authentication/payment app may be hard to
attack, the enrolment procedure itself may be weaker and therefore become a preferred target
for fraudsters. The enrolment may require information that can easily be phished, vished or
guessed, and may depend upon approvals by the victim who is easily persuadable through a scam
or may simply be exposed to manipulation by malware in an  authenticated online banking
session. If so, the fraudster may be able to perform a fake enrolment to a mobile authenticator
that can be misused afterwards to authorise any payment at any point in time.

Deepfake and other AI-enabled scams
Fraudsters are starting to exploit capabilities of evolving AI software tools to create deepfakes, i.e.
video, audio and images of banks’ customers that appear to be real/authentic. Fraudsters may
now impersonate a bank’s customer voice with greater accuracy, by creating custom synthetic
voices that can potentially bypass traditional voice biometric authentication systems used by
banks for authorization and other purposes. Especially when text-to-speech technology could be
used so that a cloned voice is speaking, regardless of the fraudsters background. Similarly,
fraudsters could spoof not well designed ID verification, Face Matching and Liveness systems used
for e-KYC purposes, by utilizing pre-made video deepfakes.

SIM swapping or duplicate SIM attacks
SIM swapping or duplicate SIM ordering are legitimate services offered by mobile network
operators. The reasons for carrying out the swap are to enable the user to move to other mobile

www.epc-cep.eu

48 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

network operator, to disable and replace a SIM card following a lost or stolen mobile device, to
change the SIM card for a new one of a different form factor or to get a duplicate card to
permanently install on another device or in a car.

SIM swap fraud happens when fraudsters transfer a customer’s mobile number to a fraudster’s
SIM. Duplicate SIM fraud happens when fraudsters order a duplicate SIM to a modified address or
collect a duplicated SIM in an ECSP’s shop. Fraudsters leverage such attacks to acquire security
messages with one-time passwords (OTP) sent to the customer by the PSP, for reconfirmation of
sensitive operations such as specific payments (e.g. 3D Secure for online card transactions),
changes to the customer profiles, whitelisting of beneficiaries, provisioning of card tokens to
wallets and then leverage those to perform fraud.

3.2.2.1  Suggested Controls and Mitigation
The general advice is that the security level for the enrolment or ordering of credentials
(authenticators or payment cards, must be as strong as (or preferably stronger than) the
authentication and confirmation of a high-risk payment. This means that the enrolment should
rely on ‘factors’ that cannot be compromised by the same method. In addition, it may be
considered to send notifications and, in case of authenticators, to only allow the authenticator to
give access to information (not payments) for a quarantine period of 1 or 2 days.

Biometrics capture during online on-boarding may also offer an interesting alternative to be used
as a possible authentication ‘factor’ during authenticator app enrolment. Face, voice, fingerprints,
veins in the hand or in the eye are characteristic features that can allow for a strong and otherwise
independent authentication in such a situation. The smart phone, moreover, can supports the app
in capturing these biometrics. But three key questions nevertheless arise:

•  What can these biometrics be compared with for authentication, i.e., does the issuer of an

authenticator app have access to reference data from the on-boarding process?

•  Does the technology perform as needed and expected, i.e., is it user-friendly and are true

users accepted and imposters rejected both with high probability?

•

Is it cost-efficient and can it be smoothly integrated with the ‘identity verification’ process
in place or established to cover for KYC and AML during on-boarding?

As of now there is no clear answer yet to these questions and most of this data will likely become
available only with the spreading of modern selfie or video based online on-boarding processes.
Nevertheless, it is deemed worth early exploring these possibilities as a valuable means against
false enrolment of authenticator apps.

At the same time, continuous reviews of processes and the in-place systems’ capabilities, coupled
with continuous research, should be performed to understand how deepfakes and other AI-
enabled scams could be effectively detected and addressed.

SIM swap and SIM duplication fraud detection identifies suspicious SIM usage patterns. It ranks
the risk based on location, device type and customer behaviour. Different risk levels trigger
different corrective actions, such as blocking transactions, locking accounts, or sending customer
communications. There are a number of controls that end users can implement to try and prevent,
or at least quickly detect, SIM swapping:

•  Enquire with your mobile operator if you have no network connectivity and you are not

receiving any calls or SMS for unusually long periods;

•  Keep personal details that would be useful to a fraudster, i.e. phone number, date of birth

etc. off social media sites;

www.epc-cep.eu

49 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

•  Ask your mobile payment service provider to give you details of every financial transaction

through two channels – for instance, SMS as well as email alerts.

In addition, a mobile payment service provider can negotiate with the ECSPs to be informed about
SIM swaps or duplicate SIM issuing. This can help in monitoring the usage of the account.

During the last years there has been a considerable increase in the use of the mobile device,
whether via SMS, call or mobile application as the authentication mechanism. Technological
solutions to try and secure the mobile device and enable out-of-band authentication via the
device continue to be developed and implemented. If credentials have been phished successfully
and the attacker tries to abuse them to make a fraudulent transaction, there may still be hurdles
to overcome (c.f. Section 3.4).

3.2.3  Payment request and invoicing processes
Although the invoicing (paper-based or e-invoicing) and payment requests are processes that, in
an end-to-end business transaction, are outside of the payment chain, they are particularly
exposed to fraud as they rely on the trust between the Payee and Payer and the security of the
environment in which this information is exchanged. Therefore, they give rise to a specific vector
of fraud for subsequent payment processes.

Often, fraud on invoices or payment request messages leads to Authorised Push Payment (APP)
fraud at the payment stage, as the payers initiate related payments in good faith, by accepting the
terms presented in the invoice or the payment request. Often e-invoices/ payment requests are
trusted when they appear to be sent by government departments (for taxes, fines), the police,
healthcare institutions or from utilities or telecommunication operators. Such claims for payment
can give rise to a fraud category commonly referred to as APP fraud.

Authorised Push Payment (APP) fraud, in which the victims – subject to a scam – actually make the
payments themselves, is showing a steep increase and for PSPs much harder to detect. At the root
of any APP scam is a ‘convincing’ lie with which the fraudster manages to deceive the victim.

UK Finance identifies the following 8 types of APP scams in its reporting30:

•  Purchase scam: the victim pays in advance for goods or services that he never receives.

These scams usually involve the victim using an online platform such as an auction website
or social media.

•

Investment scam: a criminal convinces the victims to move their money to a fictitious fund
or to pay for a fake investment. The criminal will usually promise a high return in order to
entice victims into making the transfer. These scams include investments in items such as
gold, property, carbon credits, cryptocurrencies, land banks and wine.

•  Romance scam: the victim is convinced to make a payment to a person they have met

online through social media or dating websites, and with whom they believe they are in a
relationship.

•  Advance fee scam: a criminal convinces their victim to pay a fee which they claim would
result in the release of a much larger payment or high-value goods. These scams include
claims from the criminals that the victim has won an overseas lottery, that gold or
jewellery is being held at customs or that an inheritance is due. The fraudster tells the
victims that a fee must be paid to release the funds or goods, however, when the payment

30 https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/annual-fraud-report-2024

www.epc-cep.eu

50 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

is made, the promised goods or money never materialise. These scams often begin with an
email or a letter sent by the criminal to the victim.

•

Invoice or mandate scam: the victim attempts to pay an invoice to a legitimate payee, but
the criminal intervenes to convince the victim to redirect the payment to an account they
control. It includes criminals targeting consumers posing as conveyancing solicitors,
builders and other tradespeople, or targeting businesses posing as a supplier, and claiming
that the bank account details have changed. This type of fraud often involves the criminal
either intercepting emails or compromising an email account.

•  CEO fraud: is where the criminal manages to impersonate the CEO of the victim’s

organisation to convince the victim to make an urgent payment to the scammer’s account.
This type of fraud mostly affects businesses.

•

Impersonation of police / PSP staff: in this scam, the criminals contact the victim
purporting to be from either the police or the victim’s PSP and convinces the victim to
make a payment to an account they control.

•  Other impersonations: a criminal claims to represent an organisation such as a utility

company, ECSP or government department. Common scams include claims that the victim
must settle a fictitious fine, pay overdue tax or return an erroneous refund. Sometimes the
criminal requests remote access to the victim’s computer as part of the scam, claiming that
they need to help ‘fix’ a problem.

These scams may be perpetrated using only persuasion, but the fraudster might include other
elements from his toolbox like vishing and abuse of credentials or malware on the victim’s device.

Specific fraud patterns targeting invoicing/e-invoicing processes:

•  As mentioned above, an invoice scam could take form of an illegitimate information to
payers that the account number (IBAN) of a legitimate payee has changed. This can be
called IBAN-fraud or IBAN manipulation whereby a fraudster intercepts and manipulates a
paper invoice or an invoice in digital format (e.g. unstructured PDF invoice, or structured e-
invoice in a standardised format).

•  Regarding paper-based invoices, fraudsters intercept these for example by taking them out
of the mailboxes of the payers and only change the IBAN of the payee. This might also be
the case for attached paper-slips. Because no other information is altered, the invoice still
looks legitimate. Examples are also known where such manipulation took place at the post
office before delivery.

•

•

In case of QR-codes, which contain payment-data are used as part of an invoice, only the
information in the QR-code might be altered by fraudsters, in particular the IBAN of the
payee. The parts of the invoice which are readable by the payer may show unaltered and
therefore correct IBANs related to a specific company.

In another scenario a fraudster produces fake invoices from scratch, using names and logos
of common corporates, such as utilities, insurance companies or big brands. These invoices
are then sent by mail or manually put in the mailboxes of potential victims.

•  A new form of fraud has been detected in late 2020 and 2021 in some countries, involving
different instant payment solutions using the mobile phone of the victim. The fraudsters
send a request for money while convincing the victim that it is a payment that they are
eligible to receive, for example, a refund of Government fees/taxes. Once convinced, the

www.epc-cep.eu

51 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

victim accepts the request to pay thinking that he will receive the money and instead of
that, the money is taken from his bank account31.

•  For e-invoices, the same patterns apply although they are commonly distributed via email
to a much higher number of potential victims, increasing the possibility for triggering
fraudulent payments.

3.2.3.1  Suggested Controls and Mitigation
Scams aimed at APPs resulting from fraudulent invoicing and payment request processes are very
different and require more elaborate warnings. Specific customer segments may be more exposed
to some types of scams than others and the awareness campaigns must be tailored accordingly.
For instance, corporate customers are more exposed to invoice scams and CEO-fraud. In the
private segment elderly/vulnerable customers appear to be targeted. The use of special
awareness campaigns that target certain vulnerable groups may be an APP fraud mitigation
control that PSPs consider. But since it may be difficult to reach the target groups effectively, it is
recommended to also run more general campaigns that include a suggestion to discuss the risks
with friends and family members who may be vulnerable. PSPs may further consider introducing
payment limits or geo-blocking features as is common with card payments. The restrictions could
by default depend on customer profile, but still be configurable for the individual.

As with phishing, the service provider’s ‘central monitoring’ may find a transaction ‘suspicious’,
put it on hold and request customer reconfirmation via a secure out-of-band channel. Whenever a
payment service user is prompted to approve or confirm a payment, the transaction data –
especially amount and payee – must be clearly displayed on the user’s device, supporting the user
in better identifying certain APP scams.

‘Confirmation of Payee’ or ‘IBAN/payee name matching’ is generally considered an effective risk
mitigation measure to counter certain types of APP fraud – especially invoice fraud. When a payer
wants to make a payment, he enters the account number and also the name of the beneficiary.
The payer’s PSP then first requests the beneficiary’s PSP, or a service acting on behalf of that PSP,
to validate the match between this account number and name. If there is no match or only a
partial match, the payer is informed and may decide not to proceed with the payment. Certain
countries like the Netherlands or UK have already established such service.

The European Commission regulation on instant credit transfers in euro (‘instant payments
regulation’32) and the proposed PSR33 also include provisions for such a service. Therefore the EPC
created the Verification of Payee (‘VOP’) Scheme which enables the PSP to request the PSP of the
payee to verify the IBAN and the name or an unambiguous identification code (e.g., Value-Added
Tax (VAT) number, Legal Entity Identifier (LEI), social security code) of the payee as provided by
the payer. This verification needs to happen instantly. The VOP Rulebook is published on the EPC
web site34 and entered into force on 5 October 2025.

Unsecure channels such as SMS or channels such as messaging platforms or simple links received
by email or social media, as they are not formally trusted by a specific framework for payment
requests, should be avoided. Using secure and trusted environments for sending and receiving e-
invoices and payment request can mitigate the risks related to invoicing and payment request

31 https://www.elcorreo.com/tecnologia/internet/consiste-estafa-bizum-20210506135720-nt.html
32 https://eur-lex.europa.eu/eli/reg/2024/886/oj/eng
33 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52023PC0367
34 https://www.europeanpaymentscouncil.eu/what-we-do/other-schemes/verification-payee

www.epc-cep.eu

52 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

processes. For example, the EPC SRTP scheme35 requires that service providers allowed to process
SRTP messages are scheme participants, therefore undergoing eligibility verification, either as
regulated PSPs or entities homologated through the EPC homologation process.

Payees need to undergo proper KYC processes to be able to use the SRTP scheme via Payee RTP
service providers.

3.2.4  Payment Initiation & Authentication
Payment Initiation & authentication attacks refer to those that focus on the end clients’ systems
and thus are distinct from the scam-based attacks described in the previous section that tend to
target the end clients themselves or the channels through which they get invoices or RTPs.

Payment initiation and authentication is primarily exposed to malware attacks although
authentication may be exposed also through sophisticate deception attacks. During the past years
we have seen malware evolving from key logging, capturing of online banking credentials or credit
card numbers, to man-in-the browsers taking advantage of virtual keyboards, RATs, memory
scraping functionality and eventually misuse of accessibility rights under Android. The most
important and persistent banking malware is Emotet which is described in chapter 2.5. Many
other strains of specialised malware have surged targeting banking credentials, targeting credit
card numbers, targeting POS systems with the intention to gather PINs and card data, or targeting
ATMs with the intention to enable jackpotting attacks.

Such malware may either directly manipulate transactions or steal credentials entered by the
customers towards misusing them at a later stage. It is common to see such attacks combined
with social engineering to either give the customer the impression that a specific payment has
been initiated as intended or a payment has been erroneously received and should be reimbursed,
or that access to online banking is not available for a certain time.

Deception attacks usually take a different approach, by leveraging technical functionality often
introduced to enhance user experience. For example, QR-code based mobile authentication
solutions may allow the QR-code to be scanned not only with the bank’s authentication app but
also with the device camera, or mobile authentication apps may allow face identification to
require no user acceptance screen prior to doing an identification. Such often harmless-looking
enhancements can be the basis for very effective deception attacks where a client inadvertently
logs in a fraudster by clicking a hyperlink or scanning a QR-code in an email or chat.

3.2.4.1  Suggested Controls and Mitigation
Beside the controls or mitigations listed against the social engineering and malware threats in
section 2, it is also essential that mobile applications come with an inherently secure modus
operandi protecting the end-user from being fooled by fraudster taking advantage of features
introduced for maximum ease of use.

3.2.5  Payment Execution
Payment execution attacks refer to those attacks that focus on central processing systems where
the actual validation of the transaction and the transfer of funds itself are executed. These attacks
can occur at a bank or at an account information or payments initiation service provider, at a card
processor, card issuer or acquirer network, as well as on a clearing infrastructure; attacks on
SWIFT or other clearing interfaces fall under this latter scope. Such attacks may come with severe

35  The SEPA Request-to-Pay scheme rulebook version v4.0

www.epc-cep.eu

53 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

financial consequences, given that the impact from data losses, service disruptions or
compromised transactions may be in the range of thousands up to billions of Euros.

Beside the DDoS attacks covered at large in the previous section, the greatest risk here comes
from advanced persistent threat attacks (APTs). As explained in Section 3.1.3, they usually
leverage themselves all possible techniques ranging from social engineering and DDoS up to
specially crafted malware. There have been a wide diversity of APT attacks against financial
institutions in the last years. Ultimately, they can target any entity, compromise whatever data,
and misuse whatever service.

In the financial sector we have seen major data breaches primarily compromising bank card data.
Targeted APT attacks have been conducted – most prominently – against SWIFT service bureau
and gateway infrastructures but also against acquiring and card issuer authorisation systems.

In the following we give a brief overview of each one of these types of APT attacks.

Card data breach APTs
One of the first attacks involving the breach of cardholder data took place in 2004 where 40
million cards were compromised at the former company called CardSystems. Since then, many
data breaches compromising many millions of cards have occurred and continue to occur. All
these data breaches present various modus operandi following the structured approach
mentioned in section 3.1.3.

The initial foothold is usually executed through social engineering bank employees towards
obtaining credentials, or by convincing the employee to open an attachment that will exploit a
zero day vulnerability or by exploiting a vulnerability of an external facing system.

Card data breaches vary in respect to the types of systems attacked and the types of data that
they may harvest.

Compromise of databases holding card data continues to be common despite the enforced PCI
DSS programs. These compromises have the characteristic of usually stealing data stored over
various years and generally are limited to card numbers and expiry dates. It is not uncommon
though, to also compromise CVVs as well.

Other data breaches intercept transaction data when being processed or whilst in transit in the
communications realm. These attacks tend to compromise a shorter span of data given that they
do not have access to historical transactions, compared to database compromises. On the other
hand they usually compromise data of higher value such as CVV2 and chip or magnetic track data.

Some special variants of APT attacks consist of infecting terminals, POS or ATM with malware.
These APT attacks go through the process of compromising internal systems and making lateral
movements until they grasp a system with the capability of downloading software to the POS or
ATM. In one case the malware on the infected POS was performing memory scraping getting the
card track data and exfiltrating it back over the compromised internal systems. The reusable data
is then typically sold in dark web forums and misused all over the world.

The adoption of EMV standards² based on chip cards has created a secure alternative to magnetic
stripes, countering such attacks. However, the benefits of this new chip technology will only
become fully effective with the complete ban of the magnetic stripe technology, at the basis also
of magnetic stripe skimming and shimming attacks. These past few years have seen the largest
missing countries adopting EMV, notably the US, so that cloned magnetic stripe cards can now
solely be misused in the few remaining countries that have not yet embraced EMV.

SWIFT APTs

www.epc-cep.eu

54 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

The SWIFT infrastructure has been designed with security considerations right from the very
beginning and as an example of this commitment, protection of payment transactions is based on
cryptography making use of hardware security modules. Even so, compromises have occurred
where the operators and the SWIFT gateway systems that interface with operators and service
users were exploited. This resulted in the injection of fraudulent transactions and specially crafted
software that, in some instances, would even hide the fraudulent transactions from the operators.

SWIFT gathered intelligence with regard to these attacks and shared it with their customers under
NDAs, so that customers can prepare specific mitigations against these kinds of attacks. Moreover,
the SWIFT Customer Security Program has set forward a set of security requirements that SWIFT
clients must adopt and get certified against. Very little information is publicly available about all
this except for the numerous attacks reported in the press and a substantial revealing report
published by F-Secure36.

Through the analysis of the various reported cases, it can be concluded that there are diverse
modi operandi, however infecting bank or service bureaus’ internal systems with malware is
common to most attacks and the compromise of employee credentials is frequently one of the
mechanisms used in these attacks. Most of these attacks have in common the fact that the time
taken for attackers to prepare the final heist can be unexpectedly long, sometimes taking more
than a year in preparation. On the other hand, the attackers manage to reap amounts ranging up
to nearly a hundred million Euros.

Card Processing APTs
Some major attacks have occurred relating to the manipulation of card transaction processing
parameters. Usually those attacks change the fraud control parameters, such as spending limits, of
a few cards and then in a synchronized and distributed attack withdraw as much cash as possible
in a timeframe of only a few hours.

As early as 2008, a major processor’s systems were compromised and the attackers managed to
replenish the available funds and raise the spending limits of 44 prepaid payroll cards. Three days
later 9 million USD were withdrawn in 280 cities in a time window of 12 hours. Since this attack a
few high profile attacks of the same kind have occurred: misusing a few cards to withdraw within
only a few hours37 38 39 many millions of Euro, on terminals spread all over the world.

Some of such attacks were the result of an APT laterally moving through internal issuer systems
until the card processing system was reached.

3.2.5.1  Suggested Controls and Mitigation
No dedicated controls or mitigations beside the ones listed against the social engineering and APT
threats in section 3.1.3.2.

36 ‘Threat Analysis - SWIFT Systems and the SWIFT Customer Security Program’ - https://www.f-
secure.com/content/dam/f-secure/en/business/common/collaterals/f-secure-threat-analysis-swift.pdf
37 ‘Eight Members Of New York Cell Of Cybercrime Organization Indicted In $45 Million Cybercrime Campaign’ -
https://www.justice.gov/usao-edny/pr/eight-members-new-york-cell-cybercrime-organization-indicted-45-million-
cybercrime
38 ‘Coordinated ATM Heist Nets Thieves $13M — Krebs on Security’ -
https://krebsonsecurity.com/2011/08/coordinated-atm-heist-nets-thieves-13m/
39 ‘Indian Bank Hit in $13.5M Cyberheist After FBI ATM Cashout Warning’ -
https://krebsonsecurity.com/2018/08/indian-bank-hit-in-13-5m-cyberheist-after-fbi-atm-cashout-warning/

www.epc-cep.eu

55 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

3.2.6  Mobile Wallets for Identification and Authentication
A mobile wallet is a service accessed through a mobile device, which allows the wallet holder to
securely access, manage and use a variety of services/applications including payments and non-
payment applications. This service may reside on a mobile device owned by the consumer (i.e. the
holder of the wallet) or may be remotely hosted on a secured server (or a combination thereof).
Typically, the so-called mobile wallet issuer provides the wallet functionalities, but the usage of
the mobile wallet is expected under sole control of the consumer and his mobile device.

Specific threats in the mobile wallet space include targeted attacks on mobile device key stores,
unlock credentials, user interfaces and communication controllers. All of these may get exposed
through malware leveraging accessibility, privilege escalation or rooting / jail-breaking exploits.
Although mobile devices come with inherent security like secure boot and app signing and
sandboxing, drive-by privilege escalations attacks keep on being reported across all operating
systems. Moreover accessibility rights have shown a powerful feature under Android that users
can easily be tricked into granting without understanding that they give up by this full control over
their device and all apps on this device.

For a high-level overview of digital wallet application threats, the ENISA report from 2016 on the
‘Security of Mobile Payments and Digital Wallets40 lists the following still valid threat categories:

•  Phishing and social engineering
•

Installation of rogue applications and malware
•  Unauthorized access to lost or stolen mobile device
•  Malware installation on the device
•  Reverse engineering of the application source code
•  Tampering with the mobile payment application
•  Exploit of mobile payment application vulnerabilities
•
•  Mobile Operating System Access Permissions

Installation of rootkits/malware

The EUDI Wallet
A prominent example of such a wallet is the EUDI Wallet that is planned to be deployed to all EU
citizens under the 2024 update 2.0 of the eIDAS41 regulation. This Wallet is envisioned to serve
among others also a multitude of banking use cases including account opening through selective
identity-attribute disclosures, contract signing through qualified electronic signatures, electronic
payments authentication through attestations42 and eventually also online banking authentication
(not yet specified).

Part of its security is directly mandated by the regulation, while other parts are specified by its
Architecture and Reference Framework and by a set of associated Implementation Acts. Those
cover among others for an appropriate hardware-protection (access and storage) of credentials,
but leave open for wallet providers to foresee appropriate protections against mobile device
threats that may expose the device and/or its user interfaces to remote control by fraudsters. Due

40 https://www.enisa.europa.eu/publications/mobile-payments-security
41 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32024R1183
42 https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-
framework/blob/main/docs/annexes/annex-2/annex-2-high-level-requirements.md#a2320-topic-20---strong-user-
authentication-for-electronic-payments

www.epc-cep.eu

56 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

to the fact that not all devices come with the same level of device protections against these
threats, it appears that this cannot be addressed solely with a certification of the wallet software,
and its key store.  To compensate for the fact that, under the actually envisioned operational
model of the wallet, relying parties may no longer be able to get real-time security information
from the device used for Wallet-based authentication, an additional certification of the underlying
device and its user interfaces may become a further necessity  (c.f. ARF discussion43 about lack of
advanced analytics and fraud signals from the EUDIW, as leveraged today by payment service
providers to satisfy explicit PSD2 RTS requirements).

3.2.6.1  Suggested Controls and Mitigation
Segregation mechanisms like Trusted Execution Environments (TEE) but also privilege escalation
detection and remediation mechanisms like root-kid detection or secure device boot today
represent inherent mobile platform security features that together with regular OS updating lay a
strong security foundation for mobile wallet implementations.

For identification and authentication some extra protections against the afore listed threats are
essential to establish user sole control and avoid liability discussions. To this extent, the usage of
hardware protected key stores is a necessity. However, as mentioned in Section 3.1.2, effectively
countering these threats, additionally requires trusted user interfaces to the hardware key stores,
at least for highly-sensitive identification and authentication use cases as usual in banking. A
possible framework  that supports dealing with this under the security heterogeneity of the
mobile devices hosting such wallets is part of the Fast IDentity Online (FIDO) standards. FIDO
indeed comes with an authenticator certification and a Metadata Service44 that can support
covering not only for a certification of the authenticator keystore but also for a certification of its
access means and its user interfaces via Metadata Keys in the Metadata Statement45  associated
with a specific authenticator.

43 https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/discussions/582
44 https://fidoalliance.org/specs/mds/fido-metadata-service-v3.1-ps-20250521.html
45 https://fidoalliance.org/specs/mds/fido-metadata-statement-v3.1-ps-20250521.html

www.epc-cep.eu

57 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

3.3  Fraud unique to Specific Payment Instruments
The various threats and fraud patterns described in the previous section can basically lead to two
categories of fraud, namely so called ‘Authorised payment fraud’ and ‘Unauthorised payment
fraud’. Authorised payment fraud refers to authorised transactions in which the genuine payer
initiates and approves a payment to an account under the control of a criminal. Unauthorised
payment fraud refers to an unauthorised fraudulent transaction whereby the genuine payer does
not provide authorisation for the payment to proceed and the transaction is carried out by a
criminal.

The sections below describe fraud related to specific payment instruments.

3.3.1  SEPA Schemes
The various threats and fraud enablers described in Section 3.1 and 3.2 of this document could
lead to fraud on SEPA payment schemes (SCT, SCT Inst, SDD – Core and B2B) as well as on
payment-related schemes such as SEPA Request-to-Pay and VOP. As set out in the previous
section, regardless the payment instrument, the fraud can occur at all payment-relevant processes
of a transaction.

Nevertheless, payment-related schemes aim at mitigating risks in payment-relevant processes,
along with addressing other customer needs.

These fraud scenarios are detailed in the next sections.

3.3.1.1  SEPA Credit Transfer (SCT)
SCT is a SEPA wide Credit Transfer scheme managed by the European Payments Council and its
governing rules and standards are described in the SCT Rulebook.46

The following processes of SCT transactions can be targeted by various threats and fraud enablers:

On-boarding and provision

•  A fraudster using various techniques, notably social engineering, for obtaining for example
a SIM-swap of a legitimate user mobile subscription, can open a profile and record a victim
bank account. Once the provisioning is completed, the fraudster may initiate SCT
transactions.

•  A fraudulent, one-time access to an account holder profile in an e-banking or mobile

banking application, can be used to create fake beneficiaries. Recording these beneficiaries
under genuine and known names, can trick the account holder when initiating SCT
transactions. Also once a fake beneficiary is created, automatic and periodic SCTs can be
configured so that at every term an amount of money is automatically transferred to the
fraudster without further intervention by the victim. These fraudulent credit transfer
transactions can be executed until the attack is discovered and can lead to important
losses for the victim, often hard to recover as funds can have been used for cash
withdrawal, purchase of goods or money-muling.

•  Full fraudulent bank account creation (after identity theft or weak KYC procedures) for

further use as Beneficiary account in fraud scenarios based on ‘money mules’.

46 SEPA Credit Transfer (SCT) Rulebook 2025 v1.1

www.epc-cep.eu

58 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Request-to-Pay and Invoicing

•  These processes are not directly part of the SCT scheme. The payment using SCT scheme

represents the ‘payment’ part of a larger end-to-end purchase flow and is preceded by the
invoicing or the RTP step. However, the RTP and electronic invoicing combined with
payment are beneficial for payers as they facilitate smooth payment initiation without the
need for entering transaction and beneficiary details. This advantage can be exploited by
fraudsters to further automate the fraudulent actions leading to illegitimate fund transfers
using the SCT scheme. Therefore Invoicing and RTP processes are relevant for the SCT
scheme.

•  The two main fraudulent actions with effect on invoicing and payment request processes

have been described in the corresponding section 3.2.3. These are particularly relevant for
the SCT scheme as the payment instrument most often associated with payment requests
is Credit Transfer and this is for a large extent also true for invoicing.

Payment initiation and authentication

•  During the last years, the criminals’ use of impersonation and deception scams, as well as
online attacks to compromise data, continued to be the primary factor behind fraud losses
related to SCT payments. In these methods, criminals target personal and financial details
which are used to facilitate fraud or convince the genuine account holder to authorise a
transaction to an account controlled by the criminal (Authorised Push Payment – APP).
•  Various types of social engineering – detailed in section 3.1.1 – can be used to initiate
payments, even if Strong Customer Authentication is active and mandated. Once the
victim’s trust is obtained, the fraudsters can make updates of the e-banking profile of the
customer (mentioned in the Onboarding section above) or simply initiate credit transfers.
The analysis in the 2024 Fraud Report from UK Finance47, indicates criminals increasingly
contact customers by phone, text message or email pretending to represent a trusted
organisation such as a PSP or the police, seeking to trick people into handing over personal
details and passwords or trick people into APPs. APP fraud is the fastest growing fraud in
the UK and the related loss is even larger than fraud losses related to ‘unauthorised
payment fraud’.

•

‘Unauthorised payment fraud’ is often the result of attacks using malwares. Malware gets
installed on the customers’ devices (individual or corporate customers), or on the devices
of bank agents in the banks’ branches, to either intercept authentication credentials for
further or immediate use on separate channels controller by fraudsters, or to directly
initiate fraudulent credit transfers. According to ENISA Threat Landscape 202448, malware
attacks increased again, particularly since mid-2023, after a decrease in 2020 and
beginning of 2021.

Payment execution

•  At the execution stage, once the customer is authenticated and a payment instruction has

been initiated, sophisticated intrusions could target the PSPs infrastructures or
infrastructures of the CSMs.

•  An important technique that could be used now and for the future seems to be APT. It

must be considered as a potential high risk not only for the payment infrastructure but for

47 https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/annual-fraud-report-2024
48 https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024

www.epc-cep.eu

59 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

all network related ecosystems. With a limited number of criminals involved, a maximum
result can be established (see Section 3.1.3).

•  DDoS attacks, that can also rely on botnets can target PSPs or CSMs infrastructures can
make serious damages and even if these do not have for object a fraudulent transfer of
funds from customer accounts, they may create unavailability and affect the stability and
the reputation of the payment operation infrastructures.

•

In some cases, this type of attacks masks more classical attacks and is used to divert the
attention and resource allocations of operational teams from actions of identifying and
neutralising them.

3.3.1.2  SCT Inst
SCT Inst is an ‘instant Credit Transfer’ scheme managed by the European Payments Council and its
governing rules and standards are described in the SCT Inst Rulebook49.

The SCT Inst scheme can be impacted by the same threats and fraud enablers, and at the same
stages of processing, as the classical SCT scheme. However, SCT Inst has specific features that
distinguish it from the SCT scheme and that can be exploited leading to specific fraud:

•  An SCT Inst transaction is much faster than an SCT transaction. The originator account is
immediately debited and the funds are instantly made available on the account of the
beneficiary. It is executed in seconds and therefore the following consequences can be
expected:

o  Whilst at the initiation and authentication stage, the fraud techniques based on social
engineering and malwares are performed in the same way as for SCT, initiation is
immediately followed by the execution and the use of funds fraudulently received is
immediately possible for cash withdrawal or physical purchases.

o  The overall speed of transactions to/from ‘money mules’ is much higher so that this type
of enabler/monetisation channel is expected to be more intensively used with SCT Inst.

o  At the execution stage, the mechanism for fraud detection and transactions blocking

must be executed in real-time.

•  SCT Inst transactions must be processed continuously, on a 24/7 basis so that it is not
possible to use the time before batch processing to perform anti-fraud screenings.

•  The clearing and settlement is executed in almost the same time as the payment orders so
that disruptions caused by APTs and DDoS might also affect these layers of transactions.

In this context, the European Commission proposals for a regulation on instant credit transfers in
euro (‘instant payments regulation’50) and the PSR51 include provisions for an IBAN/payee name
matching service for fraud risk mitigation. Therefore the EPC created the Verification of Payee
(‘VOP’) Scheme; this is detailed in section 3.2.3.

49 SEPA Instant Credit Transfer (SCT Inst) Rulebook 2025 v1.1
50 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52022PC0546
51 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52023PC0367

www.epc-cep.eu

60 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

3.3.1.3  SDD (Core and B2B)
SDD Core and SDD B2B are SEPA wide Direct Debit schemes managed by the European Payments
Council and their governing rules and standards are described in the SDD Core and SDD B2B
Rulebooks52.

The following processes of SDD schemes can be targeted by various threats and fraud enablers:

On-boarding and provision
As in both SDD schemes the payment transactions are ‘pull’ mode transactions (debtor account is
debited on the basis of a debit/collection request coming from the creditor – provided that a
proper mandate is signed by the debtor to allow the creditor to initiate such transaction), the on-
boarding stage concerns the creditor. Moreover, on-boarding a creditor in an SDD scheme require
a strong KYC process on the creditor PSP side. Although it might be possible that a fraudulent
entity requests from a PSP to become a creditor in an SDD scheme, there were no notable fraud
attempts of such type in the last years. This would require that representatives of the fraudulent
company be able to trick the controls that banks perform when registering companies for the role
of SDD Creditors. For this type of fraud to happen, one would have to make use of complex social
engineering targeting the corporate customer services of PSPs.

If the signature of the SDD mandate by a debtor is considered as part of the on-boarding process,
another type of fraud is that the debtor indicates on the SDD mandate an IBAN of an account that
does not belong to that debtor. A fraudulent debtor could benefit this way from goods and
services paid by SDD, whilst the payments for these services and goods are executed from
someone else’s bank account. The scheme’s rules however allow the victim to require the refund
of amounts so that the effects of this type of fraud on the debtors can be easily mitigated.

Some merchants (e.g., selling digital goods, subscriptions to digital services, parking, subscriptions
to newspapers and magazines etc.,) do not require a wet signature or the equivalent of the
mandate and instead propose customers to sign a mandate by answering to an SMS, checking an
option on a web portal, or sending an email containing an account number. Even though,
depending on the jurisdiction, these forms of expressing an agreement are legally valid, the
possibility of abusive use by some merchants could lead to fraud through social engineering.

Payment request and Invoicing
When starting a long-term, recurrent, commercial relationship merchants and service providers
may propose customers to pay their invoices by Direct Debit. Often the mandate proposal is
attached to the first invoice regardless if it is in paper or electronic format.

Wrong or unclear formulations in the mandate, identity theft, misleading presentation of the
mandate scope could all be leveraged as social engineering towards convincing customers to sign
valid SDD mandates for fraudulent purposes.

Initiation and authentication
In SDD schemes, the payment is initiated by the creditor. It is of the responsibility of the creditor
PSP to ensure proper authentication of the creditor for the execution of direct debit collections.
Nevertheless, it is neither in the SDD scheme rules, nor can it be in the authentication processes
that the SDD mandate is verified. Therefore, there is a risk that a fraudulent creditor tries to
execute SDD payments by debiting victims’ bank accounts without a mandate.

52 SEPA SDD Core Rulebook 2025 v1.1, SEPA SDD B2B Rulebook 2025 v1.1

www.epc-cep.eu

61 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

According to the 2022 yearly report from the Banque de France’s Observatory of the payment
instruments’ security, this was the main fraud technique used in 2022 in France for SDD fraud53.

Another type of SDD fraud is based on the complicity between a fraudulent creditor and a debtor.
With a proper mandate the creditor regularly debits the debtor’s account increasing the amounts.
A short time before the end of the 13-month period for legal refund, the debtor contests the
payments and asks the refund to their bank. At that moment, the creditor had transferred the
funds to another account or transformed them in cash so that the creditor bank cannot recover
these funds but is obliged to refund the debtor bank which had refunded the debtor.

It has to be noted that the SDD B2B scheme is less likely to be targeted by fraud than SDD Core, as
in SDD B2B the debtor is always a company and it is required that the debtor PSP verifies each
collection to ensure that it is authorised under the mandate.

3.3.1.4  Supporting schemes
SEPA supporting schemes can be defined as schemes covering the exchange of the data necessary
to initiate payments and facilitating interoperability.

Currently the EPC manages the ‘SEPA Request-to-Pay’ (SRTP) messaging scheme. The version 3.1
of the SRTP Rulebook was published in December 202354.

The EPC also introduced the ‘Verification of Payee’ scheme, detailed in section 3.2.3. This scheme
was specifically introduced to mitigate fraud risks, specifically invoice fraud and other fraud
vectors in the Payment request context. The Rulebook is published on the EPC website, and the
Scheme will enter into force on 5 October 2025.

Potentially when targeting supporting schemes, all relevant payment related processes that were
detailed in Section 3.2 can be affected by some threats and fraud enablers set out in Section 3.1.
Nevertheless, as the supporting schemes are relatively new, it is too early to observe specific real-
life fraud actions targeting them.

Specifically to SRTP, even if it unlikely if proper KYC processes are in place, fraudsters that have
been onboarded as Payee to an RTP service provider might distribute very large amounts of
illegitimate RTP messages, counting on the fact a significant number of payers will not thoroughly
check the underlying business (payee) and will simply authorise their PSP to initiate the payment
transaction according to the respective request. The effectiveness of this fraud vector is further
enhanced by RTPs presented within the payer’s online banking to make the payment transaction
authorisation process simpler and faster.

3.3.1.5  Suggested controls and mitigations
Fraud prevention for SEPA schemes requires measures that involve all actors in the payment chain
and are applicable to all payment processes. As part of its Scheme Management role, the EPC
provides for each scheme, a Risk Management Annex (RMA), complementing the schemes
Rulebooks. These RMAs are made available to scheme participants (PSPs) and include the
identification and evaluation of risks and measures for their mitigation aiming to ensure an
adequate degree of security, operational reliability and business continuity for the concerned
scheme participants and their customers.

53 https://www.banque-france.fr/fr/publications-et-statistiques/publications/rapport-de-lobservatoire-de-la-securite-
des-moyens-de-paiement-2022
54 SEPA Request-To-Pay (SRTP) Scheme Rulebook v3.1

www.epc-cep.eu

62 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Regardless the scheme, some measures and best practices are:

•  Establishing secure communication channels that guarantee data integrity and

confidentiality, and mutual authentication between PSPs and Clearing and Settlement
Mechanisms (CSMs)

•  Use of appropriate measures against DDoS attacks on PSPs’ and CSMs’ platforms
•

Implementation of adequate fraud monitoring systems; regarding the SCT Inst scheme,
these systems should be able to perform real-time analysis and related actions, due to the
instant characteristics of this scheme

•  Secure connection from/to the originator and beneficiary devices (PCs, mobile phones) and

the corresponding PSPs

•  Use of Strong Customer Authentication (applicable to SCT and SCT Inst) with dynamic

linking with Beneficiary identifier and transaction amount

•  Promotion of security and data protection awareness, training and education wherever
possible including warnings for phishing attacks, and encouragements to adopt security
measures on the customer devices.

•  Regarding SDD schemes (Core and B2B), the creditors should ensure the protection and

authenticity of the mandate given by Debtors.

Other measures fall under the scope of supporting schemes such as SRTP. For example, among
measures specific to the SRTP scheme, the following could be mentioned:

•  RTP Service Providers have an active role to play in the fraud prevention. If they are no

regulated entity (non-PSPs), they should complete a proper homologation process as part
of the scheme onboarding stage. Indeed, PSPs should have certainty that the processed
Requests-to-Pay are valid and originate from a legitimate scheme participant.

•  Payees need to be legitimate and accepted as customer of SRTP Scheme participants (RTP
service providers) upon completion of agreed customer authentication and identification
procedures, including a mandatory IBAN check done at the enrolment (payees are only
allowed to use the IBANs that have been duly registered and checked). Indeed, SRTP
scheme participants (and ultimately payers) should have certainty that received Request-
To-Pay (RTP) messages = are valid (i.e. created by a legitimate payee, contain valid
payment-related data like amount/payee IBAN and represent a real business transaction).
•  As concerning technical implementation of SRTP APIs, security principles stated in the API

Security Framework (ASF) document55 must be followed.

3.3.2  Card Scheme
Card based transactions have historically been very successful due to the acute balance between
security and convenience in authenticating these transactions through the card magnetic track
(something you have) and the PIN (something you know).

In the late nineties fraud trends started to explore the fact that the magnetic stripe became quite
easy to clone and thus led to the adoption of the EMV chip card to substitute the magnetic stripe.

55 https://www.europeanpaymentscouncil.eu/document-library/guidance-documents/api-security-framework

www.epc-cep.eu

63 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Meanwhile with the emergence of the internet, card-based payments started to be accepted,
opening up to new avenues of fraud. Several mechanisms were adopted along the years to secure
these transactions namely the adoption of the CVV2 and the adoption of 3-D Secure protocol.

In the 2010’s contactless cards started to surge building on the fact that chip cards were capable
of computational processing and so could support yet the processing through this new interface.

In recent years mobile devices have the capability of implementing contactless transactions by
emulating the contactless card through NFC (Near Filed Communication) technology.

As a result of the application of PSD2 RTS on SCA ([2]), all European payments benefitted of higher
levels of security. Magnetic stripes on bank cards were, for acceptance purposes, still accepted as
a fallback until the compulsion of SCA in September 2019. Meanwhile internet card payments
force SCA through the 3-D Secure protocol that has evolved to a second version that enables
frictionless and better authentication across devices. It also supports more information to
determine the risk of the transaction.

In general, the fraudster’s modus operandi is to obtain the physical payment card (or card data)
and PIN for use in a face to face, Point of Sale (POS) or ATM environment. Alternatively, he obtains
payment card data for use in an e-commerce or card not present (CNP) environment, such as
Internet shopping, mail order, phone ordering, etc. if the card supports this functionality. Lately,
omni-channel fraud e.g. using stolen card information from social engineering in wearables and
mobile devices in a POS environment has been increasing, as well as fraud cases where both SEPA-
schemes and card payments are being interlinked and used as combined vehicles to move stolen
funds and handle the exfiltration of crime gains.

The adherence to PSD2 has changed the attack context and a trend to the adoption of social
engineering attacks has been observed, as a way to circumvent the adoption of SCA. Below are the
most common, as well as new, fraud trends within the card present and card not present space.

3.3.2.1  Card present
Card present fraud is a wide-ranging term relating to the theft and crimes committed using or
involving a payment card, or other tokens with card details in physical POS terminals or ATMs. The
purpose may be to obtain goods or services to resell for cash or to obtain funds directly from a
related payment account.

Lost and stolen card fraud
Fraudsters consistently look at better and easier ways to capture PINs, e.g. using social
engineering or shoulder surfing, and then stealing the payment card using one of various methods,
often targeting the elderly or the uninformed. In this way, getting the card and the PIN to execute
real payment transactions is often hard to detect.

Contactless payment cards are being increasingly accepted in stores. A lost or stolen card can be
used for purchases as long as the cardholder authentication (PIN, CDCVM) is not required for a
contactless transaction at POS terminals, but only up to a certain number of transactions and/or to
a limited value. It is expected that there will be an increase in the theft of cards for this purpose,
i.e. to purchase goods that can be easily resold for cash. ATM cash transactions always require a
cardholder authentication thus are not subject to this attack scenario.

Another fraud type to consider is card-not-received fraud, that takes place when a criminal steals
a payment card from an individual’s mailbox or in the mail delivery process, so the rightful owner
never receives it. This type of fraud is only effective when the card is delivered in an active state. It
should be noted that most card issuers issue inactive cards, that can only be activated by the

www.epc-cep.eu

64 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

genuine cardholder. By doing so, cards intercepted in the delivery process will be of little or no use
to the attacker for card present transactions.

Contactless cards intercepted in the delivery process will not transact until a contact online
transaction is performed and so mitigate the risk of an attacker performing contactless
transactions that do not require cardholder authentication.

Account take over / Fraudulent cardholder application.
Fraudsters are using social engineering techniques such as doing visits to cardholders’ homes,
approaching PSP staff or other methods, such as spear phishing, to obtain the data needed to take
over an account or create a false cardholder application / request for a payment card or PIN.

Counterfeit and skimming
Copying magnetic-stripe track data at POS terminals and ATMs by skimming is an ever-diminishing
type of fraud in Europe.

With the compliance of PSD2, magnetic stripe-based transaction of European cards on European
terminals, were forbidden. However, the so-called one-legged transactions, where either the card
or the terminal are non-European, magnetic stripe-based transactions may be accepted.

Protecting terminals from skimmers has proven to be challenging at most. Skimmers have evolved
from classic external skimmers to non-metallic skimmers, stereo analogue skimmers, and lately to
inlay and insert skimmers. PIN capture has been enabled through PIN pad overlays or through
ever-smaller spy cameras.

Magnetic stripe cards cloned with the stolen card data may be used on terminals where EMV chip
technology is not supported or required. While such cloned magnetic-stripe payment card cannot
be used in the European area, this is still possible in countries where EMV has not yet been fully
introduced, hence fraudulent usage, namely cash-out, is often performed outside of Europe.

Shimming, like skimming, is where the aim of the fraudster is to skim or ‘shim’ data from the EMV
Chip on a payment card rather than from the magnetic stripe, using similar methods. Criminals can
exploit this when issuers have implemented the EMV protocol incorrectly. Some attacks making
use of skimmed and shimmed data, have been observed coming from out of Europe doctoring all
types of data in the messages trying to explore failures in the issuers processing implementation.

ATM fraud
ATMs are also vulnerable to several other attack vectors, not limited to, but including physical
attacks, malware/logical manipulation, black box attacks, jackpotting, card and cash trapping, etc.
Black box attacks observed a rise in European ATMs since 2020. Malware designed specifically
developed for ATMs continue to occur throughout the world.

ATM MitM relay attacks have been observed recently in several European countries. These attacks
intercept communications between the EMV chipcard and the ATM through a shimmer and relay
information to another ATM (rogue ATM), controlled by the attacker, using  communications
equipment. The victim will be unaware to the setup. The PIN will have to be captured as well and
transmitted, typically by streaming video to the attacker that will type it in at the rogue ATM.
Meanwhile the ATM where the victim is operating will have to be fooled into taking the
transaction forward, including requesting the PIN introduction, but should be led to abort the
transaction so as to avoid the ATM transmitting the transaction to the processor.

For more insights on ATM-related fraud and attacks, please revert to the bi-annual report
produced by EAST (European Association of Secure Transactions).

www.epc-cep.eu

65 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

First party fraud (overdrafting credit limits)
Non-credit worthy people try to get payment cards and bank accounts with the only purpose to
overdraw the accounts/credit limits, without any intention to pay back, to get cash and/or to
purchase goods/services. First party fraud is usually caused by a weak KYC procedure and too
flexible card products provided to the customer with generous credit limits.

Friendly/Family fraud
Friendly fraud occurs where a victim’s relative or acquaintance performs transactions without the
knowledge of the victim. This kind of fraud usually involves non-significant amounts but usually is
complex to investigate and requires significant effort.

Merchant refund fraud
This fraud occurs when the fraudster, through different methods, hijacks an in-store card terminal
and uses it to make refund purchases with stolen cards. To make sure the merchant has sufficient
funds on their account, the fraudster often first makes purchases using stolen cards. They then
cash out in ATMs immediately afterwards. The fraudster has knowledge about terminal
functionality and can in some cases also have inside help at the targeted merchant. This type of
modus operandi, according to multiple sources e.g. Mastercard, increased during the Covid-19
pandemic, given that the genuine flow of refunds increased due to cancelled services and events.

Shell companies and fake merchants
It has been noted that criminals set up fake, or bought existing non-active corporations, and used
these to sign card acquiring agreements in order to accept card payments that will be later used to
exfiltrate funds. These modi operandi are often complex and are performed in several steps, from
setting up the corporation, acquiring info on the target, creating a good cover story for the social
engineering to exit with the illicit gains.

3.3.2.2  Card not present (CNP)
Card not present fraud is a term relating to the theft and crimes committed using or involving
payment card credentials for making authorized or unauthorized purchases in the e-commerce
space, MOTO or other instances where the physical card is not involved in the process. The
purpose may be to test the validity of the credentials, to obtain goods or services to resell for cash
or to obtain funds directly from a related payment account.

Unauthorized card not present fraud
As the volume of payment card purchases made via the Internet continues to grow, so too do the
attempts of Card Not Present (CNP) fraud. E-commerce is the preferred way to buy goods or
services where the payment card is not physically present, and stores must rely on the cardholder
information indirectly. Fraudsters obtain payment card details in various ways: by malware, data
hacks, phishing or fake merchants stealing the information. This information is later sold on
criminal marketplaces on Darknet/Deep Web to be used by other fraudsters, or sometimes used
by the bad actors stealing the credentials themselves. The modus operandi for committing the
CNP-fraud is normally either through large volume automated algorithmic attacks on well-known
e-commerce websites, trying to hide the fraudulent transactions in the vast volume of legitimate
transactions, or by using the credentials more diligently for single high-amount purchases on
selected merchants or merchant categories.

A common modus operandi of cybercriminals is to try to extrapolate card numbers, expiry dates
and sometimes also CVV. They then use those generated numbers for large scale BIN-range

www.epc-cep.eu

66 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

attacks involving low amounts and when they get a positive hit, they may use that card on a high
amount transaction to purchase easily transactional goods.

Below are the most common ways for criminals to access card details.

Account Data Compromises

ADC attacks are targeted at specific stores, financial institutions, services providers or other sites
holding valuable card or customer information in their databases, with the aim to compromise the
network or payment system and gain payment card data.

Everyday tens of vulnerabilities are published, usually relating to widely adopted software. Some
vulnerabilities are called zero-day vulnerabilities given that at the time of disclosure no patch
exists for its resolution. It is typical for small merchants not to have the necessary awareness or
resources to prevent and maintain secure environments for the processing of card data given that
security is not their main focus.

In connection with the above, hotels, online tour operators are currently, and historically,
responsible for a large part of the stolen card data. Card data is stolen in transit or in data storage,
and it results in various sorts of unauthorized CNP-fraud.

Although these attacks can occur on any payment systems there have been attacks against
payment card issuers resulting in serious fraud losses. Payment cards with an almost infinite limit
are issued by the fraudsters and intercepted, duplicated and distributed within their global fraud
network. Attacks are organised and occur mainly during periods when fraud monitoring is at a low
level, e.g. at night or during weekends. After penetrating a system, fraudsters can sometimes wait
for months, ‘sleeping’ inside the system before completing their attack.

Card generation, testing and harvesting

The objective of this attack is for the criminal to acquire knowledge on the existence, status or
other sensitive information related to accounts. For example, in a testing attack a malicious actor
may try to test if a card PAN exists, test CVVs or expiry dates related to a certain PAN or try to
inject any transaction with doctored fields to try to fool the authorisation system in accepting the
transaction as valid.

These attacks can be performed through the transaction authorisation systems or even through
the ACS enrolment verification systems. Account testing attacks can harvest millions of card
credentials if no fraud detection system is in place, with the capability to intercept transactions.
Attacks have been detected where accounts are tested at great speeds (up to 12 per second).

Testing the accounts can be performed on certain merchants that do not have mechanisms in
place to detect these kinds of attacks and once the elements are all known, the attacker can
perform high value transactions on unsuspecting merchants.

Simple Account Take Over

A cardholder enrols to a payment page on a merchant’s website who has a secure storage solution
(PCI compliant or equivalent) of card data on file. The loading of card data on file occurs with or
without 3DS. The access for making payments on the merchant site is sometimes through a simple
cardholder ID and password, chosen by the cardholder. In this case a fraudster can find out about
these credentials and subsequently make payments using the cardholder’s secured card-data-on-
file, after possibly changing delivery address, service to be delivered etc.

www.epc-cep.eu

67 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

Digital skimmers

Malicious code is increasingly being injected into websites catering for the payment process at
various e-commerce merchants. The code can identify the card and customer credentials, provide
them to the criminal and later resolve itself to avoid detection. The Magecart groups responsible
for this are highly active and are behind several noticeable incidents.

Fake merchants

A huge source for stolen card credentials, is the increasing number of fake merchant websites that
can offer anything from high end consumer goods to gift cards or freight deliveries. They often
work through social media advertisement, phishing e-mails or text messages. Even if the card
holder’s authorised or not authorised card payment is declined by the issuer’s preventive
measures, the actors behind the fake merchant still apprehend the customer and card credentials,
to later be used for various fraudulent attempts.

Authorized fraud and scams
With more SCA solutions in place all over Europe, this type of card not present fraud is increasing
and expected to increase even more as the related requirements of the PSD2 ([1]) and the RTS
([2]) legislation get implemented. Basically, the fraudster goes after the weak link in a SCA
payment chain, which often is the human. You could normally split this modus operandi in two
main tracks, both often initiated via some sort of phishing:

•

Identity theft. The fraudster steals or tricks the victim to disclose their card/personal
credentials/online banking verification methods and thereafter make the transaction,
often to money mule accounts. Here we also have seen a recent problem with Global
Wallets for contactless or e-commerce payments. If the card issuer does not have strong
enough enrolment and card credential provisioning solutions, this service can become a
vessel for social engineering fraudsters who download wallets into their own mobile
devices and can perform fraudulent SCA-transactions. In many of these types of fraud the
entry point towards the victim consists of different forms of phishing/vishing/smishing
obtaining the online banking credentials and the exit of money is with card payments.
•  Authorised card transaction scams. In this case the fraudster persuades the card holder to
perform the transactions themselves, either by impersonating to be someone/something
else or by selling fake services or goods. This fraud can be very devastating for the victim
since they are not always refunded in view of unclear definitions of fraud and related
liability. There is also often a personal shame in being scammed like this, hence the hidden
number of victims can be big. Examples of authorised transactions fraud where card
payments are used include investment fraud, romance fraud, phishing sms/e-mails leading
to fake websites, fake purchases of goods turning into unwanted subscriptions, fake
advertising for renting apartments etc. Recently, more elaborate spear phishing techniques
has been seen to a greater extent, where the fraudster has spent time for background
checks and in various ways create a more plausible story for the victim to believe when
they are approached, e.g. pretending to be from the card issuer security department or the
police.

3.3.2.3  Suggested Controls and Mitigation
For Merchants and acquirers:

•  3D Secure: security protocol to authenticate users for payment card transactions in card-

not-present scenarios. 3DS version 2.x has enabled the possibility for the merchant to pass

www.epc-cep.eu

68 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

extra data to the issuer. This data supports risk-based authentication maintaining the
transaction as frictionless as possible, and should be used for fraud detection systems
•  Tokenisation: process of substituting sensitive data with a non-sensitive equivalent called
token. This reduces the risk as well as liability related to an eventual data compromise .
•  Fraud monitoring: deploy a responsive, real-time fraud system with prevention capabilities

that identifies suspicious patterns of behaviour.

•  Patch vulnerabilities and adopt recommendations: always use the latest recommended
update and recommendations for the operational systems from service provider, card
schemes, etc. Always patch systems when needed.

•  Perform an annual risk assessment by your Security, Risk and / or Fraud Departments to

check if all mitigating measures are completely set and in control.

•  Educate store employees on how to identify and how to act when they suspect fraudulent
behaviour in POS-environment. Make sure to have well working routines to alert and how
to protect the cash register and card terminals.

•  Store and process customer data according to PCI DSS standards (if the respective card

scheme adheres to this standard). Restrict the number of places where card data is stored
and processed to a minimum. If possible, do not store card data in your own environment,
rather let the payment gateway or service provider do that.

•  Make sure that the customer onboarding process when signing new card terminal

agreements, is robust and performs a diligent KYC to avoid bad actors getting into the
system to be able to accept card payments for illicit purposes.

•

In order to mitigate ATM relay attacks, tweak the timeouts to trim excessive chip card
response times.

•  Check integrity of card data whenever possible so that magnetic stripe, chipcard and

contactless data are consistent between themselves.

For Card Issuers:

•

Inform cardholders of the contact channels for reporting lost and stolen cards or any
detected suspicious fraud situation.

•  Provide means for the cardholder to consult bank statements in order to facilitate the

detection of illegitimate transactions.

•  Geo-blocking: to protect payment cards from being misused by skimming fraud, it is

strongly recommended to protect payment cards within a geographical region of use.
•  Restrictions and blockings: To limit the usage of payment cards to specific channels or

specific contexts according to the Issuer’s defined risk appetite.

•  Offer virtual cards that will have lowered spending limits, shorter validity periods or

restrictions on the merchants where they may be used.

•  Adopt Strong Customer Authentication (SCA) with every aspect of the payment card and

PIN replacement.

•  3D Secure: security protocol to authenticate users for payment card transactions in card-

not-present scenarios. 3DS version 2 .x should be adopted given that the extra data passed
on from the merchant to the issuer will allow a risk-based authentication maintaining the
transaction as frictionless as possible.

•  Card synchronisation in stand-in systems: some stand-in systems have no knowledge of
what cards exist and are active (they only know of the ranges of cards that they process)

www.epc-cep.eu

69 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

and therefore the capability to detect account testing attacks is greatly reduced so too is
the capability to protect against brute force attacks.

•  Non-sequential issuance of cards. Some issuers still issue cards in a sequential manner.
Thus, all cards in a certain range will be valid and with the same expiry date. In order to
reduce the level of success for an attacker to determine valid PANs and also in order to
help fraud detection systems, PANs should be issued in a non-sequential fashion. By doing
so, an attacker that sweeps through a range of PANs, will generate a high percentage of
‘Inexistent PAN’ errors and ultimately be detected with greater ease.

•  Card limits: allow for easy access customer customisation of ATM withdrawal limits, daily

spend, e-com environment and contactless functionality, possibility for temporary block in
mobile bank app etc. Promote customer awareness on this.

•  Transaction information: inform your cardholders about authorised transactions in real

time (could be SMS or push messages) to enable quick customer feedback.

•  Perform an annual risk assessment to check if all mitigating measures are completely set

and in control.

•  Besides the technical measures, awareness-raising (customer education) is an essential

point to prevent, more in particular, ‘low-tech’ fraud.

•  Work together, non-competitively, with other players and law enforcement agencies

within your market to establish good communication lines and information sharing forums.
Use these forums for mutual information sharing and raise awareness to customers.

•  Make sure your Fraud and Chargeback team works closely together and with resources and

tools available to identify the growing problem of friendly fraud.

•  Within your local market, engage in working with others to develop standardised digital
identification methods for safer e-com purchases and online access to bank account
information.

•  Make sure no credit limits can be overdrawn in any offline environment with your issued

cards. Perform a diligent credit underwriting process.

•  Make sure no offline limits can be reset by card holder actions to commit friendly fraud.
•  Global Wallets: employ an enrolment solution with Strong Customer Authentication to

heavily reduce the risk of fraud.

•  Fraud monitoring: use a multi-layered approach from authentication to authorisation,

which includes automatic customer interaction. Deploy a responsive, self-learning, real-
time fraud system with prevention capabilities and risk scoring. Ensure your fraud system
identifies suspicious patterns of behaviour to stop fraud based on both generic and tailor-
made scenarios and rules.

•  Geographically incompatible fraud rules are quite important to detect card present

transactions that are impossible to be performed given the excessive velocity necessary to
perform both transactions. This is quite useful to help detect some relay attacks such as
the ATM MitM and relay attack.

•  Deploy mechanisms and intelligence designed to proactively identify breached, leaked and
skimmed card credentials with the purpose of taking action such as card exchange or
dedicated monitoring on specific at-risk cards.

www.epc-cep.eu

70 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

For Cardholders:

•  Always keep your payment card in a safe place and protect your PIN. Report immediately

to your card issuer, if the payment card goes missing.

•  When typing in your passwords or PINs, especially in public environments, shield the typing

from rogue cameras or eavesdropping attackers, with your hand or body.

•  Do not give away your personal information or codes to your identification method if you

do not initiate the event yourself.

•

•

If a financial institution offers controls on limits and e-com and contactless functionality for
the payment card, ensure you set these at the settings typical for your daily usage.

If your financial institution offers geo-blocking, set the correct geographical region of use
and adjust it on time for your convenience.

•  Always check with your card issuer first if you receive suspicious information or requests
via SMS/mail/telephone to initiate a log-in procedure or approve a transfer. The issuer
never requests the cardholder to do that. Fraudsters typically press on the urgency for the
victim to act fast, which is also not how banks and issuers communicate.

•  Avoid  to store your card credentials ‘on file’ at an e-commerce merchant. But if not, make
sure that you understand what type of payments can be made, and who is able to initiate a
payment with your card.

•  Always stop and challenge if a social media advertisement is too good, an offer seems very
lucrative or if someone tries to talk you into investing in a once in a lifetime opportunity.
Check with your issuer or bank first and talk with a family member or friend to assess the
situation in a calm way.

3.3.3  Mobile Wallets for Card Payments
Innovations in mobile payment options facilitate adoption of this technology by consumers and
businesses, but also increase the interest of fraudsters to steal money, payment card information
or history of operations.

Mobile wallet card payments like all other payment types are exposed to the generic payment
process relevant attacks mentioned in Section 3. There use cases may include contactless and
card-not-present in-app e-commerce payments, but may also be based upon prepaid accounts or
cover for person-to-person payments. By the fact that implementations are typically all virtual,
mobile wallets supporting card payments generally leverage some type of card tokenization and
with this also take advantage of the security add-ons that tokenization offers over physical cards.
Nevertheless, mobile wallets also introduce new threats and third-party dependencies worth
taking a closer look in this section.

Card payment wallet specific threats

In order to best possibly leverage today’s mobile user experience and mobile device support for
biometric authentication, card schemes encourage wallet providers to support Consumer Device
Cardholder Verification Methods (CDCVM) instead of traditional CVMs like PIN@PoS (Point of
Sale) or signature.

What this means from an ecosystem perspective is that

(i)

terminals cannot work offline anymore with cards proposing CD CVM in contactless
transactions (there is no plastic card anymore to support classical CVMs)

www.epc-cep.eu

71 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

(ii)

(iii)

card credentials cannot be protected by certified payment chips anymore (there is no
payment chip as those wallets exist only virtually on a mobile phone or server)
issuers cannot authorise transactions on the basis of a PIN securely entered at a POS
anymore (as PIN entry and verification are substituted by CD CVM on the mobile device).

In summary card payment wallets thus come with a significant increase in user experience at the
cost of a new ecosystem setup, in which Original Equipment Manufacturers (OEMs) and wallet
providers often take over a large part of the security set-up without taking over its associated
liability.

As a matter of fact, security largely differs between mobile device types and wallets. CD CVM
credentials may be biometric, possession- or knowledge-based and card keys or tokens may be
hardware or software protected. Moreover, mobile wallets may confirm a successful CD CVM
based authentication to the card or token issuer on the basis of a device being unlocked at the
time of payment initiation or may require an on-purpose validation of a device unlock credential
or a wallet-specific authentication means.

Specific threats in the mobile wallet and CD CVM space include targeted attacks on mobile device
key stores, unlock credentials, user interfaces and NFC controllers. All of these may get exposed
through malware leveraging privilege escalation or rooting / jail-breaking exploits. Although
mobile devices come with inherent security like secure boot and app signing and sandboxing,
drive-by privilege escalations attacks keep on being reported across all operating systems.

Particularly worth mentioning in the mobile wallet space are NFC relay attacks, whereby a card on
the cardholder’s mobile device can relatively easy get exposed to contactless payments on a
fraudster device. But also other mobile device interface attacks, in which a fraudulent app
remotely exposes the mobile device user interfaces (display and/or touch input) or tricks a user in
submitting his device’s unlock credentials for a fake purpose (e.g. fingerprint for health checking)
pose new threats. While there is first evidence from EAST56 about an increase of relay attacks
happening in the wild, interface attacks have been observed at various levels for a while. An
illustrative example for remote exposure of user interfaces is the accessibility interface attack
formerly observed against a well-known payment processor57 but also the newer attacks by the
Vultur RAT58. Worth mentioning are also physical attacks against biometric authentication
implementations, be it through copying fingerprints from the touchscreen or exploiting biometric
sensor implementation weaknesses59.

For a high-level coverage of mobile application user, mobile device and digital wallet application
threats, the ENISA report from 2016 on the ‘Security of Mobile Payments and Digital Wallets60 still
remains a good reference.

3.3.3.1  Suggested Controls and Mitigation
Segregation mechanisms like Trusted Execution Environments (TEE) but also privilege escalation
detection and remediation mechanisms like root-kid detection or secure device boot today
represent inherent mobile platform security features that together with regular OS updating lay a
strong security foundation for mobile wallet implementation. However, as they regularly also

56 https://www.association-secure-transactions.eu/european-terminal-fraud-attacks-double/
57 https://www.welivesecurity.com/2018/12/11/android-trojan-steals-money-paypal-accounts-2fa/
58 https://arstechnica.com/gadgets/2021/07/new-bank-fraud-malware-called-vultur-infects-thousands-of-devices/
59 https://www.computing.co.uk/news/3082909/natwest-nationwide-samsung-fingerprint
60 https://www.enisa.europa.eu/publications/mobile-payments-security

www.epc-cep.eu

72 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

show exploitable software bugs and network providers at some point in time block OS updates for
older devices, the security of CD CVM must independently be assured.

An EMVCo document61 covers for both ‘CD CVM best practices’ and ‘CD CVM security
requirements’. While the security requirements document comes with a very comprehensive risk
analysis and specific CD CVM attacks and countermeasures, the best practice document states the
following general security-related recommendations that give a good insight to the challenges
encountered and worth controlling in this rapidly growing third-party dependency space:

•  Do not set a dormant value (factory-set default Reference Data) for a CD CVM Solution
•  Warn the user when prompting for consumer authentication if the device is not in the

appropriate secure state.

•  Prolonged authentication should not extend beyond a reasonable period of time.
•

If the conditions for persistence are broken, then re-authentication must be performed.

•  The number of incorrect CD CVM attempts should be limited.
•  Do not allow weak CD CVMs
•  Manage the lifecycle of a CD CVM appropriately
•  Biometric modalities should not allow the registration of too many of those same

modalities.

•  The platform should provide a means for a Mobile Application to determine whether a

suitable level of consumer authentication is active for the device.

•  The fall-back/primary CD CVM should be sufficiently strong.
•  For a biometric, there should be a balance between allowing the verification of the

incorrect biometric and not verifying the correct biometric.

•  There should be a mechanism for liveness detection and the ability to spoof the solution

should be minimised.

To support these objectives, EMVCo has established a Security Evaluation Process to help ensure
CD CVM solutions maintain certain minimum levels of security, including mechanisms and
protections designed to withstand known attacks.

61 https://www.emvco.com/terms-of-use/?u=wp-content/uploads/documents/CDCVM-statement_FINAL.pdf (the
document is in the members’ area of the EMVCo website, credentials are needed to access it)

www.epc-cep.eu

73 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

4  Liability Shift Discussions related to Specific Fraud Types
Social engineering (c.f. Section 3.1.1) aims at tricking the customer in a self-exposing behaviour he
or she is not supposed to adopt. As a consequence, the customer at first hand appears liable for
his or her own misbehaving. The fact that APP fraud or more generally fraud related to scams has
been rapidly growing over the last years raises attention among regulators on how to possibly
counter this evolution with liability shifts.

While website and email domains allow for technical controls that help mitigating the phishing
exposure, fraudsters started increasingly leveraging phone or SMS calls with fake caller IDs to
impersonate the customer’s bank or other authoritative authorities. With caller IDs not under the
remit of the banks but solely under the control of the respective ECSP, liability shifts discussions
have extended to focus not only on banks but, in case of impersonation via phone or SMS, also on
ECSPs.

Discussions are still ongoing and are neither conclusive nor fully aligned for the time being.
Nonetheless, there is an observable tendency to increase PSP’s and ECSP’s liability for not
detecting fraud occurring because of social engineering and impersonation of banks.

UK Status

Discussions started in the UK, where the Payment Systems Regulator by now mandates sending
and receiving PSP to cover each one for 50% of the reimbursement in cases where customers fall
victim of APP fraud. While this is backed by the Financial Services and Markets Act from 2023, the
legislation has been released end of 2023 and reimbursement obligations have become effective
since Q4 2024, with facts nicely consolidated in a policy statement from May 202562. The
reimbursement requirement applies only to Faster Payments and CHAPS payments sent and
received by PSPs in the UK across the Faster Payments system, including payment initiation service
(PIS) transactions.  There is currently no liability shift to ECSPs.

SG Status

MAS and IMDA released a framework for equitable sharing of losses arising from phishing scams.
The shared responsibility framework63 turned into force in Q4 2024 and is the first one that also
deals with impersonation of a legitimate business or government entity (e.g., FIs, non-banks and
government agencies) over telecom networks. It makes not only banks but eventually also ECSPs
liable for reimbursing phishing scams that happen because of impersonation.

EU Status

In the EU, the draft payment services regulation (PSD3/PSR) proposal from 2023 also deals with
the topic64 by granting customers a refund rights in two situations:

•  when consumers suffered damages caused by the failure of the IBAN/name verification

service to detect a mismatch between the name and IBAN of the payee

•  when consumers are falling victim of a spoofing fraud where the fraudster contacts the
consumer pretending to be an employee of the consumer’s bank, tricking the consumer
into carrying out some actions causing financial damages to the consumer.

62 See https://www.psr.org.uk/publications/policy-statements/ps255-app-scams-reimbursement-requirement/
63 https://www.mas.gov.sg/regulation/guidelines/guidelines-on-shared-responsibility-framework
64 See https://ec.europa.eu/commission/presscorner/detail/en/ip_23_3543

www.epc-cep.eu

74 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

While the negotiation on finalizing PSD3/PSR proceed, it appears that liability shifts to ECSPs have
been added in there as well. The EBA 'Opinion on new types of fraud and possibly mitigations65
from April 2024 notably states:

“…additional provisions to mitigate fraud have been proposed in a report by the European
Parliament’s Economic and Monetary Affairs Committee (ECON) on the PSD3/PSR proposals
and agreed by the European Parliament in a vote in April 2024. These aim, for example, at
making electronic communications service providers outside the financial sector - e.g.
telecommunications and internet providers, social media companies - also responsible for
tackling payment fraud.”

As those liability shifts are for authorized payments only and are subject to no gross-negligent
behavior from the customer, the EBA also suggested that a proper delineation between
authorized and unauthorized transactions, as well as a clarification of the concept of ‘gross
negligence’, be further considered for inclusion into the legislation.

The final PSD3/PSR legislation is still expected by end of 2025 / beginning of 2026.

65  https://www.eba.europa.eu/publications-and-media/press-releases/eba-has-identified-new-types-payment-fraud-
and-proposes-measures-mitigate-underlying-risks-and

www.epc-cep.eu

75 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

5  Annex I – Summary Threats versus Controls and Mitigations

Threat

Suggested Controls & Mitigations

Social Engineering
Section 3.1.1

Malware
Section 3.1.2

Awareness campaigns for consumers, SMEs and corporates, and PSPs staff
Technical measures for email security (SPF, DKIM, DMARC)
Use of authentication mechanisms that do not expose user credentials
Transaction filtering and monitoring
Enable customers to determine if an email, call or website is genuine
Takedown of phishing web sites

Applicable to the following payment-relevant processes:
On-boarding/provisioning, Request-to-Pay/Invoicing,
Initiation/Authentication, Execution

Regular software updates on consumer devices including mobile devices
Firewalls and antivirus on consumer devices
Awareness campaigns by PSPs to customers and staff, including
awareness about danger of opening attachments
Script and macro blockers, IPS / IDS functionality
Limited usage of admin rights
Web traffic and email content analysis
Specific controls and mitigation measures targeting Cloud services

Advanced
Persistent Threats
Section 3.1.3

Distributed Denial
of Service
Section 3.1.4

Applicable to the following payment-relevant processes:
On-boarding/provisioning, Request-to-Pay/Invoicing,
Initiation/Authentication, Execution

Behaviour analysis tools
Real time advanced security data analytics
Incorporation of security threat intelligence into infrastructure
Advanced IP scanner/ APT scanner
Red Team/Blue Team approach
Five styles of Advanced Threat Defense Framework

Applicable to the following payment-relevant processes:
Execution

Dynamic DDoS security control framework
DDoS mitigation scrubbing service
Periodic tests of anti DDoS measures
Security intelligence feeds and incident response team
‘Forensic ready’ logging

Applicable to the following payment-relevant processes:
Execution

Botnets
Section 3.1.5

Blacklisting
Sinkholing and blocking
Distribution of fake/traceable credentials

www.epc-cep.eu

76 / 77

Report 2025 Payments Threats and Fraud Trends

EPC162-24/ Version 1.4

DNS-based countermeasures
Direct takedown of C&C server
Packet filtering on network and application level
Walled gardens
Peer-to-peer countermeasures
Infiltration and remote disinfection
Take downs by law enforcement
Awareness raising and co-operation

Applicable to the following payment-relevant processes:
Execution

Third-party and
supply chain
attacks
Section 3.1.6

Management of relations with suppliers in a way to ensure effectiveness
of the contractual clauses related to IT security measures.
Apply a risks assessment process able to identify dependencies on third-
party suppliers.

Monetisation
Channels
Section 3.1.7

Raise awareness
Register/ share information about identified mules
Monitor, detect and stop mule-like behaviour at PSP and regulator level
Detect complex mule and money laundering schemes

Liability for social
engineering fraud
Section 4

Involved stakeholders should be aware of ongoing discussions

Table 7 Summary threats versus controls and mitigations

www.epc-cep.eu

77 / 77