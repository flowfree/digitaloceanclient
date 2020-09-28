from .http_client import HttpClient
from .models import Tag


class Tags(HttpClient):
    """
    Create, read, update, and delete the tags.
    """

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
            The Tag model.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
            If receives HTTP errors.
        """

        return super().create(payload={'name': name})

    def get(self, name):
        """
        Retrieve a Tag.

        Parameters
        ----------
        name : str
            The name of the tag to be retrieved.

        Returns
        -------
        digitaloceanclient.models.Tag
            The Tag model.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
            If receives HTTP errors.
        """

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
            If receives HTTP errors.
        """

        return super().delete(path=f'tags/{name}')
