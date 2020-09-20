from . import Model
from .region import Region


class DropletAction(Model):
    # Unique identifier
    id = ''

    # The current status of the action
    # The value of this attribute will be "in-progress", "completed", or "errored"
    status = ''

    # The type of action that the event is executing (reboot, power_off, etc.)
    type = ''

    # When the action was initiated
    started_at = ''

    # When the action was completed
    completed_at = ''

    # A unique identifier for the resource that the action is associated with
    resource_id = None

    # The type of resource that the action is associated with
    resource_type = ''

    # The region where the action occurred
    region = None

    # The slug for the region above
    region_slug = ''

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except KeyError:
            pass
