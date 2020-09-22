from .http_client import HttpClient
from .models import Action
from .exceptions import MalformedResponse


class Actions(HttpClient):
    model = Action

    def refresh(self, action):
        assert (type(action) == Action)
        assert (action.id != '' and action.id != None)

        response = self._request('GET', f'actions/{action.id}')
        try:
            action.from_json(response['action'])
        except (KeyError, TypeError):
            raise MalformedResponse("Invalid response: 'action'")
