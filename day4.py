''''n = int(input())

for i in range(1,n+1):
    if i==1 or i==n:
        print(" "*(n-i)+"* "*i)
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")'''
'''n = int(input())
str1=""
for j in range(1,i+1):
    if i==1 or i==n:
        print(" "*(n-i)+"* "*i)
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")'''
n= str(input())
s = 0
power = len(n)
for i in n:
    s+= int(i)**power

if s==int(n):
    print("is amstrong")
else:
    print("not amstrong")