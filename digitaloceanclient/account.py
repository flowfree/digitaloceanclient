from .http_client import HttpClient

from .models import Account as AccountModel


class Account(HttpClient):
    def get(self):
        response = self._request('GET', 'account')
        data = response.get('account')
        return AccountModel.from_json(data)
