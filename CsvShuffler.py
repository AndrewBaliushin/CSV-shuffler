import csv
import random
import sys
import datetime

from helpers.CsvParser import CsvParser
from helpers.DateHelper import DateHelper


def main():
    if len(sys.argv) == 4 or len(sys.argv) == 6:
        path_to_original_csv = sys.argv[1]
        lines_in_output_file = int(sys.argv[2])
        output_file_path = sys.argv[3]

        csv_parser = CsvParser(path_to_csv=path_to_original_csv, delimiter=';')

        # if dates are specified by input params then use them
        # else use youngest and oldest dates in original file as interval for date generation
        if len(sys.argv) > 4:
            start_date = datetime.datetime.strptime(sys.argv[4], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(sys.argv[5], "%Y-%m-%d")
        else:
            date_list = csv_parser.get_unique_values_for_col(0)
            min_and_max_date_arr = DateHelper.find_min_and_max_date_in_list(date_list)
            start_date = min_and_max_date_arr[0]
            end_date = min_and_max_date_arr[1]

        device_ids_list = list(csv_parser.get_unique_values_for_col(1))
        log_msgs_list = list(csv_parser.get_unique_values_for_col(3))
        severity_list = list(csv_parser.get_unique_values_for_col(4))

        with open(output_file_path, 'wb') as csvfile:
            appender = csv.writer(csvfile, delimiter=';')
            for x in range(0, lines_in_output_file):
                rndm_date_in_interval = DateHelper.get_random_date_from_interval(start_date, end_date)
                random_device_id = random.choice(device_ids_list)
                random_severity = random.choice(severity_list)
                random_log_msg = random.choice(log_msgs_list)

                appender.writerow([rndm_date_in_interval, random_device_id, "NA", random_log_msg, random_severity,
                                  "NA", "NA", "NA"])
        print(output_file_path + " file successfully created")

    else:
        f = open("README.md", "r")
        print(f.read())
        f.close()


if __name__ == "__main__":
    main();
