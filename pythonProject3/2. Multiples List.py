factor = int(input())
count = int(input())


elements = []

for e in range(1, count+1):
    elements.append(e*factor)

print(elements)