def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        # Return True if num is divisible by divisor and False otherwise
        return num % divisor == 0     
    else:
        # Raise an error if num and divisor are not numeric
        raise ValueError("Both num and divisor must be numeric")


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))