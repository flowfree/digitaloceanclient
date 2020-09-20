from . import Model
from .region import Region


class FloatingIPAction(Model):
    # Unique identifier
    id = ''

    # The status of the action
    status = ''

    # Type of the action
    type = ''

    # When the action was initiated
    started_at = ''

    # When the action was completed
    completed_at = ''

    # A unique identifier for the resource that the action is 
    # associated with
    resource_id = ''

    # The type of resource that the action is associated with
    resource_type = ''

    # Full region object containing information about the region 
    # where the action occurred
    region = None

    # The slug for the region object
    region_slug = ''

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass
