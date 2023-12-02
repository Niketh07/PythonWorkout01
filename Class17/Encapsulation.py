class computer:
    def __init__(self):
        self._maxprice=900

    def sell(self):
        print("Selling price is ",format(self._maxprice))
    
    def setmaxprice(self,price):
        self._maxprice=price
c=computer()
c.sell()

#changing the value of maxprice
c._maxprice=1000
c.sell()

c.setmaxprice(2000)
c.sell()