# -*- coding: utf8 -*-

"""
代理模式和门面模式都在真实对象前加入一个代理/门面对象
区别是
代理对象为目标对象提供占位符，控制原始对象的访问；门面模式是提供了其对象的一系列接口
代理对象与目标对象有相同接口，保存有目标对象的引用；门面模式实现了子系统之间通信和依赖的最小化
"""

from abc import ABCMeta, abstractclassmethod


class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def do_pay(cls):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_funds(self):
        print(f'Bank: Checking if account {self.__get_account()} has enough funds')
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print('Bank: pay the merchant')
            return True
        else:
            print('Bank: sorry, insufficient funds')
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Proxy: punch in card number: ')
        self.bank.set_card(card)
        return self.bank.do_pay()


class Customer:
    def __init__(self):
        print(f'Customer: Let us buy the Denim shirt')
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print(f'Customer: Denim shirt is Mine :)')
        else:
            print(f'Customer: I should earn more :(')


if __name__ == '__main__':
    customer = Customer()
    customer.make_payment()
