import json 

import jsonpickle


class Droplet(object):
    STATUS_NEW = 'new'
    STATUS_ACTIVE = 'active'
    STATUS_OFF = 'off'
    STATUS_ARCHIVE = 'archive'

    # Unique identifier for the droplet instance
    # This will be automatically generated upon droplet creation
    id = None

    # Human readable name set for the droplet instance
    name = ''

    # Memory of the droplet in megabytes
    memory = 0

    # The number of virtual CPUs
    vcpus = 0

    # The size of the disk in gigabytes
    disk = 0

    # A boolean value indicating whether the Droplet has been locked, 
    # preventing actions by users.
    locked = False

    # Time value given in ISO8601 combined date and time format that 
    # represents when the droplet was created
    created_at = ''

    # A status string indicating the state of the Droplet instance. 
    # This may be "new", "active", "off", or "archive".
    status = ''

    # An array of backup IDs of any backups that have been taken of 
    # the Droplet instance. Droplet backups are enabled at the time 
    # of the instance creation.
    backup_ids = []

    # An array of snapshot IDs of any snapshots created from the Droplet instance.
    snapshot_ids = []

    # An array of features enabled on this Droplet.
    features = []

    # The region that the Droplet instance is deployed in
    region = None

    # The base image used to create the Droplet instance
    image = None

    # The size object describing the droplet
    size = None

    # The unique slug identifier for the size of this Droplet.
    size_slug = ''

    # The details of the network that are configured for the Droplet instance. 
    # This is an object that contains keys for IPv4 and IPv6.
    networks = None

    # The current kernel. This will initially be set to the kernel of the base 
    # image when the Droplet is created
    kernel = None

    # An array of Tags the Droplet has been tagged with.
    tags = []

    # A flat array including the unique identifier for each Block Storage volume 
    # attached to the Droplet.
    volume_ids = []

    # A string specifying the UUID of the VPC to which the Droplet is assigned.
    vpc_uuid = ''


    def __str__(self):
        return self.name

    @staticmethod
    def from_json(d):
        if type(d) != dict:
            d = json.loads(d)
        d['py/object'] = 'digitaloceanclient.models.Droplet'
        for attrib in ['kernel', 'image', 'region']:
            try:
                d[attrib]['py/object'] = f'digitaloceanclient.models.{attrib.title()}'
            except (KeyError, TypeError):
                pass
        return jsonpickle.decode(json.dumps(d))
