# Whitepaper Name Goes Here
S U B H E A D
## 2023 Hospitality Sector Threat Landscape
T R U S T W A V E  T H R E A T  I N T E L L I G E N C E 
B R I E F I N G  A N D  M I T I G A T I O N  S T R A T E G I E S 

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Generative AI and Large Language Models (LLMs)](#generative-ai-and-large-language-models-llms)
- [Contactless Technology](#contactless-technology)
- [Third-party Risk and Exposure](#third-party-risk-and-exposure)
- [Dissecting the Attack Flow for Hospitality](#dissecting-the-attack-flow-for-hospitality)
- [Attack Flow Overview](#attack-flow-overview)
- [Attack Flow Steps](#attack-flow-steps)
- [Initial Foothold: Phishing and Business Email Compromise (BEC)](#initial-foothold-phishing-and-business-email-compromise-bec)
- [Initial Foothold: Logging in](#initial-foothold-logging-in)
- [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
- [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
- [Initial Payload](#initial-payload)
- [Expansion / Pivoting](#expansion--pivoting)
- [Malware: Infostealers](#malware-infostealers)
- [Malware: RATs](#malware-rats)
- [Malware: Ransomware](#malware-ransomware)
- [Exfiltration / Post Compromise](#exfiltration--post-compromise)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
- [Threat Groups](#threat-groups)
- [ALPHV/BlackCat](#alphvblackcat)
- [BianLian](#bianlian)
- [Black Basta](#black-basta)
- [BlackShadow](#blackshadow)
- [Clop](#clop)
- [Conti](#conti)
- [Hive](#hive)
- [Karakurt](#karakurt)
- [LockBit](#lockbit)
- [LV](#lv)
- [Magniber](#magniber)
- [Medusa](#medusa)
- [Play](#play)
- [Qillin, Royal](#qillin-royal)
- [Ragnar](#ragnar)
- [Vice Society](#vice-society)

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
Contents
Executive Summary‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 1
Emerging and Prominent Trends‧
 ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  5
Generative AI and Large Language Models (LLMs)‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 6
Contactless Technology‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  8
Third-party Risk and Exposure ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 10
Dissecting the Attack Flow for Hospitality ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 12
Attack Flow Overview‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 13
Attack Flow Steps‧
 ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 13
Initial Foothold: Phishing and Business Email Compromise (BEC) ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  15
Initial Foothold: Logging in‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 19
Initial Foothold: Vulnerability Exploitation‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  21
Initial Foothold: Supply Chain ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 25
Initial Payload‧
 ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 27
Expansion / Pivoting‧
 ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 30
Malware: Infostealers‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ 
32
Malware: RATs‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 35
Malware: Ransomware ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 39
Exfiltration / Post Compromise‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 42
Key Takeaways and Recommendations‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 44
TOC
SEPTEMBER 2023
3
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
Appendix/Reference ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 48
Threat Groups‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 49
ALPHV/BlackCat  ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 49
BianLian  ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 49
Black Basta ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 50
BlackShadow  ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 50
Clop ‧
 ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 50
Conti ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  51
Hive‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  51
Karakurt ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  51
LockBit ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 52
LV‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 52
Magniber‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ ‧ 
53
Medusa‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 53
Play ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 53
Qillin, Royal‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 54
Ragnar‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 54
Vice Society‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 54
<a id="executive-summary"></a>
## Executive Summary
2
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
The global hospitality industry employs nearly 
300 million individuals worldwide, and provides a place 
to stay, eat, and relax for billions of people all over the 
world. Spanning from hotels to restaurants to cruise 
ships, the industry has become deeply woven into our 
everyday routines, making its cybersecurity threat 
landscape especially vast, complex, and critical. 
Nearly 31% of hospitality organizations have reported a data breach in their 
company’s history, of which 89% have been affected more than once in a 
year, according to a report by Cornell University and FreedomPay. These 
cyberattacks have resulted in the loss of sensitive data, financial losses, and 
reputational damage. While the average cost of a hospitality breach ($3.4M) 
is lower than the cross-industry average ($4.4M), the impact on reputation 
can cause significant harm to the bottom line due to the highly competitive 
nature of the industry.
A surge towards digital technologies prompted by the pandemic, along with 
the overall resurgence of the hospitality industry, has rendered hospitality 
companies well-acquainted with cyberattacks.
In February 2022, the global hotel and resort company Marriott was targeted 
through social engineering, and the attackers made out with 20 gigabytes 
of sensitive customer data, including personal information and credit card 
numbers. In September 2022, InterContinental Hotels Group (IHG) was hit by 
a cyberattack that downed its booking systems and mobile apps. 
With over 250 security researchers across the globe, the Trustwave 
SpiderLabs team puts its resources to task in looking into what leads to these 
breaches. We are uniquely positioned to do so, as we perform over 100,000 
hours of penetration tests and uncover tens of thousands of vulnerabilities 
annually. We also have a dedicated email security team analyzing millions 
of phishing URLs validated daily, including 4,000-8,000 a day that are 
uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec 
disciplines, including Continuous Threat Hunting, Forensics and Incident 
Response, Malware Reversal, and Database Security, give us insight into 
identifying how these breaches occur as well as mitigations and controls that 
your organization can put in place to prevent these compromises.
31% 
OF HOSPITALITY 
ORGANIZATIONS HAVE 
REPORTED A DATA 
BREACH IN THEIR 
COMPANY’S HISTORY, 
OF WHICH 89% HAVE 
BEEN AFFECTED MORE 
THAN ONCE IN A YEAR
3.4
million 
THE AVERAGE COST OF A 
HOSPITALITY BREACH
3
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
There are a few factors that make the hospitality industry’s cybersecurity 
threat profile especially unique, including: 
	
- **Seasonal and Less Sophisticated Workforce**: 
The hospitality sector 
employs a diverse workforce, with seasonal and less sophisticated staff 
often engaged during peak periods to meet demand. This presents a 
distinct risk of insider threat, intentional or not, due to the challenge of 
providing consistent security training to a continually changing group of 
employees.  
	
- **Constant User Turnover**: 
Hospitality establishments encounter a fresh 
set of users virtually every day. This ongoing cycle demands consistent 
uptime, addresses bandwidth constraints, and strives to minimize potential 
exposure to security threats.  
	
- **Dirty Networks**: 
Given the substantial volume of network users, whether 
they’re hotel guests or individuals connecting to coffee shop Wi-Fi, 
organizations within hospitality must operate under the assumption that 
their networks are highly susceptible to attacks due to the sheer number 
of users. There are hesitancies to deploy patches and configuration 
changes that might have an adverse impact on day-to-day operations.    
	
- **Physical Security Concerns**: 
Unlike conventional office buildings where 
employee access is typically controlled through access cards, hospitality 
establishments face cybersecurity risks due to the accessibility of 
hardware by guests. For instance, the server closet in a hotel could be left 
unlocked and easily accessible or a thumb drive could easily be inserted 
into a nearby device.  
	
- **Franchise Model**: 
The franchise framework leads to disparities in 
policy consistency and implementation across the industry, including 
cybersecurity measures. Different franchisers and franchisees adopt 
varied business models, resulting in divergent cybersecurity practices. 
Given these circumstances, it is crucial for the hospitality sector to minimize 
its risk and prioritize information protection. This report’s objective is to 
thoroughly examine the multitude of threats that pose challenges to the 
hospitality industry.  
We will begin by highlighting the significant trends currently affecting the 
industry, including contactless technology, generative AI, and third-party 
risk. Subsequently, we will analyze the attack flow specific to the hospitality 
sector, offering insight on specific threat actors, actionable intelligence, and 
recommended mitigations for each stage to illustrate how organizations can 
proactively identify and prevent attacks to avoid lasting impact.
4
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
In this report, we will examine many of the most prevalent threat tactics and 
threat actors operating across hospitality and throughout the attack chain, 
including:
THREAT ACTORS 
	
- LockBit
	
- Medusa
	
- Vice Society
	
- BianLian
	
- BlackBasta
	
- Qillin, Royal
	
- Karakurt
	
- Ragnar
	
- Alphv
	
- Clop
	
- Conti
	
- Lv
	
- Play
	
- Hive
	
- BlackShadow 
THREAT TACTICS 
	
- Email-borne Malware 
(Emotet, Qakbot)
	
- Phishing (IPFS, Image Based, 
Brand Impersonation) 
	
- Scams (Fake Order Scams, 
Extortion Scams) 
	
- BEC (e.g., Payroll Diversion) 
	
- Malware  
	
- Credential Access (Bruteforcing, 
Auctioned Accounts) 
	
- Vulnerability Exploitation
For additional information about the most prevalent threat actors, please go 
to the Appendix. 
<a id="emerging-and-prominent-trends"></a>
## Emerging and Prominent Trends
6
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
<a id="generative-ai-and-large-language-models-llms"></a>
## Generative AI and Large Language 
Models (LLMs)
The Threat
Generative AI and Large Language Models (LLMs) continue to take the world 
by storm. Generative AI is a powerful tool that is being increasingly used 
by the hospitality sector to improve the guest experience with services like 
chatbots or language translation. Following the Covid-19 pandemic, many 
hospitality entities began leveraging chatbots to interact with guests and 
provide 24/7 customer support.
However, similar to other industries, using this technology also raises 
concerns about data privacy and security. Hospitality businesses need 
to carefully consider the risks and benefits of using generative AI before 
deploying it.
How This Could Affect You
Generative AI systems can be used to collect and store large amounts 
of data about guests, including personal information, travel preferences, 
identification documents, and payment details. This can either be through 
employees inputting the information, or by the guests themselves through 
use of a chatbot. If exposed or accessed, this data could be used by 
cybercriminals to commit identity theft, fraud, or other crimes.
The hospitality industry is in the business of knowing its guests and their 
preferences. As a result, tailored and personalized marketing is a core 
component to stay competitive. As more business intelligence and customer 
analytics platforms integrate generative AI into their tools, the hospitality 
sector must vet and audit the security protections within those systems.
Additionally, social engineering attacks can become more sophisticated 
as LLMs have the capability to create highly personalized and targeted 
messages.
While the potential benefits of these tools could be substantial, the security 
of these systems has not yet been proven. Therefore, it is essential to adopt 
a risk-benefit approach and carefully consider the implications with the CISO 
leading the way.
ARTIFICIAL 
INTELLIGENCE AND 
GENERATIVE AI
Unique implications and risks 
due to the sensitive nature of 
the data potentially being shared 
with these tools, as well as 
advances in phishing.
7
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
What Trustwave SpiderLabs Is Seeing
Trustwave is monitoring the progress and attacker implementation of 
generative AI and LLMs. Based on Trustwave's observations to date, the 
primary areas of concern are the increased speed and quality at which 
attackers can create phishing emails and exploit code can be enhanced. 
This ability will require security vendors to adjust their detection and 
response capabilities accordingly.
While LLMs and other technologies categorized as AI seem to have matured 
at a near-miraculous rate over the past year, Trustwave doesn’t have any 
indication that LLMs have "changed the game" in any substantive way beyond 
the existing cat-and-mouse scenarios we've always worked against in the 
security industry. Attackers are turning to tools like WormGPT and FraudGPT to 
bypass security controls, as outlined in a recent SpiderLabs blog.
Trustwave continues to monitor this emerging trend, tracking the novel ways 
threat actors use it and in opportunities for risk reduction on the defenders' 
side. While we explore methods of integrating LLMs to augment our workflow, 
we see promising trends in identifying PoC exploit code, reverse-engineering 
malware, and processing large amounts of log files to identify and prioritize 
threats that must be addressed.
Mitigations to Reduce Risk
	
- Evaluate your security solutions with generative AI and LLMs 
in mind. Choose security tools or partners that can detect AI-
generated threats like advanced phishing.
	
- Create robust internal policies, controls, and employee training for 
proper data usage and data sharing to help minimize the risk of 
data breaches. 
	
- Consider instituting an internal AI Infosec working group across 
relevant teams (like Legal, Privacy, IT, Marketing, et al.) to deal 
with governance and data sharing guidelines.
	
- Carefully vet your supply chain and inspect their policies and 
controls around use of your corporate or customer data in their 
generative AI and LLM applications.
	
- Monitor generative AI systems for suspicious activity and keep 
them up to date.
<a id="contactless-technology"></a>
## Contactless Technology
The Threat
During and following the pandemic, the hospitality industry rapidly adopted 
contactless technology. This is due to the many benefits that contactless 
technology offers, such as improved customer or guest experience, 
competitive differentiation, increased efficiency, and during the pandemic, a 
reduced risk of infection.
For example, for hotels, contactless check-in, payments, and room access 
have become industry standard. Across the restaurant industry, ordering 
food, making reservations, and paying is increasingly going mobile. Concert 
venues and sporting events have accelerated the use of mobile ticketing and 
contactless payments.
While these shifts have led to improved efficiency, they’ve also introduced 
new security challenges, such as the need to protect sensitive data and 
prevent fraud. 
How This Could Affect You
With hotels bowing to the demand of their customers, 80% of which prefer 
using mobile technology, mobile has now become a prime attack surface for 
the hospitality industry.
Frequently, these attacks commence with cunning social engineering 
tactics like phishing emails, which enable the introduction of malware into 
the hospitality organization’s network. Compounding this issue, the reliance 
on hospitality Wi-Fi networks poses another avenue for exploitation, as 
evidenced by past instances like the DarkHotel cyber espionage campaign. 
Due to the interconnectedness of the systems, a breach can take a 
hospitality organization’s operations fully offline. For example, in December 
2021, Nordic Choice Hotels fell victim to a ransomware attack that resulted 
in the shutdown of corporate systems, check-in counters, and internet-
connected devices. Hotel staff were left to check guests into their rooms 
with pen and paper.
What Trustwave SpiderLabs Is Seeing
In most hotels and hospitality locations, customers and guests will regularly 
encounter contactless technologies and IoTs such as electronic key cards, 
kiosks, digital billboards, electronic gaming devices, online reservations 
systems, smart TVs, tablets, online menus, and mobile PoS (point-of-sale) 
devices. For a threat actor, these are enticing avenues for attack.
In fact, based on our research, a threat actor does not even need to be onsite 
to attack hospitality devices and systems. Trustwave SpiderLabs has seen 
a multitude of exposed ports, services, and applications from hospitality 
organizations that are publicly available on the Internet. Prevalent ones are 
network devices, property management systems, backup power controllers, 
power distribution systems, phone systems, smart energy management 
systems, and IP cameras. 

MOBILE HAS 
NOW BECOME A 
PRIME ATTACK 
SURFACE FOR 
THE HOSPITALITY 
INDUSTRY
9
2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies
We have also seen less prevalent exposures, but exposures nonetheless, 
in equally critical systems like fingerprint readers, wind river systems, air 
conditioning and water control systems, HVAC controls, RDP sessions, and 
hotel power backup devices. Needless to say, some of these are systems 
that support the operations of the organizations and could potentially cause 
major disruption of services if successfully attacked and compromised.
The surge of technological advancements in this sector continues to expand 
the attack surface and opens fresh possibilities and opportunities, both 
for the business and the threat actors. For example, newer features like 
contactless table payments and smartphone-card reader integrations offer 
a seamless experience to businesses and customers alike but also introduce 
new vectors of attack. It's critical to rigorously scrutinize these technologies' 
security aspects