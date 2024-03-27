from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        self.strength -= 30 * 1.3 if peak.difficulty_level == "Advanced" else 30 * 2.5
        self.conquered_peaks.append(peak.name)
