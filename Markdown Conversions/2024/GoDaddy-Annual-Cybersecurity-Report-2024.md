# GoDaddy Annual Cybersecurity Report: 2024 Website Malware Threat Landscape

## Table of Contents
- [Summary](#summary)
- [Key statistics](#key-statistics)
- [Methodology](#methodology)
- [Detection statistics](#detection-statistics)
- [Emerging patterns and trends](#emerging-patterns-and-trends)
- [Website infection analysis](#website-infection-analysis)
- [Malware](#malware)
  - [Balada Injector](#balada-injector)
  - [SocGholish](#socgholish)
  - [Sign1](#sign1)
  - [Bogus URL shorteners](#bogus-url-shorteners)
  - [Uncategorized VexTrio redirects](#uncategorized-vextrio-redirects)
  - [DNS TXT Records](#dns-txt-records)
  - [Web3 crypto drainers](#web3-crypto-drainers)
  - [Web shells](#web-shells)
- [SEO spam](#seo-spam)
  - [Hidden content](#hidden-content)
  - [Japanese SEO Spam](#japanese-seo-spam)
  - [Gambling SEO spam](#gambling-seo-spam)
- [Credit card stealers](#credit-card-stealers)
- [Defacements](#defacements)
- [External malware distribution networks](#external-malware-distribution-networks)
- [Distribution by campaign](#distribution-by-campaign)
- [Top campaign networks](#top-campaign-networks)
  - [SocGholish](#socgholish-1)
  - [Balada Injector](#balada-injector-1)
  - [Mal.Metrica](#malmetrica)
- [Credits](#credits)

## Summary

In 2024, GoDaddy InfoSec researchers monitored and analyzed website security threats using Sucuri SiteCheck’s remote scanning technology, which processed over 70 million website scans across all hosting providers globally. This analysis provides insights into attack patterns and malware campaigns affecting websites worldwide.

The GoDaddy InfoSec malware research team helps protect the broader web ecosystem through automated continuous threat monitoring and detailed analysis, benefiting both our customers and the wider internet community. Our researchers develop and maintain sophisticated detection signatures by analyzing new malware samples, tracking emerging campaigns, and reverse engineering attack methodologies. This proactive approach helps us to identify and block new threats before they can impact our customers. Through collaboration between our malware research and threat intelligence teams along with analysis of malware samples and attack patterns, our security researchers documented sophisticated traffic distribution systems, social engineering tactics, and new methods of malware delivery and persistence.

Analysis of 1.1 million infected websites revealed that malware and malicious redirects dominated the threat landscape, accounting for 74.7% of detected infections. Our researchers saw an increasing number of threat actors using social engineering tactics like fake browser updates and captchas to lure website visitors into installing malware. Additionally, we saw major campaigns including Balada Injector (149,351 detections) and Sign1 (96,084 detections) leveraging traffic distribution systems to monetize compromised website traffic while employing sophisticated visitor profiling to avoid detection.

The abuse of legitimate WordPress plugins and themes continued to be a significant trend, with campaigns storing malicious code in database options rather than files to evade traditional security controls. This technique was particularly evident in the DNS TXT Records campaign, which utilized WPCode to execute malicious PHP code while maintaining persistence through automated reactivation systems. Additionally, the increase in compromises through stolen administrative credentials highlighted the growing connection between endpoint security and website security.

SEO spam techniques continued to evolve, affecting 422,741 websites globally through various methods. Japanese spam (117,393 detections) and gambling-related content (79,817 detections) represented the most prevalent spam categories, employing advanced cloaking techniques and geo-targeting capabilities to maintain effectiveness while avoiding detection.

## Key statistics

*   70.8 million global website scans
*   1,176,701 infected websites detected with various forms of malicious code and unauthorized modifications
*   822,651 detections of malware infections and malicious redirects targeting website visitors
*   422,741 detections of websites compromised with various forms of SEO spam
*   18,622 detections of credit card stealing malware
*   16,474 detections of unwanted advertisements
*   169,163 websites loading resources from domains associated with known malware campaigns

Note: Compromised websites are often infected with one or more of the above categories.

## Methodology

### Data collection and analysis methodology

**Scan coverage**:
*   70.8M scans performed
*   **Period**: January 1 - December 31, 2024
*   **Geographic distribution**: Global
*   **Platform coverage**: All major CMS platforms

This report analyzes data collected through 70.8 million public remote website scans conducted throughout 2024 via Sucuri SiteCheck. Users can request to scan any site by submitting a URL to the tool; therefore, data is not limited to sites that belong to any specific CMS, platform, hosting provider, or country.

The SiteCheck service employs remote scanning technology to analyze websites for security threats and malicious behavior. The scanner operates at the browser level, examining websites as a typical user would experience them.

This approach allows for:
*   Analysis of client-side source code
*   Detection of malicious JavaScript injections
*   Identification of unauthorized redirects
*   Recognition of defacements and visual modifications
*   Verification of security headers and configurations

Detection signatures are developed and maintained by GoDaddy InfoSec researchers who regularly analyze new threats and malware campaigns. These signatures enable the identification of specific indicators of compromise across various malware families.

## Detection statistics

We broke down these global detection results into five distinct malware families:

1.  Malware and redirects (74.7% of infections)
2.  SEO Spam (38.4% of infections)
3.  Credit card stealers (1.7% of infections)
4.  Unwanted ads (1.5% of infections)
5.  Defacements (0.8% of infections)

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
*   Japanese spam campaigns creating extensive networks of doorway pages
*   Gambling-related content targeting both English-speaking and South-East Asian markets through geo-specific delivery systems

## Website infection analysis

In 2024, we used results from the SiteCheck remote scanner to categorize website infections across five distinct malware families. Each family represents different attacker tactics and objectives, from malicious redirects to search engine manipulation.

Let's examine the characteristics and impact of each category.

### Malware

Primary category encompassing malicious code injections and organized campaigns.

During 2024, SiteCheck detected 822,651 websites across the internet infected with various forms of malware. The landscape was dominated by several sophisticated campaigns that demonstrated increasing complexity in their attack methodologies.

#### Balada Injector

The Balada Injector campaign was one of the most prevalent threats in 2024, with 149,351 detected infections on websites hosted by multiple providers. This established campaign is known to inject obfuscated JavaScript code that redirects visitors to various scam sites through a chain of traffic direction systems (TDS), starting with their own TDS and ending with third-party traffic brokers like VexTrio. The malware specifically targets WordPress installations, exploiting vulnerabilities in widely-used plugins.

The infection process follows a systematic approach to establish persistence. Initial compromise may begin with JavaScript injections using cross-site scripting vulnerabilities in WordPress themes and plugins and then proceeding with silently attacking logged in site administrators to add malicious users and counterfeit WordPress plugins that function as backdoors.

The campaign's infrastructure relies on a methodical domain management system. Operators maintain a network of domains constructed using three-word combinations in paired variations (e.g., "cleanreditems"/"cleanblueitems", "brownsisteroftime"/"greensisteroftime"). These domains, often protected behind CDN services, serve different stages of the attack chain and regularly rotate to avoid detection. The malware also employs advanced administration detection, modifying its behavior when it detects logged-in WordPress administrators to facilitate deeper compromise.

![Image description: Example of a Balada script injection found on a compromised website.]

**Key characteristics of Balada infections include:**
*   Strategic injection points in database options, theme files and common JavaScript files
*   Multiple layers of code obfuscation that use diverse techniques like obfuscator.io, random comments character code arrays, base64, etc.
*   Installation of disguised backdoor plugins for persistence
*   Complex domain infrastructure with recognizable naming patterns
*   Advanced admin detection for privilege escalation
*   Integration with push notification scams and traffic distribution systems

#### SocGholish

Commonly referred to as “fake browser updates”, SocGholish represents one of the more dangerous threats detected in 2024, with 147,332 infections identified across the internet. Active at least since 2017, this malware is responsible for redirecting site visitors to malicious pages designed to trick victims into installing fake browser updates. JavaScript is used to display notices in the victim's web browser and initiate a download for remote access trojans, allowing the attacker to gain full access and remotely control the victim's computer. Attackers are not just infecting websites, they are also leveraging the compromised environments to phish large corporations and employees. The campaign is particularly notorious for its role in ransomware distribution chains, often serving as the initial compromise vector for larger-scale attacks against corporate networks.

The malware typically operates in multiple stages, beginning with an initial JavaScript injection that evaluates visitor characteristics. If a visitor meets the campaign's targeting criteria, the malware presents a convincing browser update notification customized to match the user's actual browser type. This social engineering tactic has proven remarkably effective at convincing users to download and execute the malicious payload.

![Image description: Example of a fake Chrome update served by SocGholish malware.]

In 2024, we observed several distinct types of website infections that served SocGholish malware, with NDSW/NDSX (also known as Parrot TDS) remaining the most prevalent. This variant uses both obfuscated code injected into multiple (sometimes all) legitimate JavaScript files and malicious PHP files that serve as a custom PHP proxy system to dynamically obtain the most current SocGholish payload. Both JavaScript and PHP components of this malware feature signature markers such as ndsw, ndsj and ndsx (thus the name of the campaign). However, in April 2024 new variants emerged where the markers changed to zqxw, zqxq and qwzx.

![Image description: Example of SocGholish malware seen on infected websites in 2024.]

Another notable campaign served SocGholish to eligible visitors using fake WordPress plugins that injected script tags pointing to Keitaro TDS URLs on their own servers.

![Image description: Variations of SocGholish-related injections that use Keitaro TDS.]

**SocGholish infection indicators include:**
*   Browser-specific update notifications that match the visitor's exact browser type and language settings
*   Multi-stage infection chain delivering RATs through fake browser updates
*   Systematic modification of JavaScript files and custom PHP proxy files in the web environment with NDSW/NDSX variants
*   Installation of fake WordPress plugins and modification of themes’ function.php files for Keitaro variations
*   Advanced visitor fingerprinting to target specific user profiles while avoiding security researchers

#### Sign1

The Sign1 malware campaign emerged as a major threat in 2024, with 96,084 detected infections across the internet. This campaign specifically targets WordPress environments, exploiting legitimate plugins that allow custom code insertion, such as Simple Custom CSS and JS. Once established, Sign1 implements an intricate system of traffic filtering and dynamic payload delivery that effectively evades detection and removal.

A distinctive characteristic of Sign1 is its time-based URL generation and validation mechanism. The malware creates URLs containing hexadecimal timestamps that expire after 10 minutes. When visitors arrive from major platforms like Google or Facebook, the malware validates these timestamps before executing its payload. The execution typically triggers a series of redirects through intermediary domains, ultimately leading visitors to VexTrio scam infrastructure.

The campaign employs multiple evasion techniques, including XOR encoding and dynamic code generation. Rather than modifying server files, Sign1 infections store malicious code in WordPress databases utilizing functionality of legitimate plugins and custom HTML widgets. This approach circumvents standard cleanup procedures and bypasses file-based integrity monitoring systems, making the malware particularly challenging to identify and eliminate.

![Image description: Example of a Sign1 malware injection found on an infected WordPress website.]

**Key characteristics of Sign1 infections include:**
*   Advanced traffic filtering based on referrer headers from major platforms like Google and Facebook generated time-based URLs that expire within 10-minute windows
*   Multiple layers of code obfuscation including XOR encoding and dynamic JavaScript generation
*   Deep integration with VexTrio's traffic distribution system
*   Use of legitimate WordPress plugins to inject malicious code and store it in a database to evade file-based detection

#### Bogus URL shorteners

The Bogus URL Shortener campaign, detected on 35,758 websites across the internet in 2024, leverages links resembling URL shortening services to redirect website visitors to low-quality question and answer sites monetized through Google Adsense.

This campaign specifically targets mobile users, creating complex redirect chains that eventually lead to low-quality content farms monetized through aggressive advertising. The attackers have demonstrated remarkable adaptability, regularly introducing new domains and modification techniques to evade detection.

What makes this campaign particularly effective is its multi-faceted approach to code injection. Rather than relying on a single technique, attackers employ various methods ranging from highly obfuscated JavaScript to simple external script tags. In 2023, we observed the campaign expanding its scope to include cryptocurrency-related scams, with compromised sites redirecting mobile traffic to AI-generated blogs about cryptocurrency investments.

The campaign's infrastructure shows significant investment in evasion techniques. Attackers maintain a large network of disposable domains hidden behind DDos-Guard and CloudFlare services/proxies. In 2024, they continued registering bogus URL shortening domains including cuttlyco[.]asia, urlcuttly[.]net, and servme[.]observer.

![Image description: Example of bogus URL shortener malware found on an infected website.]

**Indicators of compromise include:**
*   Sophisticated traffic filtering targeting mobile devices through extensive user agent analysis
*   Complex redirect chains implementing multiple intermediate hops to avoid detection and blocking
*   Continuous rotation of shortener domains through automated infrastructure to maintain campaign resilience
*   Hybrid injection techniques combining both obvious and deeply obfuscated code to complicate removal

#### Uncategorized VexTrio redirects

In 2024 SiteCheck found generic uncategorized redirects to VexTrio URLs on 30,191 websites across the internet. Multiple malware campaigns use VexTrio for monetization. The most prominent of them (including Sign1, Balada Injector, and DollyWay) have their own distinct signatures. However, sometimes our SiteCheck scanner can only see generic patterns of VexTrio redirects. This often occurs when the main malicious functionality is hidden on the server side.

VexTrio operates a complex network of redirect chains designed to funnel visitors through various scam operations.

**Distinctive features include:**
*   Multi-layer traffic filtering system analyzing user agents, IP addresses, and browser characteristics
*   Redirects to various scam sites, including:
    *   Browser push notification scams (“Click allow if you are not a robot”)
    *   LosPollos dating and sweepstakes scams
    *   Tech support scams

#### DNS TXT Records

The DNS TXT Records malware campaign, detected on 24,936 websites across the internet in 2024, represents one of the most innovative approaches to traffic manipulation observed during the year. This campaign distinguishes itself by storing malicious redirect URLs within DNS TXT records of attacker-controlled domains, effectively creating a dynamic, hard-to-detect and block command and control infrastructure. The technique allows attackers to modify their redirect destinations without touching the compromised websites' files or making HTTP requests, making traditional detection methods less effective.

The campaign's evolution throughout 2024 demonstrated increasing complexity, particularly in its shift from client-side JavaScript injections to stealthier server-side PHP redirects in March. This transition significantly improved the malware's ability to evade detection while maintaining its effectiveness. The malware is injected as a WPCode PHP snippet, establishes multiple persistence mechanisms to maintain control even after initial discovery and removal attempts.

The technical implementation reveals careful attention to operational security. The malware employs various evasion techniques, including hiding plugin presence from WordPress admin panels, disguising administrative notifications, and implementing cookie-based backdoors. These backdoors serve multiple purposes, allowing attackers to update DNS tracking domains and create rogue administrator accounts at will. Perhaps most notably, the campaign maintains persistence through automated bot networks that actively monitor and reactivate disabled malicious plugins, making complete removal particularly challenging.

![Image description: Typical redirect destination to a DNS TXT Record scam notification.]

**Key technical characteristics include:**
*   Sophisticated DNS TXT record query system retrieving encrypted redirect URLs from attacker-controlled domains
*   Evolution from client-side JavaScript to stealthier server-side PHP implementations for redirect handling
*   Implementation of persistent backdoors using cookie-based authentication mechanisms
*   Advanced plugin concealment techniques preventing detection in WordPress administrative interfaces
*   Automated systems monitoring and reactivating disabled malicious components through bot networks

The campaign primarily leverages domains like tracker-cloud[.]com, ads-promo[.]com, logsmetrics[.]com, tracker-cloud[.]com, cloud-stats[.]com, airlogs[.]net, logs-web[.]com, dns-routing[.]net, cdn-routing[.]com, webdmonitor[.]io for its DNS TXT record infrastructure. Hosting providers are advised to sinkhole DNS queries for these domains and their subdomains to disrupt functionality of the malware.

#### Web3 crypto drainers

SiteCheck detected Web3 Crypto Drainer malware on 23,372 infected websites across the internet in 2024. This campaign represents a novel form of website malware targeting Web3 and cryptocurrency assets through crypto drainers injected onto compromised websites.

The malware employs phishing tactics, using misleading popups to trick visitors into connecting their cryptocurrency wallets to the compromised site. Once connected, the malware drains funds from the victim's wallet by signing unauthorized transactions that transfer assets to the attacker's wallet.

![Image description: Example of a known Web3 crypto-drainer popup.]

Historically, drainers have been used on phishing sites designed to attack people interested in cryptocurrencies. These phishing sites were promoted through social networks and instant messaging applications like Telegram.

In 2024, however, bad actors decided that cryptocurrency adoption had improved to a point that made it worthwhile to expose completely unsuspecting visitors of random compromised sites to Web3 scams. In Q1, we saw a number of infections redirecting website visitors to phishing sites containing crypto draining malware. Researchers also saw drainer scripts injected directly into compromised websites.

The most notable malware campaign that injected Angel Drainer scripts used the following URLs:
*   billlionair[.]app/cachingjs/turboturbo.js
*   dynamiclinks[.]cfd/cachingjs/turboturbo.js
*   dynamiclink[.]lol/cachingjs/turboturbo.js
*   dynamic-linx[.]com/chx.js

![Image description: Example of crypto-draining malware found on a compromised website.]

Detections for this malware peaked in February-March 2024 and then gradually died down. It’s likely that the efficacy of crypto drainer scams on compromised sites was significantly lower than those found on specialized phishing sites, so we suspect bad actors needed to wait for the next milestone in Web3 technology adoption.

**Characteristics of web3 crypto drainers include:**
*   Targets users of popular cryptocurrency wallets through convincing connection interfaces
*   Displays “Connect Wallet” pop-ups unrelated to site functionality.
*   Along with connecting the wallet, users are tricked to give permission to transfer all their digital assets to third-party wallets controlled by the drainer operators.

#### Web shells

16,978 scans resulted in detection of public web interfaces of known web shells, which are used by bad actors to control and manipulate compromised environments. Using web shells, attackers can perform unauthorized file operations, access and manipulate databases and execute shell commands.

![Image description: Example of a web shell interface.]

## SEO spam

Unauthorized content and link injections designed to manipulate search engine rankings and redirect valuable organic traffic

SEO spam infections affected 422,741 websites in 2024, representing a significant portion of all detected compromises. These attacks continue to evolve, employing various techniques to manipulate search engine rankings and redirect valuable organic traffic.

### Hidden content

Hidden content SEO spam, detected on 114,318 websites across the internet in 2024, represents a common black hat SEO technique used to conceal injected spam content (usually containing links to third-party sites) within legitimate web pages. This technique exploits the difference between how search engines and human visitors interpret web content, allowing attackers to inject spam while maintaining a seemingly legitimate appearance for regular users. The primary goal is to leverage the compromised site's domain authority to improve rankings for unauthorized content without alerting website owners to the compromise.

The technical implementation of hidden content spam shows remarkable ingenuity in exploiting web technologies. Attackers employ various CSS and JavaScript techniques to conceal spam content, with the most common method being the creation of div elements positioned far off-screen using large negative pixel values. Another prevalent technique involves creating containers with zero height or font size, effectively rendering the content invisible to humans while remaining indexable by search engines.

![Image description: Example of hidden content SEO spam.]

The persistence of hidden content spam is particularly problematic because it often survives routine cleanup attempts. Attackers frequently inject their code into legitimate template files, database entries, and even widget configurations, making complete removal challenging without comprehensive scanning tools. The spam content typically promotes high-value keywords related to pharmaceuticals, gambling, adult content, and counterfeit goods.

**Common techniques observed in 2024 include:**
*   CSS manipulation using extreme negative positioning values to shift content completely off-screen
*   Use of JavaScript to make spammy HTML blocks invisible to human visitors
*   Implementation of containers with close-to-zero dimensions and hidden overflow to conceal spam content while remaining indexable

### Japanese SEO Spam

Japanese SEO spam continues to be a pervasive threat, with 117,393 detections across the internet in 2024. This campaign specializes in creating massive networks of doorway pages written in Japanese. This spam campaign targets users from Japan who search for cheap counterfeit luxury goods, designer brands, and other merchandise.

Search engines index thousands of doorway pages created by attackers. However, when people click on such search results, instead of going to the compromised site, they are being redirected to obscure Chinese online stores that use disposable, constantly-changing domain names.

![Image description: Examples of typical titles found on Japanese spam pages.]

The sophistication of Japanese SEO spam lies in its approach to compromising websites. Attackers don't simply inject spam content; they implement complex systems to protect their injections and ensure persistence. A distinctive characteristic is the placement of .htaccess files throughout the compromised environment - often exceeding 300 files in a typical WordPress installation. These files serve a dual purpose: preventing the execution of competing attackers' backdoors while maintaining access for their own malicious code.

The impact of Japanese SEO spam extends beyond simple content injection. When a website is compromised, search results become polluted with Japanese keywords and spam content, severely affecting the site's legitimate search rankings. Website owners often remain unaware of the infection until they notice unusual traffic patterns or receive reports of strange search results. The spam content is frequently cloaked, appearing normal to regular visitors while serving different content to search engines, making manual detection even more challenging.

![Image description: Typical search results of a site hacked with Japanese spam.]

**Characteristics of Japanese SEO spam infections include:**
*   Thousands of unauthorized pages in Japanese poison compromised sites’ search results
*   Advanced cloaking mechanisms that serve Japanese-language doorway pages to search engines while maintaining normal site appearance for visitors
*   Redirection of Japanese search engine users to obscure online stores that sell Chinese replicas of luxury goods and other stuff that you can commonly find on sites like AliExpress/Alibaba
*   Server-side PHP scripts dynamically generate doorway pages obtaining their content from third-party servers
*   Strategic placement of modified .htaccess files throughout website directories to protect malicious code while blocking competitor access

### Gambling SEO spam

Gambling SEO spam continues to be a dominant threat in 2024, with 79,817 detected infections across the internet. This category of spam specifically targets the lucrative online gambling market, creating vast networks of doorway pages designed to capture search traffic for casino- and betting-related keywords. There are multiple threat actors involved in this black hat SEO activity, capitalizing on affiliate programs run by various gambling sites.

Gambling spam infections range from injection of links, creating overlays with casino/bookmaker ads to redirecting search traffic to sites that serve as anonymous proxies to bigger gambling sites. In addition to using compromised sites, gambling SEO campaigns are notorious for using thousands of recently expired domains with existing authority, leveraging their established trust to boost rankings for gambling content.

![Image description: Example of a gambling SEO spam infection.]

The technical implementation of gambling spam reveals an advanced understanding of search engine algorithms and regional regulations. Attackers frequently employ geo-targeting techniques to serve different content based on visitor location, particularly focusing on regions where online gambling faces strict regulation. This approach allows the spam network to maximize its effectiveness while minimizing detection by serving legitimate-looking content to visitors from regions where gambling is heavily monitored.

The persistence mechanisms employed by gambling spam operators demonstrate significant evolution in 2024. Rather than simple content injection, modern gambling spam frequently implements dynamic content generation systems that create region-specific landing pages on demand. These systems often integrate with legitimate CMS functionality, making them particularly difficult to identify and remove without disrupting the site's normal operation.

![Image description: Example of gambling SEO spam infection.]

**Characteristics of gambling spam infections include:**
*   Region-specific content delivery systems that adapt to local gambling regulations and language preferences
*   Automated generation of doorway pages optimized for gambling-related keywords and local betting terms
*   Strategic acquisition and exploitation of expired domains with established authority
*   Dynamic content translation systems serving region-specific gambling content in appropriate languages
*   Advanced cloaking techniques that evade detection by displaying legitimate content to security scanners

## Credit card stealers

Malicious code injected into e-commerce checkout processes to steal payment card data from site visitors.

Client-side credit card skimming malware, also known as MageCart, affected 18,622 websites across the internet in 2024. These attacks specifically target e-commerce platforms, with a particular focus on WooCommerce and Magento installations. The malware operates by injecting malicious code into checkout processes to harvest customer payment information in real-time.

Many of the detected skimmer injections in 2024 can be attributed to the Magento/Adobe Commerce CVE-2024-34102 vulnerability (aka CosmicSting).

**Key characteristics of credit card skimming infections include:**
*   Integration with multiple e-commerce platforms
*   Advanced data exfiltration through encrypted channels
*   Masquerading techniques mimicking legitimate analytics services
*   Creation of exact payment form replicas to avoid detection

## Defacements

Visual modifications to websites, often including unauthorized content changes and fake update notifications

While representing a smaller portion of total infections with 8,452 affected websites across the internet, defacements often create immediate and visible impact on compromised sites. Unlike more stealthy forms of compromise, defacements are designed to be noticed, either to make political statements or simply to demonstrate the attacker's ability to compromise the site.

### Visual modifications

The majority of defacement detections (7,513) involved direct modifications to website content, replacing legitimate pages with unauthorized messages or imagery. While the majority of defaced websites are regular sites, we often hear about these attacks when hacktivists target high-profile or government websites to maximize their impact and visibility. These attacks frequently serve as a distraction from more serious compromises occurring simultaneously.

## External malware distribution networks

Website compromises often involve loading malicious code from external servers through injected script tags or iframes. GoDaddy InfoSec researchers maintain a comprehensive blocklist of these malicious domains and URLs. In 2024, SiteCheck identified 169,163 websites across the internet loading resources from 575 known malicious domains.

### Distribution by campaign

| Campaign          | Percentage |
| :---------------- | :--------- |
| SocGholish        | 38.95%     |
| Mal.Metrica       | 14.67%     |
| Other             | 13.80%     |
| Unwanted Ads      | 13.27%     |
| Balada Injector   | 9.11%      |
| Drainer           | 5.48%      |
| Fake Updates      | 4.72%      |

## Top campaign networks

Malware campaigns rely heavily on external infrastructure to deliver malicious payloads and maintain control over compromised websites. These domains often masquerade as legitimate services, using names that mimic content delivery networks, JavaScript libraries, or development resources. The most prevalent domains typically serve as malware distribution points for major campaigns, with some domains responsible for thousands of website infections.

### SocGholish

Certain website malware campaigns associated with SocGholish are known to avoid obfuscated injections. Instead, they use fake WordPress plugins to place script tags referencing external scripts on their own servers. In 2024 we detected such scripts from 77 different domains on over 65,000 sites across the internet.

The top five most commonly detected SocGholish-related domains include:
*   marvin-occentus[.]net (9,664 detections)
*   aitcaid[.]com (8,862 detections)
*   packedbrick[.]com (4,978 detections)
*   blacksaltys[.]com (3,824 detections)
*   frontendcodingtips[.]com (3,385 detections)

In addition to 77 domains related to SocGholish, we also detected 61 domains related to other campaigns that used similar social engineering tactics tricking site visitors into downloading and installing malware (mostly remote access trojans and infostealers) under pretext of updating their browser, solving a captcha, or fixing some non-existent problem.

### Balada Injector

The Balada Injector campaign operates through a sophisticated network of domains with distinctive naming patterns, often combining multiple English words to create legitimate-looking domain names.

In 2024, Balada Injector mainly used obfuscated malicious code, but we still detected over 15,000 sites across the internet with external script tags loading malware from 68 Balada own domains injected in 2023 and earlier. For example, the most detected Balada Injectors domain startperfectsolutions[.]com is related to massive infections that took place in November 2023.

The top five detections include:
*   startperfectsolutions[.]com (11,374 detections)
*   clickandanalytics[.]com (643 detections)
*   digestcolect[.]com (705 detections)
*   scriptsplatform[.]com (495 detections)
*   firstblackphase[.]com (89 detections)

### Mal.Metrica

This campaign is known to exploit cross site scripting vulnerabilities to inject external script tags, leveraged a network of domains masquerading as content delivery services. The tell-tale pattern of Mal.Metrica script URLs are the use of third-level subdomains and absence of the script paths — the domain's “home page” serves the malicious JavaScript instead of a conventional HTML page.

In 2024 we detected over 21,000 sites with injected Mal.Metrica scripts referencing 21 blocklisted domains.

The top five detections include:
*   cache.cloudswiftcdn[.]com (5,539 detections)
*   static.rapidglobalorbit[.]com (3,941 detections)
*   synd.edgecdnc[.]com (2,839 detections)
*   secure.gdcstatic[.]com (2,584 detections)
*   content.gorapidcdn[.]com (1,747 detections)

## Credits

*   Denis Sinegubko - Principal Security Engineer, Malware Research
*   Rianna MacLeod - Technical Writer
*   Rodrigo Escobar - Senior Manager, Malware Research
*   Vineeth Surendra - Senior Director Security Operations, Hosting