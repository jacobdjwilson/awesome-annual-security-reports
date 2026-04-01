# 2024 State of Threat and Exposure Management Report

Organization: NopSec  
Year: 2024  
[www.nopsec.com](http://www.nopsec.com)

This 2024 iteration of NopSec annual state of vulnerability management focuses on the crossroad between threat-based prioritization and contextual risk management, delving deeper on how NopSec Risk Score prioritizes riskier vulnerabilities and how vulnerabilities CVE and ATT&CK framework can be mapped together to expand the threat and contextual risk vision of attack surface management. This report is divided into three parts: how the vulnerability landscape is measured in terms of vulnerability prevalence and remediation efficiency, how the NopSec Risk Score works in real-life vulnerability scenarios, and how CVE and ATT&CK taxonomies are mapped to expand the risk scenarios beyond vulnerability management.

## Table of Contents
- [VOLUME 1: Measuring the Vulnerability Landscape](#volume-1-measuring-the-vulnerability-landscape)
- [VOLUME 2: NopSec Risk Score Calculations In Real Life Scenarios](#volume-2-nopsec-risk-score-calculations-in-real-life-scenarios)
- [VOLUME 3: Mapping MITRE ATT&CK Taxonomies to CVEs](#volume-3-mapping-mitre-attck-taxonomies-to-cves)
- [APPENDIX](#appendix)

---

## VOLUME 1: MEASURING THE VULNERABILITY LANDSCAPE

An independent analysis of real-world vulnerability and remediation data in collaboration with the Cyentia Institute.

THIS SECTION analyzes 36 million vulnerabilities detected by organizations using NopSec to help prioritize remediation efforts. We begin by examining the prevalence of those vulnerabilities across assets to determine which ones are most common. Then we measure how quickly those vulnerabilities are remediated and what factors speed up or slow down that process. The section closes by identifying examples of vulnerabilities that are prone to slip through the cracks of traditional prioritization strategies so your organization won’t waste valuable time and energy chasing after the wrong things.

### Vulnerability Prevalence

We measure vulnerability prevalence in three basic ways:
1. Vulnerabilities published on the CVE List.
2. Enterprise assets affected by those vulnerabilities.
3. The total number of detected vulnerabilities (open and closed) across all assets.

![Figure 1: Prevalence of 15 most common vendors across CVEs, assets, and vulnerabilities]

Microsoft immediately jumps out from Figure 1. That single vendor is behind 11% of all published CVEs, which together affect 55% of all organizational assets and comprise 40% of all vulnerabilities detected.

### Vulnerability Exploitation

![Figure 2: Commonality of vulnerability factors relevant to exploitation]

In the top half, we see that vulnerabilities that enable phishing and/or remote attacks are quite common, affecting over half of all organizational assets. The enablement of lateral movement is (thankfully) less common among CVEs and detected vulnerabilities but still affects a quarter of assets.

### Risk Ratings

![Figure 3: Breakdown of CVSSv3 and NopSec Business Risk Scores for detected vulnerabilities]

According to CVSS, over 70% of all detected vulnerabilities are rated high or critical severity. That’s unrealistic from a risk assessment standpoint. NopSec assigns a Business Risk Score to each vulnerability; a much more manageable 20% of vulnerabilities are rated as high or critical.

### Remediation Timelines

Based on a survival analysis of all vulnerabilities in our dataset, we calculate the overall average time-to-remediation at 212 days.

![Figure 4: Comparison of vulnerability remediation timelines among asset categories]
![Figure 5: Effect of vulnerability attributes on average remediation timelines]
![Figure 6: Comparison of vendors based on vulnerability prevalence and remediation speed]
![Figure 7: Vulnerability remediation timelines for NopSec’s Business Risk Score ranges]

### Celebrity Vulnerabilities

![Figure 8: CVEs plotted by CVSSv3 vs. NopSec Business Risk Score with “celebrity vulns” highlighted in orange]
![Figure 9: CVEs plotted by NopSec Business Risk Score vs. prevalence across assets with “celebrity vulns” highlighted in orange]

---

## VOLUME 2: NOPSEC RISK SCORE CALCULATIONS IN REAL-LIFE SCENARIOS

For relevance, we selected vulnerabilities for further analysis from three main categories:
- Both celebrity and non-celebrity vulnerabilities with high NopSec score and low CVSSv3 score.
- Both celebrity and non-celebrity vulnerabilities with high CVSSv3 score and low NopSec risk score.
- Both celebrity and non-celebrity vulnerabilities with high NopSec risk score present in a high percentage of assets.

### 1. CVE-2022-22965 - Spring Framework JDK 9+ Remote Code Execution Vulnerability
The vulnerability is inherently important because the Spring framework is used by several software vendors. Our NopSec Risk Score is at 9.263. It is associated with public exploits, malware, and remote code execution.

### 2. CVE-2021-26084 - Atlassian Confluence Server and Data Center OGNL injection
The vulnerability is inherently important because the Atlassian Confluence platform is used in DevOps. Our NopSec Risk Score is at 9.282.

### 3. CVE-2021-44832 - Apache Log4J2 Remote Code Execution Vulnerability
The vulnerability is labeled as a celebrity vulnerability. Our NopSec Risk Score is at 3.835. It is not associated with working public exploits or malware.

### 4. CVE-2021-34527 - Windows Print Spooler Service Remote Code Execution Vulnerability
Known as “PrintNightmare.” Our NopSec Risk Score is at 9.279. It is associated with public exploits and malware.

### 5. CVE-2021-26855 - Microsoft Exchange Server Remote Code Execution Vulnerability
Known as “ProxyLogon.” Our NopSec Risk Score is at 9.275.

### 6. CVE-2023-35315 - Windows Layer-2 Bridge Network Driver Remote Code Execution Vulnerability
The vulnerability can be easily deprioritized because it does not have any public exploit code available. Our NopSec Risk Score is at 3.073.

### 7. CVE-2021-40444 - Microsoft MSHTML Remote Code Execution Vulnerability
The vulnerability has exploit code available and it has been leveraged as part of several ransomware campaigns. Our NopSec Risk Score is at 9.278.

---

## VOLUME 3: MAPPING MITRE ATT&CK TAXONOMIES TO CVES

The MITRE ATT&CK framework is a knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world observations of attacks. NopSec believes that defining novel relationships between CVE and ATT&CK taxonomies is a problem well suited for large language models (LLMs).

### ATT&CK Framework and LLMs
NopSec elected to use two different models to assist in mapping CVEs to ATT&CK techniques: Google Gemini and Bidirectional Encoder Representations from Transformers (BERT).

### Mapping CVE by ATT&CK Technique
![Table: CVE mapping based on BERT ATT&CK technique embedding]
![Table: CVE mapping based on Gemini ATT&CK technique embedding]

### Where do we go from here?
It’s clear from the results of our research that LLMs can complement our understanding of risk by providing relevant contextual information about the nature of a vulnerability.

### Why does this matter?
The techniques described above highlight the importance of mapping the vulnerability information that are first exploited by an attacker to the ATT&CK TTPs that are further developed down the attack chains.

### Conclusions
NopSec intends to leverage their proprietary threat intelligence feed to augment NVD CVE information. We think like hackers. We think you should too.

---

## APPENDIX

### Appendix A
Mapping CVE by ATT&CK Tactic and Technique.

### Appendix B
Mapping CVE by ATT&CK Technique with a Single Sentence.

[^1]: Footnote content here.

---

to establish a meaningful relationship. This method of mapping CVEs to ATT&CK techniques
relied on filtering based on tactics first. Due to this behavior the resulting TTPs output by the LLMs using this
technique did not accurately map to the vulnerability described by the CVE.

APPENDIX B

Mapping CVE by ATT&CK Technique with a Single Sentence

We encountered an interesting result when analyzing the mapping of CVEs to ATT&CK TTPs when comparing
the similarity between CVE descriptions and the ATT&CK technique description. In the case of CVE-2021-
26855, BERT, Gemini, and a human analyst all arrived at the same TTPs. This CVE was unique because the
CVE description consisted of a single sentence. Based on this outlier result, NopSec limited the CVE input data
to the first sentence of the CVE description when calculating similarity to TTPs, as captured in the results table
below.

www.nopsec.com

35

An analysis of the results didn’t provide much additional insight or improved accuracy. It appears that BERT is
more accurate when analyzing a limited amount of input text, which is in contrast to the Gemini framework.
However, neither BERT nor Gemini returned a substantial number of relevant ATT&CK TTPs when input data
was limited to a single sentence of a CVE vulnerability description.

www.nopsec.com

36

www.nopsec.com

www.nopsec.com

37