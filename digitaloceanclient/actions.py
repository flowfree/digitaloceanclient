from .http_client import HttpClient
from .models import Action
from .exceptions import MalformedResponse


class Actions(HttpClient):
    """
    List all actions and retrieve a single action.
    """

    model = Action

    def all(self):
        """
        List all actions.

        Yields
        ------
        digitaloceanclient.models.Action
        """

        return super().all()

    def get(self, action_id):
        """
        Retrieve an action.

        Parameters
        ----------
        action_id : str
            The ID of the specified action.

        Returns
        -------
        digitaloceanclient.models.Action
            The Action model.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().get(action_id)

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

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
