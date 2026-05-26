# Secure Sign-in Trends Report 2024

## Table of Contents
- [First, a word on measuring MFA adoption](#first-a-word-on-measuring-mfa-adoption)
- [Summary of key findings](#summary-of-key-findings)
- [Introduction](#introduction)
- [How to use the data](#how-to-use-the-data)
- [Current state of MFA adoption](#current-state-of-mfa-adoption)
- [MFA adoption over time](#mfa-adoption-over-time)
- [MFA adoption by region](#mfa-adoption-by-region)
- [MFA adoption by industry](#mfa-adoption-by-industry)
- [MFA adoption by organization size](#mfa-adoption-by-organization-size)
- [MFA adoption by user type](#mfa-adoption-by-user-type)
- [MFA adoption by authenticator type](#mfa-adoption-by-authenticator-type)
- [A data-driven assessment of authenticator usability and security](#a-data-driven-assessment-of-authenticator-usability-and-security)
- [Authenticator challenge time](#authenticator-challenge-time)
- [Authenticator enrollment time](#authenticator-enrollment-time)
- [Authenticator challenge failure rate](#authenticator-challenge-failure-rate)
- [Phishing-resistant coverage](#phishing-resistant-coverage)
- [Phishing-resistant alert coverage](#phishing-resistant-alert-coverage)
- [Authenticator challenge brute-force failure rate](#authenticator-challenge-brute-force-failure-rate)
- [Authenticator Metric Survey](#authenticator-metric-survey)
- [Assessing authenticator performance and adoption](#assessing-authenticator-performance-and-adoption)
- [The way forward](#the-way-forward)
- [Methodology](#methodology)

---

It took a little time to convince the world of the virtues of multi-factor authentication (MFA).

From the outset, the consensus in the security community was that MFA was essential to protecting against wave after wave of password-based attacks, but many organizations would only require an MFA challenge for access to their most treasured systems.

During the pandemic, MFA adoption went mainstream. Okta observed a 15% rise in the use of MFA within a few short months, as the world rushed to support remote work. We’re now at the point where most Okta admins, and the majority of users, access workplace applications after MFA challenges. And we’re seeing regulators and standards bodies across the world demanding that organizations secure access with these stronger sign-in methods.

In this year’s Secure Sign-in Trends Report, we find strong growth in the adoption of passwordless, phishing-resistant sign-in methods. In January of this year, 5% of users on our workforce platform didn’t sign in once using a password. That small number belies a huge, latent, exciting potential. It’s a small number that says that passwordless is here and now. It’s possible. If these Okta customers did it, so can you.

So we expect the next wave of MFA adoption won’t be driven by security purists, or even by those very sensible policy makers demanding that regulated entities enroll users in MFA. It’s going to be driven by a demand for a better user experience and higher security assurance. Once you’ve experienced passwordless, whether as an employee or a customer, you will never want to go back.

I hope you enjoy geeking out on these numbers. Thanks for reading.

**Todd McKinnon**
CEO, Okta

---

## First, a word on measuring MFA adoption

Before you dive in, it’s important to understand that the data and conclusions in this report reflect the authentication choices made by organizations, their administrators, and employees. While we frequently refer to users, these users are typically employees in a workplace setting and their authentication options are often limited by organizational policies.

There are multiple ways to measure multi-factor authentication (MFA) adoption. For this study, we measured adoption for actual MFA usage: the percentage of users who signed in using MFA over a given period.

![Table: Measurement and Aggregation options for MFA adoption]

It’s also important to keep in mind that this study only counted direct MFA authentication events in the Okta Workforce Identity Cloud (WIC). If users authenticate exclusively using MFA provided by other Identity providers and make use of enterprise federation or social login to connect to Okta, they are not captured by our MFA adoption data. Therefore, it’s likely that the reported MFA adoption rate will slightly underestimate the overall rate of MFA use among our customers. We have also excluded test accounts. All adoption and metric data is derived from revenue-linked production orgs/tenants.

---

## Summary of key findings

- **MFA adoption continues its upward trajectory**: As of January 2024, MFA adoption climbed to 66% among Okta workforce users, and 91% of administrators use MFA.
- **Adoption rates vary widely by industry and company size**: Government and Education saw above 5% year-over-year growth in adoption.
- **Phishing-resistant authenticators show great momentum**: The adoption rate for FIDO2 WebAuthn increased from 2% in 2023 to 3% in 2024, while the adoption rate for Okta FastPass leaped from 2% to 6% in the same time period.
- **Passwordless has arrived**: The number of Okta customers who are using passwords is finally starting to decline. Just under 5% of users did not use a password during any sign-ins during January 2024.
- **Security vs. user experience is a false choice**: Phishing-resistant authenticators offer a superior user experience. In our authenticator performance and usability assessment, FastPass and FIDO2 WebAuthn came out on top.

---

## Introduction

"[Multi-Factor Authentication] MFA is widely recognized as one, if not the most, important preventative security controls available today. It provides a strong defense against various adversarial attack techniques such as password spraying, compromised password reuse, and—in some instances— phishing. However, a key challenge is that it is notoriously difficult to deploy and many organizations, small and large, still have not done so even if they recognize the value." [^1]

In this report, we explore the wide variety of approaches companies today are taking to verify their users' identities and prevent unauthorized access. Based on anonymized data from Okta customers’ billions of monthly authentications, we've updated our assessment of the state of authentication.

[^1]: https://media.defense.gov/2023/Oct/04/2003313510/-1/-1/0/ESF%20CTR%20IAM%20MFA%20SSO%20CHALLENGES.PDF

---

## How to use the data

This report provides a framework for measuring the usability and security properties of a comprehensive list of authenticators. We asked critical questions to help CIOs, CSOs, and policymakers understand the why behind the varying rates of MFA adoption, including:

- How has MFA adoption changed over time?
- Does an organization's industry group, location, or size affect MFA adoption rates?
- What observable usability features are relevant to MFA adoption?
- What observable security features are relevant to MFA adoption?

---

## Current state of MFA adoption

MFA is an essential part of any high-assurance security posture. When signing in using MFA, a user must provide two or more distinct factors to verify their Identity.

### MFA adoption over time
As of January 2024, 66% of users sign in using MFA. Since the pandemic-driven surge in 2020, year-over-year growth in MFA adoption was at 6% per year from 2020 to 2023, and slowed down to 2% in 2024.

### MFA adoption by region
MFA adoption rates are between 61 and 68% for the Americas (AMER), Asia Pacific (APAC) and EMEA (Europe, Middle East and Africa). Location is not a primary determining factor in MFA adoption.

### MFA adoption by industry
The technology sector continues to record the highest MFA adoption rate (88%). Government and Education sectors saw an increase of above 5% year-over-year.

### MFA adoption by organization size
There is a rough inverse correlation between the number of employees and the rate of MFA adoption: The larger the organization, the lower the adoption rate.

### MFA adoption by user type
MFA adoption among Okta administrators is 91%. Okta has begun requiring customers to configure MFA to access administrative and management consoles.

### MFA adoption by authenticator type
Traditional MFA authenticators include Email, Hardware Token, Push, Security Question, SMS, and Soft Token. Phishing-resistant MFA authenticators include Okta FastPass, FIDO2 WebAuthn, and Smart Card.

---

## A data-driven assessment of authenticator usability and security

### Authenticator challenge time
Authenticators that combine possession and inherence (such as biometric checks) offer the fastest challenge times (4 seconds).

### Authenticator enrollment time
Voice, SMS, and FIDO2 WebAuthn boast the shortest enrollment times at less than 25 seconds.

### Authenticator challenge failure rate
Knowledge-based authenticators impose the most considerable burden on users. FIDO2 WebAuthn and smart card authentication result in fewer unintended user mistakes.

### Phishing-resistant coverage
Three authenticators have phishing-resistant coverage above zero: Okta FastPass, FIDO WebAuthn, and smart card.

### Phishing-resistant alert coverage
Today, Okta FastPass is the only authenticator capable of creating server-side events when a phishing attempt results in a failed origin check.

### Authenticator challenge brute-force failure rate
Knowledge-based secrets continue to be targeted by automated tools most often. Using authenticators based on possession or biometric factors can dramatically reduce the likelihood of account takeover.

---

## Authenticator Metric Survey

We conducted a survey of Okta IT and Security practitioners to understand the relative importance of each of the usability and security metrics. This allows us to align the data we collected from our logs with the importance that our administrators place on those metrics.

---

## Assessing authenticator performance and adoption

In information security, it’s frequently assumed that technology decision-makers must “trade off” security for user experience. Our analysis finds that this is a false choice. Phishing-resistant authentication offers a superior user experience.

---

## The way forward

Phishing-resistant MFA is secure, user friendly, and achievable. It is the leading technology to protect against pervasive threats.

### 5 tips to improve your authentication strategy
1. **Require MFA** in sign-on policies and enforce phishing-resistance for administrative access.
2. **Make MFA adoption a C-suite and board-level priority.**
3. **Take a Zero Trust approach** to access.
4. **Create dynamic access policies** that evaluate user attributes, device context, and network attributes.
5. **Develop a longer-term plan** to minimize or eliminate the use of passwords.

---

## Methodology

To create this report, we relied on data from Okta Workforce Identity Cloud. We anonymized and aggregated data from billions of monthly authentications and verifications from countries around the world. Customer company size is defined by the number of full-time employees in the company. Company industry taxonomy aligns with the North American Industry Classification System (NAICS).

---

ustry, and geographic region are
validated using third-party resources.

Unless otherwise noted, this report focuses exclusively on Okta
Workforce Identity Cloud data and workforce use cases. It does
not include Okta Customer Identity Cloud data.

51

The Secure Sign-in Trends Report 2024Okta Inc.
100 First Street
San Francisco, CA 94105
info@okta.com
1-888-722-7871