pyramid_5_expected = """
#
##
###
####
#####
""".lstrip()


def test_ascending_pyramid():
    assert nested_pyramid(5, '#', 'ASC') == pyramid_5_expected
