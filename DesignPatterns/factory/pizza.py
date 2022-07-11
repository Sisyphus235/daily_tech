from abc import ABCMeta, abstractclassmethod


class VegPizza(metaclass=ABCMeta):
    @abstractclassmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractclassmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, ' is served with chicken on ',
              type(VegPizza).__name__)


class MexicanPizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, ' is served with Ham on ',
              type(VegPizza).__name__)


class PizzaFactory(metaclass=ABCMeta):
    @abstractclassmethod
    def createVegPizza(self):
        pass

    @abstractclassmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanPizza()

    def createNonVegPizza(self):
        return HamPizza()


class PizzaStore:
    def __init__(self) -> None:
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.makePizzas()
