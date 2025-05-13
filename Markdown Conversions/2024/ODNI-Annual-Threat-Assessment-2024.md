# AI Instruction Set for Converting Technical PDFs to Markdown
## Purpose
Ensure technical PDFs are converted to Markdown with complete fidelity, preserving all content, structure, and formatting.
## Goals
1. **Full Conversion**: Include all text, quotations, footnotes, references, and technical terminology without omission or summarization.  
2. **TOC Format**: Include a fully functional Table of Contents with proper linking.  
3. **Markdown Conventions**: Use clear, consistent, and professional formatting.  
4. **Images**: Describe image contents without embedding.
## Conversion Instructions
### Content
- **Include All Text**: Retain all sections, preserving the original structure and content.  
- **Headings**: Format with `#` for main headings, `##` and `###` for subheadings.  
- **Lists**: Use `1.` for ordered lists, `-` for unordered lists.  
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and \`\`\` for code blocks.  
- **Links**: Format as `[text](URL)` and ensure accuracy.
### Images
- **Do Not Embed**: Replace with descriptive text: `![Image description]`.
### Table of Contents
- Place after the document title but before the main content:
  ## Table of Contents
  - [Section Title](#section-title)
  - [Subsection Title](#subsection-title)
- Ensure anchor links work and follow the format `(#section-title)`.
### Footnotes and References
- Use Markdown footnote syntax:  
  Content with a footnote[^1].  
  [^1]: Footnote content here.
- Retain all technical and academic terms exactly.
## Verification and Quality Assurance
1. **Accuracy**: Verify the entire document is converted without omissions.  
2. **TOC Functionality**: Check all links point to the correct headings.  
3. **Readability**: Ensure professional formatting and adherence to Markdown standards. DO NOT enclose the top and bottom of the content in ```markdown and ``` . 
4. **Fidelity**: Confirm the output matches the original PDF exactly.  

# ANNUAL THREAT ASSESSMENT OF THE U.S. INTELLIGENCE COMMUNITY

## Table of Contents
- [INTRODUCTION](#introduction)
- [FOREWORD](#foreword)
- [STATE ACTORS](#state-actors)
  - [China](#china)
  - [Russia](#russia)
  - [Iran](#iran)
  - [North Korea](#north-korea)
  - [Conflicts and Fragility](#conflicts-and-fragility)
    - [Gaza Conflict](#gaza-conflict)
    - [Potential Interstate Conflict](#potential-interstate-conflict)
    - [Potential Intrastate Turmoil](#potential-intrastate-turmoil)
- [TRANSNATIONAL ISSUES](#transnational-issues)
  - [Contested Spaces](#contested-spaces)
    - [Disruptive Technology](#disruptive-technology)
    - [Digital Authoritarianism and Transnational Repression](#digital-authoritarianism-and-transnational-repression)
    - [WMD](#wmd)
  - [Shared Domains](#shared-domains)
    - [Environmental Change and Extreme Weather](#environmental-change-and-extreme-weather)
    - [Health Security](#health-security)
    - [Migration](#migration)
  - [Non-State Actor Issues](#non-state-actor-issues)
    - [Transnational Organized Crime](#transnational-organized-crime)
    - [Human Trafficking](#human-trafficking)
    - [Global Terrorism](#global-terrorism)
    - [Private Military and Security Companies](#private-military-and-security-companies)

# INTRODUCTION

This annual report of worldwide threats to the national security of the United States responds to Section 617 of the FY21 Intelligence Authorization Act (Pub. L. No. 116-260). This report reflects the collective insights of the Intelligence Community (IC), which is committed every day to providing the nuanced, independent, and unvarnished intelligence that policymakers, warfighters, and domestic law enforcement personnel need to protect American lives and America’s interests anywhere in the world.
This assessment focuses on the most direct, serious threats to the United States primarily during the next year. The order of the topics presented in this assessment does not necessarily indicate their relative importance or the magnitude of the threats in the view of the IC. All require a robust intelligence response, including those where a near-term focus may help head off greater threats in the future.
Information available as of 22 January was used in the preparation of this assessment.

# FOREWORD

During the next year, the United States faces an increasingly fragile global order strained by accelerating strategic competition among major powers, more intense and unpredictable transnational challenges, and multiple regional conflicts with far-reaching implications. An ambitious but anxious China, a confrontational Russia, some regional powers, such as Iran, and more capable non-state actors are challenging longstanding rules of the international system as well as U.S. primacy within it. Simultaneously, new technologies, fragilities in the public health sector, and environmental changes are more frequent, often have global impact and are harder to forecast.
One need only look at the Gaza crisis—triggered by a highly capable non-state terrorist group in HAMAS, fueled in part by a regionally ambitious Iran, and exacerbated by narratives encouraged by China and Russia to undermine the United States on the global stage—to see how a regional crisis can have widespread spillover effects and complicate international cooperation on other pressing issues. The world that emerges from this tumultuous period will be shaped by whoever offers the most persuasive arguments for how the world should be governed, how societies should be organized, and which systems are most effective at advancing economic growth and providing benefits for more people, and by the powers—both state and non-state—that are most able and willing to act on solutions to transnational issues and regional crises.
New opportunities for collective action, with state and non-state actors alike, will emerge out of these complex and interdependent issues. The 2024 Annual Threat Assessment highlights some of those connections as it provides the IC’s baseline assessments of the most pressing threats to U.S. national interests. It is not an exhaustive assessment of all global challenges, however. It addresses traditional and nontraditional threats from U.S. adversaries, an array of regional issues with possible larger, global implications, as well as functional and transnational challenges, such as proliferation, emerging technology, climate change, terrorism, and illicit drugs.
China has the capability to directly compete with the United States and U.S. allies and to alter the rules-based global order in ways that support Beijing’s power and form of governance over that of the United States. China’s serious demographic and economic challenges may make it an even more aggressive and unpredictable global actor. Russia’s ongoing aggression in Ukraine underscores that it remains a threat to the rules-based international order. Local and regional powers are also trying to gain and exert influence, often at the cost of neighbors and the world order itself. Iran will remain a regional menace with broader malign influence activities, and North Korea will expand its WMD capabilities while being a disruptive player on the regional and world stages. Often, U.S. actions intended to deter foreign aggression or escalation are interpreted by adversaries as reinforcing their own perceptions that the United States is intending to contain or weaken them, and these misinterpretations can complicate escalation management and crisis communications.
Regional and localized conflicts and instability, such as from the HAMAS attacks against Israel and Israel’s subsequent invasion of Gaza, will demand U.S. attention as states and non-state actors struggle in this evolving global order, including over major power competition and shared transnational challenges. From this, conflicts and bouts of instability from East Asia to Africa to the Western Hemisphere—exacerbated by global challenges—have greater potential to spill over into many domains, with implications for the United States, U.S. allies and partners, and the world.
Economic strain is further stoking this instability. Around the world, multiple states are facing rising, and in some cases unsustainable, debt burdens, economic spillovers from the war in Ukraine, and increased cost and output losses from extreme weather events even as they continue to recover from the COVID-19 pandemic. While global agricultural food commodity prices retreated from their 2022 peak, domestic food price inflation remains high in many countries and food security in many countries remains vulnerable to economic and geopolitical shocks.
At the same time, the world is beset by an array of shared, universal issues requiring cooperative global solutions. However, the larger competition between democratic and authoritarian forms of government that China, Russia, and other countries are fueling by promoting authoritarianism and spreading disinformation is putting pressure on longstanding norms encouraging cooperative approaches to the global commons. This competition also exploits technological advancements—such as AI, biotechnologies and related biosecurity, the development and production of microelectronics, and potential quantum developments—to gain stronger sway over worldwide narratives affecting the global geopolitical balance, including influence within it. The fields of AI and biotechnology, in particular, are rapidly advancing, and convergences among various fields of science and technology probably will result in further significant breakthroughs. The accelerating effects of climate change are placing more of the world’s population, particularly in low- and middle-income countries, at greater risk from extreme weather, food and water insecurity, and humanitarian disasters, fueling migration flows and increasing the risks of future pandemics as pathogens exploit the changing environment.
The 2024 Annual Threat Assessment report supports the Office of the Director of National Intelligence’s commitment to transparency and the tradition of providing regular threat updates to the American public and the United States Congress. The IC is vigilant in monitoring and assessing direct and indirect threats to U.S. and allied interests. For this requirement, the IC’s National Intelligence Officers—and the National Intelligence Council that they collectively constitute—work closely and regularly with analysts across the IC. This work diagnostically examines the most serious of both the immediate and long-term threats to the United States, along with the evolving global order and other macro-trends, that will most influence the direction and potential impact of these threats.
The National Intelligence Council stands ready to support policymakers with additional information in a classified setting.

# STATE ACTORS

PREFACE
Several states are engaging in competitive behavior that directly threatens U.S. national security while a larger set of states—including some allies—are facing intrastate conflict or domestic turmoil. These pressures and dynamics have the potential to spill over borders and across regions to destabilize areas and threaten the livelihoods, safety, and stability of billions of people. China vies to surpass the United States in comprehensive national power and secure deference to its preferences from its neighbors and from countries around the world, while Russia directly threatens the United States in an attempt to assert leverage regionally and globally.

## China

Regional and Global Activities
President Xi Jinping envisions China as the preeminent power in East Asia and as a leading power on the world stage. The Chinese Communist Party (CCP) will attempt to preempt challenges to its reputation and legitimacy, undercutting U.S. influence, driving wedges between Washington and its partners, and fostering global norms that favor its authoritarian system. Most significantly, the People’s Republic of China (PRC) will press Taiwan on unification, an effort that will create critical friction points with the United States. Despite economic setbacks, China’s leaders will maintain statist economic policies to steer capital toward priority sectors, reduce dependence on foreign technologies, and enable military modernization.

- China views Washington’s competitive measures against Beijing as part of a broader U.S. diplomatic, economic, military, and technological effort to contain its rise, undermine CCP rule, and prevent the PRC from achieving its regional and global power ambitions.
Nevertheless, China’s leaders will seek opportunities to reduce tension with Washington when they believe it benefits Beijing and protects core interests, such as Xi’s willingness to meet with President Biden at the APEC Summit in late 2023.
- China faces myriad domestic challenges that probably will hinder CCP leaders’ ambitions. CCP leaders have long believed that China’s technology-powered economic growth would outpace Western countries. However, China’s growth almost certainly will continue slowing thanks to demographic challenges and a collapse in consumer and investor sentiment due in large part to Beijing’s heavyhanded policies.
- PRC leaders’ regional and global ambitions are also hampered by growing resistance to China’s heavyhanded and coercive economic, diplomatic, and military tactics toward Taiwan and other countries. In particular, China’s policies have led many countries and businesses to accelerate de-risking in key sectors and to limit exports of sensitive technology to China, which is further hindering PRC leaders’ goals for technology-enabled economic and military development.

The PRC combines its economic heft with its growing military power and its diplomatic and technological dominance for a coordinated approach to strengthen CCP rule, secure what it views as its sovereign territory and regional preeminence, and pursue global power. In particular, Beijing uses these whole-of-government tools to compel others to acquiesce to its preferences, including its assertions of sovereignty over Taiwan.

- In 2024, following Taiwan’s presidential and legislative election, Beijing will continue to apply military and economic pressure as well as public messaging and influence activities while promoting long-term cross-Strait economic and social integration to induce Taiwan to move toward unification. Taiwan is a significant potential flashpoint for confrontation between the PRC and the United States as Beijing claims that the United States is using Taiwan to undermine China’s rise. Beijing will use even stronger measures to push back against perceived increases in U.S. support to Taiwan.
- In the South China Sea, Beijing will continue to use its growing military and other maritime capabilities to try to intimidate rival claimants and to signal it has control over contested areas. Similarly, China is pressing Japan over contested areas in the East China Sea.
- Beijing aims to expand its influence abroad and be viewed as a champion of global development via several multinational forums and PRC-branded initiatives such as the Belt and Road Initiative, the Global Development Initiative, and the Global Security Initiative. China is promoting an alternative to existing, often Western-dominated international development and security forums in favor of norms that support state sovereignty and place political stability over individual rights. As part of this effort, Beijing seeks to champion development and security in the Global South—areas that Beijing perceives are receptive to engagement with China because of shared historical experiences under colonial and imperialistic oppression—as a way to build global influence; demonstrate leadership; and expand its economic, diplomatic, and military presence.

Beijing is balancing the level of its support to Moscow to maintain the relationship without incurring risk to its own economic and diplomatic interests. In return, China is securing favorable energy prices and greater access to the Arctic.

- The PRC is providing economic and security assistance to Russia’s war in Ukraine through support to Russia’s defense industrial base, including by providing dual-use material and components for weapons. Trade between China and Russia has been increasing since the start of the war in Ukraine, and PRC exports of goods with potential military use rose more than threefold since 2022.

Economics
During the next few years, China’s economy will slow because of structural barriers and Beijing’s unwillingness to take aggressive stimulus measures to boost economic growth. Beijing understands its problem but is avoiding reforms at odds with Xi’s prioritization of state-directed investment in manufacturing and industry. A slower Chinese economy probably would depress commodity prices worldwide, erode export competitiveness of countries that directly compete against China, and slow global growth, but it is unlikely to curtail Beijing’s spending on state priorities.

- China’s slowing economy could create resource constraints in the long run and force it to prioritize spending between social issues, industrial policy, military, and overseas lending.
- Xi is prioritizing what he deems “high-quality growth”—which includes greater self-sufficiency in strategic sectors and a more equitable distribution of wealth—replacing the focus on maximizing GDP growth, while also attempting to mitigate the threat of U.S. sanctions and unhappiness with semiconductor export controls.

Technology
China seeks to become a world S&T superpower and to use this technological superiority for economic, political, and military gain. Beijing is implementing a whole-of-government effort to boost indigenous innovation and promote self-reliance, and is prioritizing advanced power and energy, AI, biotechnology, quantum information science, and semiconductors. Beijing is trying to fast-track its S&T development through investments, intellectual property (IP) acquisition and theft, cyber operations, talent recruitment, scientific and academic collaboration, and illicit procurements.

- In 2023, a key PRC state-owned enterprise has signaled its intention to channel at least $13.7 billion into emerging industries such as AI, advanced semiconductors, biotechnology, and new materials. China also announced its Global AI Governance Initiative to bolster international support for its vision of AI governance.
- China now rivals the United States in DNA-sequencing equipment and some foundational research. Beijing’s large volume of genetic data potentially positions it to lead in precision medicine and agricultural biotechnology applications.
- China is making progress in producing advanced chips for cryptocurrency mining and cellular devices at the 7-nanometer (nm) level using existing equipment but will face challenges achieving high-quality, high-volume production of cutting-edge chips without access to extreme ultraviolet lithography tools. By 2025, 40 percent of all 28-nm legacy chips are projected to be produced in China, judging from the number of new factories expected to begin operating during the next two years.

WMD
China remains intent on orienting its nuclear posture for strategic rivalry with the United States because its leaders have concluded their current capabilities are insufficient. Beijing worries that bilateral tension, U.S. nuclear modernization, and the People’s Liberation Army’s (PLA) advancing conventional capabilities have increased the likelihood of a U.S. first strike. As its nuclear force grows, Beijing’s confidence in its nuclear deterrent probably will bolster the PRC’s resolve and intensify conventional conflicts.

- China probably has completed construction of more than 300 new ICBM silos and has loaded at least some of those silos with missiles.

China probably possesses capabilities relevant to chemical and biological warfare (CBW) that pose a threat to U.S., allied, and partner forces as well as civilian populations.

Military
Beijing will focus on building a fully modernized national defense and military force by 2035 and for the PLA to become a world-class military by 2049. In the meantime, the CCP hopes to use the PLA to secure what it claims is its sovereign territory, to assert its preeminence in regional affairs, and to project power globally, particularly by being able to deter and counter an intervention by the United States in a cross-Strait conflict. However, China lacks recent warfighting experience, which probably would weaken the PLA’s effectiveness and leaders’ willingness to initiate a conflict. In addition, PRC leaders almost certainly are concerned about the ongoing impact of corruption on the military’s capabilities and reliability, judging from a purge of high-level officers including the defense minister in 2023.

- The PLA has fielded modern systems and improved its competency to conduct joint operations that will threaten U.S. and allied forces in the western Pacific. It operates two aircraft carriers and is expected to commission its most advanced carrier in 2024, operates a host of ballistic and cruise missiles as well as the DF-17 hypersonic glide vehicle, and is fielding fifth-generation fighter aircraft.
- PLA ground forces have conducted increasingly realistic training scenarios to improve their readiness and ability to execute operations, including a potential cross-Strait invasion.

The PLA is developing and deploying new technologies to enhance its capability to process and use information at scale and machine speed, allowing decisionmakers to plan, operate, and support cross-domain unconventional and asymmetrical fighting. The PLA is researching various applications for AI, including support for missile guidance, target detection and identification, and autonomous systems.

- The PLA is accelerating the incorporation of command information systems, providing forces and commanders with enhanced situational awareness and decision support to more effectively carry out joint missions and tasks.

The PLA will continue to pursue the establishment of overseas military installations and access agreements in an attempt to project power and protect China’s interests abroad. Beyond developing its military base in Djibouti and its military facility at Ream Naval Base in Cambodia, Beijing reportedly is considering pursuing military facilities in multiple locations, including—but not limited to—Burma, Cuba, Equatorial Guinea, Pakistan, Seychelles, Sri Lanka, Tajikistan, Tanzania, and the UAE.

For at least a decade, Beijing and Moscow have used high-profile, combined military activities to signal the strength of the China–Russia defense relationship but have made only minor enhancements to interoperability in successive exercises.

Space
China remains committed to becoming a world-class space leader and continues to demonstrate its growing prowess by deploying increasingly capable space systems and working towards ambitious scientific feats. By 2030, China probably will achieve world-class status in all but a few space technology areas.

- Space-based intelligence, surveillance, and reconnaissance (ISR), as well as position, navigation, and timing, and satellite communications are areas the PLA continues to improve upon to close the perceived gap between itself and the U.S. military.
- In early 2023, China’s Manned Space Agency announced its intention to land astronauts on the Moon around 2030 and is engaging countries to join its lunar research station effort as part of its broader attempt to develop an alternative bloc to the U.S.-led Artemis Accords.
- China’s commercial space sector is growing quickly and is on pace to become a major global competitor by 2030. For example, China is developing its own low-earth orbit (LEO) satellite Internet service to compete with Western commercial satellite Internet services.

Counterspace operations will be integral to potential PLA military campaigns, and China has counterspace-weapons capabilities intended to target U.S. and allied satellites. China already has fielded ground-based counterspace capabilities including electronic warfare (EW) systems, directed energy weapons, and antisatellite (ASAT) missiles intended to disrupt, damage, and destroy target satellites.

- China also has conducted orbital technology demonstrations, which while not counterspace weapons tests, prove China’s ability to operate future space-based counterspace weapons.

Cyber
China remains the most active and persistent cyber threat to U.S. Government, private-sector, and critical infrastructure networks. Beijing’s cyber espionage pursuits and its industry’s export of surveillance, information, and communications technologies increase the threats of aggressive cyber operations against the United States and the suppression of the free flow of information in cyberspace.

- PRC operations discovered by the U.S. private sector probably were intended to pre-position cyber attacks against infrastructure in Guam and to enable disrupting communications between the United States and Asia.
- If Beijing believed that a major conflict with the United States were imminent, it would consider aggressive cyber operations against U.S. critical infrastructure and military assets. Such a strike would be designed to deter U.S. military action by impeding U.S. decisionmaking, inducing societal panic, and interfering with the deployment of U.S. forces.
- China leads the world in applying surveillance and censorship to monitor its population and repress dissent. Beijing conducts cyber intrusions targeted to affect U.S. and non-U.S. citizens beyond its borders—including journalists, dissidents, and individuals it views as threats—to counter views it considers critical of CCP narratives, policies, and actions.

Malign Influence Operations
Beijing is expanding its global covert influence posture to better support the CCP’s goals. The PRC aims to sow doubts about U.S. leadership, undermine democracy, and extend Beijing’s influence. Beijing’s information operations primarily focus on promoting pro-China narratives, refuting U.S.-promoted narratives, and countering U.S. and other countries’ policies that threaten Beijing’s interests, including China’s international image, access to markets, and technological expertise.

- Beijing’s growing efforts to actively exploit perceived U.S. societal divisions using its online personas move it closer to Moscow’s playbook for influence operations.
- China is demonstrating a higher degree of sophistication in its influence activity, including experimenting with generative AI. TikTok accounts run by a PRC propaganda arm reportedly targeted candidates from both political parties during the U.S. midterm election cycle in 2022.
- Beijing is intensifying efforts to mold U.S. public discourse—particularly on core sovereignty issues, such as Hong Kong, Taiwan, Tibet, and Xinjiang. The PRC monitors Chinese students abroad for dissident views, mobilizes Chinese student associations to conduct activities on behalf of Beijing, and influences research by U.S. academics and think tank experts.

The PRC may attempt to influence the U.S. elections in 2024 at some level because of its desire to sideline critics of China and magnify U.S. societal divisions. PRC actors’ have increased their capabilities to conduct covert influence operations and disseminate disinformation. Even if Beijing sets limits on these activities, individuals not under its direct supervision may attempt election influence activities they perceive are in line with Beijing’s goals.

Intelligence Operations
China will continue to expand its global intelligence posture to advance the CCP’s ambitions, challenge U.S. national security and global influence, quell perceived regime threats worldwide, and steal trade secrets and IP to bolster China’s indigenous S&T sectors.

- Officials of the PRC intelligence services will try to exploit the ubiquitous technical surveillance environment in China and expand their use of monitoring, data collection, and advanced analytic capabilities against political security targets beyond China’s borders. China is rapidly expanding and improving its AI and big data analytics capabilities for intelligence operations.
- More robust intelligence operations also increase the risk that these activities have international consequences, such as the overflight of the United States by the high-altitude balloon in February 2023.

Challenges
Xi Jinping’s prioritization of security and stability for the CCP is undermining China’s ability to solve complex domestic problems and will impede achieving the CCP’s goal of becoming a major power on the world stage. China’s leaders probably are most concerned about corruption, demographic imbalances, and fiscal and economic struggles—all of which influence economic performance and quality of life, two key factors underpinning domestic support for the government and political stability.

- Beijing’s growing national security focus has generated new laws on data security and anti-espionage targeting foreign firms, driven a crackdown on PRC technology companies, and calls for all of China’s society to participate in counterintelligence activities.
- Xi continues to regularly reprimand, publicly warn, investigate, and conduct firings based on the dangers of corruption. However, anti-corruption efforts probably never will uproot underlying problems because of the unrivaled power of top party officials, and Xi’s insistence that the party apparatus has exclusive power to monitor and fight corruption.
- Despite an easing of restrictions on birth limits, China’s birth rate continues to decline. Marriage rates are on a similar downward trajectory, which will reinforce negative population trends and a shrinking labor force.
- Xi’s blending of domestic and foreign security threats is undermining China’s position and standing abroad, reducing Beijing’s ability to influence global perceptions and achieve its objectives. Beijing’s hardline approach to alleged separatism in Xinjiang, Hong Kong, and Tibet, as well as broader crackdowns on religion and dissent in China, have generated widespread global criticism of China’s human rights abuses and extraterritorial interference.

## Russia

Regional and Global Activities
Russia’s war of aggression against Ukraine has resulted in enormous damage at home and abroad, but Russia remains a resilient and capable adversary across a wide range of domains and seeks to project and defend its interests globally and to undermine the United States and the West. Russia’s strengthening ties with China, Iran, and North Korea to bolster its defense production and economy are a major challenge for the West and partners. Russia will continue to pursue its interests in competitive and sometimes confrontational and provocative ways and press to influence other countries in the post–Soviet space to varying extents.

- Russia almost certainly does not want a direct military conflict with U.S. and NATO forces and will continue asymmetric activity below what it calculates to be the threshold of military conflict globally. President Vladimir Putin probably believes that Russia has blunted Ukrainian efforts to retake significant territory, that his approach to winning the war is paying off, and that Western and U.S. support to Ukraine is finite, particularly in light of the Israel–HAMAS war.
- Putin has upended Russia’s geopolitical, economic, and military revival and damaged its international reputation with the large-scale invasion of Ukraine. Nevertheless, Russia is implementing policies to mitigate these costs and leveraging foreign relationships to minimize sanctions-related damage and rebuild its credibility as a great power.
- Moscow’s deep economic engagement with Beijing provides Russia with a major market for its energy and commodities, greater protection from future sanctions, and a stronger partner in opposing the United States. China is by far Russia’s most important trading partner with bilateral trade reaching more than $220 billion in 2023, already surpassing their record total 2022 volume by 15 percent.

Moscow will continue to employ all applicable sources of national power to advance its interests and try to undermine the United States and its allies, but it faces a number of challenges, such as severance from Western markets and technology and flight of human capital, in doing so. This will range from using energy to try to coerce cooperation and weaken Western unity on Ukraine, to military and security intimidation, malign influence, cyber operations, espionage, and subterfuge.

- Russia’s GDP is on a trajectory for modest growth in 2024 but its longer-term competitiveness has diminished in comparison to its pre-war outlook. Russia has increased social spending, which probably has reduced public backlash, and increased corporate taxes, which has provided enhanced budget flexibility and financing options.
- Moscow has successfully diverted most of its seaborne oil exports and probably is selling significant volumes above the G-7–led crude oil and refined product price caps, which came into effect in December 2022 and February 2023, respectively—in part because Russia is increasing its use of non-Western options to facilitate diversion of most of its seaborne oil exports and because global oil prices increased last year.
- Russia will retain significant energy leverage. In the first half of 2023, Russia was still the second-largest supplier of liquefied natural gas to Europe and announced reduction in its crude oil exports as part of its OPEC+ commitment.
- Russia is offsetting its decline in relations with the West by expanding ties to China, Iran, North Korea, and key Global South countries.
- The renewed efforts of Armenia, Moldova, and some Central Asian states to seek alternative partners highlight how the war has hurt Moscow’s influence, even in the post-Soviet space. Russia’s unwillingness to expend the resources and political capital to prevent Azerbaijan from reacquiring Nagorno-Karabakh from ethnic Armenians through a military offensive in September 2023 underscores how Moscow’s war in Ukraine has weakened its role as a regional security arbiter.

Conflict in Ukraine
Russia’s so-called special military operation against Ukraine has incurred major, lasting costs for Russia, failed to attain the complete subjugation of Ukraine that Putin initially sought, and rallied the West to defend against Russian aggression. Russia has suffered more military losses than at any time since World War II—roughly 300,000 casualties and thousands of tanks and armored combat vehicles.

- The Russian military has and will continue to face issues of attrition, personnel shortages, and morale challenges, though its reliance on mines, prepared defensive positions, and indirect fires has helped it blunt Ukraine’s offensives in 2023.
- Nonetheless, this deadlock plays to Russia’s strategic military advantages and is increasingly shifting the momentum in Moscow’s favor. Russia’s defense industry is significantly ramping up production of a panoply of long-range strike weapons, artillery munitions, and other capabilities that will allow it to sustain a long high-intensity war if necessary. Meanwhile, Moscow has made continual incremental battlefield gains since late 2023, and is benefitting from uncertainties about the future of Western military assistance.

Military
Moscow’s military forces will face a multi-year recovery after suffering extensive equipment and personnel losses during the Ukraine conflict. Moscow will be more reliant on nuclear and counterspace capabilities for strategic deterrence as it works to rebuild its ground force. Regardless, Russia’s air and naval forces will continue to provide Moscow with some global power projection capabilities.

- Moscow’s announced plans to massively expand its ground forces almost certainly will fall short, but nonetheless will over time result in a larger even if not qualitatively better military. Russia has been successfully recruiting record numbers of contract enlisted personnel by offering significant benefits and manipulating propaganda about the war in Ukraine. Ongoing increases in defense spending probably will provide sufficient funding to gradually increase manpower without Moscow having to resort to mobilizing reservists.

Russian Private Military and Security Companies and Paramilitary Activities
Russia will rely on private military and security companies (PMSCs) and paramilitary groups to achieve its objectives on the battlefield in Ukraine, to augment Russian forces, to move weapons and to train fighters, to hide Moscow’s hand in sensitive operations, and to project influence and power in the Middle East and Africa.

WMD
Russia will continue to modernize its nuclear weapons capabilities and maintains the largest and most diverse nuclear weapons stockpile. Moscow views its nuclear capabilities as necessary for maintaining deterrence and achieving its goals in a potential conflict against the United States and NATO, and it sees this as the ultimate guarantor of the Russian Federation.

- Russia’s inability to achieve quick and decisive battlefield wins, coupled with Ukrainian strikes within Russia, continues to drive concerns that Putin might use nuclear weapons. In 2023, Putin publicly touted his willingness to move nuclear weapons to Belarus in response to a longstanding request from Minsk.
- Moscow will continue to develop long-range nuclear-capable missiles and underwater delivery systems meant to penetrate or bypass U.S. missile defenses. Russia is expanding and modernizing its large and diverse set of nonstrategic systems, which are capable of delivering nuclear or conventional warheads, because Moscow believes such systems offer options to deter adversaries, control the escalation of potential hostilities, and counter U.S. and Allied conventional forces.

Russia will continue to pose a CBW threat. Scientific institutes there have researched and developed CBW capabilities, including technologies to deliver CBW agents. Russia retains an undeclared chemical weapons program and has used chemical weapons at least twice during recent years: in assassination attempts with Novichok nerve agents, also known as fourth-generation agents, against Russian opposition leader Aleksey Navalny in 2020 and against UK citizen Sergey Skripal and his daughter Yuliya Skripal on UK soil in 2018.

Cyber
Russia will pose an enduring global cyber threat even as it prioritizes cyber operations for the Ukrainian war. Moscow views cyber disruptions as a foreign policy lever to shape other countries’ decisions and continuously refines and employs its espionage, influence, and attack capabilities against a variety of targets.

- Russia maintains its ability to target critical infrastructure, including underwater cables and industrial control systems, in the United States as well as in allied and partner countries.

Malign Influence Operations
Russia will remain a serious foreign influence threat because of its wide-ranging efforts to try to divide Western alliances, undermine U.S. global standing, and sow domestic discord, including among voters inside the United States and U.S. partners around the world. Russia’s war in Ukraine will continue to feature heavily in its messaging.

- Moscow views U.S. elections as opportunities and has conducted influence operations for decades and as recently as the U.S. midterm elections in 2022. Russia is contemplating how U.S. electoral outcomes in 2024 could impact Western support to Ukraine and probably will attempt to affect the elections in ways that best support its interests and goals.
- Russia’s influence actors have adapted their efforts to better hide their hand, and may use new technologies, such as generative AI, to improve their capabilities and reach into Western audiences.

Space
Russia will remain a key space competitor despite facing difficulties from the effects of additional international sanctions and export controls, domestic space-sector problems, and increasingly strained competition for program resources within Russia. Moscow is prioritizing assets critical to its national security and integrating space services—such as communications; positioning, navigation, and timing; and ISR.

- Moscow employs its civil and commercial remote-sensing satellites to supplement military-dedicated capabilities and has warned that other countries’ commercial infrastructure in outer space used for military purposes can become a legitimate target.
- Russia continues to train its military space elements and field new antisatellite weapons to disrupt and degrade U.S. and allied space capabilities. It is expanding its arsenal of jamming systems, directed energy weapons, on-orbit counterspace capabilities, and ground-based ASAT missiles that are designed to target U.S. and allied satellites.
- Russia is investing in EW and directed energy weapons to counter Western on-orbit assets and continues to develop ground-based ASAT missiles capable of destroying space targets in LEO.

Challenges
While Putin portrays the failure of the PMSC Vagner revolt in June 2023 as evidence that Russian society is united behind his leadership, he continues to face domestic challenges, including support from elites, economic pressure, and the burden of the war in Ukraine.

- Moscow probably needs to balance increased military spending with the need for additional revenue without overburdening private and state-backed firms or the Russian public with the cost of the war. Russia faces long-term problems including a lack of foreign investment, particularly in its energy sector.

## Iran

Regional and Global Activities
Iran will continue to threaten U.S. interests, allies, and influence in the Middle East and intends to entrench its emergent status as a regional power while minimizing threats to the regime and the risk of direct military conflict. Tehran will try to leverage recent military successes through its emboldened threat network, diplomatic gains, its expanded nuclear program, and its military sales to advance its ambitions, including by trying to further bolster ties with Moscow. Iran will seek to use the Gaza conflict to denounce Israel, decry its role in the region, and try to dissuade other Middle Eastern states from warming ties with Israel, while trumpeting Iran’s own role as the champion of the Palestinian cause. However, Iran’s position on the conflict is unlikely to mask the challenges that it faces internally, where economic underperformance and societal grievances still test the regime.

- Decades of cultivating ties, providing support, funding, weapons, and training to its partners and proxies around the Middle East, including Lebanese Hizballah, the Huthis, and Iranian-backed militias in Iraq and Syria, will enable Tehran