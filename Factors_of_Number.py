## FACTORS OF A NUMBER
#Approach 1
n = 15
num = n
factors = []
for i in range(1, num // 2 ):
  if num % i == 0:
    factors.append(i)
factors.append(num)
print(factors)
  



  
