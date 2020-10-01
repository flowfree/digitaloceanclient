from .http_client import HttpClient

from .models import Account as AccountModel
from .models import Balance


class Account(HttpClient):
    def info(self):
        """
        Retrieve information about the current user's account.

        Returns
        -------
        digitaloceanclient.models.Account
            The current user's account information.
        """

        response = self._request('GET', 'account')
        data = response.get('account')
        return AccountModel(data)

    def balance(self):
        response = self._request('GET', 'customers/my/balance')
        return Balance(response)
