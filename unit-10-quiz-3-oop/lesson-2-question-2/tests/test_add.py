def test_add():
    calc = Calculator()
    assert hasattr(calc, 'add'), "The Calculator class doesn't seem to have an add method"

    assert calc.add(2, 3) == 5
    assert calc.add(10, 11) == 21
