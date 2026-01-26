# Enhanced 5G and Zero Trust Cloud and Operational Security Aspects

## Table of Contents
- [Executive Summary](#executive-summary)
- [1. Implications and Scope of ZTA for 5G Cloud](#1-implications-and-scope-of-zta-for-5g-cloud)
- [2. Current State of Zero Trust for 5G](#2-current-state-of-zero-trust-for-5g)
  - [2.1 NIST ZTA](#21-nist-zta)
  - [2.2 CISA Zero Trust Maturity Model (ZTMM)](#22-cisa-zero-trust-maturity-model-ztmm)
  - [2.3 3GPP](#23-3gpp)
  - [2.4 ETSI NFV-SEC Expert Group](#24-etsi-nfv-sec-expert-group)
  - [2.5 O-RAN ALLIANCE](#25-o-ran-alliance)
  - [2.6 FCC CSRIC](#26-fcc-csric)
- [3. 5G Cloud Deployment Models](#3-5g-cloud-deployment-models)
  - [3.1 5G Cloud Infrastructure](#31-5g-cloud-infrastructure)
  - [3.2 Four 5G Cloud Deployment Models](#32-four-5g-cloud-deployment-models)
  - [3.3 Implications of the 5G Cloud Deployment Models](#33-implications-of-the-5g-cloud-deployment-models)
- [4. 5G Cloud Zero Trust Security Controls](#4-5g-cloud-zero-trust-security-controls)
  - [4.1 ZT Elements of 5G Cloud Deployments](#41-zt-elements-of-5g-cloud-deployments)
  - [4.2 Cloud-Native Policy Management for Zero Trust](#42-cloud-native-policy-management-for-zero-trust)
- [5. Conclusions, Recommendations, and Next Steps](#5-conclusions-recommendations-and-next-steps)
  - [5.1 Recommendations](#51-recommendations)
  - [5.2 Next Steps](#52-next-steps)
- [Acronyms & Abbreviations](#acronyms--abbreviations)
- [References](#references)
- [Acknowledgments](#acknowledgments)
- [Copyright and Disclaimer](#copyright-and-disclaimer)

## Executive Summary

Zero Trust (ZT) is a concept that no digital system or human user, whether external or internal, can be trusted, regardless of ownership and location. Zero Trust Architecture (ZTA) is a plan to implement ZT in a digital system or network of digital systems. ATIS published a paper in July 2023, “Enhanced Zero Trust and 5G,” that focused on broadly implementing a ZTA in 5G. In it, ATIS enumerated 12 required central security controls for a 5G ZTA, along with numerous recommendations to 3rd Generation Partnership Project (3GPP) to align 5G and 6G security specifications with a ZTA.

5G Mobile Network Operators (MNOs) architect and deploy their 5G wireless offerings on fully virtualized or cloud-native platforms and networks. When implementing cloud-native networks, the cloud computing platforms host all the various parts of a 5G System, including the 5G Core Network, Operations and Business Support Systems (OSS and BSS), and Open Radio Access Networks (O-RAN).

At present, there are four dominant cloud models in production use. Two of these models are considered legacy in that they use traditional virtualized and cloud compute architectures, while the other two leverage the cloud services delivered by Hyperscaler Cloud Providers (HCPs). The HCP-based models are gaining momentum in the industry and driving new investments in the public cloud. The two legacy models are the multi-vendor stack and the single vendor full stack, which are private cloud implementations. The two public cloud models leverage well-known public cloud offerings from the cloud providers. One is the standard public offering, and the second is private and uses the same technology stacks but is dedicated specifically for the 5G MNO installed on their physical locations.

5G networks are currently being deployed in a hybrid cloud environment using combinations of the four models of private and public clouds. The 5G MNO must rely on several different Standards Development Organizations (SDOs) for cloud computing architecture and security.

This paper looks at the implementation and operational aspects of implementing a ZTA in the 5G MNO cloud environments that are hosting their 5G services. We will look at the four cloud deployment models in terms of a ZTA in combination with a discussion of the 12 security controls. We will highlight any potential deployment issues relating to these 12 security controls for each of the four models. The development and rollout of the security controls have also been primarily centered in the IT world. For some, there are gaps due to differences from the IT side that must be filled in order to deploy the controls in the 5G realm. This paper highlights these gaps, including threat intelligence feeds. Gaps filled by new threat models such as MITRE’s FiGHT and Groupe Spéciale Mobile Association (GSMA) Mobile Threat Intelligence Framework (MOTIF) are also highlighted.

The ATIS Cloud 5G ZTA study was informed by the work at U.S. Department of Commerce National Institute of Standards and Technology (NIST) and ZT subject matter experts from organizations that are stakeholders in 5G network security. The recommendations enumerated in Section 5 provide concluding strategic guidance to enhance security and operational resilience in 5G cloud environments through a ZT framework. Recommendations are broken down into sections for each responsible standards bodies, infrastructure vendors, HCPs, and security operations teams.

## 1. Implications and Scope of ZTA for 5G Cloud

Traditionally, network infrastructure has been deployed within the MNO’s premises where the MNO owns, manages, and controls all assets, including facilities, transport infrastructure, network services, network applications, and data. Mobile networks are evolving toward cloud-based architectures that introduce a layered implementation where multiple stakeholders, including vendors, integrators, and providers, may own, manage and control facilities, network services, network applications, and/or infrastructure.

The introduction of third parties and cloud-native deployments facilitate new threats from internal and external attacks on 5G critical infrastructure. External and internal threat actors could gain access to 5G virtual or cloud-native functions through the infrastructure, owned or managed by these third parties, to perform confidentiality, integrity, and availability attacks on the network. Within the cybersecurity domain, the act of a threat actor (internal and external) gaining a foothold in a network is called an Advanced Persistent Threat (APT). Most recently, Salt Typhoon is an APT that received considerable industry recognition [1]. In addition, many cloud models can obscure visibility into lower layers of the infrastructure, making it much more difficult to monitor for cybersecurity vulnerabilities and attacks. The impact of these attacks on 5G voice and data services could include outages, performance degradation, unauthorized reconnaissance, and data theft.

Mitigating these threats can be challenging because each of the third-party vendors/providers may have their own set of security controls that may or may not be sufficient and may not seamlessly interwork with other system-wide security controls. As such, ATIS has created a set of fundamental zero trust security control groups to help address this issue.

![Image description: ATIS’ 12 ZTA Security Control Groups diagram showing 12 interconnected security controls: 1. Sensitive Data Encryption, 2. Identity and Access Management, 3. PKI-based Mutual Authentication, 4. Multi-Factor Authentication, 5. Network Micro-segmentation, 6. Anomalous Behavior Detection, 7. Threat and Endpoint Detection and Response, 8. Continuous Monitoring, Logging, and Alerting, 9. Secure Software Development, 10. Threat Intelligence, 11. Automated Security Testing, 12. SIEM/SOAR Integration.]

Figure 1 illustrates the 12 fundamental security control groups identified in the 2023 ATIS paper, “Enhanced Zero Trust and 5G” [2], to achieve a ZTA for 5G networks. These are:

1. Sensitive Data Encryption for data in motion, data at rest, and data in use
2. Identity and Access Management (IAM), including dynamic access control policies and the principle of least privilege
3. Public Key Infrastructure (PKI)-based Mutual Authentication for machine-to-machine communications
4. Multi-Factor Authentication (MFA) for human users
5. Network micro-segmentation and micro-perimeters
6. Anomalous Behavior Detection, using artificial intelligence/machine learning (AI/ML)
7. Threat and Endpoint Detection and Response (TDR/EDR)
8. Continuous Monitoring, Logging, and Alerting
9. Secure software development based upon the DevSecOps including continuous integration/continuous deployment (CI/CD)[3] and NIST Secure Software Development Framework (SSDF)
10. Threat Intelligence
11. Automated Security Testing/Configuration Validation
12. Security Information Event Management (SIEM)/Security Orchestration, Automation, and Response (SOAR) integration

The focus of this paper is to provide recommendations about how to implement a ZTA and all of the ATIS-defined security controls into the 5G cloud infrastructure. This leaves a gap in terms of what security controls are required within the infrastructure to define ZTA for the 5G cloud. One of the primary goals of this paper is to recommend how the ATIS-defined 12 critical security controls are implemented uniformly in the 5G cloud infrastructure to provide layers of defense required for a Defense in Depth strategy.

There is an overlap with some of these controls across the 3GPP Network Functions (NFs), applications, and management within the 5G cloud. Examples of this include security and audit logs, alerts, and telemetry being sourced from the 3GPP NFs and the applications, which are then streamed toward continuous monitoring and control systems such as the Security Information Event Management (SIEM) and EDR functions. SIEM and EDR agents may exist within the NF and/or the underlying cloud infrastructure.

Another key mechanism is an IAM system that controls human access to the NFs and applications. That same IAM can control access for the 5G cloud infrastructure components. This paper will give guidance about how these security controls should be deployed in the 5G cloud and the overlap into the 3GPP components. Gaps that exist along with recommendations to close them are enumerated for the appropriate standards or industry bodies.

![Image description: 12 ZT Security Control Groups Categorized into two main buckets: Securing the Cloud Environment (Controls 1, 2, 3, 4, 5, 9, 11) and Information Input Sources to Enable ZT Policy Decisions (Controls 6, 7, 8, 10, 12).]

Figure 2 shows how the ATIS 12 ZT security control groups have been divided into two categories: “Securing the Cloud Environment” and “Information Input Sources to Enable ZT Policy Decisions.” Given the critical role of policy management, we also include a section describing the role of policy management in ZT cloud deployments and the relationship to the security controls. Security controls should be deployed at each layer (Application, CaaS, Infrastructure) and visibility (via logging, Fault, Configuration, Accounting, Performance, and Security (FCAPS), EDR, and other telemetry) should be handled for each layer at that layer. In other words, one layer should not provide visibility at another layer. Telemetry across the layers can be sent to a centralized system, such as SIEM or Service Management and Orchestration (SMO), for centralized collection and correlation.

The focus of this document specifically addresses the intersection of ZT and 5G infrastructure (i.e., the 5G Core and Radio Access Network (RAN)) as deployed in cloud-native environments. ZT mechanisms for the operations and management environment of the 5G infrastructure are not specifically addressed in this document. In addition, important considerations such as the creation of a security architecture and associated trust boundaries are not addressed.

## 2. Current State of Zero Trust for 5G

### 2.1 NIST ZTA
NIST defines zero trust as a concept that no digital system or human user, whether external it internal, can be trusted, regardless of ownership and location. Zero Trust Architecture (ZTA) is a plan to implement ZT in a digital system or network of digital systems. However, NIST points out that, within a ZTA, an “implicit trust zone” can exist in a system which represents an area where all the entities are trusted to at least the level of the last PDP/PEP gateway. NIST advises that the implicit trust zone within the ZTA must be as small as possible [4].

NIST defined seven tenets as foundational for its ZT architecture:

**List 1. NIST Seven Tenets of Zero Trust [4]**
- **T1.** All data sources and computing services are considered resources
- **T2.** All communication is secured regardless of network location
- **T3.** Access to individual resources is granted on a per-session basis
- **T4.** Access to resources is determined by dynamic policy
- **T5.** The operator monitors and measures the integrity and security posture of all owned and associated assets
- **T6.** All resource authentication and authorization are dynamic and strictly enforced before access is allowed
- **T7.** The operator collects information about the current state of assets, network infrastructure and communications and uses it to improve its security posture

The tenets are intended to provide a set of principles that are intentionally broad but also fully inclusive so that any gaps can be avoided.

### 2.2 Cybersecurity and Infrastructure Security Agency (CISA) Zero Trust Maturity Model (ZTMM)
The ZTMM is a framework that helps organizations assess and improve their ZTA implementation through a journey of four stages that provide a structured approach to measure progress and identify areas for improvement:

1. **Traditional Stage**: Security controls are implemented only at the perimeter to protect against external threats.
2. **Initial Stage**: Foundational security controls are in place and basic ZT principles are applied to protect NFs as micro-perimeters from external and internal threats. This consists of increased visibility and control of network traffic, and authentication and authorization of external and internal subjects requesting access to resources.
3. **Advanced Stage**: More advanced security controls are in place to enable greater visibility and control over network traffic on external and internal interfaces. Micro-segmentation is utilized to prevent lateral movement within the network and the implementation of continuous authentication and authorization.
4. **Optimal Stage**: AI/ML is leveraged for advanced threat detection and decision-making. This allows for AI/ML driven automated responses to identified threats and for continuous, automatic optimization of security policies.

### 2.3 3GPP
3GPP has undertaken a phased approach to the evaluation of 3GPP architecture for all seven of the NIST ZT tenets. The initial focus has been on evaluation of the 3GPP 5G Core Service-Based Architecture (SBA), while the O-RAN Alliance is focused on ZTA for Open RAN.

The first 3GPP evaluation was undertaken and documented in 3GPP Release 18 Technical Report (TR) 33.894 [5], which noted that Tenets 1, 2, and 3 required no further study as applicable security mechanisms already exists. For the remaining Tenets, although this report did not agree to standardize solutions for ZT, it did allow for further studies related to exposing information for security monitoring and policy enforcement. A subsequent evaluation of the 3GPP 5G Core SBA was undertaken in 3GPP Release 19 TR 33.794 [6], where the focus was on two aspects: 1) data exposure for security evaluation and monitoring and 2) security mechanism for dynamic policy enforcement. For data exposure to enable security evaluation and monitoring, it was concluded that it can be addressed with NF requirements to generate security event logs so data can be collected at the SBA layer for the following security incidents/scenarios:

1. Authentication and authorization failure event
2. Unexpected setup of Transport Layer Security (TLS) session and Application Programming Interface (API) invocation related to unauthorized reconnaissance
3. Malformed message event
4. High service load
5. Unexpected SBI call flows
6. Unexpected use of APIs exposed by services in SBA layer

As of this writing, further progress was made, and 3GPP approved a Rel. 20 work item for 5G-Advanced features on security-related events handling [7]. The main objective of this work item is to specify the data collection requirements that can be used for security purposes, which includes the following:
- General requirements for security events handling and collection
- Security requirements to transfer or communicate security events
- To specify events that need to be reported

Further work is needed for policy enforcement in the 5G Advanced and 6G systems. ATIS is working on a subsequent publication that will provide additional industry insight into what is required.

### 2.4 ETSI NFV-SEC Expert Group
The Security Expert Group of ETSI Network Function Virtualization (NFV) (ETSI NFV-SEC) is responsible for developing specifications around Whole System Security Management and Monitoring including:
- Virtualized Network Function (VNF) Package Security
- VNF Lifecycle Management Security
- Dynamic Certificate Management for Virtual Entities
- Isolation and Trust Domains (Containers)
- API Access (Tokens)
- And more

ETSI GS NFV-SEC024 Security Management Specification [8] provides a number of ZT-related specifications such as those relating to component compromise, multi-layer security, ZT security as an overlay, trust-but-verify approach, resiliency and redundancy, and more. This work was delayed during the COVID-19 pandemic, but ETSI NFV-SEC published updated drafts in October 2023 October 2024. Their plan is to finalize their draft by end of May 2025 and publish the final document in August 2025.

In March 2024, ETSI MEC Working Group published a Study on MEC Security [9] that references 3GPP’s TR 33.894 [5] ZT study as something that they are tracking. ETSI is studying the security aspects related to Multi-access Edge Compute (MEC) application provenance verification with cryptographic attestations, including leveraging secure boot processes that incorporate a hardware root of trust and aspects of Internet Engineering Task Force’s (IETF) Remote ATtestation procedureS (RATS) Architecture (RFC 9334) [10]. This study has identified key issues relating to stolen MEC application access tokens, stolen MEC application identity, compromised MEC applications and asset theft, compromise of application package during on-boarding, compromise of application during updates, threats associated with application package deletion, and MEC application anomalous behavior.

### 2.5 O-RAN ALLIANCE
O-RAN ALLIANCE [11] is committed to the security of the entire O-RAN architecture. O-RAN security is led by the O-RAN ALLIANCE’s Security Work Group 11 (WG11), which is responsible for threat and risk analysis and normative security specifications. One of the approaches to open the RAN ecosystem is to have cloud-native NFs run on O-RAN-optimized cloud infrastructure, which is referred to as the O-Cloud. O-Cloud is specified by the O-RAN ALLIANCE WG6, with security requirements specified by WG11.

The WG11 technical report “O-RAN Study on Security for O-Cloud” [12] analyzes the security of O-Cloud architectural components and interfaces and provides a risk assessment of O-Cloud hardware and software infrastructures managed by the Service Management and Orchestration (SMO) via the O2 interface. The O-RAN Security Requirements and Controls Specification provides the normative security requirements for O-Cloud, SMO, and the O2 interface, along with the other O-RAN architecture elements and interfaces.

O-RAN Alliance is pursuing a ZTA [13] with core principles of continuous monitoring, authentication and authorization for internal and external subjects requesting access to O-RAN resources, least privilege access, and confidentiality and integrity protection of data, plus other comprehensive security controls throughout the O-RAN architecture, to protect against continuously evolving threats. The O-RAN Alliance is following the CISA ZTMM [14] to reach a ZTA in a phased approach.

O-RAN Alliance has identified O-RAN security specifications as being at the Initial stage of the CISA ZTMM, with plans to progress to the Advanced stage and eventually the Optimized stage[14]. To guide progress through the CISA ZTMM stages, WG11 has a ZTA work item. The work item’s objectives are to study the applicability of the seven ZT tenets defined in NIST Special Publication (SP) 800-207 “Zero Trust Architecture”[4] to O-RAN Alliance’s current security architecture and specifications, conduct an analysis on the current alignment between the seven tenets and O-RAN’s security requirements and controls, and define new specifications where needed.

In October 2024, WG 11 published version 1 of their technical report for this work item, “Study on Zero Trust Architecture for O-RAN” [15]. In this technical report, WG 11 determined that at varying level of degrees, all seven tenets are applicable to O-RAN Alliance’s architecture. Fully realizing all seven tenets may require integration with systems outside of the scope of O-RAN Alliance. This will have to be left up to each MNO implementation. For its part, O-RAN Alliance will specify security requirements, controls, and specifications that support the NIST tenets. WG 11 is still in the process of reviewing the current O-RAN architecture, including O-Cloud, to develop these new security requirements, controls, and specifications as needed.

### 2.6 Federal Communications Commission (FCC) CSRIC
Guided by the U.S. National Cybersecurity Strategy published on March 2, 2023 [16], the CSRIC VIII Report on Recommendations on the Role of the FCC in Promoting the Availability of Standards for 5G Environment of Virtualization Technology [17], responds to the four inquiries presented to the Communications Security, Reliability, and Interoperability Council (CSRIC) VIII by the FCC.

- **Query 1**: “Steps that the FCC should take (if any) to help coordinate formal standards, informal standards, and any collaborative open-interface community efforts to ensure interoperability in the virtualized 5G space.”
- **Query 2**: “Recommendations on how the FCC can promote collaborations to achieve innovation in virtualized 5G.”
- **Query 3**: “Recommendations on actions the FCC can take to build confidence in virtualized 5G solutions based upon open-source cloud computing software.”
- **Query 4**: “Any other ways in which FCC can promote a diverse, competitive 5G environment.”

The CSRIC report, which was developed through a cross-private and public sector collaboration effort, goes on to provide detailed recommendations for each of these queries. Most relevant to this document is the committee’s recommendations on security and resiliency in response to Query 4.

The report recommends that the FCC can build confidence in virtualized 5G solutions by ensuring that security is built into systems from outset, rather than security being treated as something to be added later. The FCC should work with other government agencies to develop concise security requirements for virtualized 5G telecommunication environments based on ZT. Furthermore, the FCC should work with relevant U.S. government agencies to support the development of open-source test and evaluation tools to test these requirements.

## 3. 5G Cloud Deployment Models

### 3.1 5G Cloud Infrastructure
5G cloud infrastructure is the set of computation, storage, and networking equipment with related software that offers physical and/or virtual cloud resources and services to host 5G NFs and management systems [18].

Examples of 5G NFs and management systems hosted on 5G cloud infrastructures include the 5G Core, O-RAN NFs (i.e., O-CU-CP, O-CU-UP, and O-DU), and O-RAN SMO functions [19].

Table 1 describes the typical resources for a 5G cloud infrastructure, which requires management, orchestration, and workflow management services to include, but are not limited to, the following functionalities:
- Discovery and administration of 5G cloud infrastructure resources (i.e., storage, compute, networking)
- Software management of 5G cloud infrastructure, NFs, and management systems [19]
- Scale-In, Scale-Out of 5G cloud infrastructure resources, NFs, and management systems
- FCAPS (PM, CM, FM, Communication Surveillance) of 5G cloud infrastructure resources, NFs, and management systems

| 5G Cloud Infrastructure Resources | Description |
| :--- | :--- |
| Operating System | In virtualized host and guest environments, the OS runs within each VM. Alternatively, if there is no underlying hypervisor present, the operating system runs directly on the bare metal hardware. |
| Virtual Machine | A virtual guest environment executed on a hypervisor on a host. A set of system isolation technologies that provide various degrees of security isolation with the host machine’s OS kernel. |
| Containers | A method for packaging and securely running an application that allows execution of multiple isolated user space instances while sharing the same underlying OS kernel. |
| Virtual Network Infrastructure | For communications within and between virtual machines and containers. |
| Hypervisor | When virtualization is used to manage resources, the hypervisor is responsible for allocating resources to each virtual machine. It may also be leveraged for implementing security. |
| Processing & Memory | The physical hardware that supplies central processing unit (CPU) time and physical memory. |
| Data Storage | The physical hardware used for file storage. |
| Network | This can be a physical or virtual network. It is responsible for carrying communications between systems and possibly the internet. |
| Physical Facility | The actual physical building where the cloud systems are located. |

**Table 1: 5G Cloud Infrastructure Resources (Adapted from PCI SSC Cloud Computing Guidelines [20])**

NIST SP 500-292 NIST Cloud Computing Reference Architecture [21] breaks down the three major types of Cloud Service Models. For 5G MNOs (the cloud consumer in the NIST models), these service types are relevant to the public cloud and related private cloud offerings from the various cloud providers.

- **Infrastructure as a Service (IaaS)**: The cloud provider provides the physical infrastructure (data centers, servers, hypervisors, network). The 5G MNO is responsible for the operating systems, virtual machines, container software systems, and containers that run the 5G NFs.
- **Platform as a Service (PaaS)**: The cloud provider provides the platform, which includes the operating systems, virtual machines, and the Container-as-a-Service (CaaS) software components. The CaaS is located in the middleware layer defined by NIST. 5G MNOs load their NFs as Linux containers and virtual machines. Everything below the NFs themselves is the responsibility of the cloud provider PaaS service.
- **Software as a Service (SaaS)**: The cloud provider provides the infrastructure and platform. The application can be owned by an application vendor, which can be different from the cloud provider. The 5G MNO purchases the use of that application and is responsible for securing user access and managing data.

![Image description: NIST SP 500-292 NIST Cloud Computing Reference Architecture diagram showing the interaction between Cloud Consumer, Cloud Provider, Cloud Auditor, Cloud Broker, and Cloud Carrier. The Cloud Provider section details Service Orchestration, Resource Abstraction and Control Layer, and Physical Resource Layer.]

### 3.2 Four 5G Cloud Deployment Models

![Image description: Four 5G Cloud Deployment Models diagram showing: 1. Multi-Vendor Stack (MNO Data Center), 2. Telco Vendor Full Stack (MNO Data Center), 3. HCP Vendor Public Offering (HCP Data Center), and 4. HCP Vendor Private Cloud (MNO Data Center).]

Within 5G MNO cloud networks, there are four concurrent cloud models that are in production use. Two of these are legacy, and two of them constitute a movement into the public cloud, where much of the present cloud investment is moving. The two legacy models are the multi-vendor stack and the telco vendor full stack.

In prior years, 5G MNOs built private clouds in their data centers using these two models, which support both Linux-based VNFs and Container Network Functions (CNFs) for their telco applications. With 5G, much of the investment is being transferred into two variations of the offerings with the Hyperscale Cloud Providers (HCPs). These are public cloud and a variant of the public cloud, which is an HCP private offering that uses the same technology stacks, but is dedicated specifically for the 5G MNO on their physical location, in a configuration also referred to as Hybrid Cloud.

At present, it is common to find all four models currently in both proof-of-concept testing and production. This current state constitutes a hybrid cloud environment using combinations of these private and public cloud models.

#### 3.2.1 Multi-Vendor Stack
The multi-vendor stack is composed of different vendors for the server hardware, virtual or cloud-native NFs, and data storage. The CaaS portion hosts the 5G NFs, which run as containers provided by the telco infrastructure vendor. Each 5G MNO has historically chosen its own mix of vendors for their multi-vendor stacks, which causes a large variety of combinations across different 5G MNOs. In this model, the 5G MNO has complete control over all layers and components of the cloud stack, and they function as the primary integrator responsible for making all of the component parts work together from an operational standpoint. This model is deployed on the physical premises of the 5G MNO.

#### 3.2.2 Telco Vendor Full Stack
In the vendor full stack model, the infrastructure vendor provides both the various NFs that run the mobile network and the full cloud-based infrastructure including the server hardware, the applications, and the data storage. The infrastructure vendor selects the different vendors that will make up the cloud stack layers. The CaaS architecture is chosen by the infrastructure vendor and can be built around open-source solutions that are part of the Linux distributions used.