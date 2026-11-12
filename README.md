<div align="center">🧮 Python Calculator

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x" />
  <img src="https://img.shields.io/badge/Status-In_Development-yellow?style=for-the-badge" alt="In development" />
  <img src="https://img.shields.io/badge/Interface-CLI-181717?style=for-the-badge&logo=windowsterminal&logoColor=white" alt="CLI" />
</p>An interactive command-line calculator built with Python.

Exploring mathematical operations, recursive algorithms, input validation, and expression parsing with Abstract Syntax Trees.

<p>
  <a href="#features">Features</a> •
  <a href="#technical-highlights">Technical Highlights</a> •
  <a href="#technologies">Technologies</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#roadmap">Roadmap</a>
</p></div>---

About

Python Calculator is a command-line application developed as a hands-on project to practice Python programming and problem-solving.

It goes beyond basic arithmetic by exploring Abstract Syntax Trees (AST), recursive expression evaluation, exception handling, input validation, and manual string parsing.

The project is a work in progress: features are being improved as new programming concepts are learned and applied.

Features

Feature| Description| Status
➕ Basic operations| Addition, subtraction, multiplication, and division| 🟢
⚡ Exponentiation| Power calculations using the "**" operator| 🟢
√ Square root| Square root calculations using "math.sqrt()"| 🟢
🧮 Expression evaluation| Recursive evaluation of mathematical expressions using AST| 🟢
📊 Percentages| Percentage calculations, increases, and discounts| 🟢
📐 First-degree equations| Initial parsing and coefficient extraction| 🚧
📈 Second-degree equations| Equation-solving functionality| ⏳

<sub>🟢 Implemented · 🚧 In development · ⏳ Planned</sub>

Technical Highlights

Abstract Syntax Trees (AST)

One of the main features of this project is the use of Python's "ast" module to parse mathematical expressions.

Instead of relying on Python's built-in "eval()", the calculator traverses the generated syntax tree recursively and processes supported mathematical operators.

Currently supported operators:

Operator| Operation
"+"| Addition
"-"| Subtraction
"*"| Multiplication
"/"| Division
"**"| Exponentiation
"//"| Floor division
"%"| Modulo
"+x" / "-x"| Unary operations

Input validation and exception handling

The application uses "try/except" blocks and validation loops to handle invalid numerical inputs and menu selections, allowing users to retry instead of immediately terminating the program.

Percentage calculations

The percentage module currently includes three modes:

- Percentage of a given number.
- Percentage increase.
- Percentage decrease.

Equation parsing

The first-degree equation module explores manual string parsing, character indexing, variable identification, and coefficient extraction. The solving logic is still being developed.

Technologies

<div align="center"><img src="https://skillicons.dev/icons?i=python" height="64" alt="Python" />Python 3

</div>Technology| Purpose
Python 3| Main programming language
"math"| Mathematical functions
"ast"| Expression parsing and syntax tree traversal

Getting Started

Prerequisites

- Python 3.x
- Git

Clone the repository

git clone https://github.com/GugaChali/Calculadora-Python.git
cd Calculadora-Python

Run the application

python calculadora.py

Roadmap

- [ ] Complete first-degree equation solving.
- [ ] Implement second-degree equation calculations.
- [ ] Improve AST node and input validation.
- [ ] Handle unsupported expressions and mathematical edge cases.
- [ ] Standardize decimal input handling.
- [ ] Refactor the application into reusable functions.
- [ ] Improve code organization and maintainability.
- [ ] Expand mathematical operation support.

Learning Objectives

Through this project, I am practicing and applying:

- Python control flow and loops.
- Conditional statements.
- Exception handling.
- Input validation and type conversion.
- String manipulation and slicing.
- Recursive algorithms.
- Abstract Syntax Trees.
- Mathematical problem-solving.
- Code organization and maintainability.

---

<div align="center">Built with Python 🐍

A continuous learning project focused on programming fundamentals and software development.

</div>