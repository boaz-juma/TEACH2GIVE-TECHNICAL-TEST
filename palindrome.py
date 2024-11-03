#Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def is_palindrome(text):
    """
    Checks if a given word or phrase is a palindrome.
    
    Args:
        text (str): The word or phrase to check.
    
    Returns:
        bool: True if the input is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the cleaned text is the same as its reverse
    return cleaned_text == cleaned_text[::-1]