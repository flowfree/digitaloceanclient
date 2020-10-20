from digitaloceanclient.models import Firewall


def test_load_from_json():
    data = {
        "id": "bb4b2611-3d72-467b-8602-280330ecd65c",
        "name": "firewall",
        "status": "waiting",
        "inbound_rules": [{
            "protocol": "tcp",
            "ports": "80",
            "sources": {
                "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"]
            }
        }, {
            "protocol": "tcp",
            "ports": "22",
            "sources": {
                "tags": ["gateway"],
                "addresses": ["18.0.0.0/8"]
            }
        }],
        "outbound_rules": [{
            "protocol": "tcp",
            "ports": "80",
            "destinations": {
                "addresses": ["0.0.0.0/0", "::/0"]
            }
        }],
        "created_at": "2017-05-23T21:24:00Z",
        "droplet_ids": [8043964],
        "tags": [],
        "pending_changes": [{
            "droplet_id": 8043964,
            "removing": False,
            "status": "waiting"
        }]
    }

    firewall = Firewall(data)
    assert model_matches(firewall, data)


def model_matches(a, b):
    is_matches = a.id == b['id'] and \
                 a.name == b['name'] and \
                 a.status == b['status']

    for idx, a_inbound_rule in enumerate(a.inbound_rules):
        b_inbound_rule = b['inbound_rules'][idx]

        is_matches &= a_inbound_rule.protocol == \
                      b_inbound_rule['protocol'] and \
                      a_inbound_rule.ports == \
                      b_inbound_rule['ports']
        
        if a_inbound_rule.sources:
            if a_inbound_rule.sources.tags:
                is_matches &= a_inbound_rule.sources.tags == \
                              b_inbound_rule['sources']['tags']
            if a_inbound_rule.sources.addresses:
                is_matches &= a_inbound_rule.sources.addresses == \
                              b_inbound_rule['sources']['addresses']
            if a_inbound_rule.sources.load_balancer_uids:
                is_matches &= a_inbound_rule.sources.load_balancer_uids == \
                              b_inbound_rule['sources']['load_balancer_uids']

    for idx, a_outbound_rule in enumerate(a.outbound_rules):
        b_outbound_rule = b['outbound_rules'][idx]

        is_matches &= a_outbound_rule.protocol == \
                      b_outbound_rule['protocol'] and \
                      a_outbound_rule.ports == \
                      b_outbound_rule['ports']
        
        if a_outbound_rule.destinations:
            if a_outbound_rule.destinations.tags:
                is_matches &= a_outbound_rule.destinations.tags == \
                              b_outbound_rule['destinations']['tags']
            if a_outbound_rule.destinations.addresses:
                is_matches &= a_outbound_rule.destinations.addresses == \
                              b_outbound_rule['destinations']['addresses']
            if a_outbound_rule.destinations.load_balancer_uids:
                is_matches &= a_outbound_rule.destinations.load_balancer_uids == \
                              b_outbound_rule['destinations']['load_balancer_uids']

    for idx, a_pending_change in enumerate(a.pending_changes):
        b_pending_change = b['pending_changes'][idx]
        is_matches &= a_pending_change.droplet_id == b_pending_change['droplet_id'] and \
                      a_pending_change.removing == b_pending_change['removing'] and \
                      a_pending_change.status == b_pending_change['status']

    is_matches &= a.created_at == b['created_at'] and \
                  a.droplet_ids == b['droplet_ids'] and \
                  a.tags == b['tags']

    return is_matches
