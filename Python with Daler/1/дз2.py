dct = {"Name":"Zafar", "age":11, "national":"tajik", "weight":40}
print(dct)
dct2=dct.copy()
dct.clear()
print(dct)
print(dct2)

dct3 = dict.fromkeys(['one', 'two', 3], "ZafarMolodets_Avi_net")
print(dct3)

print(dct3.get(3))

en = {"apple":"яблоко","ant":"муравей"}
print(en.items())

print(en.keys())

print(en.values())

print(en.pop("apple"))
print(en)

en.update({'run': 'бежать','shoe': 'туфля'})
print(en)

en.popitem()
print(en)
en.popitem()
print(en)

dct3.setdefault("one", 1)
print(dct3)

dct3.setdefault("four", 4)
print(dct3)

dct3.setdefault("four", 5)
print(dct3)
