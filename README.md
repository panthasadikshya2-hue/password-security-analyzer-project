# Password Security Analyzer

A Python-based cybersecurity project that analyzes password security using multiple security indicators.

## Features

* Checks password length
* Detects uppercase and lowercase characters
* Detects numbers and special characters
* Calculates estimated password entropy
* Detects repeated-character patterns
* Detects sequential patterns
* Detects keyboard patterns
* Checks against a common password dictionary
* Calculates a security score from 0 to 100
* Provides a security rating
* Generates secure passwords using Python's `secrets` module
* Includes automated tests with pytest

## Project Structure

```text
password-security-analyzer-project/
│
├── app.py
├── generator.py
├── password_analyzer.py
├── patterns.py
├── pytest.ini
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── common_passwords.txt
│
├── docs/
│   └── threat_model.md
│
└── tests/
    └── test_analyzer.py
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Go into the project folder:

```bash
cd password-security-analyzer-project
```

Install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## How to Run

Start the password security analyzer with:

```bash
python3 app.py
```

The program will ask you to enter a password and analyze its security characteristics.

The analyzer provides information such as:

* Password length
* Character types
* Entropy estimate
* Detected patterns
* Common-password matches
* Security score
* Security rating

## Password Generator

The project also includes a secure password generator using Python's `secrets` module.

Run:

```bash
python3 generator.py
```

The generator creates a randomly generated secure password.

## Running Tests

This project uses `pytest` for automated testing.

Run the tests with:

```bash
python3 -m pytest
```

All 8 automated tests currently pass.

## Security Analysis

The analyzer evaluates several characteristics of a password, including:

* Length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Estimated entropy
* Repeated-character patterns
* Sequential patterns
* Keyboard patterns
* Common passwords

These factors are used to calculate a security score from **0 to 100** and provide an overall security rating.

## Threat Model

A basic threat model is included in:

```text
docs/threat_model.md
```

The threat model discusses common password security threats and characteristics that can make passwords easier to guess or attack.

## Technologies Used

* Python
* Python `secrets` module
* pytest
* Git
* GitHub

## What I Learned

This project helped me practice Python programming while learning about cybersecurity and password security.

I learned how to work with:

* Functions
* Conditional statements
* Strings and character analysis
* Lists and sets
* Pattern detection
* File handling
* Python modules
* Automated testing
* Secure random password generation
* Basic cybersecurity concepts

## Future Improvements

Possible future improvements include:

* Adding a graphical user interface
* Improving password pattern detection
* Adding more common passwords to the dictionary
* Adding more detailed security recommendations
* Creating a web-based version of the analyzer

## Disclaimer

This project is intended for educational purposes. The security score is an estimate and should not be considered a complete measure of real-world password security.


