from abc import ABC, abstractmethod

class DataExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class CsvDataExporter(DataExporter):
    def export(self, data) -> str:
        return f"Exporting to CSV {data}"


class DataExporterFactory(ABC):
    @abstractmethod
    def get_exporter(self) -> DataExporter:
        pass


class CsvDataExporterFactory(DataExporterFactory):
    def get_exporter(self) -> DataExporter:
        return CsvDataExporter()


def client_code(_factory: DataExporterFactory, data):
    exporter = _factory.get_exporter()
    print(exporter.export(data))


factory = CsvDataExporterFactory()
client_code(factory, "some data")
