from scapy.all import rdpcap, IP, TCP

#load the saved packet capture
packets = rdpcap("tcp_capture.pcapng")

#store TCP packets
tcp_packets = []

for packet in packets:
    if packet.haslayer(IP) and packet.haslayer(TCP):
        tcp_packets.append(packet)

# Display analysis
print("===============================")
print("     TCP NETWORK ANALYZER")
print("===============================")

print("Total packets captured:", len(packets))
print("Total TCP packets:", len(tcp_packets))

print("\nTCP PACKET DETAILS")
print("-------------------------------")

for number, packet in enumerate(tcp_packets, start=1):
    ip = packet[IP]
    tcp = packet[TCP]

    print("\nPacket:", number)
    print("Source IP:", ip.src)
    print("Destination IP:", ip.dst)
    print("Source Port:", tcp.sport)
    print("Destination Port:", tcp.dport)
    print("TCP Flags:", tcp.flags)

