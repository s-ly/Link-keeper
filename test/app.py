class A:
    def __init__(self, n):
        self.name = n
    
class B(A):
    def __init__(self, x, n):
        # super().__init__(n)
        self.age = x
    
a = A(n='abc')
print(a.name)
b = B('asd', 12)
print(b.name, b.age)