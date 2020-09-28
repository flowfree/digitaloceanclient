from .http_client import HttpClient
from .models import Image


class Images(HttpClient):
    model = Image

    def all(self, type_=None):
        """
        Get all images.

        Parameters
        ----------
        type_ : {'distribution', 'application', 'private'}, optional
            Filter images by the given type.

        Yields
        -------
        digitaloceanclient.models.Image
        """

        if type_:
            if type_ in ['distribution', 'application']:
                params = {'type': type_}
            elif type_ == 'private':
                params = {'private': True}
            else:
                raise ValueError(f'Invalid type: {type_}')
        else:
            params = None

        return super().all(params)

    def get(self, image_id=None, slug=None):
        """
        Retrieve an image by ID or slug.

        Parameters
        ----------
        image_id : str
            The ID of the specified image.
        slug : str, optional
            The slug of the specified image.

        Returns
        -------
        digitaloceanclient.models.Image
        """

        if image_id == None and slug == None:
            raise ValueError('Please specify the image ID or the image slug.')
        if not image_id:
            image_id = slug
        return super().get(image_id)
