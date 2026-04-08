## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Takeaways](#key-takeaways)
- [Email Security Among the Nikkei 225](#email-security-among-the-nikkei-225)
  - [Results](#results)
  - [By Industry](#by-industry)
  - [CISO Takeaways](#ciso-takeaways)
- [Web Service Security Among the Nikkei 225](#web-service-security-among-the-nikkei-225)
  - [HTTPS Support](#https-support)
  - [HSTS Adoption](#hsts-adoption)
  - [Summary](#summary)
  - [CISO Takeaways](#ciso-takeaways-1)
- [Version Complexity Among the Nikkei 225](#version-complexity-among-the-nikkei-225)
  - [Version Dispersion Among Web Servers](#version-dispersion-among-web-servers)
  - [Version Dispersion: Focus on Microsoft Exchange](#version-dispersion-focus-on-microsoft-exchange)
  - [CISO Takeaways](#ciso-takeaways-2)
- [High-Risk Services Among the Nikkei 225](#high-risk-services-among-the-nikkei-225)
  - [Findings: RDP, SMB, and Telnet](#findings-rdp-smb-and-telnet)
  - [Windows Remote Desktop Protocol (RDP)](#windows-remote-desktop-protocol-rdp)
  - [Windows Server Message Block (SMB)](#windows-server-message-block-smb)
  - [Telnet](#telnet)
  - [Exposure Overview](#exposure-overview)
  - [CISO Takeaways](#ciso-takeaways-3)
- [Vulnerability Disclosure Programs Among the Nikkei 225](#vulnerability-disclosure-programs-among-the-nikkei-225)
  - [Results: Prevalence of VDP Adoption](#results-prevalence-of-vdp-adoption)
  - [CISO Takeaways](#ciso-takeaways-4)
- [Conclusion](#conclusion)
- [CISO Actions at a Glance](#ciso-actions-at-a-glance)
- [Appendix: Prioritization in Times of Crisis](#appendix-prioritization-in-times-of-crisis)

---

# Executive Summary

As the world’s knowledge workers were driven home amid a pandemic and cases of ransomware ran rampant across the internet, measuring the world’s most critical businesses’ internet exposure has become more important than ever. In this round of Internet Cyber-Exposure Reports (ICERs), researchers at Rapid7 evaluate 5 areas of cybersecurity that are both critical to secure to continue doing business on and across the internet, and are squarely in the power of CISOs, their IT security staffs, and their internal business partners to address.

These five facets of internet-facing cyber-exposure and risk include:

1. Authenticated email origination and handling (DMARC)
2. Encryption standards for public web applications (HTTPS & HSTS)
3. Version management for web servers and email servers (focusing on IIS, nginx, Apache, and Exchange)
4. Risky protocols unsuitable for the internet (RDP, SMB, and Telnet)
5. The proliferation of vulnerability disclosure programs (VDPs)

In this report, we examine the internet-facing cyber-exposure of the top companies listed on Japan’s Nikkei 225[^1]. Each section is accompanied by real-world, practical advice that practitioners can start implementing today.

[^1]: https://indexes.nikkei.co.jp/en/nkave/index?type=index

---

# Key Takeaways

- **Nikkei 225 email security posture is lagging behind the US and UK.** At the beginning of 2021, email security among the Nikkei 225 isn’t keeping pace with its peers in the US and UK. While DMARC adoption in the US and UK hovers around 50%, only about 13% of all the surveyed companies operating in Japan have any DMARC records configured, and of those, 25 out of 29 (about 86%) are set with a p=none (or passthrough) policy.
- **Exposed, dangerous services are less of a concern in Japan.** While dangerous protocol exposures of Windows Remote Desktop (RDP) file-sharing (SMB), and Telnet continue to be an issue across the surveyed companies, it does not appear to be nearly as much of a problem as we’ve seen among the U.S.-based Fortune 500: For RDP and SMB, over 90% of the Nikkei 225 had no exposure.
- **Telnet and HSTS remain concerning, however.** Telnet is a different story; about 27% of the Nikkei 225 has some legacy telnet exposed to the internet. Additionally, when we looked at secure HTTP (HTTPS) deployment, we found that while HTTPS is standard for 100% of the Nikkei 225 companies, very few listed companies (18%) have implemented HSTS directives.
- **Version dispersion is on the right track in Japan.** Only 16 companies in the Nikkei are running their own Exchange servers, and of these, about 75% are running at least 1 instance of the latest supported version. That said, we did count 93 distinct versions of Apache, 75 distinct versions of Nginx, and 17 distinct versions of IIS in the Nikkei 225.
- **The Japanese Technology sector stands alone in vulnerability disclosure.** Nearly all of the 16 VDPs we found across the 225 surveyed companies are either in the Technology sector proper, or in tech-heavy Consumer Goods companies.

---

# Email Security Among the Nikkei 225

![Chart showing 2020 Nikkei DMARC Coverage: 196 (87%) No Valid Policy, 29 (13%) Valid]

## Results
We found that 29 (or approximately 13%) of the Nikkei 225 set of organizations had implementations of DMARC for their primary domains.

## By Industry
![Chart showing DMARC policies by sector: Technology, Materials, Capital Goods, Consumer Goods, Financials, Transportation and Utilities]

## CISO Takeaways
If DMARC has not already been implemented in your organization, take proactive measures to get it set up. It is a foundational fixture of email hygiene.

---

# Web Service Security Among the Nikkei 225

## HTTPS Support
Among the sites we examined in the Nikkei 225, 100% of them supported HTTPS.

## HSTS Adoption
![Chart showing HSTS Policy: 81.78% No HSTS Policy, 12.44% HSTS Enabled, 2.67% HSTS Enabled & Include Subdomains, 2.22% HSTS Enabled & Preload & Include Subdomains, 0.89% HSTS Enabled & Preload]

## Summary
Securing and encrypting traffic to your user-facing domains is not only good practice, but it also protects your corporate brand.

## CISO Takeaways
If your company’s website is not supporting HSTS, it might be worthwhile to find out why. Is it a technical, organizational, or budgetary constraint?

---

# Version Complexity Among the Nikkei 225

## Version Dispersion Among Web Servers
There are at least more than 93 distinct versions of Apache, 75 distinct versions of Nginx, and 17 versions of IIS running across the entire set of Nikkei 225 members.

![Chart showing Web Server Version Dispersion in 2021 Nikkei 225 Members]

## Version Dispersion: Focus on Microsoft Exchange
Only 6% of Nikkei 225 organizations still have at least 1 internet-facing Exchange server handling business-critical email.

![Chart showing Exchange Server Age/Up-to-Date Status]

## CISO Takeaways
Organizations deploy services to meet a business need, and it is far easier to sustain service uptime and stability if there are fewer moving parts to maintain.

---

# High-Risk Services Among the Nikkei 225

## Findings: RDP, SMB, and Telnet
Any non-zero number of these services made available to the general internet is considered to be unacceptable in organizations with mature security programs.

## Windows Remote Desktop Protocol (RDP)
On the default RDP port of 3389/tcp, we observed 89 services across 18 companies.

## Windows Server Message Block (SMB)
We observed 146 servers across 17 organizations on port 445/tcp. All servers supported SMBv1, which means they are missing several critical security controls.

## Telnet
Our survey found 243 hosts across 62 companies.

## Exposure Overview
![Heatmap of High-Risk Exposure by Industry]

## CISO Takeaways
Develop and maintain an inventory of internet-facing hosts that includes software versions, roles, and services that are expected to be exposed.

---

# Vulnerability Disclosure Programs Among the Nikkei 225

## Results: Prevalence of VDP Adoption
Only 16 of the exchange-listed companies (or about 7%) have a discoverable VDP.

![Chart showing VDP Status by Industry: Technology and Consumer Goods are the only sectors with VDPs]

## CISO Takeaways
Launching and running a successful VDP may be tricky—after all, the presence of a VDP implies a level of security maturity that may not yet exist at a given company.

---

# Conclusion
The Nikkei 225 organizations show a mixed bag of security maturity. While they excel in basic HTTPS adoption, they lag significantly in DMARC implementation, HSTS adoption, and the establishment of formal Vulnerability Disclosure Programs.

---

# CISO Actions at a Glance
1. **Implement DMARC**: Move toward a `p=reject` policy to protect brand reputation.
2. **Enable HSTS**: Ensure all web traffic is forced over encrypted channels.
3. **Reduce Version Dispersion**: Standardize web server versions to simplify patching.
4. **Eliminate High-Risk Services**: Remove RDP, SMB, and Telnet from the public internet.
5. **Launch a VDP**: Establish a clear channel for security researchers to report vulnerabilities.

---

# Appendix: Prioritization in Times of Crisis
If your organization is currently dealing with active incident response or crisis management, focus on the "low-hanging fruit" first:
- Ensure critical infrastructure (Exchange, VPNs) is patched against known, exploited vulnerabilities.
- Block all unauthorized access to management ports (RDP, Telnet, SMB) via firewall rules.
- Monitor for unauthorized email spoofing using basic DMARC reporting.

---

tep approach to establishing a minimal VDP is a contact and policy document placed at

<hxxps://your-company.com/.well-known/security.txt>. This is a relatively new standard for VDP communication

that provides for basic contact information signalling, readable by both humans and machines.46

44 https://www.iso.org/standard/72311.html
45 https://www.iso.org/standard/69725.html
46 Interested CISOs can read up on it at https://securitytxt.org/

Industry Cyber-Exposure Report (ICER): Nikei 225 34

Conclusion

The global COVID-19 pandemic forced many of these companies to abruptly shift to a large work-from-home

workforce in short order, and each company is its own miracle of corporate survival in the face of such drastic

and unprecedented changes to the workplace. In addition, Japanese companies are doing pretty well in stamp-

ing out dangerously exposed services and version dispersion when compared to other regions surveyed by

Rapid7.

However, these companies are lagging their international counterparts in the 3 other areas we measured for

this report: adoption of DMARC, HSTS, and VDPs. More progress must be made, and faster. Because of their

outsized position in the Japanese business community, they also tend to have access to the best and brightest

cybersecurity experts from around the world, and so it is incumbent upon them to behave more like model inter-

net citizens. The researchers at Rapid7 who contributed to this report sincerely hope these companies—and the

organizations that have business relationships with them—find this information and advice useful in our shared

responsibility of advancing security for everyone.

CISO at a Glance

Throughout this report, we’ve kept our focus on what CISOs in the Nikkei 225 can do, today, to reduce their ex-

posure to the most common issues we’ve discussed here. For the reader’s convenience, those recommendations

are summarised here.

Email Security: If you’re on the Domain-based Message Authentication, Reporting & Conformance (DMARC)

path, like 13% of the Nikkei 225, that’s great! Now is the time to plan out how you’ll move from a p=none to a

p=quarantine policy, and ultimately a p=reject policy. This is not an easy journey, since you will certainly uncover

pockets of shadow IT running their own email infrastructure, but the confidence of being able to authenticate

mail from your major brand domains is a pretty great feeling, and a nice item to report to your board of direc-

tors.

Web Security: HTTP Strict Transport Security (HSTS) is rapidly becoming table stakes for running a reasonably

secure website, and this is the kind of security feature that browser manufacturers like Google, Apple, Microsoft,

and Mozilla are likely to enforce in future versions of Chrome, Safari, Edge, and Firefox. It’s a relatively easy

switch that CISOs can flick (compared to the universe of nice-to-haves in cybersecurity, anyway), so take some

time to investigate whether your organisation is using HSTS and if not, why not?

Version Dispersion: For the mega-corporations that roam the fields of capitalism, mergers and acquisitions

are a fairly common activity throughout the year. That means the Nikkei 225 CISO is never truly “done” with

ensuring version consistency across the enterprise, even after investing in an excellent asset and vulnerability

management toolchain. New networks and network services will join your ranks, and that means undertaking a

fairly continuous modernization and normalization effort for those new assets. Taking on this continuous effort

will pay off in easier, more straightforward planning for the next patch cycle, scheduled or surprise.

Industry Cyber-Exposure Report (ICER): Nikei 225 36

High-Risk Services: Telnet, SMB, and RDP have no business being exposed directly to the world at large, and

are just waiting for the next self-replicating cyberattack to sweep across the internet. An up-to-date inventory of

exposed services, sourced from internal and external scanning, is worth its virtual weight in Bitcoin, and will help

you enforce a no-nonsense policy of network service exposure to the internet. As stated above, though, there

are very few of these exposed services left in the Nikkei 225 as of 2021.

Vulnerability Disclosure Programs: As a CISO, you might have hired the best of the best software, QA, and

platform engineers. But, without a good way to harness the smarts of the tens of thousands of talented hackers

around the world, you may never learn about the most critical vulnerabilities in your products and services. A

VDP is a bridge to that enormous community of well-meaning investigators who have goals aligned with your

own: a safer and more secure internet. Getting that program spun up now will give you plenty of time to prac-

tice safer software production. As a bonus, most of the pioneering work is already done for you, in the form of

ISO 29147 and ISO 30111.

Industry Cyber-Exposure Report (ICER): Nikei 225 37

Appendix: Prioritization
in Times of Crisis

The disclosure of both the SolarWinds-related multiple-technology vulnerabilities (and associ-

ated campaigns), the release of the out-of-band Microsoft Exchange patches responding to ac-

tive exploitation campaigns, and the Codecov compromise that will undoubtedly impact many,

many software development CI/CD processes, have all strained virtually every single informa-

tion-security team in every industry. We wanted to take a moment to help ensure you’re on

safer ground now, and also put each section into context, relative to some of the crises we’ve

had to deal with this year.

The SolarWinds and Codecov situation brought third-party risk square into focus like it has nev-

er been before. If you had a solid list of partners/vendors and a well-oiled contact plan (which

many organizations did), you may have weathered that portion of these extended incidents

fairly well. If not, we hope you had the support required to put such things in place and have

been able to use it in some subsequent serious vulnerability disclosures and exploit campaigns

since.

When it comes to being able to get a feel for how well a partner/vendor values safety and

resilience, you may want to heed the advice in the “CISO Takeaway” section. It’s much easi-

er to sleep at night knowing that the bulk of your third-party contacts prioritize email safety,

avoid exposing dangerous services to the internet, and stay current with both patching and

advanced encryption standards. You will also know how to contact them in the event you do

discover a security issue with any of their products and services, since they’ll have a vulnerabili-

ty-disclosure program in place.

Similarly, the massive Exchange vulnerability and associated malicious campaigns further

demonstrated how quickly 1 weakness in a component used by hundreds of thousands of

organisations can come out of the blue to disrupt execution on even the most well-crafted en-

terprise information-security roadmap. Having current, accurate telemetry of what is deployed

internally and externally, along with highly agile quality assurance and change management

processes (as noted in the section on version complexity), can be the difference in having an

unexpected patch (like Exchange) be a quick exercise with a slight bit of triage (to ensure at-

tackers did not have time to target you) versus an “all hands on deck” massive incident.

We hope our quantification, context, and advice prove useful as you emerge from these 2

major incidents to take on the remaining challenges that await us all in 2021 and beyond.