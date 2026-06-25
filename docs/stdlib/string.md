# String Functions

String functions operate on values of type `S`.

All string functions return new values and do not modify the original string.

---

## length(string)

Returns the number of characters in a string.

### Parameters

|   Name   | Type |        Description               |
|----------|------|----------------------------------|
| `string` | `S`  | String whose length is returned. |

### Returns

`N`

### Example

```nova
text: S = "Nova"

print(length(text))
```

Output:

```text
4
```

---

## upper(string)

Returns an uppercase copy of a string.

### Parameters

|   Name   | Type |    Description     |
|----------|------|--------------------|
| `string` | `S`  | String to convert. |

### Returns

`S`

### Example

```nova
print(
    upper("Nova")
)
```

Output:

```text
NOVA
```

---

## lower(string)

Returns a lowercase copy of a string.

### Parameters

|   Name   | Type |   Description      |
|----------|------|--------------------|
| `string` | `S`  | String to convert. |

### Returns

`S`

### Example

```nova
print(
    lower("NOVA")
)
```

Output:

```text
nova
```

---

## trim(string)

Removes leading and trailing whitespace.

### Parameters

|   Name   | Type |   Description   |
|----------|------|-----------------|
| `string` | `S`  | String to trim. |

### Returns

`S`

### Example

```nova
print(
    trim("   Nova   ")
)
```

Output:

```text
Nova
```

---

## contains(string, substring)

Returns whether a string contains another string.

### Parameters

|    Name     | Type |     Description      |
|-------------|------|----------------------|
| `string`    | `S`  | String to search.    |
| `substring` | `S`  | Value to search for. |

### Returns

`B`

### Example

```nova
print(
    contains(
        "Nova Language",
        "Language"
    )
)
```

Output:

```text
true
```

---

## startsWith(string, prefix)

Returns whether a string begins with the specified prefix.

### Parameters

|   Name   | Type |    Description    |
|----------|------|-------------------|
| `string` | `S`  | String to search. |
| `prefix` | `S`  | Prefix to test.   |

### Returns

`B`

### Example

```nova
print(
    startsWith(
        "Nova",
        "No"
    )
)
```

Output:

```text
true
```

---

## endsWith(string, suffix)

Returns whether a string ends with the specified suffix.

### Parameters

|   Name   | Type |   Description     |
|----------|------|-------------------|
| `string` | `S`  | String to search. |
| `suffix` | `S`  | Suffix to test.   |

### Returns

`B`

### Example

```nova
print(
    endsWith(
        "Nova",
        "va"
    )
)
```

Output:

```text
true
```

---

## replace(string, old, new)

Returns a copy of a string with every occurrence of a substring replaced.

### Parameters

|   Name   | Type |      Description       |
|----------|------|------------------------|
| `string` | `S`  | Source string.         |
| `old`    | `S`  | Substring to replace.  |
| `new`    | `S`  | Replacement substring. |

### Returns

`S`

### Example

```nova
print(
    replace(
        "Hello World",
        "World",
        "Nova"
    )
)
```

Output:

```text
Hello Nova
```

---

## split(string, delimiter)

Splits a string into an array of strings.

### Parameters

|    Name     | Type |           Description               |
|-------------|------|-------------------------------------|
| `string`    | `S`  | String to split.                    |
| `delimiter` | `S`  | Separator used to split the string. |

### Returns

`[S]`

### Example

```nova
parts: [S] = split(
    "A,B,C",
    ","
)

print(parts)
```

Output:

```text
[A, B, C]
```