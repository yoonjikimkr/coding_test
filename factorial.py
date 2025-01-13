def factorial(num): # 5*4*3*2*1 = num*(num-1)*(num-2)*...*1  fac=3*2*4*1  num 5 -i 1 = 4  
    for i in num:
        if i > num/2:
            fac = i*(num-i)*fac
    return fac*num
print(factorial(6))

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(5))  # Output: 120
