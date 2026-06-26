# Mathematical Functions

Mathematical functions perform common numeric operations.

All functions in this module require:

```nova
import math
```

---

## math.abs(number)

Returns the absolute value of a number.

### Parameters

|   Name   | Type | Description  |
|----------|------|--------------|
| `number` | `N`  | Input value. |

### Returns

`N`

### Example

```nova
print(
    math.abs(-15)
)
```

Output

```text
15
```

---

## math.min(a, b)

Returns the smaller of two numbers.

### Parameters

| Name | Type |  Description  |
|------|------|---------------|
| `a`  | `N`  | First value.  |
| `b`  | `N`  | Second value. |

### Returns

`N`

### Example

```nova
print(
    math.min(
        5,
        10
    )
)
```

Output

```text
5
```

---

## math.max(a, b)

Returns the larger of two numbers.

### Parameters

| Name | Type |  Description  |
|------|------|---------------|
| `a`  | `N`  | First value.  |
| `b`  | `N`  | Second value. |

### Returns

`N`

### Example

```nova
print(
    math.max(
        5,
        10
    )
)
```

Output

```text
10
```

---

## math.pow(base, exponent)

Raises a number to a power.

### Parameters

|   Name     | Type |   Description   |
|------------|------|-----------------|
| `base`     | `N`  | Base value.     |
| `exponent` | `N`  | Exponent value. |

### Returns

`N`

### Example

```nova
print(
    math.pow(
        2,
        10
    )
)
```

Output

```text
1024
```

---

## math.sqrt(number)

Returns the square root of a number.

### Parameters

|  Name    | Type | Description |
|----------|------|-------------|
| `number` | `N`  | Input value.|

### Returns

`N`

### Example

```nova
print(
    math.sqrt(25)
)
```

Output

```text
5
```

---

## math.round(number)

Rounds a number to the nearest integer.

### Parameters

|   Name   | Type | Description |
|----------|------|-------------|
| `number` | `N`  | Input value.|

### Returns

`N`

### Example

```nova
print(
    math.round(4.7)
)
```

Output

```text
5
```

---

## math.floor(number)

Rounds a number downward to the nearest integer.

### Parameters

|   Name   | Type | Description |
|----------|------|-------------|
| `number` | `N`  | Input value.|

### Returns

`N`

### Example

```nova
print(
    math.floor(4.9)
)
```

Output

```text
4
```

---

## math.ceil(number)

Rounds a number upward to the nearest integer.

### Parameters

|   Name   | Type | Description |
|----------|------|-------------|
| `number` | `N`  | Input value.|

### Returns

`N`

### Example

```nova
print(
    math.ceil(4.1)
)
```

Output

```text
5
```

---

## math.random()

Returns a pseudo-random number.

### Parameters

None.

### Returns

`N`

### Example

```nova
print(
    math.random()
)
```

Example output

```text
0.734829517
```

The exact value returned is implementation-defined and will differ between calls.
