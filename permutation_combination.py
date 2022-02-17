import math
#Taking iput from users
n = float(input("Please provie the n:"))
r = float(input("Please provide the r:"))
# calculate: nPr
print(n,r)
permutation = math.factorial(n)/math.factorial(n-r)
combination = math.factorial(n)/(math.factorial(n-r) * math.factorial(r))

print(f"Permutation is:{permutation} ")
print(f"Combination is: {combination}")
