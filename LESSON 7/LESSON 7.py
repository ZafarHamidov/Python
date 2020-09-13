a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(b, a - 1, -1):
    if ((i % 10 == c) or (i % 10 == d)):
        print(i, end=' ')      