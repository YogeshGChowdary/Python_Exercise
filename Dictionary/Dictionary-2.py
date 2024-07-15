# generating dictionary from two lists

fruits = ["apple", "banana", "cherry", "date"]
prices = [1.2, 0.5, 2.0, 3.0]

fruit_dict = {}  # Avoid using `dict` as a variable name since it's a built-in type

# Loop through indices of `fruits` list
for i in range(len(fruits)):
    fruit_dict[fruits[i]] = prices[i]

print(fruit_dict)