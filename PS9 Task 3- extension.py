payment1 = int(input("How much did the first customer pay?"))
payment2 = int(input("How much did the second customer pay?"))
class CashRegister:
    # Provides a sold product and the price for it, with the use of variables.
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        self._totalprice = 0
        self._change = 0.00
        self._change2 = 0.00
    # Calculates the new total price by adding the second item’s price.
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
        self._totalprice = int(self._totalPrice)
    # Returns the sum of prices in total.
    def getTotal(self):
        return self._totalPrice
    # Tells us the number in total of all sold items.
    def getCount(self):
        return self._itemCount
    # Clears(erases) all the registered data.
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
    # Excludes the pence from the price.      
    def getPounds(self):
        return self._totalprice
    # Calculates the change given to first cash register.
    def giveChange(self, payment):
        self._change = payment1 - (self._totalPrice)
        return self._change
    # Calculates the change given to second cash register.
    def giveChange2(self, payment):
        self._change2 = payment2 - self._totalPrice
        return self._change2

    
register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register2 = CashRegister()
register2.addItem(1.90)
register1.giveChange(payment1)
register2.giveChange2(payment2)

print("This is the number of items the first customer bought:")
print(register1._itemCount)
print("And this is how much it costed:")
print(register1._totalPrice)
print("Total price only pounds:")
print(register1._totalprice)
print("That is his change.")
print(register1._change)
print("This is the number of items the second customer bought:")
print(register2._itemCount)
print("And this is how much it costed:")
print(register2._totalPrice)
print("That is how much pounds:")
print(register2._totalprice)
print("That is his change.")
print(register2._change2)

