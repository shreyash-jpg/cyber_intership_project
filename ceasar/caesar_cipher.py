def caesar_cipher(text, shift, mode):
    result = ""
    
    # Agar decrypt karna hai, toh shift ko negative kar denge
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Space ya special characters ko vaise hi chhod denge
        else:
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Tool ---")
    while True:
        choice = input("\n Enter Process(encrypt/decrypt/exit): ").lower().strip()
        
        if choice == 'exit':
            print("Goodbye!")
            break
            
        if choice not in ['encrypt', 'decrypt']:
            print("Wrong option! Please Enter'encrypt', 'decrypt' or 'exit'.")
            continue
            
        message = input("Enter your Msg: ")
        try:
            shift = int(input("Enter Shift value (number): "))
        except ValueError:
            print("Please Enter valid number (integer) ")
            continue
            
        output = caesar_cipher(message, shift, choice)
        print(f"\nResult ({choice}ed): {output}")

if __name__ == "__main__":
    main()
