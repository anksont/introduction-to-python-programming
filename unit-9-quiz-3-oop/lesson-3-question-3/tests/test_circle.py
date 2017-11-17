def test_circle():
    c1 = Circle(radius=1)
    assert c1.get_area() == 3.14

    c2 = Circle(radius=3)
    assert c2.get_area() == 28.26

    c3 = Circle(radius=9)
    assert c3.get_area() == 254.34
