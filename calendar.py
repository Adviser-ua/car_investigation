# coding: utf-8
# Konstantyn Davidenko
from text_object import TextObject


class MyCalendar:

    def __init__(self, init_week=1, init_month=1, init_year=1800):
        self.init_week = init_month
        self.init_day = init_week
        self.init_year = init_year

        self.current_week = init_week
        self.current_month = init_month
        self.current_year = init_year

    def increment_date(self):
        self.current_week += 1
        if self.current_week >= 5:
            self.current_week = 1
            self.current_month += 1
        if self.current_month >= 13:
            self.current_year += 1
            self.current_month = 1

    def print_date(self):
        print('date', self.current_week, self.current_month, self.current_year)
