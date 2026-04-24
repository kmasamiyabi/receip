# Exceptionクラスを継承する
class MyError(Exception):
    pass

def divide(a, b):
    ans = a / b
    return ans



if __name__ == "__main__":
    try:
        # x = divide(3, 4)
        # x = divide(3, 0)
        x = divide(3, "zero")

    except Exception as e:
        print(e)
    else:
        print(f"計算結果：{x}")


