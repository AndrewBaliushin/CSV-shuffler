__author__ = 'Andrey Baliushin'

import calendar
import random

import datetime


class DateHelper():
    fmt = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def add_date(start_date, days_to_add):
        struct_time = datetime.datetime.strptime(start_date, DateHelper.fmt)
        end_date = struct_time + datetime.timedelta(days=days_to_add)
        print(end_date)

    @staticmethod
    def get_random_date_from_interval(start_date, end_date):
        '''
        Substract X days from original date and randomly returns date that is in interval between these two dates.
        :param start_date: format of 'datetime' module
        :param days_to_subtract_from_date: int
        :return:
        '''
        start_date_as_timestamp = calendar.timegm(start_date.timetuple())
        end_date_as_timestamp = calendar.timegm(end_date.timetuple())
    
        random_timestamp_in_interval = random.randrange(start_date_as_timestamp, end_date_as_timestamp)
        return datetime.datetime.fromtimestamp(random_timestamp_in_interval)

    @staticmethod
    def find_min_and_max_date_in_list(date_list):
        '''
        :param date_list: as datetime object
        :return: list of dates where index[0] -- oldest date, [1] -- youngest date
        '''
        oldest_date = datetime.datetime.now()
        youngest_date = datetime.datetime.strptime("1900-1-1 20:10:10", DateHelper.fmt)
        for i, val in enumerate(date_list):
            if datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S") < oldest_date:
                oldest_date = datetime.datetime.strptime(val, DateHelper.fmt)
            if datetime.datetime.strptime(val, DateHelper.fmt) > youngest_date:
                youngest_date = datetime.datetime.strptime(val, DateHelper.fmt)
        return [oldest_date, youngest_date]