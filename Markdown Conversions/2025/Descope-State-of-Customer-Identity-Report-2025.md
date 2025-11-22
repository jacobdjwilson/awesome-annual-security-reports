# State of Customer Identity [2025 Report]

**Descope** | [www.descope.com](https://www.descope.com) | docs.descope.com

---

## Table of Contents

* **Executive Summary** (Page 3)
* **Impact of CIAM** (Page 6)
* **Authentication Stagnation** (Page 9)
* **Developer Experience** (Page 14)
* **Security and CX** (Page 18)
* **Agentic AI** (Page 23)
* **Conclusion** (Page 27)
* **Methodology** (Page 28)

---

## Executive Summary

Authentication should be easy and effective. But in practice, especially for the teams that manage it every day, it's often the complete opposite.

We commissioned a survey of over four hundred CIAM (Customer Identity and Access Management) decision-makers across industries, from engineering leaders to security experts. Our goal was to understand how organizations handle customer authentication today: their challenges, motivations, and burning desires.

While these sorts of studies often boil down to predictable "bad thing is bad" conclusions, the responses we gathered surprised us and they'll probably offer you a few lightbulb moments, too. You might deeply identify with the struggles our respondents face, or perhaps see a previously hidden path in your own auth journey.

In either case, the following report reveals a marketplace wrestling with fundamental contradictions and searching for better ways forward.

### Identity crisis is the status quo
Organizations deploy authentication strategies they already know don't deliver. Username/password authentication appears in 87% of companies' customer-facing applications, yet only 2% of respondents believe it effectively balances security and user experience. The near-universal use of passwords isn't a revelation, but the dismal sentiment for them speaks volumes.

The lack of password alternatives could be because more than half (53%) of respondents currently repurpose their workforce IAM for customer authentication. It's a square-peg-into-round-hole approach that a mere 8% would choose if they started fresh today.

Why the disconnect? Teams know better options exist, and they see passwordless and purpose-built CIAM succeeding elsewhere. But when you're barely keeping the lights on with legacy systems, the path from status quo to the best auth available feels like an uphill battle.

### Pay the invisible auth tax
Authentication misfires rarely stay contained, and they often directly affect an organization's growth. Our data shows that 82% of organizations suffered tangible business impacts from CIAM issues, with a wide variety of root causes.

As expected, security incidents from weak or missing multi-factor authentication (MFA) affected a significant portion (39%) of respondents. But identity issues also played havoc with product roadmaps: 37% of organizations delayed projects to address authentication gaps, while 46% postponed CIAM updates to deal with other pressures.

Companies know they can't defer authentication improvements indefinitely, but many feel torn between competing priorities. Respondents were acutely aware of moments when their marching orders should have been to upgrade CIAM tools, but other projects took precedence. In these scenarios, organizations end up paying an unseen "auth tax" when they least expect it: in the form of long-term tech debt, as an obstacle to moving upmarket, or even from a damaging breach.

### Security vs. user experience vs. both
CIAM decision-makers have been locked in a debate since before the days of dialup: lock it down or open it up?

Our respondents split into three groups:
* 39% emphasize security
* 26% favor user experience
* 34% aim for a balance between them

Yet, 73% admit their organizations struggle to find equilibrium, regardless of which side they favor. The consequences of overcorrection can carve a chunk out of a company's bottom line, with over a quarter (27%) of organizations reporting lost revenue after implementing stricter authentication controls. Conversely, more than a third (39%) of companies that attempted low-security strategies experienced a harmful incident as a direct result.

Company size heavily influences these sentiments. Among enterprises with more than 20,000 employees, 48% put security first. This seems to indicate that scale and risk exposure push organizations toward more constrained, restrictive approaches. However, the practical outcomes seem to defy this sentiment, with large organizations that enforce stricter policies reporting a much higher rate of customer pushback compared to their smaller counterparts.

### Devs do everything (while equipped with less)
Over half (51%) of the organizations we surveyed have developers with minimal authentication experience building customer-facing identity systems prone to vulnerabilities. Meanwhile, the time they spend on developing authentication is a point of contention. The majority (64%) of respondents say devs spend too little time on authentication (creating security risks), while 36% say they spend too much time (delaying core features).

The most inexperienced devs in this bunch—who are admirably willing to learn on the job—aren't really responsible for the gap in expertise. This technical gulf is about specialization, not potential. For example, if we drill down into companies who use in-house, DIY authentication (36% of all respondents), only 27% have full-time CIAM developers.

That's a shockingly low number, and it points to two core issues:
1.  Developers who work on authentication are asked to do more with less (time, training, and resources).
2.  Organizations tend to make auth decisions based on short-term thinking (meeting immediate needs rather than planning long-term).

Modern authentication requires deep knowledge of security best practices that simply won't occur to a novice. Asking product developers to master this highly focused domain while shipping features is a recipe for neither goal being met.

### AI attitudes and adoption blues
As organizations embrace AI at a seemingly breakneck pace, identity management often lags behind. While 88% of our respondents are using or planning to use AI agents, only 37% have actually progressed beyond small pilot programs. The identity considerations? Mostly uncharted territory.

A nearly unanimous 95% of respondents recognize that authentication is critical for AI security. Yet, the trust dynamics in human versus non-human identities (NHIs) appear to be in flux. Organizations just starting with AI see humans as the bigger data breach risk (70% vs. 30%). But among those with wider AI deployments, that gap narrows by 33% (60% vs. 40%). In other words, the longer companies spend working with AI agents, the less likely they are to trust them with sensitive information.

---

## Impact of CIAM: Why does it matter?

Authentication is the only feature every customer is guaranteed to see. Because of this unique position in the product experience, it's simultaneously critical to everyone—and partially owned by all.

**Perspectives compete and CIAM stagnates.**
Just think about the ways CIAM touches each part of an organization:
* **Marketing** needs clean identity data for outreach campaigns.
* **Sales** wants to know if that demo request is legitimate or a bot.
* **Product teams** balance friction against user experience and conversions.
* **Security** demands strong protection and fraud prevention.
* **Support and customer success** bear the cost of confused users.

Each team has metrics, motivations, and priorities. Every one of them might have some say in how CIAM works, yet none are its "true" owner. The result? Everyone wants CIAM to work toward their team's goals, but virtually no one has the time and resources to improve it.

**84%** agree that authentication is critically important, but the needs are not unique to their business.

### Impact of broken authentication
It's the digital equivalent of a door handle: utterly necessary for operating your business, but no one's first pick when it comes to improving the bottom line. But remember how 46% of our respondents had delayed CIAM improvements to deal with other projects on their roadmap? Authentication gets de-emphasized often because it isn't seen as a top-line revenue source.

**82%** have experienced business impact as a result of customer authentication issues.

**Negative Business Impacts Experienced:**
* **52%** - Costs to manage support or help desk tickets.
* **37%** - Delayed engineering roadmap due to authentication and identity-related tasks.
* **30%** - User drop-off due to complex onboarding process.
* **28%** - Lost customer trust due to authentication-related security incident.
* **23%** - Lost revenue from abandoned transactions.

**Direct Business Impact of CIAM Decisions:**
* **27%** experienced revenue loss or customer dropoff after implementing a stricter approach (e.g., mandatory MFA).
* **39%** experienced a security incident as a result of a lower-friction approach (e.g., no MFA or perishable MFA).
* **14%** have experienced **BOTH** revenue loss and security issues.

### Why endless auth cycles keep happening
The issues above result from what we've dubbed the "authentication doom spiral": auth problems pile up, but fixes are perpetually deprioritized because no one really owns it.

The build-versus-buy dilemma directly amplifies these risks. Organizations using **open-source CIAM solutions** see dramatically worse outcomes:
* 50% report revenue loss from stricter authentication (compared to 26% for commercial solutions).
* 51% suffer security incidents from lax controls (versus 39% for commercial).

Our data indicates that the DIY approach, often chosen to maintain control over the implementation or to reduce costs, doubles down on the very problems it aims to solve.

### Authentication can be a competitive advantage
Case studies highlight the benefits of modern CIAM:
* **Cequence Security:** Switching to a modern CIAM platform allowed product devs to stop resolving identity issues, and customer SSO onboarding became a self-service process that cut support time by 90%.
* **BalkanID:** Migrating from open-source Ory Kratos to a commercial platform recouped development time, with customers self-configuring SSO and support for multiple login ID linking saving up to 2 days a month.
* **Branch Insurance:** Implementing passkeys cut auth-related support requests in half.

---

## Authentication Stagnation and the Password Paradox

**Why is everyone using methods that nobody wants?**
Organizations in 2025 are feeling insecure about their relationship with passwords. They know passwords are inherently destructive to their security posture and user experience, but they're hesitant to change.

**The Disconnect:**
87% of companies still rely on username/password-based authentication, but only 2% believe it effectively balances security and user experience.

| Authentication Method | Current Use | Believed Most Effective (Security + UX) |
| :--- | :--- | :--- |
| Username/password | 87% | 2% |
| SSO | 75% | 21% |
| Authenticator apps | 71% | 27% |
| OTP | 58% | 14% |
| Passkeys or biometrics | 45% | 26% |
| Security challenge questions | 40% | 2% |
| Social login | 16% | 4% |
| Magic links | 9% | 2% |
| Google One Tap | 7% | 0.5% |

### MFA is a work in progress
94% have some form of MFA, but only **10%** have it across all applications.
* 10%: MFA for all applications.
* 27%: MFA for most applications, but not all.
* 32%: Mix of applications, some with MFA and some without.
* 24%: MFA for a few select applications.
* 6%: Do not have customer MFA.

### Passkeys show disconnect between knowledge and practice
72% of organizations have already adopted passkeys for CIAM or plan to do so in the next 2 years.
* Existing Use: 45%
* Plan to use (next 2 years): 27%

Surprisingly, passkeys are only identified by 26% of respondents as most effective for balancing security and UX, trailing behind Authenticator apps (27%).

### Challenges in CIAM
**95%** report that they find CIAM challenging; finding the balance between CX and security tops the list.

**Top Challenges:**
1.  Struggle to find the right balance between security and customer experience (69%).
2.  Struggle to modernize and stitch together legacy systems (47%).
3.  We perceive users being hesitant to use newer authentication methods (37%).
4.  Lack budget and executive buy-in to implement better authentication methods (31%).
5.  Other engineering priorities prevent authentication improvements (31%).

### The "what if" of authentication
**51%** of organizations use workforce solutions for CIAM, but only **8%** would choose the same path if starting from scratch.

**Current vs. Preferred Solution (if starting from scratch):**
* **Workforce solution:** 51% use it, but only 8% prefer it.
* **Commercial CIAM:** 26% use it, but 57% prefer it.
* **In-house/Custom:** 37% use it, but 14% prefer it.
* **Open Source:** 21% use it, but 14% prefer it.

**Top Priorities when choosing a solution:**
1.  Security and Compliance (64%)
2.  Total cost of ownership (51%)
3.  Reliability, scalability, and uptime (43%)

---

## The Developer (in) Experience

Developer experience with CIAM looks a bit like a game of Hot Potato: nobody wants to hold the responsibility of authentication when the music stops.

### So much to do, so little time
CIAM decision-makers are almost twice as likely to think developers don't spend enough time on authentication.
* **64%** say developers don't spend *enough* time (creating security risks).
* **36%** say developers spend *too much* time (distracting from core product).

**The Expertise Gap:**
**51%** of survey respondent organizations task developers with **minimal authentication experience** to build and manage CIAM systems.
* Only **28%** have dedicated developers working only on authentication.
* **59%** have developers with deep experience who also work on other areas.

### The quiet cost of context switching
Organizations with 20,000+ employees show the most acute problems, with 58% reporting CIAM projects were delayed by other priorities (versus 33% for smaller companies).

**Impact by Solution Type:**
* **Open Source:** 50% report revenue loss; 51% report security incidents.
* **In-house:** 30% report revenue loss.
* **Commercial CIAM:** Lowest rates of revenue loss (26%) and security incidents (39%).

**Opinions on improving developer experience**
52% say their CIAM development teams would benefit from self-service SSO and SCIM setup.

**Capabilities beneficial to developers:**
* Comprehensive support for open identity standards (OAuth, WebAuthn, etc.): 57%
* Self-service SSO and SCIM setup: 52%
* Unified authentication experiences across apps: 51%
* Adaptive, phishing-resistant MFA: 49%
* Abstraction layers (no/low code): 39%

---

## The Security-CX Balancing Act

Three-quarters (73%) of organizations say finding the right balance between security and customer experience is genuinely hard.

**Approaches to Balance:**
* **39%** - Security is the priority, even if we impact customer experience.
* **34%** - We do not choose between security and CX; we know we have to make both work.
* **26%** - Customer experience is the priority, even if we open ourselves to security risks.

**Team Alignment:**
* **Engineering/Product** teams favor security the most (42%).
* **Identity** teams favor CX the most (30%).

**Company Size:**
The largest companies (20,000+ employees) are most likely to prioritize security (48%). However, 29% of these large companies saw negative impacts from implementing too-strict security policies.

### Adaptive MFA: Adapting to modern expectations
Only **23%** currently use adaptive or risk-based MFA, although **37%** plan to use it. Surprisingly, **33%** have no plans to use it.

### Passkey adoption
**72%** of the market is bought in or buying in soon.
* Microsoft data: Passkey users log in 3x faster with a 98% success rate (vs 32% for passwords).

---

## The Agentic AI Future

**Everyone is betting on AI, but nobody's ready.**
* **88%** of respondents are using or planning to use AI agents.
* Only **37%** have progressed beyond pilot programs.
* **95%** believe authentication is critical for secure AI adoption.

**Concerns are universal and justified:**
94% have concerns about identities and chatbots.
* **57%**: AI agents/chatbots could share data with unauthorized users.
* **57%**: AI agents could access information they are not authorized to access.
* **46%**: Engineering team lacks time/expertise to maintain identity processes for AI.
* **39%**: Users won't have required visibility/consent.

**Who owns AI Auth?**
It is a shared responsibility:
* Security Team: 66%
* Existing Engineering Teams: 47%
* Identity Team: 41%
* AI Engineering Team: 31%

**Trust erodes with experience:**
When asked whether human users or AI agents pose a greater risk, 65% say humans are riskier. However, among those with wide AI deployment, the gap narrows (60% human vs 40% AI), suggesting that experience with AI agents leads to increased caution.

**Model Context Protocol (MCP):**
Only 26% of decision-makers consider themselves knowledgeable about MCP. Of those adopting it, 60% are deploying local servers only.

---

## Conclusion

The state of customer identity in 2025 reveals a marketplace in the middle of transformation. Today, organizations are wrestling with a painful paradox: Everyone agrees authentication matters, yet it stays on the back burner.

However, there is optimism:
* Organizations are no longer satisfied with antiquated security methods.
* The scramble to secure AI is forcing authentication conversations.
* Modern methods like passkeys and adaptive MFA are being embraced.

Ultimately, we're confident that more and more organizations will stop seeing customer identity as a burden—and recognize it as a key business enabler.

---

## Methodology

* **Survey Date:** Mid-2025.
* **Respondents:** 416 qualified individuals with decision-making responsibility for CIAM.
* **Company Size:** All respondents from companies with more than 500 employees.
* **Roles:** IT/Security (20%), Identity (30%), Engineering/Product (50%).

**About Descope**
Descope is a drag & drop platform to help organizations manage all their external identities. Our no/low code external IAM solution helps organizations create, modify, and secure authentication and authorization journeys for customers, partners, AI agents, and MCP servers.