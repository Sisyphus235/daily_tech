# -*- coding: utf8 -*-

from abc import ABCMeta, abstractclassmethod


class Subscriber(metaclass=ABCMeta):
    @abstractclassmethod
    def update(cls):
        pass


class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.latest_news = news

    def get_news(self):
        return f'Got news: {self.latest_news}'


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for subscribers in [SMSSubscriber, EmailSubscriber]:
        subscribers(news_publisher)
    print(f'\nsubscribers: {news_publisher.subscribers()}')
    news_publisher.add_news('Init')
    news_publisher.notify_subscribers()
    print(f'\ndetached: {type(news_publisher.detach()).__name__}')
    print(f'\nsubscribers: {news_publisher.subscribers()}')
    news_publisher.add_news('Another')
    news_publisher.notify_subscribers()
