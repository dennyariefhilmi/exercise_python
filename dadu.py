from itertools import count
from operator import index
import random


putaran = int(input("Masukkan jumlah putaran : "))
mylist = [1,2,3,4,5,6]
results = []
ganjil = []
genap = []
for i in range (0,putaran):
    dadu = random.randint(1,6)
    print("Putaran ke-",i+1," adalah : ",dadu,"Total : ",dadu)
    results.append(dadu)
print("Peluang angka 1 adalah",results.count(1),"/",i+1,"=",round(results.count(1)/i,2),"%")
print("Peluang angka 2 adalah",results.count(2),"/",i+1,"=",round(results.count(2)/i,2),"%")
print("Peluang angka 3 adalah",results.count(3),"/",i+1,"=",round(results.count(3)/i,2),"%")
print("Peluang angka 4 adalah",results.count(4),"/",i+1,"=",round(results.count(4)/i,2),"%")
print("Peluang angka 5 adalah",results.count(5),"/",i+1,"=",round(results.count(5)/i,2),"%")
print("Peluang angka 6 adalah",results.count(6),"/",i+1,"=",round(results.count(6)/i,2),"%")


    

    


    
    