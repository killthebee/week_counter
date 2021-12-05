import datetime

from dateutil import parser
from dateutil.parser._parser import ParserError


class PossibleDate:
    month_nums = {'января': '1', 'февраля': '2', 'марта': '3', 'апреля': '4', 'мая': '5', 'июня': '8',
                  'июля': '7', 'августа': '8', 'сентября': '9', 'октября': '10', 'ноября': '11', 'декабря': '12'}
    week_counter_start = datetime.date(2019, 1, 1)
    first_week_days = 5
    days_in_week = 7
    initial_week_count = 2

    def __init__(self, possible_date: str):
        self.possible_date = possible_date

    def _transform_letters_to_month(self):
        """
        make possible_date string more "parseble" if possible
        """
        normalized_possible_date = self._delete_empty_strings(self._normalize_date(self.possible_date).split(' '))
        for index, date_part in enumerate(normalized_possible_date):
            month_num = self.month_nums.get(date_part, None)
            if month_num:
                self._put_month_on_first_position(normalized_possible_date, month_num, index)
                break
        else:
            try:
                month_num = normalized_possible_date[1]
                self._put_month_on_first_position(normalized_possible_date, month_num, 1)
            except IndexError:
                return
        self.possible_date = ' '.join(normalized_possible_date)

    @staticmethod
    def _put_month_on_first_position(normalized_possible_date, month_num, index):
        normalized_possible_date.pop(index)
        normalized_possible_date.insert(0, month_num)

    @staticmethod
    def _delete_empty_strings(normalized_possible_date):
        return list(filter(None, normalized_possible_date))

    @staticmethod
    def _normalize_date(possible_date: str) -> str:
        chars_to_replace = """_()-.\,"""
        for character in possible_date:
            if character in chars_to_replace:
                possible_date = possible_date.replace(character, ' ')
        return possible_date

    def parse_date(self):
        self._transform_letters_to_month()
        try:
            return parser.parse(self.possible_date).date()
        except ParserError:
            return None

    def count_weeks(self, date: datetime.date) -> int:
        date_delta = (date - self.week_counter_start).days
        if date_delta <= 4:
            return 1
        return int((date_delta - self.first_week_days) / self.days_in_week + self.initial_week_count)
