class User():
    
    def __init__(self,name,gender,salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        
        
    def showdetails(self):
        print(self.name)
        print(self.gender)
        print(self.salary)
        





class Bank(User):
    usercount = 0
    __balance = 0
    def __init__(self,name,gender,salary):
        super().__init__(name,gender,salary)
        #self.__balance=self.salary
        Bank.usercount += 1
        

    def deposit(self,amount):
        self.amount = amount
        self.__balance+=self.amount


    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.__balance):
            print(f"Insuffient balance\n Current Balance{self.__balance}")
        elif(self.amount >= 100 and self.amount <= self.__balance):
            print("Thank u for visiting again")
            self.__balance -= self.amount
            print(f"Current balance :{self.__balance}")
        else:
            print("You cannot withdraw less than 100")

    def viewbalance(self):
        print(self.name.title())
        print(f"Account no :{self.usercount}")
        print(self.__balance)

    def transfer(self,user,amount):
        self.amount = amount
        if(self.amount > self.__balance):
            print(f"Insuffient balance\n Current Balance:{self.__balance}")

        elif(1<=self.amount<=self.__balance):
            user.__balance+=self.amount
            self.__balance-=self.amount
            print("Transaction succefull ")
            print(f"Current Balance{self.__balance}")

        else:
            print(f"You cannot transfer amount less than 1 Current Balance{self.__balance}")
            
        
        
        
        
        
        
        
