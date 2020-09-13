n = int(input())
if (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0):
    print(0)
elif (n % 2 == 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0):
    print(1)
elif (n % 2 == 0) and (n % 3 == 0):
    print(2)