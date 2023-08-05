from project.clients.base_client import BaseClient


class Student(BaseClient):
    AVAILABLE_LOAN = "StudentLoan"
    INITIAL_INTEREST = 2.0

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=Student.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 1.0
