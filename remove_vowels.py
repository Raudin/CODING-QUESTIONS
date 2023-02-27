# Function to remove vowels from string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    # Using list comprehension to remove vowels
    new_string = "".join([char for char in string if char not in vowels])
    return new_string

# Taking input from user
string = input("Enter a string: ")

# Printing the string with vowels removed
print("The string with vowels removed is:", remove_vowels(string))