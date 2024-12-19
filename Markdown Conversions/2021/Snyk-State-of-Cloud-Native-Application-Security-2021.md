# State of Cloud Native Application Security

## How cloud native adoption transforms the way organizations defend against security threats

### 99% of companies recognized security as important to their cloud native strategy

Success in the cloud native era is defined by an organization's ability to deliver new versions of software faster and more efficiently, which is reinforced by our survey results. Being able to deploy code to production faster and more easily manage those applications were the primary reasons for moving towards containerized infrastructure. However, as companies embrace cloud native technologies as part of their digital transformation, security is seen as a key factor to building successful platforms. While only 36% of respondents stated that security was one of the main reasons for moving their production applications into containers, 99% of respondents recognized security as an important element in their cloud native strategy. In addition, over 80% stated security is very important to them.

Snyk Report: State of Cloud Native Application Security | 01

### What are the main reasons for moving your applications into containers?

#### How important is security to your cloud native strategy?

| Reason             | %  |
|----------------------|----|
| Deployment velocity  | 68 |
| Ease of management   | 67 |
| Reduce costs         | 43 |
| Improved security    | 36 |
| Attracting talent    | 11 |

| Importance         | %  |
|----------------------|----|
| Very important      | 83 |
| Somewhat important   | 16 |
| Not important        | 1  |

*As cloud native adoption increases, security needs to be built in as standard*

### Over 78% of production workloads are deployed as containers or serverless applications

In total over 78% of production workloads are deployed as containers or serverless applications. Containers continue to be the dominant mechanism for cloud native application deployment, with nearly 60% of production workloads deployed in containers. Penetration of serverless technologies is now significant across all company sizes, and makes up more than a fifth (mean average) of all production workloads. Usage of cloud native technologies is strong across all company sizes, indicating that adoption is becoming mainstream. With over 50% of respondent’s workloads also being deployed with some form of Infrastructure As Code, use of software-driven infrastructure has increased alongside the container and serverless growth trends. Usage of these core technologies is one of the key indicators of cloud native transformation in general, and so we use these metrics throughout this report as indicative of the level of adoption within an organization.

Snyk Report: State of Cloud Native Application Security | 02

| Technology    | %  |
|---------------|----|
| Containers    | 58 |
| Serverless    | 21 |
| IaC           | 51 |

### While 95% of respondents use automation, only 33% fully automate their deployment pipeline

Deployment automation is one of the key tenets of cloud native practices, enabling development velocity. Our survey showed that over 95% of respondents were using some level of automation with almost a third having an entirely automated deployment pipeline. By comparing the upper and lower quartiles of cloud native production usage (high levels of adoption vs low levels of adoption), we can see that organizations that show high levels of cloud native adoption are over twice as likely to have an entirely automated deployment process than organizations with low cloud native adoption.

Snyk Report: State of Cloud Native Application Security | 03

#### Are your application deployments manual or automated?

| Automation Level     | %  |
|----------------------|----|
| Not automated at all  | 1.7|
| Partially automated  | 56 |
| Entirely automated   | 42 |

#### Low adoption

| Automation Level     | %  |
|----------------------|----|
| Not automated at all  | 6  |
| Partially automated  | 76 |
| Entirely automated   | 18 |

#### High adoption

*Download Snyk’s Infrastructure as Code Security Insights report for the trends on how companies are using and securing IaC today and common roadblocks to it’s wide spread use*

[Download now](link_to_download)

### Misconfiguration and known unpatched vulnerabilities were responsible for the greatest number of security incidents in cloud native environments

In contrast to where organizations are most concerned, we also asked about previous incidents that occured in production. The top two incident types by a distance were misconfiguration and known unpatched vulnerabilities, at 45% and 38% respectively. Over 56% experienced a misconfiguration or known unpatched vulnerability incident involving their cloud native applications. Data leaks by insiders were more than twice as likely to have occurred in organizations with high levels of cloud native adoption, reinforcing that adopting zero trust principles becomes increasingly important in fully automated cloud based environments.

Snyk Report: State of Cloud Native Application Security | 04

### Over half of respondents suffered from a misconfiguration or known vulnerabilities incident

| Incident Type                | All | Low Adoption | High Adoption |
|------------------------------|-----|--------------|---------------|
| Malware                      | 10% | 14%          | 18%           |
| Misconfiguration             | 45% | 43%          | 50%           |
| Known unpatched vulnerabilities| 38% | 33%          | 45%           |
| Failed audit                 | 17% | 14%          | 21%           |
| Secret leaks                 | 18% | 18%          | 21%           |
| Data leaks by insider        | 14% | 7%           | 21%           |
| Haven’t experienced any security incidents | 18% | 21%          | 14%           |
| Prefer not to answer         | 10% | 10%          | 10%           |

### Nearly 60% have increased security concerns since adopting cloud native

Adoption of cloud native technologies will undoubtedly change the security posture of your overall application. While the core security principles remain constant, as with all emerging ecosystems the best practice is still being defined, driving fresh concern as teams navigate through unfamiliar landscapes. Our survey shows organizations are nearly 4x more likely to have increased rather than decreased concerns over their security posture since adopting cloud native.

Snyk Report: State of Cloud Native Application Security | 05

| Concern Level  | %  |
|----------------|----|
| Increased      | 58 |
| Decreased      | 15 |
| Hasn’t changed | 20 |
| Don’t know     | 7  |

### Misconfiguration is the area of most concern when moving to cloud native

Cloud native platforms utilizing automated tooling will rely on credentials such as secrets and API tokens in order to operate, and necessitates a more decentralized approach to managing such access. The need for effective management of these kinds of artifacts is a key differentiator from the more centralized pre-cloud era, and a major area of concern for operations teams transforming their infrastructure. Our survey showed that misconfigurations were the biggest area of increased concern, with over half of respondents stating it’s a bigger problem for them since moving to a cloud native platform. Despite secret leaks and data leaks not showing up highly in the actual incidents data, they feature strongly as areas of increased worry particularly among high adopters of cloud native technologies.

Snyk Report: State of Cloud Native Application Security | 06

#### Areas of concern

| Area of Concern               | All | Low Adoption | High Adoption |
|-------------------------------|-----|--------------|---------------|
| Misconfiguration              | 53% | 50%          | 57%           |
| Known unpatched vulnerabilities| 38% | 34%          | 45%           |
| Secret leaks                  | 44% | 35%          | 45%           |
| Data leaks by insider         | 23% | 17%          | 30%           |
| Malware                       | 16% | 18%          | 20%           |
| Insecure APIs                 | 29% | 22%          | 34%           |
| Ownership to handle/fix       | 52% | 45%          | 53%           |
| Impact of security on deployment velocity | 20% | 16%          | 22%           |
| Ability to respond quickly to risks | 45% | 38%          | 50%           |

### Deployment automation unlocks scalable security controls

Snyk Report: State of Cloud Native Application Security | 07

### Highly automated pipelines are twice as likely to be incorporate security testing throughout their development lifecycle

While building fully automated deployment pipelines can be challenging, once automation and processes are in place, they can create a virtuous cycle providing multiple integration points to enable further automation This is a key enabler for security testing. Companies with high levels of deployment automation were more than twice as likely to have adopted security testing at all points throughout the software development lifecycle, when compared to organizations with no automation. While companies of all sizes showed a clear preference to test in CI and earlier, enterprises were more likely to also be testing during later deployment and production stages. Despite testing in local development environments, such as an IDE, being a developer driven task, more automated organizations were nearly twice as likely to see their development teams adopt security early on in their workflows.

Snyk Report: State of Cloud Native Application Security | 08

#### When do you do security testing?

| Stage                       | All  | Enterprise | Medium | Small | Entirely Automated | Not Automated |
|-----------------------------|------|------------|--------|-------|--------------------|---------------|
| Local development eg IDE’s and CLI tools | 40%  | 34%        | 42%    | 39%   | 45%                | 24%           |
| Source Code repositories    | 50%  | 64%        | 56%    | 58%   | 65%                | 40%           |
| CI system                   | 36%  | 37%        | 22%    | 25%   | 74%                | 28%           |
| Deployment time             | 19%  | 15%        | 26%    | 19%   | 33%                | 8%            |
| Production                  | 15%  | 28%        | 32%    | 8%   | 32%                | 26%           |

### Continuous deployment empowers continuous testing

Snyk Report: State of Cloud Native Application Security | 09

Once the use of security tooling is integrated throughout the software development lifecycle, this dramatically expands the possibilities for more regular security testing. Nearly 70% of respondents with high levels of deployment automation were able to test their security daily or more frequently. This was 17x more than respondents who had no deployment automation, and 60% of those only tested their security monthly or less frequently. This was 3x more than respondents who had full deployment automation.

Snyk Report: State of Cloud Native Application Security | 10

#### How often do you do security testing?

| Frequency               | All  | Enterprise | Medium | Small | Entirely Automated | Not Automated |
|-------------------------|------|------------|--------|-------|--------------------|---------------|
| Continuously or daily   | 47%  | 54%        | 44%    | 34%   | 69%                | 4%            |
| Weekly                  | 18%  | 17%        | 12%    | 20%   | 18%                | 36%           |
| Monthly or less frequently | 35%  | 29%        | 44%    | 46%   | 12%                | 60%           |

### Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 week

Snyk Report: State of Cloud Native Application Security | 11

Testing faster leads to fixing faster. Over 72% of respondents with high levels of automation had an average time to fix vulnerabilities of less than one week, with 36% having an average of one day or less. Those with full automation were over 4x more likely to fix security issues in a day and over twice as likely to fix within a week. Automated testing is also a key enabler of visibility - you can’t fix what you can’t see. This was reinforced by the 28% of organizations with low levels of automation who responded that they didn’t know how long it takes them to fix issues.

| Time to Fix Critical Sec Issues | All  | Entirely Automated | Not Automated |
|---------------------------------|------|--------------------|---------------|
| 1 day or less                   | 24%  | 36%                | 8%            |
| 1 week                          | 45%  | 37%                | 20%           |
| 2 weeks                         | 10%  | 12%                | 6%            |
| 1 month                         | 8%   | 10%                | 3%            |
| Longer than 1 month             | 3%   | 8%                 | 8%            |
| Don't know                      | 10%  | 8%                 | 28%           |

### Companies who automate are twice as likely to implement security testing

Snyk Report: State of Cloud Native Application Security | 12

### Automation empowers shift left security

Adopting a broad and deep approach to security practices throughout the software development life cycle is key to a successful Cloud Native Application Security program. Our survey shows that companies with higher levels of cloud native automation have a greater adoption of security testing techniques. They tend to focus more on Static Application Security Testing (SAST), scanning for vulnerabilities in application dependencies with Software Composition Analysis (SCA), container image testing, and scanning infrastructure as code which are all techniques which fit well into the paradigm of automation. Organizations with fully automated deployment pipelines are twice as likely to adopt SAST and SCA tooling into their SDLC, and almost 3x as likely to add Dynamic Application Security Testing (DAST), although in general, dynamic testing isn’t as well adopted when compared with static testing. Policy compliance testing is still an emerging field, with only 23% of respondents having adopted it.

#### Enterprises are more likely to adopt security practices, yet smaller companies with less established security practices are keeping up

Larger companies and enterprises are, of course, more likely to have the resources to run dedicated security teams so it shouldn’t come as a surprise to see enterprises having the support to adopt formal Cloud Native Application Security Practices. While in smaller organizations the security function may be wholly owned by another org, such as the engineering teams, our survey shows that they are still able to keep up, particularly in the static testing space with over half of small organizations adopting SAST, SCA and container image scanning.

Snyk Report: State of Cloud Native Application Security | 13

#### Which software development life cycle security practices are you following?

| Practice                            | All  | Enterprise | Medium | Small | Entirely Automated | Not Automated |
|-------------------------------------|------|------------|--------|-------|--------------------|---------------|
| Static code analysis (SAST)          | 50%  | 56%        | 48%    | 51%   | 65%                | 33%           |
| Code scanning for package dependency vulnerabilities (SCA) | 50%  | 56%        | 48%    | 51%   | 65%                | 33%           |
| Dynamic Application Security Testing (DAST) | 29%  | 38%        | 27%    | 26%   | 43%                | 16%           |
| Interactive Application Security Testing (IAST) | 10%  | 12%        | 8%     | 10%   | 10%                | 10%           |
| Scanning infrastructure as code (Terraform, Kubernetes) | 34%  | 43%        | 32%    | 31%   | 44%                | 24%           |
| Container image scanning            | 45%  | 51%        | 43%    | 48%   | 58%                | 32%           |
| Policy compliance tools (Open Policy Agent/Gatekeeper) | 23%  | 29%        | 22%    | 20%   | 28%                | 16%           |

*Watch this on-demand webinar to learn tips for implementing security automation into modern development environments*

[Watch Now](link_to_webinar)

### Developers are adding security to their stack of hats

The move towards the concept of DevSecOps has accelerated in conjunction with adoption of cloud native technologies, as security shifts left in the software development lifecycle. Developers now have a pivotal role in ensuring that cloud native applications and infrastructure are secure since they increasingly contribute to the application, the infrastructure code, and workload deployment technologies. With this in mind, perception of security ownership provided interesting results in our survey set. While less than 10% of respondents in security roles believed developers were responsible for the security of their cloud native environment and applications, over 36% of developers stated that they were responsible.

Traditionally, in a more siloed organization, the ownership of security would have sat firmly with the security team. Respondents in security roles are almost 3x more likely to attribute security ownership to the IT security team than respondents in development teams are. These indicators suggest that this ownership is being accepted by the development teams faster than the security teams are willing to let go of it. Security teams are still adjusting to the shifting responsibilities which transitioning to cloud native brings, and development teams are increasingly aware of their growing role in Cloud Native Application Security.

Snyk Report: State of Cloud Native Application Security | 14

### Security isn't just for the security team

Snyk Report: State of Cloud Native Application Security | 15

#### Who is primarily responsible for the security of your cloud native environment and applications?

| Role                  | Developer Response | Security Response |
|-----------------------|--------------------|-------------------|
| Developers            | 37%                | 10%               |
| DevOps/DevSecOps       | 31%                | 33%               |
| IT security team      | 13%                | 31%               |
| Application security team | 14%                | 23%               |
| No-one                | 3%                 | 2%                |

### Developers and security both understand the importance of Cloud Native Application Security

The increased awareness of security in development teams was also reinforced by the survey results around security exposure concerns. Both developers and security professionals alike shared that switching to cloud native technologies had increased their security concerns. Developers were just as likely to be invested in good security outcomes as the security team - good news for the adoption of DevSecOps principles which relies on shared security goals across the organization.

Snyk Report: State of Cloud Native Application Security | 16

#### Has switching to Cloud Native technologies increased or decreased your security exposure concerns?

| Concern Level  | Developer Response | Security Response |
|----------------|--------------------|-------------------|
| Increased      | 58%                | 61%               |
| Decreased      | 13%                | 13%               |
| Hasn’t changed | 21%                | 18%               |

*Learn how Twilio’s Head of Product Security scaled through dev-first security and devsecops in a cloud native environment*

[Watch Now](link_to_twilio_webinar)

> Snyk’s CNAS report shows clear movement in a positive direction. 99% of respondents recognize that security is important to their business strategy. That’s a world I want to live in

### Curious how Snyk can help?

Snyk is a developer-first platform for building software securely. Learn more about how Snyk can help you secure cloud native applications across your IDEs, repos, containers, and pipelines.

[Learn more](link_to_snyk)
