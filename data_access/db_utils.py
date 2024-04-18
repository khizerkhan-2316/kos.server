from config.firebase_config import db


class DBUtils:
    def __init__(self):
        self.db = db

    def get_document(self, collection_name, document_id):

        doc_ref = self.db.collection(collection_name).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def add_document(self, collection_name, document_data):

        doc_ref = self.db.collection(collection_name).document()
        doc_ref.set(document_data)
        return doc_ref.id

    def update_document(self, collection_name, document_id, update_data):

        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.update(update_data)

    def delete_document(self, collection_name, document_id):

        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.delete()

    def get_all_documents(self, collection_name):

        docs = self.db.collection(collection_name).stream()
        documents = []
        for doc in docs:
            documents.append(doc.to_dict())
        return documents
