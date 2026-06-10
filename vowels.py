sentence = input("\nEnter the sentence or word to find total numbers of vowels and consonent: ")

# 1. Define vowels as a clean string or set (no commas needed)
vowels = "aeiouAEIOU"
consonent = "qwrtypsdfghjklzxcvbnmQWRTYSDFGHJKLZXCVBNM"

# 2. Use a loop to count each time a character matches a vowel
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("\nTotal num of vowels in the above sentence are:", count)

count = 0
for character in sentence:
    if character in consonent:
        count += 1

print("\nTotal num of consonent in the above sentence are:", count)

