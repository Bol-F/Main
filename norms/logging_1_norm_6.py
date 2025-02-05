import logging
import csv

logging.basicConfig(
    level=logging.DEBUG,
    filename="newfile_6.log",
    format='%(asctime)s -%(levelname)s- %(message)s',
    filemode='a'
)
logger = logging.getLogger()


try:
    with open("output1.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    logger.warning("File not found")


try:
    with open("output2.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    logger.warning("File not found")