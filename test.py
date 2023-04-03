from abc import ABC, abstractmethod
from inspect import isabstract


class Animal(ABC):
    @abstractmethod
    def eat(self) -> None:
        print("Animal eats.")


class Herbivore(Animal):
    pass


class Rabbit(Herbivore):
    def eat(self) -> None:
        print("Rabbit eats carrot.")


print(isabstract(Animal))
print(isabstract(Herbivore))
print(isabstract(Rabbit))
