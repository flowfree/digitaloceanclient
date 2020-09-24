from . import Model


class Balance(Model):
    """
    Represents current user's balance information.

    Attributes
    ----------
    month_to_date_balance : float
        Balance as of the generated_at time
        This value includes the account_balance and month_to_date_usage
    account_balance : float
        Current balance of the customer's most recent billing activity
    month_to_date_usage : float
        Amount used in the current billing period as of the generated_at time
    generated_at : str
        The time at which balances were most recently generated
    """

    month_to_date_balance = 0
    account_balance = 0
    month_to_date_usage = 0
    generated_at = ''

    def __init__(self, data):
        super().__init__(data)
        self.month_to_date_balance = float(self.month_to_date_balance)
        self.account_balance = float(self.account_balance)
        self.month_to_date_usage = float(self.month_to_date_usage)
