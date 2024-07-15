# Adding a New Element at a Specific Position

# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Add a new element at a specific "position" (key)
my_dict['d'] = 4
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Replace an existing element at a specific "position" (key)
my_dict['c'] = 30
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 30, 'd': 4}

# Adding a new element at the "end"
my_dict['e'] = 5
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 30, 'd': 4, 'e': 5}

# List of dictionaries
list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Initialize an empty dictionary
my_dict = {}

# Add each dictionary in the list as a key-value pair in my_dict
for idx, d in enumerate(list_of_dicts):
    my_dict[idx] = d

print(my_dict)
#In this example, enumerate() is used to iterate over list_of_dicts, where each dictionary (d) is added to my_dict with its index (idx) from the list
{
    0: {'name': 'Alice', 'age': 30},
    1: {'name': 'Bob', 'age': 25}
}


# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Delete the key 'c' and its corresponding value
del my_dict['c']

print(my_dict)  # Output: {'a': 1, 'b': 2, 'd': 4}


# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Remove the key 'c' and its corresponding value
removed_value = my_dict.pop('c')

print(my_dict)        # Output: {'a': 1, 'b': 2, 'd': 4}
print(removed_value)  # Output: 3

