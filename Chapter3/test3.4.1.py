def sample_func(param1, param2, param3):
    print(f"{param1}, {param2}, {param3}")

def func_sum(*args):
    total = 0

    for arg in args:
        total += arg
    return total

def func_sum2(args2):

    return sum(args2)

sample_func(param1=1, param2=2, param3=3)
sample_func( param2=2, param3=3,param1=1)
sample_func( 2, 3,1)
sample_func(1, param3=2, param2=3)

args_p = [ x for x in range(10) ]

print(args_p)

print(func_sum(*args_p))

