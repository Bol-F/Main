import logging

logging.basicConfig(filename='file_manager.log', format='%(asctime)s - %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

class FileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
            return self.file

        except Exception as e :
            logger.error(f'Can not open the file {self.file_path}: {e}')
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f'Error occur {exc_val}')
            if self.file:
                self.file.close()
            return True



with FileManager('file_to_read', 'r') as f:
    print(f.read())