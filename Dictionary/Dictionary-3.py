# generating dicitionary form list and dictionary

# List of keys
keys_list = ["key1", "key2", "key3"]

# Dictionary of values
values_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Initialize an empty dictionary
result_dict = {}

# Populate the result dictionary using a loop
for key in keys_list:
    if key in values_dict:
        result_dict[key] = values_dict[key]

# Print the generated dictionary
print("Generated dictionary:", result_dict)