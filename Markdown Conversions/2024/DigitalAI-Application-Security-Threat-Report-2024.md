# 2024 Application Security Threat Report

## Table of Contents
- [Introduction and key findings](#introduction-and-key-findings)
- [Terminology](#terminology)
- [How at risk is your app in 2024?](#how-at-risk-is-your-app-in-2024)
- [Risks to apps by industry](#risks-to-apps-by-industry)
- [Risks to apps by device type](#risks-to-apps-by-device-type)
- [The relationship between risk and popularity](#the-relationship-between-risk-and-popularity)
- [Risks across app instances](#risks-across-app-instances)
- [Protecting your apps in the wild](#protecting-your-apps-in-the-wild)
- [Contact us](#contact-us)
- [Appendix: methodology](#appendix-methodology)

---

## Introduction and key findings

There is no question that we’re living in an app-happy world. The Apple Store now offers 1.96 million apps; the Google Play store has 2.87 million apps;[^1] and a whopping 148.2 billion mobile, desktop, and web apps were downloaded in 2023.[^2] More than 52,000 new apps were released on Google Play in February 2024 alone.[^3]

The problem is that these apps, which typically run outside corporate firewalls (“in the wild”), are prime targets for cybercriminals. And the security risks are rising even faster than app usage. There are now more than a billion malware programs out there, and 560,000 new pieces of malware are detected daily.[^4]

However, since most research focuses only on threats and attacks inside corporate firewalls, app users have only a vague notion of the risks that could impact them, and security researchers have little guidance on how to protect apps and their users.

This study continues the work Digital.ai initiated in 2023 by illuminating and quantifying threats to apps in 2024. It also offers insights about the rising use of AI (by app developers and cybercriminals), along with advice on specific actions security teams can take to stay a step ahead of hackers.

### Key findings
**01 Overall risk is up:** The likelihood of an app being attacked over a 4-week period rose from 57% in 2023 to 65% in 2024.

**02 Gaming and FinServ vulnerabilities remain high:** Gaming and financial services (FinServ) apps face the highest risk of attack (76% and 67%, respectively), and the risk in both sectors is up since 2023.

**03 Android and iPhone attacks surging:** Android apps remain more likely to be run in unsafe environments than iPhone apps (70% vs. 94%, respectively), but the likelihood of both has spiked in 2024.

**04 Popularity does not increase risk:** Less popular apps are often attacked more frequently than popular apps.

---

## Terminology

- **Application or app:** One discrete executable that runs on a mobile operating system, in a browser, or on a desktop/server operating system.
- **Consumer:** The end-user of applications created by Digital.ai customers.
- **Instance:** One discrete executable on a single consumer’s device.
- **Attack:** Any action taken on a mobile/web/desktop app that violates the EULA (End User License Agreement) of the organization creating the app and/or the App Store/Play Store.
- **Guard:** A protection added to an application to frustrate reverse engineering or tampering attempts.
- **FinServ app:** Any consumer-facing application created by a bank, insurance company, credit card issuer, or payments platform.
- **Gaming app:** Any web, mobile, or desktop app used to play games, exclusive of apps used to place bets or to gamble.
- **All other verticals:** An application made by an organization in any industry other than the gaming or FinServ industry — for instance, medical devices, manufacturing, online retail, industrial controls, etc.

---

## How at risk is your app in 2024?

The data in this report is anonymized and aggregated global customer data collected over a four-week period from February 1 to February 28, 2024. “Risk,” in this case, is measured from the enterprise creating the application’s perspective.

### Overall threat level
In 2023, the inaugural year of this study, the likelihood of an app being attacked in a four-week period was 57%. In 2024, that figure rose to 65%. This uptick was driven by several trends:
- **Tool democratization:** Reverse-engineering tools (Ghidra) and dynamic instrumentation toolkits (Frida) are becoming more sophisticated.
- **Cryptocurrencies:** Rebound in crypto makes it easier for threat actors to “cash out.”
- **Nationalization of attacks:** State-sponsored resources are increasingly available to threat actors.
- **Jailbreaking:** An increase in jailbreaking activity to bypass OS restrictions.
- **AI/ML:** Surging use of AI increases productivity for both developers and malware creators.

A recent McKinsey study[^5] found that generative AI can increase development speed by 10-30 percent. This translates to faster malware coding and more effective attacks.

---

## Risks to apps by industry

The study found that gaming and FinServ apps continue to be the most likely to be attacked.

- **FinServ app attack likelihood:** February 2023 (62%) | February 2024 (67%)
- **Gaming app attack likelihood:** February 2023 (63%) | February 2024 (76%)

Apps outside of FinServ and gaming still have a 66% chance of being attacked. Examples include implantable medical devices, Bluetooth-connected car apps, and industrial control software.

---

## Risks to apps by device type

Android apps remain more likely to be targeted with environmental attacks than iPhone apps (70% vs. 94%, respectively), but attacks on both have spiked in 2024.

- **iOS app likelihood of unsafe environment:** 2023 (34%) | 2024 (84%)
- **Android app likelihood of unsafe environment:** 2023 (70%) | 2024 (94%)
- **iOS app attack likelihood:** 2023 (17%) | 2024 (29%)
- **Android app attack likelihood:** 2023 (70%) | 2024 (94%)

The rise in iOS vulnerabilities is partially explained by the ongoing phenomenon of iOS jailbreaking.

---

## The relationship between risk and popularity

Similarly to the 2023 study, the 2024 edition found no correlation between the likelihood of being attacked and the app’s popularity. 

![Scatterplot showing popularity vs. attack frequency for 2023 and 2024]

---

## Risks across app instances

To grasp the full scope of cybersecurity challenges, it is imperative to delve deeper into the granularity of app instances. The following table outlines attack risk by OWASP MASVS guard category.

![Table: Attack risk by OWASP MASVS guard category]

- **Unsafe environment guards:** The odds of an individual instance of an app suffering an attack on its environment were .96%.
- **Application integrity guards:** The odds of an individual instance of an app suffering an integrity attack were .19%.
- **Instrumentation detection guards:** The odds of an individual instance of an app suffering an instrumentation attack were .02%.

---

## Protecting your apps in the wild

Digital.ai offers application security solutions that build in security in multiple ways:

**Embedding security into the development process:**
- Obfuscate code to prevent reverse-engineering.
- Prevent tampering by detecting unsafe environments and code changes.
- Configure customized or automated protections.

**Providing visibility:**
- Produce stand-alone reports or integrate with existing Security Operations Center tools.
- Create searchable logs.

**Automatically responding to threats:**
- Force step-up authentication.
- Alter app features.
- Shut down applications that are under attack.

---

## Contact us
For more information, visit [https://digital.ai/why-digital-ai/contact/](https://digital.ai/why-digital-ai/contact/)

---

## Appendix: methodology
This study was conducted using anonymized and aggregated data gathered from Digital.ai App Aware customers around the globe from February 1 to February 28, 2024.

---

[^1]: 42matters, April 2024.
[^2]: Statista, February 2024.
[^3]: Statista, March 2024.
[^4]: AV-Test Institute, 2024.
[^5]: McKinsey & Co., “Unleashing Developer Productivity with Generative AI,” June 27, 2023.