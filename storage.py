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
    # goods_items = {}  # ИЛИ ТУТ ПРАВИЛЬНО ДЕЛАТ ПОЛЕ
    storage_quantity = 10

    def __init__(self):
        self.goods_items = dict()

    @classmethod
    def _get_total(cls):
        return cls.storage_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.storage_quantity = qnt

    @classmethod
    def get_free_space(cls):  # - вернуть количество свободных мест
        return cls.storage_quantity

    def add(self, name, qnt):
        if qnt < self._get_total():
            self.storage_quantity = (self.storage_quantity + qnt)
            self._set_total(self._get_total() + qnt)
        else:
            self._set_total(self._get_total() - self.storage_quantity)
            self.storage_quantity = 0

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

    def remove(self, name, qnt):
        if qnt < self.storage_quantity:
            self.storage_quantity = (self.storage_quantity - qnt)
            self._set_total(self._get_total() - qnt)
        else:
            self._set_total(self._get_total() - self.storage_quantity)
            self.storage_quantity = 0

        for key in self.goods_items.keys():
            if name == key:
                if self.goods_items[key] - qnt >= 0:
                    self.goods_items[key] = self.goods_items[key] - qnt
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} - нет на складе")

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.goods_items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        pass


if __name__ == '__main__':
    print("Всего на складе: ", Store.storage_quantity)

    # store = {"печенье": 5, "конфеты": 4, "халва": 3, "шоколад": 6, "мороженное": 2}
    warehouse = {"коробка": 30, "лента": 1, "скотч": 2, "бумага": 1, "пленка": 2}

    # storage = Shop()
    # for item, value in store.items():
    #     storage.add_item(item, value)

    stock = Store()
    for item, value in warehouse.items():
        stock.add(item, value)


    # stock = Store()
    # stock.add(warehouse)
    # stock.add('s', 2)
    # stock.add('sa', 1)
    # stock.add('sas', 1)
    print(stock.goods_items, 'lj')
    print("Число отгруженных товаров возросло до:", stock.storage_quantity)
    # print("Остаток на складе: ", storage.storage_quantity)
    # remove_stor = Store()
    # stock.remove("s", 2)
    print(stock.get_free_space(), 're')
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
