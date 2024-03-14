from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS_NAMES = {
        MortgageLoan.__name__: lambda: MortgageLoan(),
        StudentLoan.__name__: lambda: StudentLoan(),
    }

    VALID_CLIENTS_NAMES_AND_THEIR_LOANS = {
        Adult.__name__: {"instance": lambda x, y, z: Adult(x, y, z), "loan": MortgageLoan.__name__},
        Student.__name__: {"instance": lambda x, y, z: Student(x, y, z), "loan": StudentLoan.__name__},
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS_NAMES:
            raise Exception("Invalid loan type!")
        new_loan = self.VALID_LOANS_NAMES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS_NAMES_AND_THEIR_LOANS:
            raise Exception("Invalid client type!")

        if len(self.clients) + 1 > self.capacity:
            return f"Not enough bank capacity."

        new_client = self.VALID_CLIENTS_NAMES_AND_THEIR_LOANS[client_type]["instance"](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        current_client = [client for client in self.clients if client.client_id == client_id]
        current_loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        if current_client and current_loan:
            try:
                client_loan = self.VALID_CLIENTS_NAMES_AND_THEIR_LOANS[current_client[0].__class__.__name__]["loan"]
                if client_loan != loan_type:
                    raise Exception("Inappropriate loan type!")
                current_client[0].loans.append(current_loan[0])
                self.loans.remove(current_loan[0])
                return f"Successfully granted {loan_type} to {current_client[0].name} with ID {client_id}."
            except KeyError:
                pass

    def remove_client(self, client_id: str):
        current_client = [client for client in self.clients if client.client_id == client_id]
        if not current_client:
            raise Exception("No such client!")
        if current_client[0].loans:
            raise Exception("The client has loans! Removal is impossible!")
        else:
            self.clients.remove(current_client[0])
            return f"Successfully removed {current_client[0].name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        if loan_type in self.VALID_LOANS_NAMES:
            for loan in self.loans:
                if loan.__class__.__name__ == loan_type:
                    loan.increase_interest_rate()
                    number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        number_of_changed_rates = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                number_of_changed_rates += 1
        return f"Number of clients affected: {number_of_changed_rates}."

    def get_statistics(self):
        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {sum([client.income for client in self.clients]):.2f}\n"
                  f"Granted Loans: {sum([len(client.loans) for client in self.clients])}, "
                  f"Total Sum: {sum([sum([loan.amount for loan in client.loans]) for client in self.clients]):.2f}\n"
                  f"Available Loans: {len(self.loans)}, "
                  f"Total Sum: {sum([loan.amount for loan in self.loans]):.2f}\n")

        average_client_interest_rate = 0
        try:
            average_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            pass
        result += f"Average Client Interest Rate: {average_client_interest_rate:.2f}"
        return result
