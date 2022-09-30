vowels =0 
consonants = 0

for letter in "Test test tset":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants+1
        
print(vowels)
print(consonants)
        