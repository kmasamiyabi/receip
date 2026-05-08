
num = [x for x in range(10) if x % 2 == 0 ]

print(num)
print(sum(num))
print(sum(num, 100))

# def add(a, b):
#     return a + b

def add(a, b, c = 0):
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3))