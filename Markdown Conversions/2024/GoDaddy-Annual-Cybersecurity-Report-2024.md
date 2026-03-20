# GoDaddy Annual Cybersecurity Report: 2024 Website Malware Threat Landscape

## Table of Contents
- [Summary](#summary)
- [Key statistics](#key-statistics)
- [Methodology](#methodology)
- [Emerging patterns and trends](#emerging-patterns-and-trends)
- [Website infection analysis](#website-infection-analysis)
- [Malware](#malware)
- [SEO spam](#seo-spam)
- [Credit card stealers](#credit-card-stealers)
- [Defacements](#defacements)
- [External malware distribution networks](#external-malware-distribution-networks)
- [Credits](#credits)

## Summary

In 2024, GoDaddy InfoSec researchers monitored and analyzed website security threats using Sucuri SiteCheck’s remote scanning technology, which processed over 70 million website scans across all hosting providers globally. This analysis provides insights into attack patterns and malware campaigns affecting websites worldwide.

The GoDaddy InfoSec malware research team helps protect the broader web ecosystem through automated continuous threat monitoring and detailed analysis, benefiting both our customers and the wider internet community. Our researchers develop and maintain sophisticated detection signatures by analyzing new malware samples, tracking emerging campaigns, and reverse engineering attack methodologies. This proactive approach helps us to identify and block new threats before they can impact our customers. Through collaboration between our malware research and threat intelligence teams along with analysis of malware samples and attack patterns, our security researchers documented sophisticated traffic distribution systems, social engineering tactics, and new methods of malware delivery and persistence.

Analysis of 1.1 million infected websites revealed that malware and malicious redirects dominated the threat landscape, accounting for 74.7% of detected infections. Our researchers saw an increasing number of threat actors using social engineering tactics like fake browser updates and captchas to lure website visitors into installing malware. Additionally, we saw major campaigns including Balada Injector (149,351 detections) and Sign1 (96,084 detections) leveraging traffic distribution systems to monetize compromised website traffic while employing sophisticated visitor profiling to avoid detection.

The abuse of legitimate WordPress plugins and themes continued to be a significant trend, with campaigns storing malicious code in database options rather than files to evade traditional security controls. This technique was particularly evident in the DNS TXT Records campaign, which utilized WPCode to execute malicious PHP code while maintaining persistence through automated reactivation systems. Additionally, the increase in compromises through stolen administrative credentials highlighted the growing connection between endpoint security and website security.

SEO spam techniques continued to evolve, affecting 422,741 websites globally through various methods. Japanese spam (117,393 detections) and gambling-related content (79,817 detections) represented the most prevalent spam categories, employing advanced cloaking techniques and geo-targeting capabilities to maintain effectiveness while avoiding detection.

## Key statistics

- 70.8 million global website scans
- 1,176,701 infected websites detected with various forms of malicious code and unauthorized modifications
- 822,651 detections of malware infections and malicious redirects targeting website visitors
- 422,741 detections of websites compromised with various forms of SEO spam
- 18,622 detections of credit card stealing malware
- 16,474 detections of unwanted advertisements
- 169,163 websites loading resources from domains associated with known malware campaigns

_Note: Compromised websites are often infected with one or more of the above categories._

## Methodology

### Data collection and analysis methodology

- **Scan coverage**: 70.8M scans performed
- **Period**: January 1 - December 31, 2024
- **Geographic distribution**: Global
- **Platform coverage**: All major CMS platforms

This report analyzes data collected through 70.8 million public remote website scans conducted throughout 2024 via Sucuri SiteCheck. Users can request to scan any site by submitting a URL to the tool; therefore, data is not limited to sites that belong to any specific CMS, platform, hosting provider, or country.

The SiteCheck service employs remote scanning technology to analyze websites for security threats and malicious behavior. The scanner operates at the browser level, examining websites as a typical user would experience them.

This approach allows for:
- Analysis of client-side source code
- Detection of malicious JavaScript injections
- Identification of unauthorized redirects
- Recognition of defacements and visual modifications
- Verification of security headers and configurations

Detection signatures are developed and maintained by GoDaddy InfoSec researchers who regularly analyze new threats and malware campaigns. These signatures enable the identification of specific indicators of compromise across various malware families.

### Detection statistics

We broke down these global detection results into five distinct malware families:

1. Malware and redirects (74.7% of infections)
2. SEO Spam (38.4% of infections)
3. Credit card stealers (1.7% of infections)
4. Unwanted ads (1.5% of infections)
5. Defacements (0.8% of infections)

The overall infection rate across scanned websites was 1.66%, with malicious code and redirects representing the most common form of compromise.

## Emerging patterns and trends

### Traffic Distribution Systems
In 2024, traffic brokers like VexTrio were central hubs for malicious redirects. Major campaigns including Balada Injector, Sign1, and DNS TXT redirects routed compromised website traffic through these systems to scam operations. The malicious TDS systems help monetize any visitor regardless of their location, web browser and operating system and at the same time filter out traffic from various bots and security researchers.

### Social engineering
Malware campaigns increasingly relied on social engineering tactics to compromise website visitors. Operators for massive campaigns like SocGholish, ClearFake/ClickFix created convincing fake browser update notifications, CAPTCHA challenges, and system repair prompts to deceive users. These tactics proved particularly effective when combined with visitor profiling and geo-targeting, allowing attackers to serve customized lures to specific audiences while avoiding security researchers.

### WordPress plugin abuse
Attackers increasingly leveraged legitimate WordPress plugins for malware persistence. DNS TXT Redirects, DollyWay, and Sign1 campaigns utilized plugins like WPCode and WordPress widgets to execute malicious PHP code and inject JavaScript malware. This approach stores malicious code in WordPress databases instead of files, circumventing traditional file-based security controls.

### Administrative credential theft
Website compromises through stolen credentials increased as information-stealing malware targeted WordPress and hosting control panel access. Threat actors acquired and monetized these credentials through underground markets, establishing a cycle of system and website compromises.

### Magento platform targeting
The CosmicSting vulnerability (CVE-2024-34102) led to widespread compromise of Magento e-commerce platforms. Multiple threat actors exploited this vulnerability to compromise thousands of online stores, resulting in credit card theft and malware distribution.

### Cryptocurrency targeting
Q1 2024 saw the emergence of crypto-drainer infections designed to compromise cryptocurrency wallets. While these attacks didn't achieve widespread adoption, they represent continued exploration of new monetization methods by threat actors.

### SEO spam
Two primary SEO spam categories dominated in 2024:
- Japanese spam campaigns creating extensive networks of doorway pages
- Gambling-related content targeting both English-speaking and South-East Asian markets through geo-specific delivery systems

## Website infection analysis

In 2024, we used results from the SiteCheck remote scanner to categorize website infections across five distinct malware families. Each family represents different attacker tactics and objectives, from malicious redirects to search engine manipulation.

## Malware

Primary category encompassing malicious code injections and organized campaigns. During 2024, SiteCheck detected 822,651 websites across the internet infected with various forms of malware.

### Balada Injector
The Balada Injector campaign was one of the most prevalent threats in 2024, with 149,351 detected infections. This campaign is known to inject obfuscated JavaScript code that redirects visitors to various scam sites through a chain of traffic direction systems (TDS).

![Example of a Balada script injection found on a compromised website.]

**Key characteristics of Balada infections include:**
- Strategic injection points in database options, theme files and common JavaScript files
- Multiple layers of code obfuscation
- Installation of disguised backdoor plugins for persistence
- Complex domain infrastructure with recognizable naming patterns
- Advanced admin detection for privilege escalation

### SocGholish
Commonly referred to as “fake browser updates”, SocGholish represents one of the more dangerous threats detected in 2024, with 147,332 infections. This malware is responsible for redirecting site visitors to malicious pages designed to trick victims into installing fake browser updates.

![Example of a fake Chrome update served by SocGholish malware.]
![Example of SocGholish malware seen on infected websites in 2024.]
![Variations of SocGholish-related injections that use Keitaro TDS.]

**SocGholish infection indicators include:**
- Browser-specific update notifications
- Multi-stage infection chain delivering RATs
- Systematic modification of JavaScript files and custom PHP proxy files
- Installation of fake WordPress plugins
- Advanced visitor fingerprinting

### Sign1
The Sign1 malware campaign emerged as a major threat in 2024, with 96,084 detected infections. This campaign specifically targets WordPress environments, exploiting legitimate plugins that allow custom code insertion.

![Example of a Sign1 malware injection found on an infected WordPress website.]

**Key characteristics of Sign1 infections include:**
- Advanced traffic filtering based on referrer headers
- Time-based URLs that expire within 10-minute windows
- Multiple layers of code obfuscation including XOR encoding
- Deep integration with VexTrio's traffic distribution system
- Use of legitimate WordPress plugins to inject malicious code

### Bogus URL shorteners
The Bogus URL Shortener campaign, detected on 35,758 websites, leverages links resembling URL shortening services to redirect website visitors to low-quality question and answer sites monetized through Google Adsense.

![Example of bogus URL shortener malware found on an infected website.]

**Indicators of compromise include:**
- Sophisticated traffic filtering targeting mobile devices
- Complex redirect chains
- Continuous rotation of shortener domains
- Hybrid injection techniques

### Uncategorized VexTrio redirects
In 2024 SiteCheck found generic uncategorized redirects to VexTrio URLs on 30,191 websites. VexTrio operates a complex network of redirect chains designed to funnel visitors through various scam operations.

### DNS TXT Records
The DNS TXT Records malware campaign, detected on 24,936 websites, stores malicious redirect URLs within DNS TXT records of attacker-controlled domains.

![Typical redirect destination to a DNS TXT Record scam notification.]

**Key technical characteristics include:**
- Sophisticated DNS TXT record query system
- Evolution from client-side JavaScript to stealthier server-side PHP
- Implementation of persistent backdoors using cookie-based authentication
- Advanced plugin concealment techniques

### Web3 crypto drainers
SiteCheck detected Web3 Crypto Drainer malware on 23,372 infected websites. The malware employs phishing tactics, using misleading popups to trick visitors into connecting their cryptocurrency wallets to the compromised site.

![Example of a known Web3 crypto-drainer popup.]
![Example of crypto-draining malware found on a compromised website.]

### Web shells
16,978 scans resulted in detection of public web interfaces of known web shells, which are used by bad actors to control and manipulate compromised environments.

![Example of a web shell interface.]

## SEO spam

SEO spam infections affected 422,741 websites in 2024.

### Hidden content
Hidden content SEO spam, detected on 114,318 websites, exploits the difference between how search engines and human visitors interpret web content.

![Example of hidden content SEO spam.]

### Japanese SEO Spam
Japanese SEO spam continues to be a pervasive threat, with 117,393 detections. This campaign specializes in creating massive networks of doorway pages written in Japanese.

![Examples of typical titles found on Japanese spam pages.]
![Typical search results of a site hacked with Japanese spam.]

### Gambling SEO spam
Gambling SEO spam continues to be a dominant threat in 2024, with 79,817 detected infections.

![Example of a gambling SEO spam infection.]
![Example of gambling SEO spam infection.]

## Credit card stealers

Client-side credit card skimming malware, also known as MageCart, affected 18,622 websites. These attacks specifically target e-commerce platforms, with a particular focus on WooCommerce and Magento installations.

## Defacements

While representing a smaller portion of total infections with 8,452 affected websites, defacements often create immediate and visible impact on compromised sites.

## External malware distribution networks

In 2024, SiteCheck identified 169,163 websites across the internet loading resources from 575 known malicious domains.

| Campaign | Percentage |
| :--- | :--- |
| SocGholish | 38.95% |
| Mal.Metrica | 14.67% |
| Other | 13.80% |
| Unwanted Ads | 13.27% |
| Balada Injector | 9.11% |
| Drainer | 5.48% |
| Fake Updates | 4.72% |

## Credits

- Denis Sinegubko - Principal Security Engineer, Malware Research
- Rianna MacLeod - Technical Writer
- Rodrigo Escobar - Senior Manager, Malware Research
- Vineeth Surendra - Senior Director Security Operations, Hosting