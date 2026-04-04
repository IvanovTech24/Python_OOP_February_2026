from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    _SPECIALIZATION = "EngineerAstronaut"
    _STAMINA = 80

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self._SPECIALIZATION, self._STAMINA)


    def train(self):
        self.stamina = min(100, self.stamina + 5)
        