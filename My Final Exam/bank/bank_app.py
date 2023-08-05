from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity):
        self.capacity = capacity    # The number of clients a bank can have
        self.loans = []    # Will contain loan objects
        self.clients = []    # Will contain clients objects

    def add_loan(self, loan_type):
        if loan_type not in self.VALID_LOANS.keys():
            raise Exception("Invalid loan type!")

        new_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_CLIENTS.keys():
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        client = self.__find_client_by_client_id(client_id)
        loan = self.__find_loan_by_loan_type(loan_type)

        if client.AVAILABLE_LOAN != loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        client = self.__find_client_by_client_id(client_id)

        if not client:
            raise Exception("No such client!")

        if len(client.loans) != 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        loans_with_increased_interest = 0

        for loan in self.loans:
            if isinstance(loan, StudentLoan) and loan_type == "StudentLoan":
                loan.increase_interest_rate()
                loans_with_increased_interest += 1
            elif isinstance(loan, MortgageLoan) and loan_type == "MortgageLoan":
                loan.increase_interest_rate()
                loans_with_increased_interest += 1

        return f"Successfully changed {loans_with_increased_interest} loans."

    def increase_clients_interest(self, min_rate):
        clients_with_increased_interest = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                clients_with_increased_interest += 1

        return f"Number of clients affected: {clients_with_increased_interest}."

    def get_statistics(self):
        count_active_clients = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)

        loans_granted_to_clients = 0
        for client in self.clients:
            if client.loans:
                loans_granted_to_clients += len(client.loans)

        granted_loan_sum = sum(loan.amount for client in self.clients for loan in client.loans)
        count_available_loans = len(self.loans)
        not_granted_loan_sum = sum(loan.amount for loan in self.loans)

        if count_active_clients == 0:
            avg_client_interest_rate = 0
        else:
            avg_client_interest_rate = sum(client.interest for client in self.clients) / count_active_clients

        return f"Active Clients: {count_active_clients}\nTotal Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_granted_to_clients}, Total Sum: {granted_loan_sum:.2f}\n" \
               f"Available Loans: {count_available_loans}, Total Sum: {not_granted_loan_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

    def __find_client_by_client_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

        return None

    def __find_loan_by_loan_type(self, loan_type):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan

        return None