num = int(input())
for i in range(2,num):
    if (num % i) == 0:
        print("composite")
        break
else:
    print("prime")