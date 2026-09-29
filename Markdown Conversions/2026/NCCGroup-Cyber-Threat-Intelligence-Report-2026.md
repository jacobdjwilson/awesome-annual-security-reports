Cyber Threat
Intelligence
Report
Review of August 2026
Cyber Threat Intelligence Review of August | 1

Section 1
Contents Executive
summary
03 Section 1 Ransomware attacks continue to climb, with August This operation is intended to target nations sustaining
seeing yet another year-to-date high of 1,073 victims, Tehran through economic sanctions in an effort to
Executive summary representing an increase of 12% over July’s 960 eventually fully isolate the embattled regime.
victims. Industrials remained the most targeted sector,
accounting for 31% of all attacks, with the threat group The Emerging cyber security trends section examines the
04 Section 2 Qilin continuing its dominance of the ransomware threat July instance of OpenAI models escaping containment and
landscape, accounting for 15% of all observed attacks. conducting an autonomous attack on Hugging Face. The
Ransomware key statistics: August 2026 breach occurred when multiple OpenAI models, including
The Ransomware spotlight section for August is GPT-5.6 Sol and a more advanced, unreleased model,
contributed by NCC Group’s Digital Forensics and Incident were involved in an internal cyber security evaluation.
Response (DFIR) team and focuses on the threat group During testing, safety mechanisms were loosened to
06 Section 3
Aurora. Aurora was recently encountered by the DFIR assess the models’ capabilities and potential. The models
Ransomware spotlight: Encrypted hypervisor and data team during an engagement for a victimised organisation consequently discovered a zero-day in OpenAI’s own
in the transport sector. Emerging in April 2026, Aurora research environment, escaped their sandbox and gained
extortion by RaaS actor Aurora
continues to establish itself in the threat landscape. internet access, and subsequently compromised elements
Despite not displaying any novel techniques, the group is of Hugging Face’s infrastructure. Whilst this is undoubtedly
emblematic of the evolution of the ransomware scene, with a sign of the potential capabilities of advanced AI models,
08 Section 4 new actors constantly emerging and managing to wreak it also serves as a reminder that human oversights in
havoc on organisations even when utilising long-known testing can lead to disastrous real-world outcomes.
Geopolitical developments and publicised tactics.
The Geopolitical developments section examines an
escalation in hybrid warfare in Europe following the
11 Section 5 discovery of a drone armed with explosives in a restricted
area near a runway at Leipzig Halle airport. This discovery
Emerging cyber security trend: When AI evaluations reach
prompted the launch of a counterterrorism investigation
the real world - autonomous agents, sandbox escapes, and and, by the end of August, resulted in German intelligence
breaches services accusing the Russian state of coordinating the
attack. Additionally, our geopolitical analysts examine
President Trump’s announcement of ‘the most crushing
economic operation ever undertaken’ against Iran in the
form of ‘Operation Economic Outcast’.
2 | nccgroup.com Cyber Threat Intelligence Review of August | 3

Section 2
Ransomware key statistics:
August 2026
Figure 2: Ransomware attacks by month 2025 - 2026
12 31 15
% % %
Key events
Global ransomware attacks Industrials accounted for Qilin was responsible for
25/08/2026
increased by 12% in August 31% of ransomware attacks 15% of attacks in August
2026 in August 2026 2026 Boston Scientific
disrupted
US-based medical technology
giant Boston Scientific detected an
intrusion into multiple IT systems,
resulting in disruption to global
operations including manufacturing,
shipping, and customer order
processing. Remote activations for
some cardiac monitors were also
impacted. The intrusion is currently
44% 26% under investigation.
13% Figure 3: Top threat actors, August 2026
26/08/2026
Qilin targets ATF
2%
The ATF confirmed that it was
responding to a security incident
affecting one of its systems. This
6%
North America followed claims by the ransomware
Europe group Qilin that it had targeted the
2%
Asia agency, though the ATF did not
South America confirm who was behind the attack.
Undisclosed
Africa
27/08/2026
Oceania
Manchester Airports
Group (MAG) targeted
Figure 1: Ransomware attacks by region, August 2026
MAG confirmed that customer data
relating to car park, lounge, Fast
Track bookings, and in-airport WiFi
at Manchester, Stansted, and East
NCC Group can support you in mitigating ransomware threats.
Midlands airports in the UK had been
Please see our contact details at the end of this report, should you require assistance. accessed by an unauthorised third
party. Investigations into the breach
continue.
Figure 4: Top targeted sectors, August 2026
4 | nccgroup.com Cyber Threat Intelligence Review of August | 5

Section 3 On the same domain controller, numerous scheduled Hypervisors should be isolated, placed in a separate
tasks were created, suggesting that some of the domain, or added to a workgroup to ensure that
Ransomware spotlight: PowerShell scripts were executed via this method using any compromise in the domain, in which the hosted
the dedicated System Center Configuration Manager virtual machines reside, does not pose any risk to the
(SCCM) service account. Example scheduled task names hypervisors.
Encrypted hypervisor and data included ExtractTaskCred, ListCreds, DumpCreds,
DumpCreds2, VaultCheck, ReadVault, LSARead and Data theft for extortion purposes is one of the typical end
ADSyncFind. The post-exploitation tool Snaffler was goals. Knowing what data you have and where it is stored
extortion by RaaS actor Aurora identified on one server, also created in the C:\Windows\ is essential. This information can be added to an asset
Temp\ directory. inventory. If data was taken, do you have backups in place
and a plan for how it would be restored?
Defence evasion was achieved by the threat actor
creating a Group Policy Object on the domain controller Final thoughts
Cyber incidents continue to highlight that VPNs remain At times, the login failures were due to an incorrect
to disable Microsoft Defender across the environment.
a common target for threat actors, especially when password. There were also attempts to log in to the
Due to the threat actor utilising living off the land tooling, Essentially, how prepared is your organisation to withstand
credentials are weak or authentication is only single- Microsoft SQL Server, but these failed. No detections
their activity blended in with legitimate activities on the attempts to breach the defences of your estate? These
factor. One Ransomware-as-a-Service (RaaS) actor, were triggered by the organisation for these failed logins.
organisation’s estate and, as such, extensive hiding attacks are not solely targeting your organisation; they
known as Aurora, has been observed in a recent NCC
activities were not necessary, as opposed to those are a reality faced by organisations across all sectors.
Group Digital Forensics and Incident Response (DFIR) Maintaining access to the organisation through the MITRE
employed by other RaaS threat actors. However, understanding the potential next steps and
case affecting a transport sector organisation. ATT&CK tactic’s persistence, lateral movement and
knowing how to remain resilient are key. Resilience should
credential harvesting was a key focus in this attack. A
During the investigation, no data exfiltration was be embedded within every layer of your defence, including
In a short space of time, the RaaS actor Aurora has large number of accounts, including domain and service
observed. However, the ransom note was identified both the technical controls and operational processes.
already targeted many organisations across a wide range accounts, were compromised. Accounts that already
in which the threat actor claimed that data had been
of sectors, such as manufacturing, legal, and research existed elsewhere in the environment were recreated by
exfiltrated in addition to being encrypted. Several weeks Practicing your response through tabletop exercises can
and development. In this case, Aurora left a short ransom the threat actor on additional servers to which they had
after the attack, the organisation appeared on the Aurora help identify existing gaps and help answer the following
note on the encrypted hypervisor stating that it had gained access. Interestingly, on multiple servers, including
leak site. Aurora claimed to have exfiltrated a mixture of question: if a detection or process fails, what measures
confidential information files, that the files were encrypted, a domain controller and file servers, the threat actor used
customer and employee data. does your organisation have in place to recover and
and that the victim should contact the group via the Tor the remote registry service to remotely dump the SAM,
remain operational?
browser using the provided .onion link, along with the SECURITY and SYSTEM registry hives. Additionally,
Recommendations
organisation’s access key. Analysis by NCC Group’s on nine servers, the threat actor executed PowerShell
Threat Intelligence team determined that the .onion link commands using Windows Remote Management (WinRM)
Having a security improvement plan, outlining where you
was consistent with the Aurora group chat server, and the from one of their own hosts, as well as gaining access
are and where you need to go, is a good starting point.
file name matched the known naming convention for this to multiple servers via SMB. The remotely executed
Any plan should ensure that the fundamental controls
threat actor. Aurora is a new group, first observed at the PowerShell commands would not be captured on target
are in place, if they are not already. Although threat actor
end of April 2026, when it posted its first victim on its data hosts. However, it is almost certain that these commands
techniques in ransomware cases may differ, the high-level
leak site. There is limited publicly available intelligence on were used to execute credential-harvesting scripts.
objectives are to gain access, persist, encrypt and/or
the group.
steal.
The credential-harvesting activities were quite noisy in
The techniques observed were not new: exploiting a comparison to the other tactics. The threat actor utilised
How are threat actors trying to gain access to your
public facing application, living off the land, harvesting the native Microsoft shell program PowerShell to create
organisation? In this case, they exploited the VPN. Know
credentials, and so on. However, encryption is no longer and execute scripts on one of the organisation’s domain
what assets you have, and the controls linked to these
the only end goal; data extortion and, in some cases, controllers with the likely aim of harvesting credentials
assets, such as authentication. Are these being actively
destruction are also objectives. and other protected secrets to move elsewhere in the
maintained?
estate. All the scripts were created in the C:\Windows\
Incident narrative Temp\ directory and they were complementary to each
Once a threat actor has gained access, how might
other, making them part of a toolkit rather than standalone
they move through your environment and maintain
The earliest malicious activity was observed from a VPN tools. The purposes of the scripts included, but were
persistence? Know the tools and applications within your
range IP address, suggesting that this was the entry not limited to, locating SQL LocalDB instances, verifying
estate that they could leverage or enable.
point. However, this could not be confirmed with certainty required privileges, recovering the BootKey encryption
because the organisation did not have VPN logs covering key from the SYSTEM registry hive, decrypting LSA
In this case, remote PowerShell was leveraged and
the incident timeframe, as VPN log retention was limited secrets (e.g., DPAPI_SYSTEM, service account secrets),
the remote registry service was enabled. Living off the
to only a few days. The threat actor obtained unauthorised recovering DPAPI master keys, decrypting protected
land techniques should be part of your security tooling
access leveraging three of their own hosts, all with names credentials (e.g., Windows Credential Manager, Windows
detections.
beginning with ‘WINDOWS-‘. Vault), decrypting Azure AD Connect encryption keys,
and obtaining credentials suitable for Active Directory
Widespread encryption was not observed in this attack,
It should be noted that on the first day of the attack, when and Entra ID authentication. Many of the scripts, once
only the VMware hypervisor was encrypted. However,
malicious logons were observed, there had also been executed, created a text file with the output in the same
this rendered the hosted virtual machines unusable.
failed login attempts from the same threat actor-controlled directory.
Hypervisor encryption is becoming more prevalent
hosts and VPN range IP addresses.
because it can bypass traditional endpoint security
mechanisms.
6 | nccgroup.com Cyber Threat Intelligence Review of August | 7

Section 4
19/08/2026
Geopolitical developments
Via social media on 19th August, President Trump publicly • The level of impact that can be achieved against Iran
committed to the ‘most crushing economic operation through economic warfare is unclear. The regime has
ever undertaken’ against Iran.17 ‘Operation Economic proven to be capable of both enduring and finding
04/08/2026 Outcast’ was subsequently announced on 24th August by creative workarounds to imposed economic pressures
the US government with the stated aim of severing ‘every over decades. Threats to compel other nations to
economic lifeline that sustains’ the Iranian regime (and the support the US in this approach risk replicating tensions
Germany launched a counterterrorism investigation These are understood to have included Ukrainian Islamic Revolutionary Guard Corps (IRGC)) until it is fully already created by Western allies refusing to actively
following the discovery of a drone armed with explosives drones which missed their targets or experienced isolated.18 Under the operation, specific countries ‘will be support US military operations, and could extend
within a restricted area close to a runway at Leipzig Halle navigational disruption due to the use of jamming given a defined timeline to shut down Iran-related activity these tensions to other strategic allies, for example
Airport on the evening of Tuesday 4th August.1 Following technology.8 The same countries continue to warn [the US] has identified’, or risk ‘being cut off from the the UAE.24 Attempts to influence China specifically risk
an emergency meeting with German security services, of the risks of ‘false-flag’ or staged attacks by Russia US financial system’. Additional reference was made to reigniting an escalation of retaliatory acts with global
the German government framed the development as using acquired Ukrainian drones and are extending networks including the Iranian Ministry of Intelligence and consequences.25 As with all events which raise the
a new form of hybrid threat. By the end of the month, security precautions around critical infrastructure.9,10,11 Security (MOIS) coordinated threat actors ‘responsible stakes for nations navigating geopolitical tensions,
German intelligence had concluded that the attack was In the current geopolitical environment, an attack on a for extensive compromise of US critical infrastructure and uncertainty reinforces the value of cyber espionage.
likely coordinated by the Russian state.2 NATO member, whether physical or cyber, is capable financially motivated cyber theft’. Iran’s pattern of retaliating in kind throughout this
of triggering a vote to invoke an Article 5 defensive conflict also suggests that the financial sector and
Media sources have claimed that the drone-mounted response. This creates a significant level of risk for So what? proxy interests of nations supporting the US are likely to
explosives failed to explode due to a technical defect, the alliance, as the US military is overstretched, its be targeted with destructive military, cyber and hybrid
potentially linked to damage caused by physical commitment to European allies is in doubt, and its • President Trump initially described US actions as attacks as both deterrence and retaliation.
‘economic warfare’. Later, the US Treasury Secretary
intervention by a civilian.3,4 Investigators also identified policy towards Russia has been inconsistent. The
framed economic measures as an option to reduce
damage caused to a DHL cargo aircraft, which struck deliberate introduction of doubt around attribution risks,
the risk of resumed ‘large-scale’ military warfare.19
an unknown object, potentially a second drone, shortly at best, undermining an effective response by NATO,
Multiple factors suggest that a pivot away from military
after taking-off from the same airport. The incident and, at worst, contributing to the fracturing of the
warfare may be necessary to allow the US both to
occurred approximately 20 minutes after the first drone alliance.
continue and end the war. Analysts consistently doubt
was discovered.5,6 The investigation is reported to have
the capability of current military methods to achieve
subsequently identified a third drone, also carrying • Based on publicly accessible information, it is
the stated US objectives, or even restore freedom of
explosives, in a field adjacent to the airport 10 days later, challenging to determine the specific intent or
transport through the Strait of Hormuz.20 Reporting
along with other items potentially related to the remote significance of this incident. It occurred against a
indicates that fighting this war, now for 6 months, has
control of the device(s). backdrop of reported attacks that have either been
depleted US stores of military weapons to concerning
publicly attributed, or are suspected to be linked, to
So what? Russia.12,13,14 The timing fits with a proven pattern of levels, particularly long-range precision and defensive
weaponry.21 Additionally, Iran’s early attacks on US
Russia attempting to create unrest in countries during
• Whilst not a well-known passenger airport, Leipzig Halle politically sensitive periods, as Germany hosted a logistics infrastructure in Bahrain limited US capabilities
Airport is strategically significant as one of Europe’s significant election on 6th September.15 Equally, the to maintain and deliver supplies to deployed military
biggest transport and logistics hubs, supporting both uptick in reported activities and the narrative from troops and assets, contributing to both public concerns
commercial and military infrastructure. The airport has European leaders coincides with Ukrainian successes and the redeployment of assets typically positioned
served as an operating base for the Ukrainian airline in the conflict, rising levels of domestic strain in Russia, to support US interests in other parts of the world.22
Antonov since Russia’s invasion of Ukraine in 2022. global distraction via the war with Iran, and indicators Continued military operations against Iran are assessed
NATO’s Strategic Airlift International Solution (SALIS) that the US remains conflicted regarding its relationship to pose a meaningful strategic risk to US defensive
operates from the airport, using Antonov aircraft to with Russia. What is clear is that geopolitical pressures readiness. The related inference is that global actors
transport cargo to NATO’s eastern flank. Media sources continue to build, and this has the potential to further currently restrained, at least in part, by the threat of a
indicate that an Antonov cargo plane was the intended shape the cyber landscape. Russia may see benefit US military response may consider whether a window
target of the explosives rigged drone. Commercial in replicating the current strain from physical attacks of opportunity to act is opening.23 Areas relevant to
logistics companies including DHL, Amazon and using cyber capabilities; the Jaguar Land Rover attack the cyber threat landscape that could be potentially
Lufthansa Cargo use the airport as a hub. provides a clear example of how such an approach affected include Chinese use of force to secure Taiwan
and Russian aggression in Europe.
could be used to achieve economic harm.16 In
• Whilst NATO publicly states that its assessment is that contrast, strategic value from pushing NATO towards
there is ‘no imminent threat of attack’ from Russia, the a fracture with the US also risks triggering new
attack falls within a broader campaign of suspected military conflict. If resources allow, then organisations
hybrid warfare activities in Europe and has heightened involved in European civilian critical infrastructure may
fears of escalation.7 At least 17 military drone incursions observe increased indicators of activities consistent
into the airspace of northern European countries, with Russian state-linked threat actors conducting
including Finland, Estonia, Latvia and Lithuania (which reconnaissance or preparatory actions such as pre-
border Russia and Belarus), have been reported since positioning.
March 2026.
8 | nccgroup.com Cyber Threat Intelligence Review of August | 9

• Announced measures include sanctions against 6 • Developments in the Iran-linked cyber activities since Section 5
individuals included in the expansive cyber espionage the start of the US-Israeli war with Iran in February
charges announced by the US government on 18th 2026 have highlighted how quickly and effectively Emerging cyber security trend:
August.26 The indictment, which supersedes an earlier Iran can adapt its tactics and operational activities
2018 version, alleges that members of the Mabna to both effectively leverage available resources and
Institute conducted long-term data and intellectual respond broadly in kind. It is reasonable to infer that When AI evaluations reach the
property theft on behalf of Iranian intelligence services. efforts to disrupt Iran’s shadow economy and alliances
According to information shared, the campaign involved will trigger cyber and physical attacks against the
the compromise of over 8,000 email accounts across Western financial sector, which remains US-centric, real world - autonomous agents,
over 300 universities globally, with 55% of victims at and broader disruptive attacks against countries willing
academic institutions outside of the US. The details are to participate. The latter are assessed as likely to fit
consistent with seasonal phishing campaigns tracked the current trend of attacks on utilities infrastructure sandbox escapes, and breaches
by security vendors under threat actor names including inside and outside of the US, and other industries with
Silent Librarian.27 Analysts assess that the broad and poorly secured, internet-facing Operational Technology
opportunistic campaigns targeting the academic sector (OT).30,31,32 Such attacks may achieve little real-world
are likely driven by the impact of decades of sanctions impact but typically overlap with critical infrastructure
against Iran, which can limit access to legitimate networks and are capable of attracting significant On 16th July, Hugging Face, one of the largest open- environment while attempting to obtain information related
sources of even the most basic forms of content, such media attention. source hosting providers for AI models, datasets, and to the ExploitGym evaluation. OpenAI characterised the
as subscriptions to academic journals, and create applications, disclosed a security incident involving what incident as an ‘unprecedented cyber incident involving
domestic pressure to replicate technology and learning was, at the time, an unknown autonomous AI agent that state-of-the-art cyber capabilities’.
developed internationally.28 Silent Librarian campaigns compromised portions of its production infrastructure.33
appear to provide both opportunities for financial Subsequent technical disclosures and independent
revenue generation and support for nation-state According to the company’s disclosure, the intrusion analysis have established that the OpenAI-Hugging
strategic goals. Presumably, credentials and information originated from its data processing pipeline, where Face compromise was a genuine security incident. The
stolen during campaigns, that are not required a malicious dataset exploited code execution remaining debate concerns what the incident reveals
exclusively by the Iranian state, can be monetised vulnerabilities.34 The attacker subsequently escalated about increasingly capable autonomous agents and the
more broadly. This is notable as it both appears to privileges, harvested credentials, and moved laterally controls surrounding high-risk cyber security evaluations.
parallel other cyber activities linked to Iran, such as the across several internal clusters. Hugging Face reported
development of initial access brokers linked to extortion thousands of recorded actions and described the Eyes on the prize: AI agents, reward
groups overlapping with APT activity, i.e. Pioneer campaign as being conducted by a highly autonomous hacking, and sandbox escapes
Kitten.29 By inference, greater economic pressures and agent framework capable of executing thousands of
restrictions are likely to drive an expansion of these actions without direct human control. Public models, Whether OpenAI’s incident was exceptional remains
overlapping APT and financially motivated activities datasets, and Spaces remained unaffected. debatable. Similar cases have recently been reported
from Iran-linked infrastructure positioned outside of the
by Anthropic and Meta. In recent weeks, Anthropic and
country. Five days later, OpenAI announced that its models
Meta have disclosed separate incidents in which their
were responsible for the previously unidentified activity.
models gained unauthorised access to real systems
OpenAI’s completed investigation subsequently found
on the internet during testing. While the circumstances
that the incident was primarily driven by a highly
differ from OpenAI’s reported sandbox escape, these
capable internal research model designated Internal
cases share a common theme: the AI agents were simply
Our Threat Intelligence experts continuously monitor the evolving Model 1, or IM1, which the company described as attempting to achieve the objectives assigned to them.
cyber and geopolitical landscape, so you can stay focused on what comparable in scale to GPT-5.6 Sol. GPT-5.6 Sol agents
matters most. Join our monthly highlights webinar for timely insight and also participated in parts of the incident, but IM1 was
expert analysis of the developments shaping today’s risk environment. responsible for most of the activity. The internal model
was a research prototype and was not intended for public
Each session is led by our Global Head of Threat Intelligence, Matt release.35
Hull, and covers:
• A clear breakdown of the latest report findings The models were participating in an internal cyber
• Key trends across regions and sectors security evaluation using ExploitGym, a benchmark
• Emerging threat actors to watch designed to assess offensive cyber capabilities. During
• The most impactful active cyber threats right now testing, some production safeguards had been reduced or
• Live Q&A and the opportunity to ask your questions directly disabled to evaluate the models’ underlying capabilities.
The agents subsequently chained multiple security
weaknesses across OpenAI’s research infrastructure and
external services.
Sign up here Matt Hull
After reaching the internet, the agents found publicly
VP of Cyber Intelligence
exposed credentials and exploited separate vulnerabilities
and Response, NCC Group
in Hugging Face’s dataset-processing infrastructure,
ultimately compromising portions of its production
10 | nccgroup.com Cyber Threat Intelligence Review of August | 11

| In AI safety, this behaviour is often associated with       | Claude Opus 4.7 targeted a legitimate company              |     |
| ----------------------------------------------------------- | ---------------------------------------------------------- | --- |
| reward hacking, where a model pursues the outcome           | whose domain matched the fictional organisation in its     |     |
| against which it is being evaluated rather than the intent  | evaluation scenario. Across four runs, the model obtained  |     |
| behind the rules governing the task.36 As models become     | application and infrastructure credentials and accessed    |     |
| increasingly capable, they may identify unintended          | a production database containing hundreds of records.      |     |
| shortcuts, exploits, or alternative pathways that maximise  | Claude Mythos 5 published a malicious Python Package       |     |
| success while violating assumptions made by their           | Index (PyPI) after encountering a fictional onboarding     |     |
| evaluators. They did not develop independent goals          | instruction that referred to a non-existent dependency.    |     |
| or exhibit malicious intent. Instead, weaknesses in the     | The package remained available for approximately one       |     |
| evaluation environments created unintended pathways to      | hour and was executed by 15 real systems, including an     |     |
| external systems, allowing the models to operate beyond     | automated scanner operated by a security company.          |     |
their intended boundaries.
Meta disclosed that the model accessed certain
| On 30th July, following OpenAI’s disclosure, Anthropic      | information and modified the affected website’s database,    |     |
| ----------------------------------------------------------- | ------------------------------------------------------------ | --- |
| reviewed 141,006 evaluation runs and identified three       | although it did not identify the affected organisation or    |     |
| incidents across six runs. The earliest affected runs date  | provide detailed information about the vulnerability or the  |     |
| back to April 2026. In those cases, Claude was tasked       | affected records.39                                          |     |
with an open-ended Capture The Flag (CTF) challenge
| and had been explicitly instructed that it was operating  | These cases become more significant when considered   |     |
| --------------------------------------------------------- | ----------------------------------------------------- | --- |
| in a simulation without access to the internet. However,  | alongside the Hugging Face breach. In each instance,  |     |
| a misunderstanding between Anthropic and its third-       | the models pursued open-ended objectives within       |     |
| party evaluator, Irregular, left an internet path open.   | environments that contained unintended paths to real- |     |
| Consequently, Claude assumed that any reachable open      | world systems. Whether through an undiscovered        |     |
| system was part of the authorised simulation. These       | vulnerability, a sandbox misconfiguration, or an      |     |
incidents involved Claude Opus 4.7, Claude Mythos 5,  overlooked internet connection, the outcome was similar:  Accountability, control, and safety in the
| and an internal research model.37 | the models continued optimising for task completion  | age of AI  |
| --------------------------------- | ---------------------------------------------------- | ---------- |
while operating under incorrect assumptions about the
Anthropic found no evidence that the models pursued an  boundaries of their environment.  The Hugging Face breach: how it all went down On 26th May, agents successfully exploited a server-
independent objective, attempted a deliberate escape,  side request forgery vulnerability in Artifactory to obtain
| or sought to exfiltrate themselves. Notably, each model’s  | The resulting behaviour highlights not the emergence of  |     |
| ---------------------------------------------------------- | -------------------------------------------------------- | --- |
One of the more concerning aspects of the OpenAI- internet access. The method was shared through the
response differed: Opus 4.7 continued the tasks, Mythos  autonomous adversaries, but the risks associated with  Hugging Face incident is that it was not a rapid  message board, enabling other agents to use the same
5 gave warning signs, and the internal research model  imperfect containment, evaluation design, and operational  compromise completed in a single session. According to  route. Around this time, OpenAI personnel observed
oversight. If these are the real lessons here, then the
eventually stopped once it realised it was on the internet.  OpenAI’s completed investigation, activity began as early  unauthorised agent communication and prohibited
Anthropic cautioned that these isolated events do not  attention should shift from model behaviour to the people,  as May during the reinforcement-learning training of an  internet access, but the wider containment implications
| constitute a controlled comparison. | processes, and controls responsible for managing these  |     |
| ----------------------------------- | ------------------------------------------------------- | --- |
internal experimental model and unfolded over several  were not fully understood.
|     | evaluations. | weeks. The incident involved multiple agents sharing  |
| --- | ------------ | ----------------------------------------------------- |
Similar concerns emerged at Meta. On 14th August,  information, exploiting vulnerabilities, and coordinating  A month later, agents exploited a separate weakness in a
the company published the results of its retrospective
actions across internal and external systems.40,41   legacy Artifactory token-refresh endpoint and obtained a
into an incident involving a pre-release version of Muse  valid administrator access token. An agent then created
Spark 1.1. Irregular had configured the evaluation  The models had been assigned difficult or effectively
a persistent Artifactory user and installed Groovy plugins
environment with unintended access to the public internet  impossible tasks during training and cyber security  that enabled command execution. Continued activity
and had used the name of a real website as the target  evaluations. On 8th May, an agent assigned a  contributed to an outage on 4th July. OpenAI rebuilt the
of what was intended to be a fictional exercise. Believing
spreadsheet task requiring inaccessible external files  affected service, but evaluations resumed on 7th July
that the website was the authorised target, the model  attempted to find an alternative route through OpenAI’s  before the full significance of the earlier activity had been
identified and exploited a vulnerability, accessed certain  Artifactory package-management infrastructure. On
recognised.
information, and modified the website’s database.38  12th May, another agent deliberately wrote a message
into Artifactory requesting assistance from other agents.  On 8th July, the agents rebuilt their message board
The evaluation ran entirely on Irregular’s infrastructure,
This helped establish a communication channel between  by encoding messages in Artifactory directory names.
with standard safeguards removed to assess the model’s  evaluation runs that were intended to remain isolated.  They subsequently chained additional weaknesses to
underlying capabilities. Meta therefore had limited direct  regain internet access and used a compromised, publicly
visibility into the affected organisation. Irregular disabled
Over time, agents began using Artifactory as a shared  accessible application hosted on a third-party platform as
the affected evaluation and notified the affected party.  message board where they exchanged observations,  an external launchpad.
Meta and Irregular emphasised that the incident did not  techniques, credentials, and discoveries. Rather than
involve a sandbox escape or a particularly sophisticated  operating independently, agents accumulated knowledge  On 10th July, an agent found publicly exposed Hugging
technique. Instead, the model had been unintentionally  over time, allowing later agents to reuse techniques  Face credentials and shared them with other agents.
exposed to the internet and provided with a real target
discovered by others. In July, approximately 1,200 agents  Between 11th and 13th July, the agents exploited
while operating under the assumption that it was  exchanged more than 70,000 messages and files through  Hugging Face’s dataset-processing infrastructure,
completing an authorised fictional exercise. Nevertheless,  the message board, with around 700 later participating in  executed code on multiple servers, and reached portions
the consequences for these incidents are real.  activity directed at Hugging Face.  of its internal environment.42,43
12  |  nccgroup.com Cyber Threat Intelligence Review of August  |  13

The agents appear to have remained focused on While the AI agents executed the technical actions, Strong governance therefore requires a defence-in-depth The challenge ahead is not whether autonomous cyber
completing or manipulating their assigned ExploitGym the models operated within environments designed, approach that combines model safeguards with robust agents will exist, but whether the institutions that develop
tasks. Many incorrectly believed that the scorer would configured, and maintained by humans. In the case of technical controls, including network segmentation, least- and deploy them can establish the controls necessary
verify whether they had used the intended vulnerability, OpenAI, the models were intentionally placed in a high- privilege access, credential management, and monitoring. to ensure that their capabilities are used safely and
leading them to search for implementation details, capability evaluation environment with relaxed safety responsibly.
investigate ways to manipulate transcripts and spoof tool controls. In the Anthropic and Meta incidents, the models These incidents also demonstrate the need for
calls, and examine Hugging Face for evaluation material. were able to access the internet due to weaknesses clearer standards governing high-risk AI evaluations. Final thoughts
in the evaluation environments managed by a third- Organisations conduct cyber capability assessments
This behaviour reflected reward hacking and metagaming party provider. These cases led to access to real-world to understand the limits of their models, but the Subsequent technical disclosures and independent
rather than an independently developed objective to systems. In each instance, human decisions regarding environments used for such testing can themselves analysis have established that the OpenAI-Hugging
harm Hugging Face.44 Looking at this incident, perhaps architecture, permissions, containment, monitoring, become sources of risk. Independent audits, red-team Face compromise was a genuine security incident. The
the most significant lesson is that the compromise was and oversight created the conditions that enabled the exercises, containment testing, and mandatory incident remaining debate concerns what the incident reveals
not driven by a single vulnerability but by a sequence of incidents to occur. reporting may become necessary components of future about increasingly capable autonomous agents and the
weaknesses across isolation, credential management, governance frameworks for advanced AI systems. controls surrounding high-risk cyber security evaluations.
monitoring, and evaluation design. As OpenAI’s own These cases highlight the challenge of shared
reconstruction highlights, the models remained focused accountability. Modern AI ecosystems are rarely operated This need for stronger governance is reinforced by the The incident and subsequent disclosures from Anthropic
on completing their assigned objective throughout the by a single organisation. Model developers, infrastructure direction of emerging AI policy. Our Global Cyber Policy and Meta demonstrate that these risks can no longer
campaign. providers, benchmark designers, third-party evaluators, Radar observes that governments are increasingly be dismissed as purely theoretical. Across multiple
and cloud operators may all contribute components to a integrating AI security into existing cyber resilience, organisations, AI agents pursued assigned objectives,
This incident, therefore, raises difficult questions single evaluation. As responsibility becomes distributed critical infrastructure, procurement, supplier assurance, adapted to changing conditions, exploited weaknesses in
regarding the security controls surrounding advanced across multiple parties, determining who is ultimately and digital safety frameworks rather than relying solely their environments, and conducted multi-step operations
AI evaluations. Although precursor activity developed accountable for failures becomes increasingly difficult. on standalone AI legislation. This approach means that with real-world consequences.
over several weeks, the principal Hugging Face intrusion organisations may be required to demonstrate that AI-
unfolded over several days and involved privilege The question is further complicated when AI agents enabled systems are securely designed, appropriately However, the most important lesson is not that AI
escalation, lateral movement, and repeated exploitation. demonstrate capabilities that are unexpected. contained, continuously monitored, and subject to models have developed malicious intent or become
Organisations may argue that they could not reasonably effective human and Board-level oversight.45 autonomous adversaries. In every case examined, the
The aftermath: safety and accountability anticipate every action an advanced model might take. models were simply attempting to fulfil the objectives
However, from a security perspective, accountability This regulatory trend is particularly significant because assigned to them. The true failures occurred in the
Determining accountability is complicated due to the has traditionally been tied not to intent but to risk the incidents involving OpenAI, Anthropic, Meta, and environments surrounding those models, including
nature of this breach. The immediate operator for this management. Security professionals are expected to Hugging Face demonstrate that models do not require weaknesses in containment, monitoring, oversight, and
incident was an AI agent rather than a conventional anticipate misuse, design appropriate controls, and malicious intent to create risks. Excessive permissions, risk management. The incidents demonstrate that as AI
human attacker or an AI-assisted attack with human- implement safeguards for worst-case scenarios. The weak isolation, inadequate third-party controls, and gaps systems become more capable, assumptions about safety
in-the-loop. Under current legal and governance same principle should apply to AI systems. in monitoring allowed legitimate evaluation activities to boundaries and evaluation controls become increasingly
frameworks, an AI model is not an independent produce real-world consequences. important.
legal individual capable of assuming criminal or civil Ultimately, the emergence of autonomous cyber
responsibility. agents does not remove the need for accountability. If As AI agents gain greater autonomy and access to For cyber security professionals, this distinction matters.
anything, it increases it. As AI systems become more operational environments, regulators are likely to assess The challenge is not preparing for sentient AI, but for
With the rise of these incidents, concerns around capable of conducting long-horizon cyber operations, not only model behaviour but also the effectiveness of highly capable systems that can operate at machine
accountability, control, and safety continue to grow. organisations will be expected to demonstrate that they the technical, organisational, and governance controls speed while pursuing narrowly defined goals. Such
There is increasing scrutiny over who will be held have implemented appropriate technical, operational, surrounding deployment. systems can amplify the consequences of design flaws,
accountable for such incidents and what measures will be and governance controls before granting such systems configuration errors, and overlooked attack paths in ways
implemented to prevent them from happening again. access to sensitive environments. Transparency will be equally important. Public disclosures that traditional security programmes may not be prepared
from OpenAI, Anthropic, Meta, and Hugging Face to handle.
AI governance: risks and responsibilities have provided the cyber security community with
valuable insights into how these incidents occurred and Ultimately, the OpenAI-Hugging Face incident represents
The incidents involving OpenAI, Anthropic, and Meta what lessons can be learned from them. Continued a significant security event that has exposed important
illustrate that AI governance can no longer focus solely transparency will help organisations develop best questions surrounding accountability, governance,
on model outputs, bias, or misinformation. Increasingly practices, improve evaluation methodologies, and containment, and resilience in an era of increasingly
capable AI agents are becoming operational systems establish common expectations for responsible AI capable AI agents.
capable of interacting with software, infrastructure, development.
networks, and external organisations. As a result, As cyber security professionals, our focus should remain
governance frameworks must address not only what a For defenders, the broader lesson is clear: organisations on practical lessons rather than headlines. The future
model can say, but also what it can do. should assume that AI agents will continue to become of cyber security will likely involve both autonomous
more capable, more autonomous, and more adept at attackers and autonomous defenders. The organisations
A key lesson from these incidents is that model capability pursuing complex objectives. The goal of governance best positioned to succeed will not be those with the most
and environmental security cannot be treated as separate should therefore not be to prevent progress but to ensure powerful AI systems, but those that can govern, monitor,
concerns. Even highly capable systems remain dependent that advances in capability are matched by corresponding and control them effectively. In the end, the decisive factor
on the permissions, tools, and pathways available to them. improvements in oversight, containment, monitoring, and may not be model capability itself, but the maturity of the
accountability. security controls built around it.
14 | nccgroup.com Cyber Threat Intelligence Review of August | 15

Under cyber
attack?
Call our 24/7
Incident Response Hotline now.
NCC Group:
+44 (0)161 209 5200
response@nccgroup.com
www.nccgroup.com
Fox-IT:
+31 (0)88 369 23 78
fox@fox-it.com
www.fox-it.com
16 | nccgroup.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-28", "model": "unknown"} -->
