__author__ = 'cpt2aba'

import calendar
import random

import datetime


class DateHelper():
    fmt = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def add_date(start_date, days_to_add):
        struct_time = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        end_date = struct_time + datetime.timedelta(days=days_to_add)
        print(end_date)

    @staticmethod
    def get_random_date_from_interval(start_date, days_to_subtract_from_date):
        '''
        Substract X days from original date and randomly returns date that is in interval between these two dates.
        :param start_date: format of 'datetime' module
        :param days_to_subtract_from_date: int
        :return:
        '''
        date_in_past = start_date - datetime.timedelta(days=days_to_subtract_from_date)
        today_timestamp = calendar.timegm(start_date.timetuple())
        date_in_past_timestamp = calendar.timegm(date_in_past.timetuple())
    
        ts_in_interval = random.randrange(date_in_past_timestamp, today_timestamp)
        return datetime.datetime.fromtimestamp(ts_in_interval)