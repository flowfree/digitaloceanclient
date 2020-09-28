from .http_client import HttpClient
from .models import Tag


class Tags(HttpClient):
    model = Tag 

    def create(self, name):
        """
        Create a new Tag.

        Parameters
        ----------
        name : str
            The name of the new tag.

        Returns
        -------
        digitaloceanclient.models.Tag

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().create(payload={'name': name})

    def get(self, name):
        return super().get(path=f'tags/{name}')

    def delete(self, name):
        """
        Delete a Tag.

        Parameters
        ----------
        name : str
            The name of the tag to be deleted.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().delete(path=f'tags/{name}')
