class Account :
    """
    Gives the Balance
    :parameter : None
    :rtype : None
    :type : int
    """
    def __init__(self):
        self._balance = 100

    @property
    def balance(self) -> int :
        return self._balance 

    @balance.setter
    def balance(self , n) : 
        if n < 0 :
            raise ValueError("Invalid amount!")
        self._balance = n


    def withdraw(self , n):
        self.balance -= n #self.balance = 80 this is when the maggic happpens

    def deposite(self , n) :
        self.balance += n 

account = Account()
print(account.balance)
account.withdraw(100)
print(account.balance)

help(Account)






#so this iss another program called meow in here it just shows the fundemental good luck 

#def meow(n : int) -> None: # instead of None could be int str what ever 
#                             This just shows the return type nothing else
#    for _ in range(n) :
#        print("Meow")


#number : int = int(input("Enter your number: "))
#meows : str = meow(number)
# The : indicates the type that's it!
#print(meows , end ="")


