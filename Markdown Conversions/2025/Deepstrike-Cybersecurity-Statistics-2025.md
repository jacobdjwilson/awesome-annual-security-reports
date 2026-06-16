# Cybersecurity Statistics 2025: Breach Costs, Ransomware & AI Threats

## Table of Contents
- [Global Overview of 2025 Cybersecurity](#global-overview-of-2025-cybersecurity)
- [Cost Breakdown: Data Breaches by the Numbers](#cost-breakdown-data-breaches-by-the-numbers)
- [Attack Vector Distribution in 2025](#attack-vector-distribution-in-2025)
- [Industry Breakdown: Who Are the Biggest Targets?](#industry-breakdown-who-are-the-biggest-targets)
- [Regional Breakdown: Global vs. Local Threats](#regional-breakdown-global-vs-local-threats)
- [Major Breaches of 2025: Notable Incidents](#major-breaches-of-2025-notable-incidents)

---

**Organization:** Deepstrike  
**Report Title:** Cybersecurity-Statistics  
**Year:** 2025  
**Date:** November 29, 2025 (Updated: November 26, 2025)  
**Author:** Mohammed Khalil

Cybersecurity statistics for 2025 reveal a digital ecosystem under siege by increasingly sophisticated threats. This report analyzes the key data and trends shaping global cybersecurity in 2024–2025, a period during which cyber incidents reached record levels in frequency and impact. 

### Global Overview of 2025 Cybersecurity

In 2025, cybersecurity entered a new era defined by unprecedented economic stakes and relentless attack volumes. 

- **Global Cybercrime Cost**: Projected to cost the world $10.5 trillion annually by 2025, equivalent to the third-largest economy. This translates to about $333,000 lost every minute.
- **Data Breach Costs**: The global average cost of a data breach in 2025 is $4.44 million, a 9% decrease from 2024’s $4.88M.
- **Ransomware Surge**: Involved in 44% of breaches in 2025, up from ~32% in 2024.
- **Supply Chain Risk**: Breaches involving third parties doubled to ~30% of total incidents.

![Table: Select global cybersecurity metrics, 2024 vs 2025]

### Cost Breakdown: Data Breaches by the Numbers

The economics of a breach vary by region and industry. While the global average is $4.44 million, the United States faces a record $10.22 million average cost, driven by stringent notification laws and high litigation risks.

- **Incident Response & AI Dividends**: Organizations using extensive AI-driven security slashed their breach lifecycle by 80 days and saved $1.9M per incident on average.
- **Mega Breaches**: Incidents exposing over 1 million records (e.g., the Change Healthcare breach affecting ~190 million records) continue to skew costs into the nine-figure range.
- **Cyber Insurance**: The market grew to ~$23 billion in 2025, with premiums rising by ~28% as insurers demand stricter security controls like MFA and backups.

![Table: 2025 breach cost breakdown by region, industry, and key factors]

### Attack Vector Distribution in 2025

Attackers are shifting tactics, with Generative AI supercharging social engineering and supply chain exploits becoming a primary entry point.

- **Phishing**: Remains the #1 vector (15.9% of breaches). AI-generated lures and deepfake audio have increased success rates.
- **Vulnerability Exploitation**: Jumped to 20% of breaches, an 8x increase in exploits targeting VPNs and edge devices.
- **Shadow AI**: The use of unsanctioned AI tools increased breach costs by ~$670K on average when present.

![Table: Primary attack vectors in data breaches 2025 with prevalence and impact]

### Industry Breakdown: Who Are the Biggest Targets?

- **Healthcare**: The most expensive industry for the 14th consecutive year ($7.42M average).
- **Financial Services**: The second most expensive sector ($5.56M average), heavily targeted for direct financial theft and BEC (Business Email Compromise).
- **Manufacturing**: Experienced a 61% surge in ransomware attacks due to the high cost of production downtime.
- **Retail**: Faces a blend of customer data theft and ransomware, with retail-related leaks on extortion sites rising to 11%.
- **Government**: Frequently targeted by nation-state actors (Russia, China) for espionage and critical infrastructure disruption.

### Regional Breakdown: Global vs. Local Threats

- **United States**: Highest financial impact; 88% of the world’s breach litigation occurs here.
- **Europe**: GDPR compliance has stabilized costs, though the region faces high volumes of state-sponsored attacks.
- **Middle East**: Significant investment in AI defenses led to an 18% YoY decline in breach costs.
- **Africa**: Rapid digitization is outpacing security investment, leading to a rise in digital extortion and crypto scams.
- **Asia Pacific**: A diverse landscape where advanced economies (Japan, Singapore) face targeted supply chain attacks, while emerging markets struggle with volume-based threats.

### Major Breaches of 2025: Notable Incidents

1. **Coinbase (May 2025)**: Insider threat via third-party contractors led to the exposure of 69,000 customers' data.
2. **Marks & Spencer (May 2025)**: Ransomware attack via an IT outsourcing partner caused an estimated £300M loss.
3. **Qantas Airlines (October 2025)**: Mega-breach of a third-party Salesforce-based platform exposed 5.7 million customer records.
4. **Red Hat (September–October 2025)**: Unauthorized access to an internal GitLab server exposed 570 GB of consulting data.
5. **Salesloft/Drift (August 2025)**: OAuth token theft allowed attackers to pivot into over 700 organizations' Salesforce instances.

---

d party app
controls e.g., reviewing what apps are authorized in your SaaS
environment and using least privilege for their tokens. It also
emphasized monitoring cloud API usage abnormal data
extraction might have been detected earlier if monitoring was in
place. This incident is reminiscent of the 2020 OAuth thefts like
the SolarWinds related 0Auth abuse at Microsoft, reaffirming that
tokens are as sensitive as passwords and need protection.
Each of these major breaches from 2025 carries lessons:
Insiders and Third Parties: Coinbase and M&S show that those
with insider access, whether direct employees or contractors, can
cause immense damage, deliberately or accidentally. Continuous
background checks, least privilege access, and monitoring of
privileged activities are needed, as is careful security due
diligence on outsourcing partners.
Ransomware Evolution: The M&S and Qantas cases highlight
ransomware groups combining data theft with traditional
encryption, and not hesitating to leak data when unpaid. Itʼs a
warning that even if you choose not to pay, which is the
recommended stance by law enforcement, you must be ready for
the fallout of sensitive data potentially going public. It reinforces
having strong backups to not need to pay for decryption and also
robust encryption of data at rest to limit the damage if stolen data
is leaked i.e., if itʼs encrypted or tokenized, the impact is less.
Supply Chain Attacks: The Qantas, Red Hat, and Salesloft
incidents all show supply chain weaknesses whether itʼs a
vendorʼs app or a subcontractorʼs credentials can lead to
breaches at many organizations at once. Itʼs the mass casualty
approach of cyberattacks. Companies must therefore vet the
security of their suppliers and consider technical measures like
conditional access for third party apps e.g., limit what data an
integration can see, and use behavior analytics to detect if an
integration suddenly pulls vastly more data than usual.
Cloud Token Security: The Salesloft breach especially
underscores that in the cloud, tokens = keys to the kingdom. An
OAuth token that grants an app access to your data should be
guarded, rotated, and revokable. Zero trust principles suggest
monitoring and maybe limiting scopes only give third party apps
the minimum scope needed. Additionally, implementing anomaly

detection on admin accounts and OAuth usage could flag unusual
activity like an app pulling thousands of records per minute.
Resilience Over Prevention: Interestingly, none of these
organizations were completely cyber inept Coinbase, Red Hat,
etc., all invest in security. Yet breaches happened. This shows
that prevention isnʼt foolproof. What matters is how quickly you
respond and contain. For example, Coinbase caught the issue by
May and didnʼt lose funds, M&S had a defined recovery timeline,
Qantas had backups so flight operations were unaffected, it was
customer data, not flight systems. The statistics show most
organizations faced at least some operational disruption from
breaches and majority took over 100 days to fully recover.
Planning for resilience assuming breach, and being ready to
mitigate impact fast is as important as trying to prevent every
breach.
These major incidents of 2025 collectively illustrate the breadth of
threats from insider collusion to sophisticated supply chain exploits
and reinforce many of the yearʼs statistical trends like rise of supply
chain attacks, persistence of ransomware, and consequences of not
paying ransoms.
Emerging Trends in Cybersecurity for 2025
Looking at the statistics and breaches in 2025, several emerging
trends and themes stand out. These are areas where we see rapid
development either on the side of attackers innovating or defenders
adapting or both. Understanding these will help anticipate how the
cybersecurity landscape might shift moving into 2026 and beyond:

1. AI Powered Cyber Attacks and Defenses: 2025 could be dubbed
the year AI hit cybersecurity in full force. On one hand, attackers
are leveraging Generative AI to scale and sharpen their
campaigns. As noted, 16% of breaches now involve malicious
use of AI. Phishing emails are now often AI written meaning
nearly flawless grammar and personalization, defeating the old
Nigerian prince telltale signs. Deepfakes AI generated synthetic
media moved from novelty to a real tool in attackersʼ kits: 2025
saw deepfake voice scams fool companies into making large
transfers a tactic called voice phishing or vishing. There was even
an incident where criminals created a deepfake video of a CEO in
a Zoom meeting to authorize a fraudulent transaction. On the
other hand, defenders are increasingly deploying AI and machine
learning in cybersecurity products from user behavior analytics to
detect anomalies to AI that helps triage and respond to alerts. The
payoff is clear: companies using AI extensively shaved 80 days
off breach response and saved ~$1.9M per incident. Weʼre also
seeing AI in threat intel e.g., ML models sifting through dark web
forums to identify threats. Expect this AI race to accelerate:
Gartner predicts by 2028, 50% of entry level security work
might be handled by AI assistants like analyzing logs, filtering
phishing. However, a caveat: IBMʼs report warns that AI adoption
is outpacing AI governance 63% of orgs lack policies for AI use
and those lacking governance pay more when AI related incidents
happen. Going forward, weʼll hear more about AI safety in cyber
ensuring AI tools themselves arenʼt vulnerable or misused.
2. Zero Trust Architecture Becomes Standard: With the traditional
network perimeter effectively gone thanks to cloud and remote
work, Zero Trust never trust, always verify is no longer just a
buzzword but an emerging standard. The 2025 stats reinforce
why: many breaches stem from over privileged access or implicit
trust whether itʼs a supplier, an employee on the LAN, or an on
prem app. Zero Trust frameworks from NIST, etc. prescribe
measures like continuous authentication, micro segmentation of
networks, and strict verification for every access request. We see
uptake especially after high profile breaches: for example, in the
wake of supply chain breaches, companies are implementing
network segmentation and MFA for third party access as zero
trust measures. Identity is the new perimeter, so Identity and
Access Management IAM and phishing resistant MFA like FIDO2
security keys are trending. One data point: in 2024 about 25% of
organizations were moving to Zero Trust models, and that
number is rising into 2025 as mandates like U.S. federal agencies
are required to adopt zero trust by 2024 per an executive order.
Zero Trust is a journey, not a product, but expect these concepts

like continuous monitoring of device posture, least privilege
principles to underpin most security strategies moving forward.
3. Rise of Double/Triple Extortion & Ransomware Industrialization:
Ransomware groups have evolved their business model to ensure
they get paid even when victims have backups. Double extortion
encrypting data and stealing copies to threaten leaks is now
standard. In 2025 we saw triple extortion become more common:
adding a third pressure point such as DDoS attacks or harassing
customers of the victim. The stats show ransom payments are
down more refusal, so attackers compensate by causing
maximum pain. Some gangs even contact the victimʼs clients or
partners to pressure payment. Ransomware has effectively
become a professional industry Ransomware as a Service groups
with affiliates. The prediction is by 2031 a ransomware attack will
occur every 2 seconds essentially fully automated attacks hitting
globally. Weʼre not far off if IoT botnets and worm like
ransomware like 2017ʼs WannaCry/NotPetya come back. Another
trend: ransom demands peaked in 2021–22, and actually the
average demand dropped a bit e.g., Chainalysis reported total
ransomware revenue fell in 2024 due to non payment, but the
cost of handling a ransomware incident remains extremely high
$5M+. Also, more ransomware data leaks means more
secondary fraud if your data was stolen and leaked, you might
face fraud years later from that info e.g., leaked health records
used for insurance fraud. Itʼs a lasting impact. We also see the
target profile shifting: threat actors focus on critical sectors
manufacturing, healthcare for higher leverage. And smaller
businesses are not spared in fact, about 70% of ransomware
attacks in 2024 targeted SMBs small and mid sized businesses,
since they often have weaker security and might be more likely to
pay a smaller ransom.
4. Cloud Security and Misconfiguration Epidemic: The mass
migration to cloud has led to many security failures simply due to
misconfiguration or user error. As noted, through 2025 about
99% of cloud breaches are the customerʼs fault, not the cloud
providerʼs. In 2025, we continued to see embarrassing exposures
of data due to things like public storage buckets, accidentally
publishing credentials on GitHub, or forgetting to secure an API.
One stat: 9% of publicly accessible cloud storage buckets
contain sensitive data per a 2024 survey thatʼs a lot of open data
troves. Also, many companies lack visibility: 80% of companies
experienced a cloud breach in the past year and often only
discovered it months later. Attackers are capitalizing by
automating searches for misconfigs. Looking ahead, cloud native
threats like container compromises and Kubernetes attacks will

rise. We also anticipate regulators will start penalizing cloud
misconfigurations leading to breaches some GDPR fines already
did for exposed buckets. Shift left security embedding security in
DevOps, infrastructure as code scanning is an emerging practice
to catch misconfigs before deployment. Secure cloud
architectures and zero trust cloud access like CASB, SSPM tools
will be key trends to combat this.
5. Internet of Things IoT and OT Security Risks: By 2025, there are
an estimated 18+ billion IoT devices connected to everything
from smart cameras to industrial sensors. IoT often has weak
security, and many such devices became part of botnets like
Mirai successors. In 2025, the BadBox 2.0 botnet infected over
10 million smart TVs and set top boxes, which were then used to
launch DDoS attacks. This is an emerging trend: IoT botnets
fueling record breaking DDoS already. We've seen some ~3 Tbps
attacks in recent years. On the OT side Operational Tech
controlling physical processes, half of publicly reported cyber
incidents in 2025 involved OT in some way. Attacks on critical
infrastructure water systems, power grids, manufacturing lines
are particularly worrying because they can cause real world
harm. A 2025 example: an attack on a European portʼs OT
network caused days of shipping delays. Governments are
waking up e.g., the U.S. issued new security directives for
pipelines after the Colonial Pipeline hack, and in 2025 worked on
similar rules for rail and aviation systems. For IoT, we see
emerging standards, some countries mandating unique default
passwords, etc.. The trend is that IoT/OT security is becoming as
important as IT security requiring network segmentation,
specialized monitoring, and incident response that accounts for
safety.
6. Cyber Talent Shortage and Burnout: On the defensive side, a
critical emerging issue is the workforce gap. As discussed,
thereʼs a shortage of 4.8 million cybersecurity professionals
globally in 2025. This gap grew by 19% in a year because, while
threats rose, many companies froze hiring or even cut security
budgets due to economic pressures. Paradoxically, 33% of
organizations said lack of budget is now the top reason they canʼt
fill cyber roles so even though the need is dire, money isnʼt
always available to expand teams. As a result, existing security
staff are overworked and burning out: 66% say their job stress
increased significantly over 5 years, and nearly half of cyber
leaders are considering quitting by 2025 due to stress. This
trend is alarming because technology alone canʼt solve
everything, skilled humans are needed to configure, analyze, and
respond. The industry is responding with a twofold approach:

broaden the talent pipeline, more training programs, diversifying
hiring to people with non-traditional backgrounds and augment
with automation using AI to handle level 1 tasks to free humans for
complex issues. Going forward, organizations that canʼt address
the talent gap may face increased risk. Statistics even show
companies with big staffing shortages had breach costs $1.76M
higher than those well staffed. The trend is that cybersecurity will
become a more cross disciplinary responsibility DevOps, IT, etc.,
all share some load rather than relying solely on a small infosec
team.
7. Quantum Computing and Post Quantum Prep: While still on the
horizon, many began discussing the Q Day the moment a
quantum computer could break current encryption like RSA/ECC.
The consensus is that might be in the early 2030s, but 2025 saw
increased urgency in preparing for it. NIST finalized a set of post
quantum cryptography PQC algorithms in 2024. By 2025,
forward looking organizations started inventorying their
cryptographic assets and making plans to shift to PQC for things
like VPNs and PKI. Why is this relevant now? Because of a threat
called Steal Now, Decrypt Later adversaries, particularly nation
states, may be stealing encrypted data now and storing it, with
the expectation that in a decade they can decrypt it with quantum
computers. Thatʼs especially concerning for sensitive long term
secrets think: military or personal data thatʼs still relevant in 20+
years. The emerging trend is companies and governments
beginning migration to quantum resistant encryption. The U.S.
government, for example, has directives for agencies to start that
process. Itʼs a slow, systemic change, but noteworthy as an
emerging theme in security planning.
In sum, the emerging trends of 2025 indicate that cybersecurity is at
an inflection point with AI dramatically changing the threat and
defense paradigm, trust models shifting toward Zero Trust, attackers
doubling down on extortion strategies, and systemic issues like
cloud complexity and talent shortages forcing new approaches. The
wise organization will note these trends and start adapting today:
e.g., experiment with AI driven defenses but also manage AI risk,
implement Zero Trust incrementally, engage in tabletop exercises for
ransomware extortion scenarios, tighten cloud config processes,
invest in OT monitoring if you have factories, and support your
security team to prevent burnout maybe by automating grunt work
and providing training.
What These Statistics Mean: Insights and Implications

Statistics without context can be just numbers. So, what do these
2025 cybersecurity stats really tell us, and what should
organizations do about it? Here are the key insights and strategic
implications drawn from the data:
Cybersecurity is a Core Business Risk Not Just IT: When
cybercrime costs are hitting trillions of dollars globally, it means
cyber risk has become macro economic. Executives and boards
must treat cybersecurity as a fundamental business risk, on par
with market or credit risk. The fact that a single breach costs $4M
on average and could be much more means that for many
companies a major cyber incident could wipe out a yearʼs profits.
We saw examples of this: the M&S ransomware causing $400M
in losses thatʼs a huge hit to a retailerʼs balance sheet. Insight:
Security can no longer be relegated to the IT department alone. It
requires C suite attention hence rise of CISOs reporting to CEOs
and enterprise wide risk management.
Itʼs Not If, But When Focus on Resilience: The stats showing
constant attack frequency every few seconds globally and high
odds of human error 68% of breaches involve human factors
reinforce that no organization can be 100% breach proof. Despite
best efforts, something will eventually slip through be it a clever
phish or an unpatched server. Smart organizations are shifting
strategy from solely prevention to resilience and damage control.
This means investing in capabilities to limit impact: robust data
backups so ransomware doesnʼt cripple you, incident response
plans so you contain and eradicate threats faster, network
segmentation so an intruder in one area canʼt roam freely, and
business continuity plans to keep critical services running
manually if needed. The IBM data that organizations with incident
response teams and regular testing saved ~$250K in breach
costs supports this. Also, the trend of refusing ransom and

recovering anyway shows resilience is possible if you prepare.
The goal becomes not just to keep attackers out, but to ensure
that when they get in, you can withstand the hit and bounce back
quickly.
Speed Matters Detect Fast, Respond Decisively: A clear
message from 2025 stats is the huge difference speed makes.
Breach lifecycle time to identify and contain globally is ~241
days, but cutting that down even by a few weeks can save seven
figures in costs. Organizations with AI that cut 80 days from
response saved $1.9M. Also, many ransomware incidents are
discovered within a week now often because the attackers
announce themselves. The takeaway: early detection and quick
containment are critical. This implies investing in 24/7 monitoring
like a Security Operations Center with threat detection tools,
using automation to correlate alerts to not miss early warning
signs, and having an empowered incident response team that can
act fast e.g., isolate affected systems, rotate credentials, engage
law enforcement if needed. The difference between catching an
intrusion at day 1 vs day 100 could be the difference between a
minor incident and a catastrophic breach.
Human Element Build a Security Culture: With phishing and
social engineering being top vectors, and insider errors
contributing heavily, technology alone wonʼt stop breaches.
People are the weakest link, but they can also be the strongest
defense if properly trained and engaged. The stat that 88% of
breaches are caused by human error, while perhaps a bit high,
underscores the need for ongoing security awareness.
Companies should invest in regular, engaging training including
phishing simulations. But beyond training, building a culture of
security is key. Employees should feel itʼs part of their job to be
vigilant like questioning unusual requests, reporting incidents
promptly without fear of blame. The concept of cyber hygiene
needs to be as routine as workplace safety drills. Additionally,
with burnout stats so high among cyber teams, leadership must
also address employee well being and workload otherwise the
defenders your IT/security staff become a weak link if theyʼre too
overwhelmed to respond effectively. Organizations might rotate
staff, provide mental health support, or bring in managed service
providers to offload some pressure.
Technology Investment AI and Zero Trust Are Game Changers:
The data makes a strong case that certain technologies and
frameworks are no longer optional luxuries, but essentials for
cost effective security. For example, AI/automation in security is
delivering measurable savings so not adopting it could leave you
at a financial disadvantage against those who do plus leave you

more exposed as threats scale beyond human capacity. Similarly,
Zero Trust architecture directly addresses some of the main
causes of breaches like stolen creds and lateral movement. If
22% of exploit paths were via VPN/edge devices, Zero Trust
would dictate not trusting those implicitly requiring further
authentication or segmentation inside. The takeaway is
organizations should accelerate plans to implement these modern
approaches. Itʼs not hype: the stats prove AI works in defense,
and Zero Trustʼs philosophy matches the threat reality. That said,
implementing them should be done thoughtfully e.g., ensure AI
tools themselves are secure and that zero trust doesnʼt impede
business more than necessary. But doing nothing is worse.
Third Party Risk Trust But Verify and Limit: One of the loudest
messages of 2025 data is that your cybersecurity is only as
good as that of your vendors/partners. With 30% of breaches
involving third parties, companies must re-evaluate how they
handle vendor risk. This means conducting thorough security
assessments of critical suppliers, contractually requiring certain
safeguards like encryption, breach notification, right to audit, and
technically limiting third party access donʼt give a vendor full
network access if they only need a specific subset. Network
segmentation can ensure a breach in a vendorʼs remote support
tool doesnʼt compromise your crown jewels. Also, have a
response plan for supply chain incidents know how to quickly
disconnect or shut off an integrated system if itʼs been
compromised. Think of it this way: youʼre effectively inheriting
risk from anyone you digitally connect with, so diligence and
contingency plans are vital.
Data Protection and Encryption Reduce the Value of Stolen
Data: Attackers want data they can monetize personal info, credit
cards, IP, etc. One strategy to mitigate impact is encrypting or
tokenizing sensitive data so that even if itʼs stolen, itʼs useless to
attackers. The stats show many breaches include personal data
and lead to identity theft. By using strong encryption for data at
rest and in transit, and by adopting things like Zero Knowledge
architectures where possible, organizations can lower the stakes.
Indeed, IBMʼs report found that extensive use of encryption was a
top cost reducing factor cutting breach costs significantly. Also,
implementing data loss prevention DLP and rigorous access
controls limits what data insiders and attackers can access or
exfiltrate. In short, assume the adversary will get in somewhere
what will they find? If your most sensitive databases are
encrypted or segregated, the damage can be contained. This
goes hand in hand with the minimize data collection ethos keep

what you need, securely, and dispose of what you donʼt less data
= less to lose.
Cyber Insurance as Safety Net But Not a Substitute: Many
companies are turning to cyber insurance to offset risk. The
market stats projected ~$24B in 2025 premiums show huge
growth. Insurance can indeed help cover certain costs, incident
response services, legal fees, sometimes even ransom payments
if allowed. However, insurers now require stringent proof of
security practices essentially they wonʼt insure you if youʼre not
already doing a decent job. Also, insurance might not cover all
losses e.g., reputational damage or long term lost business. So,
the insight is: insurance is a complement, not a replacement for
good security. Treat it as the last layer in your defense in depth: if
all else fails, it cushions the blow. And ensure you understand
policy details, some claims have been denied when companies
didnʼt meet security warranties or when an act was deemed
nation state cyber war some policies exclude that. The trend is
that insurance will push companies to adopt best practices almost
like an external auditor, which in the end improves security
overall.
Collaboration and Intelligence Sharing: Given the scale of
threats, thereʼs an increasing need for organizations to not fight
alone. Industry groups and governments are promoting threat
intelligence sharing, so everyone can benefit from early
warnings. The Verizon DBIR and other reports compile cross
industry data these stats we discuss are themselves a form of
shared knowledge. The implication is organizations should
participate in info sharing like ISACs Information Sharing and
Analysis Centers for their sector and build relationships with law
enforcement and incident response firms before an incident. For
example, knowing that a certain phishing campaign is going
around targeting finance firms can help your company
preemptively warn staff. Or sharing IoC Indicators of Compromise
of a new malware found in one hospital can help others check if
theyʼre hit. The old mindset of keeping breaches secret is fading
also due to breach laws, the new mindset is transparency and
collective defense. The stat that almost half of breached
organizations plan to raise prices of goods/services post breach
is alarming it shows breaches have economy wide effects
inflationary pressure. The more we collaborate to prevent
breaches, the less these costs get passed around.
In essence, these statistics mean that cybersecurity in 2025 must be
proactive, resilient, and integrated into all aspects of business.
Attacks will happen possibly frequently but those who heed the data

can drastically reduce their odds of a catastrophic event. Itʼs about
converting lessons from numbers into action: each percentage or
dollar figure is a signpost of where to shore up defenses or allocate
budget. The numbers tell us: invest in AI and skilled staff, assume
breaches via phishing or supply chain will happen and plan
accordingly, never underestimate human error, and donʼt wait the
threat environment is worsening, so the cost of inaction or slow
action is climbing.
Best Practices for 2025 and Beyond
Based on the statistics and trends weʼve explored, here are
actionable best practices that organizations should implement to
bolster their cybersecurity posture in 2025. Think of this as a
checklist derived from hard data each practice addresses a specific
weakness highlighted by the numbers:
1. Implement Multi Factor Authentication Everywhere: Since
credential theft is rampant 16% of breaches start with stolen
creds, require MFA for all user and admin logins especially for
remote access, VPNs, email, and critical applications. Favor
phishing resistant MFA methods hardware security keys or push
app prompts over SMS. This wonʼt stop all attacks, but itʼs a
strong speed bump, Microsoft reports MFA can block 99% of
automated account attacks.
2. Adopt a Zero Trust Approach: Donʼt trust any connection by
default internal or external. Segment your network so that
compromise of one system doesnʼt grant open access to others
contain lateral movement. Use least privilege for user and service
accounts staff and applications should only have the minimum
access they need. Verify device security posture before allowing

it onto the network especially BYOD devices, given 46% of
devices with corporate creds are unmanaged. Essentially, verify
explicitly every user, device, and transaction. Start with high risk
areas: e.g., require re auth when accessing finance systems even
from internal network, or implement microsegmentation in your
data center for sensitive workloads.
3. Continuous Security Monitoring and Faster Detection: Given
breaches can go undetected for months, invest in 24x7
monitoring tools and services. Deploy an EDR Endpoint Detection
& Response solution on all endpoints to catch suspicious behavior
like unknown processes, lateral movement attempts. Use a
SIEM/SOAR platform to aggregate logs from network, cloud, and
endpoints and leverage detection rules, possibly AI driven to spot
anomalies. If budget is an issue for in-house SOC, consider a
managed detection and response MDR service. Also, actively
hunt for threats in your environment, donʼt just wait for alerts.
Threat hunting can find stealthy intrusions important since
median dwell time was 11 days in Mandiantʼs data, so thereʼs a
window to catch them. Aim to bring down detection + response
time to days or hours instead of weeks.
4. Regular Patching and Vulnerability Management: The spike in
exploitation of known vulns 20% of breaches means basic cyber
hygiene like patching is crucial. Maintain an up to date inventory
of all software/hardware. Subscribe to threat intelligence for new
vulnerabilities CVE feeds and prioritize patching critical ones
especially those that are being actively exploited in the wild many
attacks in 2025 hit known unpatched flaws. If you canʼt patch
immediately e.g., operations constraints, use mitigations: virtual
patching via WAF/IPS, segmentation, or disabling vulnerable
services. Also, harden configurations disable unused services,
enforce least functionality. Donʼt forget to update things like VPN
and network device firmware, as those were big targets in 2025.
Many breaches are preventable by closing doors that attackers
commonly exploit.
5. Back Up Data and Practice Restores: With ransomware so
prevalent, offline, secure backups are your lifeline. Regularly back
up critical systems and data, and ensure at least one backup
copy is offline or immutable so attackers canʼt encrypt or delete
it. Just as important: test your backups and restoration process
frequently. Statistics show many who paid ransoms could have
restored if backups were better. So verify that backups are
complete, uncorrupted, and you know how long a full restore
takes. Include key systems: databases, file servers, and also
configuration data network device configs, etc.. If hit by
ransomware, you want to be confident that you can rebuild

systems from scratch and recover data without paying. Also
consider snapshotting critical virtual machines and using cloud
backup services many modern attacks try to find and wipe out
backups, so use solutions with strong access controls.
6. Educate and Phish Test Your Workforce: Since phishing is the
top entry point 3.4 billion phishing emails sent per day globally,
train employees regularly on how to spot phishing and social
engineering. Use real world inspired phishing simulation
campaigns to gauge who clicks and then coach them. Encourage
a culture where employees report suspicious emails or activity
make it easy like a Report Phish button in email client. Also,
educate beyond email: include vishing phone scams, smishing
text scams, and attacks via social media. Given the rise of AI
deepfakes, educate high risk personnel like finance, HR to verify
unusual requests through a second channel e.g., if a CEO calls
asking for a wire, call them back on a known number. The goal is
to reduce that 16% of breaches that start with a phish. While you
canʼt get to zero clicks, you can lower the odds and maybe
ensure employees report it quickly if they do click speeding
response.
7. Secure Your Supply Chain and Third Parties: First, identify your
critical suppliers and partners especially those with network or
data access. Perform due diligence: ask them about their
security. Do they follow standards like ISO 27001, SOC 2? Do they
do pen tests?. Where feasible, include security requirements in
contracts e.g., vendor must notify us within 48 hours of a breach
affecting our data. Technically, limit what third party accounts can
do on your systems, use dedicated vendor access accounts that
can be disabled when not in use, and monitor their activity
closely, consider requiring MFA for them too via your access
gateways. For software supply chain: verify hashes/signatures of
software updates, use dependency management for open source
to avoid pulling in poisoned packages, and apply updates to third
party components promptly like libraries, Docker images. If using
cloud/SaaS providers like the Salesforce example, regularly
review connected apps and revoke those not needed. Also,
implement zero trust for APIs donʼt assume trust because itʼs
internal traffic if itʼs between services. In short, trust but verify
every partner and software component.
8. Incident Response Plan and Drills: Develop a clear Incident
Response IR plan that outlines what to do in various scenarios
e.g., ransomware outbreak, data breach, DDoS attack. Identify
roles who is the decision maker, who interacts with law
enforcement, who handles PR. Include communication plans with
backups, assume email or IT may be down during an incident,

have out of band contacts. Practice this plan at least annually via
a tabletop exercise or even a full simulation. The IBM stat that
companies with IR teams and tested plans save ~$2.66M on
average per breach shows how valuable this is that stat was from
prior reports. In particular, rehearse a ransomware scenario:
decide in advance your stance on paying or not. FBI advises not
to pay, but itʼs a business decision. Having a plan reduces chaos
under pressure and ensures faster containment. Also, ensure you
have relationships established with key external partners: a digital
forensics firm you can call, legal counsel for breach notification,
and law enforcement contacts. An IR plan is like a fire drill you
hope to never need it, but when a real fire happens, it can save
your proverbial life or at least a lot of money and reputation.
9. Protect Data on All Fronts Data Governance: Implement Data
Loss Prevention DLP tools to monitor and block sensitive data
exfiltration via email, web, or USB. With many breaches involving
data theft, DLP can act as a tripwire or prevention for unusual
data movement. Also, maintain an inventory of your sensitive data
and apply classification public, internal, confidential, highly
confidential, enforce encryption and access control accordingly.
For cloud data, ensure cloud storage buckets are private by
default and use cloud security posture management CSPM tools
to catch misconfigurations. Mask or tokenize personal data in non
production environments to avoid leaks from test databases. The
principle is least privilege for data too, not everyone should
access everything. If you had a breach, youʼd want as little
sensitive info accessible as possible. Also consider employing
Privacy Enhancing Technologies if relevant, like homomorphic
encryption or data anonymization for analytics, so even if data is
accessed itʼs not in clear form.
10. Maintain an Updated Response to Emerging Threats: The threat
landscape evolves quickly. Best practices today may need
updating tomorrow. Stay informed through threat intelligence
feeds, industry groups, and by following cybersecurity news e.g.,
subscribe to CISA alerts, vendor threat reports. When you learn
of a new widespread threat like a severe zero day exploit or a new
phishing scam type, be agile: patch immediately or issue an
advisory to your staff as needed. For example, if a critical
vulnerability PrintNightmare or ProxyShell etc. is revealed, have a
process to fast track patch testing and deployment. Or if thereʼs
news of an attack campaign targeting, say, Office 365 via a
particular phishing method, use that intel to reinforce training or
adjust email filters. A best practice is conducting routine cyber
risk assessments in light of current threats e.g., simulate a breach
via a red team or at least run automated penetration tests to find

weaknesses before attackers do. Finally, consider aligning with
security frameworks like NIST CSF or ISO 27001 they provide a
comprehensive set of controls and processes that, if followed,
inherently cover many best practices.
By implementing these best practices, an organization will address
the most common and damaging attack vectors highlighted in
2025ʼs statistics. Itʼs a multi-layered approach: secure the identity
MFA, least privilege, secure the infrastructure patching, monitoring,
zero trust, secure the data backups, encryption, DLP, and prepare to
respond IR plan, user training. No defense is 100%, but these
measures collectively can prevent the majority of opportunistic
attacks and significantly mitigate the impact of sophisticated ones.
Remember, cybersecurity is a continuous process regularly review
and update these practices as new data and threats emerge.
Frequently Asked Questions about Cybersecurity Statistics 2025
How much will cybercrime cost the world by 2025?
Cybercrime is projected to cost the world about $10.5 trillion
annually by 2025. This staggering figure includes the damage from
theft of money and IP, fraud, ransomware, business disruption, and
recovery efforts. To put it in perspective, if cybercrime were a
country, its GDP $10.5T would make it the third largest economy
globally, behind the U.S. and China. In 2015, cybercrime damages
were estimated around $3 trillion, so the growth has been explosive
reflecting how as we digitize more of the economy, cybercriminals
have more opportunities. By 2031, forecasts go even higher around
$12 trillion as cybercriminal enterprises continue to scale up. The
bottom line: cybercrime has become a huge economic drag and
companies need to invest in cyber defenses to avoid contributing to
that cost.
What is the average cost of a data breach in 2025?
Globally, the average cost of a data breach in 2025 is about $4.44
million. This is actually a slight decrease from the 2024 average of
$4.88M, thanks in part to faster response times and wider use of
security AI. However, the cost varies a lot by region. In the United
States, the average breach cost reached $10.22 million, the highest
on record for any country. High costs in the U.S. are driven by
factors like notification laws, legal expenses class action lawsuits,
and high customer turnover after breaches. In contrast, Europeʼs
average is around $4M e.g., UK $4.14M and places like Latin

America or India often see lower averages, sometimes $2–3M due to
different economic impact and response costs. Itʼs important to note
these figures include both direct costs forensics, technology,
regulatory fines and indirect costs lost business due to reputational
damage. Also, certain industries skew higher e.g., healthcare
breaches average $7M+ globally, and financial services around
$5M.
How often do cyberattacks happen?
Cyberattacks are extremely frequent. Various statistics suggest
hundreds or thousands of attacks occur every day. One analysis of
FBI complaint data indicated a cyber attack or at least a reported
cyber incident happens roughly every 39 seconds on average.
Another way to look at it: Forbes reported that hackers make about
2,200 attempts per day on an average organization, which is about
one attack every 39 seconds as well. At a global scale, that
translates to tens of thousands of attacks per day. In fact, in 2023,
the FBI received 859,000 cybercrime reports which averages to
about one incident reported every 37 seconds. Itʼs also said that
hackers attack around 26,000 times a day worldwide which is one
every ~3.3 seconds. Keep in mind these range from minor phishing
attempts to major breach attempts. Automated bots are constantly
scanning and attacking targets on the internet, so any exposed
system will likely see some kind of attack within minutes of going
online. The takeaway: attacks are essentially continuous, so
defenses and monitoring must be as well.
Which industries have the highest data breach costs?
The Healthcare industry has the highest data breach costs of any
sector. In 2025, the average breach in healthcare cost about $7.42
million globally. Healthcare has led in cost for over a decade
because medical data is very sensitive and valuable on the black
market, plus healthcare organizations often canʼt afford downtime
life critical services. After healthcare, the next highest is typically
Financial Services, with average breach costs often in the $5–6
million range. Financial firms are lucrative targets money and
financial data at stake and face heavy regulation. Other industries
with higher than average costs include Pharmaceuticals and
Technology, often due to intellectual property value. Manufacturing
and Energy breaches have high costs mainly when operations are
disrupted ransomware causing factory downtime can be very
expensive. By contrast, sectors like Retail or Hospitality might have
lower per-incident costs around $3–4M average because the data
compromised like credit cards can be quickly changed, though they

often involve large volumes of records. Itʼs also worth noting
government breaches, while not calculated the same way for cost,
can be very impactful security clearances, citizen data, etc.. But
strictly by reported cost, Healthcare is #1, Finance #2, then probably
sectors like Industrial, Tech, and Energy vying for #3 depending on
the year.
What is the main cause of data breaches in 2025?
The majority of data breaches have a human element at their core.
In 2025, about 68% of breaches involved some form of human error
or social engineering. If we break it down by initial attack vector:
Phishing is the leading cause, accounting for roughly 16% of
breaches as the first point of entry. Phishing emails trick employees
into giving up credentials or clicking malware, so itʼs a huge factor.
The next most common causes are things like compromised
credentials, stolen passwords, ~10% of breaches, and third party or
supply chain compromises ~15% of initial vectors. Also notable is
system vulnerabilities unpatched software leading to breaches was
on the rise, representing about 20% of breaches in 2025 as an initial
vector. But even those often tie back to human factors not patching
in time, misconfigurations. Insider incidents intentional or accidental
data misuse by employees also occur, but are a smaller slice around
8% malicious insiders in IBMʼs study. So, in summary, the main
causes are phishing/social engineering, use of stolen credentials,
and exploits of vulnerabilities or poor security processes. Almost all
of those can be traced to human mistakes at some level falling for
scams, using weak passwords, not updating systems, etc.. Thatʼs
why security training and process discipline are so important.
How are hackers using AI in cyberattacks in 2025?
Hackers have started to use Artificial Intelligence to enhance their
attacks in a few ways. A recent IBM report noted that 16% of data
breaches involved attackers using AI tools at some stage. The
primary use is in phishing and social engineering: attackers use
generative AI like advanced language models to craft very
convincing phishing emails that are grammatically perfect and
contextually tailored often in the victimʼs native language and even
mimicking a personʼs writing style. This increases the success rate
of phishing, since the usual red flags, bad grammar/spelling, odd
phrasing are gone. Additionally, AI is used to create deepfake
content for example, cloning voices to bypass voice verification or
making fake videos/images for extortion or misinformation. In
breaches where AI was involved, 37% of those attacks used AI
generated phishing content, and 35% used deepfake

impersonations. Another way attackers use AI is to automate the
discovery of vulnerabilities using ML to scan code or network traffic
patterns for weaknesses faster than a human. On the flip side,
defenders are also using AI heavily to detect anomalies and respond
at machine speed. But criminals have access to many of the same AI
tools which are often open source or easily accessible. We even saw
instances of malware in 2025 that had AI routines to evade detection
e.g., adapting its behavior if it sensed it was in a sandbox. So, in
summary: hackers use AI to scale up social engineering, create
convincing fake content for scams or evading security checks, and
potentially to automate parts of their hacking finding paths of least
resistance. This trend is likely to grow, basically turning cyber
attacks into an AI vs. AI battle in some cases.
How large is the cybersecurity talent shortage in 2025?
The cybersecurity industry is facing a significant talent shortage in
2025. Globally, there is an estimated gap of about 4.8 million unfilled
cybersecurity jobs. This is the number of additional trained
professionals needed to adequately defend organizations. The gap
has been growing itʼs up roughly 19% from the previous year 2024
when it was around 4 million. The total cybersecurity workforce in
2025 is about 5.5 million people, but the demand is for over 10
million, hence the shortfall. Regionally, the largest gaps are in the
Asia Pacific region particularly in populous countries like India which
needs hundreds of thousands more professionals. North America
has around 700k open roles, and Europe around 250k–500k
depending on estimates. The shortage exists at all levels, but
especially in roles like cloud security, incident response, and
security engineering. One concerning stat: 33% of organizations say
budget constraints are now the top reason they canʼt fill cyber
positions meaning some companies want more staff but canʼt afford
them, and others simply canʼt find qualified people for the salary
they offer. The implications of this gap are serious: overworked
security teams leading to burnout indeed over 50% of cyber
professionals report significant stress and potential security
oversights due to understaffing. Itʼs prompting more investment in
automation to do more with fewer people and creative solutions like
reskilling IT staff or hiring people with non-traditional backgrounds.
But until this gap closes, it remains a challenge as one report put it,
87% of organizations see themselves as having a shortage of cyber
skills internally.
The cybersecurity statistics of 2024–2025 paint a clear and urgent
picture: we are living through an era of unprecedented cyber
insecurity, where the scale and stakes of digital threats have risen to

macroeconomic and geopolitical significance. The data weʼve
explored shows both crisis and opportunity. On one hand, cyber
attacks are more frequent, sophisticated, and costly than ever with
global cybercrime damage soaring towards $10.5 trillion and
average breach costs hitting record highs in places like the U.S..
Ransomware and supply chain breaches have demonstrated their
power to disrupt critical services, from hospitals to pipelines to
software supply chains, underscoring that no sector is immune. On
the other hand, the statistics also illuminate a path forward:
organizations that invest in smart defenses, AI, automation, zero
trust architectures and cultivate a culture of security and resilience
are seeing tangible reductions in risk and impact.
Several strategic themes emerge from the numbers:
AI is Mandatory The competitive edge in cybersecurity now often
comes from leveraging Artificial Intelligence and machine
learning. Companies fully deploying AI driven security saw a 34%
cost reduction in breaches, making it clear that automation is the
only viable way to keep up with machine speed attacks and to
augment overstretched human teams. However, the advent of
attacker AI from deepfake phishing to AI written malware means
defenders must also govern AI use wisely and develop counter AI
strategies.
Zero Trust as the New Normal The failure of perimeter centric
security models is evident when phishing and stolen credentials
remain so successful. A Zero Trust approach never trust, always
verify directly addresses many of the weak points highlighted by
the stats requiring continuous verification thwarts many phishing
based credential attacks, and microsegmentation limits the
damage if an intruder does get in. As breaches via third parties
and cloud misconfigurations grew, Zero Trust principles like strict
identity verification and least privilege are increasingly seen as
the standard architecture for resilience.
Resilience Over Prevention We must acknowledge that
determined adversaries or inadvertent mistakes will occasionally
bypass even good defenses. Thus, the focus shifts to cyber
resilience, the ability to minimize damage and recover quickly.
The data shows more organizations refusing ransom demands
and still restoring operations, a heartening sign of resilience.
Breach lifecycle has shortened, indicating better incident
response. Strategies like regular drills, strong backups, and
having incident response partners on retainer can mean the
difference between a bad day and an existential crisis when a
breach occurs. In 2025, many organizations started to measure

success not just by did we keep threats out? but when a threat
got in, did our systems absorb the shock and continue running?
Collaborative Defense and Regulation The immense scale of
cyber threats has prompted greater collaboration across
industries and with government. Public private information
sharing has improved e.g., CISA alerts, sector ISACs, which is
reflected in faster response to widespread threats like critical
vulnerabilities. Regulators around the world have raised the bar:
hefty GDPR fines in the EU, new SEC disclosure rules in the US,
and critical infrastructure cyber laws in various countries. These
moves, driven by the statistical reality of growing breaches, aim
to enforce baseline security hygiene and transparency. The
implication is that cybersecurity is no longer optional or just an IT
cost center, itʼs a legal and strategic imperative, backed by
regulatory teeth.
As we look ahead to the coming years, the convergence of trends
suggests an even more challenging landscape. The possible
weaponization of emerging technologies from quantum computing
potentially breaking current encryption in the future, to autonomous
AI agents conducting attacks or defenses at speeds humans can
hardly comprehend will define the next frontier of cybersecurity. The
complete digitization of critical infrastructure smart cities, IoT
everywhere means the stakes will include not just data and money,
but public safety and national security. The cyber domain is poised
to remain the most dynamic and consequential battlefield of the
modern world.
Yet, there is reason for cautious optimism: the same data that charts
the growth of threats also illuminates solutions. By studying these
statistics and trends, business leaders, policymakers, and security
professionals can make data driven decisions to strengthen their
defenses. The 2025 landscape shows that organizations who
proactively invest in security technology, foster skilled and alert
teams, and plan for worst case scenarios fare markedly better in
cyber resilience metrics than those who do not.
In conclusion, the cybersecurity statistics of 2025 are a clarion call
to action a call to innovate in defense as fast as adversaries innovate
in offense, a call to break down silos and treat cybersecurity as a
shared responsibility across enterprises and nations, and a call to
build a digital world where insecurity is managed and minimized, if
never completely eliminated. The volatility of the cyber era can be
navigated successfully with insight, preparation, and agility. The
data driven insights in this report aim to equip stakeholders with the
knowledge to do exactly that: anticipate the threats, quantify the

risks, and act decisively to mitigate them in the turbulent yet
opportunity filled years ahead.
References:
1. Cybersecurity Ventures Cybercrime to Cost the World $10.5
Trillion Annually by 2025
2. DeepStrike.io Cybercrime Statistics 2025: $10.5T Losses &
Shocking New Statistics
3. IBM Security Cost of a Data Breach Report 2025 The AI Oversight
Gap
4. Varonis 139 Cybersecurity Statistics and Trends [updated 2025]
5. NordLayer Cybersecurity statistics 2025: figures, stories, and
what to do next
6. HIPAA Journal Average Cost of a Healthcare Data Breach Falls to
$7.42 Million 2025
7. Verizon Data Breach Investigations Report DBIR 2024
8. FBI IC3 Report 2024 Internet Crime Report FBI.gov
9. Interpol Africa Cyberthreat Assessment Report 2025
10. DeepStrike.io Cybersecurity Skills Gap: 4.8M Roles Unfilled,
Costs Surge 2025
11. SentinelOne Key Cyber Security Statistics for 2025
12. Netscout Egypt Cyber Threat Intelligence Report 1H 2025
13. BrightDefense List of Recent Data Breaches in 2025
About the Author
Mohammed Khalil is a Cybersecurity Architect at DeepStrike,
specializing in advanced penetration testing and offensive security
operations. With certifications including CISSP, OSCP, and OSWE,
he has led numerous red team engagements for Fortune 500
companies, focusing on cloud security, application vulnerabilities,
and adversary emulation. His work involves dissecting complex
attack chains and developing resilient defense strategies for clients
in the finance, healthcare, and technology sectors.