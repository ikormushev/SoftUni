from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) + 1 <= MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) + 1 <= MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return f"DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return (f"{current_customer.name} should be at least "
                    f"{current_dvd.age_restriction} to rent this movie")

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        return ("\n".join([customer.__repr__() for customer in self.customers]) + "\n" +
                "\n".join([dvd.__repr__() for dvd in self.dvds]))
