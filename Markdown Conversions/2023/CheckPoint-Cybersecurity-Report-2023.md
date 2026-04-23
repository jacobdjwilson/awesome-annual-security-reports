# 2023 CYBER SECURITY REPORT

## Table of Contents
- [Chapter 1: Introduction to the 2023 Cybersecurity Report](#chapter-1-introduction-to-the-2023-cybersecurity-report)
- [Chapter 2: Timeline of Key 2022's Cyber Events](#chapter-2-timeline-of-key-2022s-cyber-events)
- [Chapter 3: 2022's Cybersecurity Trends](#chapter-3-2022s-cybersecurity-trends)
  - [Russo-Ukrainian conflict](#russo-ukrainian-conflict)
  - [The year of wiper disruption](#the-year-of-wiper-disruption)
  - [Hacktivism graduates to major player on geopolitical stage](#hacktivism-graduates-to-major-player-on-geopolitical-stage)
  - [Weaponization of Legitimate Tools](#weaponization-of-legitimate-tools)
  - [Ransomware Extortion—Shifting focus from encryption to data extortion](#ransomware-extortionshifting-focus-from-encryption-to-data-extortion)
  - [Mobile Malware Landscape—The Risk of Trusting the Familiar](#mobile-malware-landscape-the-risk-of-trusting-the-familiar)
  - [Cloud: Third Party Threat](#cloud-third-party-threat)
- [Chapter 4: Global Analysis](#chapter-4-global-analysis)
- [Chapter 5: High Profile Global Vulnerabilities](#chapter-5-high-profile-global-vulnerabilities)
- [Chapter 6: Incident Response Perspective](#chapter-6-incident-response-perspective)
- [Chapter 7: 2023 Insights for CISOs: Disruption and Destruction](#chapter-7-2023-insights-for-cisos-disruption-and-destruction)
- [Chapter 8: Prevention is at Reach](#chapter-8-prevention-is-at-reach)
- [Chapter 9: Malware Family Descriptions](#chapter-9-malware-family-descriptions)
- [Chapter 10: Conclusion](#chapter-10-conclusion)

---

## Chapter 1: Introduction to the 2023 Cybersecurity Report
**By Maya Horowitz**

In 1976, Queen Elizabeth II sent the first royal email. It was sent over ARPANET, 7 years before the internet was invented, and a long 13 years before the first recorded internet hack.

Almost 50 years later, email has evolved into a popular communication method, and the most popular vehicle for threat actors to initiate their attacks. In fact, the Check Point Research (cp<r>) annual Security Report shows that in 2022, the proportion of email-delivered-attacks has increased, reaching a staggering record of 86% of all file-based attacks in-the-wild.

In our Security Report, we discuss a few more trends observed by cp<r> throughout the year. The Russia-Ukraine war demonstrated how the traditional, kinetic, war can be augmented by a cybernetic war. It has also influenced the broader threat landscape in the rapid changes of hacktivism and how independent threat actors choose to work for state-affiliated missions. The war has also seen enhanced usage of wiper malware, and this trend has been adopted by several actors, reaching a point where 2022 has seen more wiper attacks globally, than in the previous decade altogether. Traditional cybercrime has also changed—in 2022, threat actors started using more legitimate tools in their operations, including native operating system files, IT software and penetration testing tools, all helping them in their efforts to stay under the radar. In their ransomware attacks, threat actors are starting to skip the encryption process, realizing that the financial rewards comes mostly from data breaches and the threat to publish victim data.

In attacks on mobile devices, attackers make a habit out of mimicking legitimate applications, and in the cloud threat landscape—companies’ data is at risk mostly when hosted by third parties, and susceptible to attacks due to misconfigurations, over-permissive roles and permissions, and access keys stored publicly.

In the last days of 2022, we witnessed a dramatic advancement in the field of generative artificial intelligence, now widely available to the public, and which is able to generate highly professional text (code included) on demand in seconds. As we step into 2023, we should keep in mind that this technology may quickly be adopted by threat actors, to craft even more malicious emails, in even better quality than those typically authored by threat actors, and with endless variations of malware and malicious code in general. This comes to prove, yet again, the importance of zero day prevention of attacks, across the entire IT infrastructure, including email, endpoint, network, cloud, and everything in between.

Check Point Software is committed to ensuring our customers are provided the best and prevention-first security across all these vectors. At Check Point Research, we are happy to provide this annual Security Report to help in raising awareness and vigilance, so that we can all join hands in preventing the next cyberattack.

**Maya Horowitz**
VP Research at Check Point Software Technologies

---

## Chapter 2: Timeline of Key 2022's Cyber Events

![Timeline of 2022 events]

*   **January**: Ukraine government websites defaced; Iran state broadcaster hacked by opposition group.
*   **February**: Ransomware attack on oil terminals in Belgium, Germany, and the Netherlands; DDoS attacks on Ukraine; Russia-Ukraine conflict cyber-espionage surges.
*   **March**: Ukraine "IT Army" attacks Russian sites; Lapsus$ breaches NVIDIA and Samsung; Miratorg Agribusiness hit by ransomware.
*   **April**: Spike in APT attacks using war lures; Spring4shell vulnerability; ALHACK vulnerabilities in ALAC audio format; Everscale wallet vulnerability.
*   **May**: Costa Rica state of emergency due to Conti ransomware; Lincoln College closes after ransomware; Sberbank DDoS attack; Turla reconnaissance campaign.
*   **June**: Follina vulnerability (CVE-2022-30190) exploited; Largest HTTPS DDoS attack mitigated; Russian intelligence increases attacks on NATO-supporting nations.
*   **July**: Norway and Lithuania DDoS attacks; Twitter data breach (5.4 million accounts).
*   **August**: Atlassian Confluence vulnerability; Cisco breached by Yanluowang; Killnet targets Lockheed Martin; South Staffordshire Water ransomware; Apple zero-day patches; Nitrokod crypto-mining campaign.
*   **September**: Moscow taxi service Yandex hacked; Albania government systems disrupted by Iran-linked attacks; Uber data breach; Record-breaking DDoS attack.
*   **October**: Iranian regime targeted by hacktivists; Optus data breach (10 million Australians); Killnet targets US state websites; MyDeal, Medibank, Vinomofo, and EnergyAustralia breaches; Aurubis cyberattack; OpenSSL high-severity vulnerability.
*   **November**: IT Army of Ukraine claims access to Russia's Central Bank; Malicious PyPI package; Azov wiper distributed; Meta fires employees for bribery; European Parliament DDoS attack; Black Basta campaign.
*   **December**: Medibank data released on dark web; Schoolyard Bully Android Trojan; Cloud Atlas cyber-espionage analysis; AI risks (ChatGPT/Codex) discussed.

---

## Chapter 3: 2022's Cybersecurity Trends

### Russo-Ukrainian conflict
The ongoing Russian-Ukrainian war has had a profound effect on cyberspace. The role of cyberwarfare has been well documented in this first full-blown hybrid conflict. While cyber activity cannot win the war on its own, it plays a significant part in tactical operations and has an indisputable psychological and economic effect.

### The year of wiper disruption
Wipers are destructive malware designed to inflict damage with limited potential for financial gain. In 2022, we saw a massive uptick in disruptive cyberattacks carried out by Russia against Ukraine, with at least nine different wipers deployed in less than a year.

### Hacktivism graduates to major player on geopolitical stage
Hacktivism has matured. Groups like the "IT Army of Ukraine" and the Russia-affiliated "Killnet" operate with military-like structures, conducting recruitment, training, and target allocation. The boundaries between state-sponsored cyber operations and hacktivism have become increasingly blurred.

### Weaponization of Legitimate Tools
Threat actors are shifting away from custom malware to "Living off the Land" (LotL) techniques, utilizing built-in operating system capabilities and legitimate IT management tools (e.g., Cobalt Strike, Brute Ratel, Atera, Wazuh) to evade detection.

### Ransomware Extortion—Shifting focus from encryption to data extortion
Ransomware actors are increasingly skipping the encryption process, focusing instead on data exfiltration and extortion to maximize pressure on victims.

### Mobile Malware Landscape—The Risk of Trusting the Familiar
Attackers are increasingly mimicking legitimate applications to distribute mobile malware, exploiting user trust in familiar brands and services.

### Cloud: Third Party Threat
Companies' data is at risk when hosted by third parties, susceptible to attacks due to misconfigurations, over-permissive roles, and publicly stored access keys.

---

## Chapter 4: Global Analysis
*(Content omitted in source)*

## Chapter 5: High Profile Global Vulnerabilities
*(Content omitted in source)*

## Chapter 6: Incident Response Perspective
*(Content omitted in source)*

## Chapter 7: 2023 Insights for CISOs: Disruption and Destruction
*(Content omitted in source)*

## Chapter 8: Prevention is at Reach
*(Content omitted in source)*

## Chapter 9: Malware Family Descriptions
*(Content omitted in source)*

## Chapter 10: Conclusion
*(Content omitted in source)*

---

ecome

more	dominant	in	the	ransomware	crime

scene,	and	better	skilled	at	identifying	sensitive

information	in	victims’	networks,	even	skip	the

encryption	phase	altogether	and	rely	solely	on

data	publication	threats	to	generate	ransom

payments.	This	may	have	serious	implications

for	defense	mechanisms,	attribution,	and	future

analysis	of	the	ransomware	ecosystem.

Ransomware	attack-management	has	also

evolved	with	an	increase	in	threat	actors	that

operate	a	Ransomware-as-a-Service	model

(RaaS)	through	affiliates.	Affiliates,	who

may	participate	in	multiple	RaaS	programs

simultaneously	and	choose	between	various

encryption	tools	have	become	the	”producers”,

initiating	attacks	and	paying	part	of	the

revenue	back	to	the	RaaS	operator.	Affiliates

In	the	early	days,	ransomware	attacks were

further	outsource	operations	by	purchasing

conducted	by	single	entities	who	developed

stolen	credentials	or	network	access	from

and	distributed	massive	numbers	of	automated

access-brokers.	The	fragmented	nature	of	this

payloads	to	randomly	selected	victims,

operation	complicates	the	attribution	of	attacks

collecting	small	sums	from	each	“successful”

and	the	tracking	of	criminal	entities.	Tactics,

attack.	Fast	forward	to	2022	and	these	attacks

techniques,	and	procedures	(TTPs)	used	to

have	evolved	to	become	mostly	human-operated

gain	initial	access	to	a	system	are	no	longer

processes,	carried	out	by	multiple	entities	over

necessarily	connected	to	the	affiliate	or	to	the

several	weeks.	The	attackers	carefully	select

RaaS	payload	later	deployed.

3434

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   3

Current	Ransomware-as-a-Service	(RaaS)

was	first	observed	in	2020,	and	is	referred	to

actors	are	competing	for	the	attention	of

as Triple	Extortion.	Many	different	types	of

affiliates,	and	typically	charge	10%	-	20%	of

information	are	considered	sensitive,	from

the	ransom	payment	as	a	fee	for	their	services.

corporate	financial	and	proprietary	data	to

The	speed	of	the	encryption	module	is	one	of

personal	data	relating	to	physical	or	mental

the	main	“selling	points”,	allowing	the	attacker

health,	financial	data	or	any	other	personal

to	reduce	the	encryption	time	and	probability

identifiable	information	(PII),	which	makes

of	detection.	RaaS	actors’	attempts	to	shorten

the	threat	of	data	exposure	even	more	potent.

encryption	time	include	allowing	affiliates

to	choose	from	various	encryption	modes

or	even	offering	partial	file	encryption

(“intermittent	encryption”).

Negotiation	with	the	victims	is	often	conducted

over	relatively	secure	mediums,	using

proprietary	access	codes.	This	is	typically

done	to	prevent	uncontrolled	publication

Some	groups	now	skip	the	encryption	phase

which	would	result	in	reduced	potential

altogether,	relying	on	threats	of	data	exposure

leverage.	At	least	in	theory,	victims	who	pay

alone	to	extort	money.	In	September	2021,

can	emerge	from	an	attack	relatively

a	group	named	Karakurt	Team	started	to

unscathed,	without	their	details	posted	on

employ	extortion	without	encryption.	Attacking

Karakurt’s	shame-site,	and	thereby	stopping

mostly	North	American	and	European	victims,

their	customers	or	the	authorities	from

Karakurt	operators	typically	contact	their

finding	out	they	have	been	attacked.

victims,	provide	screenshots	and	copies	of

the	stolen	data,	and	threaten	to	auction	the

information	or	release	it	unless	their	demands

are	met.	They	often	contact	the	victims’

employees,	business	partners	and	clients

to	ramp	up	the	pressure.	This	new	behavior,

involving	direct	contact	with	the	victims’	clients,

An	example	of	the	effectiveness	of	the	threat	of

personal	data	exposure	was	demonstrated	in	a

recent	attack	on	Medibank,	an	Australian	health

insurer,	in	October	2022.	When	the	company

refused	to	pay	ransom	demands	of	$10M,	the

attackers	(possibly	connected	to	the	REvil

group)	dumped	massive	amounts	of	personal

information	relating	to	pregnancy	termination,

drug	and	alcohol	abuse,	mental	health	issues

and	other	confidential	and	highly	sensitive

medical	data	relating	to	millions	of	Australian

and	international	customers.

3535

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   3

The	Lapsus$	group	also	received	a	lot	of	public

added searchable	data	mechanisms,	allowing

attention	following	a	series	of	data	breaches

employees,	customers	and	other	potential

of	large	tech	companies,	including	Microsoft,

victims	to	search	repositories	of	stolen	data.

Nvidia	and	Samsung.	Since	its	first	recorded

Also,	valuable	stolen	data	is	often	monetized

attack	in	December	2021	on	the	Brazilian	health

by	selling	it	on	Darknet	markets.

ministry,	in	which	they	stole	and	threatened	to

publish	medical	information	regarding	COVID-19

vaccinations,	the	group	has	focused	on	data

exfiltration	rather	than	encryption.	Headed

by	young	criminals	of	British and Brazilian

nationality,	Lapusus$	uses	various	methods

to	gain	initial	access	to	their	victims,	including

payments	to	employees,	purchasing	credentials

and	social	engineering.	The	group	focuses	on

locating	and	exfiltrating	the	proprietary	source

code	of	their	victims’	products.	The	ensuing

threat	of	publication	is	estimated	to	have

generated	$14M	in	revenue	after	only	a	few

months	of	activity.

Some	RaaS	actors	even	recommend	their

affiliates	to	avoid	encrypting	critical	areas

such	as	data	belonging	to	healthcare	patients.

They	permit	attacking	and	exfiltrating	data

from	hospitals	but	not	encrypting	them,

suggesting	some	twisted	version	of	a	moral

code	among	hackers.	Hive	RaaS,	which	focuses

on	healthcare,	sometimes	makes	an	effort	to

not	disable	the	systems.	Publishing	stolen	data

has	proven	effective	and	threat	actors	have

developed	elaborate	extortion	mechanisms.

BlackCat	and	Lockbit	ransomware	groups

Other	threat	actors	have	turned	to	destroying

data	instead	of	encrypting	it.	The	Onyx

ransomware	group,	active	since	April	2022,

destroys	files	larger	than	2MB	instead	of

encrypting	them.	Others	have	followed	suit.

A	new	sample	of	the	ExMatter	exfiltration	tool

now	includes	dedicated	wiping	functionality.

Although	it	was	initially	detected	as	part	of

the	BlackMatter	RaaS	in	late	2021,	ExMatter

development	is	attributed	to	an	affiliate	and

not	the	RaaS	entity.	This	marks	the	possible

independence	of	ransomware	affiliates	from

their	RaaS	partners.

Choosing	to	base	their	extortion	solely	on

data	publication	is	understandably	attractive

to	attackers.	It	offers	the	option	of	quick

deployment,	without	a	prolonged	and	messy

encryption	process,	thereby	reducing	the

possibility	of	detection.	Victim	management

becomes	simpler.	There	is	no	need	to	supply

individual	decryption	keys	to	different	victims

and	operate	a	logistically	complicated

“customer	support”	mechanism.	Above	all,

it	frees	affiliates	from	their	dependence	on

large	RaaS	actors	who	demand	their	share

of	the	income.

3636

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   3

As	this	data	extortion	model	becomes	prevalent,

and	existing	protection	mechanisms	which	are

possible	ramifications	include	increased

based	on	detecting	encryption	activity	could

fragmentation	of	the	ransomware	ecosystem.

prove	less	effective.	In	its	place,	cyber	security

Attribution	of	ransomware	operations	and

providers	will	need	to	focus	more	on	data

tracking	threat	actors	may	become	even	harder

wiping	and	exfiltration	detection.

I TAY   C O H E N

Technology	Leader,
Check	Point	Software
Technologies

  A s this data extortion model becomes prevalent, possible

ramifications include increased fragmentation of the

ransomware ecosystem. Attribution of ransomware operations

and tracking threat actors may become even harder and

existing protection mechanisms which are based on detecting

encryption activity could prove less effective. In its place,

cyber security providers will need to focus more on data

wiping and exfiltration detection.

3737

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023RANSOMWAREC H A P T E R   3

MOBILE MALWARE L ANDSCAPE—
THE RISK OF TRUSTING
THE FAMILIAR

In	our	2022	mid-year	report	we	reviewed	some

Mod	APKs	(Android	Package	Kits;	applications

major	events	in	the	mobile	threat	landscape,

for	Android	devices)	are	reworked	copies	of

including	the	vast	increase	in	the	number	of

well-known	applications,	designed	to	provide

malicious	applications	infiltrating	Google	and

users	with	extended	functionalities	or	access

Apple	stores.	Often	disguised	as	innocent

that	are	not	available	in	the	original	version.

applications	like	QR	readers,	external	Bluetooth

In	the	past	few	years,	we	have	seen	modified

apps,	flashlights	or	games,	they	are	designed

versions	of	a	variety	of	applications,	from

to	attract	as	little	attention	as	possible.	In

instant	messaging	and	social	media	apps,	to

our	latest	analysis,	we	focus	on	attempts	to

live	streaming,	VPN	services	and	more.	The

hide	mobile	malware	in	“unofficial”	versions

apps	are	usually	distributed	through	unofficial

of	well-known	applications.	Mostly,	these

channels	to	users	looking	for	free	versions

are	malicious	modified	versions	(aka	Mods),

of	known	apps,	or	for	additional	features

typically	distributed	through	third-party	app

that	do	not	exist	in	the	original	versions.	In

stores	and	downloaded	by	users	who	prefer	an

some	cases,	users	are	targeted	and	offered

unofficial	version	for	a	variety	of	reasons.	This

direct	links	to	the	modified	APKs.	In	others,

is	not	a	completely	unheard	of	threat,	but	2022

users	seek	them	out	voluntarily	due	to	limited

has	seen	multiple	attacks	using	apps	that	are

access	to	official	applications.	For	example,

well	known,	trusted,	and	widely	used.

FMWhatsApp	allows	users	to	redesign	their

WhatsApp	interface	and	edit	the	“last	seen”	and

“blue	tick”	functionalities.	These	Mods	are	not

scrutinized	as	carefully	as	the	official	version,

which	makes	them	a	natural	exploitation

target	for	threat	actors.	Often	the	infection	is

achieved	through	advertisement	SDKs,	used	by

the	Mods’	developers.	This	was	the	case	with

HMWhatsApp	infection	with	the	Triada	Trojan	in

August	2021,	and	APKPure	later	that	year.

3838

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023When	made	aware	of	these	threats,	WhatsApp

In	most	cases,	Mods	are	not	distributed	through

issued an alert	in	July	2022,	warning	users

official	app	stores.	However,	sometimes

not	to	use	modified	versions	of	the	app,

unsuspecting	users	can	obtain	them	through

and	described	its	joint	efforts	with	Google

official	channels.	In	October,	WhatsApp’s

to	eradicate	previous	malicious	versions.

parent	company	Meta,	filed	a	lawsuit	against

Despite	this	warning,	another	modified	build

three	companies	based	in	China	and	Taiwan	for

of	WhatsApp	was	reported	in	October	2022.

developing	unofficial	versions	of	the	application,

Once	again,	the	YoWhatsApp	Mod	was	found

and	selling	them	on	their	websites	and	in	the

to	contain	the	Triada	malware.	When	it	is

Google	Play	Store.	Once	installed,	the	modified

implemented	in	a	fully	functioning	version	of	the

application	was	used	to	hijack	accounts	and

popular	messenger	app,	the	malware	is	granted

steal	sensitive	information	from	more	than	one

extensive	permissions,	including	access	to

million	Android	users.

SMS	messages,	similar	to	the	permissions

the	official	WhatsApp	app	receives.	This	can

allow	threat	actors	to	bypass	Multi	Factor

Authentication	mechanisms	and	take	over	a

wide	range	of	applications	and	accounts,	from

email	to	banking	and	corporate	accounts,	as

well	as	the	WhatsApp	account	itself.	The	latest

campaign	deploying	Triada	malware	through

modified	applications,	which	was	reported	by

Check	Point	Research,	weaponized	copies	of

the	Telegram	messaging	app	to	steal	personal

information	from	multiple	users.

Mods	have	also	been	used	by	nation-state

actors.	In	August,	researchers	exposed	the

Dracarys	Android	spyware	deployed	in	a

modified	version	of	the	Signal	messaging

application.	Despite	reports	of	attacks	against

its	users,	Signal	is	considered	a	secured

messenger,	but	its	modified	version	provided

attackers	with	extensive	spying	capabilities

along	with	its	regular	functions.	The	operation

was	attributed	to	Bitter	APT,	a	group	known

to	operate	in	South	Asia,	which	is	reportedly

also	producing	similar	Mods	for	Facebook,

3939

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023MALWAREC H A P T E R   3

Telegram,	YouTube	and	WhatsApp.	The

financially	or	politically	motivated	actors.	This

attack	was	deployed	using	phishing	sites

was	the	case	in	2018	and	2019	when	the	Iranian

that	mimicked	the	genuine	Signal	site,	and

government	blocked	secure	instant	messaging

most	likely	targeted	users	through	phishing

(IM)	apps,	resulting	in	an	increase	in	cloned

emails	and	social	media.	Meta	also	accused

unofficial	versions	of	Telegram,	Instagram	and

Transparent	Tribe	(APT-36),	a	Pakistan	affiliated

other	IM	applications.	Many	of	the	unofficial

state-sponsored	threat	actor,	of	creating	and

applications	were	later	revealed	as	part	of	a

using	fake	versions	of	WhatsApp,	WeChat

government	program	to	spy	on	and	control

and	YouTube,	and	identified	more	than	10,000

opposition	and	minority	groups.

potentially	affected	users.

Mobile	devices	are	targeted	by	hostile	entities

Malicious	modified	versions	of	two	mobile	VPN

for	a	variety	of	reasons	and	motivations.

applications,	SoftVPN	and	OpenVPN,	were	used

Attackers	often	target	the	most	popular,

to	spy	on	users	by	the	mercenary	Bahamut	APT

well-	known	and	widely	used	applications

group,	which	offers	hacking	services	to	a	wide

which	users	would	consider	safe.	Exploits

range	of	clients.

Populations	of	totalitarian	regimes	often	have

limited	access	to	applications	in	the	official	app

stores	and	must	seek	other	alternatives.	This

makes	them	more	susceptible	to	attacks	by

can	come	in	either	the	form	of	modified	or

fake	applications,	or	through	the	exploitation

of	vulnerabilities	in	the	original	versions.	We

should	take	this	as	a	reminder	of	the	need	to

stay	vigilant,	especially	when	using	the	most

popular	and	widely	used	applications.

S H A N I   S H P R I N G E R

Data	Research	Analysis
Team	Leader,
Check	Point	Software
Technologies

Mobile devices are targeted by hostile entities for a variety of

reasons and motivations. Attackers often target the most popular,

well- known and widely used applications which users would

consider safe. Exploits can come in either the form of modified

or fake applications, or through the exploitation of vulnerabilities

in the original versions. We should take this as a reminder of the

need to stay vigilant, especially when using the most popular and

widely used applications.

4040

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   3

CLOUD:
THIRD PART Y THREAT

Over	the	past	few	years,	Check	Point	Research

(cp<r>)	has	been	tracking	the	increasing

adoption	of	cloud	infrastructure	in	corporate

environments,	as	well	as	the	evolution	of	the

cloud	threat	landscape.	Currently,	around	98%

of	organizations	use	cloud-based	services,	and

76%	of	them	have	multi-cloud	environments

that	incorporate	services	from	two	or	more

cloud	providers.

When	comparing	the	past	two	years,	we	have

seen	a	significant	increase	in	the	number

of	attacks	on	cloud-based	networks	per

organization,	which	shot	up	by	48%	in	2022

compared	with	2021.	Although	the	overall

number	of	attacks	on	cloud-based	networks	is

17%	lower	than	non-cloud	networks,	a	closer

examination	of	the	types	of	attacks	shows	that

newly	disclosed	vulnerabilities	(2020-2022)	are

exploited	more	frequently	on	cloud-based	than

on-premise	environments.	This	might	indicate

a	shift	that	some	threat	actors	now	prefer

to	scan	the	IP	range	of	cloud	providers.	This

might	enable	to	gain	easier	access	to	sensitive

information	or	critical	services.

27.4%

22.9%

Cl oud

On- prem

Figure	1	-	Percentage	of	attacks	leveraging	recent

vulnerabilities	(disclosed	2020-2022)

In	addition	to	vulnerability	exploitation

attempts,	cloud	environments	have	become

both	a	source	and	target	of	security	incidents

and	breaches	that	involve	improper	access

management,	sometimes	combined	with	the

use	of	compromised	credentials.	In	March	2022,

the	ransomware	gang	Lapsus$	announced	in	a

statement	on	its	Telegram	channel	that	it	had

gained	access	to	Okta,	an	identity	management

platform.	Lapsus$	has	a	history	of	publishing

4141

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   3

sensitive	information,	often	source	code,	stolen

On	its	Telegram	channel,	Lapsus$	claimed	that

from	high-profile	tech	companies	such	as

Okta	was	storing	AWS	keys	in	Slack	and	that

Microsoft,	NVIDIA,	and	Samsung.	However,	this

Okta’s	third-party	support	engineers	had	access

time,	the	actors	claimed	their	target	was	not

to	all	the	company’s	8,600	Slack	channels.	It

Okta	itself,	but	rather	its	customers.

is	possible	that	Lapsus$	gained	initial	access

BEFORE PEOPLE START ASKING: WE DID NOT
ACCESS/STEAL ANY DATABASE FROM OKTA - our
focus was ONLY on okta customers.

Figure	2	-	L APSUS$	announcement	about	OKTA	on	their
telegram	channel

Following	the	breach,	Okta	released	an	official

statement	revealing	that	approximately	2.5%	of

their	customers	were	affected	by	the	Lapsus$

breach—around	375	companies,	according

to	independent	estimates.	Okta,	is	used	by

thousands	of	companies	to	manage	and	secure

user	authentication	processes,	as	well	as	by

developers	to	build	identity	controls.	This

effectively	means	that	hundreds	of	thousands

of	users	worldwide	could	potentially	be

compromised	by	the	company	responsible

for	their	security.

to	Okta	via	Slack	using	stolen	cookies	and/

or	social	engineering.	cp<r>	suggested	that

Lapsus$’s	access	to	Okta	clients	could	explain

the	cybercrime	gang’s	modus	operandi	and

impressive	record	of	successes,	all	thanks	to

excessive	permissions	granted	to	a	third-party

within	the	corporate	cloud	environment.	Identity

and	Access	Management	(IAM)	role	abuse	attacks

were	thoroughly	discussed	by	cp<r>	in	2021,

and	while	this	is	still	an	ongoing	issue,	there	are

other	risks	of	which	businesses	need	to	be	aware.

On	September	16,	2022,	Uber	stated	that	they

were responding	to	a	security	incident	which

they	later	attributed	to	a	hacker	connected	to

the	very	same	Lapsus$	group.	The	company

explained	that	the	attacker	used	stolen

credentials	of	an	Uber	contractor	in	a	Multi

Factor	Authentication	fatigue	attack,	where

the	contractor	was	flooded	with	two-factor

authentication	(2FA)	login	requests	until	one

of	them	was	accepted.	These	credentials	were

then	used	for	lateral	movement	and	privilege

escalation	that	resulted	in	the	intruder	gaining

administrator	access	to	Uber's	AWS	cloud

account	and	its	resources.

4242

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   3

Towards	the	end	of	the	year,	Uber	suffered	another

From	basic	rules	like	not	storing	cloud

high-profile	data	leak	that	exposed	sensitive

access	keys	publicly	or	not	ignoring	2FA

employee	and	company	data.	This	time,	attackers

bypass	attempts,	to	more	complicated	but

breached	the	company	by	compromising	an	AWS

essential	ones	such	as	prevention	of	cloud

cloud	server	used	by	Tequivity,	which	provides

misconfigurations	and	using	proper	IAM,	the

Uber	with	asset	management	and	tracking

events	of	2022	show	that	any	violations	of

services.	It	is	not	clear	if	the	unauthorized	access

these	rules	puts	cloud	environments	at	risk.

was	due	to	misconfiguration	or	stolen	credentials,

but	it’s	evident	that	we	need	to	adapt	our	methods

of	assessing	third-party	risk	to	the	world	of

cloud	infrastructure.

O M E R   D E M B I N S K Y

Data	Research	Group	Manager,
Check	Point	Software
Technologies

When comparing the past two years, we have seen a significant

increase in the number of attacks on cloud-based networks per

organization, which shot up by 48% in 2022 compared with 2021.

Although the overall number of attacks on cloud-based networks

is 17% lower than non-cloud networks, a closer examination of

the types of attacks shows that newly disclosed vulnerabilities

(2020-2022) are exploited more frequently on cloud-based than

on-premise environments. This might indicate a shift that some

threat actors now prefer to scan the IP range of cloud providers.

This might enable to gain easier access to sensitive information

or critical services.

4343

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023THREATC H A P T E R   4

GLOBAL
ANALYSIS

44

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

CYBER ATTACK CATEGORIES BY REGION

GLOBAL

MULTIPURPOSE MALWARE*

32%

INFOSTEALERS

24%

CRYPTOMINERS

16%

MOBILE

9%

RANSOMWARE
7%

Figure	3:	Percentage	of	organizations	affected	by	malware	type	globally	in	2022.

* Banking Trojans and botnets, previously classified as two distinct types, are combined in a single category. As many banking Trojans received additional functionalities,
making the differentiation between the two categories less distinct, we introduce the category “multipurpose malware” to include both genres.

AMERICAS

23%

18%

MULTIPURPOSE MALWARE

INFOSTEALERS

CRYPTOMINERS

12%

MOBILE

7%

RANSOMWARE
5%

Figure	4:	Percentage	of	organizations	affected	by	malware	type	in	the	Americas	in	2022.

CHECK POINT SOFT WARE  |  SECURITY REPORT 2023
CHECK POINT SOFT WARE  |  SECURITY REPORT 2022

45
4545

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023CYBER ATTACK CATEGORIES BY REGION

C H A P T E R   4

EMEA

33%

25%

MULTIPURPOSE MALWARE

INFOSTEALERS

CRYPTOMINERS

15%

MOBILE

8%

RANSOMWARE
8%

Figure	5:	Percentage	of	organizations	affected	by	malware	type	in	EMEA	in	2022.

APAC

MULTIPURPOSE MALWARE

44%

30%

25%

INFOSTEALERS

CRYPTOMINERS

MOBILE

14%

RANSOMWARE

9%

Figure	6:	Percentage	of	organizations	affected	by	malware	type	in	APAC	in	2022.

CHECK POINT SOFT WARE  |  SECURITY REPORT 2023
CHECK POINT SOFT WARE  |  SECURITY REPORT 2022

46
46

C H A P T E R   4

GLOBAL THREAT INDEX MAP

The	map	displays	the	cyber	threat	risk	index	globally,	demonstrating	the

main	risk	areas	around	the	world.*

*	Darker	=	Higher	Risk

*	Grey	=	Insufficient	Data

Figure	7.	Global	Threat	Index	Map

4747

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

Education / Research

Government / Military

Healthcare

Communications

ISP / MSP

Finance / Banking

Utilities

Insurance / Legal

Manufacturing

Leisure / Hospitality

SI / VAR / Distributor

Retail / Wholesale

Transportation

Software Vendor

Consultant

Hardware Vendor

2314

(+43%)

1661

(+46%)

1463

(+74%)

1380
1372

(+27%)

(+28%)

1131
1101

(+52%)

(+48%)

(+47%)

(+36%)

(+60%)

(+18%)

957
950
943
904
871

(+66%)

750
747

(+41%)

(+37%)

689

(+19%)

448

(+25%)

Figure	8	-	Global	Average	of	weekly	attacks	per	organization	by	Industry	in	2022	[%	of	change	from	2021]

Data	collected	in	2022	shows	a	continued	rise	in	attacks	against	all	industries.	Most

targeted	are	the	educational	and	research	institutions,	with	an	average	of	2,314

attacks	per	week	per	organization,	an	increase	of	more	than	40%	from	2021.	Attacks

on	the	healthcare	sector	registered	the	highest	surge,	74%	more	attacks	than	last

year,	placing	it	as	the	third	most	targeted	industry	in	this	index.	From	hospitals

and	clinics	to	research	facilities,	attackers	have	been	focusing	on	the	healthcare

industry	since	the	beginning	of	the	COVID-19	pandemic,	seeking	financial	gain.	89%	of

healthcare	organizations	reported	cyberattacks	within	the	last	year	with	an	average

total	cost	reaching	$4.4M.	Reported	attacks	included	the	CommonSpirit	Health,	the

second	largest	non-profit	hospital	chain	in	the	US.	CommonSpirit,	which	operates	140

hospitals,	has	reported	data	of	more	than	600K	patients	stolen,	the	attack	resulting

in	medical	damage	to	patients.	Hospitals	in	New	York	were	hit	by	ransomware	in

November	leaving	medical	systems	down	for	weeks	after	the	attack.	An	attack	on	the

Dallas-based	Tenet	health	care	cooperation,	operating	hundreds	of	medical	sites,

caused	disruption	to	acute	care	operations.	Among	ransomware	groups	reported	to

target	healthcare	organizations	are	Lockbit,	BlackCat,	Cuba,	Zeppelin	and	more.

4848

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

2018

2019

2020

2021

33%

36%

17%

16%

67%

64%

83%

84%

2022

14%

86%

EMAIL

WEB

Figure	9:	Delivery	Protocols—Email	vs.	Web	Attack	Vectors	in	2018-2022.

4949

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023

C H A P T E R   4

TOP MALICIOUS FILE T YPES—WEB VS. EMAIL

57%

10%

8%

5%

4%

3%

exe

pdf

dll

xls

lnk

ps1

2%

jar

1%

1%

1%

html

xlsb

doc

Figure	10:	Web—Top	malicious	file	types	in	2022.

26%

22%

17%

15%

9%

4%

3%

3%

0.8%

0.6%

exe

pdf

xls

xlsx

xlsm

docx

rtf

doc

html

vbs

Figure	11:	Email—Top	malicious	file	types	in	2022.

5050

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

51%

15%

9%

6%

4%

2%

2%

2%

zip

rar

img

gz

7z

r00

cab

iso

1%

z

1%

tgz

Figure	12:	Top	malicious	archive	files	delivered	by	both	Web	and	Email	in	2022.

The	proportion	of	email-delivered-attacks	has	increased,	reaching	a	staggering

record	of	86%	of	all	file	based	in-the-wild	attacks.	Data	shows	an	increase	in

the	utilization	of	various	types	of	archive	file	formats,	as	threat-actors	attempt

to	conceal	malicious	payloads.	Included	in	password	protected	archives,

the	functionality	of	malware	is	hidden	until	they	are	extracted,	making	their

identification	as	malicious	by	security	products	especially	challenging.	Zip	files

are	the	most	commonly	used	format	for	this	purpose,	while	in	the	top	malicious

archives	types	we	observe	also	.img	and	.iso	files,	since	their	extraction

functionality	is	integrated	in	Windows	or	with	very	popular	tools.	Archive	files

are	often	used	to	bypass	the	mark-of-the-web	based	protection	mechanism.

5151

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

GLOBAL MALWARE STATISTICS

Data	comparisons	presented	in	the	following	sections	of	this	report	are	based	on	data	drawn	from

the	Check	Point	ThreatCloud	Cyber	Threat	Map	between	January	and	December	2022.

For	each	of	the	regions	below,	we	present	the	percentage	of	corporate	networks	impacted	by	each

malware	family,	for	the	most	prevalent	malware	in	2022.

GLOBAL

10%

8%

4%

3%

3%

3%

2%

2%

2%

1%

Lokibot

XMRig

njRAT

Guloader

Remcos

Qbot

SnakeKeylogger

Emotet

AgentTesla

Formbook

AMERICAS

8%

Emotet

Figure	13:	Most	prevalent	malware	globally—2022

3%

3%

2%

2%

2%

AgentTesla
Qbot

Formbook

Guloader

1%

1%

1%

1%

XMRig

njRAT

SnakeKeylogger

Remcos

Lokibot

Figure	14:	Most	prevalent	malware	in	the	Americas—2022

5252

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

10%

9%

4%

4%

4%

3%

2%

2%

1%

1%

Emotet

AgentTesla

Formbook

Lokibot

XMRig

Remcos

njRAT

Guloader

Qbot

SnakeKeylogger

Figure	15:	Most	prevalent	malware	in	EMEA—2022

ASIA PACIFIC (APAC)

15%

14%

9%

7%

5%

4%

3%

3%

2%

2%

Lokibot

XMRig

Ramnit

Qbot

njRAT

Glupteba

Emotet

AgentTesla

SnakeKeylogger
Formbook

Figure	16:	Most	prevalent	malware	in	APAC—2022

5353

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

GLOBAL ANALYSIS OF TOP MALWARE

Rising	back	from	its	fourth	place	in	Check	Point’s	2021	most	prevalent	malware

list,	Emotet	has	regained	its	position	at	the	top	of	2022	table,	affecting	10%	of	all

corporate	networks.	Initially	discovered	in	2014	as	a	banking	Trojan,	Emotet	has

developed	into	a	significant	multipurpose	malware,	serving	as	an	initial	access

malware	and	used	by	sophisticated	Eastern	European	cyber	criminals.	Identified

as	one	of	the	major	cyber	threats,	Emotet	was	taken	down	in	January	2021,	on	a

global	law	enforcement	operation,	only	to	resurge	by	the	end	of	that	year.	On	its

return	Emotet	was	distributed	with	Trickbot’s	assistance	and	later	deployed	large

scale	spam	campaigns	with	malicious	Office	documents.	Relying	heavily	on	Office

macros’	exploitations,	Microsoft’s	intension	to	disable	VBA	macros	in	documents

obtained	from	the	internet	was	expected	to	affect	Emotet’s	distribution.	Emotet’s

operators	prepared	for	the	change,	experimenting	with	alternative	file	types

including	.lnk,	.xll zip	and	.iso	files.	In	November,	Emotet	returned	from	one	of

its	routine	breaks,	and	went	back	to	its	previous	weapon	of	choice—Excel	files

with	malicious	macros.	To	bypass	the	Mark-of-the-Web	limitations,	the	attached

maldocs	displayed	detailed	instructions	directing	users	to	copy	the	files	into

the	trusted	“Templates”	folder.	Emotet	continues	to	use	email	threads	hijacking

technique	and	customizes	email	content	according	to	the	targeted	country.	Emotet

was	observed	deploying	other	malware	families	like	IcedID	and	XMRig	on	victim

system.	Other	Emotet	campaigns	in	2022	include	a	campaign	targeting	IKEA

employees;	a	US	phishing	campaign	impersonating	the	IRS	during	the	2022	tax

season	and	many	more.

Infostealers	occupied	a	central	place	in	this	year’s	table,	with	four	of	the	most

commonly	used	stealers,	AgentTesla,	Formbook,	SnakeKeylogger	and	LokiBot

occupying	the	top	six	places	in	our	top	malware	list.	The	popularity	of	infostealers

is	connected	to	the	growing	market	for	stolen	credentials	and	their	availability

to	threat	actors	for	relatively	low	prices.	One	of	the	emerging	techniques	of

cyber	cybercriminals	is	using	infostealers	for	widely	spread	infections	that

are	not	specifically	focused	on	corporate	networks.	After	the	initial	infection,

cybercriminals	mine	the	data	to	identify	corporate	VPN	credentials,	which	will

allow	them	to	get	an	initial	access	to	corporate	networks.

5454

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

TOP MULTIPURPOSE MALWARE

GLOBAL

AMERICAS

22%

3%
5%

5%

5%

15%

Emotet

Qbot

Raspberry Robin

Phorpiex

Glupteba

Icedid

Other

45%

19%

3%
5%

5%

6%

19%

Emotet

Qbot

Raspberry Robin

Phorpiex

Glupteba

Icedid

Other

43%

Figure	17:	Most	prevalent	multipurpose
malware	globally

Figure	18:	Most	prevalent	multipurpose	malware
in	the	Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

23%

3%
3%
4%

5%

17%

Emotet

Qbot

Raspberry Robin

Phorpiex

Glupteba

Icedid

Other

46%

23%

3%
5%

6%

7%

9%

Emotet

Qbot

Glupteba

Phorpiex

Raspberry Robin

Mylobot

Other

47%

Figure	19:	Most	prevalent	multipurpose	malware
in	EMEA

Figure	20:	Most	prevalent	multipurpose	malware
in	APAC

5555

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

MULTIPURPOSE MALWARE GLOBAL ANALYSIS

As	in	our	last	midyear	report,	two	malware	categories,	banking	Trojans	and

botnets,	which	were	previously	classified	as	distinct	types,	have	been	merged.

As	many	banking	Trojans	received	additional	functionalities,	that	make	the

differentiation	between	the	two	categories	less	distinct,	we	introduce	the	unified

category,	“multipurpose	malware”.	Comparisons	in	this	category	therefore	relate

to	the	last	midyear	report	rather	than	to	older	annual	data.

Emotet and Qbot	have	increased	their	relative	activity	and	now	comprise	of	more

than	60%	of	infection	attempts	in	this	category.	Raspberry Robin is	a	new	entrant

to	the	multipurpose	list.	First	detected	in	September	2021	using	infected	USB

devices	and	wormable	capabilities	to	spread,	Raspberry	Robin	has	become	one

of	the	largest	active	malware	distribution	platforms	within	a	year.	It	was	reported

to	deploy	various	other	malware	families,	including	IcedID,	Bumblebee	and

ransomware	brands	like	Clop	and	LockBit.	With	possible	relations	to	Evil	Corp

this	malware	constitutes	a	serious	new	threat.

The Phorpiex	botnet,	which	has	been	known	for	distributing	other	malware

families	via	spam	campaigns,	as	well	as	for	fueling	large-scale	spam,	sextortion

campaigns	and	ransomware	spread,	started	2022	with	crypto-transaction	hijacking

and	continues	its	expansion,	occupying	the	fourth	place	in	the	multipurpose	table.

Glupteba	has	fully	returned	from	the	2021	takedown	operation	carried	out	by

Google.	This	malware	features	a	variety	of	capabilities	including	a	credential

stealer,	crypto	miner,	router	exploiter	and	more.	However,	Glupteba	is	best	known

for	its	use	of	the	bitcoin	blockchain	technology	as	its	C&C	infrastructure	to	receive

configuration	information.	Glupteba’s	use	of	bitcoin	records	improves	its	resilience

against	takedowns,	since	the	blockchain	transactions	cannot	be	deleted,	however

they	remain	exposed	for	public	inspection.	Tracking	Glupteba’s	activity	through

the	blockchain	has	exposed	a	large	ongoing	campaign	which	started	in	June	2022.

5656

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

TOP INFOSTEALER MALWARE

GLOBAL

AMERICAS

11%

1%
5%

AgentTesla

Formbook

SnakeKeylogger

12%

35%

Lokibot

Vidar

Pony

Other

16%

20%

16%

2%

8%

12%

29%

12%

22%

AgentTesla

Formbook

SnakeKeylogger

Lokibot

Vidar

RedLine Stealer

Other

Figure	21:	Top	infostealer	malware	globally

Figure	22:	Top	infostealer	malware	in	the	Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

10%

1%
4%

AgentTesla

Formbook

SnakeKeylogger

12%

38%

Lokibot

Vidar

xloader

Other

15%

19%

8%

1%
5%

12%

35%

17%

21%

AgentTesla

Formbook

SnakeKeylogger

Lokibot

Vidar

Pony

Other

Figure	23:	Top	infostealer	malware	in	EMEA

Figure	24:	Top	infostealer	malware	in	APAC

5757

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

INFOSTEALER MALWARE GLOBAL ANALYSIS

The	growing market for	stolen	credentials	and	cookies,	which	are	later	used	in

the	evolving	life	cycle	of	access-brokers,	ransomware	affiliates	and	RaaS

suppliers,	has	contributed	to	the	growing	popularity	of	infostealers.	Check	Point

data	reveals	a	steady	increase	in	infostealers	use,	affecting	18%	of	corporate

networks	in	2020,	21%	in	2021	and	reaching	as	much	as	24%	of	all	organizations	in

2022.	Infostealers	are	sold	on	underground	forums	for	a	monthly	subscription	fee

that	ranges	between	$60	to	$1,000,	to	threat	actors	of	varying	levels	of	technical

knowledge.	This	market,	which	was	previously	divided	between	multiple	smaller

malware	families,	has	consolidated	and	this	year	three	brands,	AgentTesla,

Formbook	and	SnakeKeylogger	are	responsible	for	71%	of	Check	Point	monitored

infostealers	attacks.

Formbook,	detected	in	20%	of	infostealer	cases	is	a	commodity	malware

sold	as-a-service	on	underground	forums	since	2016.	It	is	designed	to	collect

keystrokes,	search	and	access	files,	take	screenshots,	harvest	browser

credentials	and	download	and	deploy	additional	payloads.	It	has	been	used

by	multiple	actors,	often	distributed	using	email	attachments	including	pdf,

doc,	RTF	document,	exe,	zip,	rar	etc.	Formbook	has	been	deployed	this	year

targeting	Ukraine	and	in	numerous	other	campaigns.

The SnakeKeylogger	modular	.NET	infostealer	has	tripled	its	rank	compared	to

our	2021	top	malware	statistics.	Snake	first	surfaced	around	late	2020,	and	quickly

grew	in	popularity	among	cyber	criminals.	Snake’s	main	functionalities	include

recording	keystrokes,	taking	screenshots,	harvesting	credentials	and	clipboard

content,	in	addition	to	supporting	exfiltration	of	the	stolen	data	by	both	HTTP	and

SMTP	protocols.	In	August,	researchers	observed	SnakeKeylogger	in	malspam

campaign	spreading	via	phishing	emails	to	target	IT	firms	located	in	the	US.

5858

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

TOP CRYPTOMINING MALWARE

GLOBAL

AMERICAS

1%

5%

8%

10%

1%

4%

4%

7%

XMRig

LemonDuck

Wannamine

Kinsing

Other

76%

XMRig

LemonDuck

Wannamine

Lucifer

Other

84%

Figure	25:	Top	cryptomining	malware	globally

Figure	26:	Top	cryptomining	malware	in	the	Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

2% 6%
3%

5%

XMRig

LemonDuck

Wannamine

JenkinsMiner

Other

84%

XMRig

LemonDuck

Wannamine

NRSMiner

Other

2%

5%

14%

15%

64%

Figure	27:	Top	cryptomining	malware	in	EMEA

Figure	28:	Top	cryptomining	malware	in	APAC

5959

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

CRYPTOMINERS GLOBAL ANALYSIS

The	crypto	market	cap	has	fallen	dramatically	in	2022,	losing	nearly	$2	Trillion,

from	a	record	$2.9T	in	November	2021.	Low	crypto	rates	combined	with	increased

mining	costs	affect	mining	profitability	and	with	it	the	motivation	for	cryptomining.

This	explains	cryptominers’	visibility	decreasing	from	21%	in	2021	to	16%	globally

in	2022.	This	decline	has	left	XMRig,	a	legitimate	open-source	mining	tool,	as	the

most	dominant	tool	used	by	attackers	for	malicious	purposes.	XMRig	has	been

used	in	76%	of	cryptomining	attacks	in	2022	and	as	reported	in	the	CPIRT	chapter

often	marks	a	breach	which	could	later	lead	to	the	deployment	of	other	malware.

LemonDuck,	a	relatively	new	cryptomining	malware	has	no	legitimate	use,

and	since	its	initial	detection	in	2019	added	extensive	malicious	functionalities

including	credential	stealing	and	lateral	movement.	As	Lemonduck	is	equipped

with	the	ability	to	drop	additional	tools	for	human-operated	attacks,	its	detection

should	be	treated	seriously	as	a	possible	precursor	for	severe	attacks.

6060

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

TOP MOBILE MALWARE

GLOBAL

AMERICAS

25%

20%

8%

5%

5%

42%

Joker

Anubis

AlienBot

Hiddad

Hydra

Other

26%

24%

31%

6%

7%

11%

Joker

Anubis

AlienBot

Hydra

Hyddad

Other

Figure	29:	Most	prevalent	banking	Trojans	globally

Figure	30:	Most	prevalent	banking	Trojans	in	the	Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

19%

Anubis

Joker

AlienBot

Hydra

Hiddad

Other

49%

18%

9%

5%

6%

Joker

Anubis

Sharkbot

Hiddad

AlienBot

Other

38%

34%

5%

5%

5%

17%

Figure	31:	Most	prevalent	banking	Trojans	in	EMEA

Figure	32:	Most	prevalent	banking	Trojans	in	APAC

6161

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   4

MOBILE MALWARE GLOBAL ANALYSIS

Joker,	an	Android	mobile	malware,	is	a	stealer	capable	of	accessing	SMS

messages,	contact	lists	and	device	information	but	mostly	generates	income

through	unauthorized	subscriptions	to	paid	premium	services.	Joker	uses	its

access	to	SMS	messages	to	authenticate	requests	and	authorize	payments.

Joker	(aka	Bread)	was	first	identified	in	2017	concealed	in	more	than	1,700	benign

looking	applications	offered	on	Google	Play	Store.	The	malware	has	resurged	this

year,	hiding	in	at	least	8	applications	on	Google	Store	with	more	than	3	million

downloads	in	2022,	climbing	to	the	top	of	Check	Point’s	global	mobile	malware	list.

Anubis	is	a	banking	Trojan	malware	designed	for	Android	mobile	phones.	Since	it

was	initially	detected	in	2017,	it	has	gained	additional	functions	including	Remote

Access	Trojan	(RAT)	functionality,	keylogging,	and	audio	recording	capabilities.

It	has	been	detected	on	hundreds	of	different	applications	available	in	the	Google

Store	reaching	Check	Points	top	mobile	malware	list	earlier	this	year.

6262

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   5

HIGH PROFILE
GLOBAL
VULNERABILITIES

6363

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   5

The	following	list	of	top	vulnerabilities	is	based	on	data	collected	by	the	Check

Point	Intrusion	Prevention	System	(IPS)	sensor	net	and	details	some	of	the	most

popular	and	interesting	attack	techniques	and	exploits	observed	by	cp<r>	in	2022.

PROX YSHELL VULNERABILITIES (CVE-2021-34473,
CVE-2021-34523 AND CVE-2021-31207)

This	is	the	name	given	to	an	attack-chain	which	exploits	three	vulnerabilities

in	Microsoft’s	Exchange	Server.	Combining	these	vulnerabilities	allows

unauthenticated	attackers	to	perform	Remote	Code	Execution	(RCE)	on	vulnerable

servers.	All	three	vulnerabilities	have	been	reported	and	patched	in	2021	they

remain	at	the	top	of	the	most	exploited	vulnerabilities	list	even	in	2022.	Some	of

the	reasons	for	their	popularity	with	attackers	are	their	simple	exploitation,	the

prevalence	of	MS	Exchange	servers	with	government	and	large	businesses	and

the	fact	they	were	thoroughly	analyzed,	and	discussed	by	researchers.	Check

Point	data	shows	that	21%	of	our	customers	have	been	impacted	with	ProxyShell

attempts	in	2022.	ProxyShell	vulnerabilities	have	been	exploited	for	a	variety	of

motivations	including	by	financially	motivated	threat	actors	to	deploy	ransomware,

for espionage	in	the	Middle	East	and	Africa	and	by	Iranian	APT	entities	to	gain

access	to	American,	Australian,	Canadian	and	UK	entities.	Check	Point	Incident

Response	Team	(CPIRT)	investigations	found	ProxyShell	exploitations	in	one

in	every	six	attack	cases.	Together	with	ProxyLogon	and	the	recently	reported

ProxyNotShell,	these	MS	Exchange	vulnerabilities	constitute	a	significant	attack

surface,	frequently	exploited	in	the	wild,	often	resulting	in	major	breaches.

6464

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023
C H A P T E R   5

FOLLINA IN MICROSOFT OFFICE (CVE-2022-30190)

Reported	in	May	2022,	this	vulnerability	in	Microsoft	Support	Diagnostic	Tool

(MSDT)	is	exploited	using	Microsoft	Office	documents.	Microsoft	has	gone	a

long	way	in	their	effort	to	reduce	attacks	utilizing	office	documents	by	disabling

macros	in	documents	from	external	sources.	Exploiting	the	new	Follina

vulnerability,	attackers	are	now	using	specially	crafted	.docx	and	.rtf	documents

to	download	and	execute	malicious	code	even	in	Protected	Mode	and	when	macros

are	disabled.	Despite	Microsoft’s	mitigation	efforts,	threat	actors	have	exploited

Follina	in	unpatched	systems	to	deploy	Qbot,	and	other	RATs,	making	Follina

one	the	most	frequently	used	vulnerability	discovered	in	2022	contributing	to

the	popularity	of	malicious	office	docs.

FORTINET CVE-2022-40684 AND CVE-2022-42475

Two	critical	bugs	reported	in	October	(CVSS	score:	9.6)	and	December	(CVSS	score:

9.3)	in	Fortinet	products	allow	unauthenticated	attackers	to	execute	arbitrary

code	via	specially	crafted	requests.	The	company	notified	of	in-the-wild

exploitations	and	issued	updates	while	CISA	warned	of	significant	risk	to

the	federal	enterprise.	Exploitation	attempts	of	CVE-2022-40684	in	the	last

3	month	impacted	18%	of	organizations.

6565

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   5

2022

2021

2020

2019

2018

2017

2016

2015

2014

2013

2012

Earlier

6%

5%

9%

9%

7%

7%

4%

12%

11%

10%

10%

10%

Figure	33:	Percentage	of	attacks	leveraging	vulnerabilities	by	Disclosure	Year	in	2022.

4

6

8

10

12

2

0

New	vulnerabilities	discovered	and	reported	in	2022	have	been	quickly

weaponized	and	used	by	threat	actors	this	year.	Compared	to	only	2%	of	attacks

in	2021	using	same-year	vulnerabilities,	this	year	they	were	observed	in

6%	of	the	attacks	monitored	by	Check	Point.	In	addition	to	the	vulnerabilities

reviewed	above,	the	Atlassian	Confluence	RCE	(CVE-2022-26134)	and	F5	BIG	IP

(CVE-2022-1388)	reviewed	in	our	midyear	report	contributed	their	share	to

new	exploitation	attempts.	Our	data	shows	that	vulnerabilities	reported	in	the

last	three	years	made	up	24%	percent	of	exploitation	attempts	compared	to

only	18%	in	2021.	This	indicates	an	upgrade	in	threat	actors’	competence	and

integration	ability,	especially	manifested	in	cloud	based	attacks,	with	27%	of

the	attacks	leveraging	new	vulnerabilities	(2020-2022).	Exploitation	of	older

vulnerabilities	continued	with	widely	used	2017	CVEs	including,	Apache	Struts2

6666

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   5

Remote	Code	Execution	(CVE-2017-5638)	which	is	used	by	botnets	and	the

PHPUnit	remote	code	execution	(CVE-2017-9841),	still	used	to	exploit	vulnerable

WordPress	plugins.	Information	collected	by	the	CPIRT	(Check	Point	Incident

Response	Team)	shows	the	proportion	of	newly	reported	vulnerabilities	in

successful	attacks	is	even	higher,	with	the	ProxyShell	vulnerabilities	alone

used	in	17%	of	investigated	cases.	This	demonstrates	that	while	4-5	year	old

vulnerabilities’	exploitation	attempts	are	widespread,	successful	attacks	more

often	rely	on	newly	discovered	flaws,	exploited	before	patched.	The	“long	tail”

phenomenon	of	vulnerability	exploitation	persists,	with	50%	of	attacks	in	the

wild	targeting	vulnerabilities	reported	before	2017.	These	are	mostly	less	effective

and	used	by	less	advanced	attackers.	These	findings	once	again	highlight	the

importance	of	timely	system	patching.

6767

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023VULNERABILITYC H A P T E R   6

INCIDENT
RESPONSE
PERSPECTIVE

6868

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   6

(A	specific	case	investigated	by	CPIRT	in	2022	is	highlighted	in	the	boxed	text.

Other	text	includes	observations	and	data	referring	to	all	cases	handled	in	2022.

Certain	details	have	been	modified	to	ensure	customer	confidentiality)

On a Monday morning in March 2022, the Check Point Incident Response

Team (CPIRT) received a call from a medium-sized European technology

company which had been the victim of a Quantum Locker ransomware

attack deployed early in the morning the day before. Robert, the

company’s CISO, was on the line. Thus began a typical workday in the life

of an IR analyst, which is often one of the worst days of the customers’

(professional) life.

Unlike	the	analysis	and	trends	discussed	in	previous	chapters	of	this	report,	which

are	based	on	Check	Point	products’	anonymized	data	collected	during	routine

preventative	protection,	this	chapter	offers	the	perspective	of	the	Check	Point

Incident	Response	Team	who	provide	attack	mitigation	services	in	response	to

various	types	of	active	breaches,	and	not	specific	to	Check	Point	customers.

Robert reported that most of their data center servers, including the

Domain Controllers and File Servers, had been encrypted and rendered

non-functional. With no backups, their entire operation came to a halt

and they were in need of assistance to investigate and mitigate this attack.

CPIRT’s mission was to look for ongoing vulnerabilities and malicious

activity, resume network functionality, and perform root cause analysis

to identify the initial attack vector and prevent future attacks.

6969

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   6

CPIRT	involvement	usually	follows	the	discovery	of	visible	malicious	activity,

such	as	encrypted	files	(ransomware),	detection	of	spoofed	or	forged	emails

(email	compromise),	or	the	presence	of	malware	files	or	unknown	processes	on

a	computer	system.	CPIRT’s	breakdown	of	the	initial	threat	indication	provides

a	different	perspective	of	the	threat	landscape	than	the	one	routinely	provided

by	our	product	data.

Ransomware

Email Compromise

Single server compromise

Phishing attempt

Compromised Credentials

Multiple host compromise

Single host compromise

Brute Force

Data Leak

Other

7%

3%

3%

3%

4%

5%

5%

10%

11%

49%

Figure	34:	Breakdown	of	CPIRT	cases	by	initial	threat	indication	in	2022

D A N I E L   W I L E Y
Head	of	Threat	Management
and	Chief	Security	Advisor,
Check	Point	Software
Technologies

  Analysis of the initial threat indications as seen by CPIRT in 2022

indicates that almost 50% of investigations involve ransomware

infections. The threat breakdown above is different from what

we see in our product data, which places multipurpose malware

and infostealers at the top of the threat list. However, CPIRT data

shows that the biggest risks that are visible from a large corporate

perspective—are full-blown ransomware attacks and full network

compromises. Product telemetry that records multipurpose

malware activity often just shows the initial incursion which if

prevented, blocks much larger damage.

7070

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   6

After the initial CPIRT forensic investigation, it became clear that the entry

point to the organization was the company’s exchange server. The server

had not been patched and was vulnerable to two very popular exploits used

by threat actors since 2021: the same group of vulnerabilities used

by Hafnium (CVE-2021-26855 and CVE-2021-26855, CVE-2021-26857 or

CVE-2021-26858) and the ProxyShell vulnerabilities (CVE-2021-34473,

CVE-2021-34523, CVE-2021-31207).

In	almost	half	of	CPIRT	cases,	the	initial	foothold	is	achieved	by	exploiting	a

vulnerable	server	with	an	unpatched	RCE	vulnerability	and	open	ports	to	the

internet.	In	fact,	ProxyShell	vulnerabilities	specifically	were	the	cause	of	one

in	every	six	incidents	CPIRT	investigated	in	2022,	despite	those	vulnerabilities

being	disclosed	and	patched	in	2021.

RCE vulnerability

Exposed RDP Service

Phishing / Malspam

47%

24%

21%

Brute force / Credential stuffing

Insider threat

8%

7%

Compromised Credentials

3%

Figure	35:	Breakdown	of	the	initial	entry	vector	in	CPIRT	cases	in	2022

0

10

20

30

40

50

7171

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   6

An	exposed	RDP	service	is	often	used	by	attackers	in	combination	with	an

RCE	vulnerability	or	password	attacks	such	as	brute	force	or	credential	stuffing

attack	to	gain	a	foothold	in	the	network.	Mail	servers	are	often	the	weak	link	in

a	network	and	are	a	common	initial	entry	point	for	attackers	and	more	easily

encrypted.	That	is	because,	due	to	performance	considerations,	endpoint

security	and	anti-ransomware	products	are	frequently	not	installed	on	servers.

Combined	with	the	high	number	of	vulnerabilities,	network	exposure	and	poor

patch	management,	in	many	organizations,	it’s	the	servers	and	not	the	peripheral

endpoints	that	are	the	weakest	point	and	are	therefore	exploited	in	many	attacks.

Further analysis revealed that the same vulnerable Exchange server had

been exploited twice, in incidents nine months apart. The first exploitation

of the server occurred in June 2021. Initially, “only” a cryptominer was

installed, utilizing multiple assets across the network.

This	emphasizes	the	need	to	treat	every	breach	as	seriously	as	a	full-blown

ransomware	attack.	As	in	this	case,	cryptominers	and	other	“minor”	malware

types	are	often	initial	indicators	of	possible	exploitation	that	could	lead	to

cyber	disasters	later	on.

Persistence in this attack was achieved by changing a registry key to

periodically connect and download an external resource. Initially, this

was a cryptominer installed on dozens of machines, but the resource

could easily have been changed to another payload. By the end of the

initial attack in mid-2021, the attackers leaked a list of network assets in

the network, and used Mimikatz to harvest credentials from the infected

network. Some of the harvested passwords were NTLM hashes which,

due to the practice of simple passwords, were easily reverse-engineered

to the plain text version.

7272

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   6

CPIRT	case	statistics	reveal	extensive	utilization	by	attackers	of	non-signature

tools.	The	top	tools	used	this	year	were	Cobalt	Strike	and	Mimikatz.	However,

for	the	first	time,	the	third	most	popular	tool	in	this	list,	AnyDesk,	is	a	legitimate

admin	tool.	As	threat	actors	have	started	using	more	legitimate	admin	tools	in

their	attacks,	the	use	of	customized	malware	built	by	the	same	threat	actors

has	declined,	and	we	are	seeing	an	increase	in	attacks	that	might	not	include

any	malware	at	all.	This	shift	in	the	tools	deployed	by	attackers	is	detailed	in	a

dedicated	chapter	in	this	report.

38%

33%

Cobalt Strike

Mimikatz

AnyDesk

XMRig

PsExec

RdpWrap

Teamviewer

Session Gropher

Metasploit

Kali Linux

Chrome Password Reader

21%

13%

9%

8%

7%

7%

6%

6%

6%

ADAudit

5%

0
Figure	36:	Tools	used	on	compromised	systems	in	2022	CPIRT	cases.

15

20

25

30

10

5

35

During the second breach in March 2022, the attackers used the data

retrieved nine months earlier. The asset list and credential dump

stolen during the first attack were now used to enable and direct the

ransomware deployment.

40

7373

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   6

Stolen	credentials	and	initial	access	to	corporate	networks	are	now	often	traded

between	threat	actors	or	sold	by	“initial	access	brokers”.	The	outsourcing	of	more

and	more	parts	of	the	attack	process,	and	the	further	fragmentation	of	the	threat

landscape,	complicates	attribution	efforts.	For	these	reasons,	in	many	of	CPIRT

cases	in	2022,	the	attack	attribution	was	not	to	a	very	well-known	or	common

threat	group.	We	have	also	seen	multiple	malware	families	used	in	a	single	attack,

for	example,	the	use	of	IceID	to	deliver	RansomEXX.

Lockbit

Black Basta

Conti

Dharma

Hive

Royal

Vice Society

Phobos

8%

7%

7%

5%

5%

5%

4%

4%

Figure	37:	Top	Ransomware	Families	seen	in	IR	cases	in	2022

0

1

2

3

4

5

6

7

8

While the first attack went relatively unnoticed, the second attack

resulted in the encryption of critical servers and ensuing serious damage.

But there is a happy ending: at the end of a long, nerve-wracking process,

thanks to CPIRT assistance, Robert was able to recover his company’s

data and resume normal business activity.

This	case	is	one	of	many	dozens	handled	by	CPIRT	in	2022	that	emphasizes	the

critical	importance	of	the	following:

•  Patch	immediately	when	an	update	is	available.

•

Impose	a	complex	password	policy	with	frequent	updates.

•  Use	endpoint	security	and	anti-ransomware	on	critical	systems.

As	Robert	can	attest,	these	actions	prevent	corporate	catastrophes.

7474

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

2023 INSIGHTS FOR
CISOS: DISRUPTION
AND DESTRUCTION

75

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

EXPECT INCREASED GLOBAL ATTACKS ON BUSINESSES,
STRICTER GOVERNMENT REGULATIONS AND MORE

CISOs	had	to	deal	with	a	lot	in	2022.	Global	attacks	increased	by	28%	in	the

third	quarter	of	2022	compared	to	same	period	in	2021,	and	the	average	weekly

attacks	per	organization	worldwide	reached	over	1,130.	As	we	look	ahead	to	2023,

that	trend	shows	no	signs	of	slowing	down	with	increases	in	ransomware	exploits

and	state-mobilized	hacktivism	driven	by	international	conflicts.	At	the	same	time,

organizations’	security	teams	and	CISOs	will	face	growing	pressure	as	the	global

cyber	workforce	gap	of	3.4	million	employees	widens	further,	and	governments

introduce	stricter	cyber	regulations	to	protect	citizens	against	breaches.

In	2022,	cyber	criminals	and	state-linked	threat	actors	continued	to	exploit

organizations’	hybrid	working	practices	as	businesses	shifted	to	decentralized

workforces,	and	the	increase	in	these	attacks	is	showing	no	signs	of	slowing	down

as	the	Russia—Ukraine	conflict	continues	to	have	a	profound	impact	globally.

Organizations	need	to	consolidate	and	automate	their	security	infrastructure	to

enable	them	to	better	monitor	and	manage	their	attack	surfaces	and	prevent	all

types	of	threat	with	less	complexity	and	less	demand	on	staff	resources.

2023 INSIGHTS: WHAT SHOULD CISOS BE LOOKING OUT
FOR, AND WHAT DOES IT MEAN FOR YOUR ORGANISATION?

Hikes in destructive malware and impactful hacking exploits

•  No	respite	from	ransomware:	this	was	the	leading	threat	to	organizations	in	the

first	half	of	2022,	and	the	ransomware	ecosystem	will	continue	to	evolve	and	grow

with	smaller,	more	agile	criminal	groups	forming	to	evade	law	enforcement.

•  Compromising	collaboration	tools:	while	phishing	attempts	against	business	and

personal	email	accounts	are	an	everyday	threat,	in	2023	criminals	will	widen	their

aim	to	target	business	collaboration	tools	such	as	Slack,	Teams,	OneDrive	and

Google	Drive	with	phishing	exploits.	These	are	a	rich	source	of	sensitive	data	given

most	organizations’	employees	often	continue	to	work	remotely.

7676

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

M AYA   H O R O W I T Z

Vice	President,	Research,
Check	Point	Software
Technologies

  Ransomware threat actors will continue to carry out

double extortions—encrypting network and sending

out the data—as big money comes from the data breach.

But we will also start to see more attacks where extortion

is only related to a data breach with no encryption taking

place, meaning that whilst the data is stolen, it can still

be used.

  When looking at compromised collaboration tools, there will

be more sophisticated attacks within multiple domains, known

as 5th Gen attacks, as the attack may start with email but move

to the network, firewall and more. This can all take months to

unfold. We are also seeing a rise in “static expressway” where

you can create static ‘allow lists’ so everything from Google is

allowed. This is common because it is hard to go through all

J E R E M Y   F U C H S

Researcher/Analyst,
Avanan	(a	Check	Point
Software	Company)

domains. For example, we can create something malicious on a popular site and know

that the receiving party will get it, with a good proportion clicking on it because it is a real

Paypal/Quickbook invoice, but with a virus attached. This could expand to other trusted

brands. With phishing, attackers use a fake email but in these cases, it seems legitimate,

so both the user and security system are at a loss.

  With the move to collaboration tools such as Slack and Teams over the pandemic period,

there will be an increase of attacks using these platforms. Most attacks so far have been

via email, but it could happen through any application or via services that use the same

logins. There is a perception that Teams is impervious to attack, which means users are

loose with sharing data and personal information, but this is not the case. Business Email

compromise has resulted in $2.4B in losses, but in reality, perhaps it should be renamed

business collaboration compromise.

7777

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

HACKTIVISM AND DEEPFAKES EVOLVE
WITH ATTACKS ON NATIONAL ORGANISATIONS
AND GOVERNMENT AGENCIES

•  State-mobilized hacktivism:	In	the	past	year,	hacktivism	has	evolved	from

social	groups	with	fluid	agendas	(such	as	Anonymous)	to	state	affiliated	groups

that	are	more	organized,	structured	and	sophisticated.	Such	groups	have

attacked	targets	in	the	US,	Germany,	Italy,	Norway,	Finland,	Poland	and	Japan

recently,	and	these	ideological	attacks	will	continue	to	grow	in	2023.

•  Weaponizing deepfakes:	In	October	2022,	a	deepfake	of	U.S.	President	Joe

Biden	singing	‘Baby	Shark’	instead	of	the	national	anthem	was	circulated

widely.	Was	this	a	joke,	or	an	attempt	to	influence	the	important	U.S.	mid-

term	elections?	Deepfakes	technology	will	be	increasingly	used	to	target	and

manipulate	opinions,	or	to	trick	employees	into	giving	up	access	credentials.

S E R G E Y   S H Y K E V I C H

Threat	Intelligence
Group	Manager,
Check	Point	Software
Technologies

  The lines between nation state actors, cybercriminals

and hacktivists will continue to blur. We will see more

hacktivists groups in support of nation-state narratives,

and nation-state actors learning techniques from veteran

cybercriminals. All of this makes it harder to attribute

attacks to any one group, so organizations will have to build

proper cyber protections against all types of threat actors.

7878

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

CLOUD-BASED AND IOT SOLUTIONS—
“VULNERABLE BY DESIGN” AFFECTS
BUSINESS ATTACK VECTORS

•  Cloud	gets	more	complicated:	It	is	clear	that	the	increased	use	of	cloud	based	and

IoT	solutions	has	presented	new	challenges	for	security	professionals.	With	less

control	and	visibility	over	where	data	is	stored	and	how	it	is	accessed,	it	can	be

difficult	to	ensure	that	access	to	sensitive	information	is	properly	secured.	This	is

especially	true	in	industries	like	healthcare	and	manufacturing,	where	IoT-based

sensors	and	devices	are	becoming	more	prevalent.	Additionally,	the	use	of	devices

such	as	cameras,	printers,	and	smart	TVs	for	video	conferencing	have	introduced

new	vulnerabilities.	Overall,	it	is	important	for	organizations	to	take	steps	to

ensure	the	security	of	their	cloud	based	and	IoT	systems	as	they	will	continue	to

be	central	and	trendier	pieces	of	any	IT	environment,	including	implementing	proper

access	controls	and	regularly	monitoring	for	potential	vulnerabilities.

M U H A M M A D   YA H YA   PAT E L

Global	Cybersecurity	Evangelist,
Check	Point	Software
Technologies

  Vulnerability exploitation is prevalent as attackers

are exceptionally quick at finding holes in well-known

products widely used by organizations. That is why it is

important to patch, patch, patch and keep up with updates

as a minimum, as these simple security measures are

usually overlooked.

7979

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

  I expect to see cloud transformation slow down due to

cost and complexity, with many companies considering

the action of bringing workloads back in-house, or at least

to private data centers. This could help in reducing the

overall threat surface.

D E R Y C K   M I T C H E L S O N

Field	CISO	EMEA,
Check	Point	Software
Technologies

GOVERNMENTS STEP UP MEASURES
TO PROTECT CITIZENS AND ORGANIZ ATIONS

•  New laws around data breaches:	the	breach	at	Australian	telco	Optus	has

driven	the	country’s	government	to	introduce	new	data	breach	regulations

to	protect	customers	against	subsequent	fraud,	with	new	laws	introduced

lifting	maximum	penalties	for	serious	or	repeated	breaches	from	the	current

A$2.22million	to	the	greater	of	A$50	million.	Similar	measures	by	the	British

Government	were	introduced	with	a	new	mandatory	reporting	obligation	on

MSPs	(Managed	Service	Providers)	to	disclose	cyber	incidents	or	be	fined	£17

million	for	non-compliance.	In	Australia,	the	government	is	also	considering

imposing	a	ban	on	ransoms	to	cybercriminals	leading	other	national

governments	to	possibly	follow	this	example	in	2023,	in	addition	to	existing

measures	such	as	GDPR.

•  New national cybercrime task forces:	More	governments	will	follow

Singapore’s	example	of	setting	up	inter-agency	task	forces	to	counter

ransomware	and	cybercrime,	bringing	businesses,	state	departments	and

law	enforcement	together	to	combat	the	growing	threat	to	commerce	and

consumers.	These	efforts	are	partially	a	result	of	questions	over	whether	the

cyber-insurance	sector	can	be	relied	upon	as	a	safety	net	for	cyber	incidents.

The	EU	has	also	strengthened	its	cybersecurity	and	resilience	with	its	new

directive,	NIS2.	NIS2	will	set	the	baseline	for	risk	management	and	reporting

across	all	sectors	including	energy,	health	and	critical	infrastructure.

8080

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

•  Mandating security and privacy by design: The	automotive	industry	has

already	moved	to	introduce	measures	to	protect	the	data	of	vehicle	owners.

This	example	will	be	followed	in	other	areas	of	consumer	goods	that	store

and	process	data,	holding	manufacturers	accountable	for	vulnerabilities	in

their	products.

A S H W I N   R A M

Cybersecurity	Evangelist,
Check	Point	Software
Technologies

  To prevent highly sensitive data from falling into the wrong

hands, CISOs must focus on understanding where the

organizations’ crown jewels are stored, including within 3rd

party systems. CISOs should take into consideration who

and what has access to their data, think APIs, and prioritize

Zero Trust implementation. This means enforcing the

principle of least privilege so that users and systems are

granted the bare minimum access to resources, to do

their job.

  Attacks on critical infrastructure will continue to increase

with threat actors becoming more shameless, though

they will be more difficult to conduct and require special

tools. Key sectors such as energy, telecommunications

and healthcare are targeted because they have so much

to lose, and are more likely to pay. Though attacks on the

education sector is random, attacks will continue because

of how the networks are built.

M AYA   H O R O W I T Z

Vice	President,	Research,
Check	Point	Software
Technologies

8181

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

ZERO-DAY VULNERABILITIES IN SUPPLY CHAIN
AND SOFT WARE CODE CAN BE EXPLOITED,
DESTROYING DAY-TO-DAY BUSINESS OPERATIONS

•  Zero-day vulnerabilities continue to plague businesses:	While	these

vulnerabilities	are	typically	discovered	and	patched	by	white	hat	hackers

before	they	are	made	public,	they	can	be	easily	exploited	once	they	are

found.	This	has	not	happened	yet,	as	most	threat	actors	are	more	interested

in	exploiting	vulnerabilities	that	are	easier	to	access.	The	proxy	logon

vulnerability,	which	was	discovered	last	year,	is	still	the	most	exploited

vulnerability	simply	because	it	is	effective.	However,	if	a	threat	actor	were

to	find	and	exploit	a	zero-day	vulnerability	before	it	was	patched,	the	damage

could	be	devastating	and	destructive.	Until	recently,	there	have	not	been

many	threat	actors	with	the	motivation	to	take	down	as	many	networks	as

possible,	but	the	current	climate	of	chaos	and	changing	motivations	may

lead	to	more	attempts	to	exploit	such	zero-day	vulnerabilities.	Patching	and

keeping	software	up	to	date	is	a	critical	mission.

P E T E   N I C O L E T T I

Field	CISO,	Americas,
Check	Point	Software
Technologies

  Supply Chain Attacks and breaches will continue

accelerating over the next year. Most companies do

not do a good enough job with managing the risk of the

components they are using and do not have visibility

into their SBOM nor a complete strategy, much less

an understanding of where the gaps are.

8282

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

CONSOLIDATION AS A SOLUTION
TO EVOLVING CORPORATE CYBER CHALLENGES

Cutting	complexity	to	reduce	risks:	Organizations	have	more	complex,	distributed

networks	and	cloud	deployments	than	ever	before	because	of	the	pandemic.	With

so	many	elements	to	consider,	security	teams	need	to	consolidate	their	IT	and

security	infrastructures	to	improve	their	defenses	and	reduce	their	workload

to	help	them	stay	ahead	of	threats.	The	statistics	speak	for	themselves,	where

over	two-thirds	of	CISOs	stated	that	working	with	fewer	vendors’	solutions	would

increase	their	company’s	security.	Security	teams	need	to	consolidate	their	IT	and

security	infrastructures	to	improve	their	defenses	and	reduce	their	workload	to

help	them	stay	ahead	of	threats.

J O N AT H A N  ‘J O N Y ’
F I S C H B E I N

CISO,
Check	Point	Software
Technologies

  The industry as a whole has made great strides in

decreasing the number of solutions to reduce the

complexity. Historically companies were using 15-17

solutions. Now CISOs are trying to cut down the number

of solutions to reduce complexity, leading the industry

to turn to consolidation as an answer. We suggest a

management dashboard that allows security professionals

to reduce the level of complexity when dealing with

security issues.

8383

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   7

D E R Y C K   M I T C H E L S O N

Field	CISO	EMEA,
Check	Point	Software
Technologies

  Consolidation will become a “real” priority in 2023,

especially as businesses look to remove cost,

heightened with the much talked about recession,

and more importantly, complexity from entire digital

and security stack.

  Organizations need to consider the new ‘work from home’

realm and how to address security challenges from the

hybrid and remote workforce as they may not have as strong

a security posture as the organizations they belong to. With

these workers leveraging the network, preventing such

attacks through these new vector needs to be considered.

Consolidating the entire cybersecurity posture would be a

step in the right direction.

A N T O I N E T T E   H O D E S

Solutions	Architect
&	Evangelist,	EMEA,
Check	Point	Software
Technologies

8484

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

PREVENTION
IS AT REACH

85

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

BECOMING A VICTIM IS NOT
PREDESTINED—PREVENTION
IS AT REACH

Zero-day attacks	are	unknown	cyber	risks	that	easily	circumvent	signature-

based	security	solutions	and	therefore	pose	an	exceptionally	dangerous	risk	to

businesses.	Ransomware	attacks	became	a	central	cyber	threat	and	oppose	a

disruptive	factor	globally	to	organizations,	corporates	and	even	governments.

Phishing	attacks	can	have	several	different	goals,	including	malware	delivery,

stealing	money,	and	credential	theft.	However,	most	phishing	scams	designed

to	steal	your	personal	information	can	be	detected	and	their	sometime	enormous

damage	can	be	prevented.	A Data breach	can	ravage	an	organization.	A	data

breach	often	results	in	expensive	security	audits,	fines	and	stakeholders	often

lose	trust	in	the	organization	as	a	result.	The	rapid	rise	of	high-profile	data

breaches	shows	it	is	critical	for	security	professionals	to	reexamine	their	current

security	strategies	and	implement	unified	security	across	network,	cloud,	and

mobile	environments	in	an	effort	to	prevent	the	next	breach.	Modern Cloud

Applications	brings	new	security	challenges	to	developers	which	needs	to	make

sure	thery	are	preventing	code	leaks	and	other	potential	breaches	that	can

be	disastrous.

In	this	section,	we	provide	security	professionals	practical	recommendations

that	can	mean	the	difference	between	joining	the	growing	statistics	of	cyber

victims	and	preventing	the	next	one.

8686

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

HOW TO PREVENT
RANSOMWARE ATTACKS

There	are	several	actions	that	a	company	can	take	to	minimize	their	exposure	to

and	the	potential	impacts	of	a	ransomware	attack.

1. Robust Data Backup

The	goal	of	ransomware	is	to	force	the	victim	to	pay	a	ransom	in	order	to	regain

access	to	their	encrypted	data.	However,	this	is	only	effective	if	the	target

actually	loses	access	to	their	data.	A	robust,	secure	data	backup	solution	is	an

effective	way	to	mitigate	the	impact	of	a	ransomware	attack.	If	systems	are

backed	up	regularly,	then	the	data	lost	to	a	ransomware	attack	should	be	minimal

or	non-existent.	However,	it	is	important	to	ensure	that	the	data	backup	solution

cannot	be	encrypted	as	well.	Data	should	be	stored	in	a	read-only	format	to

prevent	the	spread	of	ransomware	to	drives	containing	recovery	data.

2. Cyber Awareness Training

Phishing	emails	are	one	of	the	most	popular	ways	to	spread	ransom	malware.

By	tricking	a	user	into	clicking	on	a	link	or	opening	a	malicious	attachment,

cybercriminals	can	gain	access	to	the	employee’s	computer	and	begin	the	process

of	installing	and	executing	the	ransomware	program	on	it.	With	the	global	gap

in	cybersecurity	talent	impacting	organisations	around	the	world,	frequent

cybersecurity	awareness	training	is	crucial	to	protecting	the	organization	against

ransomware,	leveraging	their	own	staff	as	the	first	line	of	defence	in	ensuring	a

protected	environment.	This	training	should	instruct	employees	to	do	the	following:

•  Not	click	on	malicious	links

•  Never	open	unexpected	or	untrusted	attachments

•  Avoid	revealing	personal	or	sensitive	data	to	phishers

•  Verify	software	legitimacy	before	downloading	it

•  Never	plug	an	unknown	USB	into	their	computer

•  Use	a	VPN	when	connecting	via	untrusted	or	public	Wi-Fi

8787

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

3. Up-to-Date Patches

WannaCry,	one	of	the	most	famous	ransomware	variants	in	existence,	is	an

example	of	a	ransomware	worm.	Rather	than	relying	upon	phishing	emails	or

Remote	Desktop	Protocol	(RDP)	to	gain	access	to	target	systems,	WannaCry

spread	itself	by	exploiting	a	vulnerability	in	the	Windows	Server	Message	Block

(SMB)	protocol.	At	the	time	of	the	famous	WannaCry	attack	in	May	2017,	a	patch

existed	for	the	EternalBlue	vulnerability	used	by	WannaCry.	This	patch	was

available	a	month	before	the	attack	and	labeled	as	“critical”	due	to	its	high

potential	for	exploitation.	However,	many	organizations	and	individuals	did	not

apply	the	patch	in	time,	resulting	in	a	ransomware	outbreak	that	infected	200,000

computers	within	three	days.	Keeping	computers	up-to-date	and	applying	security

patches,	especially	those	labeled	as	critical,	can	help	to	limit	an	organization’s

vulnerability	to	ransomware	attacks	as	such	patches	are	usually	overlooked	or

delayed	too	long	to	offer	the	required	protection.

4. Strengthening User Authentication

Cybercriminals	commonly	use	the	Remote	Desktop	Protocol	(RDP)	and	similar

tools	to	gain	remote	access	to	an	organization’s	systems	using	guessed	or	stolen

login	credentials.	Once	inside,	the	attacker	can	drop	ransomware	on	the	machine

and	execute	it,	encrypting	the	files	stored	there.	This	potential	attack	vector

can	be	closed	through	the	use	of	strong	user	authentication.	Enforcing	a	strong

password	policy,	requiring	the	use	of	multi-factor	authentication,	and	educating

employees	about	phishing	attacks	designed	to	steal	login	credentials	are	all

critical	components	of	an	organization’s	cybersecurity	strategy.

5. Anti-Ransomware Solutions

While	the	previous	ransomware	prevention	steps	can	help	to	mitigate	an

organization’s	exposure	to	ransomware	threats,	they	do	not	provide	perfect

protection.	Some	ransomware	operators	use	well-researched	and	highly

targeted	spear	phishing	emails	as	their	attack	vector.	These	emails	may	trick

even	the	most	diligent	employee,	resulting	in	ransomware	gaining	access	to	an

organization’s	internal	systems.	Protecting	against	this	ransomware	that	“slips

through	the	cracks”	requires	a	specialized	security	solution.	To	achieve	its

objective,	ransomware	must	perform	certain	anomalous	actions,	such	as	opening

8888

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

and	encrypting	large	numbers	of	files.	Anti-ransomware	solutions	monitor

programs	running	on	a	computer	for	suspicious	behaviors	commonly	exhibited	by

ransomware,	and	if	these	behaviors	are	detected,	the	program	can	take	action	to

stop	encryption	before	further	damage	can	be	done.

6. Utilize better threat prevention

Most	ransomware	attacks	can	be	detected	and	resolved	before	it	is	too	late.

You	need	to	have	automated	threat	detection	and	prevention	in	place	in	your

organization	to	maximize	your	chances	of	protection.

•  Scan and monitor emails.	Emails	are	a	common	choice	of	cybercriminals

executing	phishing	schemes,	so	take	the	time	to	scan	and	monitor	emails

on	an	ongoing	basis,	and	consider	deploying	an	automated	email	security

solution	to	block	malicious	emails	from	ever	reaching	users.

•  Scan and monitor file activity.	It	is	also	a	good	idea	to	scan	and	monitor	file

activity.	You	should	be	notified	whenever	there	is	a	suspicious	file	in	play—

before	it	becomes	a	threat.

8989

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023ATTACKSC H A P T E R   8

HOW TO PREVENT
PHISHING ATTACKS

1. Always note the language in the email

Social	engineering	techniques	are	designed	to	take	advantage	of	human	nature.

This	includes	the	fact	that	people	are	more	likely	to	make	mistakes	when	they	are

in	a	hurry	and	are	inclined	to	follow	the	orders	of	people	in	positions	of	authority.

Phishing	attacks	commonly	use	these	techniques	to	convince	their	targets	to

ignore	their	potential	suspicions	about	an	email	and	click	on	a	link	or	open	an

attachment.	Some	common	phishing	techniques	include:

•  Fake Order/Delivery:	A	phishing	email	will	impersonate	a	trusted	brand

(Amazon,	FedEx,	etc.)	stating	that	you	have	made	an	order	or	have	an	incoming

delivery.	When	you	click	to	cancel	the	unauthorized	order	or	delivery,	the

website	(which	belongs	to	a	cybercriminal)	will	require	authentication,

enabling	the	attacker	to	steal	login	credentials.

•  Business Email Compromise (BEC):	BEC	scams	take	advantage	of	hierarchy

and	authority	within	a	company.	An	attacker	will	impersonate	the	CEO	or

other	high-level	executive	and	order	the	recipient	of	the	email	to	take	some

action,	such	as	sending	money	to	a	certain	bank	account	(that	belongs	to

the	scammer).

•  Fake Invoice: The	phisher	will	pretend	to	be	a	legitimate	vendor	requesting

payment	of	an	outstanding	invoice.	The	end	goal	of	this	scam	is	to	have

money	transferred	to	the	attacker’s	account	or	to	deliver	malware	via	a

malicious	document.

9090

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

2. Never share your credentials

Credential	theft	is	a	common	goal	of	cyberattacks.	Many	people	reuse	the	same

usernames	and	passwords	across	many	different	accounts,	so	stealing	the

credentials	for	a	single	account	is	likely	to	give	an	attacker	access	to	a	number

of	the	user’s	online	accounts.

As	a	result,	phishing	attacks	are	designed	to	steal	login	credentials	in	various

ways,	such	as:

•  Phishing Sites: Attackers	will	create	lookalike	sites	that	require	user

authentication	and	point	to	these	sites	in	their	phishing	emails.	Beware	of	links

that	don’t	go	where	you	expect	them	to.

•  Credential-Stealing Malware: Not	all	attacks	against	your	credentials	are

direct.	Some	phishing	emails	carry	malware,	such	as	keyloggers	or	trojans,

that	are	designed	to	eavesdrop	when	you	type	passwords	into	your	computer.

•  Support Scams:	Cybercriminals	may	pose	as	customer	support	specialists

from	Microsoft,	Apple,	and	similar	companies	and	ask	for	your	login

credentials	while	they	“help”	you	with	your	computer.

3. Always be suspicious of password reset emails

Password	reset	emails	are	designed	to	help	when	you	can’t	recall	the	password

for	your	account.	By	clicking	on	a	link,	you	can	reset	the	password	to	that	account

to	something	new.	Not	knowing	your	password	is,	of	course,	also	the	problem

that	cybercriminals	face	when	trying	to	gain	access	to	your	online	accounts.

By	sending	a	fake	password	reset	email	that	directs	you	to	a	lookalike	phishing

site,	they	can	convince	you	to	type	in	your	account	credentials	and	send	those	to

them.	If	you	receive	an	unsolicited	password	reset	email,	always	visit	the	website

directly	(don’t	click	on	embedded	links)	and	change	your	password	to	something

different	on	that	site	(and	any	other	sites	with	the	same	password).

9191

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

4. Educate Employees About Current Phishing Threats

Phishing	attacks	use	human	nature	to	trick	people	into	doing	something	that	the

attacker	wants.	Common	techniques	include	creating	a	sense	of	urgency	and

offering	the	recipient	of	the	email	something	that	they	desire,	which	increases	the

probability	that	the	target	will	take	action	without	properly	validating	the	email.

Phishers	will	often	take	advantage	of	current	events	or	impersonate	trusted

brands	in	their	emails	to	make	them	more	realistic.	By	offering	information,

goods,	or	opportunities	related	to	a	current	event	or	creating	a	situation	where

the	recipient	believes	that	something	has	gone	wrong	(like	a	fake	package	delivery

notification),	these	emails	increase	their	probability	of	getting	clicks.

Phishing	techniques	and	the	pretexts	used	by	cybercriminals	to	make	their	attacks

seem	realistic	change	regularly.	Employees	should	be	trained	on	current	phishing

trends	to	increase	the	probability	that	they	can	identify	and	properly	respond	to

phishing	attacks.

5. Deploy an Automated Anti-Phishing Solution

Despite	an	organization’s	best	efforts,	employee	cybersecurity	education	will	not

provide	perfect	protection	against	phishing	attacks.	These	attacks	are	growing

increasingly	sophisticated	and	can	even	trick	cybersecurity	experts	in	some	cases.

While	phishing	education	can	help	to	reduce	the	number	of	successful	phishing

attacks	against	the	organization,	some	emails	are	likely	to	sneak	through.

Minimizing	the	risk	of	phishing	attacks	to	the	organization	requires	AI-based

anti-phishing	software	capable	of	identifying	and	blocking	phishing	content	across	all

of	the	organization’s	communication	services	(email,	productivity	applications,	etc.)

and	platforms	(employee	workstations,	mobile	devices,	etc.).	This	comprehensive

coverage	is	necessary	since	phishing	content	can	come	over	any	medium,	and

employees	may	be	more	vulnerable	to	attacks	when	using	mobile	devices.

To learn more about protecting against phishing attacks and schedule a private

demo to see for yourself how Check Point’s email security solutions can help you

to identify and block phishing attacks against your organization.

9292

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

HOW TO PREVENT
ZERO DAY ATTACKS

Threat Prevention across your organization

•  Threat	intelligence	provides	the	information	required	to	effectively	detect	zero

day	attacks.	Protecting	against	them	requires	solutions	that	can	translate	this

intelligence	into	actions	that	prevent	the	attack	from	succeeding.

Check	Point	has	developed	over	sixty	threat	prevention	engines	that	leverage

ThreatCloud’s	threat	intelligence	for	zero	day	prevention.	Some	key	threat

prevention	capabilities	include:

•  CPU Level Inspection:	Cyberattackers	commonly	use	return	oriented

programming	(ROP)	to	bypass	defenses	built	into	CPUs.	CPU	level	inspection

identifies	attempts	to	overcome	executable	space	protection	and	code	signing,

blocking	the	attack	before	malicious	code	can	be	downloaded	and	executed.

•  Threat Emulation and Extraction:	Analysis	of	suspicious	content	within	a

sandboxed	environment	can	help	to	detect	malware	before	it	is	delivered	to	a

target	system.	This	enables	the	malware	to	be	blocked	or	malicious	content	to

be	excised	from	a	document	before	delivery.

•  Malware DNA Analysis:	Malware	authors	commonly	build	on,	borrow	from,

and	tweak	their	existing	code	to	develop	new	attack	campaigns.	This	means

that	novel	exploits	often	include	behavior	and	code	from	previous	campaigns,

which	can	be	used	to	detect	the	newest	variation	of	the	attack.

•  Anti-Bot and Anti-Exploit:	Modern	cyberattacks	often	rely	heavily	upon

compromised	machines	being	used	as	part	of	a	botnet.	After	identifying	a

compromised	machine,	an	organization	can	isolate	it	and	block	bot-related

traffic	to	stop	the	spread	of	the	malware.

•  Campaign Hunting:	Malware	is	reliant	upon	the	attacker’s	backend

infrastructure	for	command	and	control.	Using	threat	emulation	and

extraction,	Check	Point	can	identify	new	command	and	control	domains

used	by	malware	and	leverage	this	information	to	detect	other	instances

of	the	attack	campaign.

9393

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

•

ID Guard:	Account	takeover	attacks	have	become	increasingly	common	with

the	growing	use	of	Software	as	a	Service	(SaaS)	applications.	Behavioral

analysis	and	anomaly	detection	can	identify	and	block	attempted	attacks

even	if	the	attacker	has	the	correct	credentials.

Security Consolidation works

Many	organizations	are	reliant	upon	a	wide	array	of	standalone	and	disconnected

security	solutions.	While	these	solutions	may	be	effective	at	protecting	against

a	particular	threat,	they	decrease	the	effectiveness	of	an	organization’s	security

team	by	overwhelming	them	with	data	and	forcing	them	to	configure,	monitor,

and	manage	many	different	solutions.	As	a	result,	overworked	security	personnel

overlook	critical	alerts.

A	unified	security	platform	is	essential	to	preventing	zero-day	attacks.	A	single

solution	with	visibility	and	control	across	an	organization’s	entire	IT	ecosystem	has

the	context	and	insight	required	to	identify	a	distributed	cyberattack.	Additionally,	the

ability	to	perform	coordinated,	automated	responses	across	an	organization’s	entire

infrastructure	is	essential	to	preventing	fast-paced	zero-day	attack	campaigns.

Threat Intelligence must be kept up to date

Modern	cyberattacks	are	widespread	and	automated.	A	zero-day	attack	will	target

many	different	organizations,	taking	advantage	of	the	narrow	window	between

vulnerability	discovery	and	patch	release.

Protecting	against	this	type	of	large-scale	attack	requires	access	to	high-quality

threat	intelligence.	As	one	organization	experiences	an	attack,	the	data	that	it

collects	can	be	invaluable	for	other	organizations	attempting	to	detect	and	block

the	attack.	However,	the	speed	and	volume	of	modern	attack	campaigns	makes

manual	threat	intelligence	sharing	too	slow	to	be	effective.

Check	Point’s	ThreatCloud	is	the	world’s	largest	cyber	threat	intelligence	database.

ThreatCloud	leverages	artificial	intelligence	(AI)	to	distill	the	data	provided	to	it	into

valuable	insights	regarding	potential	attacks	and	unknown	vulnerabilities.	Analysis

of	over	86	billion	daily	transactions	from	more	than	100,000	Check	Point	customers

provides	the	visibility	required	to	identify	zero-day	attack	campaigns.

9494

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

DATA BREACHES
CAN BE PREVENTED

EDUCATE AND TRAIN

First	and	foremost,	educating	and
training	your	work	force	to	take
security	precautions	in	order	to
prevent	a	breach	from	occurring.

REDUCE DATA ACCESS

Reducing	the	ability	to	transfer
data	from	one	device	to	another
decreases	the	risk	of	data	getting
into	the	wrong	hands.

ENCRYPT PCS
AND DEVICES

Regulating	employee	computers
and	devices	in	which	they	have
access	to	company	data	can	be
significantly	reduced	by	using
only	encrypted	PCs	and	devices.

UPDATE PASSWORDS

Implementing	password	updates
and	two-step	authentication	also
mitigates	this	issue.	Additional
security	measures	such	as
limiting	website	access	from
work	devices,	frequent	password
changes,	updating	security
software,	and	monitoring	access
to	data	can	significantly	reduce
the	risk	of	a	data	breach.

1

2

3

4

5

6

7

8

SECURE PASSWORDS

Creating	a	secure	password
and	frequently	changing	it	to
prevent	access.

SCREEN THIRD
PARTY VENDORS

Screening	third	party	vendors	to
make	sure	that	they	have	proper
security	protocols	enabled	to
prevent	hackers	accessing	via
their	network.

CREATE AND
INTERNAL CLOUD

One	way	to	prevent	open	access
to	sensitive	data	from	being
accessed	is	by	creating	and
internal	cloud	where	only
those	who	need	access	to	it,
can	access	it.

UPDATE SOFTWARE

Frequent	security	software
updates	can	prevent	room	for
gaps	in	your	security.	Updating
in	cr ucial.

CHECK POINT SOFT WARE  |  SECURITY REPORT 2023
CHECK POINT SOFT WARE  |  SECURITY REPORT 2022

95
959595

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   8

Supply chain attacks	are	designed	to	exploit

PREVENT	COSTLY	MISTAKES

trust	relationships	between	an	organization

Mitigate	secret	leaks	caused	by	bad	credentials

and	external	parties.	These	relationships	could

hygiene	and	human	error	that	can	have

include	partnerships,	vendor	relationships,

devastating	results.

or	the	use	of	third-party	software.	Cyber

threat	actors	will	compromise	one	organization

and	then	move	up	the	supply	chain,	taking

INTEGRATE	WITH	YOUR	CLOUD
INFRASTRUCTURE

advantage	of	these	trusted	relationships	to	gain

CloudGuard	Spectral	integrates	with	all	leading

access	to	other	organizations’	environments.

CI	systems	with	built-in	support	for	Jenkins,

Such	attacks	became	more	frequent	and

grew	in	impact	in	recent	years,	therefore	it

is	essential	developers	make	sure	they	are

keeping	their	actions	safe,	double	checking

every	software	ingredient	in	use	and	especially

such	that	are	being	downloaded	from	different

repositories,	especially	ones	which	were

not	self-created.

Azure	and	others.

DETECT	AS	EARLY	AS	A	PRE-COMMIT

When	working	with	Git,	employ	our	pre-commit,

Husky	and	custom	hooks	to	automate	early

issue	detection.

INSTALL	YOUR	BUILD	SYSTEMS	PLUGIN

Scan	during	your	static	builds	with	native

plugins	for	JAMStack,	Webpack,	Gatsby,

Netlify	and	more.

Best Security From Code To Cloud,

Check	Point	CloudGuard	offers	unified

CloudGuard	Spectral’s	automated	tools

cloud	native	security	across	your	applications,

integrate	with	developers’	tools	to	detect

workloads,	and	network-giving	you	the

code	vulnerabilities	and	to	identify	secrets

confidence	to	automate	security,	prevent

and	misconfigurations	in	the	code	before

threats,	and	manage	posture-at	cloud

deployment,	preventing	unauthorized	use

speed	and	scale.	CloudGuard	Spectral is a

to	nefarious	ends.

developer-centric	code	security	platform	that

seamlessly	monitors,	classifies,	and	protects

codes,	assets,	and	infrastructure;	simply.

In	order	to	scale	this	process,	automation	is

a	necessity.

With	CloudGuard	Spectral,	organizations

can	prevent	exposing	API	keys,	tokens

and	credentials,	as	well	remediating

security	misconfigurations.

9696

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

MALWARE FAMILY
DESCRIPTIONS

97

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

AcidRain
AcidRain	is	a	destructive	malware	reported	on	24	February	2022	targeting	Viasat
modems.	Coinciding	with	the	Russian	ground	invasion	of	Ukraine,	AcidRain	attack
on	satellite	communication	systems	caused	widespread	disruption	to	communication
systems	providing	services	to	Ukraine.

AgentTesla
AgentTesla	is	an	advanced	RAT	which	functions	as	a	keylogger	and	password
stealer	and	has	been	active	since	2014.	AgentTesla	can	monitor	and	collect	the
victim's	keyboard	input	and	system	clipboard,	and	can	record	screenshots	and
exfiltrate	credentials	for	a	variety	of	software	installed	on	a	victim's	machine
(including	Google	Chrome,	Mozilla	Firefox	and	Microsoft	Outlook	email	client).
AgentTesla	is	sold	on	various	online	markets	and	hacking	forums.

AlienBot
AlienBot	is	a	banking	Trojan	for	Android,	sold	underground	as	Malware-as-a-Service
(MaaS).	It	supports	keylogging,	dynamic	overlays	for	credentials	theft,	as	well	as
SMS	harvesting	for	2FA	bypass.	Additional	remote	control	capabilities	are	provided
using	a	TeamViewer	module.

Anubis
Anubis	is	a	banking	Trojan	malware	designed	for	Android	mobile	phones.	Since	it
was	initially	detected,	it	has	gained	additional	functions	including	Remote	Access
Trojan	(RAT)	functionality,	keylogger,	audio	recording	capabilities	and	various
ransomware	features.	It	has	been	detected	on	hundreds	of	different	applications
available	in	the	Google	Store.

AZORult
AZORult	is	a	Trojan	that	gathers	and	exfiltrates	data	from	the	infected	system.
Once	the	malware	is	installed	on	a	system,	it	can	send	saved	passwords,	local	files,
crypto-wallet	data,	and	computer	profile	information	to	a	remote	C&C	server.	The
Gazorp	builder,	available	on	the	Dark	Web,	allows	anyone	to	host	an	Azorult	C&C
server	with	moderately	low	effort.

Azov
Azov	is	a	data	wiper	first	reported	in	November	2022	and	mostly	being	spread	via
SmokeLoader	malware.	The	ransom	note	left	on	victim	systems	blames	security
researchers	and	political	entities	for	the	fighting	in	Ukraine.

98

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

Bazar
Discovered	in	2020,	Bazar	Loader	and	Bazar	Backdoor	are	used	in	the	initial	stages	of
infection	by	the	WizardSpider	cybercrime	gang.	The	loader	is	responsible	for	fetching
the	next	stages,	and	the	backdoor	is	meant	for	persistence.	The	infections	are	usually
followed	by	a	full-scale	ransomware	deployment,	using	Conti	or	Ryuk.

BlackMatter
BlackMatter	is	a	ransomware	operated	in	a	RaaS	model.	The	malware	has	been
active	since	2021	with	victims	including	multiple	US	critical	infrastructure	entities.
BlackMatter	is	possibly	a	rebranding	of	the	DarkSide	ransomware.

Bumblebee
BumbleBee	is	a	new	loader	that	is	active	since	the	beginning	of	2022	and	is	used
to	deliver	other	payloads.	Bumblebee	payloads	vary	greatly	based	on	the	type	of
victim.	Infected	standalone	computers	will	likely	be	hit	with	banking	trojans	or
infostealers,	whereas	organizational	networks	can	expect	to	be	hit	with	more
advanced	post-exploitation	tools	such	as	CobaltStrike.

Conti
Conti	ransomware	emerged	in	2020	and	has	been	used	since	in	multiple	attacks
against	organizations	worldwide.	Conti	ransomware	is	delivered	as	the	final	stage
after	a	successful	intrusion	into	the	victims'	network.	Initial	intrusion	might	be
performed	using	spearphishing	campaigns,	stolen	or	weak	credentials	for	RDP,
or	phone-based	social	engineering	campaigns.

CryWiper
CryWiper	is	a	data-wiping	malware	disguised	as	ransomware	used	in	2022	to	attack
Russian	public	sector	entities.	Despite	payment	demands	displayed	in	a	ransom	note,
files	encrypted	by	CryWiper	cannot	be	restored.

Cl0p
Cl0p	is	a	ransomware	that	was	first	discovered	in	early	2019	and	mostly	targets
large	firms	and	corporations.	During	2020,	Cl0p	operators	began	exercising	a
double-extortion	strategy,	where	in	addition	to	encrypting	the	victim's	data,	the
attackers	also	threaten	to	publish	stolen	information	unless	ransom	demands
are	met.	In	2021	Cl0p	ransomware	was	used	in	numerous	attacks	where	the
initial	access	was	gained	by	utilizing	zero-day	vulnerabilities	in	the	Accellion
File	Transfer	Appliance.

99

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

Dracarys
Dracarys	is	an	Android	infostealer	discovered	in	2022,	used	by	the	Bitter	APT	group
to	steal	contacts,	messages,	call	logs,	screenshots,	and	more.

Dridex
Dridex	is	a	Banking	Trojan	turned	botnet,	that	targets	the	Windows	platform.	It	is
delivered	by	spam	campaigns	and	Exploit	Kits,	and	relies	on	WebInjects	to	intercept
and	redirect	banking	credentials	to	an	attacker-controlled	server.	Dridex	contacts	a
remote	server,	sends	information	about	the	infected	system,	and	can	also	download
and	execute	additional	modules	for	remote	control.

Dustman / ZeroCleare
Dustman	is	a	wiper,	first	detected	in	December	2019,	targeting	Middle	Eastern
entities.	Dustman	is	a	variant	of	the	ZeroCleare	wiper	and	has	code	similarities
with	Shamoon	malware.

Emotet
Emotet	is	an	advanced,	self-propagating	and	modular	Trojan.	Emotet	was	once	used
to	employ	as	a	banking	Trojan,	and	now	is	used	as	a	distributer	for	other	malware
or	malicious	campaigns.	It	uses	multiple	methods	for	maintaining	persistence
and	evasion	techniques	to	avoid	detection.	In	addition,	Emotet	can	also	be	spread
through	phishing	spam	emails	containing	malicious	attachments	or	links.

FormBook
FormBook	is	an	Infostealer	targeting	the	Windows	OS	and	was	first	detected	in	2016.
It	is	marketed	as	Malware	as	a	Service	(MaaS)	in	underground	hacking	forums	for	its
strong	evasion	techniques	and	relatively	low	price.	FormBook	harvests	credentials
from	various	web	browsers,	collects	screenshots,	monitors	and	logs	keystrokes,
and	can	download	and	execute	files	according	to	orders	from	its	C&C.

Glupteba
Known	since	2011,	Glupteba	is	a	Windows	backdoor	which	gradually	matured	into	a
botnet.	By	2019	it	included	a	C&C	address	update	mechanism	through	public	BitCoin
lists,	an	integral	browser	stealer	capability	and	a	router	exploiter.

GuLoader
GuLoader	is	a	downloader	first	reported	in	2019.	Since	then	it	was	used	to	distribute
various	malware	including	Lokibot,	NanoCore,	Formbook,	Azorult,	Remcos	and	more.

100

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

HermeticRansom
In	early	2022,	HermeticRansom	malware	was	utilized	to	distract	victims	while
HermeticWiper	attacks	were	launched	against	organizations	in	Ukraine.	These
attacks	rendered	devices	inoperable	and	as	such	were	destructive	in	nature	and
not	financially	motivated.

HermeticWiper
HermeticWiper	is	a	destructive	malware	first	reported	in	January	2022	and	used
to	target	organizations	in	Ukraine.	The	malware	is	one	of	a	series	of	wiping	malware
targeting	Ukrainian	organizations	during	the	Russian-Ukrainian	war	and	has
similarities	to	WhisperGate

Hiddad
Android	malware	which	repackages	legitimate	apps	and	then	releases	them	to	a
third-party	store.	Its	main	function	is	displaying	ads,	but	it	also	can	gain	access
to	key	security	details	built	into	the	OS.

Hive
Hive	ransomware	emerged	in	June	2021	and	uses	multiple	mechanisms	to	compromise
business	networks,	including	phishing	emails	with	malicious	attachments	to	gain
access	and	Remote	Desktop	Protocol	(RDP)	to	move	laterally	once	on	the	network.
Hive	involves	both	encryption	and	data	exfiltration	and	operate	a	“leak	site”	over	Tor.

Hydra
Hydra	in	an	Android	banking	Trojan	discovered	in	2019	distributed	through	infected
applications	on	Google	Play	Store.

IcedID
IcedID	is	a	banking	Trojan	which	first	emerged	in	September	2017.	It	spreads	by	mail
spam	campaigns	and	often	uses	other	malwares	like	Emotet	to	help	it	proliferate.
IcedID	uses	evasive	techniques	like	process	injection	and	steganography,	and	steals
user	financial	data	via	both	redirection	attacks	(installs	a	local	proxy	to	redirect
users	to	fake-cloned	sites)	and	web	injection	attacks.

Joker
Joker,	an	Android	mobile	malware	known	since	2017,	is	a	stealer	capable	of
accessing	SMS	messages,	contact	lists	and	device	information.	Joker	generates
income	mostly	through	unauthorized	subscriptions	to	paid	premium	services.

101

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

Kinsing
Discovered	in	2020,	Kinsing	is	a	Golang	cryptominer	with	a	rootkit	component.
Originally	designed	to	exploit	Linux	systems,	Kinsing	was	installed	on	compromised
servers	by	abusing	vulnerabilities	on	internet	facing	services.	Later	in	2021	a
Windows	variant	of	the	malware	was	developed	as	well,	allowing	the	attackers
to	increase	their	attack	surface.

LemonDuck
LemonDuck	is	a	cryptominer	first	discovered	in	2018,	which	targets	Windows
systems.	It	has	advanced	propagation	modules,	including	sending	malspam,	RDP
brute-forcing	and	mass-exploitation	via	known	vulnerabilities	such	as	BlueKeep.
Over	time	it	was	observed	to	harvest	emails	and	credentials,	as	well	as	to	deliver
other	malware	families,	like	Ramnit.

LockBit
LockBit	is	a	ransomware,	operating	in	a	RaaS	model,	first	reported	in	September	2019.
LockBit	targets	large	enterprises	and	government	entities	from	various	countries,
abstaining	from	Russian	or	other	Commonwealth	of	Independent	States	victims.

Lokibot
LokiBot	is	commodity	infostealer	for	Windows.	It	harvests	credentials	from	a	variety
of	applications,	web	browsers,	email	clients,	IT	administration	tools	such	as	PuTTY,
and	more.	LokiBot	has	been	sold	on	hacking	forums	and	believed	to	have	had	its
source	code	leaked,	thus	allowing	for	a	range	of	variants	to	appear.	It	was	first
identified	in	February	2016.

Mylobot
Mylobot	is	a	sophisticated	botnet	that	first	emerged	in	June	2018	and	is	equipped
with	complex	evasion	techniques	including	anti-VM,	anti-sandbox,	and	anti-debugging
techniques.	The	botnet	allows	an	attacker	to	take	complete	control	of	the	user's
system,	downloading	any	additional	payload	from	its	C&C.

Nanocore
NanoCore	is	a	Remote	Access	Trojan	that	targets	Windows	operating	system	users
and	was	first	observed	in	the	wild	in	2013.	All	versions	of	the	RAT	contain	basic
plugins	and	functionalities	such	as	screen	capture,	crypto	currency	mining,	remote
control	of	the	desktop	and	webcam	session	theft.

102

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

njRAT
njRAT,	aka	Bladabindi,	is	a	RAT	developed	by	the	M38dHhM	hacking	group.	First
reported	in	2012	it	has	been	used	primarily	against	targets	in	the	Middle	East.

Pegasus
Pegasus	is	a	highly	sophisticated	spyware	which	targets	Android	and	iOS	mobile
devices,	developed	by	the	Israeli	NSO	group.	The	malware	is	offered	for	sale,
mostly	to	government-related	organizations	and	corporates.	Pegasus	can	leverage
vulnerabilities	which	allow	it	to	silently	jailbreak	the	device	and	install	the	malware.

Phobos
Phobos	is	a	ransomware	first	detected	in	December	2018.	It	targets	windows
operating	systems	and	its	attack	vector	often	includes	exploiting	open	or	poorly
secured	RDP	ports.	Phobos	bears	great	resemblance	to	the	Dharma	ransomware,
both	in	its	ransom	note	and	with	much	of	its	code	and	is	thought	to	have	been
developed	and	used	by	the	same	group.

Phorpiex
Phorpiex	is	a	botnet	that	has	been	active	since	2010	and	at	its	peak	controlled	more
than	a	million	infected	hosts.	It	is	known	for	distributing	other	malware	families	via
spam	campaigns	as	well	as	fueling	large-scale	spam	and	sextortion	campaigns.

Ponystealer
PonyStealer	is	an	infostealer	used	for	stealing	passwords	from	a	large	number	of
applications	including	VPNs,	FTP	clients,	email	programs,	instant	messaging	tools,
and	web	browsers.

Qbot
Qbot	AKA	Qakbot	is	a	banking	Trojan	that	first	appeared	in	2008.	It	was	designed	to
steal	a	user’s	banking	credentials	and	keystrokes.	Often	distributed	via	spam	email,
Qbot	employs	several	anti-VM,	anti-debugging,	and	anti-sandbox	techniques	to
hinder	analysis	and	evade	detection.

Quantum
Quantum	is	a	rasnomware	operated	in	a	RaaS	model.	The	malware	has	been
discovered	in	2021	with	victims	including	multiple	healthcare	entities.	Investigators
link	Quantoum	to	ex-Conti	actors.

103

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

Raccoon
Raccoon	infostealer	was	first	observed	in	April	2019.	This	infostealer	targets
Windows	systems	and	is	sold	as	a	MaaS	(Malware-as-a-Service)	in	underground
forums.	It	is	a	simple	infostealer	capable	of	collecting	browser	cookies,	history,
login	credentials,	crypto	currency	wallets	and	credit	card	information.

Ramnit
Ramnit	is	a	modular	banking	Trojan	first	discovered	in	2010.	Ramnit	steals	web
session	information,	giving	its	operators	the	ability	to	steal	account	credentials	for
all	services	used	by	the	victim,	including	bank	accounts,	and	corporate	and	social
networks	accounts.	The	Trojan	uses	both	hardcoded	domains	as	well	as	domains
generated	by	a	DGA	(Domain	Generation	Algorithm)	to	contact	the	C&C	server	and
download	additional	modules.

RansomEXX
RansomEXX	is	a	ransomware	operated	in	a	RaaS	model	with	both	Windows	and
Linux	variants.	The	malware	has	been	active	since	2020	targeting	mostly	large
corporations.

Raspberry Robin
Raspberry	Robin	is	a	multipurpose	malware	initially	distributed	through	infected
USB	devices	with	worm	capabilities.

RedLine Stealer
RedLine	Stealer	is	a	trending	Infostealer	and	was	first	observed	in	March	2020.
Sold	as	a	MaaS	(Malware-as-a-Service),	and	often	distributed	via	malicious	email
attachments,	it	has	all	the	capabilities	of	modern	infostealer	-	web	browser	information
collection	(credit	card	details,	session	cookies	and	autocomplete	data),	harvesting	of
cryptocurrency	wallets,	ability	to	download	additional	payloads,	and	more.

Remcos
Remcos	is	a	RAT	that	first	appeared	in	the	wild	in	2016.	Remcos	distributes	itself
through	malicious	Microsoft	Office	documents,	which	are	attached	to	SPAM	emails,
and	is	designed	to	bypass	Microsoft	Windows	UAC	security	and	execute	malware
with	high-level	privileges.

104

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   9

REvil
REvil	(aka	Sodinokibi)	is	a	Ransomware-as-a-service	which	operates	an	“affiliates”
program	and	was	first	spotted	in	the	wild	in	2019.	REvil	encrypts	data	in	the	user’s
directory	and	deletes	shadow	copy	backups	to	make	data	recovery	more	difficult.	In
addition,	REvil	affiliates	use	various	tactics	to	spread	it,	including	through	spam	and
server	exploits,	as	well	as	hacking	into	managed	service	providers	(MSP)	backends,
and	through	malvertising	campaigns	that	redirect	to	the	RIG	Exploit	Kit.

Sharkbot
Sharkbot	steals	credentials	and	banking	information	on	Android	mobile	devices.
Sharkbot	lures	victims	to	enter	their	credentials	in	windows	that	mimic	benign
credential	input	forms.	When	the	user	enters	credentials	in	these	windows,
the	compromised	data	is	sent	to	a	malicious	server.	The	malware	implements
geofencing	feature	excluding	users	from	China,	India,	Romania,	Russia,	Ukraine
or	Belarus.	Sharkbot	has	several	anti-sandbox	evasion	techniques.

Snake Keylogger
Snake	Keylogger	is	a	modular	.NET	keylogger/infostealer.	Surfaced	around	late
2020,	it	grew	fast	in	popularity	among	cyber	criminals.Snake	is	capable	of	recording
keystrokes,	taking	screenshots,	harvesting	credentials	and	clipboard	content.
It	supports	exfiltration	of	the	stolen	data	by	both	HTTP	and	SMTP	protocols.

Somnia
Somnia	is	a	type	of	ransomware	that	was	deployed	by	the	FRwL	(From	Russia	with
Love)	group	against	Ukrainian	entities	in	November	2022.	Victims	of	Somnia	were
not	asked	to	pay	for	decryption.	The	goal	of	the	attackers	was	to	disrupt	systems,
rather	than	to	achieve	financial	gain.

Stuxnet
Stuxnet	is	a	malicious	computer	worm	discovered	in	2010	that	targeted	and
disrupted	the	Iranian	nuclear	program.	It	caused	physical	damage	to	equipment	by
manipulating	industrial	control	systems	and	was	the	first	publicly	known	example
of	nation-state	cyberattacks.

Triada
Triada	which	was	first	spotted	in	2016,	is	a	modular	backdoor	for	Android	which
grants	admin	privileges	to	download	another	malware.	Its	latest	version	is
distributed	via	adware	development	kits	in	WhatsApp	for	Android.

105

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023
C H A P T E R   9

Trickbot
Trickbot	is	a	modular	banking	Trojan,	attributed	to	the	WizardSpider	cybercrime
gang.	Mostly	delivered	via	spam	campaigns	or	other	malware	families	such	as
Emotet	and	BazarLoader.	Trickbot	sends	information	about	the	infected	system
and	can	also	download	and	execute	arbitrary	modules	from	a	large	array	of
available	modules,	including	a	VNC	module	for	remote	control	and	an	SMB	module
for	spreading	within	a	compromised	network.	Once	a	machine	is	infected,
the	threat	actors	behind	this	malware,	utilize	this	wide	array	of	modules	not	only
to	steal	banking	credentials	from	the	target	PC,	but	also	for	lateral	movement
and	reconnaissance	on	the	targeted	organization	itself,	prior	to	delivering	a
company-wide	targeted	ransomware	attack.

Vidar
Vidar	is	an	infostealer	that	targets	Windows	operating	systems.	First	detected	at	the
end	of	2018,	it	is	designed	to	steal	passwords,	credit	card	data	and	other	sensitive
information	from	various	web	browsers	and	digital	wallets.	Vidar	is	sold	on	various
online	forums	and	used	as	a	malware	dropper	to	download	GandCrab	ransomware
as	its	secondary	payload.

WannaMine
WannaMine	is	a	sophisticated	Monero	crypto-mining	worm	that	spreads	the
EternalBlue	exploit.	WannaMine	implements	a	spreading	mechanism	and
persistence	techniques	by	leveraging	the	Windows	Management	Instrumentation
(WMI)	permanent	event	subscriptions.

Whispergate
WhisperGate	is	a	destructive	malware	first	reported	in	January	2022	and	used	to
target	organizations	in	Ukraine.	The	malware	is	one	of	a	series	of	wiping	malware
targeting	Ukrainian	organizations	during	the	Russian-Ukrainian	war.	WhisperGate
damages	the	system's	MBR	while	displaying	a	false	ransom	message.

XMRig
XMRig	is	open-source	CPU	mining	software	used	to	mine	the	Monero
cryptocurrency.	Threat	actors	often	abuse	this	open-source	software	by	integrating
it	into	their	malware	to	conduct	illegal	mining	on	victims’	devices.

ZeroCleare
ZeroCleare	is	a	destructive	wiper	malware	that	was	first	identified	in	December
2020.	It	has	been	used	in	targeted	attacks	against	organizations	in	the	Middle	East,
and	is	notable	for	its	ability	to	evade	detection	and	wipe	both	hard	drives	and	backup
systems.	ZeroCleare	is	believed	to	be	the	work	of	a	state-sponsored	hacking	group.

106

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   1 0

CONCLUSION

107

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023C H A P T E R   1 0

As	we	navigate	our	way	through	a	new	year,	it	is	important	to	re-evaluate

the	cybersecurity	processes	you	have	in	place	to	ensure	they	stand	up

against	the	emerging	threats	outlined	by	our	experts	in	this	report.

There	will	undoubtedly	be	an	increase	in	ideological	motivated	attacks

in	response	to	geopolitical	conflicts	as	seen	between	Russian	and

Ukraine.	Known	threats	such	as	ransomware	will	continue	to	evolve,

and	new	vulnerabilities	will	be	exploited,	especially	given	the	huge	leaps

made	in	generative	AI,	making	it	easier	for	malicious	actors	to	craft

attacks,	leading	to	newer	strains	of	cyberattack	modes	and	breaches.

Governments	worldwide	will	tighten	up	regulations	around	cybercrime

to	protect	their	citizens,	and	organizations	will	have	to	consolidate

and	automate	their	IT	and	security	infrastructure	to	plug	the	cyber	skills

gap,	which	is	set	to	grow	even	wider	this	year.

While	we	are	seeing	a	rise	in	cyberattacks	overall,	given	the	growth

of	5th	Generation	cyberattacks	in	the	last	year,	the	maturing	of	cyber

defense	solutions	today	means	that	organisations	and	the	wider	society

can	adopt	prevention-first	solutions	to	block	threats	from	ever	reaching

us.	Businesses	and	governments	are	addressing	today’s	sophisticated

threats	and	increasing	investment	in	their	security	strategies,	which

bodes	well	as	the	world	faces	even	greater	challenges,	with	the

upcoming	recession	and	expected	evolution	of	new	malicious	software

and	nefarious	practices.	Only	time	will	tell	how	this	upward	of	attacks

will	continue	in	2023.

CHECK POINT SOFT WARE  |  SECURITY REPORT 2023
CHECK POINT SOFT WARE  |  SECURITY REPORT 2022

108
108108

CHECK POINT SOFTWARE  |  SECURITY REPORT 2023CONTACT	US

WORLDWIDE HEADQUARTERS

5 Ha’Solelim Street, Tel Aviv 67897, Israel
Tel: 972-3-753-4555 | Fax: 972-3-624-1100
Email: info@checkpoint.com

U.S. HEADQUARTERS

959 Skyway Road, Suite 300, San Carlos, CA 94070
Tel: 800-429-4391 | 650-628-2000 | Fax: 650-654-4233

UNDER ATTACK?

Contact our Incident Response Team:
emergency-response@checkpoint.com

CHECK POINT RESEARCH PODCAST
Tune in to cp<radio> to get CPR’s latest research,
plus behind the scenes and other exclusive content.
Visit us at https://research.checkpoint.com/category/cpradio/

W W W . C H E C K P O I N T . C O M

© 1994-2023 Check Point Software Technologies Ltd. All Rights Reserved.