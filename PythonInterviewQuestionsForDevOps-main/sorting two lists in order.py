a = [1, 5, 3, 9, 7]
b = [4, 2, 8, 6, 10]
c = []

# Merge and sort the lists
c.extend(a)
c.extend(b)

# Bubble sort algorithm to sort the merged list
n = len(c)
for i in range(n):
    for j in range(0, n-i-1):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]

print(c)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
