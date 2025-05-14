import logging

logging.basicConfig(level=logging.INFO, filename='file_operations.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s', )

logger = logging.getLogger()

with open('this.txt', 'w') as file:
    file.write('Hello, this is my file!\n')
    file.write('this is for testing')


def read_file(filename):
    try:
        with open(filename, 'r') as file_test:
            content = file_test.read()
            print(content)
    except FileNotFoundError as e:
        logger.error(f'{e}: {filename} not found')

def show_logs():
    a = 'Log content'
    print(f'{a:.^50}')
    with open('file_operations.log', 'r') as log:
        print(log.read())

read_file('this.txt')
read_file('another.txt')
show_logs()

