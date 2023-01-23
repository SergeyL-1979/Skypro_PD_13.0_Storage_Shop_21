#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Storage(ABC): # Нужно ли сюда делать наследование от ABC?
    """
    Создайте абстрактный класс Storage
    **Поля:**
    `items` (словарь название:количество)
    `capacity` (целое число)
    **Методы:**
    `add`(<название>, <количество>)  - увеличивает запас items
    `remove`(<название>, <количество>) - уменьшает запас items
    `get_free_space()` - вернуть количество свободных мест
    `get_items()` - возвращает содержание склада в словаре {товар: количество}
    `get_unique_items_count()` - возвращает количество уникальных товаров.
    """
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
    """
    Реализуйте класс Store. В нем хранится любое количество любых товаров.
    Store не может быть заполнен если свободное место закончилось
    **Поля:**
    items (словарь название:количество)
    capacity по умолчанию равно 100
    **Методы:**
    add(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity
    remove(<название>, <количество>) - уменьшает запас items но не ниже 0
    `get_free_space()` - вернуть количество свободных мест
    `get_items()` - возвращает содержание склада в словаре {товар: количество}
    `get_unique_items_count()` - возвращает количество уникальных товаров.
    """
    # goods_items = {}  # ИЛИ ТУТ ПРАВИЛЬНО ДЕЛАТ ПОЛЕ
    storage_quantity = 10

    def __init__(self):
        self.goods_items = {}


    @classmethod
    def _get_total(cls):
        return cls.storage_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.storage_quantity = qnt

    def add(self, name, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.storage_quantity = qnt
        else:
            self.storage_quantity = self._get_total()
            self._set_total(0)
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

    def remove(self, name, count):
        for key in self.goods_items.keys():
            if name == key:
                if self.goods_items[key] - count >= 0:
                    self.goods_items[key] = self.goods_items[key] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} - нет на складе")

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.storage_quantity

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        pass

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        pass


class Shop(Store):
    """
    Реализуйте класс Shop. В нем хранится **не больше 5 разных товаров**.
    Shop **не может быть наполнен**, если свободное место закончилось или в нем уже есть 5 разных товаров.
    **Поля:**
    items (словарь название:количество)
    capacity по умолчанию равно 20
    **Методы:**
    `add`(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity
    `remove`(<название>, <количество>) - уменьшает запас items но не ниже 0
    `get_free_space()` - вернуть количество свободных мест
    `get_items()` - возвращает содержание склада в словаре {товар: количество}
    `get_unique_items_count()` - возвращает количество уникальных товаров.
    """
    goods_items = {}  # ИЛИ ТУТ ПРАВИЛЬНО ДЕЛАТ ПОЛЕ
    storage_quantity = 20

    def add(self, name, qnt):  # - увеличивает запас items с учетом лимита capacity
        pass

    def remove(self, name, qnt):  # - уменьшает запас items, но не ниже 0
        pass

    def get_free_space(self):  # - вернуть количество свободных мест
        pass

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        pass

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        pass


class Request(Store):
    """
    Создайте класс Request в котором будет храниться запрос
    **Поля:**
    from - откуда везем (строка)
    to - куда везем (строка)
    amount = 3,
    product = "печеньки" (строка)

    При инициализации принимает список всех складов и строку типа
    **Доставить** 3 печеньки **из** склад **в** магазин

    И возвращает объект класса Request
    from = "склад",
    to =  "магазин",
    amount = 3,
    product = "печеньки"
    """
    # from - откуда везем(строка)
    # to - куда везем(строка)
    # amount = 3,
    # product = "печеньки"(строка)

    # return f"Доставить {amount} {product} из {from} в {to}"
    pass


if __name__ == '__main__':
    pass
    """
    Напишите функцию main, в которой
    - введите приглашение
    - обрабатывайте ввод пользователя
    - выполните перемещение если это возможно
    - выполните перемещение
    """
    print("Всего на складе: ", Store.storage_quantity)
    storage = Store()
    # five = storage.add('s', 5)
    # print(five)
    print("Число отгруженных товаров возросло до:", storage.storage_quantity)
    print("Остаток на складе: ", Store.storage_quantity)
    storage.remove('s', 4)
    print("Число отгруженных товаров сократилось до:", storage.storage_quantity)
    print("Остаток на складе: ", Store.storage_quantity)
    storage.add('ss', 8)
    print(storage.storage_quantity)
    print("Число отгруженных товаров сократилось до:", storage.storage_quantity)
    print("Остаток на складе: w", Store.storage_quantity)
