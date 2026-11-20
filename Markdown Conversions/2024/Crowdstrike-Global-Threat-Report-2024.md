CROWDSTRIKE 2024 GLOBAL THREAT REPORT 34

Generative AI in Social Engineering
and Information Operations
The most active and visible use of generative AI in 2023 was in social
engineering and information operations (IO).
Generative AI tools enable less skilled adversaries to create high-quality
phishing emails that closely mimic professional communication, including
proper grammar, punctuation, and contextual appropriateness. This capability
is particularly useful for low-skilled adversaries whose first language is not
English, allowing them to overcome linguistic barriers that previously served
as a reliable indicator of malicious communications.
Similarly, generative AI empowers malicious actors to rapidly generate
convincing text, images, and audio for use in social engineering campaigns
such as deepfakes for voice and video phishing (vishing) and fake profiles
for use in online influence operations. These capabilities can significantly
enhance the perceived legitimacy of fraudulent personas, increasing the
likelihood that targets will fall victim to the scam or disinformation.

2024 Global Elections
and Cyber Threats
The year 2024 is unprecedented for global democracy, with elections
scheduled in more than 40 countries representing over 40% of the
world’s population. This concentration of major national elections
creates a target-rich environment for nation-state adversaries seeking
to influence political outcomes, undermine trust in democratic
institutions, or collect intelligence on candidates and political parties.
State-nexus adversaries, particularly from China, Russia, Iran, and
North Korea, are assessed as likely to conduct influence operations
and targeted intrusion campaigns during the 2024 election cycles.
Their objectives may include:
► Discrediting candidates or political parties seen as hostile
to their national interests
► Amplifying social and political divisions within target countries
► Undermining public confidence in election integrity
► Collecting strategic intelligence on policy positions, internal
campaign dynamics, and candidate vulnerabilities
The convergence of generative AI capabilities with the 2024 election
landscape presents a significant concern. Adversaries can leverage
generative AI to scale the production of misleading content, create
convincing deepfake media targeting specific candidates, and automate
the distribution of disinformation across social media platforms with
unprecedented speed and volume.

---

## Table of Contents
- [Foreword](#foreword)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Threat Landscape Overview](#threat-landscape-overview)
- [2023 Themes](#2023-themes)
  - [Identity-Based and Social Engineering Attacks](#identity-based-and-social-engineering-attacks)
  - [Adversaries Continue to Develop Cloud-Consciousness](#adversaries-continue-to-develop-cloud-consciousness)
  - [Third-Party Relationship Exploitation](#third-party-relationship-exploitation)
  - [Vulnerability Landscape: “Under the Radar” Exploitation](#vulnerability-landscape-under-the-radar-exploitation)
  - [2023 Israel-Hamas Conflict: Cyber Operations Focus on Disruption and Influence](#2023-israel-hamas-conflict-cyber-operations-focus-on-disruption-and-influence)
- [Threats on the 2024 Horizon](#threats-on-the-2024-horizon)

---

## Foreword

The 2024 edition of the CrowdStrike Global Threat Report arrives at a pivotal moment for our global community of protectors. The speed and ferocity of cyberattacks continue to accelerate as adversaries compress the time between initial entry, lateral movement and breach. At the same time, the rise of generative AI has the potential to lower the barrier of entry for low-skilled adversaries, making it easier to launch attacks that are more sophisticated and state of the art.

These trends are driving a tectonic shift in the security landscape and the world. The “good enough” approach to cybersecurity is simply no longer good enough for modern threats. As organizations increasingly move business to the cloud, adversaries are advancing their capabilities to exploit this, and abuse features unique to the cloud. We continue to see identity-based attacks take center stage, as adversaries focus on social engineering attacks that bypass multifactor authentication. The use of legitimate tools to execute an attack, an increasingly prevalent technique, impedes the ability to differentiate between normal activity and a breach.

We are entering an era of a cyber arms race where AI will amplify the impact for both the security professional and the adversary. Organizations cannot afford to fall behind, and the legacy technology of yesterday is no match for the speed and sophistication of the modern adversary.

With the release of the CrowdStrike 2024 Global Threat Report, our elite Counter Adversary Operations team is delivering the actionable intelligence you need to stay ahead of today’s threats and secure your future. This year’s report provides critical insight and observations into adversary activity, including:

- The tactics and techniques that adversaries use to exploit gaps in cloud protection
- The continued exploitation of stolen identity credentials and increasingly sophisticated methods adversaries use to gain initial access
- The growing menace of supply chain attacks and exploitation of trusted software to maximize the ROI of attacks
- The potential for adversaries to target global elections in a year that has the potential to transform geopolitics around the world for the near future

From Day One, CrowdStrike has said, “You don’t have a malware problem, you have an adversary problem.” We pioneered the concept of adversary-focused cybersecurity because it’s the best way to protect customers and stop breaches. We know the adversary better than anyone, and we use this insight to guide our innovation, protect customers, stop breaches and increase the cost to the adversary.

A secure future requires a strong foundation. This is what we’re delivering with the AI-native CrowdStrike Falcon® XDR platform. We’re driving the convergence of data, cybersecurity and IT, with generative AI and workflow automation built natively within a single, unified platform to give you and your teams the speed you need to beat the adversary.

I hope you find the CrowdStrike 2024 Global Threat Report informative and inspiring in our shared fight against the adversary. CrowdStrike will remain unrelenting in our mission to deliver the security outcome you need most: stopping the breach.

George Kurtz  
CrowdStrike CEO/Co-Founder

---

## Introduction

As we reflect on the 2023 cyber threat landscape, the theme of stealth prevails. Adversaries have faced a hardening attack surface thanks to advancements in threat defense technology and threat awareness, and they have responded by increasingly adopting and relying on techniques that empower them to move faster and evade detection.

> DATA-THEFT EXTORTION CONTINUES TO BE AN ATTRACTIVE — AND OFTEN EASIER — MONETIZATION ROUTE, AS EVIDENCED BY THE 76% INCREASE IN THE NUMBER OF VICTIMS NAMED ON BGH DEDICATED LEAK SITES

These techniques are evident in the consistent prevalence of eCrime, a highly attractive and lucrative business venture for many criminals. Unsurprisingly, eCrime persisted as the most pervasive threat across the 2023 threat landscape as adversaries leveraged techniques to maximize stealth, speed and impact.

While ransomware remains the tool of choice for many big game hunting (BGH) adversaries, data-theft extortion continues to be an attractive — and often easier — monetization route, as evidenced by the 76% increase in the number of victims named on BGH dedicated leak sites (DLSs) between 2022 and 2023.

Access brokers continued to profit by providing initial access to eCrime threat actors throughout the year, with the number of advertised accesses increasing by 20% from 2022.

Nation-state adversaries were also active throughout 2023. China-nexus adversaries continued to operate at an unmatched pace across the global landscape, leveraging stealth and scale to collect targeted group surveillance data, strategic intelligence and intellectual property.

In other areas of the world, conflict continued to drive nation-state and hacktivist adversary activity. In 2023, as the Russia-Ukraine war entered its second year, Russia-nexus adversaries and activity clusters maintained high, sustained levels of activity in support of Russian Intelligence Service intelligence collection, disruptive activity, and information operations (IO) targeting Ukraine and NATO countries.

Iran-nexus adversaries and Middle East hacktivist adversaries were also observed pivoting cyber operations in the latter half of the year in alignment with kinetic operations stemming from the 2023 Israel-Hamas conflict.

North Korean adversaries maintained a consistently high tempo throughout 2023. Their activity continued to focus on financial gain via cryptocurrency theft and intelligence collection from South Korean and Western organizations, specifically in the academic, aerospace, defense, government, manufacturing, media and technology sectors.

Across the rest of the world, stealth played a key role in adversary activity focused on digital surveillance, information collection and control in support of government agendas. The assessed geographic range of this activity, as well as the capabilities and target scope of global threat actors, continued to underscore the extent to which targeted intrusion capabilities have proliferated beyond those demonstrated by commonly reported countries. In some cases, this activity was assisted by private sector offensive actors and openly available adversary emulation frameworks.

> OVER THE COURSE OF 2023, CROWDSTRIKE CAO INTRODUCED 34 NEW ADVERSARIES — INCLUDING A NEWLY TRACKED, EGYPT-BASED ADVERSARY, WATCHFUL SPHINX — RAISING THE TOTAL NUMBER OF ACTORS TRACKED ACROSS ALL MOTIVATIONS TO 232. IN ADDITION TO NAMED ADVERSARIES, CROWDSTRIKE CAO TRACKS MORE THAN 130 ACTIVE MALICIOUS ACTIVITY CLUSTERS.

One of the greatest threat actor motivations driving stealth in cyber threat operations is CrowdStrike’s development of new products and partnerships throughout 2023. These changed the stakes within the operational landscape and left adversaries with no place to hide.

In 2023, CrowdStrike Falcon® Intelligence and CrowdStrike® Falcon OverWatch™ merged to become CrowdStrike Counter Adversary Operations (CAO). Combining the power of threat intelligence with the speed of dedicated hunting teams and trillions of cutting-edge telemetry events from the AI-native CrowdStrike Falcon® platform that detect, disrupt and stop today’s sophisticated adversaries, this merger has exponentially raised the business cost of conducting cyberattacks.

In 2024, CrowdStrike CAO repackaged CrowdStrike’s threat intelligence modules to add managed threat hunting (an industry first), empowering organizations to better pursue adversaries and stop breaches.

Over the course of 2023, CrowdStrike CAO introduced 34 new adversaries — including a newly tracked, Egypt-based adversary, WATCHFUL SPHINX — raising the total number of actors tracked across all motivations to 232. In addition to named adversaries, CrowdStrike CAO tracks more than 130 active malicious activity clusters.

CrowdStrike CAO drives unparalleled, actionable reporting coverage that captures new cyber threat developments in real time and identifies and tracks new adversaries. The CrowdStrike 2024 Global Threat Report sheds light on the standout trends from last year, how adversaries’ activities and motivations are evolving and the ways CrowdStrike anticipates the threat landscape will evolve in the coming year.

---

## Naming Conventions

| Adversary Nation-State or Category | Code Name |
| :--- | :--- |
| RUSSIA | BEAR |
| VIETNAM | BUFFALO |
| DPRK (NORTH KOREA) | CHOLLIMA |
| ROK (REPUBLIC OF KOREA) | CRANE |
| SYRIA | HAWK |
| HACKTIVIST | JACKAL |
| IRAN | KITTEN |
| PAKISTAN | LEOPARD |
| GEORGIA | LYNX |
| COLOMBIA | OCELOT |
| PEOPLE’S REPUBLIC OF CHINA | PANDA |
| EGYPT | SPHINX |
| ECRIME | SPIDER |
| INDIA | TIGER |
| TURKEY | WOLF |

---

## Threat Landscape Overview

- **+34**: 34 new adversaries tracked by CrowdStrike, raising the total to 232
- **232**: Total adversaries tracked
- **110%**: Cloud-conscious cases increased by 110% YoY
- **75%**: Cloud environment intrusions increased by 75% YoY
- **76%**: YoY increase in victims named on eCrime dedicated leak sites
- **84%**: 84% of adversary-attributed cloud-conscious intrusions were focused on eCrime

Today’s cyber threats are particularly alarming due to the widespread use of hands-on or “interactive intrusion” techniques, which involve adversaries actively executing actions on a host to accomplish their objectives. Unlike malware attacks that depend on the deployment of malicious tooling and scripts, interactive intrusions leverage the creativity and problem-solving skills of human adversaries. These individuals can mimic expected user and administrator behavior, making it difficult for defenders to differentiate between legitimate user activity and a cyberattack.

In 2023, CrowdStrike observed a 60% year-over-year increase in the number of interactive intrusion campaigns, with a 73% increase in the second half compared to 2022.

The technology sector was the most frequently targeted industry in which CrowdStrike CAO observed interactive intrusion activity in 2023, a continuing trend from 2022. 

### Interactive Intrusions by Region
- North America: 61%
- Europe: 11%
- Middle East: 7%
- South Asia: 6%
- Oceania: 5%
- South America: 5%
- East Asia: 4%
- Africa: 1%

### Interactive Intrusions by Industry
- Technology: 23%
- Telecommunications: 15%
- Financial: 13%
- Government: 9%
- Retail: 9%
- Manufacturing: 8%
- Healthcare: 8%
- Services: 6%
- Education: 4%
- Media: 4%

After gaining initial access to a network, adversaries seek to “break out” and move laterally from the compromised host to other hosts within the environment. The time it takes for them to do this — “breakout time” — is crucial because the initially compromised machines are rarely the ones adversaries need to achieve their goals. They must move laterally into the network, conduct reconnaissance, establish persistence and locate their targets. Responding within the breakout time window allows defenders to mitigate costs and other damages associated with intrusions.

This year, the average breakout time for interactive eCrime intrusion activity decreased from 84 minutes in 2022 to 62 minutes in 2023. The fastest observed breakout time was only 2 minutes and 7 seconds.

---

## 2023 Themes

### Identity-Based and Social Engineering Attacks

Adversaries spanning multiple motivations and regions continue to use phishing techniques spoofing legitimate users to target valid accounts, as well as other authentication and identifying data, to conduct their attacks. In addition to stealing account credentials, CrowdStrike CAO observed adversaries targeting API keys and secrets, session cookies and tokens, one-time passwords (OTPs) and Kerberos tickets throughout 2023.

#### Figure 1. Identity-based attack vectors
- **Account Credentials**: Adversaries can authenticate to a system and/or user account using stolen credentials, which can either be obtained by the adversary directly (for example, using information stealers or exploiting unmanaged edge devices) or by purchasing them.
- **API Keys and Secrets**: Access to protected resources using stolen API keys and secrets may allow an adversary to steal sensitive data. Unless the API keys and secrets are changed, the adversary could maintain indefinite access.
- **Session Cookies and Tokens**: Adversaries can steal session cookies and tokens to masquerade as the legitimate user and authenticate to an application.
- **One-Time Passwords (OTP)**: OTP theft allows the adversary to bypass multifactor authentication (MFA) by SIM swapping, SS7 attacks, socially engineering the victim or email compromise.
- **Kerberos and Kerberos Tickets**: By stealing or forging Kerberos tickets, adversaries can gain access to encrypted credentials, which can then be cracked offline. CrowdStrike CAO recorded a 583% increase in Kerberoasting attacks in 2023.

---

### Adversaries Continue to Develop Cloud-Consciousness

> AS PREDICTED, CLOUD ENVIRONMENT INTRUSIONS INCREASED BY 75% FROM 2022 TO 2023 (FIGURE 2), WITH CLOUD-CONSCIOUS CASES INCREASING BY 110% AND CLOUD-AGNOSTIC CASES INCREASING BY 60%.

Cloud-conscious is a term referring to threat actors who are aware of the ability to compromise cloud workloads and use this knowledge to abuse features unique to the cloud for their own purposes.

eCrime adversaries are especially active in targeting cloud environments: 84% of cloud-conscious intrusions attributed to adversaries were conducted by likely eCrime actors, compared to 16% conducted by targeted intrusion actors. Traditional BGH adversaries, such as INDRIK SPIDER, became more cloud-conscious throughout the year.

---

### Third-Party Relationship Exploitation

Throughout 2023, targeted intrusion actors consistently attempted to exploit trusted relationships to gain initial access to organizations across multiple verticals and regions. This type of attack takes advantage of vendor-client relationships to deploy malicious tooling via two key techniques: 
1. Compromising the software supply chain using trusted software to spread malicious tooling
2. Leveraging access to vendors supplying IT services

Threat actors targeting third-party relationships are motivated by the potential return on investment (ROI): One compromised organization can lead to hundreds or thousands of follow-on targets. These stealthy attacks can also more effectively provide an opportunity for attackers seeking to exploit a hardened end target.

---

### Vulnerability Landscape: “Under the Radar” Exploitation

Threat actors have adapted to the enhanced visibility of traditional endpoint detection and response (EDR) sensors by altering their exploitation tactics for initial access and lateral movement. They are now targeting the network periphery, where defender visibility is reduced by the possibility that endpoints may lack EDR sensors or cannot support sensor deployment.

> UNMANAGED NETWORK APPLIANCES — PARTICULARLY EDGE GATEWAY DEVICES — REMAINED THE MOST ROUTINELY OBSERVED INITIAL ACCESS VECTOR FOR EXPLOITATION DURING 2023.

> THREAT ACTORS ARE ACTIVELY DEVELOPING EXPLOITS FOR EOL PRODUCTS THAT CANNOT BE PATCHED AND OFTEN DO NOT ALLOW FOR MODERN SENSOR DEPLOYMENT.

---

### 2023 Israel-Hamas Conflict: Cyber Operations Focus on Disruption and Influence

On October 7, 2023, Hamas military wing Izz al-Din al-Qassam Brigades (IDQB) and several other Gaza-based militant groups launched a massive kinetic attack against Israel, killing hundreds of Israelis and taking hostages. In the ensuing months, CrowdStrike CAO tracked ongoing cyber operations from targeted intrusion and hacktivist actors. Activity and claims from both groups primarily focus on targeting operational technology or other critical systems — likely to psychologically influence target populations — and deploying destructive wipers against Israeli or Israel-linked entities.

Most conflict-driven cyber operations observed include hacktivist activity and operations by suspected faketivists. Within the context of the Israel-Hamas conflict, the dividing line between these two threat actor types has blurred, as genuine hacktivist groups often amplify the claims of, or provide support to, likely state-nexus inauthentic personas.

---

## Threats on the 2024 Horizon

As organizations plan for potential threats emerging in 2024, two potential disruption drivers come to the forefront: generative AI and 2024 global government elections.

### Generative AI Use Within the Threat Landscape

Mainstream accessible generative AI technology exploded in late 2022, opening up a new realm of possibilities for efficient content creation and drawing the attention of adversaries seeking ways to exploit this new technology for their own purposes.

Generative AI has massively democratized computing to improve adversary operations. It can also potentially lower the entry barrier to the threat landscape for less sophisticated threat actors.

> GENERATIVE AI HAS MASSIVELY DEMOCRATIZED COMPUTING TO IMPROVE ADVERSARY OPERATIONS. IT CAN ALSO POTENTIALLY LOWER THE ENTRY BARRIER TO THE THREAT LANDSCAPE FOR LESS SOPHISTICATED THREAT ACTORS.

Two primary generative AI opportunity areas within the threat landscape include:
- Developing and/or executing malicious computer network operations (CNO), including tool and resource development such as scripts or code that could be functionally malicious if used correctly
- Supporting the efficiency and effectiveness of social engineering and information operations campaigns

---

[^1]: Footnote content here.

---

he Azure Portal.
In addition to visiting ChatGPT while browsing the Azure
Portal — presumably to understand how to navigate in
Azure — browsing activity analysis indicates INDRIK SPIDER
used search engines such as Google and Bing and searched
on GitHub during the operations to understand how to
exfiltrate Azure Key Vault credentials.
Using search engines and visiting ChatGPT indicate that
though INDRIK SPIDER is likely new to the cloud and not yet
sophisticated in this domain, it is using generative AI to fill
these knowledge gaps.
SCATTERED
SPIDER
In the second half of 2023, SCATTERED SPIDER used the
Azure AD PowerShell module to download all Entra ID
user immutable IDs at a North American financial services
victim. Using its Entra ID backdoor, the adversary could log
in as any of the downloaded users. The PowerShell used
to download the users’ immutable IDs resembled large
language model (LLM) outputs such as those from ChatGPT.
In particular, the pattern of one comment, the actual
command and then a new line for each command
matches the Llama 2 70B model output.
Based on the similar code style, SCATTERED SPIDER
likely relied on an LLM to generate the PowerShell script
in this activity.

2024 GLOBAL THREAT REPORT CrowdStrike 34
Generative AI in Social Engineering
and Information Operations
In recent years, certain language models have been able to compose fictional stories5 and generate digital
artwork.6 Since at least mid-2021, CrowdStrike has frequently reported on alleged research interest in highly
deceptive AI-fabricated images, audio and video (aka “deepfakes”) by Russia, China and Iran. Researchers
and academics have further speculated that threat actors will almost certainly use generative AI tools in
information and influence operations in the near future.7
These speculations began actualizing in 2023: A Chinese information operations campaign, likely reliant
on images produced by generative AI (specifically diffusion-model-generated images), gained authentic
engagement across several prominent social media platforms throughout September. Beyond state-nexus
actors, CrowdStrike also observed a hacktivist group attempting to create a spam tool using generative AI as
part of its efforts to disseminate pro-Azerbaijan messaging.
Outlook
Generative AI has potential for use in numerous fields not likely identified or popularized in mainstream public
discourse. AI’s continuous development will undoubtedly increase the potency of its potential misuse —
particularly within the scope of information operations and especially for less digitally literate audiences. The
degree to which popular generative AI tools can be used maliciously will likely adapt over time as companies,
tool owners and governments respond to new developments and perceived misuse.
CrowdStrike CAO assesses that generative AI will likely be used for cyber activities in 2024 as the technology
continues to gain popularity. The team will track exactly how threat actors use this technology, and how this
use differs from mainstream applications, throughout 2024. This type of research includes examinations of
both:
► The potential that adversaries will use publicly available or open-source LLMs, which will likely require
continual adversary navigation around safeguards against malicious or illegal activity (e.g., jailbreaking).
► Adversaries’ attempts to develop their own models or generative AI tools that require less prompt
engineering. Notably, the cost of training LLMs can significantly deter their independent, illicit
development. Threat actors’ attempts to craft and use such models in 2023 frequently amounted to scams
that created relatively poor outputs and, in many cases, quickly became defunct.
5 https://apnews.com/article/7f49bd9aa9d1427d8400e40beb9f5ba4
6 https://apnews.com/article/artificial-intelligence-images-rights-1c6d9e0e260e2d135a3e3bf98d5493df
7 https://cdn.openai.com/papers/forecasting-misuse.pdf

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 35
2024 Elections
In 2024, individuals from 55 countries representing more than 42% of the global
population will participate in presidential, parliamentary and/or general elections.
This includes seven of the 10 most populous countries in the world: India, the U.S.,
Indonesia, Pakistan, Bangladesh, Russia and Mexico. High-profile, national-level
elections will also occur in countries or groups involved in, or proximal to, major
geopolitical conflicts. These include Taiwan, Azerbaijan, India, Pakistan, Iran, Belarus,
Russia, Finland, Lithuania and the European Union.
2024’s potential to transform geopolitics around the globe for the near future will
likely give adversaries numerous opportunities, and a considerable strategic impetus,
to target entities involved in electoral processes throughout the coming year.
Election Targeting
Cyber activity targeting elections can range from direct attempts to disrupt electoral
»
processes to more indirect efforts to sway voter opinion toward outcomes preferred
by the adversary.8 The most direct, but least frequent, targeting involves intrusions
IN 2024, INDIVIDUALS FROM
against the software and hardware used to record, tally, count and transmit votes in
55 COUNTRIES REPRESENTING
voting systems. This form of election interference can range from using computer
MORE THAN 42% OF THE GLOBAL
network attacks to intentionally disrupt, degrade or destroy voting systems to using
POPULATION WILL PARTICIPATE IN
privileged access or vulnerabilities to attempt to alter vote counts without detection.
PRESIDENTIAL, PARLIAMENTARY
AND/OR GENERAL ELECTIONS. THIS
Less direct forms of targeted intrusion can involve attempts to compromise, disrupt
INCLUDES SEVEN OF THE 10 MOST
access to or leak data from government systems that provide logistical information to
POPULOUS COUNTRIES IN THE WORLD
voters, store voter registration data or otherwise support transparent and democratic
election conduct. These targeted intrusion efforts include using DDoS attacks or
website defacements against local, municipal, provincial and state government
systems, a tactic historically favored by hacktivists seeking to espouse their
viewpoints during tense political moments. Other parties involved in elections —
such as political candidates, parties, donors and advocacy groups — can also be
targeted in a variety of ways, including via the use of hack-and-leak operations
often designed to publicly discredit the target.
The least direct type of election targeting — but almost certainly the most
common and typically the most difficult to prevent — involves distributing mis- or
disinformation to electorates before, during and after voting processes in an effort
to influence popular opinion.
These information operations can take many forms. One common theme involves
attempts to generate disruptive narratives — for example, they may undermine public
confidence in election outcomes, enhance perceptions that specific political parties
or individuals are corrupt, impugn candidates’ personal character or disseminate
inflammatory and polarizing social rhetoric. Other operations may aim to reinforce
perspectives that portray the threat actor responsible in a more positive light;
for example, as an advocate for specific policy positions beneficial to that entity
or representative of cooperation or coexistence rhetoric.
8 Though this section details the actions of external malicious actors targeting elections, it is worth
noting that ostensibly democratic governments sometimes also use their own domestic security authorities
to legally restrict the free flow of information during election cycles (e.g., internet shutdowns and censorship).

2024 GLOBAL THREAT REPORT CrowdStrike 36
Threat Highlight:
Iranian Targeting of U.S.
Elections in 2020
In late October 2020, a few weeks before the last U.S. presidential election cycle,
Iranian threat actors conducted varied targeted IO against U.S. entities. They sent
threatening emails to voters, alleging to represent a far-right U.S. political group
and directing recipients to vote for a specific candidate. Iranian threat actors also
disseminated a video falsely alleging to depict overseas actors fabricating ballots,
implying one particular political party would seek to exploit security vulnerabilities
and compromise voting systems.
Outlook
The most common malicious activities targeting elections have historically
involved information operations likely conducted by state-nexus entities against
citizens of countries that hold specific geopolitical interest to the threat actor
and simple, short-lived hacktivism — including DDoS attacks and website
defacements — against state and local government entities. This trend is
highly likely to continue in 2024.

| CROWDSTRIKE 2024 GLOBAL THREAT REPORT |     |     |     |     |     |     |     |     |     | 37  |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EUROPEAN UNION
6 JUNE
BANGLADESH 7 JANUARY
TBD 2024
| B H U T A N    |            |     |     |     |     |     |     |     | V e n e z u e la    |     |
| -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
| 9  J AN U A RY |            |     |     |     |     |     |     |     | S o u th   A fr ica |     |
| TAIWAN         |            |     |     |     |     |     |     |     | Tunisia             |     |
| 13 JANUARY     |            |     |     |     |     |     |     |     | South Sudan         |     |
| COMOROS        |            |     |     |     |     |     |     |     | Austria             |     |
| 14 JANUARY     |            |     |     |     |     |     |     |     | Moldova             |     |
|                | FINLAND    |     |     |     |     |     |     |     | Namibia             |     |
|                | 28 JANUARY |     |     |     |     |     |     |     | Guinea-Bissau       |     |
|                | TUVALU     |     |     |     |     |     |     |     | North Macedonia     |     |
26 JANUARY
EL SALVADOR
4 FEBRUARY
|     | AZERBAIJAN       | SLOVAKIA         |     |     |              |            |     |     |     |     |
| --- | ---------------- | ---------------- | --- | --- | ------------ | ---------- | --- | --- | --- | --- |
|     | 7  F E BR UA R Y | T B D  M A RC H  |     |     | I C E L A ND | R W A N DA |     |     |     |     |
|     |                  | S R I  L A N K A |     |     | 1  J U N E   | 15  J U LY |     |     |     |     |
P 8 FE A K B IS R T U A A R N Y T B D   M A R C H A L G E R I A
T O G O SOLO M O N  I S L ANDS M 2  E JU X N IC E O TB D  D E C E M B ER
I 1 N 4   D F O E B N R E UA S R I Y A T B D   M a r c h T B D  AP R I L B ELGIUM C R O A T I A
|     |     | B E L A R U S | I N D I A |     | 9 JUNE |     |     |     | T B D   D E C E M B | E R |
| --- | --- | ------------- | --------- | --- | ------ | --- | --- | --- | ------------------- | --- |
2 5   F E B R U A R Y TB D   A P R I L C H A D R O M A N I A S A N   M A R I N O
|     |     |     | S O U T H  KOREA | MAD A G A S CAR |     |     | B T O B D T   S O C W T A O B N E R A | T BD  N O V E M B E R | T B D   D E C E M B | E R |
| --- | --- | --- | ---------------- | --------------- | --- | --- | ------------------------------------- | --------------------- | ------------------- | --- |
S 2 5 E   N F E E B G R U A A L R Y 1 0   A P R IL T BD   MA Y T B D   O C T O B E R U N I T E D   STATES
|     |     |     |     |     |     |     |     | 5 N O V E M B E R | M A U R IT I U S |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------------- | --- |
C A M B O D I A R U S S I A P 5  A M N A Y A M A M A U R I T A N IA M O Z A M B I Q U E 30  N O VE M B E R
25  F E B R U A R Y 1 7   MA R C H 22   J U N E 9  OC T OB E R G E O R G I A P 1 2 A   L N A O V U E MBER G H A N A
I R A N L I T H U A N I A N O   E L E C T I O N S   2 6   O C T O B E R 7   DE C EM BER
|     |     | 1   M A R CH P O R T U G A L |     | 1 2   M A Y D O M I N | IC AN M 2 8 O   J N U | N G E O LIA A N N | O U C E D U | R U G U A Y |     |     |
| --- | --- | ---------------------------- | --- | --------------------- | --------------------- | ----------------- | ----------- | ----------- | --- | --- |
MALI 10  M A R C H RE P U B L IC YE T   F OR   A U G- S E P 2 7   O C T O B E R
|     | TBD FEBRUARY |     |     | 19 MAY |     |     |     |     |     |     |
| --- | ------------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
JANUARY FEBRUARY MARCH APRIL MAY JUNE JULY OCTOBER NOVEMBER DECEMBER
Figure 6. Countries holding presidential, parliamentary or general elections in 2024
In 2024, countries of interest involved in election  The overall polarization of the political spectrum in many
cycles will likely be at risk of significant and lengthy IO  countries amid continuing economic and social issues
campaigns from major global powers. Russia and Iran  will likely increase the susceptibility of those countries’
will likely leverage IO against the U.S. and the EU, which  citizenries to IO — particularly IO campaigns targeted at
they consider major geopolitical opponents.  reinforcing those individuals’ negative opinions of political
opponents.10
China will also likely conduct IO against elections held
in its perceived regional sphere of influence, such as  Additionally, changes to or staff reductions affecting the
those in Indonesia, South Korea and Taiwan. Russia will  enforceability of content moderation policies at major
almost certainly behave similarly in elections occurring  social media companies will likely provide opportunities
in Belarus, Lithuania, Finland and Georgia. India and  for adversary exploitation using these platforms to
Pakistan are highly likely to conduct significant IO  disseminate IO narratives.11
campaigns against one another during their respective
elections in April and February 2024, particularly given
With such political environments currently existing in
the current political upheaval and polarization in both  most of the large and geopolitically significant countries,
countries.9 2024 will almost certainly present a challenging global
test for democracies.
Given the ease with which AI tools can generate
deceptive but convincing narratives, adversaries will
| highly likely use such tools to conduct IO against  |     |     |     |     |     | »   |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
elections in 2024. Politically active partisans within those
countries holding elections will also likely use generative
RUSSIA AND IRAN WILL LIKELY
AI to create disinformation to disseminate within their
LEVERAGE IO AGAINST THE U.S.
| own circles. |     |     |     |     |     | AND THE EU, WHICH THEY CONSIDER  |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- |
MAJOR GEOPOLITICAL OPPONENTS.
These issues were already observed within the
first few weeks of 2024, as Chinese actors used
AI-generated content in social media influence campaigns
to disseminate content critical of Taiwan presidential
election candidates.
9  https://www.eastasiaforum.org/2024/01/06/military-influence-and-political-peril-in-pakistan/
  https://foreignpolicy.com/2024/01/02/india-elections-modi-bjp-congress-nda-lok-sabha-brics/
10  https://www.cambridge.org/core/journals/american-political-science-review/article/abs/partisan-polarization-is-the-primary-psychological-motivation-
behind-political-fake-news-sharing-on-twitter/3F7D2098CD87AE5501F7AD4A7FA83602
11  https://www.theguardian.com/media/2023/dec/07/2024-elections-social-media-content-safety-policies-moderation

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 38
eCrime
Landscape
The CrowdStrike eCrime Index® (ECX) tracks activity — including the number
of observed spam emails and the average cost of buying access to a corporate
network — across multiple eCrime ecosystem segments and calculates the total
number of observed ransomware victims.
Until May 2023, the ECX exhibited trends similar to those observed in 2022. New Vulnerabilities with
However, from June 2023 onward, the ECX grew significantly, with major spikes 9/10 CVSS3 Score
between June and August. The most impactful contributors to these spikes
+6%
included high BGH incident frequency and a sudden increase in observed DDoS
attacks.
BGH Incidents Involving
The ECX spiked again in November 2023, reflecting increases in spam email Data Leaks
numbers and the rising average price for loaders and stealers. +76%
Average Loader Cost
+169%
+67%
2023
ECX Value= Average Crypter Cost
+250%
2022
Average Stealer Cost
100
+286%
75 Average Ransom
Demand
-27%
50
Identified Spam
25 Emails
-15%
0
JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC
Figure 7. eCrime index value, 2022 vs. 2023, and key observable changes, 2023

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 39
The 2023 ECX tracked the most annual activity to date, representing the index’s
year-over-year growth. Spam emails likely decreased in 2023 as adversaries
searched for other means of initial access and after a multinational operation shut
down MALLARD SPIDER’s QakBot.
Though the average ransom demand was lower in 2023 than in 2022, this highly
likely represents an outlier in the dataset and not an accurate view of the threat
landscape. Ransom demands have likely remained consistently high throughout
this period, but the ability to track these values is becoming challenging due to
threat actors and victims implementing stricter privacy measures around ransom
price demands and payments.
BIG GAME HUNTING
2023 BGH DLS Statistics
»
The number of victims named on BGH dedicated leak sites increased significantly
in 2023, with 4,615 victim posts made to DLSs — a 76% increase over 2022.
THE NUMBER OF VICTIMS NAMED
Several factors contributed to this growth, including newly emerged BGH
ON BGH DEDICATED LEAK SITES
adversaries, growth of existing adversary operations and select high-volume
INCREASED SIGNIFICANTLY IN
campaigns such as multiple GRACEFUL SPIDER zero-day exploitations.
2023, WITH 4,615 VICTIM POSTS
MADE TO DLSs — A 76% INCREASE
DLS Post Quantity
OVER 2022.
2022 vs. 2023
800
600
2023
400
200
2022
0
JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC
Figure 8. DLS post quantity, 2022 vs. 2023
Collectively, BITWISE SPIDER, ALPHA SPIDER, GRACEFUL SPIDER, RECESS SPIDER
and BRAIN SPIDER accounted for 77% of posts across all tracked adversary DLSs.
BITWISE SPIDER and ALPHA SPIDER have historically posted numerous new DLS
posts and were ranked in first and second place, respectively, for the highest
number of DLS posts in 2022 and 2023.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 40
RECESS SPIDER and BRAIN SPIDER started their own ransomware operations in
mid-2022 and January 2023, respectively. They have since grown in prominence
to account for the fourth (RECESS SPIDER) and fifth-highest (BRAIN SPIDER)
number of DLS posts in 2023.
GRACEFUL SPIDER — which has operated since 2016 and has typically conducted
low-volume campaigns — exploited three zero-day vulnerabilities in 2023 to
exfiltrate data from hundreds of victims across the globe. This adversary ultimately
published the third-highest number of DLS posts in 2023.
Top Adversaries by DLS Post
1250
1000
750
500
250
0
BITWISE ALPHA GRACEFUL RECESS BRAIN
SPIDER SPIDER SPIDER SPIDER SPIDER
Figure 9. Top five adversaries by DLS posts, 2023
SCATTERED SPIDER Adopts Ransomware
as Primary Monetization Method
SCATTERED SPIDER began using ALPHA SPIDER’s Alphv ransomware in April 2023.
The adversary had previously monetized intrusions by selling victim data and SIM
swaps as well as stealing cryptocurrency. Adopting ransomware as its primary
means of extortion has shifted the scope of the adversary’s target profile: Most
SCATTERED SPIDER victims in 2023 can be categorized as either reconnaissance
targets or monetization targets. Reconnaissance targets are typically organizations
in the business process outsourcing, customer relationship management, customer
experience, technology and telecom sectors. SCATTERED SPIDER uses intrusions
into these entities’ networks to identify data that may prove useful in downstream,
third-party monetization targeting.
The adversary’s monetization target profile is considerably broader. Most directly
observed targets include high-revenue — often Fortune 500 — U.S.-based private
sector entities. A notable uptick in North American financial services victims
occurred in the second half of 2023.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 41
Law Enforcement Activity Targets
BGH Adversaries
In 2023, various law enforcement agencies targeted BGH adversary operations
and their supporting campaigns. Their actions ranged from arresting suspected
adversary personnel to technically disrupting adversary infrastructure.
2023
Seizure of HIVE SPIDER infrastructure and acquisition of
JAN
Hive ransomware decryption keys
FEB
Sanctions issued targeting members of WIZARD SPIDER
Europol announced the arrest of two suspected core
MAR
members of DOPPEL SPIDER
JUN DOJ announced the arrest of a suspected
BITWISE SPIDER affiliate
Seizure and shut down of MALLARD SPIDER’s QakBot
AUG
infrastructure
SEP
Sanctions issued targeting members of WIZARD SPIDER
OCT
VIKING SPIDER DLS takedown and arrests
Europol announced the arrest of individuals connected to
NOV
several ransomware programs
Seizure of ALPHA SPIDER infrastructure and acquisition of
DEC
Aplhv ransomware decryption keys
Figure 10. Law enforcement activity against BGH and supporting operations, 2023

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 42
In January 2023, a coordinated international law enforcement operation resulted in
the seizure of HIVE SPIDER infrastructure and acquisition of the Hive ransomware
decryption key. The U.S. Department of Justice (DOJ) has reportedly maintained
access to HIVE SPIDER’s internal infrastructure since July 2022 and has since
provided decryption keys to more than 300 worldwide victims, preventing
ransom payments totaling 130 million USD. No HIVE SPIDER activity has been
observed since January 2023; however, Hive affiliates have since migrated to other
ransomware as a service (RaaS) operations.
In February and September 2023, law enforcement issued sanctions against
WIZARD SPIDER members aiming to restrict the named individuals’ finances, travel,
and assets and disrupt the adversary’s operations as it worked to circumvent the
restrictions.
In March 2023, Europol announced the arrest of two suspected core DOPPEL
SPIDER members. In June 2023, the DOJ announced the arrest of a suspected
BITWISE SPIDER affiliate. In August 2023, the FBI announced a multinational
operation — using a custom payload to send a shutdown command — that
removed MALLARD SPIDER’s QakBot malware from more than 700,000 hosts and
seized a significant amount of cryptocurrency. WANDERING SPIDER also used
MALLARD SPIDER’s QakBot.
In October 2023, law enforcement agencies announced they had taken down
VIKING SPIDER’s Ragnar Locker DLS and arrested a suspected Ragnar Locker
developer. In November 2023, Europol also announced it had arrested personnel
connected to an unnamed ransomware actor. Finally, in December 2023, the FBI
seized ALPHA SPIDER’s infrastructure, including the Alphv DLS — ransomware
SCATTERED SPIDER used throughout most of 2023.
The FBI offered an Alphv decryption tool to more than 500 ALPHA SPIDER victims,
prompting ALPHA SPIDER to migrate its DLS and affiliate panel to new Tor sites
while it attempted to regain control of its compromised infrastructure. ALPHA
SPIDER then removed targeting restrictions from affiliates, excepting prohibition
against targeting entities within the Commonwealth of Independent States.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 43
Data Theft and Extortion Optimization
Since 2019, BGH adversaries have threatened to publish stolen data on DLSs as
a secondary extortion means in concert with deploying ransomware.12 In 2023,
adversaries continued to invent exploitation methods to steal victim data and
increase pressure on victims, with many — including GRACEFUL SPIDER and
MASKED SPIDER — adopting data theft as their sole means of extortion.
GRACEFUL SPIDER was the most prolific data theft and extortion actor in 2023.
The adversary exploited zero-day vulnerabilities in file-transfer applications
GoAnywhere Managed File Transfer and MOVEit Transfer as well as IT
management software SysAid On-Premise. GRACEFUL SPIDER’s Clop ransomware
deployment within the scope of these campaigns was not observed, although the
adversary exfiltrated and published data to its DLS that belonged to more than
380 victim organizations. To allow broader audience access to leaks, GRACEFUL
SPIDER also published victim data on clearweb domains, a technique first used by
an ALPHA SPIDER affiliate in 2022.
BGH adversaries have historically and indiscriminately exfiltrated and published
stolen victim data. In 2023, these threat actors demonstrated greater focus on
stolen data in efforts to maximize pressure on victims, as shown by the following:
► Publishing victim Domain Admin credentials and system IP addresses on the
Black Basta RaaS DLS. This data could be leveraged by distinct threat actors to
target victim organizations.
► Creating separate victim posts for third-party organizations whose data was
identified in the victim network but were not subjected to compromises.
► Multiple RaaS affiliates compromised mental and physical healthcare entities
and highlighted their access to — and provided previews of — sensitive data
and records, including patient photos, in DLS posts.
► VICE SPIDER continued to use a PS script to automate data exfiltration
but customized the script to search for directory and filenames containing
strings such as *violence*, *abuse*, *Theft*, *Stealing*,
*humiliation*, *harassment* and *death*, likely to identify data that
posed a high potential for embarrassing victim organizations.
Many adversaries, including GRACEFUL SPIDER and MASKED SPIDER, have
struggled with cryptographic flaws in their ransomware that enable trivial
decryption under specific conditions. In contrast, data theft and extortion offer
BGH actors an easier route to monetization, and many simply steal data from a
single host or public-facing application. CrowdStrike CAO assesses that BGH
adversaries will likely continue to become more targeted in their pursuit of data
with a high potential for embarrassing victims.
12 https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 44
Outlook
»
The record number of victims named on DLSs throughout 2023 demonstrates
BGH’s status as the current most significant eCrime threat to organizations across
THE RECORD NUMBER OF VICTIMS
all geographical regions and industries. This increase is driven by various factors,
NAMED ON DLSs THROUGHOUT 2023
including GRACEFUL SPIDER’s zero-day exploitation campaigns, BGH adversaries’
DEMONSTRATES BGH’S STATUS AS
continued targeting of unmanaged devices — such as edge gateway devices
THE CURRENT MOST SIGNIFICANT
for initial access and targeting VMware ESXi for encryption — and an increasing
ECRIME THREAT TO ORGANIZATIONS
number of adversaries naming victims following data theft incidents that did not
ACROSS ALL GEOGRAPHICAL REGIONS
include ransomware deployment.
AND INDUSTRIES.
Though CrowdStrike CAO assesses that ransomware will highly likely remain
the primary extortion method through 2024, BGH adversaries will increasingly
emphasize stolen-data exploitation as a means to pressure victims into payment.
This is particularly true as U.S. Securities and Exchange Commission (SEC) rules
impact major cybersecurity incident disclosures.13
SCATTERED SPIDER’s Alphv ransomware underscored the effectiveness of
extortion as a tactic throughout 2023. Though SCATTERED SPIDER previously
monetized campaigns through cryptocurrency theft and SIM swaps, ransomware
is a more opportunistic tactic, enabling the adversary to broaden its target
scope. Barring any successful law enforcement activity targeting the adversary,
SCATTERED SPIDER will highly likely remain a critical threat to high-revenue
private sector entities in 2024, particularly those based in Europe and North
America.
Coordinated international law enforcement operations targeted BGH actors in
2023. These included adversary personnel arrests, technical action against
various capabilities, cryptocurrency seizure and sanctioning of named individuals.
The disruption of HIVE SPIDER’s Hive RaaS and MALLARD SPIDER’s enabling QakBot
malware left voids that were quickly filled by competing RaaS and malware as a
service (MaaS) actors, demonstrating the eCrime ecosystem’s resilience against
takedowns that do not arrest the individuals behind the operations.
13 https://www.sec.gov/news/press-release/2023-139

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 45
eCRIME ENABLERS
Malware Delivery Trends Following
Mark-of-the-Web Patch on ISO Files
Adversaries in 2023 experimented with malware delivery methods that do not
rely on macros or ISO files, following a sharp increase in ISO files being used for
malware delivery and a subsequent patch by Microsoft for a Mark-of-the-Web
bypass vulnerability in container files in 2022.
The number of malware campaigns using malicious OneNote files for initial
access rose significantly14 between late December 2022 and March 2023, with
the technique’s earliest adopters including criminals distributing information
stealers and commodity malware. By mid-January 2023, large-scale malware
distributors such as LUNAR SPIDER, HONEY SPIDER and MALLARD SPIDER began
using OneNote files as a primary malware distribution method. In March 2023,
Microsoft announced a change that would prevent file types commonly abused by
adversaries from being embedded in OneNote files.15 Following the announcement,
the popularity of OneNote files within adversary campaigns rapidly declined.
Though no one technique has emerged as a front-runner to replace OneNote files,
adversaries continue to experiment with malware delivery methods. Adversaries
such as LUNAR SPIDER, APOTHECARY SPIDER and HERMIT SPIDER have
consistently used malvertising and search engine optimization (SEO) poisoning.
Adversaries reliant on spam campaigns use multiple techniques and file types to
deliver malware. Several adversaries have used PDF files containing links to files
hosted on external URLs as well as HTML smuggling. More novel techniques
have included using WebDAV files to distribute payloads. Toward the end of
2023, multiple malware families were distributed in new lures containing fake
browser updates.
Malvertising and SEO Poisoning
Malvertising is a technique in which threat actors create malicious advertisements
to facilitate criminal activity. Adversaries use SEO poisoning to falsely promote
malicious websites to higher ranks in search engine results. Similar to malvertising,
SEO poisoning relies on users believing the results closest to the top of a search
result are the most credible.
Throughout 2023, adversaries such as LUNAR SPIDER regularly abused Google
advertisements to ensure their malicious ads appeared at the top of search result
pages. Threat actors such as SolarMarker operators regularly used SEO poisoning
throughout 2023.
14 https://www.crowdstrike.com/blog/qakbot-ecrime-campaign-leverages-microsoft-onenote-for-distribution/
15 https://learn.microsoft.com/en-us/deployoffice/security/onenote-extension-block

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 46
Increasing macOS Malware Use
»
Throughout 2023, multiple macOS malware variants — including MacOS
Stealer, Private MacOS Stealer, ShadowVault and COOKIE SPIDER’s Atomic macOS
ACCESS BROKERS CONTINUED TO
Stealer (AMOS) — emerged on underground marketplaces. All observed
PROFIT FROM PROVIDING INITIAL
macOS malware families are information stealers capable of harvesting
ACCESS TO A VARIETY OF eCRIME
stored passwords, cookies and cryptocurrency wallets.
THREAT ACTORS IN 2023, WITH THE
NUMBER OF ACCESSES ADVERTISED
AMOS customers have distributed these tools via SEO poisoning as well as
INCREASING BY 20% COMPARED
fake play-to-earn games and illegitimate job advertisements. MacOS Stealer
TO 2022.
customers, including BITWISE SPIDER, ROYAL SPIDER and ALPHA SPIDER
ransomware affiliates, have praised the stealer. Although COOKIE SPIDER
stated that a portion of its current 50 to 100 customers include BITWISE
SPIDER and ALPHA SPIDER affiliates, CrowdStrike CAO cannot presently
verify this claim.
macOS stealers gained traction in the eCrime ecosystem throughout
2023 due to their ability to enable opportunistic actors and ransomware
affiliates during criminal operations. Since the majority of information
stealers typically target Windows-based OSs, the increasing number of
macOS stealers in the eCrime ecosystem has expanded eCrime profit
opportunities.
Access Brokers Persistently Provide
Access Opportunities
Access brokers continued to profit from providing initial access to a variety
of eCrime threat actors in 2023, with the number of accesses advertised
increasing by 20% compared to 2022. The academic sector was the most
frequently advertised, and advertisements for U.S.-based entities far
surpassed all other regions. Initial access TTPs observed in 2023 were
relatively consistent with those used in 2022 and regularly targeted and
abused compromised credentials.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 47
TOP ACCESS BROKER
ADVERTISEMENTS BY COUNTRY
2023
70 928
TOP SECTORS ADVERTISED
BY ACCESS BROKERS | 2023
ACADEMIC
RETAIL
PROFESSIONAL SERVICES
TECHNOLOGY
MANUFACTURING
INDUSTRIALS
FINANCIAL SERVICES
HEALTHCARE
TELECOMMUNICATIONS
MEDIA
INCIDENT COUNT
Figure 11. Top 10 countries and sectors advertised by access brokers, 2023
ROTCES

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 48
Outlook
The rise of macOS malware and the evolution of malware delivery techniques
demonstrate the eCrime ecosystem’s innovative nature. Furthermore, eCrime
enablers regularly copy successful tactics used by other criminal actors, as made
evident by the increase of OneNote files for malware delivery.
eCrime enablers will highly likely continue to innovate and offer new products on
criminal marketplaces in 2024. This assessment is made with high confidence
based on historical trends in the eCrime ecosystem. Malware delivery trends will
likely continue to fluctuate, with SEO poisoning and malvertising remaining popular
and spam-reliant adversaries proceeding to regularly experiment with different
methods. This assessment is made with high confidence based on malware
delivery trends observed since the end of 2022.
The access broker threat shows no immediate sign of abating. These threat actors
will almost certainly facilitate intrusions into various organizations worldwide
throughout 2024 using a mixture of established TTPs alongside commodity and
custom tooling.
TARGETED eCRIME
Adversaries Continue Legitimate
RMM Tool Use
Throughout 2023, multiple targeted eCrime adversaries — particularly CHEF SPIDER, DISTANT SPIDER and SOLAR
SPIDER — heavily used legitimate remote monitoring and management (RMM) tools.
Starting in March 2023, CHEF SPIDER adopted sophisticated social engineering tactics to direct victims to download
Inno Setup and ClickOnce installers for RMM tool ConnectWise ScreenConnect. Though CHEF SPIDER has historically
targeted point-of-sale systems in the hospitality sector by compromising internet-facing servers, the adversary gradually
shifted to targeting U.S.-based hospitality sector service providers, financial service providers and digital marketing firms
throughout 2023.
In 2023, DISTANT SPIDER — which universally relies on ConnectWise ScreenConnect — continued deploying MSI
installers (aka Windows Installers) for this legitimate RMM tool after exploiting vulnerable internet-facing servers within
victim environments. In September 2023, an earlier DISTANT SPIDER ConnectWise ScreenConnect intrusion likely
enabled an ALPHA SPIDER affiliate to exfiltrate data and demand a ransom from a victim.
In June 2023, SOLAR SPIDER likely used phishing emails to direct victims to download a ZIP archive hosted on GitHub.
This archive contained a loader that abuses DLL search-order hijacking to run the legitimate RMM Remote Management
System tool. SOLAR SPIDER has used the legitimate RMM tool NetSupport Manager since at least October 2022.

| CROWDSTRIKE 2024 GLOBAL THREAT REPORT |     |     |     |     | 49  |
| ------------------------------------- | --- | --- | --- | --- | --- |
Historical CARBON SPIDER Malware
Distributed in Low-Volume Campaigns
Throughout 2023, eCrime actors used numerous malware families previously exclusive to
CARBON SPIDER (Figure 12). Since the now-inactive MaaS vendor Goodsoft distributed
these families in 2022 and 2023, none of these campaigns can be attributed to now-inactive
CARBON SPIDER; however, the campaigns demonstrate the tools’ enduring popularity. In
contrast to typical MaaS operators, the low volume of campaigns using Goodsoft tooling
likely indicates only a handful of customers were given access.
LIZAR STAGER
|     | Lizar Stager |       | Nemesis Loader |     |     |
| --- | ------------ | ----- | -------------- | --- | --- |
|     | Demux        | Sekur | NextGeneration |     |     |
|     | Stager       | RAT   | Loader         |     |     |
Figure 12. Legacy CARBON SPIDER tooling used in 2023

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 50
Additional LATAM-Focused
Adversaries Identified
In 2023, CrowdStrike CAO named three new SPIDER adversaries focused
primarily — but not exclusively — on Latin America (LATAM): ODYSSEY SPIDER,
ROBOT SPIDER and SQUAB SPIDER (Figure 13). Including previously identified
BLIND SPIDER, four SPIDER adversaries now focus on LATAM targeting.
SQUAB SPIDER
ORIGIN: UNKNOWN
KEY
TARGETED SECTORS
FINANCIAL SERVICES
RETAIL
HOSPITALITY
TECHNOLOGY
TRAVEL
AUTOMOTIVE
ENTERTAINMENT
GOVERNMENT
ODYSSEY SPIDER
MANUFACTURING BLIND SPIDER ORIGIN: BRAZIL
ORIGIN: COLOMBIA
REAL ESTATE
TRANSPORTATION
TARGETED BY:
ROBOT SPIDER
ORIGIN: BRAZIL
SQUAB SPIDER
ODYSSEY SPIDER
BLIND SPIDER
Utilizes ROBOT SPIDER's Fsociety tooling
Figure 13. LATAM-focused SPIDER adversaries

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 51
AVIATOR SPIDER, BLIND SPIDER and ODYSSEY SPIDER all used ROBOT
SPIDER’s Fsociety crypter service during 2023. Fsociety tools typically consist of
a set of scripts that download and execute an intermediate .NET payload that
subsequently loads a final RAT payload in memory. Throughout 2023, ROBOT
SPIDER continued to update the Fsociety crypter to improve obfuscation and add
capabilities. Generally, infection chains leveraging Fsociety culminated in commodity
RATs such as njRAT Lime.
ODYSSEY SPIDER, which is likely based in Brazil, uses ROBOT SPIDER’s Fsociety
crypter service along with other commodity crypters and RATs. ODYSSEY
SPIDER predominantly focuses on the travel and hospitality sectors in LATAM and
Southeastern Europe, specifically aiming to monetize payment card details entered
during travel-related booking processes. However, in Q3 2023, the adversary
began targeting numerous other sectors and regions, likely while leveraging local
tax return periods.
SQUAB SPIDER primarily targets financial institutions, particularly but not
exclusively those based in Mexico. The adversary achieves initial access by
exploiting web servers to deploy a wide set of webshells. From there, threat
actors rely on passive BLUEAGAVE bind shells or simple listeners to enable lateral
movement through a network and to generally avoid conventional C2 traffic.
SQUAB SPIDER likely attempts to steal transaction-related data from victims.
Outlook
Though opportunistic BGH campaigns remain the primary eCrime threat across
all sectors, a smaller eCrime actor subset will likely continue targeted eCrime
campaigns seeking to steal payment card- or transaction-related data from
victims. As with the BGH ecosystem, legitimate RMM tools will likely remain
popular among targeted eCrime operations due to their widespread use within
normal business processes. The endurance of LATAM-focused adversaries BLIND
SPIDER, ODYSSEY SPIDER, ROBOT SPIDER and SQUAB SPIDER highlights how the
LATAM-targeted eCrime ecosystem will likely persist in the mid-term.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT CrowdStrike 52
Conclusion
Over the course of 2023, CrowdStrike CAO observed adversaries across
the targeted intrusion, eCrime and hacktivist landscapes operating with
unprecedented stealth. The ability to operate undetected remains paramount for
malicious actors, and today’s sophisticated cybercriminals continue to discover
new methods to increase effectiveness, enhance operations and achieve
objectives.
eCrime remained a 2023 threat landscape cornerstone, with BGH adversaries
SCATTERED SPIDER and GRACEFUL SPIDER accounting for most activity.
CrowdStrike CAO assesses BGH will continue to pose the dominant threat within
the eCrime landscape in 2024. This assessment is made with high confidence
based on the continued success of these operations, as observed in the 76%
growth in DLS posts in 2023. Trends likely to be observed in 2024 in support of
BGH operations include ransomware-free data leak operations and an increase in
cloud-conscious operations.
The number of cloud-conscious threat actors continued to grow in 2023 — as
in 2022 — and will highly likely continue to grow in 2024. Adversaries are highly
motivated to invest in and use cloud and other new technologies, such as
generative AI, to increase the efficiency and success of their operations. Cloud-
aware adversaries will look to detect, enumerate and navigate cloud environments
to harvest valuable proprietary information from Microsoft 365, SharePoint and
code repositories. They will use this information in ongoing operations and ransom
negotiations or simply sell it to other eCrime adversaries.
Financially motivated adversaries also increasingly realized the benefits of
dedicated relationships in 2023 and were likely able to increase resulting
operational success rates. Access brokers and RaaS actors will likely continue
to forge dedicated relationships in 2024. The coming year will also likely include
enhancements in social engineering effectiveness, MFA bypass and third-party
provider targeting in efforts to leverage a single larger point of access.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT CrowdStrike 53
High-profile geopolitical conflicts — namely the Russia-Ukraine and Israel-Hamas
conflicts — generated significant targeted intrusion and hacktivist cyber activity in
2023, particularly for Iran-nexus and Russia-nexus adversaries. In 2024, these and
other high-profile conflicts will remain as significant hacktivism drivers.
Beyond cyber activity related to the Israel-Hamas conflict, Iran-nexus adversaries
remained consistent in targeting telecom organizations, a trend likely to continue
in 2024. Russia-nexus adversaries also persisted in their targeting of Ukraine,
NATO members and partner countries. They will almost certainly continue to
conduct intelligence collection operations and IO in these geographies in 2024.
CrowdStrike CAO graduated several activity clusters to named adversaries
in 2023, including the first-ever Egypt-nexus adversary, WATCHFUL SPHINX.
Consistent with previous assessments, CrowdStrike CAO expects the majority of
established adversaries and activity clusters to continue to expand or update their
capabilities in 2024. Fewer adversaries and activity clusters around the world are
likely to expand their assessed target scope; rather, they will likely continue to
focus on historical and predominantly regional target sets.
Within the vulnerability threat landscape, CrowdStrike CAO assesses that several
2023 trends — namely, edge device and EOL product targeting — will persist in
2024. eCrime threat actors remained the primary threat to most mobile users in
2023 and will likely continue as such in 2024. Targeted intrusion actors will also
almost certainly continue to target mobile devices, with increases in platform
and device security causing less sophisticated adversaries to struggle to operate
successfully in that space.
With the creation of Counter Adversary Operations, CrowdStrike remains steadfast
in its mission to stop breaches. Combining best-in-class threat intelligence with
a professional, managed threat hunting service unlike anything else offered in
the industry, CrowdStrike ensures its customers can access industry-leading
information to drive their individual operational success.
CrowdStrike CAO remained focused on disrupting the adversary in 2023 and will
continue to deliver unparalleled threat intelligence in 2024 and beyond.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 54
Recommendations
1 Make identity protection a must-have
Due to high success rates, identity-based and social engineering attacks surged in 2023.
Stolen credentials grant adversaries swift access and control — an instant gateway to a
breach. To counter these threats, it is essential to implement phishing-resistant multifactor
authentication and extend it to legacy systems and protocols, educate teams on social
engineering and implement technology that can detect and correlate threats across identity,
endpoint and cloud environments. Cross-domain visibility and enforcement enables security
teams to detect lateral movement, get full attack path visibility and hunt for malicious use
of legitimate tools. Addressing sophisticated access methods such as SIM swapping,
MFA bypass and the theft of API keys, session cookies and Kerberos tickets requires
proactive and continuous hunting for malicious behavior.
Prioritize cloud-native application
2
protection platforms (CNAPPs)
Cloud adoption is exploding as companies realize the potential for innovation and
business agility that the cloud offers. Due to this growth, the cloud is rapidly becoming a
major battleground for cyberattacks. Businesses need full cloud visibility, including into
applications and APIs, to eliminate misconfigurations, vulnerabilities and other security threats.
CNAPPs are critical: Cloud security tools shouldn’t exist in isolation, and CNAPPs provide a
unified platform that simplifies monitoring, detecting and acting on potential cloud security
threats and vulnerabilities. Select a CNAPP that includes pre-runtime protection, runtime
protection and agentless technology to help you discover and map your apps and APIs running
in production, showing you all attack surfaces, threats and critical business risks.
3 Gain visibility across the most critical
areas of enterprise risk
Adversaries often use valid credentials to access cloud-facing victim environments and then
use legitimate tools to execute their attack, making it difficult for defenders to differentiate
between normal user activity and a breach. To identify this type of attack, you need to
understand the relationship between identity, cloud, endpoint and data protection telemetry,
which may be in separate systems. In fact, the average enterprise uses 45+ security tools,
creating data silos and gaps in visibility. By consolidating into a unified security platform with
AI capabilities, organizations have complete visibility in one place and can easily control their
operations. With a consolidated security platform, organizations save time and money and can
quickly and confidently discover, identify and stop breaches.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 55
4 Drive efficiency: Adversaries are
getting faster — are you?
It takes adversaries an average of 62 minutes — and the fastest only 2 minutes — to move
laterally from an initially compromised host to another host within the environment. Can
you keep up? Let’s face it — legacy SIEM solutions have failed the SOC. They are too slow,
complex and costly, and they were designed for an age when data volumes — and adversary
speed and sophistication — were a fraction of what they are today. You need a tool that’s
faster, easier to deploy and more cost-effective than legacy SIEM solutions. Investigate
better approaches, such as CrowdStrike Falcon® Next-Gen SIEM, which unifies all threat
detection, investigation and response in one cloud-delivered, AI-native platform for unrivaled
efficiency and speed. Or, if you don’t have an internal SOC team, consider 24/7 managed
detection and response (MDR).
Build a cybersecurity culture
5
Though technology is clearly critical in the fight to detect and stop intrusions, the end
user remains a crucial link in the chain to stop breaches. User awareness programs should
be initiated to combat the continued threat of phishing and related social engineering
techniques. For security teams, practice makes perfect. Encourage an environment that
routinely performs tabletop exercises and red/blue teaming to identify gaps and eliminate
weaknesses in your cybersecurity practices and response.

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 56
CrowdStrike
Products and
Services
Endpoint Security
FALCON PREVENT | NEXT-GENERATION ANTIVIRUS
Protects against all types of threats, from malware and ransomware to sophisticated attacks,
and deploys in minutes, immediately protecting your endpoints
FALCON INSIGHT XDR | DETECTION AND RESPONSE FOR
ENDPOINT AND BEYOND
Offers industry-leading, unified EDR and extended detection and response (XDR) with
enterprise-wide visibility to automatically detect adversary activity and respond across
endpoints and all key attack surfaces
FALCON COMPLETE | MANAGED DETECTION AND RESPONSE
Stops and eradicates threats in minutes with 24/7 expert management, monitoring and
surgical remediation, proactive threat hunting, and integrated threat intelligence — all
backed by the industry’s strongest Breach Prevention Warranty
FALCON COMPLETE XDR | MANAGED EXTENDED DETECTION AND
RESPONSE (MXDR)
Expands Falcon Complete’s industry-leading MDR service with cross-domain XDR protection
run by CrowdStrike’s elite 24/7 expertise, proactive threat hunting and native threat
intelligence
FALCON FIREWALL MANAGEMENT | HOST FIREWALL
Delivers simple, centralized host firewall management, making it easy to manage and control
host firewall policies
FALCON DEVICE CONTROL | USB SECURITY
Provides the visibility and precise control required to enable safe usage of USB devices
across your organization
FALCON FOR MOBILE | ENDPOINT DETECTION AND RESPONSE
Protects against threats to iOS and Android devices, extending XDR/EDR capabilities
to your mobile devices, with advanced threat protection and real-time visibility into app
and network activity

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 57
Counter Adversary Operations
FALCON ADVERSARY OVERWATCHTM | UNIFIED THREAT HUNTING
Provides around-the-clock protection across endpoint, identity and cloud workloads
delivered by AI-powered threat hunting experts, and includes built-in threat intelligence to
expose adversary tradecraft, vulnerabilities and stolen credentials
FALCON ADVERSARY INTELLIGENCE | SOC AUTOMATION
Cuts response time from days to minutes across the entire security stack with
end-to-end intelligence automation, and allows you to instantly submit potential threats
to an AI-powered sandbox, extract indicators of compromise and deploy countermeasures —
all while continuously monitoring for fraud and safeguarding your brand, employees
and sensitive data
FALCON ADVERSARY HUNTER | INTEL-LED THREAT HUNTING
Provides world-class intelligence reporting, technical analysis, and threat hunting and
detection libraries, and cuts the time and cost required to understand and defend against
sophisticated nation-state, eCrime and hacktivist adversaries
FALCON COUNTER ADVERSARY OPERATIONS ELITE
ON-DEMAND ANALYST
Provides an assigned analyst who uses advanced investigative and threat hunting tools
powered by deep adversary intelligence to identify and disrupt adversaries across your IT
environment and beyond
Cloud Security
FALCON CLOUD SECURITY
Provides breach protection, including threat intelligence, detection and response; workload
runtime protection; and cloud security posture management across AWS, Azure and Google
Cloud Platform (GCP)
FALCON CLOUD SECURITY FOR CONTAINERS
Delivers cloud and container security and breach protection; cloud security posture
management; threat detection and response across on-premises, hybrid and multi-cloud
environments; and cloud workload protection, including container security and Kubernetes
protection
FALCON CLOUD SECURITY FOR MANAGED CONTAINERS
Provides cloud and container security, including threat intelligence, detection and response;
container image security; and Kubernetes protection

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 58
FALCON OVERWATCH CLOUD THREAT HUNTING
MANAGED SERVICES
Unearths cloud threats, from unique cloud attack paths with complex trails of cloud IOAs
and indicators of misconfiguration (IOMs) to well-concealed adversary activity in your
critical cloud infrastructure — including AWS, Azure and GCP
FALCON COMPLETE CLOUD SECURITY
MDR FOR CLOUD WORKLOADS
Provides a fully managed cloud workload protection service, delivering 24/7 expert security
management, threat hunting, monitoring and response for cloud workloads, backed by
CrowdStrike’s industry-leading Breach Prevention Warranty
Identity Protection
FALCON IDENTITY THREAT DETECTION
Enables hyper-accurate detection of identity-based threats in real time, leveraging AI
and behavioral analytics to provide deep actionable insights to stop modern attacks like
ransomware
FALCON IDENTITY THREAT PROTECTION
Enables hyper-accurate threat detection and real-time prevention of identity-based attacks
by combining the power of advanced AI, behavioral analytics and a flexible policy engine to
enforce risk-based conditional access
FALCON COMPLETE IDENTITY THREAT PROTECTION
MANAGED IDENTITY THREAT PROTECTION
Provides a fully managed identity protection solution delivering frictionless, real-time
identity threat prevention and IT policy enforcement, monitoring and remediation —
powered 24/7 by CrowdStrike’s team of experts
Security and IT Operations
FALCON DISCOVER | IT HYGIENE
Identifies unauthorized accounts, systems and applications anywhere in your environment
in real time, enabling instant visibility to improve your overall security posture
FALCON SPOTLIGHT | VULNERABILITY MANAGEMENT
Offers security teams an automated, comprehensive vulnerability management solution,
enabling faster prioritization and integrated remediation workflows without resource-
intensive scans

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 59
FALCON EXPOSURE MANAGEMENT | EXPOSURE MANAGEMENT
Allows security teams to prioritize exposures making the biggest impact and proactively
reduce an adversary’s opportunity for compromise and lateral movement
FALCON SURFACE | EXTERNAL ATTACK SURFACE MANAGEMENT
Continuously discovers and maps all internet-facing assets to shut down potential exposure
with guided mitigation plans to reduce the attack surface
FALCON DATA PROTECTION | UNIFIED DATA PROTECTION
Provides deep real-time visibility into what is happening with sensitive data and stops data
theft with policy enforcement that automatically follows content, not files
FALCON FILEVANTAGE | FILE INTEGRITY MONITORING
Provides real-time, comprehensive and centralized visibility that boosts compliance and
offers relevant contextual data
FALCON FORENSICS | FORENSIC CYBERSECURITY
Automates collection of point-in-time and historic forensic triage data for robust analysis of
cybersecurity incidents
FALCON FOR IT | AUTOMATED WORKFLOWS
Extends the Falcon platform to automate IT and security workflows with an end-to-end,
visibility-to-action life cycle
Next-Gen SIEM
FALCON NEXT-GEN SIEM | SIEM AND LOG MANAGEMENT
Empowers you to swiftly shut down adversaries and slash SOC costs by unifying industry-
leading detection, world-class intelligence, blazing-fast search and AI-led investigations in
one cloud-delivered platform
CrowdStrike Services
INCIDENT RESPONSE
Stop active breaches and restore order with the most informed and capable
IR team available
Incident Response
Compromise Assessment
Endpoint Recovery
Network Detection Services
Services Retainer

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 60
STRATEGIC ADVISORY SERVICES
Develop and mature the security program to improve defenses
Tabletop Exercise
Maturity Assessment
Ransomware Defense Assessment
SOC Assessment
SEC Readiness
Board and CXO Briefings
RED TEAM SERVICES
Stress-test and validate defenses through simulated attacks
Penetration Testing
Red Team/Blue Team Exercise
Adversary Emulation Exercise
CLOUD AND IDENTITY SERVICES
Proactively secure the new perimeter
Identity Security Assessment
Cloud Security Assessment
Red Team/Blue Team Exercise for Cloud
Cloud Compromise Assessment
TECHNICAL ADVISORY SERVICES
Audit and address security gaps to tangibly reduce risk
Technical Risk Assessment
Cyber Threat Risk Evaluation
TRAINING AND SECURITY UPSKILLING
Become security experts under CrowdStrike tutelage

CROWDSTRIKE 2024 GLOBAL THREAT REPORT 61
About
CrowdStrike
CrowdStrike (Nasdaq: CRWD), a global cybersecurity leader, has redefined
modern security with the world’s most advanced cloud-native platform for
protecting critical areas of enterprise risk — endpoints and cloud workloads,
identity and data.
Powered by the CrowdStrike Security Cloud and world-class AI, the
CrowdStrike Falcon® platform leverages real-time indicators of attack, threat
intelligence, evolving adversary tradecraft and enriched telemetry from across
the enterprise to deliver hyper-accurate detections, automated protection and
remediation, elite threat hunting and prioritized observability of vulnerabilities.
Purpose-built in the cloud with a single lightweight-agent architecture, the
Falcon platform delivers rapid and scalable deployment, superior protection and
performance, reduced complexity and immediate time-to-value.
CrowdStrike: We stop breaches.
Learn more: www.crowdstrike.com
Follow us: Blog | X | LinkedIn | Facebook | Instagram
Start a free trial today: www.crowdstrike.com/free-trial-guide
© 2024 CrowdStrike, Inc. All rights reserved. CrowdStrike, the falcon
logo, CrowdStrike Falcon and CrowdStrike Threat Graph are marks
owned by CrowdStrike, Inc. and registered with the United States Patent
and Trademark Office, and in other countries. CrowdStrike owns other
trademarks and service marks, and may use the brands of third parties
to identify their products and services.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-20", "model": "gemini-3.5-flash-lite"} -->
