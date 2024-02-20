class A:
    def display(self):
        print("Class A")


class X(A):
    def display(self):
        print("Class X Display")


class Y(A):
    def display(self):
        print("Class Y Display")


class Z(Y, X):
    pass


obj = Z()
obj.display()

