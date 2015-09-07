CSV Shuffler for AIR CAP case
=============================

This script reads example of log file that is formated like this:
2014-10-01 00:05:37;NE-1711;NA;Cisco BGP trap flapping update;Major;NA;NA;NA

Script generates similar file where:
Date is from current date to date that was 90 days ago;
Device id (col#2), Log message (col#4), Severity(col#5) are picked up randomly from source data;

Usage example:
python CsvShuffler source_file.csv 1000(lines in output file) output_file_name.csv
