import random

print("Рандомайзер ZafarkiZefirki")
print()

connect = True

while connect == True:
    a = input("От: ")
    print()
    b = input("До: ")
    print()
    if b < a:
        print("Нельзя вводить во вторую строку цифры меньше чем в первой!")
        break

    finish = random.randint(int(a),int(b))

    print("Рандомное число: ", int(finish))
    print()

input()
