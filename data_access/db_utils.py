from config.firebase_config import db


def serialize_document(doc):
    # Perform serialization of the document here
    return doc.to_dict()


class DBUtils:
    def __init__(self):
        self.db = db

    async def get_document(self, collection_name, document_id):
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc = await doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    async def add_document(self, collection_name, document_data):
        doc_ref = self.db.collection(collection_name).document()
        await doc_ref.set(document_data)
        return doc_ref.id

    async def update_document(self, collection_name, document_id, update_data):
        doc_ref = self.db.collection(collection_name).document(document_id)
        await doc_ref.update(update_data)

    async def delete_document(self, collection_name, document_id):
        doc_ref = self.db.collection(collection_name).document(document_id)
        await doc_ref.delete()

    async def get_all_documents(self, collection_name):
        docs = self.db.collection(collection_name).stream()
        documents = []

        for doc in docs:
            serialized_doc = serialize_document(doc)
            serialized_doc['id'] = doc.id  # Add the document ID to the serialized document
            documents.append(serialized_doc)

        return documents


