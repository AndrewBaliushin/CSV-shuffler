import csv
import random
import sys
from CsvParser import CsvParser
from DateHelper import DateHelper
import datetime

def main():
    if len(sys.argv) == 4:
        path_to_original_csv = sys.argv[1]
        lines_in_output_file = int(sys.argv[2])
        output_file_path = sys.argv[3]

        csv_parser = CsvParser(path_to_csv=path_to_original_csv, delimiter=';')

        device_ids_list = list(csv_parser.get_unique_values_for_col(1))
        log_msgs_list = list(csv_parser.get_unique_values_for_col(3))
        severity_list = list(csv_parser.get_unique_values_for_col(4))

        with open(output_file_path, 'wb') as csvfile:
            appender = csv.writer(csvfile, delimiter=';')
            for x in range(0, lines_in_output_file):
                rndm_date_in_interval = DateHelper.get_random_date_from_interval(datetime.datetime.now(), 90)
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
