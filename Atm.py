class atm:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Total amount =",self.num1+self.num2)

    def sub(self):
        print("Balance amount =",self.num1-self.num2)


obj1=atm(120000,6000)
obj1.add()
obj1.sub()



