from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    def reserve(self, number_of_people: int):
        reservation_price = number_of_people * self.PRICE_PER_PERSON
        self.price_for_reservation = reservation_price
        self.is_reserved = True
