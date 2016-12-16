from cash import CashRegister


r1 = CashRegister() #default cash register
r2 = CashRegister(1,0.7) #cashregister with custom values 


print(r1.getCount())
print("test",r2.getTotal())
print("test",r2.getCount())

