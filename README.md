<div align="center">

# 🧮 Python Calculator

**A command-line calculator built from scratch with Python.**

Exploring mathematical operations, recursive algorithms, input validation, and expression parsing with Abstract Syntax Trees.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x" />
  <img src="https://img.shields.io/badge/Status-In_Development-yellow?style=for-the-badge" alt="In development" />
  <img src="https://img.shields.io/badge/Interface-CLI-181717?style=for-the-badge&logo=windowsterminal&logoColor=white" alt="Command-line interface" />
</p>

[Features](#-features) · [How It Works](#-how-it-works) · [Technologies](#-technologies) · [Getting Started](#-getting-started) · [Roadmap](#-roadmap)

</div>

---

## 📌 About

**Python Calculator** is an interactive command-line application developed as a hands-on project to practice Python programming and problem-solving.

It goes beyond basic arithmetic by exploring recursive expression evaluation, Abstract Syntax Trees (AST), exception handling, input validation, and manual string parsing.

The project is continuously evolving as new programming concepts are learned and applied.

---

## ✨ Features

| Feature | Description | Status |
| :--- | :--- | :---: |
| ➕ **Basic operations** | Addition, subtraction, multiplication, and division | 🟢 |
| ⚡ **Exponentiation** | Power calculations using the `**` operator | 🟢 |
| √ **Square root** | Square root calculations using Python's `math` module | 🟡 |
| 🧮 **Expression evaluation** | Recursive evaluation of mathematical expressions using AST | 🟢 |
| 📊 **Percentages** | Percentage calculations, increases, and discounts | 🟢 |
| 📐 **First-degree equations** | Initial parsing and coefficient extraction | 🚧 |
| 📈 **Second-degree equations** | Equation-solving functionality | ⏳ |

<sub>🟢 Implemented · 🟡 Implemented, with improvements needed · 🚧 In progress · ⏳ Planned</sub>

---

## ⚙️ How It Works

### Abstract Syntax Trees (AST)
One of the central technical features is the use of Python's `ast` module to parse mathematical expressions. Instead of relying on Python's built-in `eval()`, the calculator traverses the generated syntax tree recursively and evaluates supported operations.

**Currently supported operators:**

| Operator | Operation |
| :---: | :--- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `**` | Exponentiation |
| `//` | Floor division |
| `%` | Modulo |
| `+x` / `-x` | Unary plus and minus |

### Input validation and exception handling
The application uses `try/except` blocks and validation loops to handle invalid numerical inputs and menu selections, allowing users to retry instead of immediately terminating the program.

### Percentage calculations
The percentage module currently includes three modes:
- Percentage of a given number.
- Percentage increase.
- Percentage decrease (discount).

### Equation parsing
The first-degree equation module explores manual string parsing, character indexing, variable identification, and coefficient extraction. The equation-solving logic is still being developed.

---

## 🧰 Technologies

<div align="center">
  <img src="https://skillicons.dev/icons?i=python" height="64" alt="Python" />
</div>

<br>

| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Main programming language |
| **`math`** | Mathematical functions |
| **`ast`** | Expression parsing and syntax tree traversal |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Git

### 1. Clone the repository
```bash
git clone [https://github.com/GugaChali/Calculadora-Python.git](https://github.com/GugaChali/Calculadora-Python.git)
cd Calculadora-Python
