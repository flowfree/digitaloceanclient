from .model import Model
from .region import Region


class ImageAction(Model):
    """
    Represent a task for the DigitalOcean image.

    Attributes
    ----------
    id : str
        Unique identifier for the image action
    status : str
        The status of the action. Valid values: in-progress, completed, errored
    type : str
        Type of the image action
    started_at : str
        When the action was initiated
    completed_at : str
        When the action was completed
    resource_id : str
        A unique identifier for the resource that the action is associated with
    resource_type : str
        The type of resource that the action is associated with
    region : digitaloceanclient.models.Region
        The full region object where the action occured
    region_slug : str
        The slug for the region above
    """

    TYPE_IN_PROGRESS = 'in-progress'
    TYPE_COMPLETED = 'completed'
    TYPE_ERRORED = 'errored'

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = ''
        self.status = ''
        self.type = ''
        self.started_at = ''
        self.completed_at = ''
        self.resource_id = ''
        self.resource_type = ''
        self.region = None
        self.region_slug = ''

        super().__init__(data)

        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass
