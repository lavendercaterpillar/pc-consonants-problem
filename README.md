# Consonants Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Given a string, count the total number of consonants in the string. A consonant is an English alphabet character that is not a vowel (a, e, i, o, and u). Examples of consonants include b, c, d, g, and z. For this problem, consider the letter y to be a consonant.

For example, the string `"abc de"` has 3 consonants (b, c, and d), and the string `"d E hgjl iou"` has 5 consonants (d, h, g, j, and l).

### Additional Requirements

**Use recursion** to solve this problem. As a reminder, a recursive function is one that calls itself.

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

## Notes for the Interviewer

### Clarifying Questions

#### Q: Are the characters in the string guaranteed to be upper or lower case?

A: No, the characters may be of mixed case (either upper case or lower case).

#### Q: Will there be any other kinds of characters present in the string?

A: Yes, the string may contain special characters such as numbers, spaces, dollar signs ($), octothorpe (#), etc.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate struggles writing a recursive function, ask how they would implement the function iteratively.

- If your candidate still struggles, suggest to them the use of the `ord` function in python. This function can be used to determine the unicode value of a character.

- Inform the candidate that the unicode value of uppercase letters is 65 -> 90 (letter A is 65 and letter Z is 90) and the unicode value of lowercase letters is from 97 to 122 (letter a is 97 and letter z is 122).

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of the sample solution?

- If you wrote the function with a chain of if statements (checking for each type of consonant), try using the ord() function to complete the challenge.

- If you wrote the function iteratively, try writing the function recursively.
