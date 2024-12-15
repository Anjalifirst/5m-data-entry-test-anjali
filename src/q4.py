def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if variable s is a string
    if isinstance(s, str):
        # Reverse the given string
        return s[::-1]
    
    return ''


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World"))
print(string_reverse("Python"))