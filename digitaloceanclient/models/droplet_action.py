from . import Model
from .region import Region


class DropletAction(Model):
    """
    Represents a task that can be executed on a Droplet.

    Attributes
    ----------
    id : str
        The unique identifier for the action.
    status : str
        The current status of the action. Valid values: in-progress, completed, errored.
    type : str
        The type of action that the event is executing (reboot, power_off, etc.)
    started_at : str
        When the action was initiated
    completed_at : str
        When the action was completed
    resource_id : str
        A unique identifier for the resource that the action is associated with.
    resource_type : str
        The type of resource that the action is associated with.
    region : digitaloceanclient.models.Region
        The region where the action occurred.
    region_slug : str
        The slug for the region above.
    """

    id = ''
    status = ''
    type = ''
    started_at = ''
    completed_at = ''
    resource_id = None
    resource_type = ''
    region = None
    region_slug = ''

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except KeyError:
            pass
