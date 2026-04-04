from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    _AVAILABLE_CAPACITY = 5

    def __init__(self, name: str):
        super().__init__(name, self._AVAILABLE_CAPACITY)


    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if isinstance(a, ScientistAstronaut) and a.salary <= min_value:
                a.salary += 5000.0
