# 1

ismlar = ['name0']

ismlar.append('name1')
ismlar.append('name2')
ismlar.append('name3')

ismlar[0] = 'new_name'

"""keep the value, enter index"""
ismlar.pop(0)
"""deleting completely, enter index"""
del ismlar[-1]
"""deleting completely, enter value"""
ismlar.remove('name2')

yaqinlar = ismlar[:]
yaqinlar.append('Hoef')
yaqinlar.append('Lhiih')
yaqinlar.append('Ajww')
yaqinlar.sort()
print(yaqinlar)
print(ismlar)


nums = list(range(1, 101))
print(nums[::-1])
print(nums[:9])
print(nums[(len(nums) // 2 - 5):(len(nums) // 2 + 5)])
print(nums[-10:])

print()
sonlar = tuple(range(1, 10))
print(sonlar[4:7])
sonlar = list(sonlar)
sonlar[0] = 0
sonlar.append(12)
sonlar.remove(9)
sonlar = tuple(sonlar)
print()



talaba_baholari = {"Ali": {"Matematika": 5, "Ingliz tili": 4}}

talaba_baholari.update({"Firdavs": {"Matematika": 4, "Ingliz tili": 5}})
talaba_baholari.update({"Vali": {"Matematika": 4, "Ingliz tili": 4}})
talaba_baholari.update({"Talaba": {"Matematika": 2, "Ingliz tili": 3}})
print(talaba_baholari)

talaba_baholari.pop("Talaba")
print(talaba_baholari)

# pop ozida qiymatni ushlab turadi



for name, dict2 in talaba_baholari.items():
    s = 0
    a = 0
    for grades in dict2.values():
        s += 1
        a += grades
    print(f'{name} o\'rta bahosi {a / s}')

yangi_lugat = {
    "Ali": {"Matematika": 4, "Ingliz tili": 4},
    "Vali": {"Matematika": 2, "Ingliz tili": 3},
    "Zuhra": {"Matematika": 5, "Ingliz tili": 5},
    "Anvar": {"Matematika": 4, "Ingliz tili": 5}
}

new_dict = {}
for name, dict2 in yangi_lugat.items():
    s = 0
    a = 0
    for grades in dict2.values():
        s += 1
        a += grades
    print(f'{name} o\'rta bahosi {a / s}')
    if a / s >= 3:
        new_dict.update({name: dict2})
print('-' * 11)
print(new_dict)

bosgtoplam = set(range(10))
print(bosgtoplam)
bosgtoplam.pop()
bosgtoplam.remove(1)
bosgtoplam.discard(5)
print(bosgtoplam)

toplam_1 = {1, 2, 3, 4, 5}
toplam_2 = {4, 5, 6, 7, 8}

print(toplam_1.union(toplam_2))
print(toplam_1.intersection(toplam_2))
print(toplam_1.difference(toplam_2))
print(toplam_1.union(toplam_2))

print(toplam_1 == toplam_2)