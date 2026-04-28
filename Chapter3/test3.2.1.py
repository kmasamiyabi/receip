class MyOpenContextManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print("__enter__:ファイルをOpenします")
        self.file_obj = open(self.file_name, 'r')
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("__exit__:ファイルをCloseします")
        self.file_obj.close()


if __name__ == '__main__':
    with MyOpenContextManager("python.txt") as f:
        print(f.read())
