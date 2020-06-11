class ClassTest(object):
    schema ={'a':'b'}
    
    def setUp(self):
        print('setUp')
        self.a = 4
    
    def method1(self):
        self.setUp()
        b = self.a**2
        self.a = b
        print(self.a)
    
    def method2(self):
        self.setUp()
        c = self.a**2
        self.a = c
        print(self.a)

    def method3(self, num):
        print(num**2)
