# Post-Quantum Cryptography for 5G Roaming

**Organization:** GSMA  
**Report Title:** Post-Quantum-Cryptography-for-5G-Roaming  
**Year:** 2025  
**Version:** 1.0  
**Date:** 26 June 2025  
**Security Classification:** Non-confidential

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
  - [VoNR / VoLTE Roaming](#vonr--volte-roaming)
- [5 Scope](#5-scope)
  - [5.1 Sensitive Data Discovery](#51-sensitive-data-discovery)
    - [5.1.1 5G Roaming](#511-5g-roaming)
    - [5.1.2 4G Roaming](#512-4g-roaming)
  - [5.2 Cryptographic Inventory](#52-cryptographic-inventory)
  - [5.3 Threats and Attacks against Roaming Interfaces](#53-threats-and-attacks-against-roaming-interfaces)
- [6 Migration Strategy Analysis and Dependencies](#6-migration-strategy-analysis-and-dependencies)
  - [6.1 Standards](#61-standards)
    - [6.1.1 Public Key Infrastructure & Certificate Management](#611-public-key-infrastructure--certificate-management)
    - [6.1.2 TLS 1.3](#612-tls-13)
    - [6.1.3 IKEv2 / IPSec](#613-ikev2--ipsec)
    - [6.1.4 Hybrid Cryptography](#614-hybrid-cryptography)
  - [6.2 Regulations & Migration Strategy with Roaming Partners](#62-regulations--migration-strategy-with-roaming-partners)
    - [6.2.1 National Guidelines](#621-national-guidelines-regulation-intra-plmn-and-inter-plmn)
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

The GSMA PQTN Task Force has published a series of documents about the impact of Post Quantum Cryptography (PQC) on telecoms. This document is an extension of PQ.03 v2 - Quantum Safe User Cases and Migration [1] and addresses 4G and 5G roaming.

### 1.1 Overview
3GPP and GSMA have developed a standardised roaming architecture, specifications and requirements for use-cases where a UE roams from its Home PLMN (HPLMN) to a Visited PLMN (VPLMN) and vice-versa. This document provides an overview of threats, impacts and mitigation mechanisms against a Cryptographically Relevant Quantum Computer (CRQC) targeting the roaming architecture and its interfaces.

### 1.2 Scope
This document covers mechanisms that may be employed to protect UEs and operator networks from a CRQC when a UE roams between HPLMN and VPLMN. The roaming architecture considers scenarios where a Security Edge Protection Proxy (SEPP) is responsible for protecting the operator’s core network from attacks targeting the inter-connect interfaces (N32-c, N32-f). The interfaces may be secured using:
1. Direct TLS between SEPPs
2. PRotocol for N32 INterconnect Security (PRINS)

Diameter inter-connect security is included in the analysis for 4G/5G roaming interworking.

### 1.3 Abbreviations
*(See Table 1 in original document for full list of terms including 3GPP, CRQC, SEPP, PRINS, etc.)*

### 1.4 References
*(See Table 2 in original document for full list of references including RFCs, FIPS standards, and 3GPP specifications.)*

---

## 2 Executive Summary

### 2.1 Migration Plan
A threat actor may use a CRQC to decrypt messages transported between mobile operators (Harvest Now, Decrypt Later - HNDL). Networks should protect roaming interfaces using PQC-compliant key encapsulation mechanisms (e.g., ML-KEM [15]). Impersonation and tampering attacks must be mitigated using quantum-safe certificates and signatures (e.g., ML-DSA [16]).

### 2.2 Migration Prioritization
Mitigation against HNDL attacks is the highest priority. Immediate work must be carried out to build the trust framework, including the Public Key Infrastructure (PKI).

---

## 3 Standards

### 3.1 3GPP Standards
3GPP TS 33.501 [4] provides guidance for 5G security architecture, including secure roaming and N32 interface protection.

### 3.2 GSMA Recommendations & Guidelines
GSMA NG.113 [5] details technical requirements, architectures, and procedures for 5G roaming, including SEPP deployment models.

---

## 4 Roaming Use-cases

### 4.1 5G Roaming Architecture
![Roaming Architecture – Source: TS 23.501 (Local Breakout)]

#### 4.1.1 Direct TLS
Used when no intermediaries exist. SEPPs perform mutual TLS authentication and negotiate cipher-suites.

#### 4.1.2 Protocol for N32 Interconnect Security (PRINS)
Used when roaming intermediaries (e.g., IPX) are present. SEPPs verify the validity and integrity of modifications performed by intermediaries.
![PRINS control and forwarding interfaces]

#### 4.1.3 Inter-PLMN User Plane Security
The IPUPS function enforces GTP-U security on the N9 interface using NDS/IP and IKEv2/IPSec.

### 4.2 4G Roaming
Diameter Edge Agents (DEA) serve as entry/exit points. Signaling is protected via IPSec/TLS as part of NDS/IP.
![4G Diameter Edge Agent Architecture]
![4G Diameter network entity interactions]

### VoNR / VoLTE Roaming
VoNR [13] and VoLTE [12] roaming utilize the IMS. Risks include HNDL attacks on signaling and media. PQC-based key encapsulation (ML-KEM) and quantum-safe signatures (ML-DSA) are recommended.

---

## 5 Scope

### 5.1 Sensitive Data Discovery

#### 5.1.1 5G Roaming
- **Data at Rest:** Subscriber data (SUPI), roaming agreements, private keys, certificate chains, session keys.
- **Data in Transit:** UEID, location info, key material, authentication material, authorization tokens.
![5G Control Plane Attributes that are to be Protected for Confidentiality]

#### 5.1.2 4G Roaming
- **Data at Rest:** Private keys, certificate chains, session keys.
- **Data in Transit:** Subscriber data, authentication material, location info.

### 5.2 Cryptographic Inventory
SEPPs utilize mutual TLS 1.3. Supported suites include ECDHE_ECDSA_with_AES_128_GCM_SHA256 and various RSA/ECDSA algorithms.

### 5.3 Threats and Attacks against Roaming Interfaces
- **HNDL Attacks:** Susceptibility of N32-c/N32-f interfaces due to reliance on ECDHE/DHE.
- **Spoofing/Impersonation:** Potential for CRQC to break ECDSA and compromise SEPP identities or spoof JWTs.

---

## 6 Migration Strategy Analysis and Dependencies

### 6.1 Standards
Migration involves transitioning to quantum-safe key encapsulation (ML-KEM) and digital signatures (ML-DSA).

#### 6.1.1 Public Key Infrastructure & Certificate Management
Requires migration to quantum-safe root/intermediate CAs and support for larger signature sizes in certificate profiles.

#### 6.1.2 TLS 1.3
IETF is developing specifications for TLS 1.3 with ML-KEM [26].

#### 6.1.3 IKEv2 / IPSec
RFC 8784 [28] allows for pre-shared keys to resist HNDL attacks.

#### 6.1.4 Hybrid Cryptography
Combining ML-KEM with ECDHE/DHE schemes is the recommended transitional approach [29, 30].

### 6.2 Regulations & Migration Strategy with Roaming Partners
- **Operators:** Phased migration based on risk profiles.
- **3rd-parties:** IPX providers must prioritize ML-KEM for key establishment.
- **Performance:** Minimal impact expected for TLS 1.3 handshakes; larger impact on PRINS/JWS operations.

#### 6.2.7 Gantt Chart for PQC Migration
![Gantt Chart for PQC Migration for Roaming]

#### 6.2.8 PQC Migration Process Description
1. Prioritize ML-KEM in TLS 1.3 for N32 interfaces.
2. Update JWS objects with ML-DSA.
3. Implement hybrid key agreement for JWE.
4. Manage hybrid certificates (traditional + PQC).

---

## A.1 Document History
| Version | Date | Brief Description of Change | Approval Authority |
| :--- | :--- | :--- | :--- |
| 1.0 | 26 June 2025 | New document | Technology Group |

## A.2 Other Information
- **Document Owner:** PQTN
- **Editor / Company:** Vinod Choyi, Verizon