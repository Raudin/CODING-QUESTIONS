# Function to check palindrome
def is_palindrome(string):
    # Converting the string to lowercase and removing spaces
    string = string.lower().replace(" ", "")
    # Reversing the string
    reverse_string = string[::-1]
    # Comparing the original and reversed string
    if string == reverse_string:
        return True
    else:
        return False

# Taking input from user
string = input("Enter a string: ")

# Checking if the string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")