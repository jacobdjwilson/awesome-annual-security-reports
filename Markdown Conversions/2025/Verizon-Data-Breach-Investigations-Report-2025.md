# 2025 Data Breach Investigations Report

## Table of Contents
- [Introduction](#introduction)
- [How to use this report](#how-to-use-this-report)
- [Summary of findings](#summary-of-findings)
- [Results and analysis](#results-and-analysis)
  - [The big picture](#the-big-picture)
  - [VERIS Actors](#veris-actors)

---

# Introduction

Hello, and welcome to Verizon’s 2025 Data Breach Investigations Report (DBIR)! We are thrilled to have you with us for this, the 18th annual installment of the DBIR. Whether you are a longtime reader or this is your first rodeo,[^1] you will find within the pages of this report a comprehensive examination of the recent state of cybercrime, along with insights on what threats your organization may likely face, who is behind them and what you can do to help protect yourself.

This year, the Verizon DBIR team analyzed 22,052 real-world security incidents, of which 12,195 were confirmed data breaches that occurred inside organizations of all sizes and types. This represents the highest number of breaches ever analyzed in a single report. These incidents and breaches were provided from the case files of the Verizon Threat Research Advisory Center (VTRAC) team, along with the generous support of our global contributors, and from publicly disclosed security incidents. Together, these attacks represent victims from 139 countries around the world.

Although the threat landscape can vary somewhat due to organizational size, mission and location, there are always certain overarching themes that seem to predominate our dataset regardless of any of these variables. This year is no exception. Possibly the most obvious and noteworthy among them is the role that third-party relationships play in how and why breaches occur.

While, to some extent, software vendors have long played a part in unintentionally increasing the attack surface for those who use their products and services, over the last two to three years, it has moved from the occasional (and typically minor to moderate) mishap to a much more widespread and insidious problem that can (and sometimes does) have a devastating effect on enterprises. In fact, this is the case to such an extent that it made the cover visualization for this year’s report,[^2] and you will find the subject woven throughout this document.

From this foundation, we explore in our “Results and analysis” section the growth of the well-known edge device vulnerability exploits that no cybersecurity professional could have failed to notice this year, along with the adverse effects those vulnerabilities can have on an organization’s security posture and how they can further complicate remediation efforts.

In our “Basic Web Application Attacks”[^3] section, we examine in some detail the issue of stolen credentials and application and programming interface (API) keys and what that ecosystem looks like. In addition, in our stolen credentials sidebar, we take a look at the infostealer malware problem and how it relates to bring your own device (BYOD) practices. Finally, we would be remiss if we did not mention the ever-present problem of ransomware that we discuss in our “System Intrusion” section,[^4] which grew yet again as a percentage of breaches, while at the same time declined with regard to median amount of ransom paid.

Return readers may notice some slight changes to the overall structure of this year’s report. Notably, we revisited the small- and medium-sized business section (and how smaller businesses compare to larger organizations), and the Public Administration industry snapshot was promoted to its own section (now “Public Sector” under “Focused analysis”).

And finally, as always, we wish to extend our warmest gratitude to our contributing organizations,[^5] without whose collaboration, civic mindedness and expertise this report could not be written, and to the outrageously talented VTRAC team. A very sincere thanks, as well, to our leader, Chris Novak, Vice President of Global Cybersecurity Solutions, for his continued support, insight and guidance.

Sincerely,
The Verizon DBIR team
C. David Hylender, Philippe Langlois, Alex Pinto, Suzanne Widup

[^1]: Not that we expect you to admit it if it is. No one has ever been heard to remark, “Hey, please be aware, this is my first rodeo.”
[^2]: See the inside front cover for more information about the cover graphic.
[^3]: Please feel free to come up with a catchier title and let us know what it is.
[^4]: Who are we kidding? It is so ubiquitous that it rears its ugly head in practically every page of this report.
[^5]: A complete list of all contributing organizations can be found at the end of the report.

---

# How to use this report

The Data Breach Investigations Report (DBIR) focuses on the analysis of anonymized cybersecurity incident data that Verizon collects every year from almost a hundred data contributors. Those data points are normalized using the Vocabulary for Event Recording and Incident Sharing (VERIS) framework, which provides us a great foundation for statistical analysis of this type of data.

## VERIS framework resources
The terms “threat actions,” “threat actors” and “varieties” will be referenced often. These are part of the VERIS, a framework designed to allow for the consistent, unequivocal collection of security incident details.

- **Threat actor**: Who is behind the event?
- **Threat action**: What tactics (actions) were used to affect an asset? VERIS uses seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error and Environmental.
- **Variety**: More specific enumerations of higher-level categories.

## Incident vs. breach
- **Incident**: A security event that compromises the integrity, confidentiality or availability of an information asset.
- **Breach**: An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party.

## Being confident in our data
Starting in 2019 with slanted bar charts, the DBIR has tried to make the point that the only certain thing about information security is that nothing is certain. This year, you’ll continue to see the team representing uncertainty throughout the report figures.

- ![Example slanted bar chart]
- ![Example spaghetti chart]
- ![Example dot plot]
- ![Example pictogram plot]

---

# Summary of findings

- The exploitation of vulnerabilities has seen another year of growth as an initial access vector for breaches, reaching 20%.
- The percentage of edge devices and VPNs as a target on our exploitation of vulnerabilities action was 22%, and it grew almost eight-fold from the 3% found in last year’s report.
- The presence of Ransomware, with or without encryption, in our dataset also saw significant growth—a 37% increase from last year’s report. It was present in 44% of all the breaches we reviewed, up from 32%.
- The median amount paid to ransomware groups has decreased to $115,000 (from $150,000 last year).
- The percentages of breaches where a third party was involved doubled, going from 15% to 30%.
- Espionage-motivated breaches are now at 17%.

![Known initial access vectors in non-Error, non-Misuse breaches]
![Ransomware action over time in breaches]
![Select key enumerations in breaches]
![Percentage of non-managed devices with corporate logins in infostealer logs]
![Percentage breakdown of GenAI service access account types]

---

# Results and analysis

## The big picture
This year, we pushed even more boundaries on the data collection front and are pleased to announce that, for this edition of the report, we have analyzed more than 12,000 breaches, adding even more detail to the data corpus around ransomware and Espionage-motivated breaches.

![Percentage of third-party involvement in breaches]
![Top patterns in breaches with third-party involvement]

### Credential giveaway, no purchase required
Although the old-fashioned usernames and passwords are what we think of when we talk about credentials, there are actually a variety of additional types of credentials that can also provide attackers with access to our environments.

![Top categories of exposed secrets in public git repos]
![Distribution of days to remediate leaked secrets in git repositories]

## VERIS Actors
In VERIS parlance, (threat) actors are how we describe the “who” of an incident. External actors are still at it and causing more trouble than your Internal actors or your Partners combined.

![Threat actors in breaches]
![Patterns in External actor breaches]
![Patterns in Internal actor breaches]
![Threat actor motives in breaches]
![Motive for state-sponsored actors in incidents]
![Percentage of AI-assisted malicious emails over time]

---

nterns usage. One of our email security data
and other staff. Insiders are threats, from partners allowed us to reproduce some
trusted and privileged (some more findings from one of their research
than others). the novel … articles,44 in which they have discovered
an increase of malicious AI-written
Partner: Partners include any
emails over the last couple of years.
third party sharing a business
relationship with the organization. In spite of all the uncertainty The vertical line represents when LLM-
This includes suppliers, vendors, surrounding how GenAI tools would based chat tools started becoming more
hosting providers and outsourced transform the threat landscape, one popular, and the findings before that
IT support. Some level of trust thing we felt sure about was that if there (and most likely after that for some time)
and privilege is usually implied was evidence of GenAI usage by threat can be attributed to machine translation
between business partners. actors, the platforms themselves would and grammar correction services.
Note that an attacker could use be among the first to let us know. Not Figure 23 provides us with the coveted
a partner as a vector, but that only would they have the best visibility DBIR AI headline: percentage of AI-
does not make the partner the by leveraging known indicators of assisted malicious emails doubled
Actor in this case. The partner threat actor infrastructure accessing (from 5-ish% to 10-ish%) over the
has to initiate the incident to be their systems, but they would also not past two years.
considered the responsible party. waste an opportunity to discuss another It turns out the state-sponsored actors
potential use case for their tools.
are just like legitimate organizations in
And so they did. Both OpenAI41 (twice42) their GenAI implementation life cycles.
and Google43 shared research in Attempts are being made, maybe some
late 2024 and early 2025 regarding improvements are being found, but no
identifying usage from state-sponsored one is revolutionizing anything yet. You
actors in augmenting influence are not convincing AI cheerleaders it’s
operations, phishing attempts and not happening, nor are you convincing
coding activities. There is evidence skeptics there is in fact something
of attempts to abuse the platforms revolutionary there.
themselves, but they don’t report
anything successful.
40. https://verisframework.org/actors.html
41. https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_
October-2024.pdf
42. https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-
2025-update.pdf
43. https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai
44. https://www.mimecast.com/blog/how-chatgpt-upended-email
2025 DBIR Results and analysis 24

… to the banal And those are not purely theoretical At the time of this writing, some of
risks. No matter how you may feel those functions come enabled by
about the Chinese association with the default and must be opted out by the
However, one very real way in which recently released DeepSeek model, user or a centralized mobile device
GenAI is making our environments it was found to be insecurely leaking management system.
less secure is the revitalized hoarding sensitive data, including chat history,46
We have never been fans of BYOD
by model trainers and leaking of data in late January 2025. Imagine the
solutions, given all the additional risks
by their users. Principles of data additional insult to injury of having your
that they can pose as the employees
minimization and least privilege, that not company’s confidential data leaked
leverage the same environment for
very long ago seemed to be so trendy alongside “Which number is larger, 9.9
personal affairs. This new technology
and in vogue, are now left to gather or 9.11?” and “How many r’s are
certainly adds another notch to the cons
dust as companies go back to hoard in strawberry?”
side in the corporate whiteboard. We
information for some hopeful future
Another emerging risk comes from will discuss later in this report how often
use case.
GenAI being integrated into the personal and corporate credentials are
Analyzing data from corporate browser operating system of some of the newest leaked in unison, suggesting that they
monitoring systems, we found that 14% mobile devices. With so many of its core may have come from personal devices
of employees were routinely accessing functions (such as voice assistants, that had access to corporate data.47
GenAI systems on their corporate messaging apps and cameras)
In summary, for this technology, some
devices. Figure 24 illustrates an even leveraging those data-hungry models,
use cases might be novel, but the
more concerning picture: A large the number of avenues for sensitive
abuse cases are often very standard
number of those were either using a information to be exposed can become
and known. Just another day in risk
non-corporate email as the identifier too large to count.
management and mitigation.
of their account (72%) or using their
corporate email without an integrated
authentication system such as Security
Assertion Markup Language (SAML) in
place (17%), suggesting that accessing
those systems may not be a part of the
sanctioned applications allowed in their
corporate environment.
Yes, employees have accessed
unsanctioned websites ever since the
internet was made available in work
environments,45 but some of the most
common use cases of GenAI tools—
such as summarization or coding
assistance—often invite the user to
upload confidential documents and
codebases to achieve them.
Figure 24. Percentage breakdown of GenAI service access account types
(each glyph is 0.5%)
45. Those among us who didn’t waste time on AngelFire WebRings, feel free to throw the first
14-inch CRT monitor.
46. https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak
47. We don’t know about you, but we are not going through weird social media AI-generated images on our
corporate devices.
2025 DBIR Results and analysis 25

VERIS Actions
Actions in VERIS describe the “how”
of our incidents, in an effort to try
to understand better what kinds of
techniques the threat actors are
using. This is not unlike the work that
organizations do with the ATT&CK
framework, but it covers a much broader
and sometimes non-technological48
scope. This knowledge should help
inform organizations on how they can
protect themselves and can be a pretty
good input for your risk modeling. Ask
your favorite actuary about it!
But we have a lot to talk about, so
we should go straight into Action.49
As you review Figure 25, describing
the top Actions in breaches, you will
notice that big “Other” at the top. This
is a side effect of the really long tail
of Hacking and Malware actions we
registered in our effort to memorialize
our ransomware and Espionage-
motivated breaches to a good level
of technical detail.50
Sure, you could call those sophisticated
attacks due to the large number of
Actions, but more Actions do not
necessarily mean more problems;
instead, they may actually provide more
opportunities of detection by defenders.
Readers will notice how all of those
different Action varieties combine
well together for the gathering and
exfiltration of information. The Export
data variety is right there in the chart,
after all.
We should also point out the growth
of Exploit vuln (18%), which can now
be found in a larger percentage of
breaches than Phishing (14%). Figure 25. Top Action varieties in Figure 26. Top Action varieties in
breaches (n=10,747) incidents (n=20,271)
48. All DBIR authors are issued a big gaudy brooch saying “Ask me about Environmental actions!” upon
completing their onboarding.
49. Brief glimpse into the DBIR writing process: Us authors are often encouraged to re-read sections from
previous years not only for inspiration but also to avoid making the same jokes over and over again each
year. We were shocked to find this pun has not been done before, which speaks to either its brilliance or
just how unimaginative it is.
50. Greatly facilitated by the VERIS x ATT&CK mapping we collaborate with MITRE on. Check it out on
https://center-for-threat-informed-defense.github.io/mappings-explorer/external/veris.
2025 DBIR Results and analysis 26

We have already explored this new
development this year in the initial access
vector discussion at the beginning of Too much of a
the “Results and analysis” section and
(bad) thing
will revisit it again later in this section as
we explore vulnerability management
data. Regardless, one of the takeaways As we are duty-bound to
here is that those are two very important discuss bias52 here in the
Action varieties to keep track of, as they report, it’s worth mentioning
are often in our top initial access vectors. that we, as a community, may
Whomever wins, we lose.51 have gotten a little too good
in documenting and capturing
Now let’s turn our attention to the
Ransomware breaches. The
big (and encrypted) elephant in the
Actor disclosure53 being the
room, Ransomware. Not only did it
main discovery variety for those
overtake our most common action
breaches can make it very
in breaches, the reigning champion
easy to track and aggregate
Use of stolen credentials, but it also
a large number of victims that
approached DoS as a percentage in all
have not negotiated or paid
incidents recorded, which would have
their ransoms. Meanwhile, our
been unthinkable last year. Figure 26
data contributors, ranging from
illustrates this feat.
ransomware-focused incident
Ransomware is present in 44% of all response firms to cyber
the breaches we reviewed, up from 32% insurance companies, help us
last year. On the incident side, it’s also fill in the gap for ones that might
up and is present in 31% of them, an have made the decision to pay.
increase from a less-impressive 14%
All that to say, we actively chose
last year.
to sample the ransomware-
Those large Ransomware numbers related data we had access to
include both the “traditional encrypting” and not ingest it in its totality
Ransomware kind and the “pure- Figure 27. Top industries victim to to align with other sampling
extortion, non-encrypting” kind, which Ransomware breaches (n=4,178) methods we have been fine-
we classified as Extortion in the 2024 tuning over the years. To let
DBIR. We have reverted those Extortion it completely overwhelm our
Regardless how we classify it,
entries back to Ransomware in our dataset would transform this
it’s definitely not a controversial
dataset for simplicity and clarity’s sake, document into the Verizon RIR54
statement to say that Ransomware
as those types of breaches continue to (Ransomware Investigations
is a scourge of our lives as stewards
be referred to by the majority of folks by Report), which doesn’t have
of our organization’s security. And as
the original name. as nice of a ring to it.
Figure 27 demonstrates, it does not
discriminate on the industry verticals Of course, this is not to say that
it affects. We’ll be talking (much) more we as a community should not
about Ransomware and its impact in the continue to do such a stellar
“System Intrusion” pattern section. job documenting (and shutting
down) those threat actors,
but here is hoping that with
more availability of additional
incident reporting shared due
to regulatory pressure all over
the world, the DBIR can afford
the luxury of turning down data
of other types of incidents, too.
51. Cinema buffs will recognize this expression as a fair-use variation of the poster tagline for the early
21st-century classic “Alien vs. Predator,” a timeless tale of courage in the face of adversity set in an
abandoned arctic station. It encapsulates the metaphor appropriately.
52. It’s rule number two in the Statistics Scout Book!
53. The VERIS Discovery Method most prevalent in Ransomware, in which the threat actor notifies the
victim (and everyone else at the same time) of the breach by way of dropping the ransom note.
54. For the non-Portuguese speakers out there, “rir” means “to laugh,” which is also infinitely amusing to
your Brazilian-born author over here.
2025 DBIR Results and analysis 27

Moving on, there is not a lot to write
home about55 when we review the top Action categories56
Action vectors in breaches in Figure 28.
Web application and Email have long
Hacking: attempts to
been mainstays as the top two vectors,
intentionally access or harm
but this year it is easy to notice the other
information assets without (or
vectors having a stronger showing. This
exceeding) authorization by
is also one of the benefits of extensive
circumventing or thwarting
mapping of the more technical details
logical security mechanisms.
of breaches we analyzed. We dive into
the growth of VPN and Other network Malware: any malicious software,
service as it applies to Exploit vuln in script or code run on a device that
the initial access vectors section in alters its state or function without
“Results and analysis.” Go check it the owner’s informed consent.
out if you haven’t.
Error: anything done (or
left undone) incorrectly
or inadvertently.
Social: employ deception,
manipulation, intimidation, etc.,
to exploit the human element,
or users, of information assets.
Misuse: use of entrusted
organizational resources or
privileges for any purpose
or manner contrary to that
which was intended.
Physical: deliberate threats
that involve proximity,
possession or force.
Environmental: not only
includes natural events such
as earthquakes and floods but
also hazards associated with
the immediate environment
or infrastructure in which
Figure 28. Top Action vectors in
assets are located.
breaches (n=7,372)
55. Not sure my mother would enjoy the subject even if it had any remarkable results.
56. https://verisframework.org/actions.html
2025 DBIR Results and analysis 28

We’re living Predicting this result,59 we engaged Those were all tracked by our
with all our vulnerability management vulnerability management data
on the edge partners to gather as much data as contributors and are used as a
possible to understand how defenders representative subset for comparison
(of the absurd). are dealing with all of this. The data with the full CISA KEV catalog.
collected covers 10,000 companies We reproduce this list in Table 1 and
that had to remediate vulnerabilities will ignore any criticism around “you
“One must imagine Sisyphus happy,” listed in the Cybersecurity Infrastructure should have picked such and such CVE.”
wrote Albert Camus when he introduced and Security Agency (CISA) Known
First, the good news. The messaging
the philosophy of the absurd57 in his Exploited Vulnerability (KEV) catalog.60
around the criticality of these edge
seminal work, The Myth of Sisyphus.
vulnerabilities is clearly getting through
When faced with his eternal task of
to defenders. There is a clear indication
pushing his rock onto the top of a
Vendor A CVE-2023-6548 of organizations fully remediating those
mountain, only to have it roll down again
CVE-2023-6549 edge vulnerabilities more often (54%)
upon reaching the top at the end of
over this past year when compared
the day, Camus interrogates Sisyphus’ Vendor B CVE-2023-48788
with all vulnerabilities listed on the CISA
interiority as he has those peaceful CVE-2024-21762
KEV list (38%) or even all vulnerabilities
moments walking down the mountain CVE-2024-23113
identified in their scans (a measly 9%).
path, his duty performed, to meet his CVE-2024-47575
Organizations must prioritize their
fate again at the base of the mountain.
resources, and they seem to be doing
Vendor C CVE-2023-46805
It is only when Sisyphus acknowledges CVE-2024-21887 so correctly according to Figure 29.
the futility of his task and the certainty CVE-2024-21893 The “Partially remediated” field means
of his fate that he can strip all meaning
exactly what it sounds like and is curious
from it, acknowledge its clear absurdity Vendor D CVE-2024-3400
in the context of edge vulnerabilities.
and, for a few precious moments,
One can understand choosing to (or
be content. Vendor E CVE-2024-40766
more frequently having to) only prioritize
But I digress. Where were we again? Vendor F CVE-2024-20359 assets that are not the most exposed to
Ah, vulnerability management. Right. threats. That logic should not hold for
Vendor G CVE-2023-36844 edge devices, as all of them would need
We are not pleased to report that
CVE-2023-36845 this exposure to the big bad internet by
the challenges involving vulnerability
CVE-2023-36846 design. Ever the optimists, we choose
management continued throughout
CVE-2023-36847 to believe the partially remediated folks
the last year, with a very concerning
CVE-2023-36851 have taken proper steps to mitigate the
complicating factor. A good number
exposure of the devices still showing
of vulnerabilities that had significant
Table 1. Edge device vulnerabilities as vulnerable.
impact—anecdotally58 from presence in
sampled, grouped by vendor
ransomware and Espionage-motivated
campaigns as well as overall media
coverage—were targeting devices To drill down into the edge device
organizations deploy on the edge of vulnerability issue, we have sampled
their internet perimeter. That means they a group of 17 vulnerabilities added to
are right there, in the open, for any other the CISA KEV catalog after Nov 1, 2023
device on the internet to target. (our incident data collection start date
for the 2025 DBIR), across seven
different vendors.
57. The struggle between the need of humans to attribute meaning to life and the indifference of the
universe in response. Your average light-hearted Saturday afternoon reading fare.
58. Vibes-based for any Gen Zers in our audience
59. It’s actually pretty easy to predict in 2025 what had already started happening in
late 2023 and early 2024.
60. Found as of February 2025 at https://www.cisa.gov/known-exploited-vulnerabilities-catalog
2025 DBIR Results and analysis 29

Figure 29. CVE type resolution by remediation status
When you realize that the partially
remediated options have the highest
percentages compared to both of the
other vulnerability samples, this kind
of strategy becomes clear, and its
popularity undeniable.
As for the “Unremediated,” all we can
offer is a sincere “Good luck!” Given
the volume and frequency of which
those vulnerabilities were exploited, the
30% of unmitigated vulnerabilities will
have caused a lot of trouble for those
organizations throughout the year. One
possibility for this large number is that
it is likely organizations only have one
asset (or a few load-balanced assets)
of those kinds, so the fully remediated
versus unremediated becomes a very
binary affair.
Figure 30. Distribution of the median of days until full remediation of vulnerabilities
in our edge device subset in a single company (n=431 – each dot is 2.15 unique
companies)
2025 DBIR Results and analysis 30

The overall median time for full
remediation also shows positive trends.
For the whole CISA KEV catalog, the
median is 38 days for a company to fully
remediate one of their vulnerabilities,
while for our edge vulnerability subset,
the same figure comes up as 32 days,
as Figure 30 demonstrates. This is
another piece of evidence pointing to
the proper prioritization of remediation
of edge device vulnerabilities.
However, as teased a few paragraphs
ago, there is also bad news to share.
We have made the definition of our
metric of time to mass exploit a bit more
generous,61 in order to really have an
upper bound on those values. We are
comparing the day of publication in the
Common Vulnerabilities and Exposures
(CVE) database with the date of it
being added to the CISA KEV catalog,62
since it’s likely that if it hit the KEV list,
the vulnerability is bound to have been
causing some damage already. Figure 31. Distribution of difference in days between CVE and CISA KEV publication
(n=292 – each dots 5.84 vulns)
Even by relaxing our definition, Figure
31 shows that the estimate of a median
of five days for a CISA KEV vulnerability
to be mass exploited still holds from our
findings from last year. And even more
concerning, the median time for our
edge device vulnerability subset was,
you guessed it, zero. We didn’t need a lot
of math for that one because 9 of the 17
were published on the KEV list the day
of or earlier than their CVE publication.
Figure 32 makes that clear.
The work never ends. It seems futile in
the face of the odds, but it is very likely
that outcomes would be much worse
if mitigating measures were not being
taken. One must ask Camus if Sisyphus
would still find contentment and
fulfillment if his mountain was infinite, the
day unending. He is constantly denied
the period of solace and contemplation
on his completed task, even if for a
moment. If Camus is not available to
answer, perhaps we should ask a CISO.
Figure 32. Distribution of difference in days between CVE and CISA KEV publication
in selected edge device vulnerabilities (n=17 – each dot is 0.94 vulns)
61. Even though we seem to be being generous to the vulnerabilities themselves here, you do not, under any
circumstances, “gotta hand it to them.”
62. We have limited this analysis to vulnerabilities from 2022 onwards because the catalog was created in
November of 2021.
2025 DBIR Results and analysis 31

VERIS Assets
Assets in VERIS document the The Figure 34 breakdown of Asset
“what” of an incident, where the varieties provides us the additional detail
nefarious threat actors perform we need to have the full picture. Both
their dangerous actions63 and where Web applications and Email servers are
you should likely be considering re- very common targets of both credential
enforcing your control frameworks if abuse-related actions (such as use of
they were affected in the incident. stolen credentials and brute force) and
exploit vuln. This usually guarantees top
This year, and for quite a few years
billing for them.
before this one, Server is the most
common asset in a breach and is now Of note here is the presence of Remote
present in 95% of them (Figure 33). access servers and the disappearance
If you have been reading those sections of File servers in this chart. As the
in order64 and have seen the types targets for the vulnerabilities that got
of Actions that have been the most top billing throughout the year shift,
prevalent, you shouldn’t be surprised so do our numbers, and we can see in
either. It is followed by Person65 assets Figure 35 how the actions alongside
and User dev(ices), which completes those types of assets concentrated
our usual top three most likely targets around Exploit vuln and the subsequent
of an Action. Ransomware deployment as a part of
the breaches they are related to.
Figure 34. Top Asset varieties in
breaches (n=5,719)
Figure 33. Assets in breaches
(n=10,289) Figure 35. Top Action varieties
alongside Remote access servers in
breaches (n=139)
63. Unless you are an Internal actor that was responsible for an Error action. You are as much a victim of the
complexity of technology as your employer organization. No intern blaming in this house.
64. We don’t judge. You do you. Print all the pages, throw them in the air and go from there.
65. It’s you! And me! Assuming I haven’t been replaced by a middling AI by now. Or maybe you are a
middling AI summarizing this document. What an empty and sad world that would be, no one writing
for no one. But we digress.
2025 DBIR Results and analysis 32

Asset categories66
Server: a device that performs User device: the devices used
functions of some sort supporting by Persons to perform their work
the organization, commonly without duties in the organization. Usually
end-user interaction. This is where all manifested in the form of laptops,
the web applications, mail services, desktops, mobile phones and tablets.
file servers and all that magical These are common targets in the
layer of information is generated. System Intrusion pattern but also in
If someone has ever told you “the the Lost and Stolen Assets pattern.
system is down,” rest assured that People do like to take their little
some Servers had their Availability computers everywhere.
impacted. Servers are common
Network: not the concept, but the
targets in almost all of the attack
actual network computing devices
patterns, but especially in our System
that make the bits go around the
Intrusion, Basic Web Application
world, such as routers, telephone
Attacks, Miscellaneous Errors and
and broadband equipment, and some
Denial of Service patterns.
of the traditional in-line network
Person: the folks (hopefully) doing security devices, such as firewalls
the work at the organization. No AI and intrusion detection systems. Hey,
chatbots allowed. Different types Verizon is also a telecommunications
of Persons will be members of company, OK?
different departments and will have
Media: precious distilled data in its
associated permissions and access
most pure and crystalline form. Just
in the organizations stemming from
kidding, mostly thumb drives and
their roles. At the very least, they
actual printed documents. You will
will have access to their very own
see the odd full disk drive and actual
User device and their own hopes
physical payment cards from time to
and dreams for the future. Person
time, but those are not common.
is a common target in the Social
Engineering pattern.
66. https://verisframework.org/assets.html
2025 DBIR Results and analysis 33

VERIS Attributes
The VERIS Attributes document Figure 37 shows the top Data varieties
the “effects” of the incident on the compromised in breaches. We would
environment where it happened. like to focus on the ones in which the
Every Action that a (threat) actor customer is the rightful owner, and the
takes on an Asset should affect object of potential data abuse when the
one of its corresponding Attributes. companies they trusted their data with
They encompass the tried-and- are breached. Personal data is obviously
true CIA Triad67 of Confidentiality, the most common variety throughout the
Integrity and Availability. years, but we would like to explore some
of the more specialized data types,
A straightforward DDoS attack or
such as Medical, Bank, Payment and
automated defacement68 of a website
Sensitive Personal.69
with an unauthenticated Content
Management System (CMS) would From Figure 38, the growth of Medical
each only affect one of those attributes data as a compromised data variety is
(Availability and Integrity, respectively, worth pointing out. As the Healthcare
for those following along at home). sector gets more and more attention
However, any incident with even a from ransomware operators, we see
couple of steps will most likely affect all this percentage increase. It was briefly
of the different Attributes, as the overlap surpassed by Bank and Sensitive
of those in the top-most level of our Personal (the last of which we started
taxonomy is shown in Figure 36. recording separately from Personal
starting last year) in the 2024 DBIR due,
in part, to all the MOVEit vulnerability-
related activity, which discriminated
very little by industry. Medical data
is now back to its (unfortunate)
first place in the specialized
customer-owned data varieties.
Figure 36. Top Attributes in incidents
(n=21,987)
Figure 37. Top Data varieties in
breaches (n=12,063)
67. Looks like we are not quite done with alliterations yet
68. Wow, remember those? Things used to be so simple.
69. This one includes data points such as U.S. Social Security numbers and government IDs worldwide that
could make it easy to abuse someone’s identity for any sort of fraudulent activity. It does not include the
embarrassing (but valid!) things you told your therapist in your last session.
2025 DBIR Results and analysis 34

Attribute categories72
Confidentiality: refers to limited
observation and disclosure
of an asset (or data). A loss
of confidentiality implies that
data was actually observed or
disclosed to an unauthorized
actor rather than endangered,
at-risk or potentially exposed
(the latter fall under the attribute
of Possession or Control73).
Short definition: limited access,
observation and disclosure.
Figure 38. Select Data varieties over time in breaches
Integrity: refers to an asset
(or data) being complete and
Another always noteworthy point is the unchanged from the original or
continuous decline of (card) Payment authorized state, content and
data from those stolen databases, which function. Losses to integrity
this year sits at 1% of data types. As we include unauthorized insertion,
have theorized in the past, the growth of modification and manipulation.
adoption of Near Field Communication Short definition: complete and
(NFC) and chip-based card payments unchanged from original.
in card-present transactions and
Availability: refers to an asset (or
of tokenized solutions for card-not-
data) being present, accessible
present ones is possibly limiting the
and ready for use when needed.
need for those data types to be stored.
Losses to availability include
We will defer those conclusions to the
destruction, deletion, movement,
capable pages of one of our sibling70
performance impact (delay or
publications, the Payment Security
acceleration) and interruption.
Report (PSR), but we will be keeping
Short definition: accessible and
an eye on this number nonetheless as
ready for use when needed.
we seek new data partners that could
provide us better insights.
At the polar opposite of the attribute
space are the incidents without data
disclosure, of which the Denial of
Service pattern is the undisputed
king.71 However, in the midst of all
those availability varieties shown
in Figure 39, we should keep close
tabs on Interruption. It did grow
slightly from the prior year (from 1.7%
to 2.3%) in incidents without data
disclosure and is where the business
interruption events we discussed in the
third-party section at the beginning Figure 39. Top Availability varieties in
of “Results and analysis” can likely incidents without data dislosure
manifest if this trend continues. (n=13,401)
70. Cousin? Distant relative? We certainly don’t want to impose a familiarity that is not reciprocal.
71. This is not a good figure of speech because most Denial of Service attacks nowadays are “distributed.”
That would imply multiple kings at any given time. A federated monarchy? An outpatient mental
institution that caters to patients who believe they are Napoleon Bonaparte?
72. https://verisframework.org/attributes.html
73. https://en.wikipedia.org/wiki/Parkerian_Hexad
2025 DBIR Results and analysis 35

VERIS discovery
method and timeline
We have been asked a few times over the Looking at discovery timelines focused
past couple of years to re-up our analysis on breaches not disclosed by the actors
of the discovery timeline for breaches, themselves, Figure 41 shows that for a
which had been left on the cutting room couple of years now, our categorization
floor of the report writing process for of “Weeks or more” has been very close
a while. But fear not! Because we can to “Days or less.” You can see the gap
afford to write “External actors are the narrowing since 2022, but all of those
most common category of threat actor are actually too statistically close within
this year” every single year, and in the this sample size for us to make any
hopes of appeasing the crowds, here statement from this analysis. It does
is a short analysis we can provide. look pretty, though, and vibes are also
important in the research process.
Discovery method analysis is suffering
from Ransomware as much as the Drilling down further, as presented
victims being affected by it. Given one in Figure 42, it becomes clearer that
of the best sources of information the median dwell time in non-Actor-
on ransomware breaches right now disclosed breaches has improved a
is when the actors themselves post little in relation to what we found in the
on their dark web portals, the Actor 2023 DBIR, being 24 days in our 2025
disclosure variety corresponds to dataset as opposed to 30 days in 2023.
96% of all our discovery methods. The difference between being in the
low 20s versus being in the low 30s
However, by setting it aside as we did
may not seem like much74 at face value,
in Figure 40, there is some valuable
but disrupting a breach a whole week
information we can glean around
earlier can make a lot of difference in
the importance of monitoring your
an incident response process. But we
environment for unusual activity and
shouldn’t be resting (or dwelling) on
training your employees to report the
our laurels and should keep striving to
same, helping to increase your odds Figure 40. Discovery method varieties
continue to get those numbers down.
of stopping one of those breaches in in non-Actor-disclosed breaches
its tracks. (n=204)
Figure 41. Discovery time over time in breaches Figure 42. Distribution of dwell time in
days in non-Actor-disclosed breaches
per year (n for 2022=93 – 2.32
breaches/dot) (n for 2024=248 – 6.20
breaches/dot)
74. The DBIR team members who are in their 40s and 50s would beg to differ.
2025 DBIR Results and analysis 36

3
Incident
Classification
Patterns
37 2025 Data Breach Investigations Report

Introduction
Longtime readers may recall that back in 2014, we introduced our Incident We continue to include the CIS Critical
Classification Patterns to the DBIR. Being the observant folks that we are, we noticed Security Controls75 relevant to each
that security incidents often played out again and again along similar lines. The fact pattern but have decided to discontinue
that they shared a given set of traits or characteristics, and that they were recurrent, the select relevant ATT&CK techniques
allowed us to create a set of categories in which to place them. Since it is easier for in them. We found those would often
most people, the DBIR authors concluded, to grasp concepts when we can place be too wide of a brush stroke and didn’t
them in containers that we can more readily understand, the Incident Classification seem as useful as using the mappings
Patterns were born. And because those patterns work so well to represent the in the opposite direction: translating
incidents, we still use them today, after a brief refresh of our machine learning models ATT&CK data from our partners to
that classified them in 2021. VERIS. If you found they were helpful for
a specific use case you have, please let
us know.
Basic Web These attacks are against a Web application, and after These incident patterns serve to cluster
Application the initial compromise, they do not have a large number the similar incidents into categories
Attacks of additional Actions. It is the “get in, get the data and that make them easier to understand
get out” pattern. and recall. They are based on the 4As
of VERIS (Action, Actor, Asset and
Denial of These attacks are intended to compromise the availability Attribute). The Incident Classification
Service of networks and systems. This includes both network and Patterns, of which there are eight, are
application layer attacks. defined in the table to the left.
Lost and Incidents where an information asset went missing, Returning readers will no doubt notice
Stolen Assets whether through misplacement or malice, are grouped the absence of the Lost and Stolen
into this pattern. pattern (which usually gets its own
section).76 While this is not a solved
Miscellaneous Incidents where unintentional actions directly compromised problem, the statistics change very little
Errors a security attribute of an information asset are found in this from year to year. The controls also do
pattern. This does not include lost devices, which are grouped not show much evolution over time—
with theft instead. either you got the memo that encryption
is a good thing or you did not.
Privilege These incidents are predominantly driven by unapproved
We had low frequency of the data in
Misuse or malicious use of legitimate privileges.
our report this year (as last), and while
we realize this is a bit unconventional,
Social This attack involves the psychological compromise of a person
we have included the at-a-glance table
Engineering that alters their behavior into taking an action or breaching
for you in case you are interested. If the
confidentiality.
data makes a surprising change in years
to come, we will certainly report it here,
System These are complex attacks that leverage malware
but until then, it has been relegated to
Intrusion and/or hacking to achieve their objectives, including deploying
the at-a-glance table on the next page.
Ransomware.
Everything This “pattern” isn’t really a pattern at all. Instead, it covers
Else all incidents that don’t fit within the orderly confines of the other
patterns. Like that container where you keep all the cables for
electronics you don’t own anymore—just in case.
Table 2. Incident Classification Patterns
75. https://cisecurity.org/controls
76. Sadly, it was left in the seat back pocket of an airplane bound for Timbuktu.
2025 DBIR Incident Classification Patterns 38

Figure 43. Patterns over time in incidents (n for 2025 dataset=22,052)
Figure 44. Patterns over time in breaches (n for 2025 dataset=12,195)
Lost and Stolen Assets
Frequency 149 incidents, 122
with confirmed
data disclosure
Summary
Threat actors Internal (73%),
This pattern continues to trend External (24%),
downward in terms of the number of Partner (8%),
incidents and breaches compared to Multiple (5%)
last year. This is hopefully due to (breaches)
effective controls being put in place on
the assets, rendering the data Actor motives Financial (86%–
inaccessible even when custody of the 100%), Fun
item is lost. Medical data appeared again (0%–14%),
this year in the top data types affected Convenience/
in these breaches. Espionage/Fear/
Grudge/Ideology/
Other/Secondary
(0%–7%)
What is the same?
(breaches)
Assets are still far more likely to be lost
than stolen. The motive for theft is Data Personal (77%),
overwhelmingly financial gain, and compromised Internal (27%),
organizations need to have controls in Other (25%) and
place to handle assets going missing so Medical (19%)
as not to cause a breach. (breaches)
2025 DBIR Incident Classification Patterns 39

System Intrusion
Summary It would be challenging to publish
Frequency 9,124 incidents,
a DBIR without having a discussion
Attackers within this pattern continue to 7,302 with
about one of its most persistent and
leverage the tried-and-true tactics of confirmed data
prominent patterns, System Intrusion.
stealing credentials, exploiting disclosure
For new readers, System Intrusion
vulnerabilities and phishing to
Threat actors External (99%), encapsulates all the breaches and
compromise organizations for a variety
Partner (1%) incidents that leverage a diversity of
of different objectives. However, while
(breaches) techniques, predominately hacking
Ransomware continues to impact a wide
techniques and malware, with a dash
swath of victim industries (of all sizes),
Actor motives Financial (85%), of Social Engineering. Think of this
there has been a recent decrease in the
Espionage (24%) pattern as the “hands on keyboard”
percentage of victims who pay the
(breaches) type of attackers, in which they’re using
ransoms and a decrease in the median
a combination of automation and craft
amount of ransom paid. Data Internal (85%),
to breach organizations’ defenses
compromised Other (44%), and compromise their environment,
Secrets (25%)
largely with the purpose of deploying
What is the same? (breaches) Ransomware, which accounts for
75% of breaches in this pattern. The
This pattern continues to be largely
remainder of the incidents found in this
driven by ransomware, followed by
pattern is split between Espionage and
Espionage and Magecart infections.
a few other types of financially
motivated criminals.
Same tactics,
different year
When discussing Ransomware, it is
important to note that it really captures
the monetization of system access,
and that around 42% of breaches
involve compromised credentials,
an exploited vulnerability or the use
of phishing. Although the tactics are
similar, the scale upon which they are
being leveraged differs from year to year
(Figure 45). This may not be surprising
given the fact that in certain years,
Figure 45. Known initial access vectors over time in Ransomware action breaches
widely exploited zero-days can be
(n in 2025 dataset=4,630)
dropped and used against thousands of
organizations over the course of a single
weekend. This type of activity accounts
for the large increase in exploiting
vulnerabilities that we witnessed
this year and the last year.
However, what we find interesting is
that while the number of exploited
vulnerabilities in Ransomware has
dropped from last year,77 it’s still much
higher than any of the previous years,
having doubled since 2022.
77. Which was overrepresenting vulnerabilities like MOVEit
2025 DBIR Incident Classification Patterns 40

This could be an indication that it may
become a more frequent tactic so
long as it continues to pay off. Another
interesting element is that we’re seeing
both state-sponsored actors and
financially motivated actors leverage
vulnerabilities as a common way to
compromise organizations, which
highlights the broad range of appeal
that these vulnerable systems have
to attackers.
Turning tides?
Based on our data, ransomware is
clearly still a preferred tactic, but how
much are those ransoms actually?
In the past, we have leveraged the
very detailed data of the FBI Internet
Crime Complaint Center (IC3) around
the transfer of funds to threat actors
reported to them by victims. This year,
we are trying something a bit different:
Because of the kind contribution of
data partners in cyber insurance and
ransomware negotiations, we could
get a good glimpse of what the values
were around paid-out ransoms. Then
we combined this additional data with
the IC3 dataset, as those should line up
in the timeline of the “ransom payment
cycle” and actually be from the same
point in time, after ransom payment and
before law enforcement intervention.
You can see the results for the last three
years in Figure 46. For the calendar year
2024, the median ransom paid comes up
as $115,000, which is a decrease from
$150,000 in the previous year.
A median of $150,000 in the 2023
calendar year is significantly higher
than our previously reported $46,000
in the 2024 DBIR, but we are now
drawing from a larger sample, involving Figure 46. Distribution of loss due to ransom payment in USD (2022–2024)
potentially other countries and (n for 2022=664 – each dot is 3.32 events) (n for 2023=462 – each dot is 2.31
events) (n for 2024=351 – each dot is 1.75 events)
organization sizes. Note, the customers
of ransomware negotiation companies
tend to be larger enterprises. We believe
this to be a more complete and resilient
result by the combination of distinct
data sources.
2025 DBIR Incident Classification Patterns 41

We did report that the median in 2023 While there’s some variation in
had doubled in relation to 2022 and terms of the scale, which is to be
to see this result replicated in this expected as we’re examining different
new sampling of the ransom universe datasets, the spirit of the findings is
reminds us of the sheer wizardry that the same. Discussing this with the data
is statistics.78 Not only has the median contributors that shared the raw data
changed but so have the extremes, with us, they believe that those two facts
with 95% of ransoms being less are intrinsically linked. Less folks are
than $3 million in 2024, which is a paying the ransom—maybe because
considerable drop from the $9.9 million they’re better prepared for recovery of
reported in 2023. The shift in amounts the environment—or they just don’t go
is interesting, but is this good news? with the “trust me, bro” of not disclosing
the data. Add some increased pressure
One theory as to why the ransoms
from law enforcement takedowns
are decreasing in price is because
on these groups, and their opening
fewer organizations are willing to pay
amounts for ransom have been lower
the ransoms demanded (Figure 47).
overall. It is always a treat to see free
According to data from our ransomware
market pressures we learned about
negotiation contributors, in 2022,
in Econ 101 in the wild like this.
approximately 50% of victims refused
to pay the ransom, and in 2024, that
number increased to 64% of non- Figure 47. Percentage of ransoms not
payers. Our findings seem to be paid in Ransomware incidents per
corroborated from other researchers calendar year
who found that ransomware payments in
the blockchain decreased by 35%
last year.79
78. We will henceforth be referring to our Data Scientists as Data Sorcerers.
79. https://www.chainalysis.com/blog/crypto-crime-ransomware-victim-extortion-2025
2025 DBIR Incident Classification Patterns 42

Pushing the
Wizardtrolley
Another persistent issue that we have
reported on as part of this pattern
is Magecart infections, in which
e-commerce sites are compromised
with malware that siphons out payment
card data during checkout. These
attacks make up the other main type
of incidents seen in System Intrusion.
They represent 1% of System Intrusion
breaches and 80% of breaches
involving payment cards. However, we
still believe those are not getting a lot of
representation in our incident dataset,
so we decided to do a deeper dive into
the data to figure out what we could find.
By reviewing a large-scale, multiple-year
dataset involving Magecart from one of Figure 48. Monthly vistors to Magecart-compromised sites
our data contributors, we’ve determined (n=43,324 – each dot is 216.62 websites)
that this type of attack seems to cover
multiple countries and industries. The
threat actors appear to be driven largely
by opportunity rather than by targeting
the largest vendors. The median monthly
visitor count to the affected websites
is around 7,000 (Figure 48), and the
median infection time of the websites is
less than 30 days (Figure 49).
We do not know how many of those
monthly visitors end up entering their
credit card details and having them
stolen, but it seems to be profitable
enough for the criminals to continue
doing it. But although these actors are
clever in terms of hiding their payloads
from the regular user, they leverage
many of the same tactics of exploiting
vulnerabilities and using stolen
credentials to compromise e-commerce
sites, regardless of size.
Figure 49. Magecart infection duration (n=43.324 – each dot is 866.48 websites)
2025 DBIR Incident Classification Patterns 43

They’re When looking at the hacking vectors
associated with these Espionage-
spies—but not motivated breaches, we see a relatively
strong diversity of techniques leveraged
necessarily on by attackers, with “Other networking
services” coming out clearly at the top
our side. (Figure 50). In VERIS, this is largely
associated with the lateral movement
techniques attackers leverage once
Adventures abroad, exotic cars and they’ve already set up a beachhead
thrilling romance. This is probably what within an organization, such as the
some folks expected when they signed Windows NTLM/SMB protocol, for
up as spies. Unfortunately for them, the instance. As has long been the case,
reality for espionage-related activities attackers will utilize their established
in our dataset is perhaps a little bit skills and infrastructure to pivot around
less thrilling. The actors in this domain the organization. To connect into the
are leveraging established processes organization, we see that these actors
and tooling to deceive, compromise are pretty keen on deploying some type
and collect sensitive data from their of malware, either a custom-coded work
targets. We see the majority of these of art or any of the available offensive
actors leveraging stolen credentials security tools. Or they simply waltz in
as part of their efforts, using malware through the front door via the VPN.
to maintain persistence and deceiving
users as a way into the organizations.
Figure 50. Top hacking vectors for
Espionage-motivated breaches
(n=1,326)
2025 DBIR Incident Classification Patterns 44

CIS Controls for Protecting devices Protecting accounts
consideration Secure Configuration of Enterprise Account Management [5]
Assets and Software [4] – Establish and Maintain an Inventory
– Establish and Maintain a Secure of Accounts [5.1]
Bearing in mind the breadth of activity Configuration Process [4.1] – Disable Dormant Accounts [5.3]
found within this pattern and how – Establish and Maintain a Secure
actors leverage a wide collection of Configuration Process for Network Access Control Management [6]
techniques and tactics, there are a Infrastructure [4.2] – Establish an Access Granting/
lot of safeguards that organizations – Implement and Manage a Firewall on Revoking Process [6.1, 6.2]
should consider implementing. To the Servers [4.4] – Require MFA for Externally-Exposed
right is a small subset of the things an – Implement and Manage a Firewall on Applications [6.3]
organization could do. They should End-User Devices [4.5] – Require MFA for Remote Network
serve as a starting point for building Access [6.4]
out your own risk assessments to help Email and Web Browser
determine what controls are appropriate Protections [9] Security awareness
to your organization’s risk profile. – Use DNS Filtering Services [9.2] programs
Malware Defenses [10]
Security Awareness and Skills Training
– Deploy and Maintain Anti-Malware
[14]
Software [10.1]
– Configure Automatic Anti-Malware
Signature Updates [10.2]
Continuous Vulnerability
Management [7]
– Establish and Maintain a
Vulnerability Management
Process [7.1]
– Establish and Maintain a
Remediation Process [7.2]
Data Recovery [11]
– Establish and Maintain a Data
Recovery Process [11.1]
– Perform Automated Backups [11.2]
– Protect Recovery Data [11.3]
– Establish and Maintain an Isolated
Instance of Recovery Data [11.4]
2025 DBIR Incident Classification Patterns 45

Social Engineering
Summary Hello, is this … ?
Frequency 4,009 incidents,
As defenders are improving through 3,405 with confirmed
training and hardening their user data disclosure This pattern has always been an
accounts, attackers are also adapting interesting one, not only because of
Threat actors External (100%)
their techniques to bypass those its data but also due to how common
(breaches)
protections. these types of attacks are and how
Actor motives Financial (55%), quickly they occur. This pattern has
Espionage (52%) been in our top three since 2019, and
What is the same? (breaches) that shouldn’t be a surprise—just take a
look at the spam texts on your phone.80
Phishing and Pretexting are still the main
Data Internal (68%), Other If it’s anything like ours, it’s chock full
techniques leveraged to con employees.
compromised (58%), Secrets (53%) of messages “mistakenly” sent to the
(breaches) wrong person, invoices for toll roads in
other states or “remote jobs” that are
too good to be true.
In our opinion, the really interesting
thing about these types of attacks is not
simply the scale of them but also the
amount of time attackers seem to be
dedicating to building familiarity with the
victims. AI enthusiasts would, of course,
state vehemently that this is solely due
to AI tools, but in reality, the trend has
simply been going on too long for AI to
take all the credit.81
No longer can we address this issue by
looking for basic things such as “watch
out for typos” or “does that country
really have a prince?” Now we even have
to be cautious of messages that seem
to be coming from our peers, partners
or vendors. Some originate from online
relationships that are built over a period
of months of back and forth via email (or
a messaging app) with the occasional
video chat thrown in to aid legitimacy.
Without further ado, let’s dive into
what we’re seeing and how we can
help protect ourselves against these
types of attacks.
80. And report them to your carrier! It does make a difference to pinpoint the offenders.
81. Or blame
2025 DBIR Incident Classification Patterns 46

My aunt works
at a crypto
exchange.
For this year’s data, there was a slight
shift in the who and the what we found
associated with Social Engineering. This
is perhaps not the result of a colossal
shift in what attackers are doing, but
more likely,82 it is because we are
improving at assessing data from those
persistent state-sponsored actors.
These Espionage-motivated attacks
now account for 52% of Social
Figure 51. Top select Social action Figure 52. Percentage of Microsoft
Engineering breaches. We realize this
varieties in Social Engineering incidents 365 MFA bypass by attack type
may be confusing because, being the
(n=3,208) (n=2,102)
astute reader that you are, you will
probably have noticed that Financial
also accounts for 55% of motives. A few years ago, we added some action To contrast this, we’ve also looked
The reason for this is that there are varieties to capture different techniques at security logs from Microsoft 365
certain nation-affiliated actors that used to bypass MFA, but we haven’t accounts visible to a managed
dabble both in the financially motivated really had a lot of data to talk about— security services data contributor,
and Espionage-motivated attacks83 until now. When we look at the three as Figure 52 shows.
(accounting for about 12% of state- types of techniques used to bypass
Overall, we found suspicious logins
sponsored actor incidents). MFA, Adversary-in-the-Middle (AiTM),
present in almost 40% of the attacks.
Password dumping and Hijacking (like
Figure 51 showcases some Social When looking at attacks focused on
SIM swapping), we tend to find them
action varieties of interest we have bypassing MFA, we found that Token
in equal force in our dataset, with the
found in this pattern. Alongside theft was the most popular at 31%,
caveat that they show up in only 4% of
our usual suspects of Phishing and followed by MFA interrupt and AiTM
our total breaches.
Pretexting, avid readers may notice attacks. Once again, this supports
our new action on the block, Prompt Prompt bombing is the exception and the tried-and-true notion that as our
bombing, in which users are bombarded shows at a higher rate than the others defenses shift, so do the attackers’
with MFA login requests. This is showing as noted previously. However, it is tied processes. Having MFA enabled
up along with Baiting, where typically to a couple of the large state-sponsored continues to be the gold standard to
compromised versions of legitimate campaigns that spammed a lot of help protect against authentication
software are planted via search engine targets around the world. One way of abuse, but having it enabled should
optimization (SEO) or ad purchasing. interpreting this, in the cases where not make your detection and
This results in unsuspecting users attackers bypass MFA, is that they’ll monitoring processes complacent.
downloading malware instead of some leverage whichever weakness exists in
fancy digital coupon browser extension. that MFA implementation. A dedicated
adversary will do whatever works.
The Prompt bombing is definitely of
interest, since it’s the first time that
this data has come out in full force,
but that’s mainly a result of partners
doing an excellent job reporting on the
techniques used by adversaries.
82. This is what we like to think anyway.
83. Yes, we know they do that just to confound our statistics. It has nothing to do with wanting more $$.
2025 DBIR Incident Classification Patterns 47

Doubling your
investments
Business Email Compromise (BEC) is
big business.84 In 2024 alone, according
to the FBI IC3, more than $6.3 billion
was transferred as part of these scams.
Although the total number is increasing,
the median amount of money extracted
from victims has become relatively
consistent and has settled around the
$50,000 mark. This number is based on
19,000 different complaints—a similar
Figure 53. Distribution of phishing simulation campaign click rate by organization
number of complaints as seen over the
(n=7,743 – each dot is 193.58 organizations)
last two years.
In terms of how the money is sent,
cybercriminals still by and large prefer
to pilfer via wire transfer, which made up
approximately 88% of all BEC proceeds.
While other tactics are being employed,
such as using virtual currency, those
seem to have dropped since 2023.
However, it’s the inverse relationship
in the world of ransomware in which
most transactions to ransomware
actors leverage virtual currency. For
BEC, it’s all about blending in and not
getting employees to second guess the
transaction requests. Or perhaps people
are becoming more wary of scams
involving gift cards or cryptocurrency.85
Figure 54. Distribution of phishing simulation campaign report rates by organization
There is something to be said about the
recent training status (n for No=68,492 – each dot is 3,424.60 campaigns)
importance of listening to your instincts. (n for Yes=36,325 – each dot is 1,816.25 campaigns)
Quick, Not surprisingly, but still somewhat The flip side of this is that continued
disappointing, we see that the number training on how to report phishing seems
guaranteed doesn’t quite go to zero, as Figure 53 to have a compounding positive effect
demonstrates. This might indicate that regardless of whether the individual
returns! there is a ceiling to the effectiveness of actually clicked on the phishing email.
education programs over a long period Figure 54 looks at the two relationships:
of time. It is often said, “You can fool one determining the company-wide
The foundations of user awareness some of the people all of the time, but report rate of simulated phishing by
and security training on how to report you can’t fool all the people all the time,” employees with recent training—
suspected social attacks remains one and maybe 1.5% of employees in the within 30 days—and one without it.
of the most important controls at your median case are the ones you can fool
disposal. This year, we have focused on all of the time—since they’re still clicking
analyzing the click rate of companies after all these training sessions.
who have been a part of regular security
awareness training in conjunction with
phishing simulation campaigns.
84. The emails are often short, though.
85. That $6.3 billion figure says otherwise.
2025 DBIR Incident Classification Patterns 48

What we found was remarkable. When
we examined the reporting rate of
phishing emails, we found that users
who had more recent training reported
the phishing emails at a significantly
higher rate—about 21% against a base
rate of 5%, a four times relative increase.
However, the impact of recent training in
click rate was way less prominent, with
only 5% relative impact on each training.
Maybe the compounding increments on
click rate are just that much slower, or
the simulated phishing campaigns just
keep getting nastier over time,86 as we
can see the potential of its continuous
decline in our earlier figure.
Beyond our glitzy industry reports,
academic researchers have also been
trying to pin down the efficacy of
phishing training. Some of our peers did
one such examination in a very well-
thought-out report87 looking at such
efficacy of training and found somewhat
similar results to us regarding the click
rate. They found that the failure rate
Figure 55. Phishing simulation campaign report rate by click status
(aka the click rate in our non-judgmental
parlance) was unaffected by the training,
and the difference between both We updated the tracking of report rates
groups (i.e., trained and untrained) was we had last year in Figure 55 to help
extremely low. showcase that. It certainly is a breath of
In their paper, they state limited impact fresh air to see folks continue to debate
overall from training, noting the limited and discuss this important topic, so
time spent by users engaging with we encourage our readers to consider
the training. In our opinion, this might giving the paper a read, as well.
then be a limitation of the organization Given those results, the long-term
they chose for their analysis—a strategy becomes incentivizing your
university campus—in an industry employees to report, and for those
vertical frequently plagued by lack of reports to be as automated as possible
resources or focus in cybersecurity. in your workflow in order to help block
We may not have had the opportunity offending emails and links. Finally, it will
to perform a causal analysis, but our help discover employees who may have
data contributors’ combined sample fallen victim, so they can be quarantined
size is more than 7,000 organizations. for faster remediation. If preventing all
And while our findings might be slightly clicking by employees is an impossibility,
similar in the click rate impact regard, we at least let them understand that their
found a continuous increase in reporting reporting can help the organization
as the result of continuous training. contain threats quicker.
86. The median employee today would never fall for a phishing email from Ancient Egypt. We know the
pyramids are not for sale!
87. https://people.cs.uchicago.edu/~grantho/papers/oakland2025_phishing-training.pdf
2025 DBIR Incident Classification Patterns 49

Swapper, no • Be wary of Social Engineering From the perspective of an organization
attacks: Sometimes to bypass that leverages text messaging as
SIM swapping existing protections on your device, an authentication factor, one recent
the attacker will pretend to be an development is that telecommunications
employee of your service provider providers have started offering APIs in
Being part of a major tele- and try to get you to approve a which trusted partners can verify if a
communications provider delivers login or disclose the security code number has had their SIM swapped to a
us some insights into how users can sent to the device—or the one just different device recently, regardless of
help better protect themselves from generated by your shiny new TOTP whether it was a fraudulent move or not.
certain types of MFA bypass, such MFA app. On business accounts,
Think of it as an analog to an enterprise
as SIM swapping. There is a lot of the employee who manages your
resource planning (ERP) policy of not
prevention and response work that wireless fleet is the premium target
paying an invoice to vendors that have
happens behind the scenes here for those types of attacks and should
recently changed their addresses or
at Verizon to stop those types of be made well aware of them. Make
banking information. Of course, those
attacks from happening for both sure only authorized employees have
things happen for legitimate reasons all
business and consumer customers this access, and revoke any assign
the time, but it might be worth verifying
alike; however, there are still things permissions when there are transfers
such changes when you’re talking
that you as a consumer can do or changes of employment.
about money changing hands.
to help protect your account.
One of the scammers’ favorite scenarios
What you do with the information
• Use SIM protection: Many carriers is to actually pose as a fraud agent,
will vary depending on what other
allow you to lock lines to your mobile claim a large number of devices were
MFA authentication options your
devices, preventing changes on purchased on the business account and
organization has, but providing
devices from happening and, more tell you that they are calling to confirm
some more authentication friction
importantly, preventing portability to the purchase. After the obvious negative
to customers who have recently
other carriers. Fraud or attempted from the customer, they proceed to help
changed their devices might not be
fraud is much easier to detect in the them through a password reset as a
such a bad idea for critical services
purview of a single carrier, and when security precaution and take over the
that are frequently targeted by fraud.
it crosses that boundary to another account that way.
company, detection and response
If you are lucky, it’s just device purchase
become much more difficult.
fraud and they will use your account to
• Use TOTP88 MFA on your accounts: deliver shiny new mobile devices to a
We are not here to security threat actor-controlled physical address.
shame email-based MFAs—or any But the SIM swaps and port outs are
additional factor that can help your fairly easy to perform from having full
authentication security improve. control of the account.
However, given that this has been the
single most likely avenue for business
wireless account compromise (as the
second step after a business email
intrusion), this will make a difference.
88. Those little authenticator apps on your phone. Most password managers can manage those for you, too.
2025 DBIR Incident Classification Patterns 50

CIS Controls for Protect accounts
consideration Account Management [5]
– Establish and Maintain an Inventory
of Accounts [5.1]
There are a fair number of controls to – Disable Dormant Accounts [5.3]
consider when confronting this complex
threat, and all of them have pros and Access Control Management [6]
cons. Due to the strong human element – Establish an Access Granting/
associated with this pattern, many of the Revoking Process [6.1, 6.2]
controls pertain to helping users detect – Require MFA for Externally-
and report attacks, as well as helping Exposed Applications [6.3]
protect their user accounts in the – Require MFA for Remote Network
event that they fall victim to a phishing Access [6.4]
attack. Lastly, due to the importance
of the role played by law enforcement Security awareness
in responding to BECs, it is key to have programs
plans and contacts already in place.
Security Awareness and Skills Training
[14]
Although not part of the CIS Controls,
a special focus should be placed on
BEC and processes associated with
updating bank accounts.
Managing incident response
Incident Response Management [17]
– Designate Personnel to Manage
Incident Handling [17.1]
– Establish and Maintain Contact
Information for Reporting Security
Incidents [17.2]
– Establish and Maintain an
Enterprise Process for Reporting
Incidents [17.3]
2025 DBIR Incident Classification Patterns 51

Basic Web
Application Attacks
Summary
Frequency 1,701 incidents, 1,387
Espionage has taken over this pattern as with confirmed data
threat actors are using weak credentials disclosure
at scale to compromise a variety of
Threat actors External (100%)
different victims.
(breaches)
Actor motives Espionage (61%),
What is the same? Financial (34%),
Ideology (4%)
The Use of stolen credentials is still the
(breaches)
defining action in this pattern.
Data Other (65%), Personal
compromised (36%), Credentials
(35%), Internal (31%)
(breaches)
Figure 56. Top Action varieties in BWAA
breaches (n=1,021)
Like the proverbial keys to the
kingdom, credentials are what allow
our trusted employees to bypass our
layered defenses and gain access to
the crown jewels (or at least to the
systems they need to do their jobs).
Putting aside that tired metaphor,89
this specific pattern is all about bad
actors accessing our key data with
the least amount of effort expended,
hence the name Basic Web Application
Attacks—or BWAA, for short. However,
in spite of the name, there is a certain
amount of complexity involved and
even a criminal ecosystem that has
sprung up to take advantage of these
loose keys. This can, at times, spell
disaster since these keys are sometimes
the first and last lines of defense
for many of our precious secrets.
89. We might also be victims of the author trope of self-insertion.
2025 DBIR Incident Classification Patterns 52

Credentials are largely the name of
the game for this pattern, along with
a couple of others, such as Social
Engineering and System Intrusion. In
this pattern, about 88% of the breaches
involve the Use of stolen credentials,
which sometimes serves as both
the first and only action, while other
times, it is just one piece of a larger
attack chain. As seen in Figure 56, it’s
not just stolen credentials; you also
have to contend with brute forcing
(“guessed credentials”) along with the
establishment of Backdoors or C2s
(command and controls), which enable
threat actors to maintain their hard-
earned access after they utilize those Figure 57. Brute force and Exploit vuln actions over time in BWAA breaches
nefariously acquired credentials. (n for 2025 dataset=1,021)
Vulns or Creds? In that case, the credentials seem to
have been mostly of stolen variety,
but the access control systems do
If brute forcing is Sonny, then exploiting not discriminate if credentials are
vulnerabilities would be Cher (or for stolen or guessed. We discussed
a reference from this century: Travis this campaign a bit in the big picture
to their Taylor). In Figure 57, we’ve section in “Results and analysis,”
captured how these two actions have if you are hungry for more.91
sparred and competed within this
pattern, with brute forcing coming out
on top for this year. This doesn’t mean Paths of least
that exploiting vulnerabilities are down
overall90; they’re simply not showing up resistance
as much in this pattern as the tried-
and-true method of hammering on the
credentials until a password pops out. Somewhat surprisingly, we found that
It is important to note that the brute state-sponsored actors have been using
forcing isn’t simply limited to the actual similar tactics to get those secrets.
employees of an organization, but it’s Although Espionage has always existed
also targeted toward users to find ways in this pattern, this is the first time that
of taking over accounts in a customer- it has taken the main stage (Figure
facing environment. 58). This is perhaps a testament to the
increasing quality of our partners, as well
This was certainly the case in some
as the shift by attackers to leverage the
of the third-party breaches we
easiest way in—through the front door. Figure 58. Top Actor motives in BWAA
documented this year—the most
For the last couple of years, Espionage breaches (n=688)
prominent involving the affected
has hovered around 10% to 20% of the
Snowflake customers.
BWAA breaches, but this year it accounts
for an eye-opening 62%.
90. It REALLY doesn’t. Have a look at the “VERIS Actions” section if you haven’t already.
91. Just like Lucy van Pelt, we never eat the December snowflakes. We wait until January
when they are ripe.
2025 DBIR Incident Classification Patterns 53

CIS Controls for Credential Marketplaces: Online marketplaces
are where infostealer distributors
consideration ecosystems often post the logs that are available
for sale with the domains that have
and the stolen credentials associated with
compromised systems, along with some
Mitigation efforts against
password high-level demographic information.
stolen credentials
Premium channels: The premium
Account Management [5] food chain channels allow individuals to
– Establish and Maintain an Inventory pay for access to logs that are
of Accounts [5.1] posted in private chat rooms.
In the last issue of the DBIR, we
– Disable Dormant Accounts [5.3] Live logs: These offer backend
did a relatively shallow dive into the
access to infostealer databases,
world of stolen credentials. This
Access Control Management [6] which can allow users to get access
year, we’re looking to get out of the
– Establish an Access Granting/ to logs before they show up in other
kiddie pool, put on our snorkels and
Revoking Process [6.1, 6.2] sources, such as the marketplaces.
wade into its abyssal ecosystem.
– Require MFA for Externally-
Exposed Applications [6.3] Free samples: To promote their
– Require MFA for Remote Network premium channels or offerings, many
Infostealers
Access [6.4] vendors provide daily or weekly samples
of their logs on Telegram. Some threat
Mitigation efforts against galore! actors have built their entire attack
process on leveraging these free
vulnerability exploitation
samples for account takeovers.
If the subject is stolen credentials,
Continuous Vulnerability
we have to start our exploration at
Management [7]
infostealers. The infostealers are
– Establish and Maintain a
malware that are designed to steal
Vulnerability Management
information92 from the victims’ systems,
Process [7.1]
with a strong focus on valuable data,
– Establish and Maintain a
such as stored passwords, cookies and
Remediation Process [7.2]
any available crypto-wallet information.
– Perform Automated Operating
Once these secrets are vacuumed up93
System Patch Management [7.3]
by the malware, they are exfiltrated
– Perform Automated Application
to a couple of different sources. The
Patch Management [7.4]
following is a list of the more common
places these credentials end up before
getting used by criminals. All the
collected data is then packaged up as
“logs” and distributed for others to use
as part of their attacks.
92. And not designed to have creative names
93. Or hoovered up, if the malware is of British origin
2025 DBIR Incident Classification Patterns 54

To gain an understanding of what are
in those logs, we did a sampling of
different sources and examined the
types of domains being collected.
Figure 59 has a breakdown of the types
of domains found in these logs, and it
should be of no surprise that streaming,
gaming and social media were
commonplace in each of the different
sources. For the more entrepreneurial
criminals, such ease of access to
credentials and cookies, even in the
free samples, might present a tempting
target for account takeovers. Also
interesting is how similar each of the
different log sources were, which may
indicate that it is not what is for sale as
much as how quickly and how many you
can get that is the market differentiator
between the different sources.
Another slice of data we wanted to
look into was collections of samples
that had domains that were possibly
associated with organizations, such
as developer tools, internal GitHub Figure 59. Types of captured website credentials across different infostealer log
repositories, domains indicating sources (n=33,933)
remote access servers and cloud
administration. At first cut, logs with a
lot of Education domains were gumming
up our analysis, so we removed them
in Figure 60 The same typical culprits
of social media, streaming and gaming
show up consistently, even in these
logs that have more enterprise-focused
resources. While these logs clearly
have value for attackers performing
account takeovers for these kinds
of sites, they also might unknowingly
have access to credentials that provide
access to key organizational assets,
such as credentials to the VPN, GitHub
repositories or cloud environments.
Figure 60. Types of site credentials across different log queries (EDU removed)
(n=7,855)
2025 DBIR Incident Classification Patterns 55

Enterprise- Going in line with the discussion So to put it in simpler terms, 46% of
of how many of these devices are the systems compromised with an
grade security corporate managed, the question infostealer that had possible corporate
will come up of how many of these login data were non-managed devices.
non-corporate devices might have What we don’t know is if those
Last year, we tried to use a ballpark corporate credentials. By looking at our organizations had a BYOD policy in
method to determine how many of the business app subsets, in which there’s a place or if folks just logged in with
systems were potentially corporate likely known business app domain being whatever computer they had available.
systems by looking at what percentage used, we whittled away that dataset If you don’t choose to have a BYOD
didn’t have any social media domains to records that had OS versioning policy and don’t enforce what sorts
listed. Although this is admittedly a bit of information that we could use and that of devices have access to corporate
a kludgy approach, we came up with an had at least one email domain that systems, the BYOD policy can wind up
estimate of 30% of the systems listed on wasn’t from a free email provider. From being chosen for you and you might not
the marketplaces as hypothetically being this subset, we found that 46% of the like the results. At least we can get a
corporate owned. Always on a path of devices were non-enterprise managed. pretty glyph chart out of it in Figure 61.
improvement and self-actualization, we
retried the analysis in two different ways
this year. The first used the sampling
shown in Figure 59, and we found
across the different sources between
35% and 38% of the logs didn’t contain
any of the top social media companies.
Of course, there are nuances with an
approach like this. We focused on the
top social media platforms, but there
are probably a lot of regional variants
that we didn’t know about, so there
may be biases in this specific number.
With that in mind, we took an additional
approach of looking at the version of
Windows collected by the infostealers
(we did mention they vacuum up a lot
of information, right?). What we found
was that about 34% of the Windows
versions were Enterprise, with even
a few Windows Server and Windows
XP operating systems (OSs) floating
around in there long after their end-
of-life dates.94 So with these three
combined metrics, we’re estimating
that approximately 30% of these Figure 61. Percentage of non-managed devices with corporate logins in infostealer
compromised systems are logs (each glyph is 0.5%)
Enterprise-licensed devices.
94. With the final security update for Service Pack 3 for XP released on May 14, 2019 (end of life was Apr
2014), what could possibly go wrong?
2025 DBIR Incident Classification Patterns 56

Stolen
credentials in
my ransomware
data?!
While we know that these stolen
credentials are used for things such as
account takeovers, we also wanted to
explore what, if any, was the nexus to
Ransomware. By examining some of
the victims95 posted to the ransomware
extortion sites, we found that 54% of
the victims had their domains show
up in at least one infostealer log or
in marketplace postings, and 40%
of those logs contained corporate
email addresses. Figure 62 shows
the range of distribution of when
credentials were found in relation
to ransomware actor disclosure.
Of course, there are many caveats
Figure 62. Distribution of difference in days between ransomware posting and
and additional research opportunities infostealer log discovery (n=503 – each dot is 2.52 ransomware victims)
in this area,96 but it does seem to
corroborate the anecdotal evidence
that leveraging stolen credentials
from infostealers is a key tactic used
by some ransomware operators.
95. We focused on the ones that we were able to associate an email address with.
96. We are saving it for the book deal.
2025 DBIR Incident Classification Patterns 57

More than Is this the year
(pass)words passwords
finally die?98
Compromised databases are another
data source that can feed this
ecosystem. In 2024 alone, more than Does this mean we should abandon
2.8 billion passwords—hashed or passwords and start looking toward
otherwise—were posted for sale (or free passwordless authentication solutions?
for the taking) in criminal forums. In these Yes, absolutely—humans are bad
dumps, we still often see compromised at choosing strong passwords, we
databases using the outdated MD5 frequently reuse them and we are
algorithm, resulting in about 63 million victims of Social Engineering fairly
records with very weak hashes. To put consistently. However, as rehabilitated
this in perspective, that’s about 2% of system admins, traumatized product
total records compromised—not great, owners and everyday users eager for
but not terrible.97 convenience, we realize that day is still
far away. Passphrase management by
Figure 63 captures the other types
biometrics and integration with backend
of records commonly found in these
systems in our mobile devices shows
breaches as a percentage of their total.
us an idea of what is possible, but a
In addition to passwords (regardless
lot of companies struggle with MFA
of hash status), we also found email
deployment still.
addresses (61% of breaches), phone
numbers (39%), government-issued IDs Even if we cannot take the magical
(22%) and even the occasional passport way out, there are important things
(1.8%). Not only do these compromised that we can still do to help put up
databases add to the pool of potentially protections around our stealable
compromised passwords, but they’re and fragile credentials:
also handy for criminals looking to
• MFA should not be optional or an
collect various key personal information
upsold feature in your system: Even
on individuals for follow-up fraud and
with flaws in certain implementations,
social attacks.
it is leagues better than just
usernames and passwords.
• Scrutinize logins: Cookies and
session keys are also part of the theft
Figure 63 . Percentage of breached
process, showing up in infostealer
databases with data types (n=3,903)
logs and captured via AiTM types of
attacks. Build additional protection
around their use like with a conditional
access policy that dictates how to
trust endpoints authenticating into
your environment.
97. Not unlike 3.6 roentgen.
98. As likely as this being the year of the Linux desktop
2025 DBIR Incident Classification Patterns 58

• Drop complexity requirements and The proliferation of infostealers, the
focus on passphrases: We’re not availability of stolen credentials in
great at those, as our research on access brokers and our own results
password datasets from contributors here in the DBIR that show credential
shows that only 3% of the total abuse is consistently the top initial
unique passwords meet complexity access vector can paint a picture that
requirements, and even the National all is lost. “Assume compromise,” some
Institute of Standards and Technology security companies used to say in their
(NIST) has updated its guidance. marketing materials. We have always
thought that was too bleak, and to be
• Encourage long passwords and
honest, a bit paralyzing. Rather than
credential protections on internal
“you have already been breached, so
systems: There are multiple key
stop struggling,”99 given the evidence
tactics adversaries leverage to get
we have presented, we are not blind
domain credentials, and a lot of them
to the risks. Perhaps a better, more
rely on poor configuration and weak
constructive way of thinking of how this
passwords. Just because your VPN
impacts your organization is to “assume
enforces MFA doesn’t mean that the
access, ready defenses.”
credentials used to administer internal
systems are safe. Think about how If an adversary was able to obtain
credentials are leveraged once inside credentials to your environment and get
the environment. The list of cracked in, how do you limit their reach? How far
passwords can continue to grow, and can they go until you challenge them to
with the access of shared resources, a second authentication factor? Friction
cracking hashes will continue to be an tolerance will be different among
important tactic for adversaries. administrators, regular employees and
customers of your service, but so will
• Deploy OS hardening for your
the systemic risk that each one of those
endpoint systems and domain
poses to your organization.
controllers: Secure configurations
go a long way toward hardening and
removing the low-hanging fruit that
threat actors leverage.
99. You have already been assimilated.
2025 DBIR Incident Classification Patterns 59

Miscellaneous Errors
Summary Slapstick humor: Those trips, slips and
Frequency 1,476 incidents, 1,449
falls look funny on the latest viral video,
While the number of incidents and with confirmed data
but in real life, the damage can be
breaches seen in this pattern decreased disclosure
significant. Nobody wants to admit that
overall from last year, it is possibly due
Threat actors Internal (98%), Partner their employees may be their weakest
to visibility and not people suddenly
(2%) (breaches) link in the security chain, but the fact
paying more attention. The top three
remains that human error is an enduring
were Misdelivery, Misconfiguration and
Data Personal (95%), cause of data breach events.
Publishing error, which was a change
compromised Internal (21%), Other
from last year’s top three. This year, we saw quite a decrease in
(15%), Bank (10%)
the Miscellaneous Errors pattern in the
(breaches)
number of incidents and breaches. This
is likely due to a change in the makeup
What is the same?
of the partners contributing to the report
Errors are like death and taxes—you can this year and not a miraculous lack of
always count on them. This year is no people making mistakes. We are sorry
different, with Misdelivery in the top spot to tell you that your employees can still
once again. accidentally cause breaches.100
Figure 64. Top Action varieties in
Miscellaneous Errors breaches
(n=1,399)
Although we usually see Miscellaneous
Errors primarily caused by insiders,
we did see a small number of Partner-
caused breaches this year. But
regardless of who caused these error
breaches, they are most frequently
one of three kinds: Misdelivery,
Misconfiguration and Publishing error,
as shown in Figure 64.
100. But if you’re lucky, it will be hilarious and caught on video.
2025 DBIR Incident Classification Patterns 60

Misdelivery is typically data in Unfortunately, we have seen a number CIS Controls for
electronic form, but it can also be of cases in the public dataset in which
paper documents—especially for these kinds of errors have resulted in consideration
those industries who do regular mass exposure of people whose health and
mailings, as shown in Figure 65. And well-being may be jeopardized when
Misconfigurations are most frequently the data falls into the wrong hands.
Control data
those lovely databases put on the While not all cases involving this kind
internet without controls. Hilarity, no of Sensitive Personal data have been
Data Protection [3]
doubt, ensues once they are found this serious, we urge the custodians
– Establish and Maintain a Data
by whomever might be out looking for of this type of information to be extra
Management Process [3.1]
unprotected gems of data. vigilant in designing their controls to
– Establish and Maintain a Data
help prevent such occurrences.
Finally, the data types we see affected Inventory [3.2]
by Miscellaneous Errors breaches are – Configure Data Access Control Lists
primarily of the Personal variety. And [3.3]
while this Personal information includes – Enforce Data Retention [3.4]
data points such as date of birth, mailing – Securely Dispose of Data [3.5]
address and other tidbits useful for – Segment Data Processing and
identity theft, we are also seeing some Storage Based on Sensitivity [3.12]
of the more sensitive varieties showing – Deploy a Data Loss Prevention
up to a lesser degree. Solution [3.13]
We have started classifying some data
Secure infrastructure
types as especially sensitive, hence the
Sensitive Personal category in Figure Continuous Vulnerability
66. They would include things such as Management [7]
passports, Social Security numbers – Perform Automated Vulnerability
(or equivalent government IDs) or even Scans of Externally-Exposed
the address where a victim of domestic Enterprise Assets [7.6]
violence can be found and other such
cases where that data point can put Application Software Security [16]
the data victim at increased risk. – Use Standard Hardening
Configuration Templates for
Application Infrastructure [16.7]
– Apply Secure Design Principles in
Application Architectures [16.10]
Train employees
Security Awareness and Skills Training
[14]
– Train Workforce on Data Handling
Best Practices [14.4]
– Train Workforce Members on
Causes of Unintentional Data
Figure 66. Top Data varieties in Exposure [14.5]
Miscellaneous Errors breaches (n=1,341)
Application Software Security [16]
– Train Developers in Application
Security Concepts and Secure
Coding [16.9]
Figure 65. Top Assets in Miscellaneous
Errors breaches (n=1,351)
2025 DBIR Incident Classification Patterns 61

Privilege Misuse
Summary The Privilege Misuse pattern tells the
| Frequency | 825 incidents, 757  |     |
| --------- | ------------------- | --- |
story of what occurs when someone is
While the Privilege Misuse pattern is  with confirmed data
hired to do a job and then something
disclosure
typically insiders, this year there has  goes wrong in the employee/employer
been an increase in Partner actors.
Threat actors Internal (90%), Partner  relationship. The reader may be thinking,
Most are motivated by direct financial
|     | (10%), External (3%),  | “Wait! Doesn’t that always happen?”   |
| --- | ---------------------- | ------------------------------------- |
gain, but we also see Espionage in this
|     | Multiple (3%)  | We, of course, have no comment on that.  |
| --- | -------------- | ---------------------------------------- |
pattern; it has decreased over last
|     | (breaches) | What we examine in this pattern are  |
| --- | ---------- | ------------------------------------ |
year’s high.
things such as an employee taking data
Actor motives Financial (89%),  from their employer for their own illicit
Espionage (10%),
financial gain (i.e., by selling it, taking it
What is the same?
|     | Grudge (5%),       | to a competitor or using it to set up a  |
| --- | ------------------ | ---------------------------------------- |
|     | Convenience (2%),  | business for themselves). Or in some     |
The majority of breaches are caused by
|     | Fun (2%), Other (2%),  | cases, doing things such as breaking a  |
| --- | ---------------------- | --------------------------------------- |
Internal actors using their company-
|     | Ideology (1%)  | known corporate policy or procedure by  |
| --- | -------------- | --------------------------------------- |
granted access to steal data.
|             | (breaches)              | using an unauthorized work-around.  |
| ----------- | ----------------------- | ----------------------------------- |
| Data        | Personal (72%), Other   |                                     |
| compromised | (37%), Internal (36%),  | First, the who                      |
Bank (15%) (breaches)
Misuse cases typically involve Internal
actors, but this year, we also saw
an increase in Partner actors doing
disreputable things. This is particularly
interesting since last year (like most
years) they weren’t even on the radar.
Regarding insiders, we saw a
convergence this year between End-
users (rank and file employees) and
System admins who have much higher
levels of data access due to their
job functions (Figure 67). Typically,
System admins are quite low in terms
of committing deliberate actions that
lead to a breach, whereas they figure
rather prominently in terms of accidental
breaches (again due to their privileges).
This rise in System administrator-caused
breaches is concerning, given the scope
of the damage they have the potential
to cause an organization. It begs the
question: Who is watching the watchers?
Would your organization be able to
detect if an employee with elevated
Figure 67. Top Actor varieties in  access went rogue, and exactly what
| Privilege Misuse breaches (n=91) |     | would that look like? |
| -------------------------------- | --- | --------------------- |
2025 DBIR Incident Classification Patterns 62

Then, the why
What exactly drives your trusted
employees to turn on you and start
abusing their access? It is, of course,
different for each person, but we
can see that the two most common
motives are Financial and Espionage
(Figure 68). The Financial motive is
far more common, but we did see a
peak in Espionage-motivated misuse
cases in last year’s report, although
it has since returned to more normal
levels. It is important to keep in mind
that often these motives are not as
far removed from each other as one
might think because in many cases, the
espionage is carried out to ultimately
benefit the bad actor financially.
That said, we did have some interesting
cases come to light this past year with
North Korean workers masquerading
as workers from other countries (who
Figure 68. Top Actor motives in Figure 69. Top Action vectors in
are allowed to work in the U.S.) and Privilege Misuse breaches (n=103) Privilege Misuse breaches (n=153)
funneling data and dollars in support of
their home country.
The movies might have you think it CIS Controls for
“In multiple instances, the conspirators
was during off hours when no one
supplemented their employment
was around to witness the bad actor consideration
earnings by stealing sensitive company
descending with a harness from an
information, such as proprietary source
air duct in the ceiling to photograph
code, and then threatening to leak such
the company’s top-secret research
information unless the employer made Manage access
and development (R&D) plans for their
an extortion payment. Ultimately, the
cutting-edge, anti-gravity propulsion
conspirators used the U.S. and PRC Secure Configuration of Enterprise
mechanism. Sometimes, they would be
[People’s Republic of China] financial Assets and Software [4]
right,102 but often it is simply via LAN
systems to remit the proceeds of – Establish and Maintain a Secure
access. In other words, these bad actors
their activity to accounts in the PRC Configuration Process [4.1]
(employees, contractors and partners)
for the ultimate benefit of the DPRK – Manage Default Accounts
are sitting in their usual places while
[Democratic People’s Republic of North on Enterprise Assets and
nonchalantly taking copies of data they
Korea] government.”101 Software [4.7]
have been granted access to.
However, as Figure 69 illustrates, we Account Management [5]
Finally, the how did witness about one-quarter of these – Disable Dormant Accounts [5.3]
breaches being carried out via Remote – Restrict Administrator Privileges
access. So it isn’t always your Brenda to Dedicated Administrator
Given that we don’t really expect our or Bob from Accounting stealing data Accounts [5.4]
peers to be sitting in the cubicles next instead of playing Space Invaders.
to us blatantly stealing data from the However, as the reader can see, the Access Control Management [6]
company, people are understandably vector ebbs and flows, so sometimes – Establish an Access Granting
curious about how these breaches they really are just playing Solitaire. Process [6.1]
are achieved. – Establish an Access Revoking
Process [6.2]
101. https://www.justice.gov/archives/opa/pr/fourteen-north-korean-nationals-indicted-carrying-out-multi-
year-fraudulent-information
102. And by sometimes, we mean never.
2025 DBIR Incident Classification Patterns 63

Denial of Service
Summary Imagine waking up and checking your
Frequency 6,520 incidents, 2 with
phone only to learn that your cat video
This pattern is one of the consistent confirmed data
social media site is down and your
leaders in the incident patterns, and disclosure
followers are being forced to waste time
the size of the median attack has also
Threat actors External (100%) (all at work in some other manner. While
grown substantially over the years.
incidents) perhaps not as serious as a cat video
While Availability attacks are fairly
outage, downtime can have a serious
common, their impact can be significant
impact on both an organization’s reach
on organizations without mitigation
and their bottom line.
plans in place. The most commonly
targeted industries include Finance, When those outages are caused by the
Manufacturing and Professional deliberate actions of cybercriminals,
Services, accounting for more than they show up here. So, without further
75% of these cases between them. delay, let’s take a look at the DoS
pattern. The largest of these attacks will
have the designation of being a DDoS
attack—where the traffic is coming from
What is the same?
many points on the internet.
This pattern remains a constant threat
This year, the top industry targets of
to the availability of assets. Denial of
DoS are Finance, Manufacturing and
Service is commonly the top incident
Professional Services (Figure 70), with
pattern across the dataset, although it
each accounting for 35%, 28% and 17%
rarely is the cause of data breaches.
of the cases, respectively. These same
This pattern continues to impact a wide
industries have been among the most
variety of different organizations and
frequently targeted sectors for the last
requires close collaboration with
three years and commonly jockey for
different stakeholders to properly plan
the top spot along with the Public Sector
and respond to an attack.
and Information segments.
Figure 70. Top victim industries in DoS
incidents (n=6,520)
2025 DBIR Incident Classification Patterns 64

Figure 71. Distribution over time of PPS in Denial of Service traffic (2018–2024)
Figure 72. Distribution over time of BPS in Denial of Service traffic (2018–2024)
We have been fortunate to have “Teamwork Having those relationships in place
incredible contributors (internal and before an incident occurs can be key to
external) that have stuck with us for makes the weathering any of the DDoS storms you
many years, and that allows us to look may find yourself caught up in. Here’s
at how DDoS attacks have grown over dream work.” another bonus adage for your use:
time. Figure 71 and Figure 72 show “There’s no I in Team, or DDoS
the growth of the median packets per Attacks Mitigation.”103
second (PPS) and bits per second Although a favorite saying of every high
(BPS) along with their 90% confidence school soccer and football coach in
intervals, respectively. What we’ve found the U.S. (and probably elsewhere, but
is that since 2018, there’s been over our sports-coaching sample is U.S.-
200% growth in the median for the size biased), it also applies to defending
and about 1,000% increase in the upper against DDoS. These types of attacks
bounds of the BPS of those attacks. As require a decent amount of planning
one might expect, attackers continue to and coordination with various players,
build up their capabilities to match (or such as your ISP, hosting providers and
exceed) the defenders. internal teams.
103. Before y’all email us to point out our error, we are aware that there are seven I’s in Distributed Denial of
Service Attacks Mitigation, but that’s beside the point.
2025 DBIR Incident Classification Patterns 65

4
Industries
66 2025 Data Breach Investigations Report

Introduction
Welcome to the “Industries” section of the 2025 DBIR! If you are dipping your toes
into the murky water of data breaches for the first time, please think of this as your
road map. If, on the other hand, you are a frequent visitor to this report, you may feel
free to skip ahead, as you most likely already know the way.
As mentioned in the introduction, this year we examined 22,052 security incidents, of
which 12,195 were confirmed data breaches. In this section, we break those incidents
and breaches down and look at them from an industry-specific perspective. As one
might imagine, what one industry wrestles with frequently, another industry may rarely
encounter. The differences between the threats various industries face often come
down to each organization’s unique attack surface.
A multinational financial institution, for instance, may face a different set of threats
than a regional logistics company. However, in many cases, there may also be a
surprising amount of overlap between the two. At the end of the day, as we point out
elsewhere in this report, threat actors appear to care less about an organization’s
size, industry vertical or geographical location than one might think. Today’s
cybercriminal is a bit of a pragmatist and largely subscribes to the “I’ll be happy to
steal whatever you have on hand” view. To really understand this section, you must
also keep in mind other variables, such as the differing reporting requirements that
might exist between industries and the corresponding level of scrutiny that they may
receive, the overall sample size that we have for a given industry and so on. Therefore,
we caution you to keep these and other factors in mind when judging the security
posture of any particular vertical.
Due to a recent re-org of the report, we were forced to make some hard decisions
about the industries we cover, and we now discuss in detail five, rather than the nine
that we examined previously. We appreciate all the contributions that the other four
industries made to this report, and we wish them well in their future endeavors.
If you are here for specific insights that are tailored to your industry,104 we recommend
that you spend time reviewing the top patterns for your industry and then going back
to read up on the relevant pattern sections of the report associated with your vertical.
Speaking of verticals, although we do not have sufficient space, time or, in some
cases, data to examine all industry verticals in depth, we have provided Table 3 on
the next page, which illustrates high-level information on the industries that we do not
touch upon in greater detail. And finally, Public Administration (now “Public Sector”)
has been promoted from this section and is showcased, along with small- to medium-
sized businesses, later in this report (in the “Focused analysis” section).
104. Of course you are. Why else would you be reading this in the first place?
2025 DBIR Industries 67

|     | Incidents |     |     |     | Breaches |     |     |     |
| --- | --------- | --- | --- | --- | -------- | --- | --- | --- |
Industry Total Small (1–1,000) Large (1,000+) Unknown Total Small (1–1,000) Large (1,000+) Unknown
| Total                 | 22,052 | 3,049 | 982 | 18,021 | 12,195 | 2,842 | 751 | 8,602 |
| --------------------- | ------ | ----- | --- | ------ | ------ | ----- | --- | ----- |
| Accommodation (72)    | 211    | 52    | 14  | 145    | 121    | 48    | 11  | 62    |
| Administrative (56)   | 153    | 107   | 8   | 38     | 145    | 106   | 6   | 33    |
| Agriculture (11)      | 80     | 10    | 3   | 67     | 55     | 10    | 2   | 43    |
| Construction (23)     | 307    | 151   | 7   | 149    | 252    | 145   | 4   | 103   |
| Education (61)        | 1,075  | 116   | 90  | 869    | 851    | 106   | 69  | 676   |
| Entertainment (71)    | 493    | 42    | 12  | 439    | 293    | 37    | 12  | 244   |
| Finance (52)          | 3,336  | 175   | 134 | 3,027  | 927    | 162   | 117 | 648   |
| Healthcare (62)       | 1,710  | 115   | 153 | 1,442  | 1,542  | 105   | 132 | 1,305 |
| Information (51)      | 1,589  | 171   | 76  | 1,342  | 784    | 154   | 54  | 576   |
| Management (55)       | 113    | 52    | 3   | 58     | 107    | 52    | 3   | 52    |
| Manufacturing (31–33) | 3,837  | 488   | 74  | 3,275  | 1,607  | 456   | 42  | 1,109 |
| Mining (21)           | 64     | 27    | 4   | 33     | 52     | 27    | 3   | 22    |
| Other Services (81)   | 683    | 87    | 8   | 588    | 583    | 86    | 4   | 493   |
| Professional (54)     | 2,549  | 611   | 95  | 1,843  | 1,147  | 547   | 75  | 525   |
Public Administration (92) 1,422 144 175 1,103 946 124 111 711
| Real Estate (53)       | 339    | 64    | 7   | 268    | 320    | 62    | 6   | 252   |
| ---------------------- | ------ | ----- | --- | ------ | ------ | ----- | --- | ----- |
| Retail (44–45)         | 837    | 170   | 53  | 614    | 419    | 166   | 50  | 203   |
| Transportation (48–49) | 361    | 110   | 32  | 219    | 248    | 103   | 25  | 120   |
| Utilities (22)         | 358    | 27    | 14  | 317    | 213    | 26    | 10  | 177   |
| Wholesale (42)         | 330    | 260   | 11  | 59     | 319    | 256   | 10  | 53    |
| Unknown                | 2,205  | 70    | 9   | 2,126  | 1,264  | 64    | 5   | 1,195 |
| Total                  | 22,052 | 3,049 | 982 | 18,021 | 12,195 | 2,842 | 751 | 8,602 |
Table 3. Number of security incidents and breaches by victim industry and organization size
| 2025 DBIR Industries |     |     |     |     |     |     |     | 68  |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

2025 DBIR Industries 69
nrettaP
noitcA
tessA
Incidents
Figure 73. Incidents by victim industry

2025 DBIR Industries 70
nrettaP
noitcA
tessA
Breaches
Figure 74. Breaches by victim industry

Industry  Frequency Top patterns Threat actors Actor motives Data
(NAICS) compromised
Agriculture (11) 80 incidents, 55  System Intrusion,  External (96%),  Financial (98%),  Internal (67%), Other
with confirmed data  Basic Web  Internal (4%)  Espionage (33%),  (39%), Secrets
disclosure Application  (breaches) Ideology (2%)  (35%) (breaches)
|     | Attacks and Social  |     | (breaches) |     |
| --- | ------------------- | --- | ---------- | --- |
Engineering
represent 96% of
breaches
Administrative (56) 153 incidents, 145  System Intrusion,  External (95%),  Financial (100%)  Internal (83%),
with confirmed data  Social Engineering  Internal (3%),  (breaches) Credentials
| disclosure | and Miscellaneous  | Partner (2%)  |     | (31%), Personal    |
| ---------- | ------------------ | ------------- | --- | ------------------ |
|            | Errors represent   | (breaches)    |     | (10%), Other (8%)  |
|            | 97% of breaches    |               |     | (breaches)         |
Construction (23) 307 incidents, 252  System Intrusion,  External (97%),  Financial (77%),  Internal (77%),
with confirmed data  Social Engineering  Internal (3%)  Espionage (23%)  Credentials (31%),
disclosure and Basic Web  (breaches) (breaches) Other (23%),
|     | Application Attacks  |     |     | Secrets (21%)  |
| --- | -------------------- | --- | --- | -------------- |
|     | represent 96% of     |     |     | (breaches)     |
breaches
Entertainment (71) 493 incidents, 293  System Intrusion,  External (71%),  Financial (97%),  Personal (58%),
with confirmed data  Social Engineering  Internal (29%)  Espionage (18%),  Other (39%), Internal
disclosure and Miscellaneous  (breaches) Ideology (3%), Fun  (32%), Credentials
|     | Errors represent  |     | (1%) (breaches) | (18%) (breaches) |
| --- | ----------------- | --- | --------------- | ---------------- |
76% of breaches
Information (51) 1,589 incidents, 784  System Intrusion,  External (83%),  Financial (78%),  Other (62%), Internal
with confirmed data  Basic Web  Internal (17%),  Espionage (36%),  (51%), Personal
disclosure Application  Partner (1%)  Ideology (1%)  (37%), Secrets
|     | Attacks and Social  | (breaches) | (breaches) | (27%) (breaches) |
| --- | ------------------- | ---------- | ---------- | ---------------- |
Engineering
represent 82% of
breaches
Management (55) 113 incidents, 107  System Intrusion,  External (97%),  Financial (99%),  Internal (95%),
with confirmed data  Social Engineering  Partner (2%),  Espionage (1%)  Credentials
disclosure and Privilege Misuse  Internal (1%)  (breaches) (33%), Medical
|     | represent 99% of  | (breaches) |     | (1%), Personal     |
| --- | ----------------- | ---------- | --- | ------------------ |
|     | breaches          |            |     | (1%), System (1%)  |
(breaches)
Mining + Utilities   422 incidents, 265  System Intrusion,  External (94%),  Financial (75%),  Internal (75%),
(21 + 22) with confirmed data  Social Engineering  Internal (8%),  Espionage (55%),  Secrets (49%),
disclosure and Basic Web  Multiple (2%)  Grudge (1%)  Other (47%)
|     | Application Attacks  | (breaches) | (breaches) | (breaches) |
| --- | -------------------- | ---------- | ---------- | ---------- |
represent 92% of
breaches
Table 4. At-a-glance table for victim industries without a section
2025 DBIR Industries 71

Industry  Frequency Top patterns Threat actors Actor motives Data
(NAICS) compromised
Other Services (81) 683 incidents, 583  System Intrusion,  External (68%),  Financial (69%),  Personal (57%),
with confirmed data  Social Engineering  Internal (33%)  Espionage (31%)  Internal (48%), Other
disclosure and Miscellaneous  (breaches) (breaches) (44%), Secrets (18%)
|     | Errors represent  |     | (breaches) |
| --- | ----------------- | --- | ---------- |
79% of breaches
Professional (54) 2,549 incidents,  System Intrusion,  External (93%),  Financial (88%),  Internal (70%), Other
1,147 with confirmed  Social Engineering  Internal (7%), Partner  Espionage (17%)  (25%), Credentials
data disclosure and Basic Web  (1%) (breaches) (breaches) (24%), Personal
|     | Application Attacks  |     | (24%) (breaches) |
| --- | -------------------- | --- | ---------------- |
represent 91% of
breaches
Real Estate (53) 339 incidents, 320  System Intrusion,  External (64%),  Financial (100%)  Personal (70%),
with confirmed data  Social Engineering  Internal (36%)  (breaches) Internal (40%), Other
| disclosure | and Miscellaneous  | (breaches) | (27%), Bank (17%)  |
| ---------- | ------------------ | ---------- | ------------------ |
|            | Errors represent   |            | (breaches)         |
84% of breaches
Transportation  361 incidents, 248  System Intrusion,  External (94%),  Financial (98%),  Internal (67%), Other
(48–49) with confirmed data  Basic Web  Internal (7%),  Espionage (16%),  (25%), Credentials
disclosure Application  Multiple (2%),  Ideology (1%)  (22%), Personal
Attacks and Social  Partner (1%)  (breaches) (20%) (breaches)
|     | Engineering  | (breaches) |     |
| --- | ------------ | ---------- | --- |
represent 91% of
breaches
Wholesale Trade  330 incidents, 319  System Intrusion,  External (97%),  Financial (100%)  Internal (93%),
(42) with confirmed data  Social Engineering  Internal (3%)  (breaches) Credentials (24%),
disclosure and Privilege Misuse  (breaches) Other (3%), Personal
|     | represent 98% of  |     | (3%), System (3%)  |
| --- | ----------------- | --- | ------------------ |
|     | breaches          |     | (breaches)         |
Table 4. At-a-glance table for victim industries without a section (continued)
2025 DBIR Industries 72

Educational Services
 SCIAN
16
|           |                       | The Educational Services sector is  | When we turn our attention to the  |
| --------- | --------------------- | ----------------------------------- | ---------------------------------- |
| Frequency | 1,075 incidents, 851  |                                     |                                    |
typically a common target for nefarious  actions that threat actors are utilizing
with confirmed data
activity of various sorts. However, this  to compromise educational institutions,
disclosure
year we saw a decrease in the number  Figure 76 shows a good mix of Malware
Top patterns System Intrusion,  of both incidents and breaches that  (42%) and Hacking (36%), as one might
Miscellaneous  occurred in this vertical. This is likely  expect given the fact that System
Errors and Social  less indicative of a drop in enrollment   Intrusion is the number one pattern.
Engineering represent  of threat actors attacking the institutions  The top placement of this pattern also
that educate the populace but instead  means the most prevalent variety of
80% of breaches
represents a change in visibility due to  malware in this industry is Ransomware
| Threat actors | External (62%),  |     |     |
| ------------- | ---------------- | --- | --- |
the makeup of our data contributors   (30%). To complete that narrative, we
Internal (38%)  this year. saw the Use of stolen credentials (24%)
|     | (breaches) |     | at the top of the hacking varieties. |
| --- | ---------- | --- | ------------------------------------ |
Error continues the ever-so-slight
| Actor motives | Financial (88%),  | Seating  |     |
| ------------- | ----------------- | -------- | --- |
upward trend in Educational Services
Espionage (18%)
that we have seen for the last three
|     | (breaches) | assignments |     |
| --- | ---------- | ----------- | --- |
years. Errors accounted for 29% of
| Data  | Personal (58%),  |     | breaches, with the top variety being  |
| ----- | ---------------- | --- | ------------------------------------- |
compromised Internal (49%), Other  Misdelivery at 17%. Finally, bringing up
The System Intrusion, Miscellaneous
|     | (35%), Credentials  |     | the rear, we have Social Engineering at  |
| --- | ------------------- | --- | ---------------------------------------- |
Errors and Social Engineering patterns
|     | (12%) (breaches) |     | 16% of Educational Services breaches.  |
| --- | ---------------- | --- | -------------------------------------- |
are the top three patterns for the third
If we break the Social Engineering
year in a row. Although Miscellaneous
| What is the  | System Intrusion,  |     |     |
| ------------ | ------------------ | --- | --- |
Errors (26%) surpassed Social  breaches down a bit further, we see that
| same? | Miscellaneous  |     |     |
| ----- | -------------- | --- | --- |
77% of that 16% is made up of Phishing
|     | Errors and Social  | Engineering (17%) this year, System  |     |
| --- | ------------------ | ------------------------------------ | --- |
while only 7% is Pretexting.
Intrusion was able to earn top marks
Engineering are still
once again (Figure 75). This likely
the top three patterns,
indicates that the Educational Services
as they have been for
sector is under fire from sophisticated
the last two years.
actors who will complete the extra credit
| Summary |     | assignments required to gain access to  |     |
| ------- | --- | --------------------------------------- | --- |
this industry’s data.
While we saw a decrease in the number
of both incidents and breaches in the
Educational Services industry, the
attacks that we did see were along the
lines of what we have seen in the past.
System Intrusion is far and away the top
pattern, and it is driven by financially
motivated External actors.
Figure 75. Top patterns over time in Educational Services breaches
2025 DBIR Industries 73

These threat actors typically act
with criminal intent, such as stealing
intellectual property from their current
employers to take to their new gigs.
Of those 8% misuse cases, 99% were
Privilege abuse on the part of employees
using the access they were granted to
do their jobs to steal data or perform
some other related misdemeanor.105 Of
course, this means no one is likely to
nominate them for Student of the Month.
Which data
type gets top
marks?
When we look at the kinds of data being
Figure 77. Top Actor types in
compromised in these breaches, we see
Educational Services breaches (n=845)
Personal (58%) and Internal (49%) vying
for the top two spots. In third place is
Figure 76. Top Actions in Educational
Credentials (12%), with Secrets (11%)
Services breaches (n=851)
and Sensitive Personal (10%) crowding
around with very little difference
between them (Figure 79).
The not-so-
stellar pupils
External actors are behind 62% of
the attacks in the Educational Services
vertical (Figure 77), with 59% of those
being Organized crime (Figure 78).
This makes sense when you consider
all the Ransomware and Extortion going
on here. Internal actors also made up
a significant portion of the attacks in
the Educational Services industry at
38%. This can mainly be attributed
to those careless class clowns who
continue to make mistakes of various
types. As in many other industries, their
most frequent faux pas is Misdelivery
(sending something to the wrong
recipient), which accounts for 60% of all
Figure 78. Top Actor varieties in
error-related breaches. Also bolstering
Educational Services breaches (n=658)
the insider numbers, albeit to a much
smaller degree, are the occasional
Internal actors who are guilty of
Misuse (8%).
Figure 79. Top Data varieties in
Educational Services breaches (n=768)
105. Or felony, as the case may be
2025 DBIR Industries 74

Financial and Insurance
2025 DBIR Industries 75
SCIAN
25
This sector has always had a large target Who let the
Frequency 3,336 incidents, 927
painted on its proverbial back, given this
with confirmed data
is where the big money lives. Criminals data out? Who?
disclosure
are incentivized to try and crack open
Top patterns System Intrusion, organizations in this sector for obvious
Social Engineering reasons. And they are successful in With the System Intrusion pattern
and Basic Web causing a breach about a third of the reigning supreme once again this year,
Application Attacks time, according to our frequency table we can assume that the more complex
represent 74% of to the left. Compared to last year, there attacks are getting the adversaries what
breaches are very slight changes to just how many they are after (Figure 80). We saw the
breaches and incidents we saw, but the usual suspects of action types being
Threat actors External (78%), success rate was fairly stable. responsible for breaches this year.
Internal (22%), Partner Hacking was on top, with Malware and
(1%) (breaches) Social trailing after (Figure 81).
Actor motives Financial (90%),
Espionage (12%)
(breaches)
Data Personal (54%), Other
compromised (44%), Internal (35%),
Credentials (22%)
(breaches)
What is the System Intrusion
same? remains the top
pattern once
again, due to the
preponderance
of more complex
attacks. Dare we
hope this is because
Figure 80. Top patterns over time in Financial and Insurance breaches
the adversaries are
having to expend more
effort?
Summary
The Financial and Insurance vertical is
still dominated by financially motivated
threat actors who will usually take any
data type they can lay their hands on.
However, attacks with the motive of
Espionage have increased this year.

Hacking being the top action type is The rest of the top varieties simply
no surprise, since it represents such provide more evidence for the story
a versatile toolset for attackers. We we narrated in our prior paragraph.
see it in System Intrusion breaches, Basic Web Application Attacks tend to
frequently in the form of the exploitation be the smash and grabs of cybercrime,
of vulnerabilities. However, we also see it with the perpetrators getting in and out
after a Social Engineering attack (which of the system as fast as they can. These
is the second most common pattern in are not typically the carefully crafted,
this sector) in which the attacker was well-thought-out schemes you see in
able to gain the credentials of their the movies. Think instead of someone
victim and pivot to use them in attacks kicking in a door and making off with the
against the infrastructure. And finally, equivalent of all your small electronics
we frequently see it in the Basic Web and jewelry.
Application Attacks pattern where the
However, there was a change that
adversary is using credentials that were
leans more toward cloak and dagger—
stolen in another breach and sold on the
the motive of Espionage saw a small
dark web for reuse. Hacking truly is the
increase from 5% last year to 12% in this
gift that keeps on giving. Figure 81. Top Actions in Financial and
year’s report. Admittedly, this is not a
Insurance breaches (n=927)
With regard to the action varieties, huge increase, but it does raise the flag
Figure 82 shows that Ransomware that this industry is drawing the attention
and Use of stolen credentials are the of the more sophisticated threat actors,
powerhouses for most of the breaches which is never good news. It may also be
in this sector. The groups that prefer to in part due to our increased visibility into
efficiently monetize their data access Espionage breaches with the change in
will frequently use Ransomware for the composition of our data contributors.
leverage and will often also take a
copy of the data, frequently using
stolen credentials as an entry point.
Figure 82. Top Action varieties in
Financial and Insurance breaches
(n=823)
2025 DBIR Industries 76

Healthcare
2025 DBIR Industries 77
SCIAN
26
The Healthcare industry remains a However, we have seen System Intrusion
Frequency 1,710 incidents, 1,542
favorite target of attackers, and this year surge ahead this year (Figure 83)—
with confirmed data
we saw a small uptick in both incidents and, again, keep in mind this is where
disclosure
and breaches. This is not surprising, ransomware attacks live. Healthcare
Top patterns System Intrusion, given that reporting requirements can continues to be a favorite target for this
Everything Else and be particularly stringent for healthcare kind of attacker, and the urgent need for
Miscellaneous Errors breaches in the U.S. Therefore, hoping access to data in emergency situations
represent 74% of to fly under the radar is not a good only adds to the pressure healthcare
breaches strategy for organizations in this sector. organizations feel when their systems
are all unavailable and they must resort
Threat actors External (67%), to more old-school processes.
Internal (30%), Partner Time for
(4%), Multiple (1%)
(breaches) a change
Actor motives Financial (90%),
Espionage (16%) We did see some changes in the top
(breaches) patterns this year. If you are a regular
reader of our report, you may recall
Data Medical (45%),
that Miscellaneous Errors was in the
compromised Personal (40%),
top spot in 2024.
Internal (32%), Other
(24%) (breaches)
What is the The attack patterns
same? remain the same,
although they have
changed position
since last year.
Summary
The Healthcare sector remains a
prime target for cyberattacks and
shows a slight increase in incidents
and breaches this year. System Intrusion
(including Ransomware) has overtaken
Miscellaneous Errors as the top cause
of breaches. The rise of Espionage as
a motive for attackers in this sector Figure 83. Top patterns over time in Healthcare breaches
is concerning.

Are you a help That was not When we look at the motivation of these
attackers, we were surprised to see
or a hindrance? how I planned it. Espionage jump from just 1% in last
year’s report to 16%. This may mean
the industry is being targeted by a new
And if having your own systems at risk People making mistakes, as in our kind of threat actor—one often not as
isn’t bad enough, you also need to Miscellaneous Errors pattern, are easily detected as, say, that ransomware
contend with the risks of your entire still prevalent. While it is difficult actor who leaves chaos in their wake.
supplier/partner infrastructure. These to keep this from happening at However, it may also be an indication
third-party breaches impacted a huge all, we strongly recommend the of the changes to our data contributors
number of organizations and patients introduction of mitigating controls over time.
and made headlines all year long. When to at least catch those mistakes
One glaring change worth noting was
we look at notable publicly disclosed as quickly as possible—hopefully
the Everything Else pattern gaining
data breach incidents that affected before a full-blown breach occurs.
ascendency into the top three patterns.
Healthcare this year, the partner angle is
Over the past several years, insider This pattern is our Island of Misfit
right out in front. Attackers clearly don’t
Privilege Misuse breaches have been Breaches, where the cases that have
have any ethical qualms about deploying
decreasing, and though they enjoyed little information end up. They don’t have
their tools against not only healthcare
a small increase last year, they are in the level of detail to go into one of the
providers but also the companies they
the fourth place slot this year. These other patterns—and many of those in
rely upon to get their jobs done. Those
breaches can be hard to discover, this industry came from general breach
notable breach cases affected radiology
and we have seen many instances of notification letters and announcements.
service providers, pharmaceutical firms,
insiders misusing their access for years While that data can be useful for
IT providers, medical transportation
before they are caught. Remember, getting a broad idea of what is causing
firms and pharmacies—including ones
these are not always the snooping, the breaches in this industry, the lack
whose patients are already facing
curious employees who want to know of detail really hinders classification.
end-of-life diagnoses. These high-
what their neighbors are experiencing. In a perfect world, we would see
profile Partner breaches have caught
In this industry, more than most, we more information about what caused
some organizations flat-footed as
tend to see a small number of collusion breaches and what can be done about
the downstream victims. Whether it
cases—where multiple kinds of Actors them when companies issue breach
is the data of their patients that are
are involved in a single breach. The notifications, or maybe even from more
compromised or the access to their
good news is that the number is low robust information sharing practices in
systems (or both), organizations need to
again this year at only 1%. There was this industry.
include “what happens if this partner is
a time when we saw people recruited
attacked” in their planning scenarios.
by External actors to get jobs in the
industry with the express purpose
to subsequently steal the data they
were granted access to in order to do
their jobs. We are happy to see these
days have not returned thus far.
2025 DBIR Industries 78

Manufacturing
2025 DBIR Industries 79
SCIAN 33–13
The Manufacturing industry experienced The pattern is
Frequency 3,837 incidents, 1,607
a relatively stark rise with regard to
with confirmed data
number of breaches this year, with 1,607 becoming clear.
disclosure
confirmed data breaches as opposed to
Top patterns System Intrusion, only 849 last year.
Social Engineering But while we are on the subject of
Although the majority of threat actors
and Basic Web changes, let’s take a look at what hasn’t
we see targeting this vertical continue
Application Attacks changed. The top three patterns in
to be financially motivated External
represent 85% of this industry have not changed over
actors (87%), it is quite interesting
breaches the last year. At 60% of breaches,
that approximately one-fifth (20%) of
System Intrusion is still firmly on top
Manufacturing breaches had the motive
Threat actors External (86%), and appears more than twice as often
of Espionage (compared to only 3% last
Internal (14%) as Social Engineering, which holds the
year). Although it is tempting to conclude
(breaches) number two position at 22% (Figure
that state-sponsored actors are
84). Basic Web Application Attacks
Actor motives Financial (87%), clamoring to steal exotic technologies is at number three but barely makes
Espionage (20%) used to manufacture components for a showing (9%) when compared to
(breaches) aerospace and other military industrial the top two. What does this mean for
complex applications106 (and there
members of this sector? They are
Data Internal (64%), Other can be little doubt that they are), this
likely increasingly being targeted by
compromised (37%), Personal (33%), upswing is most likely due to changes in
more sophisticated threat actors who
Credentials (22%) our contributors’ datasets.
are willing to go the extra mile to gain
(breaches)
access to their victims’ environments.
What is the System Intrusion,
same? Social Engineering
and Basic Web
Application Attacks
are still the top three
patterns, with the
majority of attacks
continuing to come
from financially
motivated External
actors.
Summary
This year, 1 in 5 breaches were due
to Espionage-motivated actors as
compared to last year’s 3%. Internal
(sensitive plans, reports, email) is, Figure 84. Top patterns over time in Manufacturing breaches
by far, the most commonly stolen
data type. And more than 90% of
breached organizations were SMBs
with fewer than 1,000 employees.
106. Like the Illudium Q-36 Explosive Space Modulator favored by Marvin the Martian

Figure 87. Victim size in Manufacturing
breaches (n=498)
Figure 85. Top Action varieties in Figure 86. Top Data varieties in
Manufacturing breaches (n=1,540) Manufacturing breaches (n=1,518)
One notable change, however, is that When we take a look at Figure 86, we
the presence of the Malware action in see what type of data criminals are
Manufacturing breaches has risen to taking. Internal (sensitive plans, reports,
66% this year. For the last five years, email) is, by far, the most commonly
it has remained relatively steady at stolen, followed by Personal data.
between 40% and 50%. It will come Credentials and Secrets data varieties
as no surprise to many of you that appear with roughly equal frequency.
Ransomware (47%) looms large in this
Finally, turning our attention to victim
picture, as it does in most every other
organization size (Figure 87), more than
industry. Hacking via the Use of stolen
90% of breached organizations were
credentials shows up in more than one-
SMBs with fewer than 1,000 employees.
third (34%) of Manufacturing breaches,
This really illustrates that there is no
while Exploit vuln (23%) and Phishing
such thing as a business so small it can
(19%) both appear in approximately one-
fly under the radar of the threat actors.
quarter and one-fifth, respectively, of all
They are the great equalizers when it
breaches in this vertical (Figure 85).
comes to causing breaches.
2025 DBIR Industries 80

Retail
2025 DBIR Industries 81
SCIAN 54–44
While many of us enjoy indulging in We take a good look at the Magecart
Frequency 837 incidents, 419
some good old fashioned retail therapy, breaches that frequently plague this
with confirmed data
there are a number of people who also industry in our “System Intrusion”
disclosure
enjoy browsing through this industry’s section, so if you want more in-depth
Top patterns System Intrusion, data. Unlike a shoplifter who steals the detail, head over there and take a look.
Social Engineering latest viral-on-social-media outfit, these
This industry did see a small uptick
and Basic Web Actors are less trendy and often go after
in the number of incidents and
Application Attacks the data they can most easily access.
breaches—on par with the increased
represent 93% of Payment card data used to be frequently
overall numbers in our dataset this year.
breaches targeted in this industry, as one might
Although we normally see most of the
expect, but surprisingly enough, rather
actors who target this sector having a
Threat actors External (96%), than seeing adversaries calmly strolling
Financial motive, we saw the Espionage
Internal (3%), Partner out the door with their pockets stuffed
motive increase from a negligible 1%
(1%) (breaches) full of credit card info, we instead see
in last year’s report to a surprising 9%
them going for other data types. Is
Actor motives Financial (100%), this year. However, as noted in several
this because the credit card info has
Espionage (9%) other sections, our data contributors
become so well protected that they go
(breaches) have changed, and we are most likely
for an easier target while they have the
benefitting from increased visibility of
access? Sadly, we do not get the “why”
Data Internal (65%), Other this kind of threat actor. Along with a
in our data, only the “what.” But it does
compromised (30%), Credentials focus on protecting the payment data,
make us wonder.
(26%), Payment (12%) defenders need to realize that they
(breaches) may be targeted by somewhat more
sophisticated (and harder to detect)
What is the The top three patterns Actors, as well.
same? in this industry have
not changed from last
year—neither their
membership nor their
order.
Summary
The Retail industry has seen an increase
in cyber incidents, though the focus has
shifted from Payment card data to other
data types that are easier to access.
There was a notable rise in Espionage-
motivated attacks as compared to last
year. Defenders should be aware of
more sophisticated and harder-to-
detect threats.
Figure 88. Top patterns over time in Retail breaches

As for our top three patterns, this year
shows absolutely no change—not in
the makeup of the top three or even
what order they rank (Figure 88). And
as far as threats go, it seems you will
just be facing more of it in the future.
The System Intrusion pattern is typically
where the more sophisticated attacks
land. Ransomware actors fall into this
pattern—ransomware is a problem
across all industries and is only getting
worse. Social Engineering in the second
spot means you need to make sure
your people know how to spot and
appropriately respond to the phishing
and pretexting lures they will receive.
Controls to stop the attacks from being
successful even when the victim falls
for the bait should also be a priority.
And finally, the Basic Web Application
Attacks pattern shows us that the
simple attacks seem to still work just
fine. Those attacks are largely about
credentials and their reuse. It seems to
be human nature to reuse a password
across multiple sites, and since many
of them use an email address for the
login, the combination is very useful
for criminals in many other places.
2025 DBIR Industries 82

5
Focused
analysis
83 2025 Data Breach Investigations Report

Introduction
The process of writing the DBIR is a demanding one, and as a team, we rarely get a
chance to step back and do more in-depth research into the areas that capture our
interest.107 This year, we decided to treat ourselves and dive a bit deeper into two
topics: We always enjoy revisiting the differences in how small and large organizations
experience cyber events, and we wanted to give some more detail into the huge topic
of Public Sector breaches. While we love all of the industries equally, it is hard not to
see how the government of any country has a wider and more complex attack profile
than any other single industry. We hope these two special focus areas spark joy with
our readers as well.108
107. Which are primarily video games
108. If not, then feel free to Marie Kondo them out of here.
2025 DBIR Focused analysis 84

Small- and medium-
sized businesses
One of the more common questions we get here on the DBIR team is “How does Ransomware forced a movement away
the threat landscape differ for large organizations versus small- and medium- from the question of “What price can
sized businesses?” It is a fair question and an interesting one, but it is not always I get for my victims’ data on the open
particularly easy to answer. Several years ago, we examined both and compared market?” to “What is my victim willing
the results to ascertain how similar (or dissimilar) the attack surface of each might to pay to maintain access to their
be to the other. The results from the first analysis in 2013 indicated that there were own data?” This new approach to the
significant differences between the two. The threat landscape for an enterprise with monetization of data was typically
more than 100,000 employees and billions of dollars annually in revenue simply did simpler, easier and more effective for the
not look the same as the landscape for the proverbial Mom and Pop grocery store or criminal, and it further contributed to the
even a moderately sized regional operation. widening of potential targets because
the methods employed are similar
In 2020, in part due to requests from our readers and also due to our own curiosity,
regardless of victim size. This year, we
we revisited the same analysis to determine whether that was still the case or
decided to take another look and see
if the situation had altered. What we found was that there was much more of a
how things currently stand. Let’s jump in
convergence with regard to the threat landscape, regardless of organizational size.
to the results, but before we do (spoiler
As we mentioned at the time, perhaps foremost among the factors contributing to
alert!), it’s mostly bad news for SMBs.
this convergence was that both large and small organizations were increasingly
relying on similar solutions to protect their infrastructures. Along with this reliance
upon the same toolbox came the continued rise of Extortion-based attacks, such as
Ransomware, which proved to be a game-changer for companies of any size.
Organization Frequency Top patterns Threat actors Actor motives Data
size compromised
Small businesses 3,049 incidents, System Intrusion, External (98%), Financial (99%) Internal (83%),
(fewer than 1,000 2,842 with Social Engineering Internal (2%), (breaches) Credentials (34%),
employees) confirmed data and Basic Web Partner (1%) Other (6%),
disclosure Application Attacks (breaches) Personal (4%)
represent 96% of (breaches)
breaches
Large businesses 982 incidents, 751 System Intrusion, External (75%), Financial (95%), Personal (50%),
(more than 1,000 with confirmed data Basic Web Internal (25%), Espionage (3%), Other (36%),
employees) disclosure Application Attacks Partner (1%), Ideology (1%) Credentials (29%),
and Miscellaneous Multiple (1%) (breaches) Internal (29%)
Errors represent (breaches) (breaches)
79% of breaches
Table 5. At-a-glance table by organization size
2025 DBIR Focused analysis 85

The first thing that is readily apparent
is that there are almost four times the
number of SMB victims than there are
large organizations. This increased
difference makes sense due in part
to the simple fact that there are more
SMBs doing business than there are
large organizations. It may also be,
to some degree, a byproduct of our
contributor bias. It does seem like a
rather intuitive finding, though, even
if it is not a finding that is particularly
encouraging if you are an SMB.
FPO
When we examine the most common
action varieties, we see that the
primary hacking variety for both is the
Use of stolen credentials, at 32% in
large organizations and 33% in SMBs.
Leveraging stolen credentials has
been one of the common ways into Figure 89. Top Action varieties by victim
an organization for the last several organization size (n=645)
years. Clearly, while these numbers are
almost identical for both, the same likely
In addition to being terribly dispiriting
cannot be said for the security posture
for SMBs, this finding goes a long
nor the security budget of an SMB
way toward refuting the common
versus the average large organization.
misconception that ransomware groups Figure 90. Top Actions by victim
Unfortunately, the adage “If you can’t run
are only targeting large organizations organization size (n=751)
with the big dogs, stay on the porch” is
and not bothering with the small fries.
less than helpful if you cannot actually
In fact, the data indicates the exact
remain on the porch because you still In fact, when we engage with large
opposite scenario. In brief, ransomware
have to run your business.109 companies who have very mature
groups don’t seem to care what size an
security programs that leverage VERIS
Not all findings are similar, though. organization is; they are quite happy to
for their internal incident records and
For instance, Figure 89 illustrates that breach smaller organizations and adjust
risk modeling,110 they often tell us how
there is a stark difference with regard to their ransom demands accordingly. It
much their numbers are skewed toward
the amount of malware seen between is simply a bonus for the attacker that
Error actions, and their leadership
the two and, in particular, the frequency SMBs are less likely to have up-to-date
will often pressure them to get those
of the Ransomware variety. Whereas and readily available backups than a
percentages down. But if those
large orgs see Ransomware only large organization.
percentages are up, it is because
comprising 39% of the breaches, SMBs
Meanwhile, Figure 90 provides a little actions that are potentially much worse
are experiencing Ransomware-related
good news for SMBs in that while Errors are trending down, such as Hacking,
breaches to the tune of 88% overall.
account for almost one in five (18%) Malware and Social.
Speaking of adages, “When it rains, it
breaches in large organizations, they are
pours” comes immediately to mind. Social attacks, on the other hand,
merely a footnote for SMBs at 1%. Sure,
account for roughly similar percentages
there are fewer people in SMBs to make
for SMBs (18%) and large organizations
those mistakes, but the amount being
(13%) and are almost exclusively of the
smaller can actually be a mixed blessing
Phishing variety. However, Pretexting
when you notice how big that Malware
attacks are more common in SMBs than
bar in the figure is.
in large organizations.
109. With the possible exception of SMBs that build and sell porches
110. This could be your organization! What are you waiting for? Adopt the VERIS framework! It can’t
make your security program mature overnight, but whatever challenges you face today could be very
neatly organized.
2025 DBIR Focused analysis 86

The mouse Who is to
that roared blame?
A reasonable question might be “Ok, As Figure 91 illustrates, the majority
so SMBs may be vulnerable, but surely of actors for both large and small
the impact of a breach of an SMB is, by companies continue to be primarily
nature, considerably less than for a large financially motivated external actors
organization, right?” Wrong. May we of the Organized crime variety. In most
direct your attention to the calamitous cases, when you see organized crime,
fiasco of the National Public Data you may safely assume ransomware was
breach111 that occurred in 2024. The involved. Also, as mentioned previously,
company, which aggregated data for large organizations have a smattering
use in background checks, was of Internal actors committing Error or
breached, and 2.9 billion records were Misuse breaches, while these are very
put up for sale (including Social Security rare in SMBs. Finally, we see Nation-
numbers, dates of birth and addresses) state actors are rarely targeting the
on the dark web containing information SMBs of the world, which at least lets
of citizens of the U.S., Canada and the us end this section on a positive note.
U.K. This was good news to the threat
actors and vendors offering credit
monitoring services. But this breach
illustrates perfectly the type of outsized
damage that an organization with
literally a handful of employees112 can
cause to the data victims affected. Figure 91. Top Actor varieties by victim
organization size (n=494)
111. https://www.cyber.nj.gov/Home/Components/News/News/1436/214
112. Estimates appear to range between 1 and 20 employees, but the number was never actually disclosed.
2025 DBIR Focused analysis 87

Public Sector
2025 DBIR Focused analysis 88
SCIAN
29
Where have all One possible explanation for the
Frequency 1,422 incidents, 946
number of breaches remaining close
with confirmed data
the data points to last year’s is simply that some of our
disclosure
other partners had sufficient visibility
Top patterns System Intrusion, gone? into breaches to keep us at or near
Miscellaneous Errors previous levels. Whatever the case, we
and Basic Web assure you that the decreased number
Application Attacks If you’re a regular reader of this report, of incidents does not indicate that
represent 78% of you may have noticed a significant attackers are giving the government (of
breaches change in the number of incidents being any country) a free pass.
reported in this industry from prior
Our top three patterns have seen a
Threat actors External (67%), years. This is largely due to one of our
change from last year (Figure 92).
Internal (33%), Partner reliable data contributors not being able
In first place is the System Intrusion
(1%) (breaches) to participate this year.
pattern, where all the complex attacks
Actor motives Financial (76%), Although we really hope to welcome live (including everyone’s favorite:
Espionage (29%), them back next year, it is interesting to Ransomware). Last year, people in the
Ideology (2%) see that while the number of incidents government making mistakes caused
(breaches) (that violated one of the three tenants of the most breaches, but this year, they’re
the CIA Triad) is considerably lower, the getting compromised through Basic
Data Personal (47%), number of confirmed breaches didn’t Web Application Attacks instead,
compromised Internal (44%), Other change all that much. We’ve said before which almost everyone can agree is
(41%), Secrets (17%) that we get the “what,” but we do not not an improvement.
(breaches) always get the “why” in our data.
What is the This industry
same? continues to
be plagued by
sophisticated
attackers looking to
gain access to the
trove of data collected
by governments about
their constituents.
Though the majority
of breaches were
from External actors,
a significant number
were from Internal
actors making simple
mistakes.
Figure 92. Top patterns over time in Public Sector breaches
Summary
While we show a drop in reported
incidents due to the makeup of
contributors this year, the number of
confirmed breaches remained steady.
This means attackers are not easing up
on government targets. Ransomware
remains a major threat, hitting 30%
of breaches across all levels of
government. Errors remain a persistent
issue, with Misdelivery in the lead.

Mix up
your errors—
it keeps things
interesting.
We had quite the shakeup in order of
ascendance this year, and the pattern
in the number two spot, Miscellaneous
Errors, was at the top of the list in the
2024 report.
Figure 93. Ransomware victims by
government level (n=312) You can see in Figure 94 that the
top error varieties are Misdelivery,
Misconfiguration and Classification
Speaking of Ransomware, it was errors. Misdelivery is a particular
present in 30% of breaches in this problem for entities such as
sector. When we look at our data in governments who do mass mailings to
Figure 93, we see that Actors have been their constituents. When the contents
targeting government organizations and the envelopes get out of sync in
large and small. We see that about 43% such large deliveries, many people
of Ransomware victims represent local end up knowing more about strangers Figure 94. Top Error varieties in Public
governments in the U.S. in locations than they wanted. At least these kinds Sector breaches (n=212)
such as the Southeast and Midwest. of breaches are less likely to result in
Councils are also being targeted across subsequent fraud.
the world, notably in Europe, Middle We understand, data classification can
East and Africa (EMEA). Lest you think Misconfigured datasets are still being sometimes be seen as a very boring art,
county-level governments (which fall into found by security researchers out on but it is necessary. People are making
our Regional category) are immune, we the internet without protective controls. decisions on what uses to put the data
have seen several examples of counties It seems no matter how the vendors to and how it should be handled based
being victimized, as well. It continues configure the defaults, some people will on how it is classified, so missteps can
at the state and federal levels, as well, still manage to turn off the basics for cause major issues for the organization.
and the real story here is that not only convenience’s sake.
are these government entities being A Classification error is when data is
targeted, but they are also the favorite of thought to be of low sensitivity and
certain ransomware gangs. actually is not. We see this in cases
What we are saying here is that in which data is marked as not being
Ransomware is not a problem that is sensitive and, thus, not requiring such
getting smaller in this sector. There is stringent controls, but in reality, the
no real possibility of going unnoticed data was covered by laws requiring data
because your public entity is relatively breach notification, and so we find out
obscure outside of your immediate area. about the breach.
These Actors are out there, and they are
actively searching for soft targets they
can monetize.
2025 DBIR Focused analysis 89

Last place The way
brought a we were:
friend. A five-year
Public Sector
We had a bit of a surprise in the third
place slot for patterns this year. The retrospective
Social Engineering and Basic Web
Application Attacks patterns were too
close to call, so they will have to share Some time ago—well, at least five years
the dubious distinction of third place.113 ago—we started breaking down the
With regard to Social Engineering, Public Sector data in our dataset by
Phishing is the tried-and-true favorite recording which level of government
action variety, but we also saw Prompt the victim belonged to—Federal versus
bombing (Figure 95) newly rising in this State, Local, Territorial or Tribal (SLTT).
year’s data. If you’re not familiar with By doing so, we now have enough data
the term, we only added it to VERIS in to look at how these different entity
2023, and it is the technique of sending sizes are experiencing breaches. We
annoying levels of authentication have provided you with data from the
requests to users in the hopes they will past five years that shows not only
just comply to make them go away.114 how the different levels of government
Is this a case of “if you track it, they organizations experience breaches
Figure 95. Top Social actions in Public
will come”? We aren’t sure, but we did but also what kinds of Actors choose
Sector breaches (n=127)
see a number of cases in which this is to target this space. Certainly we have
the tactic that ultimately succeeded. seen both Federal- and SLTT-targeted
Not only do you have to worry about attacks increase over time, with some
people reusing their passwords (which very prominent ransomware cases
remains a huge problem), but they are wreaking havoc among multiple victims.
also susceptible to this kind of attack on Some of these Actors seem to prefer
your multifactor authentication controls. SLTT targets, in fact. However, the
Prompt bombing has been successful Federal level of government attracts its
in more than 20% of Social attacks own threat actors, which means nobody
this year, so this would be a good thing is immune, and the most you can hope to
to add to your training materials. achieve is to mitigate your most common
actors and the actions they take. Read
Basic Web Application Attacks feature on for help in those areas.
several hacking varieties prominently:
Use of stolen creds at 86%, Exploit
misconfig at 45% and Brute force
at 37%. These attacks frequently
play out very quickly with few steps
required for the attacker to gain access
and abscond with their data prize.
113. Still better than a participation trophy
114. Much like a toddler trying to get their parent’s permission to have a treat
2025 DBIR Focused analysis 90

Federal One finding that immediately jumped Also keep in mind that these do not
out at us is that we have fewer breaches exclude the breaches of non-U.S.
at the Federal level than we do at the governments—while the dataset is
SLTT level. You may be looking at this dominated by the Northern American
Frequency 15,799 incidents, 848 data and wondering “Why is there so regional breaches, it includes breaches
with confirmed data little if this is a five-year retrospective?” reported from any country.
disclosure The answer is simply that sometimes
We also noticed that the top three
our data comes without an indication
patterns for both organizational sizes
Top patterns System Intrusion, Lost of what government level the breached
were not only identical in makeup115
and Stolen Assets and entity was, and because we don’t get
but also in ranked order. Now contrast
Miscellaneous Errors the victim organization’s name (except
this finding with the same graphic for
represent 81% of from the publicly disclosed sources), we
the full Public Sector dataset for this
breaches can’t make that determination. Another
year’s report (Figure 92 on page 92).
factor is that there are far fewer entities
Threat actors External (66%), at the Federal level than there are at Although it does show the same top two
Internal (46%), the regional levels and below. We in the patterns this year, it was not the case
Multiple (11%) U.S. have our federal government, which when you look backwards in time. In a
(breaches) is huge with all its various branches, retrospective view, you can see other
patterns gain ascendancy for a time and
but then you have to factor in the state,
Actor motives Financial (63%), then fall back down. This is expected
county and city levels. The further down
Espionage (33%), variation between this smaller subset
the ladder you go, the more targets
Ideology (5%) of known Federal-level breaches as
there are.
(breaches) compared to all government sector data.
Figure 96 is showing the cases where
Data Personal (66%), we did know the government level of
compromised Other (38%), Internal the victim, and these were at the
(34%), Secrets (13%) Federal level.
(breaches)
Figure 96. Top patterns over time in Federal Public Sector breaches
115. They must frequent Sephora a lot.
2025 DBIR Focused analysis 91

State, Local, While the top three patterns in the SLTT
breaches are similar in makeup,116 we
The Multi-State Information
Territorial and did have more variation in the earlier
Sharing and Analysis Center
years, as shown by the fuzziness of the
(MS-ISAC)117 is a trusted
Tribal (SLTT) potential lines in Figure 97. If you aren’t
cybersecurity resource for
familiar with how to read a spaghetti
more than 18,000 U.S. SLTT
chart, each line represents a potential
governmental organizations
path the data took, and the tighter
and has been around since
the grouping of lines, the higher the
Frequency 2,101 incidents, 1,341 the early 2000s. Part of the
confidence. Back in 2019 and 2020,
with confirmed data cybersecurity resources
there were wider pathways than there
disclosure provided to MS-ISAC members
are as we approach the present day, so
is the Nationwide Cybersecurity
Top patterns Miscellaneous Errors, the data has become easier to estimate
Review (NCSR), which
System Intrusion and with a higher confidence as to accuracy.
helps organizations assess
Basic Web Application Contrast that with the pathways in the
their overall cybersecurity
Attacks represent Federal breaches, and you see there
posture based on the NIST
79% of breaches was a tighter configuration of the data
Cybersecurity Framework. As
even early on in the recording.
part of this assessment, the
Threat actors External (55%),
The true takeaway in this is that even MS-ISAC found that 70% of
Internal (45%), Partner
when we break out the data based on NCSR respondents selected
(1%) (breaches)
how large the attacked entity was, we “Lack of sufficient funding” as
Actor motives Financial (96%), still see the same top three patterns a top security concern and that
Espionage (1%), over time. This highlights the need to 80% of NCSR respondents
Ideology (1%), have your controls (both protective had security staffing of fewer
Convenience (1%) and detective) in place for these three than five. Considering the
(breaches) patterns as a critical path to helping frequent opportunistic and
your organization take care of the data targeted attacks impacting
Data Personal (83%), Other entrusted to it by the constituents SLTT, the limitations in staffing
compromised (29%), Internal (21%), it represents. and budget to defend against
Credentials (12%) attacks can affect all of our
(breaches) private data.
Figure 97. Top patterns over time in SLTT Public Sector breaches
116. They must all watch the same makeup tutorial videos.
117. https://www.cisecurity.org/ms-isac
2025 DBIR Focused analysis 92

Comparative We have some more marked differences
looking at the patterns for the same
analysis time period (Figure 99). While System
Intrusion is a clear favorite for Federal,
Miscellaneous Errors was equally
Figure 98 shows the breakdown of the popular in the SLTT segment. The
action varieties between Federal and contrast between assets being lost and
SLTT over the past five years. You can stolen in the different segments was
see that the Use of stolen credentials is also pronounced.
one of the overall favorite initial access
vectors for both levels of government, but
as we go into the lower bars of the graph,
we do start to see some differences.
Several of these overlap sufficiently to
make it clear they are all favored tools in
the attackers’ collections.
Figure 100. Top Actor motives in
breaches by goverment level
(2020–2025) (n=501)
Finally, take a look at Figure 100,
where we show the motivations of the
attackers. Though we expect Financial
to be the top motive, the prevalence of
Espionage-motivated actors targeting
the Federal level was significant, as
well. It stands to reason that the Actors
would be targeting the highest level of
government more frequently than the
regional or local entities. These actors,
if not directly state-sponsored, are
usually at least somewhat supported
or condoned in their goals of gaining
access to sensitive government data.
Targeting smaller organizations would
be less likely to gain them access to the
Figure 99. Top patterns in breaches by types of data they prefer—namely those
Figure 98. Top Action varieties in
government level (2020–2025) data points useful for espionage on a
breaches by government level (2020–
(n=2,189) grander scale. As mentioned in previous
2025) (n=544)
sections, the uptick in Espionage-
motivated breaches is likely (at least in
part) due to our increased visibility with
the data contributor mix.
2025 DBIR Focused analysis 93

6
Regions
94 2025 Data Breach Investigations Report

Regional analysis
We are often asked how cybercrime differs (or doesn’t) when viewed from one region LAC: Latin America and Caribbean,
of the world to another. In this section, we are excited to again examine cybercrime which consists of breaches in South
from a macro-regional perspective. Our visibility into any given area is influenced by America (005), Central America (013)
regional disclosure laws, our own dataset and where our data contributors conduct and Caribbean (029)
business, to name only a few. If you would like to help feature your area among these
NA: Northern America (021), which
pages, please contact us about becoming a data contributor and encourage your
primarily consists of breaches in the
partners and clients to do the same (contact methods can be found in the “How to
United States and Canada
use this report” section).
Many readers may recognize the at-a-
We define the regions of the world in accordance with the United Nations M49118
glance tables that we place at the top of
standards, which combine the super-region and sub-region of a country together. By
each major section. We have combined
so doing, the regions we will examine are as follows:
them to provide a quick look at how the
APAC: Asia and the Pacific, including Southern Asia (034), South-eastern Asia (035), regions compare to each other with
Central Asia (143), Eastern Asia (030) and Oceania (009) regard to the frequency of incidents, top
patterns and so on.
EMEA: Europe, Middle East and Africa, including Northern Africa (015), Europe (150)
and Eastern Europe (151), and Western Asia (145)
Region Frequency Top patterns Threat actors Actor Data
motives compromised
APAC 2,687 incidents, System Intrusion, Social External (99%), Financial Internal (78%), Other
1,374 with confirmed Engineering and Basic Internal (1%) (83%), (41%), Secrets (33%)
data disclosure Web Application Attacks (breaches) Espionage (breaches)
represent 97% of breaches (34%)
(breaches)
EMEA 9,062 incidents, System Intrusion, External (71%), Financial Internal (62%),
5,321 with confirmed Social Engineering and Internal (29%) (87%), Personal (49%),
data disclosure Miscellaneous Errors (breaches) Espionage Other (37%), Secrets
represent 89% of breaches (18%) (13%) (breaches)
(breaches)
LAC 657 incidents, 413 System Intrusion, Social External (100%), Financial Internal (97%),
with confirmed data Engineering and Basic Partner (1%), (84%), Secrets (27%), Other
disclosure Web Application Attacks Multiple (1%) Espionage (24%) (breaches)
represent 99% of breaches (breaches) (27%)
(breaches)
NA 6,361 incidents, System Intrusion, External (91%), Financial Internal (49%),
2,867 with Everything Else and Social Internal (5%), (95%), Medical (35%),
confirmed data Engineering represent 90% Partner (5%), Espionage Credentials (23%),
disclosure of breaches Multiple (1%) (9%) Other (17%)
(breaches) (breaches) (breaches)
Table 6. At-a-glance table by region
118. https://unstats.un.org/unsd/methodology/m49
2025 DBIR Regions 95

Social actions account for 25% of
breaches in APAC. While paling in
comparison to the malware numbers
mentioned before, one in every four
breaches is still quite a showing. Of
those, 40% of breaches involved
Pretexting, 34% involved Prompt
bombing (a newcomer to the threat
varieties in our dataset) and 26%
involved Phishing.
And who do we think
they are?
The distribution for actors in APAC is
Figure 101. Top patterns over time in APAC breaches
very monochromatic as external actors
make up nearly 100% of the threat
The APAC Meanwhile, the Social Engineering actors targeting this region, with 80%
pattern, which reached 69% of being of the Organized crime variety and
region breaches back in the 2021 DBIR, has 33% State-affiliated actors.
been on a slow but steady decline since Finally, the data types most often
then. This year, it accounts for 20% stolen reflect the two main threats
From thriving metropolises to lush of breaches in APAC. And finally, the facing APAC: Internal (reports, plans
jungles, island paradises to the Basic Web Application Attacks pattern, and emails) that are often favored
vast, remote Outback, APAC has a the third most prominent in this region, by Ransomware actors, along with
phenomenal diversity of awe-inspiring dropped from 26% last year to 11% of Secrets, which are highly sought
landscapes. Likewise, it has a wide array breaches this year. Of course, System after by State-affiliated actors.
of cultures, languages and traditions. Intrusion is the kudzu of cybercrime and
It is also the largest of all the regions it chokes everything else out, so it is not
in the world, with regard to both area surprising that other patterns decreased
and population. Yet, in spite of these as a proportion of the whole.
differences, from a cybersecurity
perspective, we see a great deal
How do they do that?
of uniformity.
Malware increased from 58% last
The System Intrusion pattern dominates
year in APAC to 83% this year, with
the APAC threat landscape by a
Ransomware accounting for 51% of
considerable margin (Figure 101).
breaches (Figure 102). At the same time,
This fact speaks volumes about the
the Hacking action dropped somewhat
sophistication and astounding success
from 76% of breaches last year to 67%
of the attacks that reside in this pattern.
in this report. When we examine the
This year, System Intrusion rose to an
most common action varieties, we see
eye-popping 83% of all breaches from
that the Use of stolen credentials is quite
an already impressive 39% in last year’s
widespread here—as it is in most of the
report. As holding an organization’s data
world. Stolen credentials were present Figure 102. Top Action varieties in
hostage (either by encrypting it or just
APAC breaches (n=1,353)
in 55% of those cases, while Exploit
stealing and threatening to release it)
vuln appears in 37%. This well-known
continues to pay out large dividends, this
combination of hacking via the Use
pattern will likely remain at or near the
of stolen credentials, followed by the
top of not only the Asia/Pacific region
installation of Ransomware is one of the
but also for most of the globe.
main reasons why the System Intrusion
pattern remains so prevalent.
2025 DBIR Regions 96

David Koh Cybersecurity is often likened to a team Beyond our shores, we have made
sport, requiring collaboration and shared substantial contributions toward
responsibility from all stakeholders. Yet, international collaboration on cyber
Commissioner of we seldom view cybersecurity through initiatives, such as the development of
the lens of time. As CSA approaches cyber norms, to foster a multilateral,
Cybersecurity and Chief
its 10th anniversary in 2025, I am rules-based cyberspace.
Executive of the Cyber
reminded of how much cybersecurity
Nonetheless, considerable work lies
Security Agency (CSA) is like running a team marathon. The
ahead in our journey to secure our digital
difference is that there is no clear
of Singapore future. The adoption of cybersecurity
finish line—it is an enduring mission
practices among both the general public
that requires sustained effort from
and organizations in Singapore could be
all stakeholders, to stay ahead of the
better. There also remains a shortage of
ever-evolving cyberthreat landscape.
skilled cybersecurity professionals—a
Since its formation in 2015, CSA has challenge that mirrors global trends—
played a key role in strengthening despite our efforts to grow our cyber
Singapore’s cyber defenses, conceiving talent pipeline. Meanwhile, the threats we
and then implementing the Singapore all face will only continue to grow in scale
Cybersecurity Strategy. We introduced and sophistication. What is at stake is our
and updated Singapore’s cybersecurity public’s trust in the digital domain.
legislation to ensure effective oversight
We are grateful for the collaboration
of our national cybersecurity and
and commitment from all our partners—
supported organizations to better protect
including governments, industries and
themselves against cyberthreats. We
academia—in this team marathon of
also developed cybersecurity standards
securing cyberspace. This journey
and guidelines to help raise the
has remained as invigorating and
cybersecurity baseline of products and
exciting as it was a decade ago. We
services and formed deep partnerships
look forward to further and deeper
with the cybersecurity industry.
partnerships with stakeholders in the
years ahead, as we stride toward a
trusted and resilient cyberspace.
The EMEA
region
The top three patterns in EMEA remain
the same this year as last year. However,
Miscellaneous Errors dropped from an
all-time high point of 36% of breaches
in the 2024 report to 19% of breaches
this year (Figure 103). As we pointed out
last year, the significant rise in Error was
largely attributable to the inclusion of a
dataset from a new data contributor and,
as we suspected it might, it has fallen
to a more manageable level this year.
Figure 103. Top patterns over time in EMEA breaches
System Intrusion increased from 27% of
breaches last year to 53% of breaches
this year. Meanwhile, Social Engineering
decreased negligibly from 24% to 22%.
2025 DBIR Regions 97

This is how we do it.
As Figure 104 illustrates, Malware
accounts for more than half (54%)
of breaches in EMEA this year. In
an utterly unsurprising fashion, it is
most often of the Ransomware (40%)
variety. Meanwhile 39% of breaches
involved hacking actions, usually the
Use of stolen credentials (24%) or the
exploitation of vulnerabilities (16%). The
Social Engineering pattern is in second
place, with Phishing showing up in 19%
of all EMEA breaches.
The usual culprits
External actors account for 71% of the
threat actors we see in EMEA, with
87% of those representing financially
motivated criminals. However, 19%
of external actors were driven by
Espionage. Unlike many other regions,
Internal actors are also reasonably
well represented (29%) in EMEA.
These insiders are mostly composed
of employees committing unintentional
mistakes (19%), such as Misdelivery,
but there was a small number of misuse
cases (8%) as well (almost exclusively
Privilege abuse).
Figure 104. Top actions in EMEA
Figure 105. Incidents and breaches by region
breaches (n=5,321)
2025 DBIR Regions 98

7
Wrap-up
99 2025 Data Breach Investigations Report

This concludes this year’s report.
As always, we hope that you took
something away that you can use
and that it did not prove a cure
for insomnia.
The amount of effort that goes into On behalf of the team, we
producing this report each year is
wish you the very best, and
considerable to say the least, but as we
we hope that you stay safe,
have said before, it is119 a labor of love.
Over the years, you, our readers, have stay out of the headlines and
both challenged and encouraged us. You
stay in touch. Until next year,
have also instilled in us a sincere desire
happy trails!
to improve with each installment of this
report. Many of you have and continue
to reach out to us to offer suggestions
and advice and to share your insights.120
For that, we are truly grateful, and it
is in large part due to your input that
this report does, in fact, get better with
time. Likewise, our contributors who
put in a tremendous amount of effort
and resources each year to share
both their data and their astonishing
skillsets are in large part responsible for
keeping the DBIR relevant and making
it fundamentally better each year. We
sincerely thank you and find it difficult to
adequately express our gratitude.
119. mostly
120. And occasional pet pictures—thanks, we loved them!
2025 DBIR Wrap-up 100

Year in review
January The first month of the new year marked significant cybersecurity threats, including zero-day exploits, critical
vulnerabilities and active campaigns by cybercrime and state-sponsored advanced persistent threats (APTs). A
major focus was the exploitation of zero-day vulnerabilities in popular software and hardware. Ivanti’s Connect
Secure products were targeted by the Chinese APT UTA0178, prompting urgent responses, including mandates from
CISA. Citrix also reported active exploitation of two zero-days affecting NetScaler ADC and Gateway. Other critical
vulnerabilities were rapidly exploited, such as CVE-2024-23897 in Jenkins servers, Fortra’s GoAnywhere MFT and
Atlassian Confluence, stressing the risks of delayed patching. Apple, Cisco and Juniper Networks also faced critical
zero-days, including Apple’s first of the year. Cybercrime groups advanced their tactics, leveraging AI tools for BEC
and malware and exploiting Google OAuth APIs for session hijacking. Ransomware remained a key threat, with
insights on the 8Base group’s operations emerging. Nation-state actors were active, with Iranian (Mint Sandstorm) and
Russian APTs (COLDRIVER/Star Blizzard and Midnight Blizzard) conducting notable campaigns. These developments
underscored the urgent need for timely patching, robust threat intelligence and proactive defenses to counter the
persistent and evolving cyberthreat landscape.
February Ivanti remained a focal point, addressing ongoing attacks on its Connect Secure and Policy Secure products by Chinese
APT UNC5221/UTA0178, which also uncovered two new high-severity vulnerabilities. Russia-aligned APTs targeted
Ukraine with USB-based malware, while defenders scored a rare win by dismantling the Chinese threat actor Volt
Typhoon’s KV Botnet. Fortinet mitigated actively exploited Secure Sockets Layer (SSL) VPN vulnerabilities in FortiOS,
and Microsoft patched 78 vulnerabilities, including three zero-days leveraged by the new cybercrime APT Water Hydra.
Notable intelligence emerged from CrowdStrike and IBM, providing insights into evolving global threat trends. Additional
vulnerabilities surfaced in ConnectWise, VMware, Adobe and Intel products, prompting swift patching efforts. Reports
on the Israeli-Iranian cyber conflict and North Korea’s Kimsuky APT activity underscored the geopolitical complexities
of cyberoperations. Operation Cronos, a joint international law enforcement operation, disrupted the notorious LockBit
ransomware group. The joint operation took control of LockBit’s infrastructure and its affiliate panel and seized
significant information, such as LockBit source code, chats and internal communications; victim details; and decryption
keys. Operation Cronos dealt a significant blow to LockBit’s operations, seizing approximately 2,200 bitcoin and eroding
trust within its affiliate network. However, within days, a new leak site was published with new attacks being claimed,
albeit at a much-reduced capacity.
March Critical flaws in enterprise systems such as Progress Kemp LoadMaster, VMware ESXi, Cisco Secure Client and Fortinet
FortiClient EMS underscored the constant pressure on organizations to maintain up-to-date security infrastructure.
Exploited flaws included newly discovered vulnerabilities in Arcserve’s Unified Data Protection software. APT activity
persisted, with evidence of Russia-linked APT29 (Midnight Blizzard) leveraging previously exfiltrated information from
email systems to gain unauthorized access, showing a tenfold increase since January 2024. China-linked groups
deployed a Linux variant of DinodasRAT, while Iranian and North Korean APTs remained active with evolving tactics.
Cybercriminal campaigns also adapted, including TA577 targeting Windows New Techology LAN Manager (NTLM)
hashes and StrelaStealer malware harvesting email credentials. Urgent updates were announced for JetBrains TeamCity
servers, which faced proof-of-concept exploit code within hours of patch release. A notable campaign targeting VPN
infrastructure through brute force techniques prompted advisories from Verizon. The discovery of trojanized XZ Utils in
Fedora distributions underscored ongoing risks to supply chain integrity. March’s developments reaffirmed the need for
vigilant patching and monitoring of rapidly evolving APT tactics.
April A key focus was the XZ Utils supply chain attack, in which a backdoor introduced through targeted Social Engineering
in 2021 highlighted risks to open-source software. Ivanti’s VPN vulnerabilities remained critical, with organizations
urged to patch flaws in Connect Secure and Policy Secure gateways. Two major breaches dominated the month: CISA
disclosed a Sisense data breach, advising credential resets, while a Duo MFA breach exposed text messaging logs,
further emphasizing the importance of robust authentication. Palo Alto Networks patched a zero-day OS command
injection vulnerability actively exploited in its GlobalProtect firewalls. Midmonth saw Mandiant reclassify Sandworm
Team as APT44, with fresh insights into Russian APT activity. Password-guessing attacks surged, targeting VPN and
SSH interfaces. By month’s end, zero-days in Cisco Adaptive Security Appliance (ASA) firewalls and exploitation of an
older Microsoft print spooler vulnerability by APT28 (Forrest Blizzard) using a previously unknown hacking tool called
GooseEgg. April reinforced the importance of supply chain security and rapid patch management to counter evolving
APT tactics.
2025 DBIR Wrap-up 101

May North Korea’s Moonstone Sleet and Russia’s BlueDelta debuted as new nation-state threats, with Moonstone Sleet
using FakePenny ransomware for cyberespionage and BlueDelta focusing on intelligence operations across Europe
and Asia. Chinese APTs expanded cyberespionage operations to Africa, the Caribbean and the Middle East, with the
refined approach of more carefully selecting its targets and using publicly available tools. Cybercriminal activity also
evolved, with Evil Corp deploying SocGholish malware and FIN7 impersonating trusted brands and using malicious MSIX
files. Zero-day exploitation was a major challenge, including CVE-2024-5274 in Google Chrome’s V8 engine, prompting
five patches throughout the month. Cisco ASA/Firepower Threat Defense (FTD) vulnerabilities were targeted in the
ArcaneDoor campaign, while significant vulnerabilities in F5 BIG-IP and Apache ActiveMQ added to patch management
demands. MITRE Engenuity’s analysis of a 2023 breach provided insights into the China-nexus threat actor’s (UNC5221)
use of using rogue virtual machines created and managed through service accounts directly on the hypervisor rather
than through administrative consoles. The U.S. Department of Justice issued an indictment, charging Russian national
Dmitry Yuryevich Khoroshev (also known as LockBitSupp) with creating and operating LockBit ransomware. The
unsealing of the indictment was accompanied by the U.S. State Department announcing a $10M bounty for information
that leads to Khoroshev’s apprehension. Verizon’s 2024 Data Breach Investigations Report revealed a tripling in
vulnerability exploitation in breaches, linking zero-days to ransomware.
June Chinese APT Crimson Palace launched targeted cyberespionage campaigns, invariably collecting sensitive technical
information, conducting reconnaissance of specific users and accessing critical IT systems. Meanwhile, Russia-linked
APT28 (Forest Blizzard) remained active, using infostealer malware and living-off-the-land techniques. Espionage-
focused ransomware attacks continued to gain prominence, with Recorded Future identifying RedJuliett, a new Beijing-
aligned group targeting Taiwan. Other emerging China-aligned threat actors, such as SneakyChef, targeted government
entities in Asia and EMEA with SugarGh0st malware, while Velvet Ant exploited legacy F5 BIG-IP appliances for
persistence. BlackSuit ransomware actors breached CDK Global, with tactics, techniques and procedures (TTPs)
strongly suggesting it is rebranding of Royal ransomware. Results of investigations into the Snowflake breach also
began to emerge, indicating the threat actors used LummaStealer in its initial access. Critical vulnerabilities required
swift action, including flaws in Fortinet, Juniper Mist Premium Analytics, Progress Telerik and SolarWinds Serv-U. The
MOVEit vulnerability continued to see exploitation attempts, while Atlassian’s Confluence vulnerability saw exploitation
shortly after patch release. June’s developments demonstrated the blurring lines between ransomware and espionage,
highlighting the importance of strong patch management and monitoring APT TTP shifts.
July The open-source JavaScript library project polyfill.io was involved in what was believed to be the largest digital supply
chain attack to date. Polyfill.io was discovered injecting malware and redirecting users to its malicious network of online
gambling and other malicious sites, subjecting hundreds of thousands of users to increased risk. Cisco Nexus switches
faced attacks exploiting vulnerabilities dating back to April, attributed to the Chinese APT Velvet Ant. GootLoader
resumed cybercrime operations after a six-month hiatus, while North Korea’s Kimsuky APT expanded targeting to
Japan. Snowflake’s ongoing breach highlighted risks from compromised credentials, affecting 165 organizations without
MFA enforcement. A faulty software update from CrowdStrike’s Falcon agent caused widespread system failures on
Microsoft Windows devices, impacting critical sectors such as aviation, healthcare and finance. The company issued
patches, faced congressional scrutiny and reported significant quarterly financial losses but retained most of its
customer base.
2025 DBIR Wrap-up 102

August CrowdStrike released a root cause analysis report for the previous month’s massive outage, but adding to its woes, the
company also revealed that spearphishing campaigns exploited its Falcon Sensor outage, distributing Ciro malware
through fake crash report installers. Separately, the hacktivist group USDoD claimed to have leaked CrowdStrike’s
indicators of compromise (IOC) list and threat actor database. Akamai reported successfully mitigating one of the
largest DDoS attacks, blocking more than 419 TB of malicious traffic, and a massive breach at background check firm
National Public Data exposed nearly three billion records. Critical vulnerabilities in ServiceNow’s Now Platform (CVE-
2024-4879 and CVE-2024-5217) led to data breaches, and ransomware groups Akira and Black Basta exploited
an ESXi hypervisor flaw (CVE-2024-37085), driving widespread ransomware deployments. The FBI dismantled the
Dispossessor ransomware group, and CISA flagged RansomHub ransomware, linked to more than 200 attacks since
February. The two agencies also released a joint advisory on Royal ransomware’s rebranding to BlackSuit, detailing
updated tactics and IOCs. Geopolitical cyber activity escalated as Iranian state-sponsored actors combined influence
campaigns and ransomware targeting Healthcare and Financial sectors. Microsoft, Google and the FBI reported details
of various activities by Iranian threat actors targeting the 2024 U.S. presidential election, including attempted hacks
of candidates’ campaigns and influence operations designed to stir up controversy. OpenAI disrupted Iranian-linked
Storm-2035 influence operations leveraging covert propaganda on its platform. Lumen Technologies reported Chinese
APT Volt Typhoon exploiting Versa Director servers (CVE-2024-39717), enabling credential interception and malicious
code injection. VTRAC published a threat intelligence advisory detailing the emerging trend of threat actors using
“violence as a service” in conjunction with their cyberattacks.
September September saw significant developments in cybercrime takedowns, nation-state operations, ransomware tactics and
critical vulnerability exploitation. The U.S. unsealed indictments against two Russian nationals for hacking and fraud
schemes that caused more than $35M in losses, including identity theft and extortion. Separately, a joint FBI, CISA
and National Security Agency (NSA) advisory detailed GRU’s Unit 29155 cyberespionage activities and WhisperGate
attacks targeting Ukraine, which coincided with the unsealing of another indictment naming six Russian officers and one
Russian civilian associated with the GRU unit. Meanwhile, Graphika reported on China’s Spamouflage campaign, which
used fake American personas to spread divisive narratives ahead of U.S. elections. Midmonth, the FBI, enabled by Black
Lotus Labs’ investigation, dismantled the Chinese Flax Typhoon botnet, which comprised more than 200,000 Internet
of Things (IoT) devices under the code name Raptor Train. North Korean actors escalated job-themed phishing attacks
targeting aerospace and IT sectors, even infiltrating organizations via fake hires. KnowBe4 shared its experience in
accidentally hiring one such fake employee, revealing a broader, industrial-scale operation and highlighting the need for
secure hiring and onboarding processes, especially for remote-based employees. Later, law enforcement indicted two
Russian nationals for payment card theft and cryptocurrency laundering. One of the individuals was the alleged operator
of the notorious Joker’s Stash cybercrime marketplace, while the other ran the major money laundering cryptocurrency
exchange, Cryptex. RansomHub ransomware continued targeting critical infrastructure using advanced anti-endpoint
detection and response (EDR) tactics. North Korean APT Kimsuky (Sparkling Pisces) deployed two new malware
variants, KLogEXE and FPSpy. The emergence of LLMjacking, exploiting compromised cloud credentials to abuse large
language models, raised alarms over operational and financial risks.
October Key themes included record-breaking DDoS attacks, nation-state cyberactivity, election security and the persistent
evolution of ransomware and supply chain threats. Early in the month, Cloudflare mitigated a 3.8 Tbps DDoS attack, the
largest on record, driven by compromised ASUS routers and IoT devices. The Gorilla Botnet, a Mirai variant responsible
for 300,000 global attacks in September, continued to target critical infrastructure in the U.S., Canada and Germany
via sophisticated attack vectors. Reports began emerging about a massive cyberespionage campaign conducted by
the Chinese state-sponsored group Salt Typhoon targeting U.S. broadband networks. The sophisticated threat actor
reportedly infiltrated multiple U.S. telecommunication companies, exploited backdoors and stole sensitive data. The
reports subsequently prompted investigations, congressional inquiries and the formation of a Cyber Unified Coordination
Group (UCG) comprising multiple federal agencies to collaborate and coordinate the U.S. response to the attacks. Later
reports, confirmed by White House officials, would indicate the Chinese threat actors had recorded the phone calls of
senior unnamed U.S. political figures. In a win against cyberespionage, the U.S. Department of Justice and Microsoft
seized 100 domains tied to the Federal Security Service of the Russian Federation-backed Star Blizzard group. Efforts
against ransomware intensified, with indictments and sanctions against members of the LockBit ransomware group and
Evil Corp cybercrime organization. Ongoing investigations identified Evil Corp as responsible for $300M in damages.
The emergence of Mamba 2FA, a phishing as a service platform, underscored cybercriminals’ focus on bypassing MFA
in AiTM attacks. Dutch authorities dismantled the Bohemia/Cannabia, a dark web market selling drugs and cybercrime
services with a €12M monthly turnover, and OpenAI disrupted 20 malicious operations exploiting its AI models. China’s
Spamouflage operations tested new tactics against Senator Marco Rubio, and the Brazilian authorities arrested USDoD,
a notorious hacker, while the U.S. Department of Justice indicted two Sudanese nationals tied to Anonymous Sudan’s
35,000 DDoS attacks, which caused $10M in damages. The month concluded with Microsoft’s election security report
revealing disinformation campaigns by Russia, Iran and China targeting the 2024 U.S. elections.
2025 DBIR Wrap-up 103

November Reports of a new version of the FakeCall malware emerged early in the month. FakeCall is an advanced vishing attack
capable of intercepting both inbound and outbound calls as well as controlling infected mobile devices and stealing
sensitive data. Google’s Big Sleep team showcased AI’s potential for identifying flaws, uncovering a serious SQLite
vulnerability, while attackers exploited Docusign APIs to distribute convincing phishing invoices, bypassing traditional
defenses through legitimate platforms. Collaborative international law enforcement efforts led to U.S. authorities
indicting Maxim Rudometov for creating the RedLine infostealer. This coincided with an announcement by the Dutch
National Police that it had gained complete access to the servers behind the RedLine and META infostealers. Russian
national Evgenii Ptitsyn, alleged operator of Phobos ransomware, with more than 1,000 victims and $16M in ransom
payments, was extradited from South Korea to the U.S. Separately, five members of Scattered Spider faced charges
for phishing campaigns targeting corporate data and cryptocurrency. A Microsoft report warned of the Chinese threat
actor Storm-0940 targeting various organizations in North America and Europe, including think tanks, government
organizations, non-governmental organizations, law firms and the defense industrial base. The threat actors were
observed leveraging a covert network of compromised small office and home office routers and other networking
devices, known as CovertNetwork-1658 or Quad7 botnet, to conduct password spray attacks. Storm-0940 would
then steal credentials to gain initial access to the targeted organizations, move laterally within the victim’s networks
and exfiltrate data. SecurityScorecard reported a resurgence of Volt Typhoon, which exploited outdated edge devices
and routers targeting critical infrastructure. As the holiday season approached, cybersecurity risks surged, with fake
online stores increasing by 110%, credit card skimming malware targeting Magento sites and AI-driven phishing attacks
becoming more prevalent.
December The year closed with significant developments in critical vulnerability exploitation, ransomware campaigns and a number
of successes in international efforts against cybercrime. The U.S. Department of Justice charged Rostislav Panev,
a LockBit developer, as LockBit announced its 4.0 version for 2025 and, separately, seized the Rydox marketplace,
targeting 18,000 users involved in cybercrime. The U.S. Department of the Treasury sanctioned Iranian, Russian and
Chinese entities for election interference and critical infrastructure attacks, including Iran’s Cognitive Design Production
Center and Russia’s GRU-affiliated Center for Geopolitical Expertise. Operation Destabilise dismantled Russian money-
laundering networks, leading to 84 arrests and £20M in asset seizures, while Europol’s Operation PowerOFF disrupted
27 DDoS-for-hire platforms, arresting administrators and identifying 300 users. Russia also took rare enforcement
actions, charging Mikhail Matveev (Wazawaka) and sentencing Hydra Market’s leader to life imprisonment. Severe
vulnerabilities were disclosed throughout the month of December, including a directory traversal flaw in Zyxel and a
remote code execution (RCE) vulnerability in Veeam’s Service Provider Console. Cisco highlighted renewed exploitation
of legacy ASA WebVPN vulnerabilities from 2014 and released new patches for NX-OS, while critical flaws in Zabbix and
Microsoft’s partner portal underscored risks to enterprise environments. Midmonth, Zscaler reported a Zloader variant
linked to Black Basta ransomware, employing Domain Name System (DNS) tunneling for stealthy command and control,
and advanced evasion tactics were seen in a Nova Snake Keylogger variant analyzed by ANY.RUN. Critical vulnerabilities
emerged in Amazon Web Services (AWS) RedShift, Apache deserialization flaws and Progress WhatsUp Gold, affecting
more than 110,000 servers. Meanwhile, Juniper and Citrix appliances faced exploitation via default credentials and
password spraying. And in late December, ransomware and extortion group Cl0p exploited vulnerabilities in Cleo’s file
transfer tools, attacking more than 60 organizations, and threatened to release the full names of the victims unless a
ransom was paid.
2025 DBIR Wrap-up 104

8
Appendices
105 2025 Data Breach Investigations Report

Appendix A:
Methodology
One of the things readers value most about this report is the level of rigor and All contributors received instruction to
integrity we employ when collecting, analyzing and presenting data. Knowing our omit any information that might identify
readership cares about such things and consumes this information with a keen eye organizations or individuals involved.
helps keep us honest. Detailing our methods is an important part of that honesty.
Some source spreadsheets are
To begin with, we would like to remind our readers that science comes in two flavors: converted to our standard spreadsheet
creative exploration and causal hypothesis testing. The DBIR is squarely in the former. formatted through automated mapping
While we may not be perfect, we believe we provide the best obtainable version of to ensure consistent conversion.
the truth based on the datasets we have available (to a given level of confidence Reviewed spreadsheets and VERIS
and under the influence of biases acknowledged later). However, proving causality Webapp JSON are ingested by an
is best left to randomized control trials. The best we can do is correlation. And while automated workflow that converts the
correlation is not causation, they are often related to some extent, and often useful. incidents and breaches within into the
VERIS JSON format as necessary,
adds missing enumerations, and then
Non-committal disclaimer validates the record against business
logic and the VERIS schema. The
automated workflow subsets the data
We would like to reiterate that we make no claim that the findings of this report are and analyzes the results. Based on the
representative of all data breaches in all organizations at all times. Even though we results of this exploratory analysis, the
believe the combined records from all our contributors more closely reflect reality validation logs from the workflow and
than any of them in isolation, it is still a sample. And although we believe many of discussions with the partners providing
the findings presented in this report to be appropriate for generalization (and our the data, the data is cleaned and
conviction in this grows as we gather more data and compare it to that of others), reanalyzed. This process runs nightly for
bias still exists. roughly two months as data is collected
and analyzed.
The DBIR process
Our overall process remains intact and largely unchanged from previous years.121
All incidents included in this report were reviewed and converted (if necessary) into
the VERIS framework to create a common, anonymous aggregate dataset. If you are
unfamiliar with the VERIS framework, it is short for Vocabulary for Event Recording
and Incident Sharing, it is free to use, and links to VERIS resources can be found
throughout this report.
The collection method and conversion techniques differed among contributors. In
general, three basic methods (expounded below) were used to accomplish this:
1. Direct recording of paid external forensic investigations and related intelligence
operations conducted by Verizon using the VERIS Webapp
2. Direct recording by partners using VERIS
3. Converting partners’ existing schema into VERIS
121. As does this sentence
2025 DBIR Appendices 106

Incident data We make liberal use of confidence We create a subset of incidents that
intervals to allow us to analyze smaller pass our quality filter. The details of
sample sizes. We have adopted a few what is a “quality” incident are:
Our data is non-exclusively multinomial, rules to help minimize bias in reading
• The incident must have at least seven
meaning that a single feature, such as such data. Here we define “small
enumerations (e.g., threat actor
“Action,” can have multiple values (e.g., sample” as fewer than 30 samples.
variety, threat action category, variety
“Social,” “Malware” and “Hacking”).
1. Sample sizes smaller than five are too of integrity loss) across 34 fields OR
This means that percentages do
small to analyze. be a DDoS attack. Exceptions are
not necessarily add up to 100%.
given to confirmed data breaches with
For example, if there are five botnet 2. We won’t talk about count or
fewer than seven enumerations.
breaches, the sample size is five. percentage for small samples. This
However, because each botnet used goes for figures, too, and is why some • The incident must have at least one
phishing, installed keyloggers and used figures lack the dot for the median known VERIS threat action category
stolen credentials, there would be five frequency. (e.g., Hacking, Malware).
Social actions, five Hacking actions and
3. For small samples, we may talk about In addition to having the level of details
five Malware actions, adding up
the value being in some range or necessary to pass the quality filter, the
to 300%. This is normal, expected
values being greater/less than each incident must be within the timeframe of
and handled correctly in our analysis
other. These all follow the confidence analysis (Nov 1, 2023, to Oct 31, 2024,
and tooling.
interval approaches listed previously. for this report). The 2024 caseload
Another important point is that when is the primary analytical focus of the
looking at the findings, “unknown” is report, but the entire range of data
equivalent to “unmeasured.” Which is Incident is referenced throughout, notably
to say that if a record (or collection of in trending graphs. We also exclude
records) contains elements that have eligibility incidents and breaches affecting
been marked as “unknown” (whether it individuals that cannot be tied to an
is something as basic as the number of organizational attribute loss. If your
records involved in the incident or as For a potential entry to be eligible for friend’s laptop was hit with ransomware
complex as what specific capabilities a the incident/breach corpus, a few while downloading a game cheat, it
piece of malware contained), it means requirements must be met. The entry would not be included in this report.
that we cannot make statements about must be a confirmed security incident
Lastly, for something to be eligible for
that particular element as it stands in the defined as a loss of confidentiality,
inclusion into the DBIR, we have to know
record—we cannot measure where we integrity or availability. In addition to
about it, which brings us to several
have too little information. Because they meeting the baseline definition of
potential biases we will discuss on the
are unmeasured, they are not counted in “security incident,” the entry is
next page.
sample sizes. The enumeration “Other,” assessed for quality.
however, is counted because it means
that the value was known but not part
of VERIS (or not one of the other bars
if found in a bar chart). Finally, “Not
Applicable” (normally “n/a”) may be
counted or not counted depending on
the claim being analyzed.
2025 DBIR Appendices 107

Acknowledge- The second source of bias is sampling Non-incident
bias. We strive for “the best obtainable
ment and version of the truth” by collecting data
breaches from a wide variety of
analysis of bias contributors. Still, it is clear that we
conduct biased sampling. For instance, Since the 2015 issue, the DBIR has
some breaches, such as those publicly included data that requires analysis that
Many breaches go unreported (though disclosed, are more likely to enter does not fit into our usual categories
our sample does contain some of those, our corpus, while others, such as of “incident” or “breach.” Examples
as well). Many more are as yet unknown classified breaches, are less likely. of non-incident data include malware,
by the victim (and thereby unknown to We also acknowledge that some types vulnerability management, phishing,
us). Therefore, until we (or someone) of breaches that are very common in DDoS, internet-wide honeypots, internet-
can conduct an exhaustive census of a specific analysis period—looking wide scanning and other types of data.
every breach that happens in the entire at you, Ransomware—might end up The sample sizes for non-incident
world each year (our study population), being overrepresented due to the vast data tend to be much larger than the
we must use sampling. Unfortunately, availability of samples. We often try to incident data but from fewer sources.
this process introduces bias. point it out in the report when that is We make every effort to normalize the
the case. data (for example, weighting records
The first type of bias is random
by the number contributed from the
bias introduced by sampling. This The third source of bias is confirmation
organization so all organizations are
year, our maximum confidence is bias. Because we use our entire dataset
represented equally). We also attempt
+/- 0.7% for incidents and +/- 0.9% for exploratory analysis, we cannot test
to combine multiple partners with
for breaches, which is related to our specific hypotheses. Until we develop
similar data to conduct the analysis
sample size. Any subset with a smaller a collection method for data breaches
wherever possible. Once analysis is
sample size is going to have a wider beyond a sample of convenience, this is
complete, we try to discuss our findings
confidence margin. We’ve expressed probably the best that can be done.
with the relevant partner or partners
this confidence in the complementary
As stated earlier, we attempt to mitigate so as to validate the findings against
cumulative density (slanted) bar charts,
these biases by collecting data from their knowledge of the data and make
hypothetical outcome plot (spaghetti)
diverse contributors. We follow a sure we are representing it correctly.
line charts and quantile dot plots.
consistent multiple-review process and
However, sometimes the nature of non-
when we hear hooves, we think horses,
incident data we may be working with is
not zebras.122 We also try and review
not conducive to this confidence level
findings with subject matter experts in
analysis, and we might have some plain
the specific areas ahead of release.
vanilla bar and line charts throughout
the report. More on non-incident data in
the next section.
122. A unique finding is more likely to be something mundane, such as a data collection issue, than an
unexpected result.
2025 DBIR Appendices 108

Appendix B:
U.S. Secret Service
Partnering to Cybersecurity threats are resulting A threat assessment program involves
in growing economic harm, leading a team focused on identifying,
Disrupt and business leaders to increasingly ask detecting, and analyzing threats and
how to go beyond purely defensive illicit activity related to your operations.
Dismantle measures to disrupting cyber threat Consider how to join together the
actors. For over forty years, the U.S. relevant individuals with roles related
Cyber Threats Secret Service has been working with to loss prevention, security, risk
public and private sector partners for management, cybersecurity, fraud,
precisely this purpose. Based on the anti-money laundering, and related
Secret Service’s experience, to include functions. Develop a case management
By Assistant Director Michael
work done through our Cyber Fraud process for tracking threat actors
Centrella and Program
Task Forces, there are critical roles for throughout their period of activity.
Manager Ronan McGee, the private sector to perform to enable
Empower your threat assessment team
the effective disruption of cyber threats.
United States Secret Service to design and implement controls to
What is effective disruption? Disruption detect suspicious or threating activity.
is a shaping operation, influencing the Critical to this is implementing measures
future activity of a threat actor. Poorly to enhance identity management,
designed disruption operations impose authentication, and access controls
no significant costs on threat actors, related to risky or unusual behaviors.
aids them in improving their operations, The Verizon DBIR, and VERIS dataset,
and potentially emboldens further can help you identify trends in
criminal activity. In contrast, well- cyber threat activity relevant to your
designed disruption operations target businesses and prioritize your efforts
the key capabilities and items of value accordingly. Automated analytics
to threat actors, substantially impairs can greatly enhance the ability of
their threatening activity, deters future organizations to detect and respond to
criminal activity, and is well integrated suspicious activity when systems are
in a joint and sequenced campaign plan properly designed to aggregate various
to achieve the dismantlement of the potential indicators of unusual activity.
threatening organization. As specific threat actors are identified,
engage in lawful activities to understand
Achieving effective disruption is no small
their operations, their motives,
task, requiring a detailed understanding
associates, and locations.
of a threat actors’ operations and what
they value. Businesses can partner
with law enforcement to disrupt
threats by developing a threat
assessment program.
2025 DBIR Appendices 109

Once threats to your organization are Investing in the ability to timely and Several days later, Russian authorities
understood, the next step is to examine appropriately share information announced the arrests of Ivanov and
how to target their operations. Identify with law enforcement is essential to approximately 100 additional co-
what aspects are critical to their illicit disrupting cyber threats. Numerous conspirators. These actions resulted in
activity, what is valued by the threat organizations exist to help businesses dismantling one of the most significant
actor, and what could be disrupted to do this collaboration, including various systemic enablers of financially
have a lasting impact on their ability information sharing and analysis motivated cyber threats.
to engage in illicit activity. Avoid the organizations, groups like the National
Collaboration and dialogue with
temptation to take the immediate action Cyber-Forensics & Training Alliance
multiple private sector partners who
within your power, without considering (NCFTA), and the Secret Service’s
confidentially provided the Secret
potential effectiveness, the threat actor’s network of Cyber Fraud Task Forces.
Service with information, including
likely reactions, and alternative courses
Example of an effective disruption on specific breached data, was
of action. For example, suspending
campaign. In September 2024, the invaluable for developing this disruption
a threat actor’s account may be
Secret Service and the Department operation. With the growth of cyber
immediately possible, but ask yourself
of Justice announced coordinated extortion, including by ransomware,
what barriers are for them creating
actions to disrupt the money laundering some businesses are understandably
a new account and can you detect
operations of Russian nationals Sergey hesitant to be seen as partnering
when they do so? Take the time to truly
Ivanov and Timur Shakhmametov. They with law enforcement, given the
examine the threat actor’s operations
are charged for their roles in connection threats of extortionists. However,
and identify the relevant partners, both
with operating billion-dollar money the growth of extortion makes the
public and private, to deliver a lasting
laundering services for cybercrime cooperation between businesses and
effect on the threatening activity.
marketplaces, ransomware groups, and law enforcement even more essential.
Upon careful analysis, it is often clear hackers responsible for significant data It can be done in a manner to protect
that arrest and significant asset seizures breaches of major U.S. companies.123 the privacy of victims and those that
are essential to effectively disrupt threat The unsealing of the indictment cooperate with law enforcement. As
actors. This is where partnering with coincided with the seizure of millions of you develop your ability to disrupt cyber
law enforcement is essential. Establish dollars in cryptocurrency coordinated threats, engage with your local Secret
efficient processes for working with law with Dutch authorities, the seizures of Service Cyber Fraud Task Force, and
enforcement and responding to lawful cryptocurrency and payment websites other relevant law enforcement partners,
process. Cyber threats move quickly, associated with Ivanov’s money to develop the essential, trusted
and the ability of law enforcement laundering platforms, announcement relationships for disrupting threats.
to combat them depends on the of a $10 million reward for their arrests,
businesses’ providing evidence in a sanctions designation by the Office of
timely manner, to include in response Foreign Assets Control (OFAC), and
to court orders. imposition of FinCEN special measures
to address money laundering risks.
123. U.S. Attorney’s Office, Eastern District of Virginia, “Two Russian nationals charged in connection with
operating billion-dollar money laundering services; Justice Department seizes web domains for multiple
illicit crypto exchanges” (26 September 2024). Accessed 23 February 2025 at: https://www.justice.
gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-
laundering
2025 DBIR Appendices 110

9
Contributing
organizations
111 2025 Data Breach Investigations Report

| A   | Compass Security | F   |
| --- | ---------------- | --- |
Akamai Technologies Coveware by Veeam Federal Bureau of Investigation –
Internet Crime Complaint Center
| Ankura | COWBELL |     |
| ------ | ------- | --- |
(FBI IC3)
| Apura Cyber Intelligence | Cyber Security Agency of Singapore |     |
| ------------------------ | ---------------------------------- | --- |
F-Secure
| Archer Hall | CyberSecurity Malaysia, an agency  |     |
| ----------- | ---------------------------------- | --- |
Flare
under the Ministry of Communications
Arctic Wolf
|     | and Multimedia (KKMM) | Flashpoint |
| --- | --------------------- | ---------- |
Atos
Cyber Security NSW (New South Wales,
|     | Australia) | G   |
| --- | ---------- | --- |
B
|     | Cybersixgill (a Bitsight Company) | Global Resilience Federation |
| --- | --------------------------------- | ---------------------------- |
Balbix
|     | CYBIR | GreyNoise Intelligence |
| --- | ----- | ---------------------- |
bit-x-bit, LLC
Cyentia Institute
| Bitsight    |                                  | H       |
| ----------- | -------------------------------- | ------- |
| BRANDEFENSE | D                                | Halcyon |
| BreachLock  | Defense Counterintelligence and  | Hoxhunt |
Security Agency (DCSA)
| Bridewell |     | Huntress |
| --------- | --- | -------- |
DomainTools
Dragos, Inc
| C            |     | I         |
| ------------ | --- | --------- |
| Censys, Inc. |     | ImmuniWeb |
E
| Center for Internet Security (CIS) |     | Infoblox |
| ---------------------------------- | --- | -------- |
Energy Analytic Security Exchange
| Cequence Security |     | Information Commissioner’s Office (ICO) |
| ----------------- | --- | --------------------------------------- |
(EASE)
CERT Division of Carnegie Mellon  Irish Reporting and Information Security
Edgescan
| University’s Software Engineering  |                     | Service (IRISS-CERT) |
| ---------------------------------- | ------------------- | -------------------- |
| Institute                          | Emergence Insurance |                      |
Enzoic
| CERT – European Union (CERT-EU)        |             | J         |
| -------------------------------------- | ----------- | --------- |
| Check Point Software Technologies Ltd. | EUROCONTROL | JPCERT/CC |
Coalition
2025 DBIR Contributing organizations 112

| K   | P   | U   |
| --- | --- | --- |
K–12 Security Information Exchange  Proofpoint U.S. Secret Service
(K–12 SIX)
KnowBe4
|             | Q      | V                        |
| ----------- | ------ | ------------------------ |
| KordaMentha | Qualys | VERIS Community Database |
Verizon Customer Experience
| L   |     | Organization |
| --- | --- | ------------ |
R
LayerX Security Rajah & Tann Cybersecurity Pte Ltd Verizon Cyber Risk Programs
Legal Services Information Sharing and  Recorded Future, Inc. Verizon Cyber Security Consulting
Analysis Organization (LS-ISAO)
|     | RedHunt Labs  | Verizon DDoS Defense            |
| --- | ------------- | ------------------------------- |
|     | ReversingLabs | Verizon Network Operations and  |
M
Engineering
Manufacturing Information Sharing and
|     | S   | Verizon Threat Research Advisory  |
| --- | --- | --------------------------------- |
Analysis Center (MFG-ISAC)
Center (VTRAC)
SecurityScorecard
Maritime Transportation System ISAC
Verizon VTRAC Labs
| (MTS-ISAC) | Shodan               |     |
| ---------- | -------------------- | --- |
| Mimecast   | Sistemas Aplicativos |     |
W
mnemonic
|     | Six Degrees | Wabtec Corporation |
| --- | ----------- | ------------------ |
Sophos
N
|     | Swisscom | Z   |
| --- | -------- | --- |
National Crime Agency
Zscaler
| National Cyber-Forensics & Training  | T   |     |
| ------------------------------------ | --- | --- |
Alliance (NCFTA)
Temple University – Cybersecurity in
National Cyber Security Agency,  Application, Research and Education
| Thailand      | (CARE) Lab     |     |
| ------------- | -------------- | --- |
| NetDiligence® | Tenable        |     |
| NETSCOUT      | Thales S21sec  |     |
The Shadowserver Foundation
O
Tidal Cyber
Okta
Triskele Labs
OpenText Cybersecurity
2025 DBIR Contributing organizations 113

2025 DBIR Contributing organizations 114

®
Verizon
Verizon Cyber
|     | Customer  | Verizon Cyber  | Verizon DDoS  |
| --- | --------- | -------------- | ------------- |
Security
|     | Experience  | Risk Programs | Defense |
| --- | ----------- | ------------- | ------- |
Organization Consulting
| Verizon Network  | Verizon Threat  |     |     |
| ---------------- | --------------- | --- | --- |
Verizon
| Operations and   | Research Advisory  |            |     |
| ---------------- | ------------------ | ---------- | --- |
| Engineering      | Center (VTRAC)     | VTRAC Labs |     |
2025 DBIR Contributing organizations 115

© 2025 Verizon. OGREP1230425