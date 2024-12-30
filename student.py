class person :
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

class student (person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year

obj1=student("Harsh","Mulchandani",2026)
obj1.printname()
print(obj1.year)
