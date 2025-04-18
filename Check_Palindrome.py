:::: CHECK PALINDROME ::::

n = 1234

num = n # TO KEEP THE INPUT SAFE 
result = 0
while num > 0:
  ld = num % 10
  result = (result * 10) + ld 
	num = num // 10 #to get floor division
return n == result
