from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check karein agar packet me IP layer hai
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        # Protocol ka naam pata karna
        protocol_name = "Unknown"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"
            
        print(f"\n[+] New Packet Captured:")
        print(f"    Source IP:      {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        print(f"    Protocol:       {protocol_name} ({proto})")
        
        # Agar packet me raw payload/data hai toh use print karein
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            if packet.haslayer('Raw'):
                payload = packet['Raw'].load
                print(f"    Payload Data:   {payload[:50]}... (truncated)")

def main():
    print("--- Network Packet Analyzer (Sniffer) ---")
    print("[*] Packets capture hona shuru ho gaye hain... (Ctrl+C dabayein rokne ke liye)")
    print("[!] Make sure aapne terminal ko 'Admin' mode me chalaya hai.\n")
    
    try:
        # sniff function network traffic ko monitor karta hai
        # count=0 ka matlab yeh chalta rahega jab tak aap manually stop nahi karte
        sniff(prn=packet_callback, store=False, count=0)
    except KeyboardInterrupt:
        print("\n[-] Sniffer stopped.")
    except PermissionError:
        print("\n[ERROR] Permission Denied! Please run this script as Administrator/Root.")

if __name__ == "__main__":
    main()