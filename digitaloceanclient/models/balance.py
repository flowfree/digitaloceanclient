from . import Model


class Balance(Model):
    # Balance as of the generated_at time
    # This value includes the account_balance and month_to_date_usage
    month_to_date_balance = 0

    # Current balance of the customer's most recent billing activity
    account_balance = 0

    # Amount used in the current billing period as of the generated_at time
    month_to_date_usage = 0

    # The time at which balances were most recently generated
    generated_at = ''

    def __init__(self, data):
        super().__init__(data)
        self.month_to_date_balance = float(self.month_to_date_balance)
        self.account_balance = float(self.account_balance)
        self.month_to_date_usage = float(self.month_to_date_usage)
