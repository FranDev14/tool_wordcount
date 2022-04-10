import os, glob
import logging
import string
import json


class Research:
	def __init__(self):
		logging.info("Starting Research")

	# File reader function
	def readFiles(self, files, tmp):
		try:
			files = glob.glob(files)
			logging.info("Reading {} files".format(len(files)))

			if os.path.exists(tmp):
				os.remove(tmp)

			logging.info("Merging files into {}".format(tmp))
			with open(tmp, 'w') as o_file:
				for file_name in files:
					with open(file_name) as infile:
						for line in infile:
							o_file.write(line)
				o_file.close()

			txt_merged = open(tmp, 'r')

			return txt_merged

		except Exception as e:
			logging.error("Error readFiles module: {}".format(e))

	# Data Processing Function, for get all words and count. Return a dict for treatment
	def dataProcessing(self, txt_data):
		try:
			data = dict()

			logging.info("Start of data processing")

			# Data processing loop, get the lines, clean and count words
			for line in txt_data:
				# Clean the line, remove strange punctuation and lower all the words
				line = line.strip()
				line = line.lower()
				line = line.translate(line.maketrans("", "", string.punctuation))
				words = line.split(" ")

				# Loop for iterate over each word in line
				for word in words:
					if word in data:
						data[word] = data[word] + 1
					else:
						data[word] = 1

			return data

		except Exception as e:
			logging.error("Error dataProcessing module: {}".format(e))

	# Write the data into a single file function
	def sendData(self, data_send, output_file, tmp):
		try:
			logging.info("Starting dumping data into {}".format(output_file))

			if os.path.exists(output_file):
				os.remove(output_file)

			with open(output_file, 'w') as f:
				json.dump(data_send, f, indent=4)

		except Exception as e:
			logging.error("Error sendData module: {}".format(e))