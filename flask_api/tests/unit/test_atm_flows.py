def test_login_with_fixture(login):
    """
    login credentials verified
    """
    assert login[0] == 200

def test_list_atms_with_fixture(list_atms):
    """
    number of atms reconciled
    """
    assert list_atms[0] == 200
    assert list_atms[1] == 2

def test_insert_atms_with_fixture(insert_atms):
    """
    number of atms reconciled
    """
    assert insert_atms[0] == 200


def test_update_with_fixture(update_atms):
    """
    status reconciled for update operation
    """
    assert update_atms[0] == 200

def test_delete_with_fixture(delete_atms):
    """
    status reconciled for update operation
    """
    assert delete_atms[0] == 200

def test_insert_atms_invalid_payload_with_fixture(insert_atms_invalid_payload):
    """
    number of atms reconciled
    """
    assert insert_atms_invalid_payload[1]['data'] == "please provid valid atm_details payload"

def test_update_invalid_payload_with_fixture(update_atms_invalid_payload):
    """
    status reconciled for update operation
    """
    assert update_atms_invalid_payload[1]['data'] == "please provid valid id and atm_details"

def test_delete_invalid_payload_with_fixture(delete_atms_invalid_payload):
    """
    status reconciled for update operation
    """
    assert delete_atms_invalid_payload[1]['data'] == "please provid valid id"

def test_login_invalid_payload_with_fixture(login_invalid_payload):
    """
    status reconciled for update operation
    """
    assert login_invalid_payload[1]['data'] == "please provid valid Login Details"    

def test_invalid_payload_with_fixture(invalid_payload):
    """
    status reconciled for update operation
    """
    assert invalid_payload[1]['message'] == ('Internal Error has occurred while processing the request')