# The 2024 SpyCloud Malware and Ransomware Defense Report

## Table of Contents
- [Summary of Key Findings](#summary-of-key-findings)
- [Key Findings by Role and Industry](#key-findings-by-role-and-industry)
- [The Malware and Ransomware Resurgence](#the-malware-and-ransomware-resurgence)
- [Why We Do This Report](#why-we-do-this-report)
- [Survey Method: How We Collected Data for This Report](#survey-method-how-we-collected-data-for-this-report)
- [The Dark Beginnings of the Ransomware Journey](#the-dark-beginnings-of-the-ransomware-journey)
- [The Evolving Malware Landscape: Where Adversaries Gain Momentum](#the-evolving-malware-landscape-where-adversaries-gain-momentum)
  - [Stealthy Stealers at Play](#stealthy-stealers-at-play)
  - [Infostealer Infections Present in the 3 Months Prior to Reported Ransomware Attacks in 2024](#infostealer-infections-present-in-the-3-months-prior-to-reported-ransomware-attacks-in-2024)
  - [Top Infostealer Villains](#top-infostealer-villains)
  - [Battling Cyber Threats: Fighting for the Upper Hand](#battling-cyber-threats-fighting-for-the-upper-hand)
- [Malware Infection Remediation Practices: Far From a Critical Hit](#malware-infection-remediation-practices-far-from-a-critical-hit)
- [Risk from Third-Party Exposure: Adversaries’ Extra Advantage](#risk-from-third-party-exposure-adversaries-extra-advantage)
- [The Ransomware Landscape: Land of Infinite Gameplay](#the-ransomware-landscape-land-of-infinite-gameplay)
  - [Affected by Ransomware](#affected-by-ransomware)
  - [Top Industries Most Likely to Be Targeted by a Future Ransomware Attack in 2024](#top-industries-most-likely-to-be-targeted-by-a-future-ransomware-attack-in-2024)
  - [Data, Financial Knockouts](#data-financial-knockouts)
  - [Cracks in Your Cyber Defenses: Common Attack Entry Points](#cracks-in-your-cyber-defenses-common-attack-entry-points)
  - [Next-Gen Showdown: The Future of Ransomware Defense](#next-gen-showdown-the-future-of-ransomware-defense)
- [Into the Light: The Hero’s Journey](#into-the-light-the-heros-journey)
  - [Boosting Team Play](#boosting-team-play)
- [Reevaluating Priorities for the Battle Ahead](#reevaluating-priorities-for-the-battle-ahead)
- [Looking to the Horizon: How to Defeat Cybercriminals in the Long Game](#looking-to-the-horizon-how-to-defeat-cybercriminals-in-the-long-game)

---

PRESENTS

THE 2024
MALWARE AND
RANSOMWARE
DEFENSE REPORT

FROM THE COMPANY THAT BROUGHT YOU THE WORLD’S LARGEST COLLECTION IN COLLABORATION WITH

By the year 2024, the computer had become the central force of the workplace. Long gone were the days of the typewriter, filing cabinets, and notepads – and in their place, every office worker had become a machine of one, powered by their device, speeding through each eight-hour day on a keyboard and furiously clicking in the name of Productivity.

With the surge in global computer use came the creation of a new role within the modern organization – the security operations center (SOC). Given the difficult task of safeguarding the productive relationship between people and machines, the SOC quickly realized the daunting challenges they were up against. Rampant password reuse, burgeoning digital users, and the rise of crafty cybercriminals threatened their organizations at every turn.

And as the world and workplace continued to develop, the challenges only grew – from high-volume data leaks to stealthy infostealer malware, stolen session cookies, and profit-hungry ransomware gangs. The SOC gathered what tools they could find, and together with their fellow Defenders gave an admirable attempt at leveling the fight between themselves and the enemies that threatened Productivity – enemies that were shapeshifting and multiplying before their eyes.

Would it be enough?

## Summary of Key Findings

Every year, improving ransomware prevention capabilities is one of the top priorities for organizations in the immediate future. Even with focused efforts, the risk of the ransomware threat remains high – survey respondents rank ransomware as their biggest threat among eight categories.

The survey data validates security teams’ concerns, with 75% of organizations reporting being affected¹ by ransomware more than once in the past 12 months – a jump from 61% last year.

Nearly 100% of the surveyed organizations are concerned about the potential for identity, session cookie, and other data siphoned from malware-infected devices being used to enable follow-on attacks like ransomware. But some good news – respondents’ second biggest priority for the next 12-18 months is to improve visibility and remediation for compromised credentials and malware-exfiltrated data.

For organizations who reported being affected by ransomware in the past year, stolen cookies that enabled session hijacking ranked as the third most common entry point for ransomware attempts and successful attacks, following phishing/social engineering and third-party access.

More than half (57.5%) of teams report that they routinely invalidate or terminate open sessions for applications in response to a managed device getting infected with malware, which shows heightened awareness of the growing session hijacking problem.

Nearly all surveyed organizations are concerned about the risks from third-party accounts being compromised due to malware infections – and 82% are either extremely or significantly concerned. Additionally, participants rank third-party access as the second most common entry point for ransomware.

## Key Findings by Role and Industry

CIOs, CISOs, and other IT security executives are much more confident about their organization’s ability to prevent a full-blown ransomware attack – 91% of leaders are generally confident, compared to 54% of security operators, analysts, and incident responders, and 71% of access and identity management professionals. Likewise, leaders express much higher confidence in their organization’s malware and ransomware response capabilities. This difference in perception reflects a disconnect when it comes to shared understanding of an organization’s cybersecurity posture.

Identity and access management (IAM) directors, managers, and team leads are the cohort most concerned about exposure from malware-infected devices and compromised or infected third-party accounts. Case in point, 95% are extremely or significantly concerned about data siphoned from malware-infected devices being used for more harmful attacks, vs. 83% of security directors, managers, and team leads, and vs. 69% of analysts and incident responders. Additionally, IAM professionals are more concerned about risks to their organization from third-party accounts compromised by malware infections, and are also more likely to name stolen cookies as one of the riskiest ransomware entry points.

Survey respondents from each sector rank ransomware as the biggest threat to their organization. However, only three sectors – manufacturing, retail, and technology – rate improved ransomware prevention capabilities among their two main priorities in the next 12 to 18 months. Technology and manufacturing also express the highest concern for compromised third-party accounts. Interestingly, retail respondents rank their ability to identify business applications exposed by a malware infection as their organization’s top capability.

## The Malware and Ransomware Resurgence

After a brief decline in activity in late 2022, ransomware re-emerged with a vengeance over the last 18 months. Like a villain with endless lives, ransomware actors not only refused to give up, they’ve had an unprecedented run...

Ransomware payments soared past $1 billion in 2023 while the volume, frequency, scope of attacks, and number of new players spiked as well, ranging from solo actors and small groups to powerful syndicates with robust affiliate business models.

Collectively, these actors continuously wreaked havoc across sectors. In the past 12 months, they:

*   Disrupted the operations of thousands of automotive dealerships for days
*   Caused $100 million in financial losses to a major hotel and casino chain
*   Forced the ninth-largest US city to close court hearings and other services for weeks
*   Stole 6TB worth of data belonging to as many as one-third of American consumers – including identity and health information – and caused widespread outages across the healthcare ecosystem

These are just a few examples of the destructive power that ransomware wields over organizations. The losses from this destruction can be immense – the average cost of a ransomware attack is now $4.91 million.

The resurgence of ransomware comes at a time when another big shift is taking place. Cybercriminals have pivoted to next-generation tactics, using information-stealing malware (or “infostealers”) to siphon credentials, session cookies, and identity data from infected users and selling this information to ransomware operators.

At SpyCloud, we have continuously tracked the ongoing rise of the infostealer trend and its impact on follow-on attacks like ransomware. Combined with a similarly explosive growth in digital identity exposure in the past few years, these two trends are fueling a perfect storm for ransomware crimes.

**PLAYER TIP**
!
IBM security researchers reported a 266% upsurge in the use of infostealers by groups that specialize in ransomware. They also noted signs of “continued investment in infostealer innovation.”

**PLAYER TIP**
!
Here are just a few of the components that remove the barrier to entry into cybercrime for aspiring and seasoned players alike:

*   **MALWARE-AS-A-SERVICE (MaaS)**
    This off-the-shelf model for a variety of malware, and especially infostealers, enables even low-skilled cybercriminals to steal fresh and accurate identity data in bulk, including login credentials, session cookies, and device details – basically everything needed to impersonate an identity.

*   **INSTALL BROKERS**
    Also known as ad brokers, install services, and pay-per-install (PPI) services, these specialists offer a network of websites and advertisements that facilitate an affordable way to distribute malware at scale.

*   **INITIAL ACCESS BROKERS (IABs)**
    These individuals or entities sell guaranteed access into an organization’s network. IABs typically rent access to tools like infostealers from MaaS providers and then sell the access data to ransomware operators.

*   **RANSOMWARE-AS-A-SERVICE (RaaS)**
    This widely available business model provides access to an operator’s proven tools and tactics – everything needed to launch ransomware attacks, complete with support service and even tutorials – for a subscription fee or percentage of ransom payments.

**WHAT SPYCLOUD RESEARCH SAYS**
MASSIVE SCALE OF IDENTITY EXPOSURES CREATES NEW RISKS
The scale of identity exposure due to infostealers is massive: 61% of breaches last year were malware-related and responsible for 343.78 million stolen credentials.
Our recaptured data also shows that as many as 1 in 5 people are the victim of an infostealer infection, with each infection exposing anywhere from 10 to 25+ third-party business application credentials, on average.

INFOSTEALERS LEAD TO FUTURE RANSOMWARE ATTACKS
Through a deep analysis of recaptured infostealer logs, we discovered that the presence of infostealer malware correlates to the likelihood that a company will experience a ransomware attack in the near future.
Nearly one-third of companies that experienced a ransomware event last year had at least one infostealer infection in the 16 weeks prior to being attacked.

ANTIVIRUS, MFA, AND TRADITIONAL DEFENSES AREN’T ENOUGH
According to our recent research, for the first six months of 2024, at least 54% of devices infected with infostealer malware had an antivirus or EDR solution installed at the time of successful malware infection.²
With infostealers and session hijacking at play, traditional solutions like antivirus and multifactor authentication (MFA) don’t mean you’re fully protected.

So how well are current ransomware defenses keeping up with the pace, tactics, and scale of cybercriminal innovation? That’s what we set out to uncover.

## Why We Do This Report

The numbers in this report that show the prevalence and impact of ransomware only tell part of the story. The developments that every organization should be concerned about happen beyond the edges of the cybersecurity world, deep in the criminal underground. This hidden, sprawling ecosystem is home to a burgeoning number of specialized products and services for cybercrime enablement.

The standardization and professionalizing of what were once ad-hoc activities is a contributing factor that makes digital identities a top attack vector. With identity data – exfiltrated from user devices infected by malware – at their fingertips, a growing crop of unskilled cybercriminals can hijack a user session, initiate account takeover (ATO), and gain access that enables them to launch ransomware attacks.

We do this survey because our mission is to disrupt the cycle of cybercrime, and the cybercrime problem as it stands today is big.

## Survey Method: How We Collected Data for This Report

For this fourth annual report, we surveyed 510 individuals in active cybersecurity roles within organizations in the US and the UK with at least 500 employees.

As you’ll see, we asked them about:

*   Their top concerns about malware and ransomware, as well as current defense practices
*   Common entry points for real-life ransomware incidents
*   The impact of ransomware attacks on their organization in the past 12 months, including ransom payments, data recovery, and cumulative response costs
*   Key ransomware prevention strategies and future security priorities

Survey respondents’ roles range from cybersecurity analysts to C-suite security executives. About one-third of the participants come from practitioner roles and others outside of leadership (Figure 1).

![Figure 1: Survey Participants by Role](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure1.png)

The size of surveyed organizations ranges from small (500-999 employees) and mid-market (between 1,000 and 9,999 employees) to large enterprises (with 10,000 or more employees). The two biggest cohorts represent mid-sized employers: 43% with 1,000-4,999 workers and 26% with 5,000-9,999. Large enterprises (10,000+ employees) comprise a total of 15% of respondents (Figure 2).

![Figure 2: Survey Participants by Size of Organization](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure2.png)

## The Dark Beginnings of the Ransomware Journey

Like the majority of cybercriminals, ransomware actors are largely driven by their desire to build a cache of profits, and businesses are the ones that ultimately pay that price.

Research suggests that ransom payments surged last year, with a 2.6x increase in the average payment and 5x in the median. Likewise, recovery costs have followed an upward trajectory every year, climbing to an average of $2.73 million in 2024 (compared to $1.82 million in 2023). As financial losses from ransomware continue to climb, so does the frequency of incidents: insurance claims data shows a 64% increase in 2023 compared to the prior year.

**TOP THREE CONCERNS**
So it’s no surprise that ransomware maintained a strong lead among our survey respondents as the greatest threat to their organization. Like last year, ransomware, phishing, and infostealers remain the top three concerns that keep security professionals up at night (Figure 3).

1.  RANSOMWARE
2.  PHISHING
3.  INFOSTEALER MALWARE

**TOP THREATS / RISKS REPORTED BY SECURITY TEAMS**
*   RANSOMWARE: 4.04
*   PHISHING / SPEAR-PHISHING: 3.94
*   INFOSTEALER MALWARE: 3.90
*   THIRD-PARTY USERS / DEVICES: 3.85
*   SHADOW IT: 3.72
*   ACCOUNT TAKEOVER (ATO): 3.64
*   MALICIOUS INSIDERS: 3.64
*   UNMANAGED DEVICES: 3.58

**A NEXT-GEN THREAT: HOW SESSION HIJACKING COMPOUNDS RANSOMWARE RISK**
Next-generation ATO – which uses session hijacking instead of relying on traditional credentials – allows threat actors to sidestep all types of authentication, including MFA and passwordless authentication. By hijacking user sessions that have already been authenticated, cybercriminals (including ransomware operators) become a clone of a legitimate employee, without setting off typical anti-fraud alarm bells. This greatly increases their success rate of gaining access to an organization’s network and systems to launch an attack.

Last year, SpyCloud recaptured more than 20 billion cookie records from infostealer malware, with an average 2,000+ records per infected device. Leveraging malware-siphoned session cookies for next-generation account takeover is becoming an increasingly common cybercrime tactic.

## The Evolving Malware Landscape: Where Adversaries Gain Momentum

Among this year’s respondents, virtually everyone – 99.8% – is concerned about the potential for identity, session cookie, and other data siphoned from malware-infected devices being used to enable more harmful attacks like ransomware and account takeover.

![Figure 4: Concern for Malware-Siphoned Data Leading to Future Attacks](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure4.png)

Large breaches like the Medibank hack (which leveraged stolen credentials from an infostealer infection) are raising the profile of infostealer malware for security teams. Interestingly, security architects and engineers are the least concerned among the teams surveyed (Figure 4).

Our survey findings reflect the growing presence of infostealers in headlines as well as their prevalence as a tactic. What worries us the most is the stealers’ continued evolution. Every year, the vast malware expanse draws in new infostealer families – often with new capabilities that allow them to bypass IAM security features and evade detection. Elusive, for instance, uses advanced encryption to stay stealthy, while Lumma can allegedly restore expired auth cookies to hijack user accounts.

### Stealthy Stealers at Play

Because infostealers are designed to steal information from an infected host, they make great accomplices to ransomware actors attempting to gain credentials before moving laterally in an environment.

Many infostealers also double as malware loaders, allowing the stealers to load secondary payloads such as persistent malware or ransomware. This behavior is observed in RisePro, Lumma, Mystic Stealer, and others.

### Infostealer Infections Present in the 3 Months Prior to Reported Ransomware Attacks in 2024

SpyCloud research shows the relationship between specific infostealer infections and ransomware events.

*   PENNYWISE – 0.42%
*   AURORA – 1.17%
*   RACCOON – 1.71%
*   DARKCRYSTAL – 2.99%
*   SYMTIC – 3.85%
*   CAMULUS – 7.62%
*   VIDAR – 9.83%
*   CRYPTBOT – 11.54%
*   RISEPRO – 17.52%
*   METASTEALER – 19.66%
*   STEALC – 20.51%
*   REDLINE – 40.60%
*   SYNATHAMADAHAR – 76.9%

![Figure 6: Infostealer Infections Present in the 3 Months Prior to Reported Ransomware Attacks in 2024](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure6.png)

### Top Infostealer Villains

*   **LummaC2**
    Known for its dynamic configurations, LummaC2 can customize what data it steals in real time. In late 2023, it added email theft from various clients, Google cookie regeneration, and turning infected bots into SOCKS proxies. It also targets browser extensions and claims to steal 2FA secrets, making it a multi-faceted threat.

*   **RedLine**
    A highly adaptable stealer recognized for its dynamic configurations, enabling it to adjust its stealing and loading capabilities on the fly. It can also regenerate expired Google cookies, a feature first observed with LummaC2. Its flexibility and advanced functionalities make it a significant threat, and it has wide acceptance by the criminal community.

*   **StealC**
    Described as a “copycat of Vidar and Raccoon,” StealC can be customized to steal data based on the cybercriminals’ needs. This infostealer is commonly distributed by so-called malware traffers – organized cybercrime workers who are responsible for redirecting victim traffic to malicious content operated by others.

*   **MetaStealer**
    An “improved version” of RedLine that steals credentials and cryptocurrency wallets. It’s deployed through malspam email campaigns, cracked software advertisements on social media like YouTube, and malvertising.

*   **RisePro**
    A sophisticated stealer that not only exfiltrates sensitive data but also serves as a malware loader, enabling the deployment of secondary payloads like other malware or ransomware. This dual functionality enhances its threat level.

*   **CryptBot**
    Reemerged with a new and improved version targeting sensitive data like logins and credit card data stored in browsers. This infostealer is distributed via compromised websites that seem to offer cracked video games and other popular software.

**OTHER STEALERS TO KEEP ON YOUR RADAR**

*   **WorldWind / Prynt Stealer**
    While not as configurable as other stealers on this list, WorldWind uses Telegram as its exfiltration route by default, shortening the time to stolen information access, especially for less-technical cybercriminals.

*   **Atomic Stealer**
    Atomic is notorious for targeting macOS, and particularly cryptocurrency enthusiasts as its victims. It deploys a backdoor specifically designed to steal seed phrases from victims using the Ledger Live crypto wallet. It’s also well-known for harvesting data from browser extensions, making it a broad-spectrum threat.

### Battling Cyber Threats: Fighting for the Upper Hand

Despite worthwhile concerns about infostealers, surveyed organizations show some big gaps in their ability to remediate malware exposures. Identifying business applications exposed by malware and invalidating compromised web sessions are two of the most critical steps that address the long-term risks of malware – yet they rank at the bottom of malware detection and response capabilities (Figure 5).

Perceptions do vary across roles, though. Most notably, executive leaders are the only group that rank all of their organization’s capabilities higher than the average across all roles. In general, they seem more confident than other cybersecurity professionals in their security teams’ capabilities.

![Figure 5: Malware Detection and Response Capabilities](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure5.png)

**PLAYER TIP**
To fully negate opportunities for ransomware and other critical threats, organizations need to leverage post-infection remediation steps like resetting application credentials and invalidating session cookies siphoned by infostealer malware. With this extra boost, IAM teams – who are becoming instrumental in the battle against ransomware – and other defenders can finally make strides in the journey to preventing this threat.

Remediating malware can feel a bit like playing in a fog of war. Overwhelmingly, our respondents agree that having better visibility of malware-exfiltrated data (such as exposed credentials and session cookies/tokens) and automating remediation workflows would significantly improve their organization’s resistance to ransomware attacks and security posture overall (Figure 6).

![Figure 6: Better Visibility & Remediation of Malware-Exfiltrated Data is Needed](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure6.png)

Year over year, very large enterprises (25,000+ employees) and the financial services industry show the biggest growth in the number of respondents who “strongly agree” with the need to better address malware exposures – a change of +17 and +32 percentage points, respectively.

## Malware Infection Remediation Practices: Far From a Critical Hit

While there’s universal agreement that more needs to be done to address the malware problem, we also asked organizations what their standard practices look like today to better understand the baseline.

The top routine actions that organizations take in response to a malware infection on an infected device are:

*   Investigating the incident (79%)
*   Resetting passwords for potentially exposed applications (77%)
*   Attempting to remove the malware (67%)

**PLAYER TIP**
We were pleasantly surprised to see a big year-over-year jump in password resets (from 64% to 77%), which may be a positive sign of maturity – though it could just as easily indicate that this is a simple, low-hanging-fruit action.

Regardless of what drove the change, keep in mind the shift to a “brute force” reset and wipe doesn’t solve the larger issue of stolen data, and thus access, in the wrong hands. Reviewing logs to analyze exposure and determine the necessary remediation path should be a high priority. Yet even fewer security teams do this than before: only 55% this year vs. 73% last year (Figure 7).

![Figure 7: Routine Responses to Malware Infections](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure7.png)

## Risk from Third-Party Exposure: Adversaries’ Extra Advantage

Threat actors leverage plenty of strategies to gain an upper hand in the malware landscape, but nothing presents as big an opportunity as infected third-party and unmanaged devices. The digital-first environment has opened the floodgates to unmanaged and third-party devices, and security teams often have little-to-no visibility into vulnerabilities associated with these endpoints. This has huge implications because third-party devices and users greatly increase exposure to threats.

**PLAYER TIP**
!
**ILLUMINATE YOUR ATTACK SURFACE**
Security researchers found that as many as 90% of security compromises originate from unmanaged devices. Outside of IT control and visibility and with limited security, these devices hold an undeniable appeal for threat actors.

Whether these devices belong to your employees or third parties, they’re used to access your corporate applications – and our research shows that, on average, a single malware infection exposes access to 10 to 25 business applications. Add to that the fact that the average organization has more than 300 applications – technically, a single malware infection can expose access to all of them.

Last year, SpyCloud recaptured more than 4.7 million third-party application credentials harvested by malware on both managed and unmanaged devices. These malware-harvested third-party credentials came from numerous popular business apps in these categories:

*   Communication & collaboration (nearly 2M credentials)
*   Human resources (1M)
*   Software development & IT tools (714k)
*   Customer support (208k)
*   Identity & access management (204k)

Without visibility into these exposures, it’s difficult for an organization to fully understand its risk and properly defend itself. As shown in Figure 5 earlier, detecting third-party or unmanaged devices infected by malware is the capability organizations lack the most today.

Additionally, almost all survey participants are concerned about risks stemming from infected or compromised third-party accounts (Figure 8, Page 23). Nobody understands the risks better than IAM teams, who are the most “extremely” concerned – likely because they understand the reality of both the scale of third-party access to corporate applications, and limitations in organizations’ ability to detect or remediate resulting unauthorized access.

Whether cybercriminals leverage compromised third-party accounts, unmanaged devices, or other vulnerable entry points, chances are that with malware tactics, they can quickly escalate to the next level: ransomware.

## The Ransomware Landscape: Land of Infinite Gameplay

If the influx of new players is any indication, the ransomware terrain is far from inhospitable for cybercriminals. Some researchers noted 538 new variants in 2023, suggesting an onslaught of new, independent actors.

![Figure 8: Frequency of Ransomware Incidents in the Past Year](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure8.png)

Of course, we’ve seen some turbulence in this landscape, too, as law enforcement cracked down on the likes of Hive, LockBit, and Blackcat AlphV. But the setback to cybercriminals was temporary, as new ransomware actors quickly stepped up to the plate or others changed groups to avoid detection or sanctioning. Meanwhile, in the latest example of threat actors’ resilience, LockBit – though weakened – simply respawned a few days later with a new leak site and resumed posting data.

Given the ransomware cybercriminals’ stamina, it comes as no surprise to see an increase in the number of surveyed organizations that have been affected by ransomware in the past 12 months. The number of organizations affected by ransomware at least once rose from 81% to 92% – and those affected³ more than once grew even more significantly, from 61% last year to 75% this year. This means that we saw a sharp decline in organizations that weren’t hit at all, down to just 8% this year, compared to 19% in 2023.

While all sectors were reportedly affected by ransomware events, based on respondents’ answers we found that:

*   **FINANCIAL SERVICES** is the most likely to have been affected at least one time (only 8% answered “none”)
*   **TECH COMPANIES** were the most likely to have been affected at least 6 times (83%) as well as more than 10 times (6%)
*   **HEALTHCARE** is the least likely to have not been affected at all (17%), followed by professional services (12%)

**TOP INDUSTRIES MOST LIKELY TO BE TARGETED BY A FUTURE RANSOMWARE ATTACK IN 2024**
Based on recaptured data and malware logs tied to the industries we surveyed, as well as previous self-reported ransomware attacks, SpyCloud calculated a prediction to identify the industries with the greatest risk of future ransomware events.

*   **MOST LIKELY** (6.3x more likely to experience a ransomware attack)
*   **LESS LIKELY (STILL AT RISK)** (2.1x more likely to experience a ransomware attack)

**PLAYER TIP**
!
**RANSOMWARE GROUPS – OR EXTORTIONISTS?**
Technically, it can be very difficult to encrypt a target and provide keys to unencrypt it after receiving a ransomware payment. Some ransomware groups have taken to skipping the lock and encrypt component of traditional ransomware and have instead largely pivoted to simply exfiltrating data and extorting payment in order to prevent the ransomware actor from posting the stolen data on a leak site.

### Data, Financial Knockouts

Unfortunately, our data shows that year-over-year, significantly more organizations paid a ransom in the past 12 months: 62% this year vs. 48% in last year’s report (Figure 9). But only about a third of those organizations fully recovered their data, which is a stark reminder that giving in to cybercriminals’ demands is a gamble, and the odds are not always in your favor.

Additionally:

*   There was a significant uptick in those who paid and lost the data or had to recover it another way: 13% vs. 3% last year.
*   The number of those who paid ransom and lost all their data tripled, from 1.2% to 3.7%. Fortunately, this number is comparatively small; however, the implications for those who experience this data loss could be felt deeply.

![Figure 9: Response and Outcome to Ransomware Attack](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure9.png)

Perhaps buoyed by their growing success rates, ransomware groups have become bolder: nearly two-thirds of ransom demands last year were for $1 million or more, with an average of $4.3 million. One ransomware group recently received an unprecedented ransom payment of $75 million. And reports to the FBI last year show a 74% increase in the cost of ransomware incidents last year compared to 2022.

We see some of this reflected in our data as well. There was an increase in the number of organizations paying more than $1 million in cumulative costs – from 39% last year to 44% this year (Figure 10).

![Figure 10: Cumulative Cost of Ransomware Attacks in the Last 12 Months](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure10.png)

In some cases, cumulative costs can extend to general disruption, loss of business and opportunities, productivity decreases, reputational damage, and more. For instance, 49% of an organization’s computers are impacted by a ransomware attack, which can severely cripple business functions. And, as we saw from some of the recent incidents mentioned earlier, this disruption can last for weeks and sometimes months.

### Cracks in Your Cyber Defenses: Common Attack Entry Points

For the first time, we also asked survey participants who were affected by ransomware to share the entry points used by attackers to gain initial access. They reported the most common entry points to be phishing/social engineering, third-party access, and stolen cookies that enabled session hijacking (Figure 11).

While compromised session cookies are a newer entry point for ransomware, we expect to see session hijacking continue to gather momentum, and the more organizations are aware and prepared, the better off they’ll be.

Interestingly enough, identity teams are ahead of others in seeing this entry point more often: 20% of IAM directors, managers, or specialists called it out, compared to only 12% of their security counterparts and 15% of analysts and incident responders.

Some session cookies can remain valid for weeks, months, and even longer. Since many organizations don’t yet monitor for cookies stolen by infostealer malware – let alone invalidate those sessions – a single infection could leave an organization exposed. When leveraged by ransomware perpetrators, this access can come with immense consequences.

![Figure 11: Most Common Entry Points for Ransomware](https://spycloud.com/resource/report/2024-malware-ransomware-defense-report/figure11.png)

In terms of general perceptions about the riskiest potential entry point, it’s not unexpected to see phishing/social engineering and unpatched vulnerabilities among the top factors. Most organizations are going to think about areas that historically have been big issues. But this perception also colors their remediation efforts – and traditional remediation methods have lost their effectiveness when it comes to combating the full scope of the ransomware threat.

With ransomware operators showing more interest in next-generation tactics – like using infostealer-exfiltrated session cookies – organizations must shift to next-generation defense. So, are they? As our data below shows, not as much as we’d like to see.

### Next-Gen Showdown: The Future of Ransomware Defense

Traditional malware mitigation, which is only focused on the infected device, is akin to a stun. At best, it gets rid of the infection. It doesn’t prevent cybercriminals from taking advantage of the data they siphoned from the device because it stops short of remediating the prolonged risk from that exposed data. To negate the opportunities created by infostealer-exfiltrated data and to disrupt ransomware attacks, security teams and their counterparts in fraud prevention need to shift their focus to the digital identity.

**THE IDENTITY-CENTRIC APPROACH**

**PLAYER TIP**
Malicious actors are moving beyond the traditional use of stolen username and password pairs to perpetrate crimes against employees and organizations. Using expanded datasets, criminals have increased the scope of their attack patterns, based upon identity records that come from different sources and that can be linked together using PII, like social security numbers or social handles. Case in point, the National Public Data breach is a prime example of how bad actors are targeting identity data that can be used in follow-on attacks.

In this way, users now have to worry about their combined digital identity, which can be formed by cross-referencing the information that has been stolen about them from dozens or hundreds of sources. An identity-centric approach means SOC teams expand their defensive posture beyond just the device to account for the many facets of the modern digital identity.

Identity-centric malware remediation includes extra steps like resetting application credentials and invalidating session cookies that have been exfiltrated by malware. But first, you must monitor for compromised credentials and session cookies – a countermeasure lower on many organizations’ priority list this year (Figure 12).

![Figure