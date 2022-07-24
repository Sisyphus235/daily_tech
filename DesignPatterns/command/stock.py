# -*- coding: utf8 -*-

from abc import ABCMeta, abstractclassmethod


class Order(metaclass=ABCMeta):
    @abstractclassmethod
    def execute(cls):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print(f'You will buy stocks')

    def sell(self):
        print('You will sell stocks')


class Agent:
    def __init__(self):
        self._order_queue = []

    def place_order(self, order):
        self._order_queue.append(order)
        order.execute()


if __name__ == '__main__':
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    agent = Agent()
    agent.place_order(buyStock)
    agent.place_order(sellStock)
