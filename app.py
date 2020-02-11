#!/usr/bin/python

import datetime
import logging
import time
import os
import sys
import traceback
import random
import string

class BusyPod(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def main(self):
        try:
            #formatter = json_log_formatter.JSONFormatter()
            #log_fmt = '%(asctime)-15s %(levelname)-8s %(message)s'
            log_fmt = '%(message)s'
            date_fmt = '%m-%d-%Y %H:%M:%S'
            log_level = logging.INFO
            if "LOG_TO_FILE" in os.environ:
                log_path = os.environ.get('LOG_PATH', '/var/log/')
                logging.basicConfig(filename=log_path + 'logs-a-lot.log', format=log_fmt, datefmt=date_fmt, level=log_level)
            else:
                logging.basicConfig(format=log_fmt, datefmt=date_fmt, level=log_level)

            while True:
                #datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S'),
                message="{ \"message\":\"%s\", \"forward_message_to_splunk\":\"%s\", \"Severity\" : \"INFO\" }" % ( ''.join(random.SystemRandom().choice(string.digits + string.ascii_letters) for _ in range(random.randint(50, 200))), str(bool(random.getrandbits(1))).lower())
                self.logger.info(message)
                #time.sleep(random.randint(20, 40))
                time.sleep(random.randint(1, 10))

        except KeyboardInterrupt:
            logging.critical("Terminating due to keyboard interrupt")
        except:
            logging.critical("Terminating due to unexpected error: %s", sys.exc_info()[0])
            logging.critical("%s", traceback.format_exc())

if __name__ == "__main__":
    BusyPod().main()
