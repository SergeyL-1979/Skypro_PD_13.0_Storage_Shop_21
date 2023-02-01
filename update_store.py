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

    def __init__(self, goods_items: dict, capacity=100):
        self.__items = goods_items
        self.__capacity = capacity

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.__capacity - sum(self.__items.values())

    def add(self, name, qnt):
        if self.get_free_space() >= qnt:
            if name not in self.__items.keys():
               self.__items[name] = qnt
               print(f"Добавлено {qnt} {name.title()}")
        else:
            print("Склад переполнен!!!")

    def remove(self, name, qnt):
        if name not in self.__items:
            print(f"{name.title()} - нет на складе")
        elif self.__items[name] - qnt < 0:
            print(f"Слишком мало {name}")
        else:
            self.__items[name] = self.__items[name] - qnt
            print(f"Добавлено курьеру: {qnt} {name.title()}")

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.__items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        return len(self.__items)


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, qnt):  # - увеличивает запас items с учетом лимита capacity
        if self.get_unique_items_count() <= 4:
            # # if self.get_free_space() <= qnt:
            # if name not in super().get_free_space().keys():
            super().add(name, qnt)
        else:
            print("Магазин переполнен!!!")

    # def remove(self, name, qnt):  # - уменьшает запас items, но не ниже 0
    #     if name not in self.__items:
    #         print(f"{name.title()} - нет в магазине")
    #     elif self.__items[name] - qnt < 0:
    #         print(f"Слишком мало {name}")
    #     else:
    #         self.__items[name] = self.__items[name] - qnt
    #         print(f"Добавлено курьеру: {qnt} {name.title()}")


if __name__ == '__main__':
    # warehouse = {"коробка": 5, "лента": 5, "скотч": 5, "бумага": 3, "пленка": 5}
    # stock = Store(warehouse)
    # print("Всего на складе места для хранения: ", stock.get_free_space())
    #
    # for item, value in warehouse.items():
    #     stock.add(item, value)
    #
    # print("Число наименования товаров на складе:", stock.get_unique_items_count())
    # print("Остаток мест на складе: ", stock.get_free_space())
    #
    # stock.remove('коробка', 1)
    # print("***", stock.goods_items)
    # print("Остаток мест на складе: ", stock.get_free_space())
    # print("Число отгруженных товаров сократилось до:", stock.goods_items)
    # print("Остаток на складе: ", remove_stor.storage_quantity)
    # print(remove_stor.get_free_space())

    store = {"печенье": 1, "конфеты": 1, "халва": 1, "шоколад": 1, "мороженное": 1}
    storage = Shop(store)

    print("*" * 20)
    # print("Всего места для хранения: ", storage.get_free_space())
    # for item, value in store.items():
    #     storage.add(item, value)
    #
    print(f"Список товара в магазине: {storage.get_items()}")
    print(f"Группы товара в магазине: {storage.get_unique_items_count()}")
    print(f'Свободно в магазине мест: {storage.get_free_space()}')

