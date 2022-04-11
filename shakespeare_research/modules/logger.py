import logging
import os, sys


# Logger system init
class Logger:
	def __init__(self, logfile):
		# Remove older log
		if os.path.exists(logfile):
			os.remove(logfile)

		# Config the base logging system
		logging.basicConfig(format="%(levelname)s %(asctime)s - %(message)s",
		                    level=logging.DEBUG, handlers=[
					        logging.FileHandler(logfile),
					        logging.StreamHandler(sys.stdout)])
