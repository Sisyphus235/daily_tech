# -*- coding: utf8 -*-


class Hotelier:
    def __init__(self):
        print(f'Arranging the Hotel for Marriage? --')

    def __is_available(self):
        print('Is the hotel free for the event on given day?')
        return True

    def book_hotel(self):
        if self.__is_available():
            print('Registered the booking \n')


class Florist:
    def __init__(self):
        print(f'Flower decorations for the Event? --')

    @staticmethod
    def set_flower_requirements():
        print('Carnations, Roses and Lilies would be used for decorations \n')


class Caterer:
    def __init__(self):
        print(f'Food Arrangements for the Event? --')

    @staticmethod
    def set_cuisine():
        print(f'Chinese & Continental cuisine to be served \n')


class EventManager:
    def __init__(self):
        print(f'Event Manager: Let me talk to the folks \n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()


class You:
    def __init__(self):
        print(f'You: Whoa! Marriage Arrangements?!!\n')

    @staticmethod
    def ask_event_manager():
        print(f"You: Let's contact the event manager \n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print(f'You: Thanks to Event Manager, all preparations done!')


if __name__ == '__main__':
    you = You()
    you.ask_event_manager()
