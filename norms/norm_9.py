import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="newfile_9.log",
                    format='%(asctime)s -%(levelname)s- %(message)s',
                    filemode='a')
logger = logging.getLogger()


try:
    with open("norm_9.txt", newline="", encoding="utf-8") as file:
        reader = file.read()
        print(reader)
except FileNotFoundError:
    logger.warning("File not found")


with open("norm_9.txt", mode="w", newline="") as file:
    file.write("this is a new line ")
    file.write("this is another line  ")
    file.write("this is another line ")


try:
    with open("norm_9_2.txt", newline="", encoding="utf-8") as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    logger.warning("There is no such file")
    raise FileNotFoundError("This file does not exist")