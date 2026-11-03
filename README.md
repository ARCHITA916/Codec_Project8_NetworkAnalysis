# Network Traffic Analysis Using Wireshark and Python

## Project Overview

This project focuses on capturing, monitoring, and analysing network traffic using **Wireshark, Kali Linux, Python, and Scapy**.

The main objective is to understand how different network protocols communicate, examine packet details, and generate basic protocol statistics from saved packet captures.

The analysis covers ICMP, DNS, TCP, UDP, and HTTPS/TLS traffic.

## Objectives

- Capture and analyse network packets using Wireshark.
- Understand common network protocols.
- Examine source and destination IP addresses.
- Identify TCP and UDP communication.
- Analyse DNS queries and responses.
- Observe TCP connection establishment.
- Examine HTTPS and TLS handshake information.
- Use Python and Scapy to analyse saved packet captures.
- Generate basic protocol statistics.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Kali Linux | Operating system for the practical work |
| Wireshark | Network packet capture and analysis |
| Python | Packet analysis and statistics |
| Scapy | Python packet-processing library |
| Terminal | Network commands and testing |
| GitHub | Project documentation and version control |

## Protocols Analysed

### 1. ICMP (Internet Control Message Protocol)

ICMP traffic was generated using the `ping` command.

**Purpose:**
- Test network connectivity.
- Observe Echo Request and Echo Reply packets.
- Examine source and destination IP addresses.

**Wireshark filter:**
```text
icmp
```

### 2. DNS (Domain Name System)

DNS traffic was generated using `nslookup`.

**Purpose:**
- Observe DNS queries and responses.
- Understand how domain names are resolved into IP addresses.
- Examine DNS request and response details.

**Wireshark filter:**
```text
dns
```

### 3. TCP (Transmission Control Protocol)

TCP traffic was generated using an HTTPS request.

**Purpose:**
- Examine TCP packets.
- Observe SYN and SYN-ACK flags.
- Understand TCP connection establishment.
- Inspect TCP stream information.

**Wireshark filters:**
```text
tcp
tcp.flags.syn == 1
tcp.stream eq 0
```

### 4. UDP (User Datagram Protocol)

UDP traffic was generated using a traceroute command.

**Purpose:**
- Observe UDP packets.
- Examine source and destination ports.
- Identify DNS and traceroute-related UDP traffic.

**Wireshark filter:**
```text
udp && !dns
```

### 5. HTTPS and TLS Analysis

HTTPS traffic was generated using `curl`.

**Purpose:**
- Observe TLS handshake packets.
- Identify Client Hello and Server Hello messages.
- Examine TLS 1.3 communication.
- Observe encrypted Application Data.

**Wireshark filter:**
```text
tls
```

Note: The analysis observes TLS handshake information. Encrypted application content was not decrypted or inspected.

## Python Network Analyzer

A Python script named `network_analyzer.py` was developed using Scapy.

The script:
- Reads saved TCP and UDP packet captures.
- Identifies TCP and UDP packets.
- Counts identified packets.
- Displays UDP packet details.
- Generates basic protocol statistics.

The packet captures used by the script are:
- `tcp_capture.pcapng`
- `udp_capture.pcapng`

**Important:** These are two separate captures collected during different practical tests. Their statistics should not be interpreted as one continuous network capture.

## Project Structure

```text
Codec_Project8_NetworkAnalysis/
│
├── README.md
├── .gitignore
├── network_analyzer.py
├── tcp_analysis.txt
│
└── screenshots/
    ├── 01_interface_Installation.png
    ├── 02_ICMP_Packet_Analysis.png
    ├── 03_ICMP_Packet_details.png
    ├── 04_DNS_Lookup_Terminal.png
    ├── 05_DNS_Packet_Analysis.png
    ├── 06_DNS_Response_Details.png
    ├── 07_TCP_SYN_Analysis.png
    ├── 08_TCP_Stream.png
    ├── 09_TCP_Packet_Details.png
    ├── 10_Network_Analysis.png
    ├── 11_UDP_Packet_Analysis.png
    └── 12_TLS_Handshake_Analysis.png
```

## Screenshots and Practical Evidence

The screenshots folder contains practical evidence of:

1. Wireshark interface and network capture setup.
2. ICMP packet analysis.
3. ICMP packet details.
4. DNS lookup using the terminal.
5. DNS packet analysis.
6. DNS response details.
7. TCP SYN and SYN-ACK analysis.
8. TCP stream inspection.
9. TCP packet details.
10. General network traffic analysis.
11. UDP packet analysis.
12. TLS handshake analysis.

## How to Run the Python Analyzer

### Requirements

- Python 3
- Scapy

Install Scapy:

```bash
pip install scapy
```

Place both packet capture files in the same directory as `network_analyzer.py`:

```text
tcp_capture.pcapng
udp_capture.pcapng
```

Run the script:

```bash
python3 network_analyzer.py
```

The script displays packet counts and basic protocol information.

**Note:** The raw packet capture files are excluded from this public repository. They must be collected separately or placed in the project directory before running the analyzer.

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Understanding network packet structures.
- Using Wireshark for packet capture and inspection.
- Identifying ICMP, DNS, TCP, UDP, and TLS traffic.
- Understanding TCP connection establishment.
- Observing DNS resolution.
- Examining encrypted HTTPS communication at the TLS handshake level.
- Using Python and Scapy for basic packet analysis.
- Documenting practical cybersecurity work.
- Using Git and GitHub for project management.

## Limitations

- This project focuses on basic network traffic analysis.
- It does not implement a complete Intrusion Detection System (IDS).
- It does not perform malware detection.
- It does not provide advanced anomaly detection.
- Encrypted HTTPS application data is not decrypted.
- The analysis is based on selected practical packet captures.

## Conclusion

This project provided practical exposure to network traffic capture and analysis using Wireshark and Python.

By analysing different network protocols and developing a basic packet analyzer using Scapy, I improved my understanding of network communication, packet inspection, and fundamental cybersecurity analysis techniques.

---

**Project:** Network Traffic Analysis  
**Internship:** Codec Technologies Cyber Security Internship  
**Tools:** Kali Linux, Wireshark, Python, Scapy  
**Repository:** Codec_Project8_NetworkAnalysis
