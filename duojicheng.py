class A():
    def show(self):
        print("I come from class A")


class B(A):
    def show(self):
        print("I come from class B")


class C(A):
    def show(self):
        print("I come from class C")


class D(B, C):
    pass  # 占位作用不执行


d = D()
print(d.show())
