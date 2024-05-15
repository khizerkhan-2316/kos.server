from datetime import datetime
import pytz

from config.firebase_config import db
from google.cloud import firestore


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
        doc_ref.set(document_data)
        return doc_ref.id

    async def update_document(self, collection_name, document_id, update_data):
        update_data['updated_at'] = firestore.SERVER_TIMESTAMP
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.update(update_data)

    async def delete_document(self, collection_name, document_id):
        doc_ref = self.db.collection(collection_name).document(document_id)
        await doc_ref.delete()

    async def get_all_documents(self, collection_name):
        docs = self.db.collection(collection_name).stream()
        documents = []

        for doc in docs:
            # Serialize the document
            serialized_doc = serialize_document(doc)

            # Add the document ID to the serialized document
            serialized_doc['id'] = doc.id

            # Retrieve 'created_at' field from the serialized document
            created_at = serialized_doc.get('created_at')
            local_timezone = pytz.timezone('Europe/Copenhagen')

            if created_at is not None:
                # Handle 'created_at' field if present
                try:

                    serialized_doc['created_at'] = created_at.astimezone(local_timezone).strftime("%d-%m-%Y %H:%M:%S")
                except ValueError as e:
                    # Log the error or handle it as needed
                    print(f"Error converting 'created_at' field: {e}")

            # Retrieve 'updated_at' field from the serialized document
            updated_at = serialized_doc.get('updated_at')

            if updated_at is not None:
                # Handle 'updated_at' field if present
                try:
                    serialized_doc['updated_at'] = updated_at.astimezone(local_timezone).strftime("%d-%m-%Y %H:%M:%S")
                except ValueError as e:
                    # Log the error or handle it as needed
                    print(f"Error converting 'updated_at' field: {e}")

            documents.append(serialized_doc)

        return documents
