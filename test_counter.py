from utils import PossibleDate
import datetime


def test_date_parsing():
    possible_date = PossibleDate('3 января 2019')
    assert possible_date.parse_date() == datetime.date(2019, 1, 3)


def test_date_parsing_b():
    possible_date = PossibleDate('3- 12- 2019')
    assert possible_date.parse_date() == datetime.date(2019, 12, 3)


def test_wrong_date_parsing():
    possible_date = PossibleDate('300 января 2019')
    assert possible_date.parse_date() is None


def test_counting():
    possible_date = PossibleDate('3 января 2019')
    parsed_date = possible_date.parse_date()
    assert possible_date.count_weeks(parsed_date) == 1

def test_counting_b():
    possible_date = PossibleDate('3 февраля 2019')
    parsed_date = possible_date.parse_date()
    assert possible_date.count_weeks(parsed_date) == 6



