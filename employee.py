class person :
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber

    def display (self):
        print (self.name)
        print (self.idnumber)

class employee (person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post

        person.__init__(self,name,idnumber)

    def display_new (self):
        print(self.salary)
        print(self.post)

obj1=employee("Harsh",5879,250000,"CEO")
obj1.display()
obj1.display_new()

