from digitaloceanclient.models import BillingHistory


def test_load_from_json():
    data = {
        "description": "Invoice for May 2018",
        "amount": "12.34",
        "invoice_id": "123",
        "invoice_uuid": "example-uuid",
        "date": "2018-06-01T08:44:38Z",
        "type": "Invoice"
    }

    b = BillingHistory(data)

    assert b.description == 'Invoice for May 2018'
    assert b.amount == 12.34
    assert b.invoice_id == '123'
    assert b.invoice_uuid == 'example-uuid'
    assert b.date == '2018-06-01T08:44:38Z'
    assert b.type == 'Invoice'
