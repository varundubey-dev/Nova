# Type Conversion Functions

Type conversion functions convert values between NOVA's primitive datatypes.

---

## toString(value)

Converts a value to its string representation.

### Parameters

|  Name   | Type |    Description    |
|---------|------|-------------------|
| `value` | `U`  | Value to convert. |

### Returns

`S`

### Example

```nova
text: S = toString(25)

print(text)
```

Output:

```text
25
```

---

`toString()` accepts any NOVA value.

```nova
print(toString(true))

print(toString(null))
```

---

## toNumber(value)

Converts a string into a number.

### Parameters

|  Name   | Type |    Description     |
|---------|------|--------------------|
| `value` | `S`  | String to convert. |

### Returns

`N`

### Example

```nova
age: N = toNumber("19")

print(age)
```

Output:

```text
19
```

---

If the supplied string is not a valid numeric value, a runtime error is produced.

Example:

```nova
toNumber("hello")
```

Produces:

```text
Runtime Error: Invalid numeric conversion.
```

---

## toBoolean(value)

Converts a string into a boolean.

### Parameters

|   Name  | Type |    Description     |
|---------|------|--------------------|
| `value` | `S`  | String to convert. |

### Returns

`B`

### Example

```nova
flag: B = toBoolean("true")

print(flag)
```

Output:

```text
true
```

---

Accepted values are:

```text
true
false
```

Any other value produces a runtime error.

Example:

```nova
toBoolean("hello")
```

Produces:

```text
Runtime Error: Invalid boolean conversion.
```