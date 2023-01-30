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
    def __init__(self):
        self.goods_items = dict()
        self.storage_quantity = 10

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.storage_quantity - sum(self.goods_items.values())

    def add(self, name, qnt):
        if self.get_free_space() >= qnt:
            if name not in self.goods_items.keys():
                self.goods_items[name] = qnt
                print(f"Добавлено {qnt} {name.title()}")

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
    items_count = 5 #
    storage_quantity = 20

    def add(self, name, qnt):  # - увеличивает запас items с учетом лимита capacity
        pass

    def remove(self, name, qnt):  # - уменьшает запас items, но не ниже 0
        pass

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.storage_quantity - sum(self.goods_items.values())

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.goods_items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        return len(self.goods_items)


class Request:
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
    def __init__(self, _from, _to, amount, product):
        self._from = _from
        self._to = _to
        self.amount = amount
        self.product = product

    def get_request(self):
        return {
            'from': self._from,
            'to': self._to,
            'amount': self.amount,
            'product': self.product
        }


if __name__ == '__main__':
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
