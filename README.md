🧮 Python Calculator

<div align="center">  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Interface-CLI-181717?style=for-the-badge&logo=windowsterminal&logoColor=white" /><br><br>

A Python-based command-line calculator exploring mathematical operations, recursive algorithms, and expression parsing.

  <br>"Features" (#-features) •
"Technologies" (#-technologies) •
"Installation" (#-installation) •
"Roadmap" (#-roadmap)

</div>---

📖 About

Python Calculator is an interactive command-line application developed to practice and explore Python programming concepts through mathematical operations.

Beyond standard arithmetic, the project explores Abstract Syntax Trees (AST), recursive expression evaluation, input validation, exception handling, and manual string parsing.

The application is continuously evolving as new concepts and improvements are implemented.

✨ Features

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Description</th>
      <th align="center">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>➕ <b>Basic Operations</b></td>
      <td>Addition, subtraction, multiplication, and division.</td>
      <td align="center">🟢</td>
    </tr>
    <tr>
      <td>⚡ <b>Exponentiation</b></td>
      <td>Power calculations using the <code>**</code> operator.</td>
      <td align="center">🟢</td>
    </tr>
    <tr>
      <td>√ <b>Square Root</b></td>
      <td>Square root calculations using <code>math.sqrt()</code>.</td>
      <td align="center">🟢</td>
    </tr>
    <tr>
      <td>🧮 <b>Expression Evaluation</b></td>
      <td>Recursive mathematical expression evaluation using AST.</td>
      <td align="center">🟢</td>
    </tr>
    <tr>
      <td>📊 <b>Percentages</b></td>
      <td>Percentage calculations, increases, and discounts.</td>
      <td align="center">🟢</td>
    </tr>
    <tr>
      <td>📐 <b>First-Degree Equations</b></td>
      <td>Initial equation parsing and coefficient extraction.</td>
      <td align="center">🚧</td>
    </tr>
    <tr>
      <td>📈 <b>Second-Degree Equations</b></td>
      <td>Equation-solving functionality planned.</td>
      <td align="center">⏳</td>
    </tr>
  </tbody>
</table><sub>🟢 Implemented   •   🚧 In Development   •   ⏳ Planned</sub>

🧠 Technical Highlights

Abstract Syntax Trees (AST)

One of the main technical features is the use of Python's "ast" module to parse and evaluate mathematical expressions.

Instead of using Python's built-in "eval()", the application traverses the generated syntax tree recursively, identifying and processing supported mathematical operators.

Currently supported operators:

Operator| Operation
"+"| Addition
"-"| Subtraction
"*"| Multiplication
"/"| Division
"**"| Exponentiation
"//"| Floor Division
"%"| Modulo
"+x" / "-x"| Unary Operations

Input Validation

The application uses "try/except" blocks and validation loops to handle invalid numerical inputs and menu selections, allowing users to retry without immediately terminating the program.

Mathematical Calculations

The percentage module provides three calculation modes:

- Percentage of a given number.
- Percentage increase.
- Percentage decrease.

Equation Parsing

The first-degree equation module introduces manual string parsing, character indexing, variable identification, and coefficient extraction.

---

🛠️ Technologies

<div align="center">  <img src="https://skillicons.dev/icons?i=python" height="55" alt="Python" />  <br>Python 3 · "math" · "ast"

</div>Technology| Purpose
Python 3| Main programming language
"math"| Mathematical functions
"ast"| Expression parsing and syntax tree traversal

---

🚀 Installation

Prerequisites

- Python 3.x
- Git

Clone the repository

git clone <REPOSITORY_URL>

Navigate to the project directory

cd Calculadora-Python

Run the application

python calculadora.py

---

🗺️ Roadmap

- [ ] Complete first-degree equation solving.
- [ ] Implement second-degree equation calculations.
- [ ] Improve AST node validation and exception handling.
- [ ] Handle unsupported expressions and mathematical edge cases.
- [ ] Standardize decimal input handling.
- [ ] Refactor the application into reusable functions.
- [ ] Improve code organization and maintainability.
- [ ] Expand mathematical operation support.

---

📚 Learning Objectives

This project provides practical experience with:

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

<div align="center">💻 Built with Python

A continuous learning project focused on programming fundamentals and software development.

  <br>Thanks for visiting!

</div>