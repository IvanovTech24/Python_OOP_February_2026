from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    REST_POINT = 15

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list[str] = []
        self.is_prepared: bool = True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value: float):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value


    @abstractmethod
    def can_climb(self):
        pass


    @abstractmethod
    def climb(self, peak : BasePeak):
        pass


    def rest(self):
        self.strength += self.REST_POINT


    def __str__(self):
        con_peaks = sorted(self.conquered_peaks)
        return (f"{self.__class__.__name__}: /// Climber name: {self.name} "
                f"* Left strength: {self.strength:.1f} * "
                f"Conquered peaks: {', '.join(con_peaks)} ///")
