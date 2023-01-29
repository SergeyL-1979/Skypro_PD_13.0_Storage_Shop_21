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
        self.storage_quantity = 100

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.storage_quantity - sum(self.goods_items.values())

    def add(self, name, qnt):
        if self.get_free_space() >= qnt:
            if name not in self.goods_items.keys():
               self.goods_items[name] = qnt
               print(f"Добавлено {qnt} {name.title()}")
        else:
            print("Склад переполнен!!!")

    def remove(self, name, qnt):
        if name not in self.goods_items:
            print(f"{name.title()} - нет на складе")
        elif self.goods_items[name] - qnt < 0:
            print(f"Слишком мало {name}")
        else:
            self.goods_items[name] = self.goods_items[name] - qnt
            print(f"Добавлено курьеру: {qnt} {name.title()}")

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.goods_items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        return len(self.goods_items)


class Shop(Store):

    items = 5
    capacity = 100

    def add(self, name, qnt):  # - увеличивает запас items с учетом лимита capacity
        if self.get_free_space() >= self.items:
            if name not in self.goods_items.keys():
                self.goods_items[name] = qnt
                print(f"Добавлено {qnt} {name.title()}")
        else:
            print("Магазин переполнен!!!")

    def remove(self, name, qnt):  # - уменьшает запас items, но не ниже 0
        if name not in self.goods_items:
            print(f"{name.title()} - нет в магазине")
        elif self.goods_items[name] - qnt < 0:
            print(f"Слишком мало {name}")
        else:
            self.goods_items[name] = self.goods_items[name] - qnt
            print(f"Добавлено курьеру: {qnt} {name.title()}")

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.capacity - sum(self.goods_items.values())

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.goods_items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        return len(self.goods_items)


if __name__ == '__main__':
    # stock = Store()
    # print("Всего на складе места для хранения: ", stock.get_free_space())
    # warehouse = {"коробка": 5, "лента": 5, "скотч": 5, "бумага": 3, "пленка": 5}
    # for item, value in warehouse.items():
    #     stock.add(item, value)
    #
    # print(stock.goods_items, 'if main')
    # print("Число наименования товаров на складе:", stock.get_unique_items_count())
    # print("Остаток мест на складе: ", stock.get_free_space())
    #
    # stock.remove('коробка', 1)
    # print("***", stock.goods_items)
    # print("Остаток мест на складе: ", stock.get_free_space())
    # print("Число отгруженных товаров сократилось до:", stock.goods_items)
    # print("Остаток на складе: ", remove_stor.storage_quantity)
    # print(remove_stor.get_free_space())

    store = {"печенье": 1, "конфеты": 10, "халва": 10, "шоколад": 1, "мороженное": 1, "big": 10}
    storage = Shop()
    for item, value in store.items():
        storage.add(item, value)

    print(f"Список товара в магазине: {storage.get_items()}")
    print(f"Товара в магазине: {storage.get_unique_items_count()}")
    print(f'Свободно в магазине мест: {storage.get_free_space()}')


    # foods_d = dict()
    # foods_d['any_key'] = 1
    # foods_d['eshe_key'] = 2
    # print(foods_d)