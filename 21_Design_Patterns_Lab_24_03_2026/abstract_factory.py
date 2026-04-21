from abc import ABC, abstractmethod
import json


class JsonDataExporter(ABC):
    @abstractmethod
    def export(self, data) -> str:
        pass


class CsvDataExporter(ABC):
    @abstractmethod
    def export(self, data) -> str:
        pass


class DataExporterFactory(ABC):
    @abstractmethod
    def get_json_exporter(self) -> JsonDataExporter:
        pass

    @abstractmethod
    def get_csv_exporter(self) -> CsvDataExporter:
        pass

class SimpleJsonDataExporter(JsonDataExporter):
    def export(self, data) -> str:
        return json.dumps(data)


class SimpleCsvDataExporter(CsvDataExporter):
    def export(self, data) -> str:
        return "presenting data in csv"


class SimpleDataExporterFactory(DataExporterFactory):
    def get_json_exporter(self) -> JsonDataExporter:
        return SimpleJsonDataExporter()

    def get_csv_exporter(self) -> CsvDataExporter:
        return SimpleCsvDataExporter()


factory = SimpleDataExporterFactory()
json_exporter = factory.get_json_exporter()
csv_exporter = factory.get_csv_exporter()

data = {"name": "Ivan", "age": 35}

print(json_exporter.export(data))