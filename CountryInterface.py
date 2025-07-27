from abc import ABC, abstractmethod
class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """Абстрактное свойство: название страны (строка)"""
        pass

    @property
    @abstractmethod
    def population(self):
        """Абстрактное свойство: численность населения (целое положительное число)"""
        pass

    @population.setter
    @abstractmethod
    def population(self, value):
        pass

    @property
    @abstractmethod
    def square(self):
        """Абстрактное свойство: площадь страны (положительное число)"""
        pass

    @square.setter
    @abstractmethod
    def square(self, value):
        pass

    @abstractmethod
    def get_info(self):
        """Абстрактный метод для получения сводной информации о стране"""
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Численность населения должна быть положительным целым числом")
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        self._square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"

