import math
import string
from patterns import find_repeated_characters, find_sequential_patterns, find_keyboard_patterns


def calculate_entropy(password):
    if not password:
        return 0.0

    character_pool = 0

    if any(c in string.ascii_lowercase for c in password):
        character_pool += 26

    if any(c in string.ascii_uppercase for c in password):
        character_pool += 26

    if any(c in string.digits for c in password):
        character_pool += 10

    if any(c in string.punctuation for c in password):
        character_pool += len(string.punctuation)

    if character_pool == 0:
        return 0.0

    return len(password) * math.log2(character_pool)

def load_common_passwords():
    with open("data/common_passwords.txt", "r") as file:
        return {line.strip() for line in file}

def calculate_score(result):
    score = 0

    if result["length"] >= 12:
        score += 25

    if result["has_uppercase"]:
        score += 15

    if result["has_lowercase"]:
        score += 15

    if result["has_number"]:
        score += 15

    if result["has_special"]:
        score += 15

    if not result["common_password"]:
        score += 15

    return score

def get_rating(score):
    if score >= 80:
        return "Strong"
    elif score >= 50:
        return "Moderate"
    else:
        return "Weak"


def analyze_password(password):
    result = {
        "length": len(password),
        "has_uppercase": any(c.isupper() for c in password),
        "has_lowercase": any(c.islower() for c in password),
        "has_number": any(c.isdigit() for c in password),
        "has_special": any(not c.isalnum() for c in password),
        "entropy": calculate_entropy(password),
        "repeated_patterns": find_repeated_characters(password),
        "sequential_patterns": find_sequential_patterns(password),
        "keyboard_patterns": find_keyboard_patterns(password),
        "common_password": password.lower() in load_common_passwords()
    }

    result["score"] = calculate_score(result)
    result["rating"] = get_rating(result["score"])

    return result


if __name__ == "__main__":
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