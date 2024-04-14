from nums import one, two, three, four


def test_one():
    assert one() == 1


def test_two():
    assert two() == 2


def test_three():
    assert three() == 3


def test_four():
    assert four() == 4


def test_one_plus_two():
    assert one() + two() == 3
    assert one() + two() == three()
