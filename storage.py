#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Storage(ABC): # Нужно ли сюда делать наследование от ABC?
    @abstractmethod
    def add(self, name, qnt):
        pass
    @abstractmethod
    def remove(self, name, qnt):
        pass
    @abstractmethod
    def get_free_space(self):
        pass
    @abstractmethod
    def get_items(self):
        pass
    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):

    def __init__(self):
        self.goods_items = dict()
        self.storage_quantity = 10

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.storage_quantity - sum(self.goods_items.values())

    def add(self, name, qnt):
        # if qnt < self._get_total():
        #     self.storage_quantity = (self.storage_quantity + qnt)
        #     self._set_total(self._get_total() + qnt)
        #     print(name, qnt)
        #     print(self._get_total())
        #     print(self.storage_quantity)
        # else:
        #     self._set_total(self._get_total() - qnt)
        #     self.storage_quantity = 0
        is_found = False
        if self.get_free_space() > qnt:
            for key in self.goods_items.keys():
                if name == key:
                    self.goods_items[key] = self.goods_items[key] + qnt
                    is_found = True
            if not is_found:
                self.goods_items[name] = qnt
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")
        # pass

    def remove(self, name, qnt):
        if name not in self.goods_items:
            print(f"{name.title()} - нет на складе")
        elif self.goods_items[name] - qnt < 0:
            print(f"Слишком мало {name}")
        else:
            self.goods_items[name] = self.goods_items[name] - qnt
            print(f"Добавлено {qnt} {name.title()}")

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.goods_items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        return len(self.goods_items)


if __name__ == '__main__':
    store = Store()
    print("Всего на складе: ", store.get_free_space())

    # store = {"печенье": 5, "конфеты": 4, "халва": 3, "шоколад": 6, "мороженное": 2}
    warehouse = {"коробка": 30, "лента": 1, "скотч": 2, "бумага": 1, "пленка": 2}

    # storage = Shop()
    # for item, value in store.items():
    #     storage.add_item(item, value)

    stock = Store()
    for item, value in warehouse.items():
        stock.add(item, value)
    # stock.add('s', 2)
    # stock.add('sa', 1)
    # stock.add('sas', 1)
    print(stock.goods_items, 'lj')
    print("Число отгруженных товаров возросло до:", stock.storage_quantity)
    # print("Остаток на складе: ", storage.storage_quantity)
    # remove_stor = Store()
    # stock.remove("s", 2)
    # print(stock.get_free_space(), 're')
    # stock.remove('коробка', 1)
    # print(stock.goods_items)
    # print(stock.get_free_space())
    # print("Число отгруженных товаров сократилось до:", stock.storage_quantity)
    # print("Остаток на складе: ", remove_stor.storage_quantity)
    # print(remove_stor.get_free_space())

    # foods_d = dict()
    # foods_d['any_key'] = 1
    # foods_d['eshe_key'] = 2
    # print(foods_d)