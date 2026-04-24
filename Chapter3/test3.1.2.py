def divide(num1, num2):
    try:
        ans = num1 / num2
    except Exception as e:
        print(f"Exception class:{type(e)}")
        print(f"Exception occurred:{e}")
    else:
        print(f"計算結果は{ans}になります")
    finally:
        print("終了しました")



if __name__ == "__main__":
    divide(3, 0)
    divide(3, "a")
    divide(3, 2)
