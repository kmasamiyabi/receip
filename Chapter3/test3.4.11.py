def sample_func(a, b, c=None):

    if c is None:
        c = []

    c.append(a + b)
    return c

l = sample_func(1, 2)
print(l)

l = sample_func(3, 5, l)
print(l)

l = sample_func(7, 9, l)
print(l)

l = sample_func(1, 2, l)
print(l)

l = sample_func(5, 9, l)
print(l)


