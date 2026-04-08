# Unit-42-IoT-Threat-Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [01 IoT Security Landscape](#01-iot-security-landscape)
  - [Organizations Lack the Tools to Discover and Secure IoT](#organizations-lack-the-tools-to-discover-and-secure-iot)
  - [Enterprises Sit on a Time Bomb](#enterprises-sit-on-a-time-bomb)
  - [Healthcare Is in Critical Shape](#healthcare-is-in-critical-shape)
  - [Basic Network Segmentation Best Practices Aren’t Followed](#basic-network-segmentation-best-practices-arent-followed)
  - [Case Study: Conficker in Healthcare](#case-study-conficker-in-healthcare)
- [02 Top IoT Threats](#02-top-iot-threats)
  - [Exploits, Password Attacks, and IoT Worms Top the Chart](#exploits-password-attacks-and-iot-worms-top-the-chart)
  - [Unpatched Devices and Legacy Protocols: Means of Lateral Movement](#unpatched-devices-legacy-protocols-means-of-lateral-movement)
  - [Threats Evolving to Specifically Target IoT Environments](#threats-evolving-to-specifically-target-iot-environments)
  - [Case Study: Cryptojacking in the Wild](#case-study-cryptojacking-in-the-wild)
- [03 Conclusion and Recommendations](#03-conclusion-and-recommendations)
  - [Take Steps to Reduce Risk](#take-steps-to-reduce-risk)
  - [Perfect Your IoT Strategy](#perfect-your-iot-strategy)
- [About](#about)

---

## Executive Summary

According to a 2019 Gartner report, "By the end of 2019, 4.8 billion [IoT] endpoints are expected to be in use, up 21.5% from 2018." While the internet of things (IoT) opens the door for innovative new approaches and services in all industries, it also presents new cybersecurity risks. To evaluate the current state of the IoT threat landscape, the Unit 42 threat intelligence team analyzed security incidents throughout 2018 and 2019 with the Palo Alto Networks IoT security product, Zingbox®, spanning 1.2 million IoT devices in thousands of physical locations across enterprise IT and healthcare organizations in the United States. We found that the general security posture of IoT devices is declining, leaving organizations vulnerable to new IoT-targeted malware as well as older attack techniques that IT teams have long forgotten. This report details the scope of the IoT threat landscape, which IoT devices are most susceptible, top IoT threats, and actionable next steps to immediately reduce IoT risk.

- **IoT devices are encrypted and unsecured**: 98% of all IoT device traffic is unencrypted, exposing personal and confidential data on the network. Attackers who’ve successfully bypassed the first line of defense (most frequently via phishing attacks) and established command and control (C2) are able to listen to unencrypted network traffic, collect personal or confidential information and then exploit that data for profit on the dark web. 57% of IoT devices are vulnerable to medium- or high-severity attacks, making IoT the low-hanging fruit for attackers.
- **IoMT devices are running outdated software**: 83% of medical imaging devices run on unsupported operating systems, which is a 56% jump from 2018, as a result of the Windows® 7 operating system reaching its end of life. This general decline in security posture opens the door for new attacks, such as cryptojacking (which increased from 0% in 2017 to 5% in 2019) and brings back long-forgotten attacks such as Conficker.
- **Healthcare organizations are displaying poor network security hygiene**: 72% of healthcare VLANs mix IoT and IT assets, allowing malware to spread from users’ computers to vulnerable IoT devices on the same network.
- **IoT-focused cyberattacks are targeting legacy protocols**: There is an evolution of threats targeting IoT devices using new techniques, such as peer-to-peer C2 communications and worm-like features for self-propagation.

---

## 01 IoT Security Landscape

### Organizations Lack the Tools to Discover and Secure IoT
Enterprises face a significant challenge in not knowing the risk exposed by IoT devices and applications. The main reasons are lack of device discovery and inventory. 

- **IT’s lack of IoT visibility**: An outdated, static inventory of IoT assets is far from effective security management. Only by identifying the specific type of device can an organization accurately plan its network access requirements.
- **Existing security systems don’t support IoT**: Endpoint protection systems are designed for computers, tablets, and phones with the ability to run agents, but IoT devices often run custom or outdated operating systems without such ability.
- **Organizational and human resource challenges between OT and IT**: Most organizations manage information technology (IT) and operational technology (OT) as separate teams with separate processes and tools.

### Enterprises Sit on a Time Bomb
![Chart showing security issues by device type: IP Phone, Printer, Intercom, Camera, etc.]

- **IP phones**: Account for 44% of all enterprise IoT devices but only 5% of all security issues.
- **Security cameras**: Make up only 5% of enterprise IoT devices, but they account for 33% of all security issues.
- **Printers**: Account for 18% of IoT devices and 24% of security incidents.

### Healthcare Is in Critical Shape
A 2019 Gartner survey found that 40% of healthcare CIOs plan to spend new or additional funds on cybersecurity tools in 2020. Medical devices are in a critical state due to long lifecycles and outdated operating systems.

![Chart showing medical devices and security issues]
![Chart showing smart device security regulations]

### Basic Network Segmentation Best Practices Aren’t Followed
The simplest IoT risk remediation practice is network segmentation. Despite this, only 3% of all segmented networks or virtual local area networks (VLANs) in the healthcare organizations we studied contained strictly medical IoT devices.

- **Mixed networks**: 72% of healthcare VLANs house a mix of medical IoT devices, generic enterprise IoT devices, and IT devices.

### Case Study: Conficker in Healthcare
Zingbox alerted a hospital of Conficker traffic detected in its network. The offending device was a mammography machine. Despite re-imaging, the devices were reinfected because the approved images were outdated and did not include the latest security patches. This highlights the lack of real-time visibility into IoT device behavior.

---

## 02 Top IoT Threats

### Exploits, Password Attacks, and IoT Worms Top the Chart
![Chart showing breakdown of top IoT threats: Exploits (41%), User Practice (26%), Password (13%), etc.]

- **No. 1: Exploits targeting device vulnerabilities**: Devices are often used as stepping stones in lateral movement.
- **No. 2: Password attacks**: Default, manufacturer-set passwords and poor password security practices continue to fuel attacks.
- **No. 3: IoT worms**: We’re witnessing a shift away from botnets conducting DDoS attacks to malware spreading across the network via worm-like features.

### Unpatched Devices and Legacy Protocols: Means of Lateral Movement
IoT exploits represent a unique challenge because they often involve legacy OS that don’t offer security updates anymore. We found that 83% of medical imaging devices run end-of-life, unsupported OS. Furthermore, aged OT protocols like DICOM are being targeted to disrupt critical business functions.

### Threats Evolving to Specifically Target IoT Environments
- **Peer-to-peer features**: Threats are evolving to use decentralized peer-to-peer C2 communications, allowing swarms to operate even without an internet connection.
- **Fight for the host**: Malware is attempting to remove other malware to occupy the victim IoT device exclusively to address hardware resource constraints.

### Case Study: Cryptojacking in the Wild
Cryptojacking malware hides on a device and uses the machine’s resources to “mine” cryptocurrency. Zingbox alerted a customer to cryptomining code transfer between an IT storage device and an OT device. Continuous network traffic monitoring enabled the IT staff to identify the offending process and remove it.

---

## 03 Conclusion and Recommendations

### Take Steps to Reduce Risk
1. **Know your risk**: Discover IoT devices on the network using intelligent scanning.
2. **Patch printers and other easily patchable devices**: Investigate the security posture of the most abundant devices.
3. **Segment IoT devices across VLANs**: Implement network segments leveraging VLAN configurations and firewall policies.
4. **Enable active monitoring**: Use machine learning and cloud architecture to identify anomalies in real time.

### Perfect Your IoT Strategy
- **Best Practice 1: Think holistically, orchestrate the entire IoT lifecycle**: Follow the lifecycle: Identify, Onboard, Secure, Optimize, Manage, and Retire.
- **Best Practice 2: Expand security to all IoT devices through product integrations**: Integrate IoT security intelligence with existing systems like SIEM, SOAR, and NGFW.

---

## About
- **Palo Alto Networks**: Acquired Zingbox in September 2019 to provide a revolutionary approach to IoT security.
- **Unit 42**: The global threat intelligence team at Palo Alto Networks, providing in-depth research on cyberthreats.
- **Methodology**: This report is based on a two-year analysis of 1.2 million IoT devices and 73.2 billion network sessions across 2018 and 2019.