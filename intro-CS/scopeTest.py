x = [1,2,3]

class SomeClass:
    def __init__(self):
        foo = 'sandwich'
        self.bar = 'bacon'

    def test1(self):
        print(x)
        
    def test2(self):
        print(self.bar)
    
    def test3(self):
        print(foo)
    	
    def test4(self):
	    print(self.foo)
        
def mystery(y):
    x[0] = y
    z = [4,5,6]

print(x)
mystery(7)
print(x)
print(z)

obj = SomeClass()
obj.test1()
obj.test2()
obj.test3()
obj.test4()
