from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS_TYPES = {"Guitarist": Guitarist,
                             "Drummer": Drummer,
                             "Singer": Singer}

    BANDS_MUSICIANS_REQUIRED_SKILLS_FOR_CONCERT = {
        "Rock": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing high pitch notes"],
            "Guitarist": ["play rock"]
        },
        "Metal": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing low pitch notes"],
            "Guitarist": ["play metal"]
        },
        "Jazz": {
            "Drummer": ["play the drums with drum brushes"],
            "Singer": ["sing low pitch notes", "sing high pitch notes"],
            "Guitarist": ["play jazz"]
        }
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS_TYPES:
            raise ValueError("Invalid musician type!")

        try:
            musician = next(filter(lambda m: m.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")
        except StopIteration:
            self.musicians.append(self.VALID_MUSICIANS_TYPES[musician_type](name, age))
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            band = next(filter(lambda b: b.name == name, self.bands))
            raise Exception(f"{name} band is already created!")
        except StopIteration:
            self.bands.append(Band(name))
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        except StopIteration:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = None
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        band = None
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = None
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        musician = None
        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        band = next(filter(lambda b: b.name == band_name, self.bands))
        band_types = [x.__class__.__name__ for x in band.members]
        for musician in self.VALID_MUSICIANS_TYPES:
            if band_types.count(musician) < 1:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for band_member in band.members:
            for skill in self.BANDS_MUSICIANS_REQUIRED_SKILLS_FOR_CONCERT[concert.genre][band_member.__class__.__name__]:
                if skill not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
