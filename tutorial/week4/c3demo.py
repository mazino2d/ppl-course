class O:
    pass
class A(O):
    def foo(self):
        pass
class B(O):
    pass
class C(O):
    def foo(self):
        print("a")

class D(A,B):
    pass
class E(C,A):
    pass
# invalid
class F(D,B,E):
    pass
# valid
# class F(D,E,B):
#     pass
