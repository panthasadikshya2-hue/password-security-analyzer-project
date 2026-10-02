from password_analyzer import analyze_password
from generator import generate_password


def main():
    print("Password Security Analyzer")
    print("--------------------------")
    print("1. Analyze password")
    print("2. Generate secure password")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        password = input("Enter a password: ")

        result = analyze_password(password)

        print("\nPassword Analysis")
        print("-----------------")
        print("Length:", result["length"])
        print("Has uppercase:", result["has_uppercase"])
        print("Has lowercase:", result["has_lowercase"])
        print("Has number:", result["has_number"])
        print("Has special character:", result["has_special"])
        print("Estimated entropy:", round(result["entropy"], 2), "bits")
        print("Repeated patterns:", result["repeated_patterns"])
        print("Sequential patterns:", result["sequential_patterns"])
        print("Keyboard patterns:", result["keyboard_patterns"])
        print("Common password:", result["common_password"])
        print("Security score:", result["score"], "/ 100")
        print("Security rating:", result["rating"])

    elif choice == "2":
        password = generate_password()

        print("\nGenerated Secure Password")
        print("-------------------------")
        print(password)

    elif choice == "3":
        print("Goodbye!")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()