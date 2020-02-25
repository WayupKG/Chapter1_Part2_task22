def gradus():
    fahrenheit = int(input("Фаренгейт - "))
    res = (fahrenheit - 32) / 1.8
    print("Цельсия - ", res)
gradus()


def gradus_2():
    celsius = int(input("Цельсия - "))
    res = celsius * 1.8 + 32
    print("Фаренгейт - ", res)
gradus_2()