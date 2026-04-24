def raise_exception_group():
    excs = [ValueError("値が範囲外です"), TypeError("文字列は指定出来ません")]
    raise Exception("検証エラー",excs)


try:
    raise_exception_group()
except Exception as e:
    print(f"補足したエラー：{type(e).__name__}")
    print(f"メッセージ：{e}")
    print("含まれる例外:")
    for ex in e.exceptions:
        print(f" - {type(ex).__name__}: {ex}")