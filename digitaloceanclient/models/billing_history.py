from . import Model


class BillingHistory(Model):
    # Description of the billing history entry
    description = ''

    # Amount of the billing history entry
    amount = 0

    # ID of the invoice associated with the billing history entry
    invoice_id = ''

    # UUID of the invoice associated with the billing history entry
    invoice_uuid = ''

    # Time the billing history entry occured
    date = ''

    # Type of billing history entry
    type = ''

    def __init__(self, data):
        super().__init__(data)
        self.amount = float(self.amount)
