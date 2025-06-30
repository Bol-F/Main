from abc import ABC, abstractmethod


class Computer(ABC):
    total_computers = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self._price = price
        Computer.total_computers += 1

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_total_computers(cls):
        return cls.total_computers

    def __gt__(self, other):
        if not isinstance(other, Computer):
            return NotImplemented
        return self.price > other.price

    def __repr__(self):
        return f"{self.brand} {self.model}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value


class Monoblock(Computer):
    def __init__(self, screen_size, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Screen size: {self.screen_size}, Price: {self.price}"


class Laptop(Computer):
    def __init__(self, battery_life, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Battery life: {self.battery_life}, Price: {self.price}"


class Factory:
    total_factories = 0

    def __init__(self, name):
        self.name = name
        self.computers = []
        Factory.total_factories += 1

    def add_computer(self, computer):
        if isinstance(computer, Computer):
            self.computers.append(computer)
        else:
            raise ValueError("Invalid computer type!")

    def list_computers(self):
        return self.computers

    @classmethod
    def get_total_factories(cls):
        return cls.total_factories


n = Laptop(10, "Apple", "MacBook", 2021, 1000)
m = Monoblock(15, "Dell", "Inspiron", 2021, 1500)
f = Factory("Ferrari")

print(n.display_info())
print("-" * 100)
print(m.display_info())
print("-" * 100)
print(Computer.get_total_computers())
print("-" * 100)
f.add_computer(n)
f.add_computer(m)
print(f.get_total_factories())
print("-" * 100)
print(f.list_computers())
print("-" * 100)

n.price = 1000
print(n.price)
n.price = -100
