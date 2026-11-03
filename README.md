# Network Traffic Analysis Using Python and Scapy

## Project Overview

This project demonstrates basic network traffic analysis using Wireshark, Python, and Scapy in Kali Linux.

A network packet capture was created and examined to understand ICMP, DNS, and TCP traffic. A Python-based analyzer was developed to read the saved packet capture and extract information from TCP packets.

## Project Objectives

- Capture and examine network traffic.
- Identify ICMP, DNS, and TCP protocols.
- Understand TCP communication and connection establishment.
- Extract source and destination IP addresses.
- Identify source and destination port numbers.
- Examine TCP flags.
- Generate a text-based packet analysis report.

## Tools and Technologies

- Kali Linux
- Wireshark
- Python 3
- Scapy
- Nano Text Editor

## Project Structure

```text
project8_NetworkAnalysis/
│
├── network_analyzer.py
├── tcp_capture.pcapng
├── tcp_analysis.txt
├── README.md
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
    └── 10_Network Analysis.png
```

## Python Analyzer Features

The Python program uses Scapy to:

1. Read a saved PCAPNG file.
2. Identify packets containing IPv4 and TCP layers.
3. Extract source and destination IP addresses.
4. Extract source and destination ports.
5. Display TCP flags for each identified packet.

## Analysis Results

The captured file contained:

- Total packets captured: **40**
- Total TCP packets identified: **35**

The analysis also showed TCP communication over destination port 443.

## How to Run

Install Python 3 and Scapy, then open the project directory.

Run:

```bash
python3 network_analyzer.py
```

To save the output:

```bash
python3 network_analyzer.py > tcp_analysis.txt
```

## Learning Outcomes

- Understanding basic network packet analysis.
- Identifying common network protocols.
- Understanding TCP flags and connection establishment.
- Learning to use Wireshark for packet inspection.
- Using Python and Scapy to examine packet captures.

## Author

B.Sc. Computer Science with Cyber Security Student
