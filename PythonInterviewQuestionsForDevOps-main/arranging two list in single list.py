a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

c = []

index_a = 0
index_b = 0

while index_a < len(a) and index_b < len(b):
    c.append(a[index_a])
    c.append(b[index_b])
    index_a += 1
    index_b += 1

print(c)