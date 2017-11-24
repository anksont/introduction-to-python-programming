box_1x1_expected = """
@
""".lstrip()

def test_second_box():
    assert create_box(1, 1, '@') == box_1x1_expected
