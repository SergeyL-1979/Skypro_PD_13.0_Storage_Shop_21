# -*- coding: utf-8 -*-
AMOUNT, WHERE = range(2)


class sklad:
    def __init__(self):
        self.dic = {}

    def add(self, name, amount):
        self.dic[name] = [amount, None]
        self.mwhere(name, amount)

    def mwhere(self, name, amount):
        if self.dic[name][AMOUNT] <= 0:
            self.dic[name][WHERE] = "missing"
        else:
            self.dic[name][WHERE] = amount

    def plus(self, name, p):
        self.dic[name][AMOUNT] += p
        self.mwhere(name, self.dic[name][AMOUNT])

    # def minus(self, name, m):
    #     self.dic[name][AMOUNT] -= m
    #     self.mwhere(name, self.dic[name][AMOUNT])

    def minus(self, name, m):
        if self.dic[name][AMOUNT] >= m:
            self.dic[name][AMOUNT] -= m
            self.mwhere(name, self.dic[name][AMOUNT])
        else:
            print("Не хватает товара")  # В 3 ветке print("Не хватает товара")
        # также можно сделать генерацию исключения
        # else:
        # raise TypeError("Не хватает товара")


class sk:
    def __init__(self):
        self.d = {}
    def add(self, obj, name): # задаём в качестве obj оъект класса sklad
        self.d[name] = obj
    def scan(self, name):
        return self.d[name] # и дальше делаем с этим объектом что надо



if __name__ == '__main__':
    # mysklad = sk()
    # mysklad.add(sklad("Mandarin", 50), 'm1')
    # print(mysklad.scan('m1').what)  # в 3 ветке print(mysklad.scan('m1').what)

    m = sklad()
    m1, m2, m3 = "Mandarin", "pepsi", "kirpich"
    m.add(m1, 50)
    m.add(m2, 300)
    m.add(m3, 50)
    print(m1, m.dic[m1][WHERE], '\n', m2, m.dic[m2][WHERE], '\n', m3, m.dic[m3][WHERE])
    # В ветке 3:
    # print(m1, m.dic[m1][WHERE], '\n', m2, m.dic[m2][WHERE], '\n', m3, m.dic[m3][WHERE])