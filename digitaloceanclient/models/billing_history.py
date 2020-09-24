from . import Model


class BillingHistory(Model):
    """
    Represents a record of billing events for an account.

    Attributes
    ----------
    description : str
        Description of the billing history entry
    amount : float
        Amount of the billing history entry
    invoice_id : str
        The ID of the invoice associated with the billing history entry
    invoice_uuid : str
        The UUID of the invoice associated with the billing history entry
    date : str
        Time the billing history entry occured
    type : str
        Type of billing history entry
    """

    description = ''
    amount = 0
    invoice_id = ''
    invoice_uuid = ''
    date = ''
    type = ''

    def __init__(self, data):
        super().__init__(data)
        self.amount = float(self.amount)
