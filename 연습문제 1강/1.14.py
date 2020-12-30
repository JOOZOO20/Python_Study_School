def fac(n):
    result=1
    for i in range(n,0,-1):
        result*=i
    return result
print(fac(3))
print(fac(5))
print(fac(12))
print(fac(20))