from numpy.oldnumeric.random_array import randint

__author__ = 'andrew'

class SameDataRandomChoice():

    def shuffle(self, input_data):
        return input_data[randint(0, len(input_data))]

