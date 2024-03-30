from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if 1500 <= self.elevation <= 2500:
            return "Advanced"
        elif self.elevation > 2500:
            return "Extreme"