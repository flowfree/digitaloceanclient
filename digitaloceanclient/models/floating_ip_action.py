from . import Model
from .region import Region


class FloatingIPAction(Model):
    """
    Represents a command that can be given to a DigitalOcean Floating IP.

    Attributes
    ----------
    id : str
        Unique identifier for the action.
    status : str
        The status of the action
    type : str
        Type of the action
    started_at : str
        When the action was initiated
    completed_at : str
        When the action was completed
    resource_id : str
        A unique identifier for the resource that the action is associated with
    resource_type : str
        The type of resource that the action is associated with
    region : digitaloceanclient.models.Region
        Full region object containing information about the region 
        where the action occurred.
    region_slug : str
        The slug for the region object
    """

    id = ''
    status = ''
    type = ''
    started_at = ''
    completed_at = ''
    resource_id = ''
    resource_type = ''
    region = None
    region_slug = ''

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass
