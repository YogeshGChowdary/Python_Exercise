# generate dictionary from two dictionaries

# Initial dictionaries
keys_dict = {
    "key1": "name",
    "key2": "age",
    "key3": "city"
}

values_dict = {
    "key1": "Alice",
    "key2": 30,
    "key3": "New York"
}

# Initialize an empty dictionary
new_dict = {}

# Populate the new dictionary using a loop
for key in keys_dict:
    new_dict[keys_dict[key]] = values_dict[key]

# Print the generated dictionary
print("Generated dictionary:", new_dict)