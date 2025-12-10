# ACCESS SPECIFIER : PUBLIC

class a:
    
    name = 'UNiK'
    
    def __init__(self):
        self.num = 0
        
    def dis(self):
        print(self.num)
        
    def modi_num(self,n):
        self.num = n

    @classmethod
    def dis_cls(cls):
        print(cls.name)
        
    @classmethod
    def modi_name(cls,n):
        cls.name = n

obj = a()

obj.modi_num(100)
obj.dis() # 100
obj.dis_cls() # UNiK
obj.modi_name('RohaN')
obj.dis_cls() # RohaN
