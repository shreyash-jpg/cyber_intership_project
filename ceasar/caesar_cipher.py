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
        choice = input("\nKya karna chahte ho? (encrypt/decrypt/exit): ").lower().strip()
        
        if choice == 'exit':
            print("Alvida!")
            break
            
        if choice not in ['encrypt', 'decrypt']:
            print("Galat option! Please 'encrypt', 'decrypt' ya 'exit' chune.")
            continue
            
        message = input("Apna message likho: ")
        try:
            shift = int(input("Shift value (number) dalo: "))
        except ValueError:
            print("Please ek valid number (integer) dalo!")
            continue
            
        output = caesar_cipher(message, shift, choice)
        print(f"\nResult ({choice}ed): {output}")

if __name__ == "__main__":
    main()