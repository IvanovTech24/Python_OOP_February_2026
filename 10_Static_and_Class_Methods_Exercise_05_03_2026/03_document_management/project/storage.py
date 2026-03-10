from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        self.__add_object(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        self.__add_object(topic, self.topics)

    def add_document(self, document: Document) -> None:
        self.__add_object(document, self.documents)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id) -> None:
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id) -> None:
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id) -> None:
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id) -> "Document":
        return self.__find_object(document_id, self.documents)


    def __repr__(self):
        return "\n".join([d.__str__() for d in self.documents])

    @staticmethod
    def __add_object(obj, collection):
        if obj not in collection:
            collection.append(obj)

    def __edit_object(self, object_id, collection, *new_value) -> None:
        obj = self.__find_object(object_id, collection)
        if obj:
            obj.edit(*new_value)

    def __delete_object(self, object_id, collection) -> None:
        obj = self.__find_object(object_id, collection)
        if obj:
            collection.remove(obj)

    @staticmethod
    def __find_object(object_id, collection) -> Category | Topic | Document | None:
        return next((o for o in collection if o.id == object_id), None)
