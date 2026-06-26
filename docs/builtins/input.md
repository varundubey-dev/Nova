# Input Functions

Input functions read values from standard input.

---

## input(prompt?)

Reads a line of text from standard input.

If a prompt is provided, it is displayed before waiting for input.

### Parameters

|   Name   | Type |                 Description                      |
|----------|------|--------------------------------------------------|
| `prompt` | `S`  | Optional message displayed before reading input. |

### Returns

`S`

### Example

```nova
name: S = input("Enter your name: ")

print(name)
```

Example interaction:

```text
Enter your name: Varun
```

Output:

```text
Varun
```

---

The prompt parameter is optional.

```nova
name: S = input()

print(name)
```

---

## Note

`input()` always returns a value of type `S`, regardless of the entered text.

To use the input as another datatype, convert it explicitly.

```nova
age: N = toNumber(
    input("Enter your age: ")
)

print(age)
```

---

Input may be used anywhere an expression is allowed.

```nova
print(
    upper(
        input("Enter your name: ")
    )
)
```