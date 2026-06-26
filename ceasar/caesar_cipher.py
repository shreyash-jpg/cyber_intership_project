def caesar_cipher(text, shift, mode):
    result = ""

    # If we are decrypting, negate the shift.
    if mode == 'decrypt':
        shift = -shift

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
<<<<<<< HEAD
        choice = input("\nWhat would you like to do? (encrypt/decrypt/exit): ").lower().strip()

=======
        choice = input("\n Enter Process(encrypt/decrypt/exit): ").lower().strip()
        
>>>>>>> 5ba29179b65ba68693ae3d27003f5e4b5585a9c5
        if choice == 'exit':
            print("Goodbye!")
            break

        if choice not in ['encrypt', 'decrypt']:
<<<<<<< HEAD
            print("Invalid option! Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Shift value (number): "))
        except ValueError:
            print("Please enter a valid integer number.")
=======
            print("Wrong option! Please Enter'encrypt', 'decrypt' or 'exit'.")
            continue
            
        message = input("Enter your Msg: ")
        try:
            shift = int(input("Enter Shift value (number): "))
        except ValueError:
            print("Please Enter valid number (integer) ")
>>>>>>> 5ba29179b65ba68693ae3d27003f5e4b5585a9c5
            continue

        output = caesar_cipher(message, shift, choice)
        print(f"\nResult ({choice}ed): {output}")


if __name__ == "__main__":
    main()
<<<<<<< HEAD

=======
>>>>>>> 5ba29179b65ba68693ae3d27003f5e4b5585a9c5
