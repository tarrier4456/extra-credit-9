def fact(x):
    n=1
    for i in range(1,x+1):
         n = (n*i)
    return n         
print(fact(20))