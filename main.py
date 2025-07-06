# def consonant_count(characters):
#     VOWELS = {'a','e','i','o','u'}
#     result = 0

#     for char in characters:
#         if char.lower().isalpha() and char.lower() not in VOWELS:
#                 result += 1
    
#     print(result)
#     return result

# ********************************
# ********** Recursion ***********
# ********************************
def consonant_count(characters):
    VOWELS = {'a','e','i','o','u'}

    if len(characters) == 0:
            return 0
        
    if characters[0].lower().isalpha() and characters[0].lower() not in VOWELS:
        return consonant_count(characters[1:])+1
    return consonant_count(characters[1:])

### Test Case #1

characters = "abc de"
print(consonant_count(characters))
assert consonant_count(characters) == 3

# ### Test Case #2

# characters = "D E H$GJL iou"
# assert consonant_count(characters) == 5

# ### Test Case #3

# characters = "593   8fDk%@  #@d889  2dAjf"
# assert consonant_count(characters) == 7

# ### Test Case #4

# characters = "AaEeIiOoUu"
# assert consonant_count(characters) == 0

# ### Test Case #5

# characters = ""

# assert consonant_count(characters) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
