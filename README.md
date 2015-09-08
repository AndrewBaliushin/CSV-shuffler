CSV Shuffler for AIR CAP case
=============================

This script reads example of log file that is formated like this:
2014-10-01 00:05:37;NE-1711;NA;Cisco BGP trap flapping update;Major;NA;NA;NA

Script generates similar file where:
Date is generated randomly from interval that can be specified by params or selected from source file.
In case of source file date boundaries for generation will be youngest and oldest date.
Device id (col#2), Log message (col#4), Severity(col#5) are picked up randomly. (note that they are not linked together, so
same log message can have different severities in output file)

Usage example:
python CsvShuffler source_file.csv 1000(lines in output file) output_file_name.csv 2014-10-10(start date: y:m:d) 2014-10-20(end date)
