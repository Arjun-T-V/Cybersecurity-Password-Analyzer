# 🔐 Cybersecurity Password Analyzer

A Python-based command-line application that evaluates password security using multiple cybersecurity techniques. The analyzer checks password strength, calculates entropy, detects common passwords, estimates security levels, and provides suggestions for creating stronger passwords.

---

## 📌 Features

- Analyze password strength (Weak, Medium, Strong)
- Calculate password entropy (in bits)
- Provide entropy rating
- Detect common passwords using a blacklist
- Generate personalized security suggestions
- Validate user input
- Modular and reusable Python code structure
- Beginner-friendly cybersecurity project

---

## 🛠 Technologies Used

- Python 3
- Python Standard Library
  - `math`
- File Handling
- Modular Programming

---

## 📂 Project Structure

```
Cybersecurity-Password-Analyzer/
│
├── password_analyzer.py
├── common_passwords.txt
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Cybersecurity-Password-Analyzer.git
```

2. Navigate to the project folder:

```bash
cd Cybersecurity-Password-Analyzer
```

3. Run the program:

```bash
python password_analyzer.py
```

---

## 📷 Sample Output

```
========================
PASSWORD ANALYSIS REPORT
========================
        
Password Score : 4/5
Strength       : Medium
Entropy Score  : 54.79 bits
Entropy Rating : Reasonable

Suggestions:
-Add uppercase
========================

```

---

## 🔒 Password Evaluation Criteria

The analyzer evaluates passwords based on:

- Minimum length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Entropy calculation
- Common password detection

---

## 🎯 Learning Objectives

This project was developed to practice:

- Python programming
- Functions and modular programming
- File handling
- Conditional logic
- Cybersecurity fundamentals
- Password security concepts

---

## 🚧 Future Improvements

- Crack time estimation
- Secure password generator
- GUI using Tkinter
- Password breach detection using APIs
- Export analysis reports
- Flask web version
- Password history analysis

---

## 👨‍💻 Author

**Arjun T V**

Developed as a personal project to strengthen Python programming skills and explore cybersecurity concepts.
