from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    _AVAILABLE_CAPACITY = 3

    def __init__(self, name: str):
        super().__init__(name, self._AVAILABLE_CAPACITY)


    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if isinstance(a, EngineerAstronaut) and a.salary <= min_value:
                a.salary += 3000.0
