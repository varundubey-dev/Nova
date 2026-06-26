# NOVA Language Specification

### Current Version (v0.9)

This document describes the current stable version of NOVA.

The language syntax is defined by **NOVA v0.9**, which introduces NOVA's first module system with imports, exports, and importable Standard Library modules.

Historical specifications remain available in the versioned documentation.

---

## Language Versions

| Version            | Documentation               |
| ------------------ | --------------------------- |
| **Current (v0.9)** | This document               |
| v0.9               | [NOVA v0.9 Syntax](v0.9.md) |
| v0.7               | [NOVA v0.7 Syntax](v0.7.md) |
| v0.6               | [NOVA v0.6 Syntax](v0.6.md) |
| v0.5               | [NOVA v0.5 Syntax](v0.5.md) |
| v0.4               | [NOVA v0.4 Syntax](v0.4.md) |
| v0.3               | [NOVA v0.3 Syntax](v0.3.md) |
| v0.2               | [NOVA v0.2 Syntax](v0.2.md) |
| v0.1               | [NOVA v0.1 Syntax](v0.1.md) |

---

## Language Syntax

The current NOVA syntax is defined by:

* [NOVA v0.9 Language Specification](v0.9.md)

---

## Built-in Functions

NOVA provides globally available built-in functions for commonly used operations. These functions are available without imports.

Documentation:

* [Built-in Functions Index](../builtins/_INDEX_.md)
* [Input Functions](../builtins/input.md)
* [Type Conversion Functions](../builtins/conversions.md)
* [String Functions](../builtins/string.md)
* [Array Functions](../builtins/array.md)

---

## Standard Library

The Standard Library provides importable modules that extend the core language.

Current modules:

* [Standard Library Index](../stdlib/_INDEX_.md)
* [Mathematics Module](../stdlib/math.md)

---

## Current Features

### Primitive Types

* Numbers (`N`)
* Strings (`S`)
* Booleans (`B`)
* Any (`U`)

### Variables

* Mutable variables
* Immutable constants
* Deferred initialization
* Runtime datatype validation

### Expressions

* Arithmetic
* Comparison
* Equality
* Logical
* Unary
* Parenthesized expressions
* Ternary expressions

### Collections

* Arrays
* Typed arrays
* Multi-type arrays
* Nested arrays
* Array indexing
* Array mutation

### Schema Maps

* Schema declarations
* Map instances
* Optional properties
* Nested schemas
* Arrays of maps
* Property access
* Property mutation
* Runtime schema validation

### Control Flow

* `if`
* `else`
* `else if`
* Block scope
* Variable shadowing

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

### Built-in Functions

* Input functions
* Type conversion functions
* String functions
* Array functions

### Modules

* Module imports
* Selective imports
* Multiline imports
* Module aliases
* Exported variables
* Exported constants
* Exported functions
* Exported schemas
* Hierarchical module paths
* Module resolution
* Circular import detection

### Standard Library

* Importable modules
* Mathematics module

---

## Examples

Runnable examples:

* [Examples](../../examples/)

---

## Release Notes

Current release:

* [NOVA v0.9.0 Release Notes](../releases/v0.9.0.md)
* [Release Notes](../releases/)

---

## Historical Specifications

Previous language specifications are preserved for historical reference.

* [v0.1](v0.1.md)
* [v0.2](v0.2.md)
* [v0.3](v0.3.md)
* [v0.4](v0.4.md)
* [v0.5](v0.5.md)
* [v0.6](v0.6.md)
* [v0.7](v0.7.md)
* [v0.9](v0.9.md)