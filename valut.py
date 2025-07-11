class Vault: 
    def __init__(self , g , s , k) :
        self.g = g 
        self.s = s
        self.k = k

    def __str__(self):
        return f"G: {self.g} , S:{self.s} , K:{self.k}"

        

    def __add__(self , other) : 
        G = self.g + other.g 
        S = self.s + other.s 
        K = self.k + other.k 
        return Vault(G  , S , L)


harry = Vault(100 , 50 , 25)
print(harry)

ron = Vault(25 , 50 , 100)
print(ron)

total = harry + ron
print(total)