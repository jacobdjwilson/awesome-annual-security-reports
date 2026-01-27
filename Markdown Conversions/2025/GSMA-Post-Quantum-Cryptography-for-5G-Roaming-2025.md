# GSM Association PQ.05 Official Document Post Quantum Cryptography for 5G Roaming use case

**Non-confidential**

**Quantum-safe Cryptography for 4G and 5G Roaming**

**Version 1.0**

**26 June 2025**

**Security Classification: Non-confidential**

Access to and distribution of this document is restricted to the persons permitted by the security classification. This document is subject to copyright protection. This document is to be used only for the purposes for which it has been supplied and information contained in it must not be disclosed or in any other way made available, in whole or in part, to persons other than those permitted under the security classification without the prior written approval of the Association.

**Copyright Notice**
Copyright © 2025 GSM Association

**Disclaimer**
The GSM Association (“Association”) makes no representation, warranty or undertaking (express or implied) with respect to and does not accept any responsibility for, and hereby disclaims liability for the accuracy or completeness or timeliness of the information contained in this document. The information contained in this document may be subject to change without prior notice.

**Compliance Notice**
The information contain herein is in full compliance with the GSM Association’s antitrust compliance policy.

V1.0 | Page 1 of 24

---

## Table of Contents

- [1 Introduction](#1-introduction)
  - [1.1 Overview](#11-overview)
  - [1.2 Scope](#12-scope)
  - [1.3 Abbreviations](#13-abbreviations)
  - [1.4 References](#14-references)
- [2 Executive Summary](#2-executive-summary)
  - [2.1 Migration Plan](#21-migration-plan)
  - [2.2 Migration Prioritization](#22-migration-prioritization)
- [3 Standards](#3-standards)
  - [3.1 3GPP Standards](#31-3gpp-standards)
  - [3.2 GSMA Recommendations & Guidelines](#32-gsma-recommendations--guidelines)
- [4 Roaming Use-cases](#4-roaming-use-cases)
  - [4.1 5G Roaming Architecture](#41-5g-roaming-architecture)
    - [4.1.1 Direct TLS](#411-direct-tls)
    - [4.1.2 Protocol for N32 Interconnect Security (PRINS)](#412-protocol-for-n32-interconnect-security-prins)
    - [4.1.3 Inter-PLMN User Plane Security](#413-inter-plmn-user-plane-security)
  - [4.2 4G Roaming](#42-4g-roaming)
  - [4.3 VoNR / VoLTE Roaming](#43-vonr--volte-roaming)
- [5 Scope](#5-scope)
  - [5.1 Sensitive Data Discovery](#51-sensitive-data-discovery)
    - [5.1.1 5G Roaming](#511-5g-roaming)
    - [5.1.2 4G Roaming](#512-4g-roaming)
    - [5.1.3 VoNR / VoLTE Roaming](#513-vonr--volte-roaming)
  - [5.2 Cryptographic Inventory](#52-cryptographic-inventory)
  - [5.3 Threats and Attacks against Roaming Interfaces](#53-threats-and-attacks-against-roaming-interfaces)
- [6 Migration Strategy Analysis and Dependencies](#6-migration-strategy-analysis-and-dependencies)
  - [6.1 Standards](#61-standards)
    - [6.1.1 Public Key Infrastructure & Certificate Management](#611-public-key-infrastructure--certificate-management)
    - [6.1.2 TLS 1.3](#612-tls-13)
    - [6.1.3 IKEv2 / IPSec](#613-ikev2--ipsec)
    - [6.1.4 Hybrid Cryptography](#614-hybrid-cryptography)
  - [6.2 Regulations & Migration Strategy with Roaming Partners](#62-regulations--migration-strategy-with-roaming-partners)
    - [6.2.1 National Guidelines: Regulation (Intra-PLMN) and Inter-PLMN](#621-national-guidelines-regulation-intra-plmn-and-inter-plmn)
    - [6.2.2 Vendors](#622-vendors)
    - [6.2.3 Operators](#623-operators)
    - [6.2.4 3rd-parties (e.g. IPX providers)](#624-3rd-parties-eg-ipx-providers)
    - [6.2.5 LEAs](#625-leas)
    - [6.2.6 Performance](#626-performance)
    - [6.2.7 Gantt Chart for PQC Migration](#627-gantt-chart-for-pqc-migration)
    - [6.2.8 PQC Migration Process Description](#628-pqc-migration-process-description)
    - [6.2.9 Synergy with Internal Programs](#629-synergy-with-internal-programs)
    - [6.2.10 Synergy with External Programs](#6210-synergy-with-external-programs)
- [A.1 Document History](#a1-document-history)
- [A.2 Other Information](#a2-other-information)

---

## 1 Introduction

The GSMA PQTN Task Force has published a series of documents about the impact of Post Quantum Cryptography (PQC) on telecoms.

This document is an extension of PQ.03 v2 - Quantum Safe User Cases and Migration [1] and address 4G and 5G the roaming.

### 1.1 Overview

3GPP and GSMA have developed a standardised roaming architecture, specifications and requirements for use-cases where a UE roams from its Home PLMN (HPLMN) to a Visited PLMN (VPLMN) and vice-versa. This document provides an overview of threats, impacts and mitigation mechanisms against a Cryptographically Relevant Quantum Computer (CRQC) targeting the roaming architecture and its interfaces.

### 1.2 Scope

This document covers mechanisms that may be employed to protect UEs and operator networks from a CRQC when a UE roams between HPLMN and VPLMN and connects to the visitor network. The roaming architecture considers the scenarios where a Security Edge Protection Proxy (SEPP) is responsible for protecting the operator’s core network from attacks targeting (or originating from) the inter-connect interfaces (N32-c, N32-f). The interfaces may be secured using either:

1. Direct TLS between SEPPs
2. PRotocol for N32 INterconnect Security (PRINS)

Diameter inter-connect security is included in the analysis: when a 5G UE connects to a 4G roaming network and vice-versa.

### 1.3 Abbreviations

| Term | Description |
| :--- | :--- |
| 3GPP | Third Generation Partnership Program |
| CDR | Call Data Record |
| CRQC | Cryptologically relevant quantum computer |
| DEA | Diameter Edge Agent |
| DoS | Denial of service |
| DRA | Diameter Relay Agent |
| ECDHE | Elliptic Curve Diffie-Hellman Ephemeral |
| GSMA | GSM Association |
| GTP-U | GPRS Tunnelling Protocol User Plane |
| HNDL | Harvest Now Decrypt Later |
| HPLMN | Home PLMN |
| hSEPP | Home SEPP (Security Edge Protection Proxy) |
| IMS | IP Multimedia Subsystem |
| IPUPS | Inter-PLMN User Plane Security |
| IPX | IP exchange |
| JWE | JSON Web Encryption |
| JWS | JSON Web Signature |
| MITM | Man in the middle |
| ML-DSA | Module-Lattice-Based Digital Signature Algorithm |
| ML-KEM | Module-Lattice-Based Key-Encapsulation Mechanism |
| NDS/IP | Network Domain Security for IP based protocols |
| OCSP | Online Certificate Status Protocol |
| PDU | Protocol Data Unit |
| PGW | Packet Data Network Gateway |
| PKI | Public Key Infrastructure |
| PLMN | Public Land Mobile Network |
| PRINS | PRotocol for N32 INterconnect Security |
| RSA | Rivest-Shamir-Adleman |
| RTP | Real-time Transport Protocol |
| SBI | Service Based Interface |
| SEPP | Security Edge Protection Proxy |
| SGW | Serving Gateway |
| SIP | Session Initiation Protocol |
| SRTP | Secure RTP |
| TEID | Tunnel End-Point Identifier |
| TLS | Transport Level Security |
| UE | User Equipment |
| UPF | User Plane Function |
| VoLTE | Voice over LTE |
| VoNR | Voice over New Radio |
| VPLMN | Visited PLMN |
| vSEPP | Visited SEPP (Security Edge Protection Proxy) |

**Table 1 Abbreviations**

### 1.4 References

| Ref | Doc Number | Title |
| :--- | :--- | :--- |
| [1] | PQ.03 v2 | Post Quantum Cryptography – Guidelines for Telecom Use Cases, GSMA PQTN, PQ.03 Version 2.0, 04 Oct 2024 |
| [2] | RFC 8446 | The Transport Layer Security (TLS) Protocol Version 1.3, RFC 8446, IETF, Aug 2018 [https://datatracker.ietf.org/doc/html/rfc8446](https://datatracker.ietf.org/doc/html/rfc8446) |
| [3] | TS 23.501 | System architecture for the 5G System (5GS) |
| [4] | TS 33.501 | Security architecture and procedures for 5G system |
| [5] | NG.113 | Official Document NG.113 5GS Roaming Guidelines, Version 11.0 October 2024, GSMA |
| [6] | IR.34 | Official Document IR.34 - Guidelines for IPX Provider networks (Previously Inter-Service Provider IP Backbone Guidelines), Version 13.0 October 2016, GSMA |
| [7] | TS 33.210 | Network Domain Security (NDS); IP network layer security |
| [8] | TS 33.310 | Network Domain Security (NDS); Authentication Framework (AF) |
| [9] | RFC 7516 | JSON Web Encryption (JWE), RFC 7516, May 2015, IETF [https://datatracker.ietf.org/doc/html/rfc7516](https://datatracker.ietf.org/doc/html/rfc7516) |
| [10] | RFC 7515 | JSON Web Signature (JWS), RFC 7515, May 2015, IETF [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) |
| [11] | IR.88 | Official Document IR.88 - EPS Roaming Guidelines. Nov 2021, GSMA |
| [12] | IR.92 | Official Document IR.92 IMS Profile for Voice and SMS, June 2024, GSMA |
| [13] | NG.114 | NG.114 IMS Profile for Voice, Video and Messaging over 5GS, Jan 2024, GSMA |
| [14] | X.509 | Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile, RFC 5280, May 2008, IETF [https://datatracker.ietf.org/doc/html/rfc5280](https://datatracker.ietf.org/doc/html/rfc5280) |
| [15] | FIPS 203 | National Institute of Standards and Technology (2024) Module-Lattice-Based Key-Encapsulation Mechanism Standard. NIST FIPS 203. [https://doi.org/10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203) |
| [16] | FIPS 204 | National Institute of Standards and Technology (2024) Module-Lattice-Based Digital Signature Standard. NIST FIPS 204. [https://doi.org/10.6028/NIST.FIPS.204](https://doi.org/10.6028/NIST.FIPS.204) |
| [17] | FIPS 205 | National Institute of Standards and Technology (2024) Stateless Hash-Based Digital Signature Standard. NIST FIPS 205. [https://doi.org/10.6028/NIST.FIPS.205](https://doi.org/10.6028/NIST.FIPS.205) |
| [18] | FS.40 | Official Document FS.40 - 5G Security Guide, July 2024, GSMA |
| [19] | FS.36 | FS.36 – 5G Interconnect Security |
| [20] | RFC 7518 | JSON Web Algorithms (JWA), RFC 7518, May 2015, IETF [https://datatracker.ietf.org/doc/html/rfc7518](https://datatracker.ietf.org/doc/html/rfc7518) |
| [21] | RFC 7519 | JSON Web Token (JWT), RFC 7519, May 2015, IETF [https://datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519) |
| [22] | RFC 4210 | Internet X.509 Public Key Infrastructure Certificate Management Protocol (CMP), RFC 4210, May 2005, IETF [https://datatracker.ietf.org/doc/html/rfc4210](https://datatracker.ietf.org/doc/html/rfc4210) |
| [23] | RFC 9509 | X.509 Certificate Extended Key Usage (EKU) for 5G Network Functions, RFC 9509, Mar 2024, IETF [https://datatracker.ietf.org/doc/html/rfc9509](https://datatracker.ietf.org/doc/html/rfc9509) |
| [24] | TS 23.401 | E-UTRAN access, TS 23.401, 3GPP |
| [25] | TS 23.402 | Architecture enhancements for non-3GPP accesses, TS 23.402, 3GPP |
| [26] | - | ML-KEM Post-Quantum Key Agreement for TLS 1.3, Oct 2024 [https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) |
| [27] | - | Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for JOSE and COSE, Nov 2024 [https://datatracker.ietf.org/doc/html/draft-ietf-jose-pqc-kem-01](https://datatracker.ietf.org/doc/html/draft-ietf-jose-pqc-kem-01) |
| [28] | RFC 8784 | Mixing Preshared Keys in the Internet Key Exchange Protocol Version 2 (IKEv2) for Post-quantum Security, RFC 8784 June 2020, IETF [https://datatracker.ietf.org/doc/rfc8784/](https://datatracker.ietf.org/doc/rfc8784/) |
| [29] | - | Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3, Sep 2024, draft-ietf-tls-ecdhe-mlkem-00 [https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/) |
| [30] | - | Post-quantum Hybrid Key Exchange with ML-KEM in the Internet Key Exchange Protocol Version 2 (IKEv2), Apr 2025, draft-kampanakis-ml-kem-ikev2-09 [https://datatracker.ietf.org/doc/draft-kampanakis-ml-kem-ikev2/](https://datatracker.ietf.org/doc/draft-kampanakis-ml-kem-ikev2/) |
| [31] | RFC 6960 | X.509 Internet Public Key Infrastructure Online Certificate Status Protocol – OCSP, RFC 6960, June 2013, IETF [https://www.rfc-editor.org/info/rfc6960](https://www.rfc-editor.org/info/rfc6960) |

**Table 2 References**

---

## 2 Executive Summary

### 2.1 Migration Plan

A threat actor may use a CRQC when available, to decrypt messages transported between mobile operators when a UE roams. The attacker may be an un-authorized Man-in-the-Middle (MITM) or a compromised entity with access to the roaming intermediaries that can harvest the messages (e.g. IPX providers). Since the messages carry subscriber information (including session keys, profile, call data, CDRs, etc.) data leakage may impact the privacy of subscribers. Internal network function deployment and identifiers may be exposed to attackers, which can be used to perform secondary attacks (e.g. DoS). Networks should protect the roaming interfaces using PQC-compliant key encapsulation mechanisms (e.g. ML-KEM [15]) in order that the interfaces remain protected both from classical as well as from CRQC.

Impersonation, spoofing and tampering attacks on the roaming interface may cause service degradation, stealing of services and even Denial-of-Service. Quantum safe (e.g. ML-DSA [16]) certificates and signature generation and verification capabilities must be built into the roaming entities.

### 2.2 Migration Prioritization

Mitigation against Harvest Now Decrypt Later (HNDL) attacks are more immediate, it is imperative to specify the use of quantum-safe key encapsulation (e.g. ML-KEM) as part of TLS1.3 [2] for protecting the n32 interfaces.

Mutual authentication, authorization and integrity are the building blocks for securing the roaming interfaces. The threat posed by CRQC is not considered immediate and they are not the highest priority.

Building the trust framework for authentication and authorization takes time and therefore immediate work must be carried out for building the trust framework including the Public Key Infrastructure (PKI).

---

## 3 Standards

### 3.1 3GPP Standards

3GPP created technical specifications TS 23.501 [3] and associated specifications that describe a high-level roaming architecture as well as network functions and interfaces for roaming. In TS 33.501 [4], it provides guidance for developing 5G security architecture, including secure roaming architectures and interconnect networks. It also provides security requirements and details on the protocols for securing the n32 interfaces. The n32-c is used for establishing security context between the partners, by means of the Security Edge Protection Proxy (SEPP). The security context is then used for securing the n32-f, the forwarding plane. An NF (e.g. AMF) in one operator network would use the n32-f interface for communicating with an NF (e.g. AUSF) in another operator network.

The security architecture depends on the roaming partners involved, which may vary and may involve the use of intermediaries (e.g. IPX providers). 3GPP describes two security mechanisms for securing the interfaces. The two modes are: Direct TLS and Protocol for N32 Inter-connect Security (PRINS).

### 3.2 GSMA Recommendations & Guidelines

GSMA developed NG.113 5GS roaming guidelines [5], based on the roaming architectures and requirements specified by 3GPP, which detail the technical requirements, architectures, procedures, call flows for the control and user plane, and the security architectures for deployment. It also describes four models of SEPPs, some of which enable a mobile operator to provide the N32-endpoint to an operator or on behalf of another operator. The detailed designs of different security architectures for the deployment models are described to enable different protection schemes.

---

## 4 Roaming Use-cases

### 4.1 5G Roaming Architecture

![Roaming Architecture – Source: TS 23.501 (Local Breakout)]

The SEPP acts as the roaming firewall for 5G roaming interfaces between PLMNs over the N32 interface. The N32 interface is used by the SEPPs to communicate HTTP/2 application-level control plane messages between operators. The N32 interface consists of the N32-c (control), that is used to perform handshake between the SEPPs and the N32-f performs the forwarding of the NF control plane messages using the security parameters that had been established as part of the N32-c handshake procedure. The SEPP performs security actions based on protection profiles configured by the PLMNs and is responsible for enforcing the protection policies that have been agreed upon with the roaming partners. The protection policies may include the confidentiality and integrity protection of information elements exchanged between the PLMNs.

#### 4.1.1 Direct TLS

Direct TLS mode is used when there are no intermediaries (e.g. IPX) between the two operators. The SEPPs perform mutual TLS authentication and negotiate cipher-suites and key management to secure the N32-f messages based on agreed protection policies.

Hop-by-Hop TLS may be used between an operator and one or more intermediate roaming entity (e.g. IPX, roaming hub) and another operator. TLS 1.2 or 1.3 enable secure connections in a hop-by-hop manner, using X.509 certificates for authentication. The intermediaries are privy to the signaling messages carried over N32, since they decrypt and then re-encrypt the messages for each hop.

#### 4.1.2 Protocol for N32 Interconnect Security (PRINS)

A SEPP uses the PRINS mode when there are roaming intermediaries (e.g. IPX) present between the operators. The roaming intermediaries may be allowed to modify the application layer messages based on policies and therefore the SEPPs shall be able to verify the validity and integrity of the modification performed by the intermediaries. Additional transport mechanisms may be used for communications between the SEPP and the roaming intermediaries that includes NDS/IP [7, 8] and TLS VPN.

![PRINS control and forwarding interfaces]

The SEPPs rely on JSON Web Encryption (JWE) [9] for encrypting attributes deemed to be confidential. The JWE Authenticated Encryption with Associated Data (AEAD) algorithm generates JWE encrypted text (ciphertext) and a JWE authentication tag (Message Authentication Code).

The roaming intermediaries use JSON Web Signature (JWS) [10] to provide authentication and integrity for the modifications performed by them.

#### 4.1.3 Inter-PLMN User Plane Security

The Inter-PLMN User Plane Security (IPUPS) function is used to enforce GTP-U security on the N9 interface between UPFs of home and visited PLMNs when using home routed mode [4]. The N9 interface can be protected using NDS/IP, where X.509 certificates [14] are used for mutual authentication between the home UPF (hUPF) and the visiting UPF (vUPF) and uses IKEv2 / IPSec Encapsulated Security Payload (ESP) for integrity, authenticity and confidentiality. In addition to protecting the N9 interface, the IPUPS is required to discard malformed GTP-U packets and forward only those packets that contain a valid Tunnel End-Point Identifier (TEID) that belongs to an active PDU session.

### 4.2 4G Roaming

A Diameter Edge Agent (DEA) is the entry and exit point between mobile network operators’ networks [11]. For 4G roaming, only the relay agent, the proxy agent and the translation agent are relevant. A Diameter Relay Agent (DRA) is responsible for forwarding Diameter messages. A Diameter proxy has the capability to process non-routing related Attribute Value Pairs (AVP) and can inspect the actual contents of the message to perform admission control, policy control etc. A Diameter proxy is application aware and maintains states of downstream peers to enforce resources usage, provide admission control and provisioning.

![4G Diameter Edge Agent Architecture]

The DEA is mainly used for route addressing and forwarding of Diameter signaling, including mobility management, charging policy, and charging information about roaming users, for control / signaling plane messages transmitted over the S6a, S6d, and S9 interfaces.

![4G Diameter network entity interactions]

The Diameter messages exchanged between service providers do not provide integrity or confidentiality protection by default. Therefore IPSec / TLS, specified as part of NDS/IP is used to provide hop-by-hop protection (no end-to-end protection is provided).

There is no 3GPP requirement to protect the user plane traffic over the S8 interface between a SGW in one operator network to a PGW in another roaming partner network in a home-routed scenario. The traffic therefore is only expected to be protected at the application layer without any network or transport layer protections and therefore considered out-of-scope here.

### 4.3 VoNR / VoLTE Roaming

VoNR [13] and VoLTE [12] roaming are enabled through the IP Multimedia Subsystem (IMS), where SIP is used for signaling and RTP/SRTP for media transport. In typical deployments, the S8 Home-Routed (S8HR) architecture is used, anchoring both signaling and media in the Home PLMN (HPLMN) via the IPX interconnect. Control plane signaling traverses interfaces such as S6a/Nh between the Visited PLMN (VPLMN) and HPLMN, while the user plane is established through the S8 or N9 interface, depending on whether the UE is in LTE or 5G SA/NSA. Dedicated Quanity of Service (QoS) bearers (e.g., QCI 1 for voice, QCI 5 for signaling) are used for voice sessions.

Quantum-specific risks in VoNR/VoLTE roaming:

- The susceptibility of signaling and media traffic to Harvest Now, Decrypt Later (HNDL) attacks, especially when key exchanges use classical algorithms such as ECDHE or RSA.
- Authentication vectors transmitted over Diameter (S6a) or HTTP/2 interfaces may be targeted by future quantum adversaries, compromising user privacy and allowing impersonation.
- To mitigate these risks, PQC-based key encapsulation mechanisms such as ML-KEM should be integrated into TLS sessions securing SIP and Diameter transport. Hybrid key exchange may provide a transitional safeguard. Symmetric encryption algorithms used for SRTP and user plane protection should use quantum-safe algorithms such as AES.
- During VoLTE or VoNR sessions, IPSEC sessions are established to ensure confidentiality and integrity protection. The IMS AKA procedure is used during these IPSEC sessions. The IMS AKA procedure relies on keys stored on the SIM card and the AuC/AUSF on the HSS/UDM. During the establishment of the IMS IPSEC tunnel, quantum-secured algorithms should be employed, and support for multiple algorithm options should be provided.
- In VoLTE/VoNR for key exchange, DH (Diffie-Hellman) or ECDH (Elliptic Curve Diffie-Hellman) algorithms are currently used. These should be replaced with ML-KEM or HQC (Hamming Quasi-Cyclic) once standardsed.
- For encryption, 3DES or AES algorithms are used in VoLTE/VoNR, with AES being highly recommended.
- For integrity control and signature, HMAC or SHA algorithms can be utilized. In the post-quantum era, ML-DSA (FIPS 204) [16] or SLH-DSA (FIPS 205) [17] algorithms should be used. Considering the computational power requirements on the terminal side, ML-DSA is highly recommended. FN-DSA may be added to the list once standardised. Other DSA algorithms necessitate larger key sizes, which could be inefficient for mobile terminals today.

A summary table is given below.

**Table 3 Proposed Cryptographic Suites for Post Quantum Security**

---

## 5 Scope

The roaming interfaces carry subscriber profile information as well as subscriber authentication data and session keys. The roaming interfaces are protected using TLS 1.3 and / or IPSec based on mutual authentication using X.509 certificates.

The N32 interface uses X.509 certificates for mutual authentication and uses JWS for integrity and authentication of the JSON payload added by the intermediaries in the PRINS mode. Attacks by a CRQC against integrity and authentication are not considered to be an imminent threat, when a CRQC becomes available, it could launch tampering as well as impersonation attacks between roaming partners.

### 5.1 Sensitive Data Discovery

#### 5.1.1 5G Roaming

**Data at Rest**
- Subscriber data including SUPI, and other subscriber data including location info
- Roaming agreements and policies associated with roaming partners
- Private Key associated with a h