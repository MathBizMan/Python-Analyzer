array = list()
num = int(input("how many numbers to be added: "))
print("Enter the value: ")
for i in range(num):
  n= int(input("num: "))
  array.append(n)
print("List is:" , array)

Sum = 0
for n in array:
  Sum+= n
print ("Sum is:" ,Sum)

average = Sum/ num
print ("average is: ", average)

v= 0
for number in array:
  v += (number - average)*(number - average)
Variance = v/num
print ("Variance: ", Variance)

import math
print("Standard Deviation: ", math.sqrt(Variance))
