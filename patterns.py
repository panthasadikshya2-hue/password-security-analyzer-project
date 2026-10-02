def find_repeated_characters(password):
    repeated = []

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            repeated.append(password[i] * 3)

    return repeated

def find_sequential_patterns(password):
    sequences = []

    password = password.lower()

    for i in range(len(password) - 2):
        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])

        if second == first + 1 and third == second + 1:
            sequences.append(password[i:i + 3])

        elif second == first - 1 and third == second - 1:
            sequences.append(password[i:i + 3])

    return sequences





def find_keyboard_patterns(password):
    keyboard_rows = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "1234567890"
    ]

    password = password.lower()
    patterns = []

    for row in keyboard_rows:
        for i in range(len(row) - 2):
            pattern = row[i:i + 3]

            if pattern in password:
                patterns.append(pattern)

    return patterns