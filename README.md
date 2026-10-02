# Password Security Analyzer

A Python-based cybersecurity project that analyzes password security using multiple security indicators.

## Features

- Checks password length
- Detects uppercase and lowercase characters
- Detects numbers and special characters
- Calculates estimated password entropy
- Detects repeated-character patterns
- Detects sequential patterns
- Detects keyboard patterns
- Checks against a common-password dictionary
- Calculates a security score from 0 to 100
- Provides a security rating
- Generates secure passwords using Python's `secrets` module
- Includes automated tests with pytest

## Project Structure

```text
password-security-analyzer-project/
├── app.py
├── generator.py
├── password_analyzer.py
├── patterns.py
├── pytest.ini
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── common_passwords.txt
├── docs/
│   └── threat_model.md
└── tests/
    └── test_analyzer.py