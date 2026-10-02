import secrets
import string


def generate_password(length=16):
    if length < 12:
        raise ValueError("Password length must be at least 12")

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print(generate_password())