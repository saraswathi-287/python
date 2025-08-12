''''def is_prime(m):
    is_prime = True
    if m <=1:
        is_prime=False
    else:
        for i in range(2,int(m**0.5)+1):
            if m%i==0:
                is_prime = False
                break
    if is_prime:
        print(m,"is a prime")

m= int(input())
for i in range(1,m+1):
    is_prime(i)'''
'''def right_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()'''
 ''' def inverted_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print() ''''

def pyramid_pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print() 