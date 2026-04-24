from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self, data):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._file = filename

    def write_data(self, data):
        with open(self._file, "w") as f:
            f.write(data)

    def read_data(self):
        with open(self._file, "r") as f:
            return f.read()


class EncryptionDecorator(DataSource):
    def __init__(self, wrapee: DataSource):
        self._wrapee = wrapee

    def write_data(self, data):
        encrypted_data = self._encrypt(data)
        self._wrapee.write_data(encrypted_data)

    def read_data(self):
        encrypted_data = self._wrapee.read_data()
        return self._decrypt(encrypted_data)

    def _encrypt(self, data):
        return "".join(chr(ord(ch) + 1) for ch in data)

    def _decrypt(self, data):
        return "".join(chr(ord(ch) - 1) for ch in data)


data_src = FileDataSource("example.txt")
data_src.write_data("Hello Python")
print("Data from file: ", data_src.read_data())

encrypted_data_src = EncryptionDecorator(data_src)
encrypted_data_src.write_data("Hello Python")
print("Encrypted data form file: ", data_src.read_data())
print("Decrypted data: ", encrypted_data_src.read_data())
