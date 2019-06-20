class A:
    def __init__(self):
        self.n = 2

    def add234(self, m):
        print("asddAA")


class C:
    def __init__(self):
        self.n = 2

    def add234(self, m):
        print("asddCC")

class D:
    def __init__(self):
        self.n = 2

    def add2345(self, m):
        print("asddD")


class B(A,C,D):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add234(m)
        self.n += 3


if __name__ == '__main__':
    b = B()
    b.add(2)
    print(b.n)