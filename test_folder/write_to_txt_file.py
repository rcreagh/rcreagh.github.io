#! usr/bin/python3

""" This program is just to cause a timestamp to be written to a csv to be
displayed on a web page. This is purely for testing/learning purposes."""

import datetime

now = datetime.datetime.now()
now.strftime('%Y-%m-%d')
txt_file = open("timestamp.txt", "w")
txt_file.write("Last time python program was run: " + str(now))
txt_file.close()
