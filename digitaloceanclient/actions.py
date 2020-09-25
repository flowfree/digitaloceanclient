from .http_client import HttpClient
from .models import Action
from .exceptions import MalformedResponse


class Actions(HttpClient):
    """
    List all actions and retrieve a single action.
    """

    model = Action

    def refresh(self, action):
        """
        Refresh the given action to get its current state.

        Parameters
        ----------
        action : digitaloceanclient.models.Action
            The action to refreshed.

        Raises
        ------
        digitaloceanclient.exceptions.MalformedResponse
            When the API response cannot be populated to the Action model.
        """
        assert (type(action) == Action)
        assert (action.id != '' and action.id != None)

        response = self._request('GET', f'actions/{action.id}')
        try:
            action.from_json(response['action'])
        except (KeyError, TypeError):
            raise MalformedResponse("Invalid response: 'action'")
