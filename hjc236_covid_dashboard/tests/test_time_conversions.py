import time
from time_conversions import *


def test_minutes_to_seconds():
    assert minutes_to_seconds(1) == 60
    assert minutes_to_seconds("3") == 180


def test_hours_to_minutes():
    assert hours_to_minutes(3) == 180
    assert hours_to_minutes("2") == 120


def test_hhmm_to_seconds():
    assert hhmm_to_seconds("03:00") == 10800
    assert hhmm_to_seconds("12:38") == 45480
    assert hhmm_to_seconds("foo") is None
    assert hhmm_to_seconds("0800") is None


def test_current_time_seconds():
    assert current_time_seconds() > 0
