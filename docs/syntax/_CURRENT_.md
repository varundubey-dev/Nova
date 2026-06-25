# NOVA Language Specification

### Current Version (v0.7)

This document describes the current stable syntax and language features supported by NOVA.

Historical specifications are available in the versioned documentation.

---

## Language Versions

| Version |           Specification       |
| ------- | ----------------------------- |
| v0.7    | [NOVA v0.7 Syntax](v0.7.md)   |
| v0.6    | [NOVA v0.6 Syntax](v0.6.md)   |
| v0.5    | [NOVA v0.5 Syntax](v0.5.md)   |
| v0.4    | [NOVA v0.4 Syntax](v0.4.md)   |
| v0.3    | [NOVA v0.3 Syntax](v0.3.md)   |
| v0.2    | [NOVA v0.2 Syntax](v0.2.md)   |
| v0.1    | [NOVA v0.1 Syntax](v0.1.md)   |

---

## Current Features

### Primitive Types

* Numbers (`N`)
* Strings (`S`)
* Booleans (`B`)
* Any (`U`)

---

### Variables

* Mutable variables
* Immutable constants
* Deferred initialization
* Runtime datatype validation

---

### Expressions

* Arithmetic
* Comparison
* Equality
* Logical
* Unary
* Parenthesized expressions
* Ternary expressions

---

### Collections

* Arrays
* Typed arrays
* Multi-type arrays
* Nested arrays
* Array indexing
* Array mutation

---

### Schema Maps

* Schema declarations
* Map instances
* Optional properties
* Nested schemas
* Arrays of maps
* Property access
* Property mutation
* Runtime schema validation

---

### Control Flow

* `if`
* `else`
* `else if`
* Block scope
* Variable shadowing

---

### Loops

* `while`
* `for`
* Exclusive ranges (`..`)
* Inclusive ranges (`...`)
* Descending ranges
* Array iteration
* Nested loops
* `break`
* `continue`

---

### Functions

* Function declarations
* Function calls
* Parameters
* Return values
* Return type enforcement
* Early returns
* Global scope access
* Local function scope
* Recursive functions

---

### Built-in Functions

See the Standard Library documentation:

* [Index](../stdlib/_INDEX_.md) `../stdlib/_INDEX_.md`
* [Input Functions](../stdlib//input.md) `../stdlib/input.md`
* [Type Conversion Functions](../stdlib/conversions.md) `../stdlib/conversions.md`
* [String Functions](../stdlib/string.md) `../stdlib/string.md`
* [Array Functions](../stdlib/array.md) `../stdlib/array.md`
* [Mathematical Functions](../stdlib/math.md) `../stdlib/math.md`

---

## Examples

Runnable examples for the language:

* [Examples](../../examples/)

---

## Release Notes

Current release:

* [Current Release](../releases/v0.7.0.md)
* [Release Notes](../releases/)

---

## Historical Specifications

Previous language specifications are preserved in the versioned documentation:

* [v0.1.md](v0.1.md)
* [v0.2.md](v0.2.md)
* [v0.3.md](v0.3.md)
* [v0.4.md](v0.4.md)
* [v0.5.md](v0.5.md)
* [v0.6.md](v0.6.md)
* [v0.7.md](v0.7.md)
