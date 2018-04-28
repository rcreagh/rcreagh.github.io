#! usr/bin/python3

""" This program is just to cause a timestamp to be written to a csv to be
displayed on a web page. This is purely for testing/learning purposes."""

import time

now = time.time()
txt_file = open("timestamps.txt", "w")
txt_file.write("Last time python program was run: " + str(now))
txt_file.close()
