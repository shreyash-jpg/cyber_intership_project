from scapy.all import sniff, IP, TCP, UDP


def packet_callback(packet):
    # Check whether the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        # Determine protocol name
        protocol_name = "Unknown"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"

        print("\n[+] New Packet Captured:")
        print(f"    Source IP:      {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        print(f"    Protocol:       {protocol_name} ({proto})")

        # Print a truncated payload preview if available
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            if packet.haslayer('Raw'):
                payload = packet['Raw'].load
                print(f"    Payload Data:   {payload[:50]}... (truncated)")


def main():
    print("--- Network Packet Analyzer (Sniffer) ---")
    print("[*] Packet capturing has started... (press Ctrl+C to stop)")
    print("[!] Make sure you run the script with Administrator privileges.\n")

    try:
        # sniff monitors network traffic until you stop it manually
        sniff(prn=packet_callback, store=False, count=0)
    except KeyboardInterrupt:
        print("\n[-] Sniffer stopped.")
    except PermissionError:
        print("\n[ERROR] Permission denied! Please run this script as Administrator/Root.")


if __name__ == "__main__":
    main()

