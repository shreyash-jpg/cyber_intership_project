# Network Packet Analyzer / Sniffer (`packet/packet_analyzer.py`)

## What it does
Captures network packets live and prints:

- Source IP / Destination IP
- Protocol (TCP/UDP/ICMP)
- (If present) truncated payload for TCP/UDP

## File
- `packet/packet_analyzer.py`

## Prerequisites
- Python 3.x
- scapy

### Install
```bash
pip install scapy
```

## Run
```bash
python packet/packet_analyzer.py
```

## Run requirements (important)
- Usually requires **Administrator** (Windows) / elevated privileges.

## How to use
1. Start the script
2. View printed packets in the terminal
3. Stop with `Ctrl+C`

## Notes
- Capturing traffic without authorization may violate laws/policies. Use only on networks you have permission to monitor.

