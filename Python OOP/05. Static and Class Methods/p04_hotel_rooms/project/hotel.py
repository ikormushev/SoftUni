from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number:
                action = room.take_room(people)
                if action is None:
                    self.guests += people
                break

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                room_guests = room.guests
                action = room.free_room()
                if action is None:
                    self.guests -= room_guests
                break

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.guests])}\n"
                f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.guests])}")
