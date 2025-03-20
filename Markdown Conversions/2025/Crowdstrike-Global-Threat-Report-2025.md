# CROWDSTRIKE 2025 GLOBAL THREAT REPORT

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Threat Landscape Overview](#threat-landscape-overview)
- [Key Adversary Themes](#key-adversary-themes)
  - [The Business of Social Engineering](#the-business-of-social-engineering)
  - [Generative Artificial Intelligence and the Enterprising Adversary](#generative-artificial-intelligence-and-the-enterprising-adversary)
  - [China’s Cyber Enterprise](#chinas-cyber-enterprise)
  - [Cloud-Conscious Threat Actors Continue to Innovate](#cloud-conscious-threat-actors-continue-to-innovate)
  - [Enterprising Vulnerability Exploitation](#enterprising-vulnerability-exploitation)
  - [SaaS Exploitation Likely to Continue](#saas-exploitation-likely-to-continue)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [CrowdStrike Falcon Platform, Products, and Services](#crowdstrike-falcon-platform-products-and-services)
- [About CrowdStrike](#about-crowdstrike)

## Foreword

Don’t Underestimate Today’s Enterprising Adversaries

Watch any nature program, and you’ll quickly discover what happens to animals that underestimate their adversaries. They become prey. The same principle applies in cybersecurity — the adversary is advancing so fast that you can’t afford to underestimate them.

Our latest research demonstrates that adversaries are becoming more efficient, focused, and business-like in their approach — in many ways, more like the enterprise organizations they prey upon. That’s why our team of security analysts, experts, and authors chose “the enterprising adversary” as the theme for this year’s CrowdStrike Global Threat Report.

Take generative artificial intelligence (genAI), for instance. Highly effective adversaries across all major categories — nation-state, eCrime, and hacktivist — have become early and avid adopters. The “force multiplier” impact of off-the-shelf chatbots has made genAI a popular addition to the global hacker toolbox.

Along with legitimate organizations, easy access to commercial large language models (LLMs) is making adversaries more productive, too. It’s shortening their learning curve and development cycles, and it’s allowing them to increase the scale and pace of their activities. Though this report indicates that malicious use of AI is growing, it remains largely iterative and evolutionary at this point in time. Only occasionally does it manifest as an entirely novel use case. But it is still early days.

At CrowdStrike, we aren’t waiting for threat actors to experience their next “aha” moment. We are accelerating our own use of AI techniques — from our foundational machine learning capabilities to our leading-edge generative and agentic AI models — to help our customers anticipate the next zero-day attacks in advance and proactively inoculate themselves against them. This is the essence of an AI-native approach to cyber defense. Unlike legacy systems — which are still relied upon by organizations globally — we don’t sit idle until an attack occurs before we can identify and stop it.

Adversarial Enterprise T
akes Its Toll

The job of protecting your organizations continues to get harder by the day. You’ll find ample evidence of this fact in the data that follows. The number of new “named adversaries” tracked by the elite CrowdStrike Counter Adversary Operations team continues to expand, and established adversaries are constantly adding new targets and more sophisticated techniques to their evasion, intrusion, and exfiltration arsenals.

> FOR MORE INFORMATION ON ANY OF THE ADVERSARIES MENTIONED IN THIS REPORT AND THOSE TARGETING YOUR INDUSTRY OR REGION, CHECK OUT THE CROWDSTRIKE ADVERSARY UNIVERSE.

The purpose of this report is to arm you, the world’s security professionals and dedicated cyber defenders, with the knowledge you need to keep a step ahead of these threat actors — and to never, ever underestimate them.

Here are a few key facts you should know about the shifting threat landscape:

- Breakout time — how long it takes for an adversary to start moving laterally across your network — reached an all-time low in the past year: The average fell to 48 minutes, and the fastest breakout time we observed dropped to a mere 51 seconds.
- Voice phishing (vishing) attacks, where adversaries call victims to amplify their activities with persuasive social engineering techniques, saw explosive growth — up 442% between the first and second half of 2024.
- Attacks related to initial access boomed, accounting for 52% of vulnerabilities observed by CrowdStrike in 2024. Providing access as a service became a thriving business, as advertisements for access brokers increased 50% year-over-year.
- Among nation-states, China-nexus activity surged 150% overall, with some targeted industries suffering 200% to 300% more attacks than the previous year.
- GenAI played a pivotal role in sophisticated cyberattack campaigns in 2024. It enabled FAMOUS CHOLLIMA to create highly convincing fake IT job candidates that infiltrated victim organizations, and it helped China-, Russia-, and Iran-affiliated threat actors conduct AI-driven disinformation and influence operations to disrupt elections.

As with every product and service we provide, we hope this year’s Global Threat Report makes you more aware, more attuned to the threats you may be facing now or in the near future, and better equipped overall to defend your organization.

CrowdStrike remains at your service and wholly dedicated to the single-minded vision and mission on which the company was founded more than a decade ago. Our company, our platform, and our people are focused on one thing: working together in close partnership with our customers to stop breaches.

CrowdStrike CEO and Founder

## Introduction

The CrowdStrike 2025 Global Threat Report is the industry’s preeminent source on adversary intelligence, examining the emerging adversary trends of the past year. During 2024, adversaries matured faster than ever, innovating techniques and tools as well as finding creative solutions to circumvent modern defenses, all while staying laser-focused on their targets. Adversaries are streamlining their tactics, refining and scaling successful strategies, and learning from both their own and their colleagues’ mistakes and successes to conduct attacks with a business-oriented approach. 2024 was the year of the enterprising adversary.

eCrime adversaries exemplified such enterprising cyberattacks, constantly adapting to shifting environments and quickly scaling effective operations. Throughout 2024, initial access techniques began to shift — eCrime adversaries began moving away from phishing to alternative access methods. This shift suggests that commodity malware operators are likely finding more effective and successful infections with innovative techniques as they face hardened security defenses. One such technique that proliferated in 2024 is social engineering leveraging telephony-based exploitation: Various eCrime adversaries are increasingly adopting vishing, callback phishing, and help desk social engineering attacks to gain a foothold into networks.

These shifting initial access methods are consistent with a larger trend identified in the CrowdStrike 2024 Threat Hunting Report: Rather than delivering malware, eCrime adversaries are increasingly leveraging legitimate remote monitoring and management (RMM) tools to access a victim’s system — and therefore making malware non-essential for successful operations. Throughout 2024, eCrime actors frequently leveraged RMM tools in their campaigns.

In 2024, China’s cyber espionage operations reached new levels of maturity, with adversaries maintaining a higher operational tempo than observed in 2023 and engaging in prolific targeting. Decades of government investment into China’s cyber workforce and programs have yielded matured capabilities and efficiencies as well as an increasing number of new, specialized China-nexus adversaries. In 2024, CrowdStrike graduated seven new China-nexus adversaries and observed a 150% increase in China-nexus activity across all sectors on average compared to 2023. Additionally, China-nexus adversaries increasingly prioritized operations security (OPSEC) and at-scale infrastructure management by obfuscating their activities via operational relay box (ORB) networks.

Democratic People's Republic of Korea (DPRK)-nexus adversaries LABYRINTH CHOLLIMA, VELVET CHOLLIMA, and SILENT CHOLLIMA consistently targeted defense and aerospace entities in various countries. However, similar to previous years, most of these adversaries’ cyber operations focused on generating currency, which has become a lifeline for the regime. Notably, FAMOUS CHOLLIMA innovated their currency generation operations in 2024 by leveraging their IT worker schemes at scale across the globe. During 2024, CrowdStrike Falcon® Adversary OverWatch™ threat hunters responded to 304 FAMOUS CHOLLIMA incidents, with nearly 40% of these representing insider threat operations.

While DPRK adversaries have skillfully shifted their operations to support large-scale currency generation over the years, the specific tactics deployed in their 2024 operations — such as leveraging virtual interviews, allocating significant resources and staffing, and using laptop farms at scale — highlight the DPRK’s enterprising approach to computer network operations (CNO).

Across the 2024 vulnerability threat landscape, threat actors continued to target devices in the network periphery and regularly leveraged publicly available vulnerability research — such as disclosures, technical blogs, and proof-of-concept (POC) exploits — to aid their malicious activity. Within the cloud landscape, an increasing number of new adversaries effectively exploited cloud environments, often employing previously tested techniques and adapting them for their own goals.

Adversaries also leveraged genAI when conducting intelligence operations (IO) targeting election processes. Throughout 2024, adversaries increasingly adopted genAI, especially as a part of social engineering efforts.

Staying one step ahead of the enterprising adversary is difficult — but not impossible. As the adversary matures, so do your defenses. As the adversary innovates, so does CrowdStrike. CrowdStrike Counter Adversary Operations raises the operational cost of conducting malicious cyber operations by combining the power of threat intelligence with the speed of dedicated hunting teams and trillions of cutting-edge telemetry events from the AI-native CrowdStrike Falcon® platform to detect, disrupt, and stop today’s sophisticated adversaries.

Counter Adversary Operations comprises two closely integrated teams. The CrowdStrike Intelligence team provides actionable reporting that identifies new adversaries, monitors their activities, and captures emerging cyber threat developments in real time. The CrowdStrike OverWatch team uses this intelligence to conduct proactive threat hunting across customer telemetry to detect and address malicious activity.

> DURING 2024, CROWDSTRIKE FALCON ADVERSARY OVERWATCH THREAT HUNTERS RESPONDED TO 304 FAMOUS CHOLLIMA INCIDENTS, WITH NEARLY 40% OF THESE REPRESENTING INSIDER THREAT OPERATIONS.

During 2024, CrowdStrike Intelligence introduced 26 newly named adversaries — including the new Kazakhstan-based adversary COMRADE SAIGA — raising the total number of named adversaries tracked across all motivations to 257. In addition to named adversaries, CrowdStrike Intelligence tracks more than 140 active malicious activity clusters and emerging threat groups.

In the past year, CrowdStrike has been working to enrich the in-platform Falcon experience by providing further insights from CrowdStrike’s broad view into the changing threat landscape in different industries and regions. CrowdStrike ties these insights to activity occurring outside the customer perimeter by monitoring the criminal underground and emerging threats.

New dashboards provide insight into Falcon Adversary OverWatch threat hunting findings across CrowdStrike’s customer ecosystem, while click-to-hunt capabilities enable seamless transition from new threat hunting query feeds to real-time investigations in CrowdStrike Falcon® Next-Gen SIEM. Additionally, new Counter Adversary Playbooks make it easy to build comprehensive intelligence monitoring programs customized for any organization.

The CrowdStrike 2025 Global Threat Report summarizes the CrowdStrike Intelligence team’s analysis performed throughout 2024 and describes notable themes, trends, and events across the cyber threat landscape. This annual report also includes anticipatory threat assessments to help prepare and protect organizations throughout the coming year.

> 26 NEW ADVERSARIES NAMED IN 2024

> 257 TOTAL ADVERSARIES NOW TRACKED BY CROWDSTRIKE

> 140 ACTIVE MALICIOUS ACTIVITY CLUSTERS AND EMERGING THREAT GROUPS TRACKED

## Naming Conventions

| ADVERSARY | NATION-STATE OR CATEGORY |
|---|---|
| BEAR | RUSSIA |
| BUFFALO | VIETNAM |
| CHOLLIMA | DPRK (NORTH KOREA) |
| CRANE | ROK (REPUBLIC OF KOREA) |
| HAWK | SYRIA |
| JACKAL | HACKTIVIST |
| KITTEN | IRAN |
| LEOPARD | PAKISTAN |
| LYNX | GEORGIA |
| OCELOT | COLOMBIA |
| PANDA | PEOPLE’S REPUBLIC OF CHINA |
| SAIGA | KAZAKHSTAN |
| SPIDER | eCRIME |
| TIGER | INDIA |
| WOLF | TURKEY |
| SPHINX | EGYPT |

## Threat Landscape Overview

Cyberattacks are escalating in speed, volume, and sophistication. As organizations work to strengthen their defenses, adversaries target their weaknesses: employees susceptible to social engineering and systems lacking modern security controls. Once inside, they act within seconds, stealthily moving across networks to execute attacks. In 2024, 79% of the detections CrowdStrike observed were malware-free, indicating adversaries are instead using hands-on-keyboard techniques that blend in with legitimate user activity and impede detection.

- China-nexus activity surged 150% across all sectors, with a staggering 200-300% increase in key targeted industries
- Access broker advertisements increased 50% year-over-year
- Vishing attacks skyrocketed 442% between the first and second half of 2024
- Valid account abuse accounted for 35% of cloud incidents
- Average eCrime breakout time dropped to 48 minutes, with the fastest breakout observed at just 51 seconds
- 52% of vulnerabilities observed by CrowdStrike in 2024 were related to initial access
- 79% of detections in 2024 were malware-free, up from 40% in 2019
- 26 new adversaries tracked by CrowdStrike, raising the total to 257

![Image description: Access broker advertisements by month, 2024]
Figure 1. Access broker advertisements by month, 2024

The Growing Reliance on Identity Attacks and Vulnerability Exploits

Every breach starts with initial access, and identity-based attacks are among the most effective entry methods. Instead of traditional malware, adversaries favor faster and stealthier methods such as vishing, social engineering, access broker services, and trusted relationship abuse.

A major driver behind this shift is the rise of access brokers: specialists who acquire access to organizations and sell it to other threat actors, including ransomware operators. Access broker activity surged in 2024, with advertised accesses increasing by nearly 50% over 2023. Meanwhile, valid account abuse was responsible for 35% of cloud-related incidents, reflecting attackers' growing focus on identity compromise as a gateway to broader enterprise environments.

But identity isn’t the only target — adversaries are also exploiting vulnerabilities to gain initial access. In 2024, 52% of observed vulnerabilities were linked to initial access, reinforcing the need to secure exposed systems before attackers establish a foothold.

As adversaries scale identity-based attacks and vulnerability exploitation, organizations must adopt proactive defense strategies, including identity verification, risk-based patching, and early detection of credential abuse, to disrupt adversary operations before they escalate.

| MONTH | 2024 |
|---|---|
| JANUARY | 590 |
| FEBRUARY | 306 |
| MARCH | 242 |
| APRIL | 186 |
| MAY | 813 |
| JUNE | 201 |
| JULY | 177 |
| AUGUST | 151 |
| SEPTEMBER | 253 |
| OCTOBER | 386 |
| NOVEMBER | 328 |
| DECEMBER | 853 |
| TOTAL | 4,486 |

The Continued Rise of Interactive Intrusions

Modern cyber threats are increasingly dominated by “interactive intrusion” techniques, where adversaries execute hands-on-keyboard actions to achieve objectives. Unlike traditional malware attacks, these intrusions rely on human adversaries mimicking legitimate user or administrator behavior, making them exceptionally difficult to detect.

In 2024, CrowdStrike observed a 35% year-over-year increase in interactive intrusion campaigns. For the seventh consecutive year, the technology sector remained the most targeted industry, with high attack volumes also observed in consulting, manufacturing, and retail. The charts on the following page reflect the relative frequency of intrusions in the top geographical regions and industry verticals.

![Image description: Interactive intrusions by region, January-December 2024]
Figure 2. Interactive intrusions by region, January-December 2024

![Image description: Top 10 industries targeted by interactive intrusions, January-December 2024]
Figure 3. Top 10 industries targeted by interactive intrusions, January-December 2024

![Image description: Percentage of detections that were malware-free, 2019-2024]
Figure 4. Percentage of detections that were malware-free, 2019-2024

Top 10 Industries Targeted by Interactive Intrusions

- TECHNOLOGY
- CONSULTING AND PROFESSIONAL SERVICES
- MANUFACTURING
- RETAIL
- FINANCIAL SERVICES
- HEALTHCARE
- TELECOMMUNICATIONS
- GOVERNMENT
- INDUSTRIALS AND ENGINEERING
- ACADEMIC

Interactive Intrusions by Region

- NORTH AMERICA
- EAST ASIA
- EUROPE
- SOUTH ASIA
- MIDDLE EAST
- SOUTH AMERICA
- OCEANIA
- AFRICA

These statistics highlight the global reach of adversary operations and the necessity for cross-domain security strategies that account for identity compromise, lateral movement, and cloud-based attack vectors.

This shift toward malware-free attack techniques has been a defining trend over the past five years. In 2024, malware-free activity accounted for 79% of detections, a significant rise from 40% in 2019.

Breakout Time: The Race Against Adversaries

Once adversaries gain initial access, their next objective is to “break out” and move laterally from the initial foothold to high-value assets. The speed of this “breakout time” determines how fast a defender must respond to reduce the costs and damages associated with an intrusion.

In 2024, the average breakout time for interactive eCrime intrusions fell to 48 minutes, down from 62 minutes in 2023. Alarmingly, the fastest breakout was recorded at just 51 seconds — meaning defenders may have less than a minute to detect and respond before attackers establish deeper control.

This rapid escalation in breakout time reinforces the need for:

- Real-time threat detection to identify and halt intrusions before they spread
- Identity and access controls to prevent adversaries from leveraging valid credentials
- Proactive threat hunting to identify pre-attack behaviors and block adversary movements early

CASE STUDY

CURLY SPIDER's Social Engineering Attack

In 2024, CURLY SPIDER emerged as one of the fastest and most adaptive eCrime adversaries, executing high-speed, hands-on intrusions. In this case, the adversary attempted to achieve their objectives without even needing to break out to another device. The entire attack chain — from initial user interaction and social engineering to introducing a backdoor account to establish persistence — took under four minutes.

This incident would have been prevented by the CrowdStrike Falcon sensor with proper prevention policies. Regardless, within minutes, CrowdStrike OverWatch threat hunters saw the suspicious activity, notified the customer, and eliminated the threat.

How CURLY SPIDER Operates

This adversary relies heavily on social engineering for initial access. In some cases, the following will occur:

- A user will receive a large volume of spam emails impersonating charities, newsletters, or financial offers
- Shortly after, a caller posing as help desk or IT support claims the spam is caused by malware or outdated spam filters
- The user is instructed to join a remote session using an RMM tool, such as Microsoft Quick Assist or TeamViewer, with the attacker guiding them through the installation if the tool is not already present; in this case, the adversary chose Quick Assist to establish control

CrowdStrike OverWatch in Action: Stopping a Social Engineering Attack in Under 4 Minutes

Once CURLY SPIDER gains initial access, their window of opportunity is limited — access will only last as long as the victim remains on the call. To extend control, the adversary’s immediate objective is to establish persistent access before the session ends.

With remote access secured, CURLY SPIDER moves quickly — often while still actively engaging with the victim — to deploy their payloads and establish persistence. The bulk of the intrusion time is spent ensuring connectivity and troubleshooting any access issues to reach their cloud-hosted malicious scripts.

1. Validating Connectivity (3:43)

    - Posing as IT support offering assistance, the adversary requests access to Quick Assist.
    - The adversary ensures a connection to pre-configured cloud storage, where they host malicious scripts and work through any access barriers. Once access is confirmed, CURLY SPIDER downloads malicious scripts.
2. Deploying Payload (0:06)

   - CURLY SPIDER executes the scripts via curl or PowerShell. These scripts:
        - Modify registry run keys, creating a user to ensure execution at startup
        - Remove forensic artifacts to erase traces of the intrusion
3. Establishing Persistent Access (0:06)

    - The adversary creates a backdoor user, embedding persistence directly into the system.
    - The final payload is executed under a legitimate binary, allowing CURLY SPIDER to blend into normal activity and evade detection.

In this example, CURLY SPIDER does not rely on traditional “breakout” techniques to move laterally. Instead, the adversary compromises the network in seconds by securing long-term access before the victim even realizes what’s happening.

![Image Description: Timeline of CrowdStrike OverWatch moving faster than CURLY SPIDER to stop a social engineering attack in less than four minutes]
Figure 5. Timeline of CrowdStrike OverWatch moving faster than CURLY SPIDER to stop a social engineering attack in less than four minutes

Impact and Connection to Ransomware

In this case, CURLY SPIDER was stopped by CrowdStrike OverWatch before they could proceed with the rest of their attack. However, CrowdStrike Intelligence has seen these tactics directly support ransomware operations, and this adversary frequently collaborates with WANDERING SPIDER, the group behind Black Basta ransomware. By combining high-tempo social engineering, legitimate remote tools, and cloud-hosted payloads, CURLY SPIDER exemplifies how modern adversaries bypass traditional defenses and achieve rapid operational success.

Proactive Defense Is Essential

Adversaries are refining their tactics to move faster and exploiting trusted access to bypass traditional defenses. The explosive growth in access broker activity, valid credential abuse, and interactive intrusions highlights the urgent need for organizations to adopt proactive security strategies that prevent, detect, and respond to these threats in real time.

Security teams must:

- Prioritize identity protection to prevent unauthorized access
- Harden cloud environments against credential abuse and address misconfigurations
- Accelerate response times to counter rapid breakout events
- Leverage AI-driven threat hunting to detect stealthy adversary movements

In 2025, attackers will only move faster. Will defenders keep up?

## Key Adversary Themes

### The Business of Social Engineering

Since 2023, eCrime and targeted intrusion adversaries have increasingly used identity compromise and other human-centric tradecraft to gain initial access and perform lateral movement. The emergence of this tactic is partly driven by the growing efficacy and abundance of modern host-based security tools such as endpoint detection and response (EDR) solutions. These factors have driven social engineering activity in which threat actors attempt to access targeted accounts or persuade legitimate employees to provide remote access to targeted systems.

In 2024, CrowdStrike Intelligence observed a massive increase in the number of distinct campaigns using telephone-oriented social engineering techniques to gain initial access, including vishing and help desk social engineering, marking a potential shift in the eCrime ecosystem.

2024 Vishing Trends

Several eCrime adversaries incorporated vishing into their intrusions in 2024, amounting to a 40% compounded monthly growth rate in observed vishing operations for the year. The latter half of 2024 saw a significant increase in the use of this tactic (Figure 6).

WHY VISHING IS SO EFFECTIVE

Similar to other social engineering techniques, vishing is effective because it targets human weakness or error rather than a flaw in software or an operating system (OS). Malicious activity may not be detected until later in an intrusion, such as during malicious binary execution or hands-on-keyboard activity, which can delay an effective response. This gives the threat actor an advantage and puts the onus on users to recognize potentially malicious behavior.

![Image description: Vishing intrusions detected by CrowdStrike OverWatch per month, 2024]
Figure 6. Vishing intrusions detected by CrowdStrike OverWatch per month, 2024

2024 Vishing Detections

- 442% Increase, H1 vs. H2 2024

In vishing campaigns, threat actors call targeted users and attempt to persuade them to download malicious payloads, establish remote support sessions, or enter their credentials to adversary-in-the-middle (AITM) phishing pages. In most 2024 vishing campaigns, threat actors impersonated IT support staff, calling targeted users under the pretext of resolving connectivity or security issues.

Throughout 2024, CrowdStrike Intelligence tracked at least six similar but likely distinct campaigns in which threat actors posing as IT staff called their targets and attempted to persuade them into establishing remote support sessions, often using Microsoft Quick Assist. In many cases, calls were made via Microsoft Teams from external tenants.

At least four of these campaigns leveraged spam bombing — sending thousands of spam emails to targeted users’ email addresses — as a pretext for the vishing call. The CrowdStrike Falcon® Complete Next-Gen MDR and CrowdStrike OverWatch teams observed a significant increase in these campaigns in the second half of 2024, detecting several relevant intrusions each day. eCrime adversary CURLY SPIDER is behind one of these campaigns, with relevant intrusions culminating in Black Basta ransomware deployment.

The long-standing Russia-based eCrime adversary CHATTY SPIDER continued to employ callback phishing as an initial access vector in data theft and extortion campaigns. In callback phishing, threat actors typically begin by sending a lure email to targeted users, often regarding an imminent charge or overdue payment. This prompts users to initiate a phone interaction. CHATTY SPIDER primarily targets the legal and insurance sectors and has demanded ransoms up to 8 million USD. Several eCrime actors used callback phishing to gain initial access in 2024, including one campaign that used it to install a remote support tool.

Brazil-based eCrime adversary PLUMP SPIDER exclusively targeted Brazil-based organizations throughout 2024 with attempts to conduct wire fraud. PLUMP SPIDER uses vishing calls to direct targeted users to sites hosting remote support and RMM tools such as RustDesk and Supremo. After gaining access, they compromise the victim’s payment systems to perform fraudulent financial transfers. In addition to targeting unwitting users, the adversary has reportedly attempted to recruit insiders at targeted organizations.

![Image Description: CURLY SPIDER, CHATTY SPIDER, and PLUMP SPIDER use vishing for initial access]
Figure 7. CURLY SPIDER, CHATTY SPIDER, and PLUMP SPIDER use vishing for initial access

Help Desk Social Engineering

In addition to vishing, multiple eCrime threat actors are increasingly adopting help desk social engineering tactics. In these campaigns, threat actors call a targeted organization’s IT help desk and impersonate a legitimate employee, attempting to persuade a help desk agent to reset passwords and/or multifactor authentication (MFA) for the relevant account.

Since early 2023, SCATTERED SPIDER has used this technique to gain access to single sign-on (SSO) accounts and cloud-based application suites. Multiple eCrime actors adopted this technique in 2024. Several relevant cases targeted academic and healthcare entities; in these incidents, threat actors subsequently used the compromised identity to exfiltrate data from cloud-based software as a service (SaaS) applications or modify employee payroll data.

IT help desks often require employees seeking password and MFA resets to provide their full name, date of birth, employee ID, and manager name or answer a previously determined security question. However, eCrime actors attempting to socially engineer help desk personnel often accurately respond to these questions. Much of this information is not necessarily privileged and can be found in public resources and social media sites. Identity data that is typically confidential, such as a Social Security number, is often advertised in underground markets.

In most help desk social engineering incidents, calls were made outside the victim’s local business hours. This is likely because it enables the threat actor to maintain longer access to the compromised account before the legitimate owner reports suspicious activity.

Threat actors using this technique often register their own device for MFA to enable persistent access to compromised accounts. They also often manually delete emails from compromised mailboxes related to suspicious account activity or configure mail transport rules to redirect relevant emails to a folder other than the main inbox.

Over the past year, several eCrime actors have openly recruited callers on popular eCrime forums. The advertisements are usually for English-speaking callers with knowledge of RMM tooling and experience conducting remote sessions. Some eCrime actors have also sought effective methods for spoofing phone numbers or encrypting calls to ensure caller IDs can be edited and appear more legitimate. This activity suggests phone-oriented social engineering will be a credible threat in 2025 as demand for these capabilities increases.

HOW TO MITIGATE HELP DESK SOCIAL ENGINEERING

- Require video authentication with government identification for employees who call to request self-service password resets
- Train help desk employees to exercise caution when taking password and MFA reset request phone calls made outside of business hours, particularly if an unusually high number of requests is made in a short time frame or if the caller purports to be calling on behalf of a colleague
- Use additional, non-push-based authentication factors such as FIDO2 to prevent account compromise
- Monitor for more than one user registering the same device or phone number for MFA

### Generative Artificial Intelligence and the Enterprising Adversary

GenAI has emerged as an attractive tool for adversaries with a low barrier to entry that makes it widely accessible. Recent advancements in genAI have enhanced the efficacy of certain cyber operations, particularly those using social engineering. It will almost certainly be employed in 2025 cyber operations.

Adversaries increasingly adopted genAI throughout 2024, particularly in support of social engineering efforts and high-tempo IO campaigns. Both were supported by genAI tools that can create highly convincing outputs without precise prompting, custom model training, or fine-tuning. Some threat actors are employing genAI, specifically LLMs, to support CNO efforts.

![Image description: Adversaries leveraging LLMs for social engineering and malicious CNO]
Figure 8. Adversaries leveraging LLMs for social engineering and malicious CNO

> A 2024 STUDY OF PHISHING EMAIL CLICK-THROUGH RATES INDICATED LLM-GENERATED PHISHING MESSAGES HAD A SIGNIFICANTLY HIGHER CLICK-THROUGH RATE (54%) THAN LIKELY HUMAN-WRITTEN PHISHING MESSAGES (12%).

GenAI Supports Social Engineering

LLMs and genAI models that create photorealistic imagery can generate convincing content at scale with minimal expertise. These tools can support social engineering efforts or IO. Despite the relative novelty of genAI, CrowdStrike has identified several examples of adversaries using it.

Social Engineering

Operators associated with DPRK-nexus adversary FAMOUS CHOLLIMA obtain positions at companies worldwide under fake personas, occasionally using genAI tools to socially engineer recruiters during the job application process. They also create fictitious LinkedIn profiles with genAI-created text and fake profile images. During interviews, many FAMOUS CHOLLIMA candidates provide answers likely derived from external sources. LLMs likely support these interviews by rapidly generating plausible responses.

GenAI is also used for BEC and fraud. In February 2024, unidentified threat actor(s) used public footage of a target company’s chief financial officer and other employees to create credible deepfake video clones and socially engineer the victim into transferring 25.6 million USD to the threat actor(s). In May 2024, industry reporting indicated threat actors had impersonated the CEO of an international professional services entity and attempted to solicit fraudulent payments. The threat actor also appeared to have used genAI to clone the CEO’s voice and attempted to persuade the call recipient to transfer funds.

The relationship between genAI and social engineering is also evidenced by the evolving focus of mobile malware. Since late 2023, the GoldPickaxe malware has been employed to steal biometric facial data from iOS and Android devices throughout the Asia Pacific (APAC) region. The malware, which cannot bypass authentication, captures images and videos to generate deepfake videos or perform face-swap operations.

Academic research further highlights the appeal of LLMs for social engineering. LLMs can generate phishing email content or credential harvesting websites at least as well as humans. A 2024 study of phishing email click-through rates indicated LLM-generated phishing messages had a significantly higher click-through rate (54%) than likely human-written phishing messages (12%). A separate 2024 study found detection rates for LLM-generated phishing pages were comparable to those for human-created phishing pages.

ADVERSARY SPOTLIGHT: FAMOUS CHOLLIMA

In 2024, FAMOUS CHOLLIMA quickly entered the spotlight due to their broad-scale operations, high operational tempo, and unique malicious insider tactics. The adversary regularly conducted financially motivated cyber operations across the globe, deploying their characteristic BeaverTail and InvisibleFerret malware families.

The adversary also oversaw a larger malicious insider campaign, using a network of personas to obtain fraudulent employment as software developers at large companies across North America, Western Europe, and East Asia (Figure 9). CrowdStrike OverWatch responded to FAMOUS CHOLLIMA activity in 304 incidents throughout the year, with nearly 40% representing insider threat operations.

![Image description: FAMOUS CHOLLIMA’s target sectors and regions, 2024]
Figure 9. FAMOUS CHOLLIMA’s target sectors and regions, 2024

FAMOUS CHOLLIMA’s cyber operations remained remarkably consistent throughout 2024, relying on delivery of a first-stage implant via a trojanized Node.js application. This application was disguised as a coding challenge for blockchain developers and delivered to victims under the guise of an employment interview. FAMOUS CHOLLIMA deployed seven distinct malware families in 2024, evading detection by slightly refining how the files were downloaded and executed.

FAMOUS CHOLLIMA’s malicious insiders appear to opportunistically pursue insider access across multiple sectors. The adversary’s activity is likely driven by available employment opportunities rather than specific targeting requirements.

Operatives use stolen or fraudulent identities to obtain software development jobs and then send their company-provided laptop to a third-party facilitator running a laptop farm. CrowdStrike OverWatch identified several laptop farms in Illinois, New York, Texas, and Florida. FAMOUS CHOLLIMA installs remote management tools and several browser extensions on the laptops. While CrowdStrike Intelligence has observed code or intellectual property exfiltration in some cases, most insider threats appear motivated by the job’s salary.

FAMOUS CHOLLIMA was one of the most active adversaries in 2024, significantly surpassing other state-nexus adversaries’ operational tempos. Notably, activity increased in the second half of 2024. This adversary will very likely continue conducting parallel cyber and insider threat campaigns well into 2025. This assessment is based on the adversary’s success, their ongoing high operational tempo, and the minimal impact of government indictments and actions against the adversary throughout 2024.

Information Operations

Adversaries can easily employ genAI tools to conduct IO campaigns and primarily use them to create tailored content at scale. Unlike other social engineering techniques, IO campaigns using AI-generated content are typically not checked for accuracy by most consumers. Adversaries may achieve their goals even if the target knows the content is fabricated.

In August 2024, industry sources reported on Green Cicada, an IO network likely enabled by a Chinese-language LLM system comprising more than 5,000 inauthentic accounts on the social media platform X. This network amplified politically divisive issues to exacerbate social divisions in the lead-up to the 2024 U.S. presidential election. Industry sources have linked the operation to China-based entities using LLMs.

Russia-aligned operators also used genAI to spread disinformation. In 2024, a propagandist likely used LLMs to generate tailored content and workflow automation tools that supported a vast IO campaign targeting U.S. audiences. Multiple Russia-nexus IO campaigns — including those targeting Israel, the U.S., and various European countries — employed genAI to generate text and images throughout 2024.

Threat Actors Leverage GenAI to Support CNO

Some adversaries are exploring the use of genAI to directly support CNO, likely using it to assist in writing utility scripts and developing tools or malware. Limited direct visibility into adversary use of LLMs often inhibits analysis of these campaigns. Nonetheless, many adversaries using LLMs are likely still familiarizing themselves with these tools.

In March 2024, a criminal actor distributed a spam email campaign that used a likely LLM-generated .txt template. The emails delivered an archive file containing the commodity malware Snake Keylogger. This campaign marks CrowdStrike’s first confirmed instance of a criminal actor using likely LLM-generated