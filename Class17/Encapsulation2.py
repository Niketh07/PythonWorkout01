class computer:
    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print("Selling price is ",format(self.__maxprice))
    
    def setmaxprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()

#changing the value of maxprice
c.__maxprice=1000
c.sell()

c.setmaxprice(2000)
c.sell()