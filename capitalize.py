"""Write a program that accepts a string as input, capitalizes the first letter of each
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming""""

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

print(capitalize_words("hi"))  # Output: "Hi"
print(capitalize_words("i love eating fish"))  # Output: "I Love eating fish "