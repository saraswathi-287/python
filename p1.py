'''n = int(input())
for i in range(10,n+8):
    print("* "*i)'''

''''n = int(input())
for i in range(1,n+1):
    str1=''
    for j in range(1,i+1):
        str1=str1+str(j)+" "
    print(str1)'''
'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)'''
'''n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*i)
    else:
        print("*"+" "*(2*i-3)+"*")'''

n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*i)
    else:
        print(" "+"* "*(2*i-3)+"*")

