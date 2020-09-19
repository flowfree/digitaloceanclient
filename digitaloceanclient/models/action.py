from . import Model 
from .region import Region


class Action(Model):
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_COMPLETED = 'completed'
    STATUS_ERRORED = 'errored'

    # Unique identifier for the action
    id = None

    # The current status of the action
    # This can be "in-progress", "completed", or "errored"
    status = None

    # The type of the action
    type = None

    # A time value given in ISO8601 combined date and time format 
    # that represents when the action was initiated
    started_at = None

    # A time value given in ISO8601 combined date and time format 
    # that represents when the action was completed
    completed_at = None

    # A unique identifier for the resource that the action is 
    # associated with
    resource_id = None

    # The type of resource that the action is associated with
    resource_type = None

    # A full region object containing information about the region 
    # where the action occurred
    region = None

    # A slug representing the region where the action occurred
    region_slug = None

    def __init__(self, data):
        super().__init__(data)
        self.region = Region(data['region'])
