from digitaloceanclient.models import Networks


def test_load_from_json():
    data = {
      "v4":[
        {
          "ip_address":"104.131.186.241",
          "netmask":"255.255.240.0",
          "gateway":"104.131.176.1",
          "type":"public"
        }
      ],
      "v6":[
        {
          "ip_address":"2604:A880:0800:0010:0000:0000:031D:2001",
          "netmask":64,
          "gateway":"2604:A880:0800:0010:0000:0000:0000:0001",
          "type":"public"
        }
      ]
    }

    networks = Networks(data)

    assert networks.v4[0].ip_address == data['v4'][0]['ip_address']
    assert networks.v4[0].netmask == data['v4'][0]['netmask']
    assert networks.v4[0].gateway == data['v4'][0]['gateway']
    assert networks.v4[0].type == data['v4'][0]['type']
    assert networks.v6[0].ip_address == data['v6'][0]['ip_address']
    assert networks.v6[0].netmask == data['v6'][0]['netmask']
    assert networks.v6[0].gateway == data['v6'][0]['gateway']
    assert networks.v6[0].type == data['v6'][0]['type']
