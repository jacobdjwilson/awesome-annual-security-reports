# 2021 Email Threat Report

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Email Spam](#email-spam)
- [Malware in Email](#malware-in-email)
- [Phishing](#phishing)
- [Business Email Compromise](#business-email-compromise)
- [Defending the Email Attack Surface](#defending-the-email-attack-surface)

---

## Introduction

Some of the most significant threats organizations face come in through email. Email has a few advantages as an effective attack vector for hackers. End-users receive email messages whether they want them or not, and email can be easily spoofed to appear legitimate. It’s no wonder that cybercriminals continue to rely on email to distribute malware, phishing scams, and spam.

This report looks at some of the significant email security trends and issues of 2020.

The COVID-19 pandemic left its mark on email security, with many criminals turning to COVID-themed malware and phishing lures to fool recipients into becoming victims. Attackers also got creative with their use of uncommon file types and techniques to defeat email scanners and avoid suspicion. Additionally, Business Email Compromise (BEC) scams grew more sophisticated with their efforts to swindle more money out of large companies, while phishers made ever greater use of popular cloud services to host landing pages and distribute spam.

---

## Executive Summary

- Spam volume continued its long-term decline in 2020, decreasing by 43 percent compared to 2019. Spam volume in 2020 represented just 15 percent of the levels seen seven years earlier in 2014.
- The proportion of malicious attachments in spam increased in 2020 but remains relatively low in a historical context.
- Microsoft documents, namely Word and Excel, are the most common way attackers delivered malware through email.
- Microsoft Excel file attachments were the single biggest attachment type utilized by attackers in 2020, representing 39 percent of malicious attachments, up from 7 percent in 2019. Forty-three percent of malicious Excel attachments made use of Excel 4.0 macros.
- The Emotet botnet was active in the second half of 2020, distributing malicious Word documents encased in password-protected archives before it was disrupted in early 2021.
- Fake extortion scams continued to be spammed out in volume, representing 10 percent of total spam.
- BEC scams continued to have a significant impact on organizations. Trustwave intercepted around 40 BEC messages per day on average for its MailMarshal Cloud customers.
- Over 50 percent of BEC emails come from Gmail accounts.
- Phishers increasingly used free cloud infrastructure to host phishing pages and files for sending emails, hosting phishing pages, storing files, and more. The services are free to use, and cybercriminals enjoy the benefits of piggybacking on the services’ brand reputation.

---

## Email Spam

Overall, spam volumes continued a multi-year decline in 2020. The Spam Volume Index chart illustrates the relative volume changes of spam seen by Trustwave MailMarshal Cloud each year since 2014 by a basket of domains we monitor.

![Trustwave Spam Volume Index chart showing a decline from 1000 in 2014 to 158 in 2020]

The spam received in 2020 measured 158 on the index, or 16 percent of the spam volume received in 2014—a 43 percent decline from 2019. With a number of large botnets having gone dark or ceased spamming in recent years, there is simply less spam circulating on the Internet now than there used to be. This is undoubtedly a welcome development from a spam-management perspective, but the spam that’s left remains a significant threat as we’ll explore later on.

### Spam Subject Matter

The composition of spam changes from year to year, owing to underlying differences in cybercriminal behavior. The chart below highlights significant categories of spam in 2020 compared to 2019.

![Spam Categories 2019-2020 bar chart comparing Health, Adult, Extortion, Dating, Scams, Phishing, Malware, and Other categories]

- Spam promoting pharmaceuticals and health cures is a perennial favorite for spammers, and not unusually, remained the top spam category in 2020 at around 33 percent of total spam.
- By contrast, adult-themed spam, which primarily advertises adult content sites, shot up from a relatively low 5 percent of total spam in 2019 to 27 percent in 2020.
- Extortion scams were consistent with last year, making up around 10 percent of total spam. These scams typically try to extort money from the recipient with fake claims of stolen data. Extortion scams evolved during the COVID-19 pandemic to use virus- and videoconferencing-related themes.
- Dating spam, mostly advertising online dating services, was up slightly to around 10 percent of all spam.
- Email scam volumes fell significantly to 1.36 percent of total spam in 2020. These messages mostly consisted of advance-fee scams in which the recipient is prompted to send the scammer a sum of money with the promise of profit or some other desirable outcome in the future. These include so-called 419 (or “Nigerian prince”) scams, inheritance scams, investment scams, dying widow scams, romance scams, and compensation scams. In 2020 scams also started to use COVID-19 themes.
- Phishing messages dropped significantly in 2020 to around 1.4 percent of all spam. The phishing messages we did encounter in 2020 tended to be more targeted than in the past and included COVID-19 themed phishing messages targeting Microsoft Outlook and Microsoft 365 corporate logins. Another noticeable shift was an increase in common mass emailing services and cloud services to send phishing messages and host phishing landing pages.
- Malware represented about 0.44 percent of total spam, an increase from 0.22 percent in 2019.

---

## Malware in Email

Email containing malware attachments accounted for 0.44 percent of total spam in 2020. This represents an increase over 2019 but remains far below the figures observed a few years ago when large botnets like Necurs routinely sent billions of malicious emails a day, at times representing more than one-quarter of all spam.

![Email Malware as a Percentage of Total Spam 2013-2020 chart]

### Malicious Email Trends and Developments

#### Covid-19–Themed Malware
Unsurprisingly, attackers were quick to take advantage of the COVID-19 global pandemic in malicious email in 2020. The COVID-19 theme showed up in phishing emails, business email compromise (BEC) scams, and in emails containing links or attachments leading to malware. One interesting trick we saw involved sending a Java Network Launching Protocol (JNLP) file that downloaded malware disguised as a COVID-19 mapping program.

![Process flow diagram showing a spam campaign distributing the TrickBot banking trojan disguised as a COVID-19 map]

#### Malicious Excel 4.0 Macros
The Microsoft Excel 4.0 macro language was first introduced in 1992. Most Excel automation—and malware—today makes use of the more powerful Visual Basic for Applications (VBA) scripting language introduced in Excel 5.0, but even the latest versions of the spreadsheet product still support the old Excel 4.0 macros. Lately, cybercriminals have been taking advantage of this by embedding 4.0 macros in modern Excel workbook files with the .xlsm and .xlsb formats.

![A spam message containing a file with malicious Excel 4.0 macros]

#### Working in a VelvetSweatshop
Another Excel 4.0 macro campaign we encountered in 2020 used a curious old feature to evade detection. If the password is “VelvetSweatshop”, Excel does not prompt for the password and simply opens the file in read-only mode. Attackers use this old default password to evade detection by malware scanners.

#### Emotet Evolves
The Emotet botnet operation continued to be a major source of malicious email attachments in 2020. One new technique the Emotet gang adopted involved putting their malicious document payloads into encrypted archive files, with the password contained in the message body, filename, or image.

![Emotet spam with an encrypted archive attachment with the password in an image]

### Malicious Email Attachment Types

![Email Malware Attachment Types 2019-2020 chart]

- Microsoft document files remain the largest category of malicious attachments.
- Notably, there was a significant shift from Word Document files to Excel files in 2020. Excel file attachments were the single biggest attachment type in 2020, representing 39 percent of malicious attachments, up from 7 percent in 2019.
- Malicious executable files remained significant, at 36 percent of the total.
- HTML attachments increased slightly from 8 percent to 13 percent.
- RTF (Rich Text Format) files accounted for nearly 2 percent of the total.

![Archives Distribution in 2020 chart]

More than three-fourths of the ultimate payloads we observed in email in 2020 came from just three malware families: Agent Tesla and Nanocore (RATs), and the banking trojan Dridex.

![Top Spam Malware Payloads 2020 chart]

![Process flow of a spam campaign delivering Agent Tesla]

---

## Phishing

In 2020, phishing messages accounted for 1.4 percent of all spam. Phishers today often try to harvest credentials for cloud services such as Microsoft 365.

### Phishing Trends and Developments

#### Phishing for COVID-19
We observed multiple phishing campaigns that sought to exploit the pandemic with a variety of lures, using subject lines such as “Covid-19 employee relief fund,” and links and attachments purporting to be from health authorities such as the World Health Organization (WHO) or Centers for Disease Control and Prevention (CDC).

![A phishing message masquerading as an official communication from the Centers for Disease Control and Prevention]

#### Malicious Calendar Files
We also observed phishing campaigns using ICS iCalendar attachments in 2020 to circulate Microsoft SharePoint phishing links as meeting invites.

![A phishing message with an iCalendar attachment containing a link to files hosted on Microsoft SharePoint]

#### Extortion Spam
In these scams, the attacker sends messages to prospective victims falsely claiming that they have been hacked or infected with malware. In 2020 the scammers quickly adapted to the COVID-19 pandemic by claiming the victim was hacked during a recent Zoom videoconferencing session.

![A typical Zoom-themed extortion scam email, with a Bitcoin wallet address provided for payment]

#### Phishing in the Cloud
Phishers often abused cloud-based disk storage and office productivity services in 2020, including Google Firebase Storage, Google Drive, Microsoft OneDrive, Microsoft OneNote, Microsoft Sway, and Microsoft SharePoint.

![Various images showing phishing messages sent through Microsoft OneDrive, Microsoft OneNote, and Google Firebase Storage]

---

## Business Email Compromise

Business email compromise (BEC) is a targeted form of phishing that criminals use to steal large sums of money from companies. According to the FBI, BEC is the most damaging type of cybercrime in terms of victim losses, amounting to more than US $1 billion per year with an average of $75,000 per incident.

### Most Common BEC From Address Domains
Gmail is a massively popular platform for sending BEC messages. More than 58 percent of BEC messages were sent with a gmail.com address in the From: field.

![Most Common BEC From Address Domains chart]

### Most Common Subjects in BEC Emails
Many are sent with single-word subject lines, such as "Request" or "Response".

![Most Common Subjects in BEC Emails chart]

---

## Defending the Email Attack Surface

To protect against the impact of email attacks, organizations should consider:

- Deploying an email security gateway.
- Locking down inbound email traffic content (quarantine executable files, block/flag macros, block password-protected archives).
- Keeping client software such as Microsoft 365 and Adobe Reader fully patched.
- Ensuring potentially malicious or phishing links in emails can be checked.
- Deploying anti-spoofing technologies (SPF, DKIM, DMARC).
- Educating users through security awareness training and mock phishing exercises.

---

Trustwave is a leading cybersecurity and managed security services provider focused on threat detection and response. For more information about Trustwave, visit [www.trustwave.com](http://www.trustwave.com).