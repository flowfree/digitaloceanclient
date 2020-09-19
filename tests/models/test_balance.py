from digitaloceanclient.models import Balance


def test_load_from_json():
    data = {
        "month_to_date_balance": "23.44",
        "account_balance": "12.23",
        "month_to_date_usage": "11.21",
        "generated_at": "2019-07-09T15:01:12Z"
    }

    balance = Balance(data)

    assert balance.month_to_date_balance == 23.44
    assert balance.account_balance == 12.23
    assert balance.month_to_date_usage == 11.21
    assert balance.generated_at == '2019-07-09T15:01:12Z'
