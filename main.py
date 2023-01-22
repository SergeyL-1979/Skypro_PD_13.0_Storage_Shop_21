#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Storage:
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
    items = {}
    goods_quantity = 10

    def __init__(self, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity = qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)

    @classmethod
    def _get_total(cls):
        return cls.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt

    @abstractmethod
    def add(self, name, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity += qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)

    @abstractmethod
    def remove(self, name, qnt):
        if qnt < self.goods_quantity:
            self.goods_quantity = (self.goods_quantity - qnt)
            self._set_total(self._get_total() + qnt)
        else:
            self._set_total(self._get_total() + self.goods_quantity)
            self.goods_quantity = 0

    @abstractmethod
    def get_unique_items_count(self):
        self.goods_quantity = self.goods_quantity + self._get_total()
        self._set_total(0)


    @abstractmethod
    def get_free_space(self):
        free_space = Store.goods_quantity < self.goods_quantity
        return free_space

    @abstractmethod
    def get_items(self):
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
    def __init__(self, count):
        super().__init__(count)
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} - нет на складе")

    def get_free_space(self):  # - вернуть количество свободных мест
        pass

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
    items = {}
    capacity = 20

    def add(self, name, count):  # - увеличивает запас items с учетом лимита capacity
        pass

    def remove(self, name, count):  # - уменьшает запас items, но не ниже 0
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
    print("Всего на складе: ", Storage.goods_quantity)
    storage = Storage(6)
    storage.add('s', 5)
    print("Число отгруженных товаров возросло до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)
    storage.remove('s', 4)
    print("Число отгруженных товаров сократилось до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)
    storage.add('ss', 8)
    print(storage.goods_quantity)
    print("Число отгруженных товаров сократилось до:", storage.goods_quantity)
    print("Остаток на складе: w", Storage.goods_quantity, Storage.items)
