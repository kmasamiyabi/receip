def sample_func(a, b, c=None):

    if c is None:
        c = []

    c.append(a + b)
    return c

print(sample_func(1, 2))
print(sample_func(3, 5))
print(sample_func(7, 9))