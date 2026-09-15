# DecodeLabs Internship — Cyber Security Track

A portfolio of four hands-on cybersecurity projects completed during my **DecodeLabs Internship (Batch 2026)**. Each project applies core security concepts through practical CLI tools: password validation, encryption, threat analysis, and system risk assessment.

## Projects

| # | Project | What You'll Learn |
| --- | --- | --- |
| 1 | [Password Strength Checker](./Project1_password_checker) | File I/O, breach-list validation, scoring logic. Evaluates password strength against a 100k NCSC breached-password list. |
| 2 | [Caesar Cipher Encryption/Decryption](./Project2_encryption_decryption) | Character encoding, modular arithmetic, encryption fundamentals. Encrypts and decrypts text using a customizable-shift cipher. |
| 3 | [Phishing Awareness Analysis](./Project3_phishing_analysis) | Threat modeling, risk classification, decision trees. Provides a triage checklist for identifying phishing red flags. |
| 4 | [System Vulnerability Checklist](./Project4_vulnerability_checklist) | System calls via `subprocess`, weighted risk scoring, real-world auditing. Performs live security audit (password + OS updates + user habits). |

## Quick Start

### Requirements
- Python 3.6+
- For Projects 1 & 4: download the [NCSC top 100k passwords list](https://www.ncsc.gov.uk/static_assets/documents/PwnedPasswordsTop100k.txt) and place it in the relevant project folder.

### Run a project
```bash
cd Project1_password_checker
python3 project1.py

cd ../Project2_encryption_decryption
python3 project2.py

cd ../Project4_vulnerability_checklist
python3 vulncheck.py
```

## Tech Stack
- Language: Python 3 (standard library only — no external dependencies)
- Focus: Core security concepts, CLI design, file I/O, and system-level operations

## About
These projects demonstrate foundational cybersecurity skills through code that solves real problems. Built for learning, portfolio building, and interview prep.

## Author
- Moin Atta Khakwani
- GitHub: [@moinatta-k](https://github.com/moinatta-k)

