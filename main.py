def consonant_count(characters):
    pass


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
