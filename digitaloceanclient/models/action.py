from . import Model 
from .region import Region


class Action(Model):
    """
    Represents record of events that have occured on the resources.

    Attributes
    ----------
    id : int
        Unique identifier for the action.
    status : str
        The current status of the action: in-progress, completed, errored.
    type : str
        The type of the action.
    started_at : str
        When the action was initiated.
    completed_at : str
        When the action was completed.
    resource_id : int
        Unique identifier for the resource that the action is associated with.
    resource_type : str
        The type of the resource that the action is associated with.
    region : digitaloceanclient.models.Region
        Full Region object about the region where the action occured.
    region_slug : str
        The slug for the region above.
    """

    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_COMPLETED = 'completed'
    STATUS_ERRORED = 'errored'

    id = None
    status = None
    type = None
    started_at = None
    completed_at = None
    resource_id = None
    resource_type = None
    region = None
    region_slug = None

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass

    def all(self, *args, **kwargs):
        raise NotImplementedError

    def is_in_progress(self):
        return self.status == self.STATUS_IN_PROGRESS
    
    def is_completed(self):
        return self.status == self.STATUS_COMPLETED

    def is_errored(self):
        return self.status == self.STATUS_ERRORED
