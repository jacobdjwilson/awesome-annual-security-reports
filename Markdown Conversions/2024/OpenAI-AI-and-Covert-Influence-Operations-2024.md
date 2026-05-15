# AI and Covert Influence Operations: Latest Trends

May 2024

## Table of Contents
- [Introduction](#introduction)
- [Building Safe, Reliable, and Trustworthy AI](#building-safe-reliable-and-trustworthy-ai)
- [A multi-pronged approach to disrupting threat actors](#a-multi-pronged-approach-to-disrupting-threat-actors)
- [Threats and Trends in 2024](#threats-and-trends-in-2024)
- [Attacker trends](#attacker-trends)
- [Defender trends](#defender-trends)
- [Distribution matters](#distribution-matters)
- [The importance of sharing](#the-importance-of-sharing)
- [The human element](#the-human-element)
- [Case Studies](#case-studies)
  - [Bad Grammar](#bad-grammar)
  - [Doppelganger](#doppelganger)
  - [Spamouﬂage](#spamouﬂage)
  - [International Union of Virtual Media (IUVM)](#international-union-of-virtual-media-iuvm)
  - [Zero Zeno](#zero-zeno)

---

## Introduction

We build AI models that improve lives and help solve complex challenges, but we know that threat actors will sometimes try to abuse our models to harm others. This includes people who abuse our models in support of covert inﬂuence operations (IO). Battling these threats requires joint eﬀorts across many disciplines and organizations. OpenAI is committed to play its part in disrupting IO and threat intelligence sharing.

This report surveys campaigns by threat actors that have used our products to further covert IO online. We deﬁne such operations as “deceptive attempts to manipulate public opinion or inﬂuence political outcomes without revealing the true identity or intentions of the actors behind them”. Some of these operations are well known; others we have discovered. While we observed these threat actors using our models for a range of IO, they all attempted to deceive people about who they were or what they were trying to achieve.

Our investigations showed that, while the actors behind these operations sought to generate content or increase productivity using our models, these campaigns do not appear to have meaningfully increased their audience engagement or reach as a result of their use of our services.

## Building Safe, Reliable, and Trustworthy AI

OpenAI is committed to developing safe and broadly beneﬁcial AI. Our investigations into suspected covert IO, some of which we describe in this report, are part of a broader strategy to meet our goal of safe AI deployment.

Our Usage Policies prohibit the use of our services to deceive or mislead others. This includes deceiving people about the authorship or source of content generated using our models, by engaging in activities such as:

- Creating content that is falsely attributed to nonexistent authors or organizations that misrepresent their origins, or impersonates organizations or living real persons without their consent or legal right.
- Creating automated systems that falsely present as being a real person, or don’t disclose to people that they are interacting with AI (unless it’s obvious from the context).

This includes misuse of our services by covert IO, which attempt to manipulate public opinion or inﬂuence political outcomes without revealing the true identity or intentions of the actors behind them.

When we discover such activity, we ban the accounts involved, share threat indicators with relevant industry peers, and share insights with our Safety Systems team, our Preparedness Framework process to inform further safety improvements. You can read more about our safety work on our website.

We intend to publish reports of this sort periodically to keep our users and the public informed on what we are seeing. We will review and reﬁne our policies and deﬁnitions as we continue to expand our understanding of these actors' behaviors.

## A multi-pronged approach to disrupting threat actors

We take a multi-pronged approach to combating abuse of our platform.

- We monitor and disrupt threat actors, including state-aligned groups and sophisticated, persistent threats. We invest in technology and teams to identify and disrupt actors like the ones we are discussing here, including leveraging AI tools to help combat abuses.
- We iterate with our Safety Systems team. As we learn from real-world use and misuse, we relay information back to our platform teams to iterate and become more secure.
- We work together with others in the AI ecosystem, collaborating with industry partners and other stakeholders to regularly exchange threat information about dangerous uses of AI.
- Finally, we communicate publicly. We highlight potential misuses of AI and share what we have learned about safety with the public.

As we’ve shared before, the vast majority of people use our models to help improve their daily lives. As is the case with many other ecosystems, there are a minority of malicious actors that require sustained attention so that everyone else can continue to enjoy the beneﬁts. Although we work to minimize potential misuse by such actors, we will not be able to stop every instance. But by continuing to innovate, investigate, collaborate, and share, we make it harder for threat actors to remain undetected across the digital ecosystem.

## Threats and Trends in 2024

Over the last three months, our work against deceptive and abusive actors has included disrupting covert inﬂuence operations that sought to use AI models in support of their activity across the Internet. These included campaigns linked to operators in Russia (two networks), China, Iran and a commercial company in Israel. The operations were:

- A previously unreported operation from Russia, which we dubbed “Bad Grammar”, operating mainly on Telegram and targeting Ukraine, Moldova, the Baltic States and the United States;
- A persistent Russian threat actor posting content about Ukraine across the internet, known as “Doppelganger”;
- A persistent Chinese threat actor posting content across the internet to praise China and criticize its critics, known as “Spamouﬂage”;
- A persistent Iranian threat actor posting web content that supported Iran and criticized Israel and the US, known as the International Union of Virtual Media (IUVM);
- A commercial company in Israel called STOIC, generating content about the Gaza conﬂict, and to a lesser extent the Histadrut trade unions organization in Israel and the Indian elections. We have nicknamed this operation “Zero Zeno” for the founder of the stoic school of philosophy, and to reﬂect the low levels of engagement that its various campaigns attracted.

We have shared threat indicators with peers across the industry. So far, these campaigns do not appear to have meaningfully increased their audience engagement or reach as a result of their use of our services. Using the Breakout Scale, which assesses the impact of IO on a scale from 1 (lowest) to 6 (highest), none of the ﬁve operations included in our case studies scored higher than a 2, indicating activity on multiple platforms, but no breakout to authentic audiences. (See each case study for details.)

While these campaigns diﬀered widely in their origins, tactics, use of AI, and apparent aims, we identiﬁed a number of common trends that illustrate the current state of the IO threat, and the ways the defender community can use AI and more traditional tools to disrupt them.

Overall, these trends reveal a threat landscape marked by evolution, not revolution. Threat actors are using our platform to improve their content and work more eﬃciently. But so far, they are still struggling to reach and engage authentic audiences.

## Attacker trends

### Content generation
All of the actors described in this report used our models to generate content (primarily text, occasionally images such as cartoons). Some appear to have done so to improve the quality of their output, generating texts with fewer language errors than would have been possible for human operators. Others appeared more focused on quantity, generating large volumes of short comments that were then posted on third-party platforms.

For example, Bad Grammar and Zero Zeno used our models to generate large quantities of short comments that were then posted across Telegram, X, Instagram and other sites. People acting on behalf of IUVM used our models to generate and proofread longer articles in English and French. Spamouﬂage and Doppelganger used our models for both quality and quantity, correcting grammatical errors, but also creating dozens of short comments in a range of languages.

It is important here to distinguish between eﬀort and eﬀect. The increased volume that these networks were able to generate did not show any signs of translating into increased engagement from authentic audiences.

### Mixing old and new
All of these operations used AI to some degree, but none used it exclusively. Instead, AI-generated material was just one of many types of content they posted, alongside more traditional formats, such as manually written texts, or memes copied from across the internet.

For example, we identiﬁed Spamouﬂage accounts on X that posted comments generated using our models. The same accounts interspersed these comments with content that appeared to have been written by humans who were not using their native language. These non-AI posts were made after their posts of AI-generated content, as well as before.

Similarly, Doppelganger posted AI-generated comments on 9GAG alongside a range of memes, some of which were years old and appear to have been copied from across the internet. This was not a case of giving up on human generation and shifting to AI, but of mixing the two.

### Faking engagement
Some of the campaigns we disrupted used our models to create the appearance of engagement across social media - for example, by generating replies to their own posts to create false online engagement, which is against our Usage Policies. This is distinct from attracting authentic engagement, which none of the networks described here managed to do.

For example, Zero Zeno posted short texts on speciﬁc themes, especially the Gaza conﬂict, on Instagram and X. These texts were generated using our models. A further set of accounts on those platforms would then reply with comments that were also generated by this operation.

Similarly, Spamouﬂage posted short comments on X criticizing Chinese dissident Cai Xia. These took the form of an initial post and a series of replies. Every comment in the “conversation” was artiﬁcially generated using our models - likely to create the false impression that real people had engaged with the operation’s content.

### Productivity gains
Many of the threat actors that we identiﬁed and disrupted used our models in an attempt to enhance productivity. This included uses that would be banal if they had not been put to the service of deceptive networks, such as asking for translations and converting double quotes to single quotes in lists.

For example, Spamouﬂage used our models to summarize and analyze the sentiment of large numbers of social media posts, especially Chinese-language posts. The people acting on behalf of IUVM used our models to create website tags, which then appear to have been automatically added to the group’s website. On at least one occasion, the website tags included a message from our model that exposed them as AI-generated.

## Defender trends

### Defensive design
Our models are designed to impose friction on threat actors. We have built them with defense in mind: for example, our latest image generation model, DALL-E 3, has mitigations to decline requests that ask for a public ﬁgure by name, and we’ve worked with red teamers—domain experts who stress-test our models and services—to help inform our risk assessment and mitigation eﬀorts in areas like deceptive messaging. We have seen where operators like Doppelganger tried to generate images of European politicians, only to be refused by the model.

### AI for defenders
Throughout our investigations, we have built and used our own AI-powered models to make our detection and analysis faster and more eﬀective. AI allows analysts to assess larger volumes of data at greater speeds, reﬁne code and queries, and work across many more languages eﬀectively.

By leveraging our models’ capabilities to synthesize and analyze the ways threat actors use those models at scale and in many languages, we have drastically improved the analytical capabilities of our investigative teams, reducing some workﬂows from hours or days to a few minutes. As our models improve, we’ll continue leveraging their capabilities to improve our investigations too.

## Distribution matters
We’ve seen threat actors using our models to generate content that was then published across the internet. But to reach any kind of audience, such content requires a distribution system, and it has to compete against all the content produced by real people across social media. In every operation we found, the content they generated failed to build interest among authentic audiences.

We use the Breakout Scale to assess the ongoing impact of IO. This divides IO into a scale from 1 (least impact) to 6 (greatest impact), depending on whether they are ampliﬁed by real people, quoted uncritically by the media or inﬂuencers, or have an impact on policy or politics.

Of all the networks described in this report, none rose higher than a Category 2 (multiple platforms, no breakout to authentic audiences); Bad Grammar stayed at Category 1. This is not to say that these operations could not reach the higher categories in the future, especially if they are unwittingly ampliﬁed by media, inﬂuencers or politicians.

## The importance of sharing
All the networks described in this report used our models to generate content that was then posted elsewhere on the internet. We identiﬁed these operations’ activity across Telegram, X, Instagram, Facebook, YouTube, and many smaller forums and websites.

To increase the impact of our disruptions on these actors, we are sharing detailed threat indicators with industry peers. We are also publishing domain names associated with the campaigns we identiﬁed, to enable open-source research.

Our own investigations built on years of research by our peers at social media platforms and open-source investigators. These included the detailed descriptions of Doppelganger by EU Disinfolab, Meta, and Microsoft; the exposure of Iranian IO by Mandiant and Reuters; investigations into Spamouﬂage by Graphika, the Australian Strategic Policy Institute, Microsoft, Meta and the FBI; and reporting on Zero Zeno by the Atlantic Council’s Digital Forensic Research Lab.

## The human element
AI can change the toolkit that human operators use, but it does not change the operators themselves. Our investigations showed that they were as prone to human error as previous generations have been.

For example, Bad Grammar posted content that included refusal messages from our model, exposing their content as AI-generated. IUVM appears to have automated its creation of website tags, so that they sometimes included messages from our AI models. Doppelganger posted a comment about Ukraine that was generated using our services as the caption for a video collage of news footage about the Gaza conﬂict, apparently mixing up its videos.

While it is important to be aware of the changing methods that threat actors use, we should not lose sight of the operators’ very human limitations. These, as well as the broader behaviors we identiﬁed, are set out in the following case studies.

## Case Studies

### Bad Grammar
*Unreported Russian threat actor posting political comments in English and Russian on Telegram*

**Actor**
We banned a previously unreported network of accounts that were using our models to create comments that were then posted on Telegram. We linked this activity to individuals from Russia. Given its focus on Telegram, its repeated posting of ungrammatical English, and its struggle to build an audience, we have dubbed this network “Bad Grammar”.

**Behavior**
This network targeted audiences in Russia, Ukraine, the United States, Moldova and the Baltic States with content in Russian and English. The network used our models and accounts on Telegram to set up a comment-spamming pipeline.

![Public Telegram comment matching a text generated by this network]

**Content**
This campaign generated short comments focused on a handful of political themes. In both English and Russian, the main topics that it posted about on Telegram were the war in Ukraine, the political situation in Moldova and the Baltic States, and politics in the United States.

![Public Telegram comment matching a text generated by this network]

**Impact assessment**
Using the Breakout Scale to assess the impact of IO, we would assess this as being in Category 1, marked by posting activity on a single platform, with no evidence of signiﬁcant ampliﬁcation by people outside the network.

### Doppelganger
*Persistent Russian threat actor posting anti-Ukraine content across the internet*

**Actor**
We banned four clusters of accounts using our models linked to people acting on behalf of the Russian inﬂuence operation known as “Doppelganger”.

**Behavior**
This activity targeted audiences in Europe and North America and focused on generating content for websites and social media. The ﬁrst cluster of accounts generated short text comments in English, French, German, Italian and Polish. These were posted on 9GAG and X alongside memes, videos, and links that do not appear to have been generated using our models.

![Comment about Ukraine, and video about Gaza, posted to 9GAG’s “Motor Vehicles” channel]

**Content**
The majority of the content that this campaign published online focused on the war in Ukraine. It portrayed Ukraine, the US, NATO and the EU in a negative light and Russia in a positive light.

**Impact assessment**
Using the Breakout Scale to assess the impact of IO, we would assess the activity that was related to the use of our models as being in Category 2, marked by posting activity on multiple platforms, but with no breakout or signiﬁcant audience engagement in any of them.

### Spamouﬂage
*Persistent Chinese threat actor posting content across the internet to praise China and criticize its critics*

**Actor**
We banned a small number of accounts associated with the China-origin operation known as “Spamouﬂage”.

**Behavior**
This network targeted global audiences, especially members of the Chinese diaspora and critics of the Chinese government. It mainly generated content in Chinese and, to a lesser extent, English, Japanese and Korean.

![Screenshot of the website revealscum.com]

**Content**
Much of the content generated by this campaign was in Chinese. Topics ranged from praising the Chinese government’s international law enforcement cooperation to criticizing abuses against Native Americans in the United States.

**Impact assessment**
Using the Breakout Scale to assess the impact of IO, we would assess this as a Category 2 operation, marked by posting activity across many platforms, but with no evidence of it being signiﬁcantly ampliﬁed by people outside the network.

**Indicators**
- revealscum[.]com

### International Union of Virtual Media (IUVM)
*Persistent Iranian threat actor generating pro-Iran, anti-Israel and anti-US website content*

**Actor**
We banned a small number of accounts linked to people associated with the International Union of Virtual Media (IUVM).

**Behavior**
This campaign targeted global audiences and focused on content generation in English and French. It used our models to generate and proofread articles, headlines and website tags.

![Tags on an article published by iuvmpress.co]

**Content**
The content that this network generated consisted of long-form articles, headlines and website tags. This content was typically anti-US and anti-Israel and praised the Palestinians, Iran, and the “Axis of Resistance”.

**Impact assessment**
Using the Breakout Scale to assess the impact of IO, we would assess this as a Category 2 operation, marked by posting activity on multiple platforms, but with no breakout or signiﬁcant audience engagement in any of them.

**Indicators**
- iuvmpress[.]co
- iuvmarchive[.]org

### Zero Zeno
*For-hire Israeli threat actor posting anti-Hamas, anti-Qatar, pro-Israel, anti-BJP, and pro-Histadrut content across the internet*

**Actor**
We banned a cluster of accounts operated from Israel that were being used to generate and edit content for an inﬂuence operation that spanned X, Facebook, Instagram, websites, and YouTube. The network was operated by STOIC, a political campaign management ﬁrm in Israel.

**Behavior**
This operation targeted audiences in Canada, the United States and Israel with content in English and Hebrew. In early May, it began targeting audiences in India with English-language content.

![English-language comments generated by this network and posted on Instagram]

**Content**
This operation was divided into a number of topical campaigns, most of which were loosely associated with the Gaza conﬂict and the broader question of relations between individuals of Jewish and Muslim faith.

**Impact assessment**
Using the Breakout Scale to assess the impact of IO, we would assess this as a Category 2 operation, marked by posting activity on multiple platforms and websites, but with no evidence of it being signiﬁcantly ampliﬁed by people outside the network.

**Indicators**
- nonagenda[.]com
- the-good-samaritan[.]com
- uc4canada[.]com
- ufnews[.]io

---
**Authors**
Ben Nimmo