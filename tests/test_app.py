
from src.app import calculate_priority, get_status


def test_calculate_priority():
    assert calculate_priority(4, 5) == 20
    assert calculate_priority(2, 3) == 6


def test_high_priority():
    assert get_status(20) == "Жоғары"


def test_medium_priority():
    assert get_status(10) == "Орташа"


def test_low_priority():
    assert get_status(4) == "Төмен"
