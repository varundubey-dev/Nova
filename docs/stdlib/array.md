# Array Functions

Array functions operate on NOVA arrays.

Functions that modify an array perform the operation in-place.

---

## length(array)

Returns the number of elements in an array.

### Parameters

|  Name   | Type  |       Description               |
|---------|-------|---------------------------------|
| `array` | `[U]` | Array whose length is returned. |

### Returns

`N`

### Example

```nova
numbers: [N] = [
    1,
    2,
    3
]

print(
    length(numbers)
)
```

Output

```text
3
```

---

## push(array, value)

Appends a value to the end of an array.

The supplied value must match the array's element datatype.

### Parameters

|   Name  | Type  |   Description    |
|---------|-------|------------------|
| `array` | `[U]` | Array to modify. |
| `value` | `U`   | Value to append. |

### Returns

`null`

### Example

```nova
numbers: [N] = [
    1,
    2,
    3
]

push(
    numbers,
    4
)

print(numbers)
```

Output

```text
[1, 2, 3, 4]
```

---

## pop(array)

Removes and returns the last element of an array.

### Parameters

|  Name   | Type  |    Description   |
|---------|-------|------------------|
| `array` | `[U]` | Array to modify. |

### Returns

`U`

### Example

```nova
numbers: [N] = [
    1,
    2,
    3
]

value: N = pop(numbers)

print(value)

print(numbers)
```

Output

```text
3
[1, 2]
```

---

## insert(array, index, value)

Inserts a value at the specified index.

The supplied value must match the array's element datatype.

### Parameters

|   Name  | Type  |      Description            |
|---------|-------|-----------------------------|
| `array` | `[U]` | Array to modify.            |
| `index` | `N`   | Zero-based insertion index. |
| `value` | `U`   | Value to insert.            |

### Returns

`null`

### Example

```nova
numbers: [N] = [
    1,
    3
]

insert(
    numbers,
    1,
    2
)

print(numbers)
```

Output

```text
[1, 2, 3]
```

---

## remove(array, index)

Removes the element at the specified index.

### Parameters

|  Name   | Type  |    Description    |
|---------|-------|-------------------|
| `array` | `[U]` | Array to modify.  |
| `index` | `N`   | Zero-based index. |

### Returns

`null`

### Example

```nova
numbers: [N] = [
    1,
    2,
    3
]

remove(
    numbers,
    1
)

print(numbers)
```

Output

```text
[1, 3]
```

---

## contains(array, value)

Returns whether an array contains the supplied value.

### Parameters

|  Name   | Type  |   Description    |
|---------|-------|------------------|
| `array` | `[U]` | Array to search. |
| `value` | `U`   | Value to locate. |

### Returns

`B`

### Example

```nova
numbers: [N] = [
    1,
    2,
    3
]

print(
    contains(
        numbers,
        2
    )
)
```

Output

```text
true
```

---

## clear(array)

Removes every element from an array.

### Parameters

|  Name   | Type  |   Description   |
|---------|-------|-----------------|
| `array` | `[U]` | Array to clear. |

### Returns

`null`

### Example

```nova
numbers: [N] = [
    1,
    2,
    3
]

clear(numbers)

print(numbers)
```

Output

```text
[]
```