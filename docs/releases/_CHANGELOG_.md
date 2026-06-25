# Changelog

All notable changes to NOVA are documented in this file.

For complete details about each release, see the release notes in [Release Notes](../releases/).
---

## Version History

| Version    | Release | Summary                                                                                                                |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| **v0.7.0** | Major   | Introduced user-defined functions, recursion, return values, parameters, function scope, and reusable program logic.   |
| **v0.6.1** | Patch   | Added `break` and `continue` statements with loop control validation.                                                  |
| **v0.6.0** | Major   | Introduced structured iteration through while loops, range loops, array iteration, nested loops, and loop scope.       |
| **v0.5.1** | Patch   | Enhanced `print()` to support multiple comma-separated expressions.                                                    |
| **v0.5.0** | Major   | Added conditional execution, block scope, variable shadowing, unary expressions, and ternary operators.                |
| **v0.4.0** | Major   | Introduced schema maps, map instances, nested schemas, property access, and structured data.                           |
| **v0.3.0** | Major   | Added arrays, typed arrays, nested arrays, array mutation, and source-aware diagnostics.                               |
| **v0.2.0** | Major   | Expanded the primitive type system with booleans, constants, null values, comparison operators, and logical operators. |
| **v0.1.0** | Initial | Initial public release establishing NOVA's lexer, parser, AST, interpreter, primitive types, and runtime.              |

---

# Evolution of NOVA

```
v0.1 ── Core Language
          │
          ▼
v0.2 ── Primitive Type System
          │
          ▼
v0.3 ── Collections (Arrays)
          │
          ▼
v0.4 ── Structured Data (Schema Maps)
          │
          ▼
v0.5 ── Conditional Execution
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
v0.8 ── Standard Library (Planned)
```

---

# Detailed Release Notes

| Version | Release Notes                          |
| ------- | -------------------------------------- |
| v0.7.0  | [NOVA v0.7.0 Release Notes](v0.7.0.md) |
| v0.6.1  | [NOVA v0.6.1 Release Notes](v0.6.1.md) |
| v0.6.0  | [NOVA v0.6.0 Release Notes](v0.6.0.md) |
| v0.5.1  | [NOVA v0.5.1 Release Notes](v0.5.1.md) |
| v0.5.0  | [NOVA v0.5.0 Release Notes](v0.5.0.md) |
| v0.4.0  | [NOVA v0.4.0 Release Notes](v0.4.0.md) |
| v0.3.0  | [NOVA v0.3.0 Release Notes](v0.3.0.md) |
| v0.2.0  | [NOVA v0.2.0 Release Notes](v0.2.0.md) |
| v0.1.0  | [NOVA v0.1.0 Release Notes](v0.1.0.md) |

---

## Roadmap

**Current Version:** `v0.7.0`

**Next Planned Release:** `v0.8.0`

Focus areas:

* Standard Library
* Built-in Functions
* Input Functions
* Type Conversion Functions
* String Functions
* Array Functions
* Map Functions
* Mathematical Functions
