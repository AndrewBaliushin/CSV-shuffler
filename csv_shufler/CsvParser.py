__author__ = 'andrew'

import csv
import sets


class CsvParser():

    number_of_columns_in_css = None

    dict_of_sets_of_column_values = dict(short='dict', long='dictionary')
    '''
        Dictionary of sets with values from csv columns.
        column_id : set("of", "values")
    '''

    def __init__(self, path_to_csv, delimiter):
        self.parse_csv(path_to_csv, delimiter)

    def parse_csv(self, path_to_csv, delimiter):
        with open(path_to_csv, 'rb') as csv_file:
            parsed_rows = csv.reader(csv_file, delimiter=delimiter)
            for row in parsed_rows:
                self.set_number_of_columns_in_csv(len(row))
                for column_id in range(0, len(row)):
                    self.add_column_value_to_collection(column_id, row[column_id])


    def add_column_value_to_collection(self, col_id, col_value):
        try:    # if index with this id not yet exist we will create it
            self.dict_of_sets_of_column_values[col_id]
        except KeyError:
            self.dict_of_sets_of_column_values[col_id] = set()
        self.dict_of_sets_of_column_values[col_id].add(col_value)

    def get_unique_values_for_col(self, col_index):
        return self.dict_of_sets_of_column_values[col_index]

    def set_number_of_columns_in_csv(self, num_of_cols):
        if self.number_of_columns_in_css is None:
            self.number_of_columns_in_css = num_of_cols