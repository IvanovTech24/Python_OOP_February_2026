from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not all(char.isalnum() or char == "-" for char in value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not value >= 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value


    def calculate_total_salaries(self):
        total_salary = sum(a.salary for a in self.astronauts)
        return total_salary


    def status(self):
        sorted_astronaut = sorted([a.id_number for a in self.astronauts])
        sorted_astronaut_str = " #".join(sorted_astronaut) if sorted_astronaut else "N/A"
        total_salaries = self.calculate_total_salaries()

        result = f"Station name: {self.name}; Astronauts: {sorted_astronaut_str}; Total salaries: {total_salaries:.2f}"
        return result


    @abstractmethod
    def update_salaries(self, min_value: float):
        pass

