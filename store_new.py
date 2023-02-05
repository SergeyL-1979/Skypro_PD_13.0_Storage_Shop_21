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
    def __init__(self, goods_items: dict, storage_quantity=100):
        self.__goods_items = goods_items
        self.__storage_quantity = storage_quantity

    def get_free_space(self):  # - вернуть количество свободных мест
        return self.__storage_quantity - sum(self.__goods_items.values())

    def add(self, name, qnt):
        if self.get_free_space() >= qnt:
            if name not in self.__goods_items.keys():
               self.__goods_items[name] = qnt
               # print(f"Добавлено {qnt} {name.title()}")
        else:
            print("Склад переполнен!!!")

    def remove(self, name, qnt):
        if name not in self.__goods_items:
            print(f"{name.title()} - нет на складе")
        elif self.__goods_items[name] - qnt < 0:
            print(f"Слишком мало {name}")
        else:
            self.__goods_items[name] = self.__goods_items[name] - qnt
            print(f"Добавлено курьеру: {qnt} {name.title()}")

    def get_items(self):  # - возвращает содержание склада в словаре {товар: количество}
        return self.__goods_items

    def get_unique_items_count(self):  # - возвращает количество уникальных товаров
        return len(self.__goods_items)


class Shop(Store):
    def __init__(self, goods_items, storage_quantity=20):
        super().__init__(goods_items, storage_quantity)
    # def add(self, name, qnt):  # - увеличивает запас items с учетом лимита capacity
    #     if self.get_unique_items_count() <= 5:
    #         if self.get_free_space() >= qnt:
    #             if name not in self.__goods_items.keys():
    #                 self.items[name] = qnt
    #                 print(f"Добавлено {qnt} {name.title()}")
    #             if name in self.__goods_items.keys():
    #                 super().__goods_items[name] = qnt
    #         else:
    #             print("Магазин переполнен!!!")

    # def remove(self, name, qnt):  # - уменьшает запас items, но не ниже 0
    #     if name not in self.__goods_items:
    #         print(f"{name.title()} - нет в магазине")
    #     elif (self.__goods_items[name] - qnt) < 0:
    #         print(f"Слишком мало {name}")
    #     else:
    #         self.__goods_items[name] = self.__goods_items[name] - qnt
    #         print(f"Добавлено курьеру: {qnt} {name.title()}")


class Request:
    def __init__(self, input_requests):
        # self.input_requests = input_requests
        self.source: Store  = storages[input_requests[4]] # Здесь будет класс shop или store
        self.destination: Shop = storages[input_requests[6]] # Здесь будет класс shop или store
        self.input_from = input_requests[4]
        self.input_to = input_requests[6]
        self.input_amounts = int(input_requests[1])
        self.input_products = input_requests[2]
        # order = Request(_from=_from, _to=_to, amounts=amounts, products=products)


if __name__ == '__main__':

    warehouse = {"коробка": 5, "лента": 5, "скотч": 5, "бумага": 3, "пленка": 5}
    # store = Store(warehouse)

    shopping = {"печенье": 1, "конфеты": 3, "халва": 1, "шоколад": 1, "мороженное": 1}
    # shop = Shop(shopping)

    storages = {
        'склад': Store(warehouse),
        'магазин': Shop(shopping)
    }
    print("\n", "*" * 20, "СКЛАД", "*" * 20)
    # print(f'На складе хранится: {store.get_items()}')
    # print(f"Количество групп товара склад: {store.get_unique_items_count()}")
    # print(f"Свободно всего мест в складе: {store.get_free_space()}")

    print("\n", "*" * 20, "МАГАЗИН", "*" * 20)
    # print(f"В магазине хранится: {shop.get_items()}")
    # print(f"Количество групп товара в магазине: {shop.get_unique_items_count()}")
    # print(f"Свободное место в магазине: {shop.get_free_space()}")

    while True:
        user_input = input('Пример ввода заказа: << Доставить 2 коробка из склад в магазин >> \n').lower()
        if user_input == 'stop' or user_input == 'стоп':
            break
        else:
            print("\n", "=" * 20, "Делаем ЗАКАЗ", "=" * 20)
            # user_input = 'Доставить 2 коробка из склад в магазин'
            # user_input = 'Доставить 3 конфеты из склад в магазин'
            # user_input = 'Доставить 3 коробка из магазин в склад'
            # user_input = 'Доставить 7 конфеты из магазин в склад'
            user_in = user_input.split()
            request = Request(user_in)
            request.source.remove(request.input_products, request.input_amounts)
            request.destination.add(request.input_products, request.input_amounts)
    # print(f"Доставить {request.input_amounts} {request.input_products} из {request.input_from} в {request.input_to}")


    # ==============================================================
    # question = input(f"Доставить 3 печеньки из склада в магазин ").lower()
    # quest = question.split()
    # if len(quest) != 7:
    #     print('Запрос не корректен')
    # else:
    #     _from = quest[4]
    #     _to = quest[6]
    #     amounts = int(quest[1])
    #     products = quest[2]
    #     order = Request(_from=_from, _to=_to, amounts=amounts, products=products)
    #
    #
    # # req = Request(_from=, _to=, amount=am, product=)
    # print(f"Доставить {order.amounts} {order.products} из {order._from} в {order._to}")


    # if order._from == 'магазин':
    #     value = shop.get_items()
    #     print(f'В магазине имеется {shop.get_items()}')
    #     shop.remove(order.products, value)
    #     print(f'Курьер забирает из магазина {value} {order.products}')




# ===================================================================================================
# while True:
#     print(f'\nВведите запрос в формате "Доставить 3 бумага из склад в магазин"\n'
#           f'(для выхода введите "stop")')
#     # question = input().lower()
#
#     if input().lower() == "stop" or input().lower() == "стоп":
#         print("sd")
#         break
#     else:
#         continue
    # stock = Store()
    # print("Всего на складе места для хранения: ", stock.get_free_space())
    # warehouse = {"коробка": 5, "лента": 5, "скотч": 5, "бумага": 3, "пленка": 5}
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

    # storage = Shop()
    # store = {"печенье": 1, "конфеты": 1, "халва": 1, "шоколад": 1, "мороженное": 1}
    # print("*" * 20)
    # print("Всего места для хранения: ", storage.get_free_space())
    # for item, value in store.items():
    #     storage.add(item, value)
    #
    # print(f"Список товара в магазине: {storage.get_items()}")
    # print(f"Группы товара в магазине: {storage.get_unique_items_count()}")
    # print(f'Свободно в магазине мест: {storage.get_free_space()}')