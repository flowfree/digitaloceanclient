from . import Model
from .region import Region


class ImageAction(Model):
    TYPE_IN_PROGRESS = 'in-progress'
    TYPE_COMPLETED = 'completed'
    TYPE_ERRORED = 'errored'

    # Unique identifier for the image action
    id = ''
    
    # Valid values: in-progress, completed, errored
    status = ''

    # Type of the image action
    type = ''
    
    # When the action was initiated
    started_at = ''

    # When the action was completed
    completed_at = ''

    # A unique identifier for the resource that the action is associated with
    resource_id = ''

    # The type of resource that the action is associated with
    resource_type = ''

    # The full region object where the action occured
    region = None

    # The slug for the region above
    region_slug = ''

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass
