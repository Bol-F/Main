import logging

logging.basicConfig(
    level=logging.INFO,
    filename='file_operations.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger()

with open('this.txt', 'w') as file:
    file.write('Hello, this is a new file!\n')
    file.write('Second line of text.')


def read_file(filename):
    try:
        with open(filename, 'r') as file_test:
            content = file_test.read()
            print("File content:")
            print(content)
            logger.info(f"Successfully read '{filename}'")
    except FileNotFoundError:
        logger.error(f"FileNotFoundError: '{filename}' not found")
        print(f"Error: '{filename}' not found")


def show_logs():
    print("\n--- Log file content ---")
    with open('file_operations.log', 'r') as log:
        print(log.read())
    logger.info("Successfully read 'file_operations.log'")


read_file('this.txt')
read_file('one.txt')
print('*' * 100)
show_logs()
