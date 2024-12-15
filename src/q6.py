def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Initialize the index 
    index = 0
    #Iterate through the list and find the first negaive number
    while index < len(lst):       
        if lst[index] < 0:  
            # Return the fist negaive number if found
            return lst[index]
        else:
            # if negative number is not found, increase the index by one
            index += 1
    # Return "No negatives" if there are no negative numbers in the list
    return "No negatives"
       
    
# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))