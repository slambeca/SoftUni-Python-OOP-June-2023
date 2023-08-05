from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    STUDENT_LOAN_INTEREST_RATE = 1.5
    STUDENT_LOAN_AMOUNT = 2000.0

    def __init__(self):
        super().__init__(interest_rate=StudentLoan.STUDENT_LOAN_INTEREST_RATE, amount=StudentLoan.STUDENT_LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2