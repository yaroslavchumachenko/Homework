import logging

counter = 0

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None


    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            global counter 
            counter += 1
            logging.info(f"Opened {self.filename} in mode {self.mode}")
            return self.file
        except Exception as e:
            logging.error(f"Failed to open {self.filename} in mode {self.mode}: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            try:
                self.file.close()
                # global counter 
                # counter -= 1
                logging.info(f"Closed {self.filename}")
            except Exception as e:
                logging.error(f"Failed to close {self.filename}: {e}")
                raise

filename = "example.txt"

with FileContextManager(filename, 'w') as f:
    f.write("Hello, World!")
with FileContextManager(filename, 'a') as f:
    f.write("\nAppending some more text.")
with FileContextManager(filename, 'r') as f:
    print(f.read())

print("Number of open files:", counter)
