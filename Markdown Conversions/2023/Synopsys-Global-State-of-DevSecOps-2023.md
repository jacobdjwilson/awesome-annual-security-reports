# Global State of DevSecOps 2023

## Strategies, Tools, and Practices Impacting Software Security

## Table of Contents
- [Overview](#overview)
- [About the Synopsys 2023 DevSecOps report](#about-the-synopsys-2023-devsecops-report)
- [On DevOps and DevSecOps](#on-devops-and-devsecops)
- [Benefits of automation](#benefits-of-automation)
- [The growing use of ASOC/ASPM in DevSecOps](#the-growing-use-of-asocaspm-in-devsecops)
- [Key Findings from the Synopsys 2023 DevSecOps Survey](#key-findings-from-the-synopsys-2023-devsecops-survey)
- [The State of DevSecOps in 2023](#the-state-of-devsecops-in-2023)
- [Lessons Learned](#lessons-learned)
- [Survey Demographics](#survey-demographics)
- [Appendix](#appendix)

---

## Overview

### About the Synopsys 2023 DevSecOps report
In early 2023, the Synopsys Cybersecurity Research Center (CyRC) and Censuswide, an international market research consultancy, conducted a survey of 1,000 IT professionals who identified security as part of their role or responsibilities. The group includes developers, AppSec professionals, DevOps engineers, CISOs, and experts who work in various roles in technology, cybersecurity, and application/software development. Participants came from the U.S., U.K., France, Finland, Germany, China, Singapore, and Japan.

Respondents from all industries and all company sizes were eligible to participate. One of the challenges faced while developing the survey is that the term “DevSecOps” embraces several disciplines, many of which have unique personas. The goal was to include a broad spectrum of professionals including “hands-on” developers who write the code and people at the CISO level, but targeting those whose work involved some aspect of software security.

![Chart showing reasons for unhappiness with AST tools: 35% do not prioritize resolution, 34% too slow for rapid release, 33% cost vs. ROI, 33% inaccuracy/unreliability]

### On DevOps and DevSecOps
Achieving the key tenets of DevOps—accelerated development, continuous delivery, pipeline resilience, scalability, and end-to-end transparency—requires a concerted effort from contributors in development, security, and operations.

An extension of the DevOps methodology, DevSecOps is designed to instill a culture of security across teams and address security early and consistently in DevOps environments. By integrating security practices into the software development life cycle (SDLC) and CI pipelines, DevSecOps aims to shift security from a separate, standalone phase to an integral part of the development life cycle.

DevSecOps has gained significant traction in every organization involved with software development. According to the SANS 2023 DevSecOps survey, DevSecOps is now clearly seen as a business-critical practice and a risk management concern. But historically, security and development teams have found themselves at odds when trying to introduce security into their processes, often a consequence of bringing legacy application security testing (AST) into the SDLC. Common complaints include AST tools’ complexity and high learning curves, slow performance, and “noisy” results causing DevOps “friction”—that is, anything in the software creation process that prevents developers from easily and quickly building code.

### Benefits of automation
A core tenet of DevOps is to automate manual processes within each stage of the SDLC. Automation is a fundamental requirement before any organization can implement continuous integration or continuous deployment to develop and deliver code faster.

Successful DevSecOps requires the interplay of integration and automation, governed by standards and policies. This allows security teams to trust that security interests are being covered, and allows DevOps teams to keep working and trust that there won’t be unpredictable breakdowns in the pipeline.

Unlike manual testing, automated security tests can be executed quickly and consistently, allowing developers to identify issues early in the development process without impacting delivery schedules or productivity.

- **Consistency**: Automated tests ensure that security checks are consistently applied to every build and deployment.
- **Scalability**: As software grows in complexity, manual testing becomes impractical. Automated tests can easily scale to handle a large number of tests across various components.
- **Continuous integration and continuous deployment (CI/CD)**: Automated testing is crucial in CI/CD pipelines, where rapid and frequent code changes are deployed.
- **Continuous improvement**: Automated testing provides data and insights that help teams improve security practices over time.
- **Documentation**: Automated tests document the testing process, making it easier to track and audit security measures and compliance requirements.
- **Reduction of human error**: Manual testing can be error-prone due to fatigue or oversight. Automated tests follow predefined scripts, reducing the risk of human error.
- **Time and cost savings**: Identifying and fixing security issues late in the development process or in production can be time-consuming and costly.
- **Improved developer experience**: Automated application security testing enhances the developer experience by offering proactive, integrated, and educational solutions.

### The growing use of ASOC/ASPM in DevSecOps
This report examines the characteristics of organizations at various stages of DevSecOps maturity and the security tools/practices the organizations employ. 

An interesting data point seen in the findings is the growing use of application security orchestration and correlation (ASOC), now more commonly referred to as application security posture management (ASPM). According to Gartner, ASPM should be a priority for any organization that uses multiple development and security tools.

ASPM solutions continuously manage application risks through the detection, correlation, and prioritization of security issues from development to deployment. ASPM also acts as a management and orchestration layer for security tools, enabling controls and the enforcement of security policies.

![28% of organizations reported using an ASOC tool]

---

## Key Findings from the Synopsys 2023 DevSecOps Survey

- **The majority of DevOps teams have adopted some level of DevSecOps**: 91% of respondents report incorporating some measure of DevSecOps activities.
- **Organizations with a more mature security program have personnel focused on security**: 29% noted a cross-functional DevSecOps team was an important factor in success.
- **There are many barriers to effectively implementing DevSecOps**: Over 33% pointed to inadequate security training as a major roadblock.
- **Over a third of respondents said that integrating automated security testing into build/deploy workflows was key to a security program’s success**.
- **Dealing with critical vulnerabilities late in the SDLC dramatically impacts the bottom line**: More than 80% said critical vulnerabilities in deployed software impacted their delivery schedules in 2022-23.
- **Twenty-eight percent of respondents said their organizations take as much as three weeks to patch critical security risks**.
- **Over 70% said automated scanning of code for vulnerabilities is a useful security measure**.
- **Nearly all respondents agreed that AST tools don’t align with their business needs**.
- **Fifty-two percent of security professionals are already actively using AI in their DevSecOps practices**, but more than three-quarters are concerned about issues with AI use.

---

## The State of DevSecOps in 2023

### DevSecOps adoption
Over a third of the 1,000 respondents characterized their security initiatives at a Level 3 stage of maturity, in which security processes are documented, repeatable, and standardized across the organization. 

![Figure A: Maturity levels: Level I (8.5%), Level II (24.1%), Level III (34.3%), Level IV (24.5%), Level V (8.5%)]

### Implementation of security practices indicate a higher level of maturity
The leading practice, security risk management (35.1%), involves integrating security considerations at every stage of the development process.

### Measuring a security program
Nearly 70% of respondents said that measuring their security programs through an assessment tool such as Building Security In Maturity Model (BSIMM) was a useful exercise.

### The importance of cross-functional teams for DevSecOps success
Twenty-nine percent of survey respondents noted that a cross-functional DevSecOps team was an important key to a security program’s success. Monolithic, stove-piped security teams have gone the way of the dodo.

### Combining manual and automated testing for the best results
The survey results indicate that the majority of respondents feel combining manual and automated security testing provides a more comprehensive approach.

### Key performance indicators
Overall reduction of open security vulnerabilities was cited by 29% of respondents as a top KPI, followed by reduction of security-related discoveries late in the SDLC (28%) and issue resolution time (28%).

### Which AST tools are in use? How useful are they?
SAST was found to be the leading AST tool used by respondents, with 72% finding it useful. It was closely followed by IAST (69%), SCA (68%), and DAST (67%).

### When to test? When to patch? What’s the impact on our schedules?
Most respondent organizations run vulnerability scans on business-critical applications an average of two to three days a week. 

### Challenges to effective DevSecOps
The shortage of cybersecurity personnel is a significant challenge, but inadequate security training for developers/engineers remains the biggest challenge (33.9%).

### Promises and pitfalls of AI
Over 50% of respondents are actively using AI in their DevSecOps practices. However, 76.6% of respondents are concerned about potential bias or errors in AI-based security solutions.

---

## Lessons Learned
While most organizations have largely adopted some level of DevSecOps practices, they continue to face barriers to its effective implementation, specifically:
1. Integrating and aligning the results of multiple AST tools to meet business priorities.
2. Reducing the time needed to resolve critical vulnerabilities.

For organizations struggling to gain cohesion across siloed security tools, ASPM can provide a needed force multiplier by automating coordination, context, and prioritization.

---

## Survey Demographics
- **Industries**: Technology (18%), Cybersecurity (15%), Application/Software Development (13%), Manufacturing (7%), FinTech (7%), Education (6%), Banking/Financial (6%), Telecommunications/ISP (5%), Healthcare (4%), Retail (4%), Media (4%), Government (3%), Insurance (3%), Transportation (3%), Nonprofit/Association (2%), Utilities (2%).
- **Global Reach**: Respondents were surveyed from the U.S., U.K., France, Finland, Germany, China, Singapore, and Japan.

---

## Appendix
*(Detailed data tables regarding industry distribution, organization size, and software types are provided in the original report documentation.)*

---

0%

39.20%

30.40%

35.20%

30.40%

29.60%

0.00%

37.30%

41.27%

28.57%

33.33%

29.37%

30.16%

30.16%

0.79%

   State of DevSecOps 2023

Overview

Q4. What practices does your organization follow? (Select all that apply)

Key Findings from the Synopsys
2023 DevSecOps Survey

Security risk management

The State of DevSecOps in 2023

Continuous monitoring and measurement

Lessons Learned

Survey Demographics

Appendix

Configuration management

Threat data & responses

Continuous deployment

Automated deployment

Continuous testing

Application security orchestration and correlation

Continuous integration

Automated testing

Infrastructure-as-code

Other (Please specify)

Global

35.13%

29.93%

29.64%

29.34%

29.05%

28.56%

28.46%

28.36%

28.16%

27.87%

27.58%

0.10%

U.K.

35.43%

25.20%

19.69%

22.83%

27.56%

18.90%

22.05%

29.13%

23.62%

19.69%

23.62%

0.00%

U.S.

40.63%

34.38%

31.25%

39.84%

35.16%

28.91%

32.03%

39.84%

30.47%

33.59%

41.41%

0.00%

France

33.60%

29.60%

24.80%

31.20%

21.60%

32.80%

24.80%

20.00%

24.80%

28.00%

22.40%

0.00%

Finland

Germany

China

Singapore

Japan

32.28%

32.28%

23.62%

28.35%

29.13%

28.35%

30.71%

19.69%

25.98%

24.41%

20.47%

0.79%

19.84%

22.22%

23.02%

19.84%

28.57%

23.81%

23.02%

18.25%

19.84%

15.08%

22.22%

0.00%

56.30%

44.44%

49.63%

41.48%

41.48%

48.15%

48.15%

51.85%

47.41%

48.15%

48.15%

0.00%

32.80%

25.60%

30.40%

27.20%

20.80%

24.80%

17.60%

28.00%

28.00%

20.00%

25.60%

0.00%

28.57%

24.60%

33.33%

23.02%

26.98%

21.43%

27.78%

18.25%

23.81%

32.54%

15.08%

0.00%

   State of DevSecOps 2023

Overview

Q5. How useful, if at all, are the following application security tools, practices, or techniques that you use in your organization?

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Defining security requirements as part of SDLC requirements stage

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Formal measurement of your software security through models such as
BSIMM, SAMM, etc.

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Automated scanning of code for security vulnerabilities and other defects
(e.g., static application security testing (SAST)

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Global

71.25%

32.09%

39.16%

16.78%

7.56%

24.34%

4.42%

Global

69.38%

33.56%

35.82%

18.06%

8.44%

26.50%

4.12%

Global

71.54%

34.35%

37.19%

17.37%

7.65%

25.02%

3.43%

U.K.

66.93%

25.20%

41.73%

15.75%

11.02%

26.77%

6.30%

U.K.

55.91%

24.41%

31.50%

25.20%

11.81%

37.01%

7.09%

U.K.

62.20%

29.13%

33.07%

22.05%

13.39%

35.43%

2.36%

U.S.

78.91%

46.88%

32.03%

12.50%

3.13%

15.63%

5.47%

U.S.

79.69%

47.66%

32.03%

10.94%

7.03%

17.97%

2.34%

U.S.

76.56%

46.09%

30.47%

10.94%

8.59%

19.53%

3.91%

France

73.60%

32.00%

41.60%

16.80%

8.00%

24.80%

1.60%

France

71.20%

25.60%

45.60%

17.60%

8.80%

26.40%

2.40%

France

76.00%

33.60%

42.40%

16.80%

5.60%

22.40%

1.60%

Finland

81.10%

35.43%

45.67%

13.39%

3.15%

16.54%

2.36%

Germany

62.70%

24.60%

38.10%

20.63%

11.90%

32.54%

4.76%

China

97.04%

54.07%

42.96%

2.96%

0.00%

2.96%

0.00%

Singapore

55.20%

17.60%

37.60%

26.40%

14.40%

40.80%

4.00%

Japan

52.38%

19.05%

33.33%

26.98%

9.52%

36.51%

11.11%

Finland

Germany

China

Singapore

Japan

70.87%

30.71%

40.16%

25.20%

2.36%

27.56%

1.57%

57.94%

26.98%

30.95%

23.02%

16.67%

39.68%

2.38%

94.81%

57.04%

37.78%

3.70%

0.74%

4.44%

0.74%

67.20%

28.80%

38.40%

16.80%

10.40%

27.20%

5.60%

55.56%

25.40%

30.16%

23.02%

10.32%

33.33%

11.11%

Finland

Germany

China

Singapore

Japan

78.74%

38.58%

40.16%

18.11%

2.36%

20.47%

0.79%

65.87%

27.78%

38.10%

17.46%

11.90%

29.37%

4.76%

94.07%

54.07%

40.00%

5.93%

0.00%

5.93%

0.00%

54.40%

21.60%

32.80%

29.60%

12.80%

42.40%

3.20%

62.70%

22.22%

40.48%

19.05%

7.14%

26.19%

11.11%

   State of DevSecOps 2023

Overview

Open source/third-party dependency analysis (SCA)

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Internal or third-party penetration testing

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Fuzz testing

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Global

67.62%

30.32%

37.29%

19.73%

8.34%

28.07%

4.32%

Global

67.91%

30.23%

37.68%

19.33%

8.64%

27.97%

4.12%

Global

62.32%

25.02%

37.29%

19.73%

9.52%

29.24%

8.44%

U.K.

50.39%

22.05%

28.35%

25.98%

14.17%

40.16%

9.45%

U.K.

53.54%

18.11%

35.43%

29.13%

10.24%

39.37%

7.09%

U.K.

50.39%

19.69%

30.71%

18.90%

14.96%

33.86%

15.75%

U.S.

75.00%

33.59%

41.41%

16.41%

5.47%

21.88%

3.13%

U.S.

71.88%

37.50%

34.38%

19.53%

7.03%

26.56%

1.56%

U.S.

75.00%

35.94%

39.06%

12.50%

4.69%

17.19%

7.81%

France

73.60%

32.00%

41.60%

18.40%

6.40%

24.80%

1.60%

France

72.00%

35.20%

36.80%

16.80%

7.20%

24.00%

4.00%

France

58.40%

17.60%

40.80%

22.40%

4.80%

27.20%

14.40%

Finland

74.80%

30.71%

44.09%

22.05%

1.57%

23.62%

1.57%

Finland

80.31%

43.31%

37.01%

16.54%

3.15%

19.69%

0.00%

Finland

68.50%

23.62%

44.88%

18.90%

9.45%

28.35%

3.15%

Germany

61.11%

23.81%

37.30%

22.22%

11.90%

34.13%

4.76%

Germany

56.35%

23.02%

33.33%

20.63%

17.46%

38.10%

5.56%

Germany

53.97%

27.78%

26.19%

23.02%

18.25%

41.27%

4.76%

China

94.81%

60.74%

34.07%

5.19%

0.00%

5.19%

0.00%

China

96.30%

48.89%

47.41%

3.70%

0.00%

3.70%

0.00%

China

88.15%

42.96%

45.19%

10.37%

0.74%

11.11%

0.74%

Singapore

53.60%

20.00%

33.60%

27.20%

12.80%

40.00%

6.40%

Singapore

54.40%

17.60%

36.80%

24.80%

15.20%

40.00%

5.60%

Singapore

55.20%

18.40%

36.80%

25.60%

12.00%

37.60%

7.20%

Japan

55.56%

17.46%

38.10%

21.43%

15.08%

36.51%

7.94%

Japan

56.35%

16.67%

39.68%

24.60%

9.52%

34.13%

9.52%

Japan

46.83%

12.70%

34.13%

26.98%

11.90%

38.89%

14.29%

   State of DevSecOps 2023

Overview

Q6. How useful, if at all, are the following application security tools, practices, or techniques that you use in your organization?

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Dynamic application security testing (DAST)

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Interactive application security testing (IAST)

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Web application firewall (WAF)

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Global

67.12%

29.44%

37.68%

19.63%

9.62%

29.24%

3.63%

Global

68.50%

31.11%

37.39%

18.06%

9.62%

27.67%

3.83%

Global

68.99%

33.17%

35.82%

18.25%

8.73%

26.99%

4.02%

U.K.

48.82%

16.54%

32.28%

32.28%

12.60%

44.88%

6.30%

U.K.

60.63%

22.05%

38.58%

18.11%

14.17%

32.28%

7.09%

U.K.

62.99%

33.86%

29.13%

19.69%

11.02%

30.71%

6.30%

U.S.

74.22%

38.28%

35.94%

16.41%

6.25%

22.66%

3.13%

U.S.

72.66%

35.16%

37.50%

20.31%

6.25%

26.56%

0.78%

U.S.

78.13%

39.84%

38.28%

14.84%

6.25%

21.09%

0.78%

France

76.80%

36.80%

40.00%

16.80%

5.60%

22.40%

0.80%

France

75.20%

34.40%

40.80%

15.20%

9.60%

24.80%

0.00%

France

66.40%

32.00%

34.40%

20.00%

10.40%

30.40%

3.20%

Finland

74.80%

29.92%

44.88%

17.32%

6.30%

23.62%

1.57%

Finland

77.17%

37.01%

40.16%

18.11%

3.15%

21.26%

1.57%

Finland

78.74%

36.22%

42.52%

15.75%

3.94%

19.69%

1.57%

Germany

62.70%

27.78%

34.92%

20.63%

12.70%

33.33%

3.97%

Germany

53.97%

18.25%

35.71%

21.43%

18.25%

39.68%

6.35%

Germany

55.56%

21.43%

34.13%

23.02%

14.29%

37.30%

7.14%

China

91.11%

46.67%

44.44%

7.41%

0.74%

8.15%

0.74%

China

96.30%

54.07%

42.22%

3.70%

0.00%

3.70%

0.00%

China

97.78%

52.59%

45.19%

2.22%

0.00%

2.22%

0.00%

Singapore

49.60%

20.00%

29.60%

28.80%

18.40%

47.20%

3.20%

Singapore

53.60%

24.00%

29.60%

24.80%

14.40%

39.20%

7.20%

Singapore

51.20%

21.60%

29.60%

32.80%

12.80%

45.60%

3.20%

Japan

57.14%

18.25%

38.89%

18.25%

15.08%

33.33%

9.52%

Japan

56.35%

22.22%

34.13%

23.81%

11.90%

35.71%

7.94%

Japan

58.73%

26.19%

32.54%

19.05%

11.90%

30.95%

10.32%

   State of DevSecOps 2023

Overview

Container security testing

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Use of vulnerability/risk management tool (e.g., XDR, SRM, etc.)

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Remediation prioritization

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

Software supply chain management/monitoring

Useful (Net)

Very useful

Somewhat useful

Not that useful

Not at all useful

Not useful (Net)

N/A

   State of DevSecOps 2023

Global

66.93%

29.93%

37.00%

18.65%

9.42%

28.07%

5.00%

Global

69.77%

32.58%

37.19%

17.86%

9.62%

27.48%

2.75%

Global

67.12%

29.83%

37.29%

18.45%

9.91%

28.36%

4.51%

Global

69.28%

32.29%

37.00%

18.84%

8.34%

27.18%

3.53%

U.K.

48.82%

20.47%

28.35%

29.13%

14.96%

44.09%

7.09%

U.K.

58.27%

24.41%

33.86%

21.26%

16.54%

37.80%

3.94%

U.K.

53.54%

21.26%

32.28%

28.35%

9.45%

37.80%

8.66%

U.K.

59.84%

24.41%

35.43%

22.83%

11.81%

34.65%

5.51%

U.S.

79.69%

38.28%

41.41%

13.28%

3.91%

17.19%

3.13%

U.S.

82.81%

47.66%

35.16%

8.59%

7.03%

15.63%

1.56%

U.S.

82.81%

40.63%

42.19%

7.81%

7.03%

14.84%

2.34%

U.S.

72.66%

36.72%

35.94%

17.19%

7.81%

25.00%

2.34%

France

73.60%

29.60%

44.00%

14.40%

8.80%

23.20%

3.20%

France

74.40%

35.20%

39.20%

19.20%

5.60%

24.80%

0.80%

France

67.20%

24.80%

42.40%

19.20%

10.40%

29.60%

3.20%

France

71.20%

33.60%

37.60%

17.60%

10.40%

28.00%

0.80%

Finland

74.80%

39.37%

35.43%

17.32%

6.30%

23.62%

1.57%

Finland

74.02%

41.73%

32.28%

22.05%

1.57%

23.62%

2.36%

Finland

71.65%

36.22%

35.43%

22.05%

5.51%

27.56%

0.79%

Finland

77.95%

32.28%

45.67%

18.11%

1.57%

19.69%

2.36%

Germany

57.94%

24.60%

33.33%

19.84%

18.25%

38.10%

3.97%

Germany

57.14%

22.22%

34.92%

19.05%

20.63%

39.68%

3.17%

Germany

53.97%

21.43%

32.54%

19.84%

17.46%

37.30%

8.73%

Germany

58.73%

25.40%

33.33%

23.81%

10.32%

34.13%

7.14%

China

91.11%

49.63%

41.48%

6.67%

1.48%

8.15%

0.74%

China

97.78%

50.37%

47.41%

1.48%

0.74%

2.22%

0.00%

China

96.30%

54.07%

42.22%

3.70%

0.00%

3.70%

0.00%

China

95.56%

57.04%

38.52%

3.70%

0.74%

4.44%

0.00%

Singapore

57.60%

21.60%

36.00%

24.00%

12.80%

36.80%

5.60%

Singapore

53.60%

20.00%

33.60%

27.20%

16.00%

43.20%

3.20%

Singapore

56.80%

21.60%

35.20%

24.00%

12.00%

36.00%

7.20%

Singapore

56.00%

19.20%

36.80%

31.20%

11.20%

42.40%

1.60%

Japan

50.00%

14.29%

35.71%

25.40%

9.52%

34.92%

15.08%

Japan

57.94%

17.46%

40.48%

25.40%

9.52%

34.92%

7.14%

Japan

52.38%

16.67%

35.71%

23.81%

18.25%

42.06%

5.56%

Japan

60.32%

27.78%

32.54%

17.46%

13.49%

30.95%

8.73%

Overview

Q7. How would you best describe the maturity of your current software security program/initiative?

Key Findings from the Synopsys
2023 DevSecOps Survey

Level I: Unstructured/disorganized.

Global

8.54%

U.K.

11.02%

U.S.

3.91%

France

4.80%

Finland

11.02%

Germany

12.70%

The State of DevSecOps in 2023

Level II: Security processes are documented and repeatable for specific
team.

24.14%

28.35%

23.44%

16.00%

29.13%

26.19%

China

2.22%

9.63%

Singapore

Japan

10.40%

12.70%

34.40%

26.98%

Lessons Learned

Survey Demographics

Appendix

Level III: Level II processes and procedures are standardized across
organization. A proactive security culture is endorsed and communicated
by leadership.

Level IV: Security processes and controls are logged, managed, and
monitored.

Level V: Security processes are continuously analyzed and improved.

Other (Please specify)

34.25%

33.07%

38.28%

40.00%

35.43%

36.51%

21.48%

33.60%

36.51%

24.53%

22.05%

20.31%

28.00%

14.96%

21.43%

48.89%

20.00%

19.05%

8.54%

0.00%

5.51%

0.00%

14.06%

11.20%

0.00%

0.00%

9.45%

0.00%

3.17%

0.00%

17.78%

0.00%

1.60%

0.00%

4.76%

0.00%

Q8. On average, how often, if at all, do you assess or test the security of your business-critical applications?

Every day

4-6 days a week

2-3 days a week

Once a week

Once every 2 to 3 weeks

Once a month

Once every 2 months

Once every 3 to 5 months

Once every 6 to 11 months

Once a year

Less than once a year, please specify

Never

Global

7.07%

17.17%

20.41%

16.98%

11.09%

7.16%

7.46%

6.38%

4.42%

1.67%

0.00%

0.20%

U.K.

3.94%

15.75%

18.90%

16.54%

11.02%

6.30%

7.87%

7.87%

7.87%

2.36%

0.00%

1.57%

U.S.

8.59%

16.41%

21.09%

15.63%

12.50%

4.69%

7.81%

10.16%

2.34%

0.78%

0.00%

0.00%

France

19.20%

15.20%

28.00%

14.40%

5.60%

5.60%

3.20%

5.60%

1.60%

1.60%

0.00%

0.00%

Finland

Germany

4.72%

11.81%

14.96%

18.11%

18.11%

12.60%

11.02%

3.15%

4.72%

0.79%

0.00%

0.00%

3.17%

11.11%

20.63%

16.67%

12.70%

7.94%

3.97%

7.14%

10.32%

6.35%

0.00%

0.00%

China

3.70%

37.04%

27.41%

17.78%

5.19%

5.19%

2.22%

1.48%

0.00%

0.00%

0.00%

0.00%

Singapore

Japan

2.40%

11.20%

14.40%

19.20%

14.40%

5.60%

18.40%

7.20%

6.40%

0.80%

0.00%

0.00%

11.11%

17.46%

17.46%

17.46%

9.52%

9.52%

5.56%

8.73%

2.38%

0.79%

0.00%

0.00%

   State of DevSecOps 2023

Overview

Q9. How do you assess or test the security of your business-critical applications? (Select all that apply)

Key Findings from the Synopsys
2023 DevSecOps Survey

Combination of both manual and automated assessments

The State of DevSecOps in 2023

External pen testing

Lessons Learned

Survey Demographics

Appendix

Automated assessments and testing

Manual assessments and/or tests (excluding pen testing)

Unknown/Unsure

Other (Please specify)

Global

52.61%

44.15%

43.66%

43.07%

0.20%

0.00%

U.K.

50.40%

37.60%

40.00%

36.00%

0.00%

0.00%

U.S.

65.63%

39.06%

46.88%

46.88%

0.00%

0.00%

France

44.80%

40.00%

39.20%

37.60%

0.80%

0.00%

Finland

Germany

China

Singapore

Japan

50.39%

43.31%

42.52%

46.46%

0.79%

0.00%

51.59%

47.62%

45.24%

44.44%

0.00%

0.00%

68.89%

63.70%

68.15%

58.52%

0.00%

0.00%

47.20%

45.60%

29.60%

33.60%

0.00%

0.00%

40.48%

34.92%

35.71%

39.68%

0.00%

0.00%

Q10. How much of an impact, if at all, has addressing a critical security/vulnerability issue had on your organization's software delivery
schedule within the past year (2022-2023)?

Global

81.06%

38.37%

42.69%

17.17%

1.77%

U.K.

U.S.

France

Finland

Germany

China

Singapore

Japan

72.44%

86.72%

80.00%

92.91%

89.68%

79.26%

80.80%

66.67%

24.41%

48.03%

25.20%

2.36%

41.41%

45.31%

12.50%

0.78%

33.60%

46.40%

17.60%

2.40%

33.86%

59.06%

7.09%

0.00%

7.09%

54.76%

34.92%

7.94%

2.38%

60.74%

18.52%

20.00%

0.74%

24.80%

56.00%

18.40%

0.80%

31.75%

34.92%

28.57%

4.76%

10.32%

20.74%

19.20%

33.33%

18.94%

27.56%

13.28%

20.00%

Impact (Net)

A large impact

A little impact

Not much of an impact

No impact at all

No impact (Net)

   State of DevSecOps 2023

Overview

Q11. Who is responsible for conducting security testing in your organization? (Select all that apply)

Key Findings from the Synopsys
2023 DevSecOps Survey

Internal security team

The State of DevSecOps in 2023

Developers/software engineers

Lessons Learned

Survey Demographics

Appendix

QA/test teams

Cross-functional DevSecOps teams

External consultants

Unsure

Other (Please specify)

Global

46.03%

45.14%

37.59%

35.53%

32.88%

0.10%

0.00%

U.K.

39.37%

34.65%

41.73%

31.50%

29.92%

0.00%

0.00%

U.S.

50.00%

53.13%

35.94%

44.53%

46.09%

0.00%

0.00%

France

36.80%

33.60%

32.80%

28.80%

28.00%

0.00%

0.00%

Finland

Germany

China

Singapore

Japan

41.73%

44.88%

33.86%

39.37%

28.35%

0.00%

0.00%

38.89%

42.86%

38.89%

30.95%

38.10%

0.79%

0.00%

67.41%

63.70%

51.11%

48.15%

32.59%

0.00%

0.00%

46.40%

44.00%

34.40%

32.00%

31.20%

0.00%

0.00%

46.03%

42.86%

30.95%

27.78%

28.57%

0.00%

0.00%

Q12. On average, how long does it take for your organization to patch/resolve critical security risks/vulnerabilities for applications
already deployed/in use?

Up to one week, please specify in days

Over one week, up to two weeks

Over two weeks, up to three weeks

Over three weeks, up to one month

Over one month, up to two months

Over two months, up to four months

Over four months, up to six months

Over six months, please specify in months

Unsure

Global

4.61%

26.40%

28.26%

19.92%

8.44%

5.50%

4.71%

0.00%

2.16%

U.K.

0.00%

14.96%

33.86%

22.83%

9.45%

3.94%

9.45%

0.00%

5.51%

U.S.

7.81%

21.88%

28.91%

19.53%

5.47%

5.47%

10.16%

0.00%

0.78%

France

11.20%

40.80%

24.80%

16.00%

3.20%

3.20%

0.80%

0.00%

0.00%

Finland

Germany

5.51%

25.98%

26.77%

21.26%

11.81%

4.72%

1.57%

0.00%

2.36%

0.00%

14.29%

23.02%

32.54%

11.90%

11.11%

4.76%

0.00%

2.38%

China

6.67%

57.04%

29.63%

4.44%

1.48%

0.74%

0.00%

0.00%

0.00%

Singapore

3.20%

10.40%

28.00%

26.40%

14.40%

8.80%

8.00%

0.00%

0.80%

Japan

2.38%

23.81%

30.95%

17.46%

10.32%

6.35%

3.17%

0.00%

5.56%

   State of DevSecOps 2023

Overview

Q13. What are the major KPIs you use to measure the success of your DevSecOps activities? (Select up to 3)

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Number of open security vulnerabilities

Global

28.95%

Reduction of security-related discoveries late in the development process

28.26%

Issue resolution time

Reduction in hours spent resolving security issues

Reduction in security-related build delays

Reduction in security-failed builds

Compliance KPIs (percentage of audits passed, etc.)

Customer ticket volume

Defect Escape Rate

There are no major KPIs we use to measure the success of our DevSecOps
activities

Other, please specify

27.58%

27.38%

26.50%

24.44%

23.75%

22.77%

22.28%

1.08%

0.00%

U.K.

27.56%

33.07%

24.41%

27.56%

25.98%

22.05%

30.71%

29.13%

22.83%

0.00%

0.00%

U.S.

32.81%

33.59%

30.47%

30.47%

28.91%

24.22%

28.91%

28.91%

17.19%

0.00%

0.00%

France

28.80%

24.00%

28.00%

24.00%

28.80%

21.60%

17.60%

25.60%

16.00%

0.00%

0.00%

Finland

Germany

China

Singapore

Japan

27.56%

24.41%

24.41%

21.26%

26.77%

25.20%

22.83%

21.26%

30.71%

1.57%

0.00%

24.60%

29.37%

23.02%

34.13%

19.84%

27.78%

26.98%

22.22%

23.81%

0.00%

0.00%

40.00%

30.37%

31.11%

32.59%

27.41%

25.93%

24.44%

15.56%

28.15%

0.00%

0.00%

26.40%

30.40%

25.60%

24.80%

26.40%

25.60%

23.20%

25.60%

17.60%

0.80%

0.00%

23.02%

20.63%

33.33%

23.81%

27.78%

23.02%

15.08%

14.29%

21.43%

6.35%

0.00%

Q14. What are the challenges/barriers in implementing DevSecOps at your organization, if any? (Select all that apply)

Inadequate/ineffective security training for developers/engineers

Shortage of application security personnel/skills

Lack of transparency into development/operations work

Continuously changing requirements and priorities

Insufficient budget/funding for security programs and tools

Organizational silos between development, operations, security

Lack of coding skills in security teams

There are no challenges/barriers

Other, please specify

Global

33.86%

31.40%

31.31%

30.42%

29.44%

29.05%

28.95%

2.06%

0.00%

U.K.

33.07%

25.98%

27.56%

25.20%

30.71%

31.50%

24.41%

4.72%

0.00%

U.S.

42.97%

29.69%

37.50%

30.47%

39.06%

42.19%

30.47%

3.13%

0.00%

France

27.20%

28.80%

28.80%

27.20%

32.80%

24.80%

26.40%

1.60%

0.00%

Finland

Germany

China

Singapore

Japan

31.50%

23.62%

35.43%

29.13%

37.01%

28.35%

31.50%

2.36%

0.00%

35.71%

31.75%

29.37%

27.78%

23.02%

29.37%

30.95%

0.79%

0.00%

32.59%

46.67%

36.30%

43.70%

22.96%

29.63%

28.89%

1.48%

0.00%

35.20%

32.80%

28.00%

32.80%

21.60%

22.40%

29.60%

0.00%

0.00%

32.54%

30.95%

26.98%

26.19%

28.57%

23.81%

29.37%

2.38%

0.00%

   State of DevSecOps 2023

Overview

Q15. What are the major issues with the application security testing tools used in your organization? (Select up to 3)

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Tool(s) do not prioritize resolution based on exposure, exploitability, and
criticality

Too slow to fit into rapid release cycles/continuous deployment

Cost vs. ROI

Inaccuracy/unreliability

High number of false positives

No way to consolidate/correlate results from different tools

There are no major issues

Other (Please specify)

Global

U.K.

U.S.

France

Finland

Germany

China

Singapore

Japan

34.74%

35.43%

41.41%

40.00%

37.01%

34.13%

35.56%

22.40%

31.75%

34.15%

33.46%

33.07%

32.19%

28.95%

3.14%

0.00%

26.77%

29.92%

25.20%

38.58%

23.62%

6.30%

0.00%

42.97%

34.38%

39.84%

39.06%

28.91%

3.13%

0.00%

33.60%

32.00%

28.80%

21.60%

22.40%

4.00%

0.00%

28.35%

38.58%

36.22%

31.50%

26.77%

2.36%

0.00%

30.16%

34.92%

33.33%

35.71%

30.95%

0.00%

0.00%

47.41%

33.33%

31.85%

29.63%

34.07%

5.19%

0.00%

40.00%

30.40%

32.00%

36.00%

28.00%

0.00%

0.00%

23.02%

34.13%

37.30%

25.40%

36.51%

3.97%

0.00%

Q16. What do you consider to be the top factors that have contributed to a security program's success? (Select up to 3)

Enforcing security/compliance policies through infrastructure-as-code

Developing security champions in Dev and Ops teams

Improving communications across Dev, Ops, and Security teams

Integrating automated security testing into build/deploy workflows

Minimizing time/cost to fix vulnerabilities through automation

Creating cross-functional DevSecOps teams

Training developers/engineers in secure coding

I don't consider there to be any top factors

Other (Please specify)

Global

33.56%

32.58%

32.48%

32.29%

30.03%

28.95%

27.58%

0.79%

0.00%

U.K.

36.22%

22.05%

34.65%

28.35%

32.28%

29.92%

25.20%

2.36%

0.00%

U.S.

37.50%

39.06%

42.97%

36.72%

31.25%

32.03%

28.91%

0.00%

0.00%

France

39.20%

32.80%

27.20%

32.00%

31.20%

21.60%

20.80%

0.80%

0.00%

Finland

Germany

China

Singapore

Japan

26.77%

28.35%

31.50%

36.22%

23.62%

37.01%

35.43%

0.00%

0.00%

26.98%

38.89%

34.13%

33.33%

27.78%

28.57%

26.98%

0.79%

0.00%

40.74%

28.15%

32.59%

32.59%

40.74%

35.56%

33.33%

0.74%

0.00%

29.60%

40.00%

34.40%

28.00%

27.20%

26.40%

21.60%

0.00%

0.00%

30.95%

31.75%

22.22%

30.95%

25.40%

19.84%

27.78%

1.59%

0.00%

   State of DevSecOps 2023

Overview

Q17. Are you currently using any AI tools to enhance your software security measures?

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Yes, we are actively using AI tools

Global

52.50%

No, we are open to the use of AI tools, but have not yet implemented them

36.51%

No, we have not implemented AI tools, and have no plans to do so

No (Net)

10.99%

47.50%

U.K.

38.58%

39.37%

22.05%

U.S.

64.06%

23.44%

12.50%

France

47.20%

42.40%

10.40%

Finland

47.24%

47.24%

5.51%

Germany

China

Singapore

Japan

69.84%

22.22%

7.94%

57.04%

40.00%

2.96%

47.20%

35.20%

17.60%

48.41%

42.06%

9.52%

61.42%

35.94%

52.80%

52.76%

30.16%

42.96%

52.80%

51.59%

Q18. How do you expect the use of AI tools to impact your DevSecOps processes and workflows? (Select all that apply)

Improve efficiency and accuracy of security measures

Global

53.69%

Increase the complexity and technical requirements of software security

52.04%

Reduce the need for manual review and analysis of security data

Have no significant impact

Other (please specify)

48.40%

0.88%

0.00%

U.K.

51.52%

51.52%

50.51%

0.00%

0.00%

U.S.

58.93%

64.29%

45.54%

0.00%

0.00%

France

49.11%

42.86%

42.86%

0.89%

0.00%

Finland

44.17%

50.83%

50.83%

0.83%

0.00%

Germany

China

Singapore

Japan

43.97%

54.31%

45.69%

2.59%

0.00%

68.70%

61.83%

64.12%

0.00%

0.00%

57.28%

47.57%

42.72%

0.00%

0.00%

54.39%

41.23%

42.11%

2.63%

0.00%

Q19. What specific areas of software security do you believe AI tools could be most effective in enhancing?

Threat detection and prevention

Vulnerability scanning and testing

Identity and access management

Compliance and regulation management

Other (please specify)

Global

45.09%

44.21%

42.01%

41.57%

0.00%

U.K.

42.42%

39.39%

43.43%

47.47%

0.00%

U.S.

50.00%

46.43%

50.00%

46.43%

0.00%

France

46.43%

45.54%

44.64%

31.25%

0.00%

Finland

Germany

China

Singapore

Japan

46.67%

46.67%

38.33%

42.50%

0.00%

41.38%

37.07%

37.93%

36.21%

0.00%

44.27%

52.67%

54.20%

45.04%

0.00%

46.60%

42.72%

33.98%

37.86%

0.00%

42.98%

41.23%

31.58%

45.61%

0.00%

   State of DevSecOps 2023

Overview

Q20. How concerned, if at all, are you about potential bias or errors in AI-based security solutions?

Key Findings from the Synopsys
2023 DevSecOps Survey

The State of DevSecOps in 2023

Lessons Learned

Survey Demographics

Appendix

Concerned (Net)

Very concerned

Somewhat concerned

Neutral/undecided

Not very concerned

Not concerned at all

Not concerned (Net)

Global

76.63%

25.36%

51.27%

16.21%

5.95%

1.21%

7.17%

U.K.

U.S.

France

Finland

Germany

China

Singapore

Japan

76.77%

83.93%

74.11%

77.50%

84.48%

55.73%

82.52%

81.58%

27.27%

49.49%

15.15%

6.06%

2.02%

8.08%

33.04%

50.89%

10.71%

4.46%

0.89%

5.36%

16.96%

57.14%

22.32%

2.68%

0.89%

3.57%

15.83%

61.67%

18.33%

3.33%

0.83%

4.17%

50.00%

34.48%

8.62%

6.03%

0.86%

6.90%

7.63%

48.09%

28.24%

13.74%

2.29%

16.03%

28.16%

54.37%

12.62%

3.88%

0.97%

4.85%

27.19%

54.39%

11.40%

6.14%

0.88%

7.02%

The Synopsys difference
Synopsys provides integrated solutions that transform the way you build and deliver software, accelerating innovation while addressing business risk. With Synopsys, your developers
can secure code as fast as they write it. Your development and DevSecOps teams can automate testing within development pipelines without compromising velocity. And your security
teams can proactively manage risk and focus remediation efforts on what matters most to your organization. Our unmatched expertise helps you plan and execute any security
initiative. Only Synopsys offers everything you need to build trust in your software.

For more information about the Synopsys Software Integrity Group, visit us online at www.synopsys.com/software .

©2023 Synopsys, Inc. All rights reserved. Synopsys is a trademark of Synopsys, Inc. in the United States and other countries. A list of Synopsys trademarks is available at www.synopsys.com/copyright.html . All other names mentioned herein are trademarks or registered trademarks of
their respective owners. October 2023.

   State of DevSecOps 2023