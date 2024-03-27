from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber,
                           "SummitClimber": SummitClimber}

    VALID_PEAKS = {"ArcticPeak": ArcticPeak,
                   "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        try:
            wanted_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{wanted_climber.name} has been already registered."
        except StopIteration:
            self.climbers.append(self.VALID_CLIMBER_TYPES[climber_type](climber_name))
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.VALID_PEAKS[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear):
        wanted_peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        wanted_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        missing_gear = [g for g in wanted_peak.get_recommended_gear() if g not in gear]

        if missing_gear:
            wanted_climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        wanted_climber = None
        try:
            wanted_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        wanted_peak = None
        try:
            wanted_peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if wanted_climber.can_climb() and wanted_climber.is_prepared:
            wanted_climber.climb(wanted_peak)
            return (f"{climber_name} conquered {peak_name} whose "
                    f"difficulty level is {wanted_peak.difficulty_level}.")
        elif not wanted_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        wanted_climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        successful_climbers = list(sorted([x for x in self.climbers if x.conquered_peaks],
                                          key=lambda x: (-len(x.conquered_peaks), x.name)))

        climbed_peaks = []

        for climber in successful_climbers:
            climber.conquered_peaks = list(sorted(climber.conquered_peaks))
            for peak in climber.conquered_peaks:
                if peak not in climbed_peaks:
                    climbed_peaks.append(peak)

        result = f"Total climbed peaks: {len(climbed_peaks)}\n**Climber's statistics:**\n"
        result += "\n".join(str(x) for x in successful_climbers)
        return result
