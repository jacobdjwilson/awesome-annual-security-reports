Threat
Monitor

Annual Report 2023

nccgroup.com

 1

## Foreword

In this year’s Annual Cyber Threat Monitor Report, we take a look back at the key events that shaped the cyber threat landscape in 2023, as well as looking ahead at the year to come, sharing insights from our Cyber Threat Intelligence team here at NCC Group.

2023 appeared to show signs that the international community beginning to take the threats from cyber adversaries more seriously.

We saw several examples of coordinated law enforcement action against criminal groups including key ransomware operators and individuals believed to be acting on behalf of foreign intelligence services. There was also consensus on the issue of ransomware, in that governments around the world have showed a united front against ransom payments and intelligence sharing through The International Counter Ransomware Initiative, which introduced several measures that offer a real opportunity to fight back against the pervasive threat from ransomware operators.

However, despite this, we saw the highest volume of ransomware victims NCC Group has ever recorded with an 84% increase in 2023 alone. The sheer volume of attacks and different types of victims proves that no organisation is safe.

Notably, ransomware operators employed new and innovative techniques to maximize their profits, targeting big software creators and managed service providers. So, even if an organisation does not perceive a direct threat from ransomware, it should consider the potential impact on its supply chain.

The ongoing threat to critical national infrastructure across the globe by hacktivists and Foreign Intelligence Services continued in 2023, following on from multiple geo-political conflicts in the Middle East, Eastern Europe, and Asia. National Cyber Security Centres in multiple countries have highlighted this threat and it is something we are monitoring as a priority moving in to 2024.

With those few things in mind, here we give further insight into what was a challenging 2023, and what organistions should be focusing on in the year ahead.

Matt Hull

Global Head of
Threat Intelligence

## CONTENT

Foreword by Matt Hull, Global Head of Threat Intelligence .........................................................................2

SECTION 1 - Critical Events Timeline ...........................................................................................................4

SECTION 2 - Incidents of Note ......................................................................................................................10

SECTION 3 - Law Enforcement Interventions ..............................................................................................14

SECTION 4 - Incident Response Findings ...................................................................................................20

SECTION 5 - SOC Findings ............................................................................................................................24

SECTION 6 - Ransomware Threat Landscape .............................................................................................28
Sectors ..............................................................................................................................................................32
Industrials ..........................................................................................................................................................33
Industries (Industrials) .......................................................................................................................................34
Consumer Cyclicals ...........................................................................................................................................35
Industries (Consumer Cyclicals) ........................................................................................................................36
Technology ........................................................................................................................................................36
Industries (Technology) .....................................................................................................................................38

SECTION 7 - Threat Actors ............................................................................................................................40
LockBit 3.0 .........................................................................................................................................................43
Sectors Targeted ...............................................................................................................................................45
Industries Targeted ............................................................................................................................................45
BlackCat ............................................................................................................................................................46
Sectors Targeted ...............................................................................................................................................47
Industries Targeted ............................................................................................................................................47
CL0P ..................................................................................................................................................................48
Sectors Targeted ...............................................................................................................................................49
Industries Targeted ............................................................................................................................................49

SECTION 8 - Regions .....................................................................................................................................50

SECTION 9 - Vulnerability Landscape .........................................................................................................52

SECTION 10 - Global Conflicts ......................................................................................................................56
Russian Invasion of Ukraine ..............................................................................................................................57
Increased Attacks, Reduced Impact ..................................................................................................................57
Influence and Information Operations ...............................................................................................................57
Disruption and Hacktivism .................................................................................................................................58
Destructive Operations ......................................................................................................................................58
Global Impact ....................................................................................................................................................59
Summary ...........................................................................................................................................................59
Israeli-Palestinian Conflict .................................................................................................................................59

SECTION 11 - Threat Spotlight ......................................................................................................................60

2

 3

### SECTION 01

### CRITICAL EVENTS TIMELINE

**10th Jan**
**Ransomware**
Royal Mail attack

Royal Mail suffered 6 weeks of disruption
to international postal services, affecting
11,500 Post Office branches.

This was due to a LockBit affiliate driven
ransomware attack, with Royal Mail
refusing to pay the ransom.

**30th Jan**
**Hacktivism**
Killnet targets NATO countries
supporting Ukraine
Pro-Russian Hacktivist group, Killnet,
launched DDoS attacks against US
healthcare organisations and public
healthcare sectors.

This followed claims the group
had successfully compromised US
Healthcare organisations. The motivation
is believed to be the retaliation against
countries in support of Ukraine, with
DDoS attacks also focused on other
NATO countries.

**7th Mar**
**Malware**
Emotet returns with new
evasion techniques
Emotet was observed returning after
a period of hiatus, with new evasion
techniques, allowing it to continue to
send malicious spam to victims, as
well as steal credentials and email
addresses, whilst enabling lateral
movement and download further
malware.

It has been observed being used by
Ransomware groups to distribute their
ransomware payloads.

**2nd Feb**
**Ransomware**
GoAnywhere MFT Zero-Day
exploited by CL0P
Remote Code Injection flaw, CVE-
2023-0669, on exposed administrative
consoles of GoAnywhere secure web file
transfer solution was shared by Fortra.

Reports at the time indicated that it had
been actively exploited by threat actors,
and later shown to be the case that
CL0P ransomware group was using this
flaw in a spate of ransomware attacks.

**14th Mar**
**Surveillance**
Russian state-sponsored TA
targets EU diplomatic entities
and systems

Nobelium, aka APT29 and Cozy
Bear, targeted European diplomatic
missions and systems sharing
sensitive political information, aiding
the Ukrainian government, and
helping Ukrainian citizens flee.

This group is affiliated with the
Foreign Intelligence Service of the
Russian Federation (FVR) and was
targeting Polish representatives
of the Ministry of Foreign Affairs
visiting the US with a spear-phishing
campaign compromising the official
EU electronic document exchange
system, LegisWrite.

4
4

 5
 5

**11th Jul**
**Breach**
Microsoft China Storm-0558
Using forged authentication tokens,
Microsoft revealed that Customer
email accounts were accessed
using Outlook Web Access (OWA)
Exchange Online.

China based threat actor,
Storm-0558 is believed responsible,
using the access to email accounts
to gather useful intelligence.

**8th Aug**
**Police Force: Data Leak**
FOI request leads to acci-
dental PII data leak

In response to a Freedom of
Information (FOI) request made to the
Police Service of Northern Ireland, a
spreadsheet detailing the locations
and names of serving employees was
mistakenly made public and posted
online, putting these employees at
risk.

Police forces in Norfolk and Suffolk
also confirmed FOI requests led
to inadvertently sharing too much
Personally Identifiable Information
(PII) publicly, whilst Cumbria
Police blamed human error for the
publication of the names and salaries
of all its officers online.

**23rd May**
**Barracuda**
Zero Day Vulnerability
Replace, don’t patch,
vulnerable devices

Barracuda announced a zero-day
vulnerability in their Email Security
Gateway, CVE-2023-2868, which
had been exploited in the wild,
the threat actor believed to be the
Chinese state affiliated UNC4841,
leveraging the flaw for espionage.

The threat actor quickly adapted
to containment and remediation
efforts, leaving Barracuda to take
the unusual step of recommending
customers replace their existing
appliances with new ones, rather
than rely on more typical remediation
efforts.

**29th Mar**
**Supply Chain Attack**
3CX Voice Over Internet
Protocol (VOIP) desktop
client compromised

North Korean threat actors
expected to be responsible for the
compromise, which was used to
go on to comprise 3CX customers
critical infrastructure organisations
within the energy sector.

A trojanised version of the legitimate
3CX software was used to
compromise their customers. What
set this attack apart is that the attack
was the result of an earlier supply
chain attack, with a 3CX employee
downloading malware infected
software package.

**31st May**
**Ransomware**
Move-IT Managed File
Transfer vulnerability in
mass Cl0p exploitation

Progress released a security
advisory regarding a Zero-Day
vulnerability, CVE-2023-34362, in
their managed file transfer (MFT)
software package, which had been
used to exfiltrate data.

Ransomware group CL0P was seen
to be leveraging this flaw, alongside
other File Transfer vulnerabilities,
to steal data to demand ransom
payments.

**14th Apr**
**Papercut: Ransomware**
 Zero-Day actively exploited
by Russian threat actors

Print Management Software maker,
Papercut, announced Remote Code
Execution (RCE) vulnerabilities in
Papercut NG and Papercut MF,
which could be levered without
authentication in this critically rated
CVE.

 A user account data flaw affecting
Papercut NG and Papercut MF was
also discovered, and both were
known to be exploited by threat
actors. Papercut has 100+ million
customers worldwide. Groups such
as LockBit then leveraged this flaw in
ransomware attacks.

**31st Aug**
**Malware**
Infamous Chisel
Ukraine Military Devices
targeted by Russian GRU

NCSC and its Five Eyes partners
issue a report associating Infamous
Chisel Malware targeting Ukrainian
military Android devices, with the
threat actor, Sandworm.

The malware allows for data
exfiltration and remote access.

The campaign is believed to be part
of the Russian war efforts against
Ukraine.

6
6

 7
 7

**20th Sept**
**FBI & CISA Advisory**
Law Enforcement – Snatch
Ransomware

The FBI and CISA released an
advisory warning that Snatch
threat actor group were targeting
a wide range of Critical National
Infrastructure (CNI) sectors for
ransomware attacks.

Sectors targeted included the
Defence Industrial Base (DIB), Food
and Agriculture as well as Information
Technology sectors.

**27 Sept**
**Law Enforcement**
Dual Ransomware Advisory

The US Federal Bureau of
Investigation (FBI) shared a
Private Industry alert warning of an
increasing trend of dual ransomware,
where victims were targeted with
more than one ransomware attack in
close succession, with threat actors
using different types of ransomware
in each instance.

Also noted was an increased use
of wiper malware to destroy data,
amongst other tactics to pressure
victims to pay ransom.

**27th Sept**
**Law Enforcement**
US and Japanese warn
of Chinese exploitation of
Cisco Router Firmware

China remains active in its offensive
cyber capabilities, warned US and
Japanese security agencies as
organisations in both countries
were targeted by People’s
Republic of China-linked threat
actors, BlackTech. Government,
Industrial, Technology, Media and
Telecommunication organisations
were amongst US and Japanese
targets, with attackers leveraging
flaws in Cisco routers.

The group breaches network devices
for international subsidiaries to then
pivot to corporate headquarters.

**7th Oct**
**Ransomware**
Caesars Casino
Hackers exfiltrated data from the
hotel and casino giant. They paid
$US 15,000,000 after negotiating
on the ransom. The threat actor
suspected to be responsible is
Scattered Spider, aka UNC3944.

**7th Oct**
**Geopolitics**
Hamas attack on Israel

Palestinian group, Hamas, officially
designated in many countries as a
terrorist organisation, launched an
armed assault against Israel.

1,200 civilians were killed in the
attacks making this one of the
deadliest attack in Israel’s history.
Hostages were also taken. 2
days later, the Israeli government
announced a complete siege of
Gaza, as a result of which over
23,000 Palestinians have since been
killed.

**12th Oct**
**Ransomware**
MGM Casino

MGM shared details of a
ransomware attack, which included
the theft of customer data, and cost
to the business in the region of $US
100,000,000.

BlackCat, aka AlphV subgroup of
Scattered Spider, took responsibility
for the attack, in which the casino
refused to pay the ransom.

**10th Oct**
**23andMe: Data Breach**
Genetic Company hacked,
and genetic ancestry data
leaked

A successful credential stuffing attack
allowed a threat actor to directly access
14,000 23andMe customer records,
stealing genetic ancestry information
and, in some cases, health related detail
based on the genetics. Some of the
stolen detail was leaked online and the
criminals offered the records for sale,
putting at risk particular groups.

Using the access to these accounts
allowed the threat actor to pivot from
there to scrape some detail from 6.9
million customers.

**12th Dec**
**Hack**
Kyivstar Telco company
disclosed records destroyed
by Russian state affiliated
TA

Russian threat actor, Sandstorm,
believed responsible for an attack
which disrupted Ukraine’s largest
mobile network operator so severely,
that its customer base of half the
population of Ukraine was left without
services for days.

This also meant they would not
receive alerts warning of Russian
attacks, therefore endangering
life. The attack wiped out ‘almost
everything’, leaving infrastructure
decimated.

 9
 9

### SECTION 02

### INCIDENTS OF NOTE

**Hybrid Warfare: Gaza conflict**

Throughout the year, the Russia and Ukraine conflict continued. However, the 7th October 2023 saw the Islamic Resistance Movement (Hamas) launch a surprise military operation against Israel. The cyber threat landscape has seen an interesting mirroring of the Russia-Ukraine conflict with hacktivism at the forefront of the cyber threat.

Mostly targeted against Israeli infrastructure, the activity has typically impacted the Availability vector of the CIA triad through Denial of Service (DoS) attacks. Furthermore, for the greatest impact, adversaries have been targeting Critical National Infrastructure sectors such as Energy and Defence, Telecommunications and Government to have the largest impact for their respective side.

The adversarial groups have also had a keen interest and relative success rate with specific targeting of Industrial Control Systems (ICS) in particularly SCADA.

**Companies targeted through digital supply chains: File sharing platforms targeted**

Throughout 2023, file sharing platforms were exploited across the globe to compromise organisations using them for data extortion and ransomware attacks.

Fortra’s GoAnywhere MFT software was targeted early in the year through a zero-day vulnerability tracked as CVE-2023-0669, which leveraged remote command execution to deploy ransomware to the userbase.

CL0P managed to successfully breach 130 companies and exposed millions of individual’s private data using this vulnerability. This flaw was patched in version 7.1.2.

Furthermore, in June 2023, MOVEit was exploited through additional zero-day vulnerabilities tracked as CVE-2023-35708 and CVE-2023-34362.

This attack had far-reaching consequences, including organisations that had supply chain usage of the tool.

This attack has been documented as the biggest data theft of 2023, with over 2,000 organisations compromised and the data theft impacting 62 million individuals. Patches are available for these vulnerabilities and should be applied.

**Capita Breach**

In March 2023, Capita, an outsourcing company suffered a data breach which impacted 90 organisations.

Microsoft 365 applications and had Black Basta ransomware deployed to 0.1% of their server estate.

This was reduced due to the intervention of Capita to stop movement. However, the reputational damage and financial impact has been costly for the company as they suffered direct cyber incident costs of around £25m. The groups share price dropped 12% showing the reputational damage of the attack starting to show in public markets.

The costs continue to mount for the company too, as they lost £67.9m for the first six months to June 2023 compared to a profit of £100,000 a year earlier.

The company attributed these losses to the fall out of the cyber incident and cannot determine the size of the fine yet.

This attack shows the real impact that supply chains can have on organisations and proves the need to hold third parties to the same security standards as your own organisation, which might include standards such as ISO27001.

10

 11

**Data compromise exposes data for hundreds of millions of individuals: KidSecurity app**

In September 2023, a tracking app for parents to know where their children are, KidSecurity, was found to have not configured authentication for their Elasticsearch and Logstash collections.

The app with over 1,000,000 downloads from the Google Play store inadvertently left user activity logs publicly available to the internet for over a month.

The instance contained over 300 million records with private data including 21,000 phone numbers and 31,000 email addresses.

This exposure also showed payment details including the first six and last four digits of card numbers, expiry dates and the issuing bank. There have been indications that threat actors have leveraged this misconfiguration to leak the data.

Open instances of Elasticsearch are often leveraged by attackers to exploit vulnerabilities.

**Ransomware re-encryption after failed negotiations: Henry Schein ransomware and data breach**

In October 2023, healthcare solutions giant Henry Schein suffered from re-encryption of their files after negotiations stalled with the ransomware group Alphv. The group claimed to have 35TB of sensitive data.

The re-encryption happened just as the company got back to operating capabilities, so this was a big setback for the company and caused a lack of availability for its applications and ecommerce platform which triggered another two weeks of operational disruption.This breach included 35,000,000 records.

**Ransomware halted physical delivery: Royal Mail hit by LockBit**

In January, Royal Mail discovered a cyberattack which halted their international shipping services due to what they referred to as, “severe service disruption.”

It later surfaced that the threat group responsible for the attack was LockBit, who announced their role in a post published on a Russian-speaking hacking site. Royal Mail were able to re-establish most of their international shipping services by the 3rd of February on Twitter, and declared that they were fully operational on the 21st of February 2023.

On the 23rd of February, LockBit leaked 44GB of data stolen from Royal Mail, as they refused to pay the £66 million ransom due to it being ‘an absurd amount of money.’

The leaked data included files relating to “various parts of Royal Mail’s business…technical information, contracts with third- party suppliers, human resource and staff disciplinary records, details of salaries and overtime payments, and even one staff member’s Covid-19 vaccination records.”

The ransom has since lowered to £33m, but Royal Mail have shown no signs of giving in to the threat groups demands.

This is an excellent example of the real-world implications of cybercrime, notably where operational disruption is concerned, with the impact extending beyond the victim itself. UK residents were forced to use alternative shipping solutions for their international exports, also highlighting the impact on customer confidence.

12

 13
 13

### SECTION 03

### LAW ENFORCEMENT INTERVENTIONS

**TrickBot:**

Trickbot is a banking trojan which started off as a derivative of the Dyre banking trojan in 2016 before evolving independent features which turned it into a flexible and modular piece of malware, enabling cybercriminals to deploy multiple payloads including malware.

Joint sanctions between the United Kingdom and the United States were levied against 11 named individuals believed to have been involved in the development of the TrickBot trojan. Additionally, two individuals have been arrested and faced charges relating to their involvement with the banking trojan, a Latvian national, Alla Witte, plead guilty to conspiracy to commit computer fraud for their involvement with the group, and in June 2023 was sentenced to 32 months imprisonment.

Additionally, Russian national Vladimir Dunaev, was arrested in South Korea in September 2021 and was extradited to the United States; he plead guilty to committing computer fraud and identity theft as well as conspiracy to commit wire fraud and bank fraud, and faces up to a maximum of 35 years in prison upon his scheduled sentencing on 20 March 2024.

**Sanctions against North Korea:**

In May, the US Treasury Department’s Office of Foreign Assets Control (OFAC) levied sanctions against four corporate, government, and academic entities as well as one individual for their involvement in international fraud for the purposes of raising funds for the North Korean regime.

Thousands of workers hide their identity to be hired as IT professionals overseas in order to generate revenue for the government through receiving foreign salaries and funnelling them back to Pyongyang.

Some of these workers receive salaries in excess of a quarter of a million dollars, and while this may not be applicable for every one of the illicit IT workers, the economy of scale through utilising thousands of DPRK agents means the Kim regime is able to generate significant funds.

US Secretary of State, Anthony Blinken, summarises the issue as:

“The DPRK conducts malicious cyber activities and deploys information technology (IT) workers abroad who fraudulently obtain employment to generate revenue that supports the Kim regime . . . The DPRK’s extensive illicit cyber and IT worker operations threaten international security by financing the DPRK regime and its dangerous activities, including its unlawful weapons of mass destruction (WMD) and ballistic missile programs.”

**BreachForums and Pompompurin**

US authorities in March arrested the threat actor responsible for successfully hacking the FBI in 2021.

Conor Brian Fitzpatrick, known online by his alias Pompompurin, and is also connected to the FBI’s InfraGard network breach in 2022, the 2022 Twitter data leak, the 2021 Robinhood hack, as well as being the owner of BreachForums.

BreachForums rose to take the place of RaidForums after its own takedown at the hands of the FBI in 2022 and has been host to such data as PII of roughly 170,000 individuals affected by the DC Health Link breach in March 2023.

Only 20 at the time of his arrest, Fitzpatrick was charged with three crimes: conspiracy to commit access device fraud; solicitation for the purpose of offering access devices; and possession of child pornography.

Held on a $300,000 bond paid by his parents, Fitzpatrick has since pled guilty to all three charges and faces up to a maximum of 40 years behind bars.

14

 15

**Ukrainian phishing ring busted**

Ukrainian cyber authorities apprehended members of a phishing ring responsible for stealing over £3 million/160 million Ukrainian hryvnia from over one thousand victims spread across Poland, Spain, France, Portugal, Czechia, and other European nations.

Joint raids were conducted on over 30 locations, resulting in the seizing of computer equipment, mobile phones, and numerous SIM cards used as part of numerous phishing campaigns.

The perpetrators of these campaigns created over 100 different phishing sites to trick victims into thinking they could purchase cheap goods, upon which the scammers would then use the payment card details for further fraudulent campaigns.

In addition to the phishing sites themselves, the group employed scammers in call centres based in Lviv and Vinnytsia for the purposes of adding legitimacy to the fake online stores through talking to victims and encouraging them to complete purchases.

This operation was conducted in collaboration with authorities from Czechia and resulted in two arrests made within Ukraine, as well as 10 more in undisclosed countries in Europe.

The suspected leaders face charges on fraud and creating criminal organisations and could face up to 12 years in jail if successfully prosecuted.

**Spanish authorities arrest 40 members of the Trinitarios group**

Authorities in Spain arrested 40 members of the notorious Trinitarios crime group in May.

The group was responsible for carrying out numerous fraud campaigns, facilitated by initial phishing and smishing attacks with which they gained banking and payment card details of victims, used to generate approximately €700,000 from over 300,000 victims.

Some of the proceeds were used to pay the legal fee of members who were already incarcerated, bought drugs for resale, as well as to purchase property in the Dominican Republic.

13 homes located across Spain in Madrid, Seville, and Guadalajara, were raided as part of the campaign to arrest the gang members, resulting in the seizure of computer equipment and cash, as well as tools for conventional crimes such as lock picks.

Amongst the 40 individuals arrested, there are thought to be two hackers who were primarily responsible for carrying out phishing and smishing attacks, as well as 15 others who are charged with crimes such as bank fraud and identity theft, typical crimes resulting from falling victim to a phishing attack.

This case shows how the gap between cybercrime and conventional crime is narrowing as the two fields merge.

**LockBit affiliate arrested**

A Russian national was arrested and charged in June for his role as an affiliate of the LockBit Ransomware-as-a-Service (RaaS) group.

Ruslan Astamirov is accused of at least five attacks between 2020 and early 2023 against victims across the globe, including in the United States.

He faces charges of conspiring to commit wire fraud and conspiring to intentionally damage protected computers and to transmit ransom demands, and faces up to a maximum of 25 years in prison.

This second LockBit arrest in six months prompted the U.S. Attorney Philip R. Sellinger for the District of New Jersey to say;

“The LockBit conspirators and any other ransomware perpetrators cannot hide behind imagined online anonymity.

We will continue to work tirelessly with all our law enforcement partners to identify ransomware perpetrators and bring them to justice.”

16

 17
 17

**6,500 arrests plus nearly a billion seized**

Following its initial compromise by European law enforcement agencies in 2020, further efforts have targeted the userbase of EncroChat.

The encrypted communications platform which ran on a specially hardened version of the Android operating system offered users self-destruct features, panic wipe capabilities, 24/7 customer support, and more for a one-time payment of €1,000 and €1,500 for a 6 month subscription.

More than 6,500 arrests have since been made, including of 197 high-value targets. This was done through analysing over 100 million conversations between approximately 60,000 users of the platform.

Through utilising this data, law enforcement agencies across Europe were able, in addition to the thousands of arrests, seize 270 tons of narcotics, 971 vehicles, 271 properties, 923 weapons, 68 explosives, 40 planes, 83 boats, as well as €740 million in cash in addition to freezing a further €154 million.

Europol states that a third of EncroChat users were members of organised crime groups, a third were drug traffickers, while the rest were included money launderers, murderers, and firearms traffickers.

This campaign sent shockwaves through OCGs (Organised Criminal Groups) across Europe, and further highlighted the intersection between conventional criminal activity and cyber-enabled crimes.

**Man indicted after acting as malicious insider against water treatment facility**

July saw the indictment Rambler Gallo, a former employee of a Massachusetts based company operating at the Discovery Bay Water Treatment Facility in California, after his alleged attack on the facility in January 2021.

Gallo, the former Instrumentation and Control Tech at the facility, is alleged to have installed software on his own private computer as well on the private internal network of his employer, and, upon resignation from the company in January 2021, exploiting his remote access to uninstall software which was the main hub of the network and which was responsible for protecting the entire water treatment system including filtration, chemical levels, and water pressure.

He faces up to 10 years behind bars and up to $240k for the charge of transmitting a program, information, code, and command to cause damage to a protected computer, in violation of 18 U.S.C. §§ 1030(a)(5)(A) and (c)(4)(B)(i).

This Discovery Bay facility attack, as well as the similar attack on the water system of Oldsmar in early 2021, likely contributed to the March 2023 decision of the Biden administration to make the conducting of cyber security audits on public water systems mandatory.

18
18

 19

### SECTION 04

### INCIDENT RESPONSE FINDINGS

Our Incident Response data represents cases handled by our CIRT Team when responding to NCC clients. In 2023, the Financials sector observed the greatest percentage of incidents raised (15%), closely followed by Industrials (14%) and Government (14%).

This reflected a shift in the top-three targeted sectors in 2022, from Government (18%), Industrials and Financials in joint second (13%) and Technology and Consumer Cyclicals (11%) in joint third.

Over the last two years, the data suggests that Financials and Industrials remain of consistent interest to threat actors, with a growth of 2% in incident response cases for the Financials sector between 2022 and 2023.

This is likely a combination of the potential for financial gain understood by cybercriminals where targeting these sectors successfully, as well as the continued need for sufficient cyber security hygiene to combat ever growing cyber threats.

20

 21

![Figure 1: Percentage of CIRT Cases by Sectors Impacted](placeholder_for_image_1)

Analysis of attack categories found that most incidents concerned Unauthorised Access (36%), Phishing (16%) and Malicious Code (15%).

Where the top-targeted sector was concerned, Financials, most attacks were related to Unauthorised Access (5%) and Phishing (5%).

Remaining aware of possible signs of authorised access such as unusual activity on devices, as well as ensuring appropriate phishing training and awareness can support organisations to prevent or minimise potential attacks.

![Figure 2: CIRT Cases by Attack Type 2023](placeholder_for_image_2)

22

 23
 23

### SECTION 05

### SOC FINDINGS

Data collated from our Global Security Operations Centre (SOC) reported 3493 true positive incidents across the European and APAC SOCs. 2023 saw a 36% increase from the 2559 true positive cases observed in 2022, reflecting a growth in the number of tickets raised across NCC Group’s client base.

This may also be in line with a growth in NCCs clientele, amounting to a greater number of incidents overall and not necessarily a growth in global security incidents. Regardless, in this section we will dive into the dataset to better understand the course of events throughout the year.

![Figure 3: Month-by-Month Count of Incidents Raised in the SOC (2023)](placeholder_for_image_3)

July recorded the greatest number of tickets raised
with 356 in total, followed by November in second
place with 336.

Comparing with the figures for 2022 (see Figure
4) we instead saw a steady growth for the period
January-May with a peak in May with 297 tickets
raised.

This was followed by a drop in June with 175 and a
growth spurt again for the period June – September;
with the highest number of tickets recorded for 2022
being in September or a total of 350.

However, this peak was again followed by a rapid
decline for the period October – December, ending
the year with 192 tickets raised in December.

As seen in Figure 3, we observe a much steadier
flow of tickets raised in 2023 for the period January –
June. After which, we notice the peak to 356 tickets
raised in July, followed by a slight decrease to 312 in
August then we see a steady increase for the period
September - November.

Similar to the previous two years, the month of
December tends to mark some of the lowest ticket
activity recorded throughout the year as whole. In
2023, we observe that the lowest number of tickets
raised was in fact in December with a total of 150.

It is, however, difficult to pinpoint a root cause for
the spike in July and November activity as a number
of variables may be at play, from client security
practices to a growth in cybercrime activity.

24

 25

While analysing incidents by sector (Figure 6), we
notice that NCC Group’s clients within Academic
& Educational Services were most susceptible to
incidents with a total of 810 recorded.

Again, this is likely to be influenced by NCC Group’s
client base as a whole. With that in mind, it is worth
mentioning that Academic & Educational Services
was also ranked as the most targeted sector in 2022
with 657 incidents.

Year-on-year, the number of incidents recorded for
the sector has experienced an increase of 23%.
Interestingly, the sector was also the top target in
2021 with 255 incidents recorded at the time.

Given the overall number of tickets recorded in the
period 2021 – 2023 for Academic & Educational
Services, there is a high possibility that this would
continue to be the case in 2024, so we would
strongly recommend that clients within the sector
stay vigilant and ensure best security practices are
followed.

The remaining targets within the top five for
2023 are actually the same sectors as in 2022
with the differences being; the higher number of
incidents recorded year-on-year as well as a shift
in Technology’s position from fifth in 2022 to third
in 2023, which means that Financials and Energy
moved to fourth and fifth respectively.

With regards to the figures, all sectors have
experienced an increase in incidents raised.
However, we notice that Technology and Energy’s
sectors have experienced the highest increases with
161% (from 217) and 95% (from 261) respectively.

Finally, Industrials and Financials’ targeting
increased by 46% (from 439) and 20% (from 435)
respectively.

We would highly recommend that clients operating
within these sectors review their defensive
mechanisms.

![Figure 4: Month-by-Month Count of Incidents Raised in the SOC (2022)](placeholder_for_image_4)

Next, we dissect the number of cases raised by true positive category, captured in Figure 5, and notice the
following; overall, 1263 incidents were mitigated (36%), and 1574 (45%) required no action, hence, the vast
majority (82% or 2837) did not need to be escalated, with no further action needed.

Finally, 588 cases were escalated to the client (17%).

![Figure 5: Number of Cases by True Positive Category (2023