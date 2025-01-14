# Consonants Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Given a string, count the total number of consonants in the string. A consonant is an English alphabet character that is not a vowel (a, e, i, o, and u). Examples of consonants include b, c, d, g, and z. For this problem, consider the letter y to be a consonant.

For example, the string `"abc de"` has 3 consonants (b, c, and d), and the string `"d E hgjl iou"` has 5 consonants (d, h, g, j, and l).

### Additional Requirements

**Use recursion** to solve this problem. As a reminder, a recursive function is one that calls itself.

Note that this problem is *not* intrinsically well-suited to recursion. It is possible and more efficient to solve this problem without recursion, but the goal is to practice using recursion.

## Examples

### Example 1

```py
characters = "abc de"
consonant_count(characters)
```

Produces

```py
3
```

### Example 2

```py
characters = "D E H$GJL iou"
consonant_count(characters)
```

Produces

```py
5
```

### Example 3

```py
characters = "593   8fDk%@  #@d889  2dAjf"
consonant_count(characters)
```

Produces

```py
7
```

### Example 4

```py
characters = "AaEeIiOoUu"
consonant_count(characters)
```

Produces

```py
0
```

### Example 5

```py
characters = ""
consonant_count(characters)
```

Produces

```py
0
```
