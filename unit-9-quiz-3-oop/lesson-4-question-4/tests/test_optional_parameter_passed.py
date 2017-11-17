def test_optional_parameter_passed():
    c2 = Car(model='Toyota MR2', color='Blue', convertible=True)

    assert c2.model == 'Toyota MR2'
    assert c2.color == 'Blue'
    assert c2.convertible == True
