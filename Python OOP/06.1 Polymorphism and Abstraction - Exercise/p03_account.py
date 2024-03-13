class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    @property  # balance has to be a property in order to get info out of it without ()
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index: int):
        return self._transactions[index]

    def __reversed__(self) -> list:
        return self._transactions[::-1]

    def __gt__(self, other) -> bool:
        return self.balance > other.balance

    def __eq__(self, other) -> bool:
        return self.balance == other.balance

    def __ge__(self, other) -> bool:
        return self > other or self == other

    def __add__(self, other):
        new_name = f"{self.owner}&{other.owner}"
        new_starting_amount = self.amount + other.amount
        new_account = Account(new_name, new_starting_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account
