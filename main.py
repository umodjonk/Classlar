class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
talaba0=User(1,'Shahzod')

class Talaba(User):
    def __init__(self,id,name,age,tel):
        self.age=age
        self.tel=tel
        super().__init__(id,name)
talaba=Talaba(1,'Odil',12,213)

print(talaba.id)
print(talaba0.name)
print(talaba.age)
print(talaba.tel)