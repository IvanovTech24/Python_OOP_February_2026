from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)


    def can_climb(self) -> bool:
        return self.strength >= 100


    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            difficulty_multiplier = 2.0
            self.strength -= 20.0 * difficulty_multiplier
        else:
            difficulty_multiplier = 1.5
            self.strength -= 20.0 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)