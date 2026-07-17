class A:
    label = "A - Base Class"


class B(A):
    label = "B - Ginger Chai"


class C(A):
    label = "C - Lemon Chai"


class D(C, B):
    pass


test = D()
print(test.label)
test2 = B()
print(test2.label)
