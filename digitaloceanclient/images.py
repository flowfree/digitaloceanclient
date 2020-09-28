from .http_client import HttpClient
from .models import Image


class Images(HttpClient):
    """
    Create, read, update, and delete images.

    Methods
    -------
    all(type_=None) 
        Retrieve all images.
    get(image_id=None, slug=None)
        Retrieve an image by ID or slug.
    update(image_id, name, description=None, distribution=None)
        Update an existing image.
    delete(image_id)
        Delete an image.
    """

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

        Raises
        ------
        digitaloceanclient.exceptions.APIError
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

    def create(self, name, url, region, distribution=None, description=None, tags=[]):
        """
        Create a new custom image.

        Parameters
        ----------
        name : str
            The display name to be given to an image.
        url : str
            A URL from which the custom Linux virtual machine image may be retrieved. 
            The image it points to must be in the raw, qcow2, vhdx, vdi, or vmdk format.
        region : str
            The slug identifier for the region where the image will initially be available.
        distribution : {"Arch Linux", 
                        "CentOS", 
                        "CoreOS", 
                        "Debian", 
                        "Fedora", 
                        "Fedora Atomic", 
                        "FreeBSD", 
                        "Gentoo", 
                        "openSUSE", 
                        "RancherOS", 
                        "Ubuntu"}, optional
            The name of a custom image's distribution.
        description : str
            An optional free-form text field to describe an image.
        tags : list
            A list of tag names to be applied to the image.

        Returns
        -------
        digitaloceanclient.models.Image

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        valid_distribution = [
            "Arch Linux", 
            "CentOS", 
            "CoreOS", 
            "Debian", 
            "Fedora", 
            "Fedora Atomic", 
            "FreeBSD", 
            "Gentoo", 
            "openSUSE", 
            "RancherOS", 
            "Ubuntu"
        ]
        if distribution and distribution not in valid_distribution:
            raise ValueError(f'Invalid distribution: {distribution}')
        payload = {
            'name': name,
            'url': url,
            'region': region,
            'distribution': distribution,
            'description': description,
            'tags': tags,
        }
        return super().create(payload=payload)

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

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        if image_id == None and slug == None:
            raise ValueError('Please specify the image ID or the image slug.')
        if not image_id:
            image_id = slug
        return super().get(image_id)

    def update(self, image_id, name, description=None, distribution=None):
        """
        Update an existing image.

        Parameters
        ----------
        image_id : str
            The ID of the specified image.
        name : str
            The new display name.
        description: str, optional
            An optional free-form text field to describe an image.
        distribution: str, optional
            The name of a custom image's distribution.

        Returns
        -------
        digitaloceanclient.models.Image

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'name': name}
        if description:
            payload['description'] = description
        if distribution:
            payload['distribution'] = distribution
        return super().update(image_id, payload=payload)
