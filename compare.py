#!/usr/bin/env python
# ================================================================================
# The program is to call comparison on TWO 10-column files or TWO 1-column files. 
# ================================================================================
import sys
import os
# from smc import *
from compare_signals import *
# from stools import *

def check_type(filename):
	"""checks the type of file being .her or .txt"""
	try: 
		with open(filename) as f:
			content = f.readlines()
			num_col = len(content[2].split())
			if num_col == 1:
				return 'TXT'
			elif num_col == 10:
				return 'HER'
			else:
				print "[ERROR]: Cannot recognize file type."
				return False 

	except IOError, e:
		print e 
		return False  
# end of check_type

def get_filename():
	file1 = ''
	file2 = ''
	para = []

	# get paths of two files 
	if len(sys.argv) >= 2:
		file1 = sys.argv[1]

	if len(sys.argv) >= 3:
		file2 = sys.argv[2]

	if len(sys.argv) > 3: 
		para = sys.argv[3:]
		for i in range(0, len(para)):
			try:
				para[i] = float(para[i])
			except ValueError:
				print "[ERROR]: invalid parameter."
				para = []
				break
	parameter = set_parameter(para)


	while not file1:
		file1 = raw_input('== Enter the path of file1: ')

	while not file2:
		file2 = raw_input('== Enter the path of file2: ')
	return parameter, file1, file2

# end of get_filename

if __name__ == "__main__":
	parameter, file1, file2 = get_filename()

	# checking file types 
	if check_type(file1) == check_type(file2) == 'TXT':
		compare_txt(parameter, file1, file2)
	elif check_type(file1) == check_type(file2) == 'HER':
		compare_her(parameter, file1, file2, False)

