from project.horse_race import HorseRace
from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    RACE_MIN_PARTICIPANTS = 2

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        try:
            horse = next(filter(lambda h: h.name == horse_name, self.horses))
            raise Exception(f"Horse {horse_name} has been already added!")
        except StopIteration:
            if horse_type in self.VALID_HORSE_TYPES:
                self.horses.append(self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed))
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
            raise Exception(f"Jockey {jockey_name} has been already added!")
        except StopIteration:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
            raise Exception(f"Race {race_type} has been already created!")
        except StopIteration:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = None
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = None
        try:
            horse = next(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses[::-1]))
        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = None
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = None
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = None
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < self.RACE_MIN_PARTICIPANTS:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey = race.jockeys[0]

        for jockey in race.jockeys:
            if jockey.horse.speed > winner_jockey.horse.speed:
                winner_jockey = jockey

        return (f"The winner of the {race_type} race, "
                f"with a speed of {winner_jockey.horse.speed}km/h is "
                f"{winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}.")
