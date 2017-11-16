def test_optional_parameter_not_passed():
    c1 = Car(model='BMW E46', color='Red')

    assert c1.model == 'BMW E46'
    assert c1.color == 'Red'
    assert c1.convertible == False
