#a = 5
#b = 8

#if a > b:
    #print("a is greater than b")
#elif b > a:
   # print("b is greater than a or a and b are equal")
#elif a == b:
   # print("a is equall to b")

#data = [1.6, 3.4, 5.5, 9.4 ]
#cars = ["Volvo", "Tesla", "Ford"]

#data.insert(4, 6)
#cars.clear()
#N = len(data)
#M = len(cars)
#print(N)
#print(M)

#X = cars[2]
#print(data[2])
#data[2] = 7.3
#print(data[2])
#start = 3
#stop = 12
#step = 3

#data = [1, 5, 6, 3, 12, 3]
#sum = 0
#for i in data:
#    sum += i
#print(sum) 

#N = len(data)
#mean = sum/N
#print(int(mean))






N = 4
fib1 = 1
fib2 = 0
#print(fib1)
#print(fib2)

for i in range(N):
   fib_next = fib2 + fib1
   fib1 = fib2
   fib2 = fib_next
   print(fib_next)