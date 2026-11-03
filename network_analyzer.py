
from scapy.all import rdpcap, IP, TCP, UDP

# Load both packet captures
tcp_packets = rdpcap("tcp_capture.pcapng")
udp_packets = rdpcap("udp_capture.pcapng")

# Combine packets from both separate captures
all_packets = list(tcp_packets) + list(udp_packets)

# Count protocols across all captured packets
tcp_count = sum(1 for packet in all_packets if packet.haslayer(TCP))

udp_count = sum(
    1 for packet in all_packets
    if packet.haslayer(UDP) and not packet.haslayer(TCP)
)

other_count = len(all_packets) - tcp_count - udp_count

total_captured = len(all_packets)

# Display analysis
print("================================")
print("      NETWORK TRAFFIC ANALYZER")
print("================================")

print("\nCAPTURE SUMMARY")
print("--------------------------------")
print("Packets in TCP capture:", len(tcp_packets))
print("Packets in UDP capture:", len(udp_packets))
print("Total packets analysed:", total_captured)

print("\nPROTOCOL STATISTICS")
print("--------------------------------")
print("TCP packets:", tcp_count)
print("UDP packets:", udp_count)
print("Other packets:", other_count)

if total_captured > 0:
    print("\nPROTOCOL DISTRIBUTION")
    print("--------------------------------")
    print("TCP:", round(tcp_count / total_captured * 100, 2), "%")
    print("UDP:", round(udp_count / total_captured * 100, 2), "%")
    print("Other:", round(other_count / total_captured * 100, 2), "%")

# Display UDP packet details from both captures
print("\nUDP PACKET DETAILS")
print("--------------------------------")

for number, packet in enumerate(all_packets, start=1):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        ip = packet[IP]
        udp = packet[UDP]

        print("\nPacket:", number)
        print("Source IP:", ip.src)
        print("Destination IP:", ip.dst)
        print("Source Port:", udp.sport)
        print("Destination Port:", udp.dport)

print("\nAnalysis completed.")
