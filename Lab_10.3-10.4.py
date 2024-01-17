"""

Create a Python file named lab_10-3.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a function called double_stuff. The function should take a list as its only parameter.
When a list is passed as an argument to the function, the function should double each value in the list, regardless of its type
Write test cases to confirm that your function works when passed a list that:
Contains only integers
Contains integer and float values
Contains a combination of integer, string, and float values

_____________________________________________________________________________________________________________

Create a Python file named lab_10-4.py

Write a program that contains a function called indexed_names. 
The function should take a list of names as its only parameter.
When a list is passed as an argument to the function,
the function should return a new list where each value is replaced by the index, 
followed by a color, space, and the original value
i.e. passing through ["John", "Jane", "Bob"] 
would return ["0: John", "1: Jane", "2: Bob"]
Write 2 test cases to confirm that your function works when passed a list that:



"""
# Author: Alsir Elsheikh

def double_stuff(input_list):
    """
    Double each value in the input list.

    Parameters:
    - input_list (list): The list to be modified.

    Returns:
    - list: A new list containing doubled values.
    """
    return [2 * item for item in input_list]

# Test case 1: Contains only integers
int_list = [1, 2, 3, 4]
result_int = double_stuff(int_list)
print(f"Original List (Integers): {int_list}")
print(f"Doubled List: {result_int}")
print()

# Test case 2: Contains integer and float values
mixed_list = [1, 2.5, 3, 4.7]
result_mixed = double_stuff(mixed_list)
print(f"Original List (Mixed): {mixed_list}")
print(f"Doubled List: {result_mixed}")
print()

# Test case 3: Contains a combination of integer, string, and float values
mixed_types_list = [1, 'hello', 3.14, 5, 'world']
result_mixed_types = double_stuff(mixed_types_list)
print(f"Original List (Mixed Types): {mixed_types_list}")
print(f"Doubled List: {result_mixed_types}")

# Author: Alsir Elsheikh

def indexed_names(names_list):
    """
    Replace each value in the input list with its index, followed by a color, space, and the original value.

    Parameters:
    - names_list (list): The list of names to be processed.

    Returns:
    - list: A new list with formatted values.
    """
    return [f"{index}: {name}" for index, name in enumerate(names_list)]

# Test case 1
names_case1 = ["John", "Jane", "Bob"]
result_case1 = indexed_names(names_case1)
print(f"Original List (Case 1): {names_case1}")
print(f"Formatted List: {result_case1}")
print()

# Test case 2
names_case2 = ["Alice", "Charlie", "David"]
result_case2 = indexed_names(names_case2)
print(f"Original List (Case 2): {names_case2}")
print(f"Formatted List: {result_case2}")


