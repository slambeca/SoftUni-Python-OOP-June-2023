from project.clients.base_client import BaseClient


class Adult(BaseClient):
    AVAILABLE_LOAN = "MortgageLoan"
    INITIAL_INTEREST = 4.0

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=Adult.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 2.0
