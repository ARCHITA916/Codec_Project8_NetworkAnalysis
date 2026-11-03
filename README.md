# Network Traffic Analysis

## Project Overview

This project focuses on capturing, observing, and analysing network traffic using **Wireshark** and **Python Scapy** in Kali Linux.

The purpose of this project is to understand how different network protocols communicate and how packet information can be examined during network analysis.

## Objectives

- Capture and analyse network packets using Wireshark.
- Observe ICMP communication using ping.
- Examine DNS queries and responses.
- Analyse TCP packets and connection details.
- Understand packet headers, IP addresses, ports, and TCP flags.
- Use Python Scapy to read and analyse a saved packet capture.

## Tools and Technologies

- **Operating System:** Kali Linux
- **Packet Analysis Tool:** Wireshark
- **Programming Language:** Python 3
- **Python Library:** Scapy
- **Network Interface:** eth0

## Protocols Analysed

### 1. ICMP
Used the ping command to generate ICMP traffic and examined ICMP request and reply packets in Wireshark.

### 2. DNS
Used `nslookup` to generate DNS traffic and inspected DNS queries and responses, including their packet details.

### 3. TCP
Generated TCP traffic using an HTTPS request and examined TCP packets, SYN flags, connection details, and a TCP stream in Wireshark.

## Python Packet Analyzer

A Python script named `network_analyzer.py` was developed using Scapy.

The script reads a saved packet capture and extracts information from IPv4 and TCP packets, including:

- Source IP address
- Destination IP address
- Source port
- Destination port
- TCP flags
- Total packet count
- TCP packet count

## Project Structure

```text
project8_NetworkAnalysis/
│
├── network_analyzer.py
├── tcp_analysis.txt
├── README.md
├── .gitignore
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
    └── 10_Network_Analysis.png
```

**Note:** The original PCAPNG capture file is excluded from this repository for privacy. To run the Python analyzer, provide your own capture file named `tcp_capture.pcapng` in the project directory.

## Installation and Usage

### 1. Install Scapy

```bash
pip install scapy
```

### 2. Provide a Packet Capture

Place your own Wireshark capture file named:

```text
tcp_capture.pcapng
```

in the project directory.

### 3. Run the Python Analyzer

```bash
python3 network_analyzer.py
```

### 4. Save the Analysis Output

```bash
python3 network_analyzer.py > tcp_analysis.txt
```

## Screenshots and Documentation

The `screenshots` folder contains evidence of the practical work, including:

- Wireshark interface and packet capture
- ICMP packet analysis
- DNS lookup and packet analysis
- TCP SYN packet analysis
- TCP stream inspection
- TCP packet details
- Overall network analysis

The `tcp_analysis.txt` file contains a summary of the packet analysis performed using Python.

## Learning Outcomes

Through this project, I gained practical experience in:

- Understanding basic network traffic.
- Identifying ICMP, DNS, and TCP packets.
- Using Wireshark display filters.
- Examining packet headers and protocol details.
- Reading packet captures using Python Scapy.
- Documenting network analysis results.

## Project Limitations

This project demonstrates basic packet capture and protocol analysis. It does not implement automated malware detection, intrusion detection, or advanced anomaly detection.

## Conclusion

This project provided practical exposure to network traffic analysis using Wireshark and Python Scapy. It helped strengthen my understanding of network protocols, packet structures, and basic traffic inspection techniques.
