СПИСОК = []
СПИСОК.append("Zafar тоесть")
СПИСОК.append('я ЛЮБЛЮ ПИТОН')
СПИСОК.append('И НЕ ТОЛЬКО')
print(СПИСОК)

списгк = []
def add_gipo(x, списгк):
    списгк.append(x)

add_gipo("fd", списгк)
add_gipo("erf", списгк)
add_gipo("asdfsadef", списгк)
add_gipo("awerwer", списгк)
print(списгк)


print(СПИСОК+списгк)
списгк.extend(СПИСОК)
print(списгк)

СПИСОК.insert(2, 99)
print(СПИСОК)

СПИСОК.remove(99)
print(СПИСОК)

СПИСОК.clear()
print(СПИСОК)

копия=списгк.copy()
print(копия)
print(списгк)

копия.append("df")
u = копия.count(3)
print(u)

print(копия)

i=копия.index('Zafar тоесть')
print(i)

копия.pop(4)
print(копия)

копия.reverse()
print(копия)

копия.sort()
print(копия)
