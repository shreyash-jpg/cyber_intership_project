# Cyber Intership Project
(5 Python Tools)

This folder contains 5 Python programs:

1. `caesar_cipher.py` — Caesar Cipher (encrypt/decrypt)
2. `image_encryptor.py` — Image Encryption (pixel XOR) *(Pillow required)*
3. `packet_analyzer.py` — Network Packet Analyzer (sniffer) *(scapy required + Admin)*
4. `password_checker.py` — Password Strength / Complexity Checker
5. `simple_keylogger.py` — Simple Keylogger *(pynput required; security/ethical risk)*

> **Note:** `simple_keylogger.py` is in the keylogger category. Running it may be blocked by OS/security/antivirus and can raise legal/ethical issues. Therefore, this README does not include run/verification steps for it.

---

## Prerequisites

- Python 3.x

External dependencies (optional, only for specific scripts):

- Image tool:
  - `pip install pillow`
- Packet analyzer tool:
  - `pip install scapy`

---

## 1) Caesar Cipher — `caesar_cipher.py`

**Command:**
```bash
python caesar_cipher.py
```

**What it does:**
- Encrypts/Decrypts user-provided text
- Applies the shift to uppercase and lowercase letters
- Keeps spaces/special characters unchanged

---

## 2) Image Encryptor — `image_encryptor.py`

**Dependency:** Pillow

**Install:**
```bash
pip install pillow
```

**Command:**
```bash
python image_encryptor.py
```

**What it does:**
- Prompts for `encrypt` / `decrypt`
- Takes input image path
- Takes output image name
- Takes a key (`1-255`)
- Performs an XOR operation on pixel RGB channels (alpha is preserved for RGBA)

---

## 3) Packet Analyzer (Sniffer) — `packet_analyzer.py`

**Dependency:** scapy

**Install:**
```bash
pip install scapy
```

**Command:**
```bash
python packet_analyzer.py
```

**Run requirements:**
- Usually requires **Administrator** / elevated permissions

**What it does:**
- Sniffs live network packets
- Prints Source IP, Destination IP, Protocol (TCP/UDP/ICMP)
- For TCP/UDP, prints a truncated preview of payload data (when available)
- Stop with `Ctrl+C`

---

## 4) Password Checker — `password_checker.py`

**Command:**
```bash
python password_checker.py
```

**What it does:**
- Checks criteria:
  - length >= 8
  - contains uppercase `A-Z`
  - contains lowercase `a-z`
  - contains digit `0-9`
  - contains special character (`\W` or `_`)
- Produces a strength label based on the number of satisfied criteria (max score: 5)

---

## 5) Keylogger — `simple_keylogger.py`

**Dependency:** `pynput`

**Important (safety/legal):**
- This script logs keystrokes and stops when you press `ESC`.
- Due to antivirus/OS permissions and ethical/legal constraints, running it can be risky.

Run instructions are intentionally not included in this README.

---

## Quick Start (Recommended)

If you do not want to install extra dependencies, you can run:

- `python ceasar/caesar_cipher.py`
- `python password/password_checker.py`

---

## File Index

- `ceasar/caesar_cipher.py`
- `image/image_encryptor.py`
- `packet/packet_analyzer.py`
- `password/password_checker.py`
- `keylogger/simple_keylogger.py`


