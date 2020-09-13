n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10 
if (n<1000):
    if ((b == c) and (c == d)):
        print('YES')    
    else:
        print('NO')    
elif n>=1000:
    if ((a == b) and (b == c) and (c != d)):
        print('YES')
    elif ((a != b) and (b == c) and (c == d)):
        print('YES')
    elif ((a == b) and (b != c) and (b == d)): 
        print('YES')
    elif ((a != b) and (a == c) and (c == d)): 
        print('YES')
    else:
        print('NO')         
else:
    print('NO') 
    

