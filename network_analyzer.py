
from scapy.all import rdpcap, IP, TCP, UDP

# Load both packet captures
tcp_packets = rdpcap("tcp_capture.pcapng")
udp_packets = rdpcap("udp_capture.pcapng")

# Count TCP and UDP packets
tcp_count = sum(
    1 for packet in tcp_packets
    if packet.haslayer(IP) and packet.haslayer(TCP)
)

udp_count = sum(
    1 for packet in udp_packets
    if packet.haslayer(IP) and packet.haslayer(UDP)
)

# Display analysis
print("===============================")
print("     NETWORK TRAFFIC ANALYZER")
print("===============================")

print("\nTCP ANALYSIS")
print("-------------------------------")
print("Total TCP capture packets:", len(tcp_packets))
print("TCP packets identified:", tcp_count)

print("\nUDP ANALYSIS")
print("-------------------------------")
print("Total UDP capture packets:", len(udp_packets))
print("UDP packets identified:", udp_count)

# Display UDP packet details
print("\nUDP PACKET DETAILS")
print("-------------------------------")

for number, packet in enumerate(udp_packets, start=1):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        ip = packet[IP]
        udp = packet[UDP]

        print("\nPacket:", number)
        print("Source IP:", ip.src)
        print("Destination IP:", ip.dst)
        print("Source Port:", udp.sport)
        print("Destination Port:", udp.dport)
# Combined Protocol Statistics
print("\nCOMBINED PROTOCOL STATISTICS")
print("-------------------------------")

total_captured = len(tcp_packets) + len(udp_packets)

print("Total packets from both captures:", total_captured)
print("TCP packets identified:", tcp_count)
print("UDP packets identified:", udp_count)

print("\nProtocol Distribution")
print("-------------------------------")

tcp_percentage = (tcp_count / total_captured) * 100
udp_percentage = (udp_count / total_captured) * 100

print("TCP:", round(tcp_percentage, 2), "%")
print("UDP:", round(udp_percentage, 2), "%")
