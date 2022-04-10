import os
import logging
from modules.research import Research
from modules.logger import Logger
from dotenv import load_dotenv
load_dotenv(".env")


def main():
	# Initialize log system and research module system
	Logger(os.getenv('LOGGING_FILE'))
	research = Research()

	# Read the files configurated into the dotenv variables
	text_merged = research.readFiles(os.getenv('TXT_SOURCE_FOLDER'), os.getenv('TMP_MERGED'))

	json_data = research.dataProcessing(text_merged)

	research.sendData(json_data, os.getenv('OUTPUT_SOURCE'), os.getenv('TMP_MERGED'))

	logging.info("Data processing finished")


if __name__ == '__main__':
	main()
