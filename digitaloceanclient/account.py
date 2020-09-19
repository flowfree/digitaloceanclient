from .http_client import HttpClient

from .models import Account as AccountModel


class Account(HttpClient):
    def info(self):
        response = self._request('GET', 'account')
        data = response.get('account')
        return AccountModel(data)
