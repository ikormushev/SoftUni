from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def add_in_storage(element_to_add, element_iterable: list):
        if element_to_add not in element_iterable:
            element_iterable.append(element_to_add)

    def add_category(self, category: Category):
        self.add_in_storage(category, self.categories)

    def add_topic(self, topic: Topic):
        self.add_in_storage(topic, self.topics)

    def add_document(self, document: Document):
        self.add_in_storage(document, self.documents)

    @staticmethod
    def edit_in_storage(element_id: int, element_iterable: list, *args):
        element_to_edit = [element for element in element_iterable if element.id == element_id]
        if element_to_edit:
            element_to_edit[0].edit(*args)

    def edit_category(self, category_id: int, new_name: str):
        self.edit_in_storage(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.edit_in_storage(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.edit_in_storage(document_id, self.documents, new_file_name)

    @staticmethod
    def delete_from_storage(element_id: int, element_iterable: list):
        element_to_remove = [element for element in element_iterable if element.id == element_id]
        if element_to_remove:
            element_iterable.remove(element_to_remove[0])

    def delete_category(self, category_id: int):
        self.delete_from_storage(category_id, self.categories)

    def delete_topic(self, topic_id: int):
        self.delete_from_storage(topic_id, self.topics)

    def delete_document(self, document_id: int):
        self.delete_from_storage(document_id, self.documents)

    def get_document(self, document_id: int):
        current_document = [document for document in self.documents if document.id == document_id]
        if current_document:
            return current_document[0]

    def __repr__(self):
        return "\n".join([document.__repr__() for document in self.documents])
