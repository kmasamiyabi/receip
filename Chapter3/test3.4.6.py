def sample_func( name, **kwargs):
    print(f'{name}')

    for key, value in kwargs.items():
        print(f"{key}:{value}")

def sample_func2( dic_kwargs):
    for key, value in dic_kwargs.items():
        print(f"{key}:{value}")


# sample_func("john", age=30, email="john@example")
# sample_func("john", age=30, email="john@example")

dic = {
    "name":"john",
    "age":30,
    "email":"john@example"
}

sample_func2(dic)
# sample_func("hoge", **dic)

sample_func( **dic)