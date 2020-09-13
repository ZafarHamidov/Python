dec = int(input())
first = dec % 10
dec = dec // 10
second = dec % 10
dec = dec // 10
dec = (dec * 10 + first) * 10 + second
print(dec)
