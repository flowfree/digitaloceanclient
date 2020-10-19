from .model import Model


class Firewall(Model):
    """
    Represents a Firewall resource.

    Attributes
    ----------
    id : str
        The unique ID for the Firewall.
    status : str
        A status string indicating the current state of the firewall. 
        This can be "waiting", "succeeded", or "failed".
    created_at : str
        When the Firewall was created.
    pending_changes : list
        An array of objects each containing the fields "droplet_id", 
        "removing", and "status". It is provided to detail exactly which 
        Droplets are having their security policies updated. When empty, 
        all changes have been successfully applied.
    name : str
        The name of the Firewall.
    inbound_rules : list
        An object specifying the inbound access rules for a firewall.
    outbound_rules : list
        An object specifying the outbound access rules for a firewall.
    droplet_ids : list
        List of droplets assigned to the Firewall.
    tags : list
        List of tags assigned to the Firewall.
    """

    class BoundLocation(Model):
        def __init__(self, data):
            self.addresses = None
            self.droplet_ids = None
            self.load_balancer_uids = None
            self.tags = None

            super().__init__(data)

    class InboundRule(Model):
        def __init__(self, data):
            self.protocol = None
            self.ports = None
            self.sources = None

            super().__init__(data)

            try:
                self.sources = Firewall.BoundLocation(data['sources'])
            except (KeyError, TypeError, ValueError) as e:
                pass

    class OutboundRule(Model):
        def __init__(self, data):
            self.protocol = None
            self.ports = None
            self.destinations = None

            super().__init__(data)

            try:
                self.destinations = Firewall.BoundLocation(data['destinations'])
            except (KeyError, TypeError, ValueError) as e:
                pass

    class PendingChange(Model):
        def __init__(self, data):
            self.droplet_id = None
            self.removing = None
            self.status = None

            super().__init__(data)

    def __init__(self, data):
        self.id = None
        self.status = None
        self.created_at = None
        self.pending_changes = []
        self.name = None
        self.inbound_rules = []
        self.outbound_rules = []
        self.droplet_ids = None
        self.tags = None

        super().__init__(data)

        classes = {
            'inbound_rules': Firewall.InboundRule,
            'outbound_rules': Firewall.OutboundRule,
            'pending_changes': Firewall.PendingChange,
        }
        for attrib, class_ in classes.items():
            try:
                setattr(self, attrib, [class_(x) for x in data[attrib]])
            except (KeyError, ValueError, TypeError):
                pass
