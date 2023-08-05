from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    MORTGAGE_LOAN_INTEREST_RATE = 3.5
    MORTGAGE_LOAN_AMOUNT = 50000.0

    def __init__(self):
        super().__init__(interest_rate=MortgageLoan.MORTGAGE_LOAN_INTEREST_RATE,
                         amount=MortgageLoan.MORTGAGE_LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5