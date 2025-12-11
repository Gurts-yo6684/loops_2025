# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
words = input("What is you favorite color?")
for letter in words:
    print(letter)
# Challenge:
# Count how many vowels are in the word.
vowels = "aeiouAEIOU"
count = 0
for letter in words:
    if letter in vowels:
        count+= 1
    print("number of vowles is", count)