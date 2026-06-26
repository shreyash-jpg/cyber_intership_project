import re


def check_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_criteria = re.search(r"[\W_]", password) is not None

    # Score calculation (max score = 5)
    score = sum(
        [
            length_criteria,
            uppercase_criteria,
            lowercase_criteria,
            number_criteria,
            special_criteria,
        ]
    )

    # Feedback
    print("\n--- Password Strength Report ---")
    print(f"[*] Length (Min 8 chars): {'✔️' if length_criteria else '❌'}")
    print(f"[*] Uppercase Letter:     {'✔️' if uppercase_criteria else '❌'}")
    print(f"[*] Lowercase Letter:     {'✔️' if lowercase_criteria else '❌'}")
    print(f"[*] Number (0-9):         {'✔️' if number_criteria else '❌'}")
    print(f"[*] Special Character:    {'✔️' if special_criteria else '❌'}")

    print("-" * 30)
    if score == 5:
        return "Strength: VERY STRONG 💪🔥"
    elif score == 4:
        return "Strength: STRONG 👍"
    elif score == 3:
        return "Strength: MEDIUM (can be improved) 😐"
    else:
        return "Strength: WEAK (Easily Crackable) ❌"


def main():
    print("--- Password Complexity Checker ---")
    while True:
        password = input("\nEnter a password to check (type 'exit' to stop): ")
        if password.lower() == 'exit':
            print("Exiting Password Checker. Goodbye!")
            break

        result = check_password_strength(password)
        print(result)


if __name__ == "__main__":
    main()

