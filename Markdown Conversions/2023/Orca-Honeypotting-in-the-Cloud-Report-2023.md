# Honeypotting in the Cloud Report: Attacker Tactics and Techniques Revealed

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive Summary](#executive-summary)
- [Research Methodology](#research-methodology)
- [Research Findings](#research-findings)
  - [1. GitHub Honeypot](#1-github-honeypot)
  - [2. AWS S3 Bucket Honeypot](#2-aws-s3-bucket-honeypot)
  - [3. SSH Honeypot](#3-ssh-honeypot)
  - [4. HTTP Honeypot](#4-http-honeypot)
  - [5. DockerHub Honeypot](#5-dockerhub-honeypot)
  - [6. ECR Honeypot](#6-ecr-honeypot)
  - [7. Elasticsearch Honeypot](#7-elasticsearch-honeypot)
  - [8. Amazon EBS (AMI) Honeypot](#8-amazon-ebs-ami-honeypot)
  - [9. Redis Honeypot](#9-redis-honeypot)
- [Summary](#summary)
- [Key Recommendations](#key-recommendations)
- [About Orca Security](#about-orca-security)

---

## Foreword

> "Know thy enemy and know yourself; in a hundred battles, you will never be defeated.”
> — Chinese general Sun Tzu.

In an era where cloud computing has become an integral part of modern business operations, ensuring the security of cloud environments is of paramount importance. Cybercriminals are relentlessly seeking to exploit vulnerabilities and misconfigurations to gain unauthorized access to valuable resources. The more security teams can understand attacker tactics and techniques, the more effective they will be at defending themselves.

For this purpose, the Orca Research Pod launched a honeypot research project to simulate misconfigured resources in the cloud, and then monitor whether bad actors would take the bait while shedding light on the latest attack vectors and providing essential insights for fortifying cloud defenses.

---

## About the Orca Research Pod

The Orca Research Pod is a group of cloud security researchers that discover and analyze cloud risks and vulnerabilities to strengthen the Orca Cloud Security Platform and promote cloud security best practices. In addition, the Orca research team discovers and helps resolve vulnerabilities in cloud provider platforms so organizations can rely on a safe infrastructure in the cloud.

![Infographic showing 14+ vulnerabilities discovered on AWS, Azure, and Google Cloud, with a timeline of research findings from 2021 to 2023.]

---

## Executive Summary

### 1. Discovery is fast
In some ways, our study confirmed what is already widely known: attackers are constantly scanning the Internet for lucrative opportunities. What did surprise us however was how fast this was happening:

- On GitHub, attackers weaponized our leaked keys within minutes. It only took 2 minutes until one of our GitHub honeypot keys was used.
- The first access to our HTTP honeypot was within 3 minutes.
- We saw access to our SSH honeypot within 4 minutes. There were no attempts to use the key we planted, but we saw hundreds of attempts to install malware and cryptominers on our server.
- Our S3 Buckets were accessed in one hour and the keys were used within 8 hours.

### 2. Attackers target each resource differently
The more popular the resource, the easier it is to access, and the more likely it is to contain sensitive information -> the more attackers will do (automatic) reconnaissance.

Certain assets, such as SSH, are highly targeted for malware and cryptomining. We saw hundreds of attempts by attackers to install malware and cryptominers on our SSH honeypot.

### 3. Automated key protection cannot be relied on
Secrets are automatically locked down on GitHub but not on any of the other resources, such as ECR and S3 Buckets. Even if key permissions are locked down (as they were on GitHub), the key is not entirely blocked. Although the policy denies most permissions, an attacker can potentially still perform malicious actions on some services, such as RDS, EKS, and Elasticsearch.

### 4. No region is safe
Although we saw 50% of the AWS key exploitation in the US, usage also occurred in almost every other region, including Canada, Asia Pacific, Europe, and South America.

---

## Research Methodology

The purpose of this research was to achieve a better understanding of how quickly attackers find assets and use secrets in each scenario. 

**Data collection:**
Our research was conducted between January and May 2023. To set up our ‘honeypots’ and simulate misconfigured resources, we basically broke all security best practices:
1. We created a number of resources in different environments that allowed public or easy access.
2. We placed a secret—in this case AWS keys—in our honeypots.
3. We observed as attackers took the bait.

---

## Research Findings

### 1. GitHub Honeypot
We created a public repository with two Python files. One contained an AWS access key, and the second contained a bucket with an access key. 
- **Key Usage:** It took only 2 minutes before keys were exploited.
- **Tactics:** The majority of key usage was reconnaissance. "GetCallerIdentity" (25%) was the most used API call.

### 2. AWS S3 Bucket Honeypot
We created 13 public buckets using commonly used names and placed canary AWS keys inside.
- **Access:** After publishing the names, we saw the first access within one hour.
- **Tactics:** The most used action was `HEAD-BUCKET` to determine if a bucket exists and if permissions were available.

### 3. SSH Honeypot
We opened port 22 and allowed any user/password combination.
- **Access:** We saw access within 4 minutes.
- **Tactics:** We saw hundreds of attempts to install malware (Mirai variants) and cryptominers.

### 4. HTTP Honeypot
We created a machine with an open port 80 and a simple webpage containing an AWS key.
- **Access:** First access was within 3 minutes. No key usage was detected.

### 5. DockerHub Honeypot
We published a Docker image containing an AWS config file.
- **Result:** The image was never downloaded.

### 6. ECR Honeypot
We created a public registry in Amazon’s ECR.
- **Result:** After 4 months, we observed two actors downloading the images and initiating calls with our keys.

### 7. Elasticsearch Honeypot
We created a publicly accessible instance on port 9200.
- **Access:** Accessed within 2 hours.

### 8. Amazon EBS (AMI) Honeypot
We created a public snapshot of an EC2 VM with embedded keys.
- **Result:** No attackers accessed the honeypot.

### 9. Redis Honeypot
We exposed port 6379 to the Internet.
- **Access:** Accessed within 2.5 hours.
- **Tactics:** Attackers attempted to load modules (`MODULE LOAD ./red2.so`) to run cryptominers.

---

## Summary
![Table comparing access times, key usage, and attack vector popularity across all tested resources.]

---

## Key Recommendations
1. **Identify & Manage Your Secrets:** Use vaults and automatic identification to prevent exposure.
2. **Check for Secrets Before Deploying Code:** Use pre-commit hooks and secret scanning.
3. **Check Your Git History:** Ensure secrets are removed from the entire commit history, not just the latest commit.
4. **Set Public Access Only When Strictly Needed:** Continuously assess public exposure.
5. **Follow “Security by Obscurity”:** Use non-obvious usernames and asset names.
6. **Bolster Authentication and Limit Authorization:** Use MFA and the principle of least privilege.
7. **Monitor for Malicious Process Execution and Malware:** Watch for abnormal execution patterns.
8. **Assess and Patch Vulnerabilities:** Prioritize patching for internet-facing assets.
9. **Implement Port Hygiene:** Limit access to only required ports.
10. **Prioritize Protection of Your Crown Jewels:** Focus security efforts on the most critical data assets.

---

## About Orca Security
Orca’s agentless cloud security platform connects to your environment in minutes and provides 100% visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate.

[Watch a recorded demo or take our free cloud risk assessment.](https://orca.security)

*Copyright Orca Security 2023. Highly Confidential.*