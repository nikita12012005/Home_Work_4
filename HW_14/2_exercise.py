class Writer:
    def write(self, data):
        raise NotImplementedError()


class FileWriter(Writer):
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)
        print(f"Data written to file: {self.filename}")


class WriterProxy(Writer):
    def __init__(self, writer):
        self.writer = writer

    def write(self, data):
        if self._is_authorized():
            self.writer.write(data)
        else:
            print("Unauthorized access. Write operation not allowed.")

    def _is_authorized(self):
        # Add your authorization logic here
        # For example, you can check if the user is logged in or has appropriate permissions
        # Return True if authorized, False otherwise
        return False


# Usage example
filename = "data.txt"
file_writer = FileWriter(filename)
proxy = WriterProxy(file_writer)
proxy.write("Hello, World!")
