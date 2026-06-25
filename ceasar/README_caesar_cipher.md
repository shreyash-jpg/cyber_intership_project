# Caesar Cipher Tool (`ceasar/caesar_cipher.py`)

## What it does
Encrypts and decrypts text using the **Caesar Cipher** (shift-based substitution).

- Uppercase letters: **A-Z** preserved, shifted by `shift`
- Lowercase letters: **a-z** preserved, shifted by `shift`
- Other characters (spaces/special chars): **kept as-is**

## File
- `ceasar/caesar_cipher.py`

## Run
```bash
python ceasar/caesar_cipher.py
```

## How to use
1. Choose: `encrypt` or `decrypt` (type `exit` to quit)
2. Enter the message
3. Enter `shift` (integer)

## Notes
- For `decrypt`, the script automatically negates the shift.

