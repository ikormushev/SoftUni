from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        try:
            already_existing_diver = next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(self.VALID_DIVER_TYPES[diver_type](diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            already_existing_fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(self.VALID_FISH_TYPES[fish_type](fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        def check_oxygen_value(diver):
            if diver.oxygen_level == 0:
                diver.update_health_status()

        wanted_diver = None
        try:
            wanted_diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        wanted_fish = None
        try:
            wanted_fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if wanted_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if wanted_diver.oxygen_level < wanted_fish.time_to_catch:
            wanted_diver.miss(wanted_fish.time_to_catch)
            check_oxygen_value(wanted_diver)
            return f"{diver_name} missed a good {fish_name}."

        elif wanted_diver.oxygen_level == wanted_fish.time_to_catch:
            if is_lucky:
                wanted_diver.hit(wanted_fish)
                check_oxygen_value(wanted_diver)
                return f"{diver_name} hits a {wanted_fish.points}pt. {fish_name}."
            wanted_diver.miss(wanted_fish.time_to_catch)
            check_oxygen_value(wanted_diver)
            return f"{diver_name} missed a good {fish_name}."

        wanted_diver.hit(wanted_fish)
        check_oxygen_value(wanted_diver)
        return f"{diver_name} hits a {wanted_fish.points}pt. {fish_name}."

    def health_recovery(self):
        unhealthy_divers = [x for x in self.divers if x.has_health_issue]
        [x.update_health_status() for x in unhealthy_divers]
        [x.renew_oxy() for x in unhealthy_divers]
        return f"Divers recovered: {len(unhealthy_divers)}"

    def diver_catch_report(self, diver_name: str):
        wanted_diver = next(filter(lambda d: d.name == diver_name, self.divers))
        return f"**{diver_name} Catch Report**\n" + "\n".join([x.fish_details() for x in wanted_diver.catch])

    def competition_statistics(self):
        sorted_divers = list(sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)))
        only_healthy_divers = [str(x) for x in sorted_divers if not x.has_health_issue]
        return f"**Nautical Catch Challenge Statistics**\n" + "\n".join(only_healthy_divers)
