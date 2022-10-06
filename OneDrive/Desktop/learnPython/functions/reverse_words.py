def reverse():
    sentence = input("Please enter a sentence").strip()
    words = sentence.split()
    new_words = words[::-1]
    return new_words

print(reverse())