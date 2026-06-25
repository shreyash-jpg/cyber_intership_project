# Image Encryptor (`image/image_encryptor.py`)

## What it does
Encrypts/decrypts an image by applying a simple **pixel XOR** operation (same operation works for encryption and decryption).

- Each pixel’s RGB channels are XOR-ed with a single integer key `1..255`
- If the image has an alpha channel (RGBA), alpha is preserved

## File
- `image/image_encryptor.py`

## Prerequisites
- Python 3.x
- Pillow

### Install
```bash
pip install pillow
```

## Run
```bash
python image/image_encryptor.py
```

## How to use
1. Choose: `encrypt` or `decrypt`
2. Provide `input image path` (e.g. `photo.jpg`)
3. Provide `output image name` (e.g. `encrypted.jpg`)
4. Provide `Encryption Key` (integer between `1` and `255`)

## Notes
- Output file is saved using the provided output path/name.
- XOR with the same key restores the original when decrypting.

