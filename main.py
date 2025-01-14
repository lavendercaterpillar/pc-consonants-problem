def is_consonant(ch):
    ch = ch.upper()
    return (
        not (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U') 
        and ord(ch) >= 65 and ord(ch) <= 90
    )

def count_helper(characters, n):
    if n == 1:
        return 1 if is_consonant(characters[0]) else 0

    currentCharacterCount = 1 if is_consonant(characters[n - 1]) else 0
    
    return count_helper(characters, n - 1) + currentCharacterCount

def consonant_count(characters):
    if len(characters) < 1:
        return 0
    return count_helper(characters, len(characters))


### Test Case #1

characters = "abc de"

assert consonant_count(characters) == 3

### Test Case #2

characters = "D E H$GJL iou"

assert consonant_count(characters) == 5

### Test Case #3

characters = "593   8fDk%@  #@d889  2dAjf"

assert consonant_count(characters) == 7

### Test Case #4

characters = "AaEeIiOoUu"

assert consonant_count(characters) == 0

### Test Case #5

characters = ""

assert consonant_count(characters) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
