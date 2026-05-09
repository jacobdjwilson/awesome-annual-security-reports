# 2024 State of Software Supply Chain Security

## Table of Contents
- [Key Findings](#key-findings)
- [Everybody’s Talking About SSCS](#everybodys-talking-about-sscs)
- [SCA as a Foundation for SSCS](#sca-as-a-foundation-for-sscs)
- [SBOMs: Stuck on the Starting Block?](#sboms-stuck-on-the-starting-block)
- [Beyond SBOMs: Building an Interdisciplinary SSCS Program](#beyond-sboms-building-an-interdisciplinary-sscs-program)
- [Allocating SSCS Responsibilities](#allocating-sscs-responsibilities)
- [Get Moving: The Next Steps in Your SSCS Journey](#get-moving-the-next-steps-in-your-sscs-journey)
- [Methodology](#methodology)

---

High-profile attacks affecting thousands of organizations have prompted stakeholders, ranging from national governments to corporate boards, to take a close look at the risk residing in the software supply chain. Attacks are frequent and malicious actors are weaponizing the open source components that make up a large percentage of applications.

While awareness is important, it is what organizations decide to do that will make the difference in managing software supply chain risk. To understand the current state of software supply chain security (SSCS) we surveyed 900 AppSec professionals in US, Europe and APAC based organizations across a wide range of industries.

The findings show an increased sense of awareness with more than half of respondents acknowledging that SSCS is a top or significant area of focus. However, only 7% have already purchased and implemented an SSCS-specific product.

Thanks to US Executive Order 14028, SBOMs have emerged as a common starting point for the SSCS journey. However, more than half of the organizations that request SBOMs from third parties say they are not using them effectively.

If SBOMs are the start, where should organizations focus next? Right now, there’s no clear or strong consensus. Most companies are doing something, but few are succeeding.

## Key Findings

- **Every organization has been victim of a software supply chain attack**: 100% of respondents said they were aware of a software supply chain attack against their organization at some point. Of these, 18% said they were attacked within the last year and 63% within two years.
- **Open source software is a big area of focus**: With much of the recent focus on SSCS being on vulnerabilities or malicious code in open source software, respondents estimated that, on average, about 56% of their applications contained open source software.
- **SSCS is a major area of concern**: With a significant percentage of their applications being open source, 75% of respondents said they were either very concerned (39%) or concerned (36%) about software supply chain security.
- **As a result, organizations are increasingly prioritizing SSCS**: 57% of respondents said that SSCS was a top or significant area of focus vs. other areas of security. 85% reported that they were actively using, purchasing, or planning to use a solution.
- **However, doing SSCS well remains a challenge**: Respondents reported big gaps between deploying a solution and using it effectively. 50% said they already request SBOMs from their software vendors, but less than half of those reported confidence that they knew how to use SBOMs effectively if needed.

## Everybody’s Talking About SSCS

The first step towards fixing a problem is knowing it exists, and there’s no question that awareness around SSCS has soared in recent years. The 2020 SolarWinds attack was a wake-up call demonstrating how a single breach in one organization could compromise thousands of customers and partners.

![Figure 01: What is your level of knowledge on software supply chain security? (SSCS)]

The urgency to act also comes from experience. As 18% of respondents report that they have experienced a SSCS attack in the past year, while 63% experienced one in the past two years.

![Figure 02: How much are you concerned about SSCS in your organization?]
![Figure 03: What is the primary reason you care about or are searching for SSCS?]

With awareness comes the realization that SSCS is also strategic. Various factors are prompting organizations to seek SSCS solutions, including board directives, compliance requirements, and competitive pressures. The most common reason for searching for SSCS solutions is “investigating additional risks beyond what we consider today”.

## SCA as a Foundation for SSCS

64% of organizations are already using or plan to use SCA tools.

Many organizations have a good foundation for building an SSCS program—even if they don’t know it—because they are using, or plan to use, software composition analysis (SCA) tools to identify open source vulnerabilities and license risks.

Attackers have weaponized open source libraries by injecting malicious code into frequently used packages that are subsequently built into applications. SCA vendors have responded to this threat by adding new checks and protections, such as:
- Checking the reputation of contributors to open source libraries
- Running code to identify malicious behavior
- Looking for instances of dependency confusion, typosquatting, chain and star-jacking.

## SBOMs: Stuck on the Starting Block?

If SCA represents the (often unknown) start to SSCS, the first conscious effort is typically focused on the Software Bill of Materials (SBOMs).

![Figure 04: If you are requesting SBOMs from your third-party software providers, how well do you think your organization uses them?]

While about half of all respondents say they are requesting SBOMs from third-party software vendors, more than half (53%) of those respondents say that they are not using them effectively.

![Figure 05: How much of your AppSec focus and resources are dedicated towards each step of the SDLC?]

Looking at how AppSec professionals allocate SSCS resources shows why this might be the case. The majority are allocating the most resources to the left of the SDLC, in the design and development stage. SBOMs are designed to come into their own when a zero-day vulnerability is released. This sits firmly in the “maintain” stage of the SDLC.

## Beyond SBOMs: Building an Interdisciplinary SSCS Program

SCA and SBOMs are common entry points to SSCS, but we know that organizations are ready to put a lot of effort into building it out further. An SBOM lists the ingredients of an application, but they don’t give insight into the process by which it was built.

> **Checkmarx Expert Insight:** Tzachi Zornstein, Head of Software Supply Chain at Checkmarx, explains: "In the case of the Ledger Connect Kit attack, the primary issue was not with the components themselves but with the compromised distribution process due to an account takeover... So, while SBOMs are vital for component transparency, they must be complemented with fast, proactive scanning mechanisms that can detect unauthorized changes or malicious activities in real-time."

## Allocating SSCS Responsibilities

![Figure 06: Which of the following SSCS technologies/approaches do you use or plan to use?]

Some of these approaches sit logically with particular teams. Establishing artifact repositories for trusted content and requesting SBOMs for third-party software, for example, are practical actions for developers to take.

![Figure 07: Who has the primary responsibility for SSCS in your organization?]

Our research shows that no single department has full responsibility for SSCS, and we’d argue that is just how it should be. It needs to be a shared, interdisciplinary process with good awareness among all stakeholders.

## Get Moving: The Next Steps in Your SSCS Journey

The interdisciplinary nature of SSCS means there are several steps you can take concurrently across different areas.

### Evolving AppSec To Support SSCS
The AppSec market has matured significantly in recent years, meaning organizations can now consolidate multiple siloed point solutions into integrated platforms that deliver clear visibility over the organization’s application security posture.

### Build on Your SCA Investment
- **Expand existing SCA coverage**: Check whether the SCA tool can identify malicious code inserted into OSS, not just vulnerabilities.
- **Integrate SBOMs into SCA**: SBOM generation should be part of your SCA tool, and you should be generating an SBOM with every version of software you produce.
- **Explore a platform approach**: Consolidating AppSec capabilities such as SAST and SCA on a single platform allows you to correlate findings from different tools.
- **Look right**: When choosing an AppSec platform look for features that support security on the right side of the SDLC, such as container security and IaC security.

## Methodology

To get more insight into current trends in software supply chain security, we commissioned a survey of 900 CISOs and application security professionals. The survey was conducted online by Global Surveyz Research. Respondents included a mix of CISOs, Deputy CISOs, VPs, Directors, and application security managers from companies in North America, W. Europe, and APAC with an annual revenue of $750M+, across a variety of industries.