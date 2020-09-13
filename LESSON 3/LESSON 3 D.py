x = int(input())
y = int(input())
z = int(input())
if ((x < y < z) or (x < z < y)):
    print(x)
elif ((y < x < z) or (y < z < x)):
    print(y)
else:
    print(z)
    
    x = int(input())
    y = int(input())
    z = int(input())
    lst = [x,y,z]
    print(min(lst))