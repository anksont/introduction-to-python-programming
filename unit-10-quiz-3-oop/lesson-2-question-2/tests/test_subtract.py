def test_subtract():
    calc = Calculator()
    assert hasattr(calc, 'subtract'), "The Calculator class doesn't seem to have a subtract method"

    assert calc.subtract(10, 3) == 7
    assert calc.subtract(1, 10) == -9
