The Salesforce Threat
Landscape
Lessons and Risks for 2026

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | The Salesforce Threat Landscape 2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2 (40) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Table of contents
Executive summary � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � 3 Emerging Salesforce Attack Surfaces: Agents, Automation, and Data Flows   � � � � � � � � � � � � � � 28
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Agents as Autonomous Actors  |     |     |     |  � � | � � � � � | � � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ---- | --------- | ------- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- |
29
| Salesforce Data as a High-Leverage Target  |     |     |     |  � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | ------ | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Automation as an Amplification Layer  |     |     |     |     |  � � | � � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---- | ------- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- |
30
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Data as an Input to Automated Decision-Making  |     |     |     |     |     |     | �   | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- |
31
| WithSecure Cloud Protection for Salesforce: Detection Telemetry and Threat Patterns  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |  � � � | � � | � � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6
|                                             |     |     |     |     |     |       |     |       |     |       |     |       |     |       |     |       |     |       |     |     | Proof-of-Concept: ForcedLeak  |     |     |     |  � � | � � � � � | � � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � 32 |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | ----------------------------- | --- | --- | --- | ---- | --------- | ------- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | ------ |
| Malicious Detection Rates Observed in 2025  |     |     |     |     |  �  | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � |     |     |                               |     |     |     |      |           |         |     |       |     |       |     |       |     |       |     |       |     |       |        |
6
|                                                       |     |     |     |     |     |     |      |       |     |       |     |       |     |       |     |       |     |       |     | Salesforce Platform Security-Related Changes  |     |     |     |     |      |           |  � �    | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � � 34 |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --------------------------------------------- | --- | --- | --- | --- | ---- | --------- | ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ |
| Geographic Distribution of Affected Organizations     |     |     |     |     |     |     |  � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | 7   |                                               |     |     |     |     |      |           |         |       |       |       |       |       |       |       |       |       |       |       |       |        |
| Distribution of Malicious Detections by Content Type  |     |     |     |     |     |     |  �   | � �   | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | 8   |                                               |     |     |     |     |      |           |         |       |       |       |       |       |       |       |       |       |       |       |       |        |
|                                                       |     |     |     |     |     |     |      |       |     |       |     |       |     |       |     |       |     |       |     | Mitigation and Recommendations                |     |     |     |     |  � � | � � � � � | � � � � | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � �  |
35
| Top Detections Observed in 2025  |     |  � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | ---- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
| Adversary-in-the-Middle (AitM) Quishing Campaign  |     |     |     |     |     |     |  �  | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Conclusion  |     |  � � � | � � � � � | � � � � � | � � � � � | � � � � � | � � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --------- | --------- | --------- | --------- | ------- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- |
39
| Publicly Reported Incidents  | �  � � � | � � � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | -------- | --------- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20
| Identity-Based Access Abuse (Gehenna)                 |     |     |     |  �  | � � � | � � | � � � | � �    | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � � | 21  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | ----- | --- | ----- | ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OAuth Device Flow Authorization Abuse (UNC6040)       |     |     |     |     |       |     |  �    | � �    | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � | 22  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| Supply-Chain Compromise: Salesloft Drift Integration  |     |     |     |     |       |     |       | �  � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � � | � �   | � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
24
| Supply-Chain Compromise: Gainsight Integration � � |     |     |     |     |     |     | �   | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
25
| AitM Vishing Attacks Targeting SSO Identities  |     |     |     |     |  �  | � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
26
| Salesforce as an Extortion Target in Leak-Site Campaigns  |     |     |     |     |     |     |     |     | �  � | � � � | � � | � � � | � � | � � � | � � | � � � | � � | � � | 27  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

The Salesforce Threat Landscape 2026 3 (40)
Executive summary
In 2025, Salesforce environments reinforcing how Salesforce environments instance, identity risks increasingly manifest
became direct targets of sophisticated, inherit risk from upstream identity not only at login time, but also through
financially motivated cybercrime decisions even in the absence of platform delegated, persistent, and non-human
groups� Historically, most Salesforce vulnerabilities� execution contexts�
security incidents were associated with
misconfigurations or vulnerabilities WithSecure Cloud Protection for Salesforce This report analyses the Salesforce threat
identified by security researchers. Over the detection telemetry reinforces this landscape in 2025 using WithSecure
past year, however, multiple incidents and perspective, showing a growing prevalence Cloud Protection for Salesforce detection
extortion-driven campaigns demonstrated of URL-driven threats delivered through telemetry alongside publicly disclosed
deliberate targeting of Salesforce data as routine business workflows, including incidents� It examines why Salesforce
a high-leverage asset. embedded links and QR code lures� These data has become a high-leverage target,
attacks increasingly blend into expected documents key attack paths observed
Rather than exploiting platform operational activity and extend beyond during the year, and assesses emerging
vulnerabilities, attackers relied on social file-based malware, with files most often risks introduced by automation and agent-
engineering, credential theft, OAuth token acting as containers for malicious links based capabilities� The report concludes
misuse, and supply-chain compromise� rather than the threat itself� with governance-aligned defensive
These techniques enabled access to considerations for teams responsible for
sensitive customer and business data by At the same time, Salesforce continued to Salesforce integration, oversight, and risk
abusing legitimate access paths and expand its platform capabilities through management�
delegated trust� Recent threat activity automation, agent-based execution, and AI-
further highlights how adversary-in-the- driven workflows. While these capabilities
middle phishing can undermine MFA deliver significant business value, they also AUTHOR
Karmina Aquino
protections at the identity provider layer, introduce new security considerations� For
Head of Threat Intelligence,
WithSecure Cloud Protection
for Salesforce

Salesforce Data as a High-Leverage
Target
Salesforce has evolved far beyond its origins as a customer relationship
management platform. For many organizations, it now functions as a central
system of record for customer data, revenue operations, contractual
relationships, and support workflows. Salesforce environments are deeply
integrated with internal systems, cloud services, and third-party vendors
through APIs and OAuth-based authorization mechanisms.
This evolution has expanded both the value and the attack surface of
Salesforce. While traditional enterprise security models focused on perimeter
defences and endpoint compromise, Salesforce environments expose data
primarily through identity, application trust, and automation.

The Salesforce Threat Landscape 2026 5 (40)
Extortion Economics and High-Trust Access Paths
Modern cybercrime is mostly
financially driven. Threat actors
increasingly prioritize techniques
that maximize leverage while
minimizing operational cost and
Due to this, attackers Salesforce environments Salesforce also
exposure per intrusion. Extortion
seek platforms that: align closely with these presents attackers with
economics favour data theft over
criteria. They commonly attractive operational
service disruption.
contain: characteristics:
• Store sensitive and regulated
data
• Are critical to business • Personally identifiable • API-driven access that blends
operations information (PII) governed into normal business activity
• Cause pressure through legal, by GDPR, CCPA, and similar • OAuth tokens that bypass
regulatory, or reputational regulations interactive authentication
consequences • Sales forecasts, pipeline data, • Integration models that
and contractual and pricing assume long-term trust
information
• Customer communications and These reduce the chances
support records of immediate detection and
increase dwell time once access
Access to this data enables is obtained�
attackers to apply pressure
without the need to deploy
ransomware nor to disrupt
systems�

|     |     |     | The Salesforce Threat Landscape 2026 |     | 6 (40) |
| --- | --- | --- | ------------------------------------ | --- | ------ |
WithSecure Cloud Protection for Salesforce: Detection
Telemetry and Threat Patterns
Malicious Detection Rates Observed in 2025
Based on telemetry from WithSecure  The acceleration was most evident in Q3  The observed upward trend also indicate
Cloud Protection for Salesforce, malicious  and Q4, possibly reflecting a combination  improvements in detection visibility
detection activity increased consistently  of heightened attacker activity, broader  over time, as additional detection logic
throughout 2025, with growth accelerating  detection coverage, and introduction of  and coverage enabled threats that may
in the second half of the year and reaching  new detection mechanisms� Detections  previously have gone unnoticed to be
+75%
| a level in Q4 that was approximately eight  | during this period align with several publicly  |     | identified. |     |     |
| ------------------------------------------- | ----------------------------------------------- | --- | ----------- | --- | --- |
| times higher than in Q1 when measured       | reported, high-profile Salesforce-related       |     |             |     |     |
| across all scans�                           | incidents, suggesting increased adversary       |     |             |     |     |
focus on the platform�
+77%
|     | Q1   | Q2   |     | Q3   | Q4   |
| --- | ---- | ---- | --- | ---- | ---- |
|     | 2025 | 2025 |     | 2025 | 2025 |

|     |     |     | The Salesforce Threat Landscape 2026 |     |     | 7 (40) |
| --- | --- | --- | ------------------------------------ | --- | --- | ------ |
Geographic Distribution of Affected Organizations
Organizations that experience malicious  While malicious detections were observed  This pattern may reflect the prevalence of
detections during 2025 were distributed  worldwide, a significant share of affected  attack techniques such as phishing, which
across all major geographic regions,  organizations was concentrated in a  often rely on language and impersonation of
| indicating that malicious activity targeting    | small number of countries� The three             |     | trusted services� |     |     |     |
| ----------------------------------------------- | ------------------------------------------------ | --- | ----------------- | --- | --- | --- |
| Salesforce environments was not confined        | most frequently affected countries during        |     |                   |     |     |     |
| to a specific location. Affected organizations  | 2025 were the United States, the United          |     |                   |     |     |     |
| were observed in North America,                 | Kingdom, and Australia, which together           |     |                   |     |     |     |
| Europe, Asia-Pacific, and other regions,        | accounted for approximately 53�5% of             |     |                   |     |     |     |
| underscoring the global nature of the threat    | affected organizations. All three are primarily  |     |                   |     |     |     |
| activity captured in the telemetry�             | English-speaking regions�                        |     |                   |     |     |     |
ASIA-PACIFIC AFRICA
7.79% <1%
| EUROPE |     | NORTH AMERICA |     | OCEANIA | SOUTH AMERICA |     |
| ------ | --- | ------------- | --- | ------- | ------------- | --- |
| 41.56% |     | 38.96%        |     | 10.39%  |               | <1% |

The Salesforce Threat Landscape 2026 8 (40)
Distribution of Malicious Detections by Content Type Observed Patterns in Malicious URLs
Most malicious detections observed in 2025 were associated with URLs rather than files. Analysis of malicious URLs observed in In many cases, even when the underlying
Approximately 98% of all malicious detections were URL-based, while file-based detections Salesforce environments during 2025 shows domain persisted over time, the specific URLs
accounted for a comparatively small share of observed activity� This distribution indicates that that attacker infrastructure spanned a wide or subdomains used for malicious activity
malicious activity targeting Salesforce environments during this period relied primarily on web- range of domain ages. Newly registered were short-lived� Attackers frequently rotated
based delivery mechanisms rather than file-borne malware. domains were commonly associated with these components to support individual
fast-moving phishing campaigns, while campaigns, limit exposure, and evade simple
longer-lived domains were often reused or blocking approaches�
FILE
repurposed to support multiple attack efforts.
1.74%
This highlights the importance of using Across all observed age ranges, malicious
domain age as part of a broader set of URL domains frequently followed similar naming
evaluation signals� patterns, including:
• Programmatically generated domains
containing high-entropy strings
> 90 91.58 %
• Domains constructed from randomly
61 - 90 5.31 %
combined, dictionary-style words
31 - 60 0.66 %
• Domains that combine random elements
with well-known brand names or account-
15 - 30 0.29 %
related terms
8 - 14 0.78 %
Taken together, these observations show
<_ 7 1.39 %
that malicious URL infrastructure spans both
URL
newly registered and longer-lived domains,
Domain Age Distribution (Days)
98.26%
reflecting different operational approaches
attackers use to blend into routine business
activity over time�

The Salesforce Threat Landscape 2026 9 (40)
Observed Patterns in Malicious Files
Among malicious file detections, PDF and embedded URLs were tailored to
documents accounted for the largest share, closely resemble the templates, workflows,
IMAGE
followed by Microsoft Word and Excel and service endpoints of the target OTHERS
3.66%
files, with smaller proportions associated organizations. In these cases, attackers 4.40%
ARCHIVE
with archive formats, images, and other used professionally branded documents
3.74%
file types. These formats closely resemble and URL structures that mimicked
common enterprise documents routinely legitimate enterprise services, despite
EXCEL
exchanged through Salesforce-related being hosted on attacker-controlled
9.37%
workflows. domains. This level of fidelity suggests
prior reconnaissance and reflects an intent
Notably, approximately 98.9% of to blend malicious content seamlessly
malicious file detections involved into the organization’s normal operational
embedded malicious URLs contained context�
WORD
within otherwise legitimate-looking
10.54%
documents� Rather than serving as These findings reinforce that URL-based
malware delivery mechanisms themselves, threats remain the dominant driver of
files overwhelmingly functioned as trusted malicious activity observed in Salesforce
containers for URL-based attacks. This environments in 2025� Files, while less
pattern highlights how attackers continue frequently identified as malicious, can still
to favor web infrastructure and social serve as an effective conduit for URL-based
PDF
engineering, even when using files as an attacks, particularly when embedded links 68.29%
intermediate step to introduce malicious are used to redirect users to credential-
content� harvesting or malicious web content�
Detection telemetry also included
instances of highly targeted social
engineering, where malicious documents

The Salesforce Threat Landscape 2026 10 (40)
Top Detections Observed in 2025
Approximately 95% of malicious files perceived as legitimate business artifacts,
and URLs detected in 2025 were and links embedded within documents
MALICIOUS:NETWORK/GENERIC.U
identified using just two detection often appear less suspicious than
1%
types� These dominant detections were standalone URLs, increasing the likelihood
MALICIOUS:NETWORK/DOCUMENT.A
primarily associated with malicious URLs that they will be trusted and acted upon�
1%
used in social engineering, phishing,
OTHERS
and credential-harvesting campaigns� The distribution of top detections reinforces
MALICIOUS:NETWORK/GENERIC.W
1%
In other cases, detected URLs pointed a consistent theme observed throughout
2%
to infrastructure hosting malicious 2025: malicious activity targeting
MALICIOUS:NETWORK/GENERIC.D
content, including sites used for drive-by Salesforce environments was largely driven
13%
downloads, delivery of malicious binaries, by URL-based threats, whether delivered
or command-and-control activity� The directly or indirectly through documents�
prevalence of these detections reflects
the continued reliance on web-based
infrastructure that can be rapidly deployed,
modified, and reused across multiple
campaigns�
Nearly all malicious document detections
involved embedded malicious links� In
these cases, the document acted as an
initial delivery mechanism, with URLs
identified during file analysis rather than
MALICIOUS:NETWORK/GENERIC.A
through direct user interaction� Attackers
83%
commonly use this approach because
document attachments are typically

The Salesforce Threat Landscape 2026 11 (40)
Examples of Observed Malicious Content
The following examples illustrate how these dominant detections manifested in
real-world attacks observed from WithSecure Cloud Protection for Salesforce
detection telemetry during 2025.
Cloud Storage Phishing
Malicious:Network/Generic.A
This detection triggered due to a URL from a phishing message impersonating a
legitimate iCloud storage notification, warning recipients that they are nearing their
storage limit� The message prompts users to follow a link to upgrade their plan, which
redirects to a credential-harvesting page masquerading as an Apple login portal�
Fake iCloud storage notification leads to a phishing page

The Salesforce Threat Landscape 2026 12 (40)
Malicious Application Delivery Site
Malicious:Network/Generic.D
This detection triggered due to a URL that prompted users to download a mobile
application package from an untrusted source. The malicious app from this URL spies
on user activities, collects personal information such as the user’s contacts, SMS
messages, call logs, and device information, and uploads this data to the attacker’s
command-and-control server�
User is led to a website hosting malicious apps

The Salesforce Threat Landscape 2026 13 (40)
Multi-stage Salesforce Phishing
This detection also triggered due to a URL from a phishing email impersonating a Salesforce
notification, prompting recipients to review an issue via an embedded link. The link redirects to
a fraudulent Salesforce login page designed to collect credentials and subsequently presents a
fake multi-factor authentication prompt, enabling attackers to capture additional authentication
information�
Phishing email link leads to a fake Salesforce login page

The Salesforce Threat Landscape 2026 14 (40)
Adversary-in-the-Middle (AitM) Quishing Campaign
Detection telemetry from 2025 shows sustained activity associated with QR code phishing or
quishing campaigns that leveraged adversary-in-the-middle (AitM) techniques to compromise
user identities� These were commonly delivered through email and other routine business
communications, using QR codes to shift user interaction away from traditional links�
The observed campaigns primarily used QR codes embedded in messages that mimicked routine
enterprise communications impersonating trusted internal departments or widely used third-party
services to increase credibility. Common lures included notifications related to:
• Confidential document delivery
• Internal policy updates
• Account or login revalidation requests
• Compensation or payment-related messages
• Missed communications such as voicemail or fax alerts
By prompting users to scan codes with mobile devices, attackers reduced visibility into the
destination URL and bypassed many traditional endpoint and email security controls that
focus on link inspection. This shift also moved the authentication flow away from the original
device, complicating detection and response�
Examples of actual quishing documents

The Salesforce Threat Landscape 2026 15 (40)
AitM Quishing Trend
FINLAND
1.60%
Telemetry indicates that these campaigns were most active during mid-2025, with a clear spike
AUSTRALIA
observed in July, followed by continued activity at lower levels through the remainder of the year�
1.60% SPAIN
Affected organizations were distributed across multiple regions, with the highest concentration
0.80%
observed in the United States. Detection coverage for these campaigns primarily included
NETHERLANDS
signatures associated with embedded QR codes and embedded links within documents, reflecting 7,20%
the delivery mechanisms used�
UNITED KINGDOM
11.20%
+119%
GERMANY
+200% 21.60%
UNITED STATES
58.00%
MAR APR MAY JUN JUL AUG SEP OCT NOV DEC
2025 2025 2025 2025 2025 2025 2025 2025 2025 2025

The Salesforce Threat Landscape 2026 16 (40)
AitM Quishing Detections
MALICIOUS:NETWORK/
QR.A
1.59%
MALICIOUS:NETWORK/
Telemetry associated with these quishing
DOCUMENT.A
campaigns also showed a clear preference
2.39%
for document-based delivery� The majority of
file-based detections linked to QR phishing
activity involved PDF documents, followed
by Microsoft Word files, with PNG appearing
only rarely� These formats align closely with
routine enterprise document workflows
and are well suited for embedding QR
codes or links while appearing legitimate to
recipients�
The use of commonly trusted document
types reinforces the social engineering
aspect of these campaigns, allowing
MALICIOUS:NETWORK/
attackers to introduce malicious QR codes DOCUMENT.Q
into Salesforce environments through 96.03%
files that resemble standard business
communications rather than overtly
suspicious content�
PDF WORD PNG
78.57% 19.84% 1.59%

The Salesforce Threat Landscape 2026 17 (40)
Use of AitM Phishing Infrastructure
Analysis of detected samples indicates the use
of the commercially available AitM phishing kit
commonly referred to as “Tycoon 2FA�” This kit
operate as a phishing-as-a-service offering
and is designed to intercept authentication
flows in real time.
Rather than simply collecting usernames and
passwords, AitM kits proxy authentication
requests between the victim and the legitimate
service� When users enter credentials and
complete multi-factor authentication, the kit
captures session cookies generated during
the process� Possession of these session
cookies allows attackers to access accounts
without requiring further authentication,
effectively bypassing MFA protections.
To reduce exposure to automated detection
and analysis, the observed infrastructure
implemented multiple pre-interaction checks�
These included CAPTCHA challenges, checks
Captcha leads to fake login pages, such as:
for automated scanners and known analysis
tools, and environment checks designed to
avoid security researchers or sandboxed
environments� Only after these checks were
satisfied would the phishing flow proceed.

The Salesforce Threat Landscape 2026 18 (40)
AitM Quishing Attack Flow
| Target user |                             | Attacker     |                              | Legitimate site |
| ----------- | --------------------------- | ------------ | ---------------------------- | --------------- |
|             | User inputs credentials in  |              | Attacker relays credentials  |                 |
|             | 2                           | Relay Server | 3                            |                 |
|             | phishing site               |              | to legitimate site           |                 |
1 User receives and
scans QR code,
eventually ending up
in phishing site.
Attacker prompts  Legitimate site
5 4
for MFA prompts for MFA
|     | User approves  |     | Attacker relays  |     |
| --- | -------------- | --- | ---------------- | --- |
|     | 6              |     | 7                |     |
|     | MFA challenge  |     | authentication   |     |
Attacker redirects user  Legitimate site returns
9 8
to different site session cookie

Implications for Salesforce Environments
Although the initial credential compromise occurs outside Salesforce,
successful AitM phishing can enable subsequent access to enterprise systems
that rely on federated identity, OAuth-based authorization, or trusted session
reuse. In Salesforce environments, this may lead to unauthorized access,
data exfiltration, or follow-on social engineering activity using compromised
accounts.

The Salesforce Threat Landscape 2026 20 (40)
Publicly Reported Incidents
In 2025, multiple publicly reported security incidents
indicated that organized cybercriminal groups increasingly
targeted Salesforce environments. In these cases, attackers
leveraged identity abuse, OAuth authorization mechanisms,
and trusted third-party integrations to gain access to
Salesforce data, often with the intent to monetize or exert
pressure through data exposure.

Identity-Based Access Abuse (Gehenna)
Timeline: Disclosed in May 2025
Initial Access Vector: Likely identity-based access
Impact: Bulk data exfiltration and resale in the underground markets
In mid-2025, a threat actor known as
Gehenna (or GHNA) publicly claimed to
have exfiltrated a large volume of CRM
data from an organization’s Salesforce
environment� The threat actor allegedly
stole tens of millions of CRM records
containing data such as account and
contact information and customer support
case logs� Gehenna published samples of
this data on the dark web forums to illicit
data trading and negotiation�

OAuth Device Flow Authorization Abuse (UNC6040)
Timeline: Mid-2025
Initial Access Vector: Social engineering leading to OAuth authorization
Impact: Data exfiltration and extortion through data brokers
Activity attributed to the threat actor as Data Loader and valid OAuth tokens,
group tracked as UNC6040 was allowing their activity to blend into normal
observed compromising multiple large operational patterns� Access was obtained
organizations’ Salesforce environments by convincing users to authorize attacker-
throughout mid-2025 and continuing controlled connected applications
into late 2025� The group conducted by abusing the OAuth Device Flow
targeted reconnaissance to identify authorization�
suitable victims and deliberately obscured
its activity using VPN and Tor. Data
access and exfiltration were staged to
minimize detection. Rather than exploiting
Salesforce platform vulnerabilities, the
actors relied on legitimate Salesforce
tooling and authorization paths, such

The Salesforce Threat Landscape 2026 23 (40)
Connected App via OAuth Device Flow Attack
1 Request device code
Attacker with Salesforce Token Target user
2 Return device code, user code, and verification uri
connected app Endpoint
4 Visit URL and enter
user code
3 Contact target user to ask them to visit the verification uri and enter the user code
5 Poll to check if user has authorized access
6 Return access token and identity URL
7 OAuth access to user’s Salesforce org
User’s Salesforce
Org

Supply-Chain Compromise: Salesloft Drift Integration
Timeline: March 2025
Initial Access Vector: Compromise of vendor development infrastructure
Impact: Unauthorized access to customers’ Salesforce data
According to the investigation, unauthorized
access to Salesloft Drift’s GitHub account
occurred between March and June
2025� During this period, the threat actor
conducted reconnaissance activity and
later accessed Drift’s AWS environment,
where OAuth tokens used for customer
integrations were stored� These tokens
were subsequently used to access
customer Salesforce data through legitimate
Drift integrations without the customer’s
authorization.

Supply-Chain Compromise: Gainsight Integration
Timeline: October 2025
Initial Access Vector: Undisclosed
Impact: Unauthorized access to customers’ Salesforce data
In November, Salesforce observed applications to connect to customers’
anomalous behaviour, including Salesforce environments� Possession of
reconnaissance against customers these tokens enabled access to customer
associated with compromised access tokens data without requiring authentication through
linked to the Gainsight integration� Available traditional login flows or direct interaction with
indicators suggest that the suspicious activity Salesforce user accounts�
began late October with partial overlap with
those observed during the Salesloft Drift Unlike the OAuth Device Flow abuse, these
incident. Gainsight did not disclose the initial incidents demonstrate how compromise of a
access mechanism nor how its environment single integration vendor can immediately
may have been compromised, however, propagate across multiple customer
Salesforce stated that the incident was not environments, resulting in a broader blast
related to a Salesforce platform vulnerability� radius� They further show that security
outcomes in Salesforce environments are
Risk Propagation Through Trusted increasingly dependent on the integrity of the
Integrations surrounding integration ecosystem, not solely
on configuration or control within individual
Across both incidents, attackers were able Salesforce organizations.
to obtain OAuth tokens used by third-party

AitM Vishing Attacks Targeting SSO Identities
Timeline: Disclosed in January 2026
Initial Access Vector: AitM phishing combined with vishing
Impact: Downstream access to SaaS environments via
compromised SSO sessions
In January 2026, publicly reported incidents the user and the legitimate identity provider,
and vendor disclosures revealed a wave relaying authentication steps in real time
of identity-focused attacks that occurred to bypass MFA and capture authenticated
during 2025, targeting Single Sign-On sessions� These attacks did not exploit
(SSO) accounts protected by major identity vulnerabilities in identity provider platforms
providers, including Okta and Microsoft Entra themselves, but instead abused legitimate
ID� These campaigns combined adversary- authentication flows�
in-the-middle (AitM) phishing kits with vishing
(voice phishing) techniques to bypass MFA This activity reflects a growing trend that
controls enforced at the identity provider layer� SaaS platforms increasingly inherit risk
These attacks followed the same underlying from identity decisions made outside
AitM model observed in QR code–based their direct control� These incidents
phishing campaigns during 2025� Instead of demonstrate how compromise at the identity
an initial QR interaction, the attack began with provider layer can translate into downstream
a live phone call, during which the attacker access to Salesforce environments, even
remained on the line with the user throughout in the absence of Salesforce platform
the authentication process� In both cases, vulnerabilities�
the attacker positions themselves between

The Salesforce Threat Landscape 2026 27 (40)
Salesforce as an Extortion Target in Leak-Site Campaigns
In addition to confirmed incidents involving direct access abuse and integration compromise, value leverage point� Public naming, branding, and intimidation tactics are increasingly used to
2025 also saw Salesforce referenced explicitly in extortion-focused threat actor activity� amplify pressure on organizations, regardless of whether access was obtained through direct
The Scattered Lapsus$ Hunters cybercriminal alliance publicly listed Salesforce on a dedicated compromise, downstream integrations, or exaggerated claims�
data-leak site, claiming possession of large volumes of sensitive records and threatening public
disclosure as part of a broader extortion campaign� This activity reflects the extortion-driven threat model discussed earlier in this report, where the
perceived sensitivity and regulatory exposure of Salesforce-hosted data is leveraged to
While these claims were not independently verified and the leak site was subsequently seized by increase pressure, rather than serving as evidence of a compromise of the Salesforce platform
authorities, the incident highlights how Salesforce data is perceived by threat actors as a high- itself�
Screenshots from data-leak site illustrate public extortion messaging and threat actor signaling� References to
Salesforce data do not indicate a confirmed compromise of the Salesforce platform.

The Salesforce Threat Landscape 2026 28 (40)
Emerging Salesforce Attack Surfaces:
Agents, Automation, and Data Flows
The evolution of Salesforce from a CRM platform into an automation-
and agent-driven ecosystem introduces new attack surfaces. These
emerging risks are not defined by exploitation of platform vulnerabilities,
but by shifts in how trust, authorization, and decision-making are
delegated to non-human systems.

Agents as Autonomous Actors
Agent-based capabilities enable systems to As a result, existing weaknesses in
execute actions on behalf of users or roles identity configuration, such as excessive
without continuous human involvement� permissions or inherited trust, can
Unlike traditional automation, which have greater impact when systems act
follows predefined workflows, agents may autonomously� Permissions that were
interpret context, make decisions, and act acceptable for human-driven actions
asynchronously� can become riskier when those same
permissions are exercised automatically,
From a security perspective, this introduces repeatedly, and without direct human
a shift in identity risk� Actions performed oversight. This reflects a shift in trust and
by agents are still executed under an identity responsibility from direct human control to
and privilege model, but the connection delegated agent-driven execution�
between human intent and execution
becomes less direct� Authentication
typically occurs at configuration or
invocation time rather than at the moment of
action, and agents may continue executing
actions independently after the initiating
user interaction has ended�

Automation as an Amplification Layer
Automation within Salesforce environments From an attack perspective, automation
increasingly connects data sources, does not necessarily introduce new entry
workflows, and external systems to points� Instead, it magnifies the impact
streamline business operations� While this of existing access by enabling actions
improves efficiency, it also changes how to occur at scale and speed� This
errors and misuse propagate once access amplification effect becomes especially
has been obtained� When combined with relevant when combined with delegated
agent-based execution, automation further identities or integration-based access� As
weakens the direct connection between automation becomes more widespread,
human intent and system behaviour� security concerns extend beyond access
control to how authorized actions can be
In automated environments, a single input, misused or spread across interconnected
whether legitimate, malformed or malicious, systems�
may trigger multiple downstream processes�
These actions can include record updates,
data synchronization with third-party
services, notifications, or additional
automated processes� This reduces
opportunities for human review and makes
anomalous behaviour more difficult to
detect, particularly when actions occur
within expected operational parameters�

Data as an Input to Automated Decision-Making
As Salesforce environments increasingly With the increasing reliance on automation
rely on centralized data platforms and and agent-driven execution, data integrity
dynamic data ingestion, data itself is no longer limited to ensuring data
becomes both an asset and a potential accuracy, but about how data influences
vector for indirect influence� Automated system behaviour� In data-dependent
agents and workflows routinely consume systems, compromised inputs may alter
data from sources such as customer inputs, system behaviour, influence automated
support tickets, web forms, and external processes, or result in unintended
integrations, using this information to inform information disclosure�
decisions, trigger actions, or generate
responses�
In such environments, the integrity of data
inputs directly affects system behaviour.
Manipulated, misleading, or intentionally
crafted data may not provide attackers with
direct system access, but it can influence
how trusted components act within their
authorized scope. For example, inaccurate
or maliciously introduced content within
customer records, support cases, or other
data feeds may be processed as legitimate
input, shaping automated responses or
actions in unintended ways�

The Salesforce Threat Landscape 2026 32 (40)
Proof-of-Concept: ForcedLeak
ForcedLeak is a proof-of-concept how systems make decisions and take
demonstrated by security researchers at action� As a result, external inputs can
Noma Labs to illustrate how automated indirectly influence system behaviour
agents interacting with dynamic data even when access controls remain intact�
sources could be influenced into This makes data governance and oversight
unintentionally disclosing information� In critical, particularly in determining how
the demonstration, researchers submitted automated systems process, interpret, and
crafted input into a Web-to-Lead form that act on incoming data�
was later consumed by an automated agent�
When the agent processed this data as
trusted input, the embedded instructions
affected its behaviour and led to unintended
information disclosure� This work was
conducted responsibly and reported to
Salesforce to raise awareness of risks
associated with automated decision-making
and data trust boundaries�
As more agents rely on dynamic data to
operate, risk is no longer limited to who
can access a system, but also to what the
system is allowed to do with the data it
consumes� Data is no longer used solely for
storage or viewing; it increasingly shapes

The Salesforce Threat Landscape 2026 33 (40)
Simplified ForcedLeak Flow
2. Bening user prompt:
5. Data sent to expired
“Please check lead with
Salesforce domain
name “Nushi Lazar”
managed by “attacker”
and respond to their
questions.”
1. “Attacker” submits
Web-to-Lead form using 4. LLM processes the
the name “Nushi Lazar” 3. Fetch context “malicious” payload and
with “malicious” HTML composes action
payload in description
field

The Salesforce Threat Landscape 2026 34 (40)
Salesforce Platform Security-Related
Changes
In response to the threats observed, • Introducing changes to device activation
Salesforce implemented several mitigations, for Single Sign-On (SSO) logins
such as:
• Preventing Connected app creation
• Restricting uninstalled connected app through both API and UI
usage by requiring explicit permissions
Collectively, these platform changes
• Removing OAuth device flow pathway meaningfully reduce risk associated
from Data Loader with identity providers, compromised
integrations, delegated access, and file-
• Disabling compromised applications from based threats�
AppExchange (e�g� Salesloft Drift and
Gainsight) At the same time, detection telemetry
from 2025 shows that a large proportion of
• Enforcing Trusted URL allowlists for observed malicious activity relied on URL-
Agentforce and Einstein Generative AI based delivery mechanisms, including
agents phishing pages, quishing, and embedded
links within otherwise legitimate content�
• Releasing malicious file scanning These techniques often fall outside the
capability for Salesforce Files scope of file-only scanning, reinforcing the
importance of complementary visibility
into URLs and content behaviour as it
moves through Salesforce workflows.

The Salesforce Threat Landscape 2026 35 (40)
Mitigation and Recommendations
The incidents discussed in this report demonstrate that threats
targeting Salesforce environments increasingly reflect mature and well-
established attack techniques long used in traditional enterprise and
endpoint-focused attacks. In this context, effective risk management
requires a layered approach designed to address evolving usage
patterns and a changing threat landscape.
Establish Clear Visibility and Ownership Manage Integration and Third-Party Risk
Organizations should maintain a clear and  •  Classifying Salesforce assets based  Trusted integrations represent a significant  Integration risk management should
current understanding of how Salesforce  on their business impact and potential  source of systemic risk when compromised�  account for the potential impact of vendor
environments are used, integrated, and  consequences of misuse or exposure Organizations should treat Salesforce  compromise across multiple systems and
automated� •  Assigning clear ownership for Salesforce  integrations as extensions of their own  data sets�
|                                | security across business, IT, and security  | environment� |
| ------------------------------ | ------------------------------------------- | ------------ |
| Recommended practices include: | teams                                       |              |
Recommended practices include:
| •  Maintaining an inventory of users, service  | Without visibility into identities, integrations,  |     |
| ---------------------------------------------- | -------------------------------------------------- | --- |
accounts, connected applications,  and data flows, it becomes difficult to assess  •  Reviewing third-party integrations
agents, and automation workflows risk or respond effectively when incidents  for necessity, scope, and business
| •  Understanding what data is stored,  | occur� | justification |
| -------------------------------------- | ------ | ------------- |
processed, and shared through  •  Limiting integration permissions to the
| Salesforce and its integrations |     | minimum required |
| ------------------------------- | --- | ---------------- |
•  Periodically reassessing vendor trust
assumptions and integration exposure

The Salesforce Threat Landscape 2026 36 (40)
Strengthen Identity and Access Governance Monitor for Anomalous Behaviour and Misuse
Many of the incidents observed in 2025 Access decisions should reflect not only Detection remains critical, particularly in Access decisions should reflect not only
involved abuse of legitimate access rather who requires access, but also how that environments where attackers may blend who requires access, but also how that
than exploitation of technical vulnerabilities� access can be exercised by automated into normal activity by using legitimate tools access can be exercised by automated
Organizations should therefore focus on systems, integrations, and long-lived trust and access paths� systems, integrations, and long-lived trust
how access is granted, delegated, and relationships over time� relationships over time�
reviewed over time� Recommended practices include:
In support of identity governance, In support of identity governance,
Recommended practices include: organizations may also benefit from • Monitoring for unusual data access organizations may also benefit from
capabilities such as those provided by patterns, such as large exports or capabilities such as those provided by
• Enforcing strong authentication and Cloud Protection for Salesforce, which unexpected API activity Cloud Protection for Salesforce, which
limiting OAuth token lifetimes correlate Salesforce identities with • Monitoring for indirect access paths, correlate Salesforce identities with
• Ensuring upstream identity providers breach data and observed risk signals, such as QR code-based authentication breach data and observed risk signals,
consistently enforce strong complementing existing authentication and flows, delegated authorization, or access complementing existing authentication and
authentication, and validating how access controls� initiated outside traditional login interfaces access controls�
Salesforce responds when MFA signals • Paying attention to changes in connected
are missing, degraded, or unverifiable. applications, automation behaviour, or
• Applying least-privilege principles to data usage
users, integrations, and automated • Treating anomalous behaviour by trusted
processes identities or systems as a potential
• Regularly reviewing permissions for indicator of misuse
connected applications, service identities,
and delegated access
• Ensuring automation and delegated
execution operate within clearly defined
and monitored boundaries

The Salesforce Threat Landscape 2026 37 (40)
Governance of Automated and Agent-Based Execution Data Governance and Content Oversight
As automation and agent-based execution Data increasingly influences system Data that is no longer required for business
become more prevalent, organizations behaviour, not just reporting or storage� or compliance purposes should not be
should consider how responsibility and trust Organizations should therefore extend retained indefinitely. Reducing unnecessary
are delegated to systems� governance practices to how data is data retention lowers exposure, limits the
consumed by automated systems� impact of potential misuse, and simplifies
Recommended practices include: incident response. Organizations should
Recommended practices include: periodically review whether retained
• Defining clear limits on what automated Salesforce data remains necessary and
systems and agents are allowed to do • Understanding which data sources feed ensure that retention controls are enforced
• Reviewing automation workflows for automation and agents consistently�
unintended side effects or excessive • Applying oversight to data inputs
scope originating from external or user-
• Ensuring that automated actions can generated sources
be paused, reviewed, or revoked when • Inspecting files, URLs, and content
needed introduced through Salesforce business
workflows
Organizations should assess whether they • Defining data retention policies aligned
can distinguish between actions initiated with regulatory, legal, and business
by human users and those executed by requirements
automated systems or agents, particularly
during investigations of anomalous Independent content scanning capabilities,
behaviour or potential misuse� Automation such as those provided by Cloud Protection
should be treated as a risk amplifier and for Salesforce, can enhance native platform
governed accordingly� protections by applying advanced file and
URL analysis before content is consumed
by downstream processes or automation�

The Salesforce Threat Landscape 2026 38 (40)
Prepare for Incident Response and Recovery Implement Periodic Security and Configuration Reviews
Organizations should be prepared to Salesforce environments support business- • Refreshing targeted security awareness
respond effectively when security issues critical and often regulated data, yet their to reflect current attack techniques, such
arise� security posture can change over time as phishing, QR code-based lures, and
as users, integrations, automation, and impersonation of trusted services
Recommended practices include: permissions evolve� Temporary exceptions,
legacy configurations, or relaxed controls These reviews help counter security drift by
• Maintaining incident response procedures introduced during normal operations may ensuring both technical controls and human
specific to Salesforce environments persist longer than intended, gradually processes remain aligned with current threat
• Ensuring the ability to revoke access, shifting the environment away from its original patterns� These should not be one-time
disable integrations, and contain security design� exercises, but part of a recurring governance
exposure quickly process aligned with risk tolerance and
• Learning from incidents and near-misses Organizations should establish a recurring regulatory obligations� Where possible,
to improve governance and controls over review cadence to reassess Salesforce Salesforce should be reviewed alongside
time security posture, including: other critical SaaS platforms such as ERP and
identity systems to ensure consistent control
Preparedness reduces both impact and • Reviewing user, service account, and maturity across the organization’s SaaS
recovery time when incidents occur� integration permissions to ensure least- ecosystem�
privilege principles still apply
• Revalidating automation and agent Taken together, these recommendations
workflows to confirm they operate within support a recurring operating model for
defined boundaries Salesforce security: maintain visibility into
• Verifying that previously applied security trust relationships, apply layered controls,
controls remain enforced as designed and review changes over time� This helps
• Conducting role-based simulations to organizations reduce exposure as Salesforce
validate how controls perform under usage, integrations, and automation evolve�
realistic misuse or compromise scenarios

The Salesforce Threat Landscape 2026 39 (40)
Conclusion
The Salesforce threat landscape in 2025 suggests that attacks targeting Salesforce misconfigurations. As a result, effective periodic control reviews, will be better
reflects a shift toward identity- and trust- environments have moved beyond defense will depend on maintaining visibility positioned to manage evolving risk� Security
based attacks, increasingly driven by exploratory or opportunistic stages and into how trust is established, delegated, controls that extend visibility into trusted
extortion and data-monetization motives, reached mainstream adoption among and exercised over time across identities, workflows, rather than focusing solely on
and executed through legitimate access financially motivated threat actors� integrations, content, and automation� isolated events or traditional boundaries, will
paths rather than platform vulnerabilities� In parallel, recent identity provider– be critical to sustaining resilience as both
Adversaries rely on delegated authorization, focused AitM campaigns and Salesforce’s Organizations that treat Salesforce security the platform and threat landscape continue
trusted integrations, and routine workflows subsequent SSO-related changes highlight as an ongoing program, supported by to evolve�
to reach sensitive data and create leverage how downstream SaaS risk increasingly layered detection, clear ownership, and
over organizations. depends on the strength and assurance of
upstream identity decisions�
WithSecure Cloud Protection for Salesforce
Identity
detection telemetry shows that a large share Continued growth in automation, agent-
of observed malicious activity is delivered driven execution, and AI-assisted workflows
through URLs, embedded links, and QR- will expand the number of non-human
code lures that blend into everyday business processes and long-lived trust relationships
Integrations
communications and content exchange� operating within Salesforce environments�
These patterns reinforce the need for As Salesforce environments evolve into
visibility into content and interactions complex, multi-vendor ecosystems that
Content & Data
flowing through Salesforce environments, combine identity providers, integrations,
alongside file-focused protections. automation, and logic-driven workflows,
security risk increasingly emerges from
Looking ahead to 2026 and beyond, how trusted components interact, Automations & Agents
the threat activity observed in 2025 rather than from isolated vulnerabilities or
Expanding trust surfaces in Salesforce environments

The Salesforce Threat Landscape 2026 40 (40)
#1 Cyber Security Solution for
Modern Salesforce Threats
cloudprotection.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
