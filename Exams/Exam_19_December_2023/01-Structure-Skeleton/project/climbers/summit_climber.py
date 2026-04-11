from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)


    def can_climb(self) -> bool:
        return self.strength >= 75


    def climb(self, peak : BasePeak):
        if peak.difficulty_level == "Advanced":
            difficulty_multiplier = 1.3
            self.strength -= 30.0 * difficulty_multiplier
        else:
            difficulty_multiplier = 2.5
            self.strength -= 30.0 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)