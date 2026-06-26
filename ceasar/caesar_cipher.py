def caesar_cipher(text, shift, mode):
    result = ""

    # If we are decrypting, negate the shift.
    if mode == "decrypt":
        shift = -shift

    # Normalize shift so large integers behave consistently.
    shift %= 26

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep spaces/special characters unchanged
        else:
            result += char

    return result


def main():
    print("--- Caesar Cipher Tool ---")

    while True:
        choice = input("\nWhat would you like to do? (encrypt/decrypt/exit): ").lower().strip()

        if choice == "exit":
            print("Goodbye!")
            break

        if choice not in ["encrypt", "decrypt"]:
            print("Invalid option! Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift (integer): ").strip())
        except ValueError:
            print("Please enter a valid integer shift.")
            continue

        output = caesar_cipher(message, shift, choice)
        label = "encrypted" if choice == "encrypt" else "decrypted"
        print(f"\nResult ({label}): {output}")


if __name__ == "__main__":
    main()

