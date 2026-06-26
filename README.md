<div align="center">

# NOVA

*A simple, modern, statically-typed programming language implemented in Python.*

[![Version](https://img.shields.io/badge/version-v1.0-blue.svg)](https://github.com/varundubey-dev/nova/releases)
[![Python](https://img.shields.io/badge/python-3.13+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Stable-success.svg)](docs/releases/v1.0.0.md)
[![Interpreter](https://img.shields.io/badge/runtime-Tree--Walk-orange.svg)](docs/syntax/_CURRENT_.md)

<p>

<a href="#-features">Features</a> •
<a href="#-implemented-components">Implementation</a> •
<a href="#-documentation">Documentation</a> •
<a href="#-installation">Installation</a> •
<a href="#-try-nova">Try NOVA</a> •
<a href="https://nova.varundubey.dev">Website</a>

</p>

NOVA is a statically-typed programming language built entirely from scratch using a handwritten lexer, recursive-descent parser, abstract syntax tree (AST), module system, and tree-walk interpreter.

The project demonstrates the complete implementation of a programming language—from lexical analysis to runtime execution—while remaining approachable enough to study, extend, and experiment with.

</div>

---

# ✨ Features

- Modern statically-typed language
- Clean and readable syntax
- Rich primitive and collection types
- Runtime type checking
- Schema-based structured data
- User-defined functions
- Recursion
- Module system
- Import / Export support
- Standard Library
- Built-in functions
- Command-line interface
- Comprehensive documentation
- Hundreds of runnable examples

---

# ⚙️ Implemented Components

- Handwritten Lexer
- Recursive-Descent Parser
- Abstract Syntax Tree (AST)
- Runtime Type System
- Tree-Walk Interpreter
- Module Loader
- Module Resolver
- Circular Import Detection
- Standard Library
- Built-in Function System
- CLI
- Source-aware Diagnostic System

---

# 🚀 Example

```nova
import math
import stats
import random

User: M = {
    name: S,
    scores: [N]
}

student: User = {
    name = "Varun",
    scores = [
        92,
        87,
        95
    ]
}

print(student.name)

print(
    "Average:",
    stats.mean(student.scores)
)

print(
    "Square:",
    math.pow(5, 2)
)

print(
    "Lucky Number:",
    random.randint(
        1,
        10
    )
)
```

Output

```text
Varun
Average: 91.33333333333333
Square: 25
Lucky Number: 7
```

---

# 🏗 Architecture

```text
             Source Code
                  │
                  ▼
          Handwritten Lexer
                  │
                  ▼
     Recursive-Descent Parser
                  │
                  ▼
      Abstract Syntax Tree
                  │
                  ▼
        Module Resolution
                  │
                  ▼
      Tree-Walk Interpreter
                  │
                  ▼
         Runtime Values
```

---

# 📚 Documentation

The repository contains complete language documentation covering every released version.

## Language

| Documentation | Description |
|--------------|-------------|
| [`Language Specification`](docs/syntax/_CURRENT_.md) | Complete language reference |
| [`Release Notes`](docs/releases/) | Detailed release history |
| [`Changelog`](docs/releases/_CHANGELOG_.md) | Version overview |

---

## Standard Library

| Module | Documentation |
|---------|---------------|
| Math | [`math.md`](docs/stdlib/math.md) |
| Array | [`array.md`](docs/stdlib/array.md) |
| Random | [`random.md`](docs/stdlib/random.md) |
| Statistics | [`stats.md`](docs/stdlib/stats.md) |
| Time | [`time.md`](docs/stdlib/time.md) |

Complete Reference

- [`Standard Library Index`](docs/stdlib/_INDEX_.md)

---

## Built-in Functions

Documentation

- [`Built-in Function Index`](docs/builtins/_INDEX_.md)

Available Categories

- Arrays
- Strings
- Input
- Type Conversion

---

## Examples

Every language release includes runnable demonstrations and error cases.

```text
examples/

├── v0.1
├── v0.2
├── v0.3
├── v0.4
├── v0.5
├── v0.6
├── v0.7
├── v0.8
├── v0.9
└── v1.0
```

---

# 📦 Installation

## Requirements

- Python >= 3.10

## Install from PyPI

Install the latest stable release.

```bash
pip install nova-pl
```

Verify the installation.

```bash
nova --version
```

Run a NOVA program.

```bash
nova hello.nova
```

---

## Build from Source

Clone the repository.

```bash
git clone https://github.com/varundubey-dev/nova.git

cd nova
```

Install the development version.

```bash
pip install .
```

Or install in editable mode while contributing to NOVA.

```bash
pip install -e .
```

---

# 🏛 Repository Layout

```text
nova/
│
├── lexer/
├── parser/
├── ast/
├── interpreter/
├── modules/
├── stdlibs/
├── api.py
└── cli.py

docs/
├── syntax/
├── stdlib/
├── builtins/
└── releases/

examples/
├── v0.1
├── ...
└── v1.0
```

---

# 📈 Evolution

```text
v0.1 ── Core Language
          │
          ▼
v0.2 ── Primitive Type System
          │
          ▼
v0.3 ── Arrays
          │
          ▼
v0.4 ── Schema Maps
          │
          ▼
v0.5 ── Control Flow
          │
          ├── v0.5.1  Multi-expression print()
          ▼
v0.6 ── Iteration & Loops
          │
          ├── v0.6.1  break / continue
          ▼
v0.7 ── User-defined Functions
          │
          ▼
v0.8 ── Built-in Functions
          │
          ▼
v0.9 ── Module System
          │
          ▼
v1.0 ── Standard Library
```

---

# 🌐 Official Website

The NOVA website provides everything needed to learn, explore, and experiment with the language directly in your browser.

| Resource | Link | Description |
|----------|------|-------------|
| 🏠 Home | `https://nova.varundubey.dev` | Project homepage |
| 🚀 Playground | `https://nova.varundubey.dev/playground` | Run NOVA programs online |
| 📖 Documentation | `https://nova.varundubey.dev/docs` | Complete language documentation |
| 📚 Standard Library | `https://nova.varundubey.dev/docs/stdlib` | Standard Library reference |
| 🔧 Built-in Functions | `https://nova.varundubey.dev/docs/builtins` | Built-in function reference |
| 💡 Examples | `https://nova.varundubey.dev/examples` | Interactive examples |
| 📰 Release Notes | `https://nova.varundubey.dev/releases` | Complete release history |

---

# 💻 Try NOVA

### Run Locally

```bash
git clone https://github.com/varundubey-dev/nova.git

cd nova

pip install .

nova hello.nova
```

### Run in Your Browser

Visit the NOVA Playground.

```text
https://nova.varundubey.dev/playground
```

No installation required.

---

<div align="center">

### ⭐ If you found NOVA interesting, consider starring the repository!

Built from scratch in Python.

Made by **Varun Dubey**

</div>