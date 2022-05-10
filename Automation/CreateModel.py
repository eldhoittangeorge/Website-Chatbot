from haystack.nodes import FARMReader
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever
from haystack.pipelines import ExtractiveQAPipeline
from pymongo import MongoClient
from haystack.schema import Document
# import config
from configparser import ConfigParser


class ModelCreator():

    def __init__(self) -> None:
        print("Initailization started")
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.client = MongoClient(self.config.get("Database", "mongodb_uri"))
        self.db= self.client[self.config.get("Database", "mongodb_database")]
        self.collection = self.db[self.config.get("Crawler", "crawler_name")]
        # self.client = MongoClient(config.MONGODB_URI)
        # self.db = self.client[config.MONOGODB_DATABASE]
        # self.collection = self.db[config.CRAWLER_NAME]
        self.documents = self.load_documents()
        self.document_store = FAISSDocumentStore(faiss_index_factory_str="Flat")
        self.pipeline = None
        self.retriever = None
        self.reader = None
        print("Initailization ended")

    def load_documents(self):
        docs = []
        for document in self.collection.find({}):
            content = document['content']
            for para in content.split("\n\n"):
                if not para.strip():
                    continue

                tmp_doc = Document(content=para)
                tmp_doc.id = str(document["_id"])
                tmp_doc.meta = {"source": document['source'], }
                tmp_doc.content_type = "str"
                docs.append(tmp_doc)

        return docs


    def create_retriever_reader(self):
        print("Model creation started")
        self.document_store.write_documents(self.documents)

        self.retriever = DensePassageRetriever(document_store=self.document_store,
            query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
            passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',
            max_seq_len_passage=512,
            max_seq_len_query=64,
            batch_size=16,
            use_gpu=True,
            embed_title=True,
            use_fast_tokenizers=True,
            similarity_function="cosine")
        print("Retriever initialized")
        self.document_store.update_embeddings(self.retriever)

        self.reader = FARMReader(model_name_or_path="../Models/Context Models/Saved Models/roberta_base_squad2/", use_gpu=True,
            num_processes=0)        
        print("Reader initialized")

        self.pipeline = ExtractiveQAPipeline(reader=self.reader, retriever=self.retriever) 
        print("Model creation ended")


    def create_and_save(self):
        self.create_retriever_reader()
        print("Model saving started")
        self.retriever.save("context_model_retriever")
        self.document_store.save("document_store")        
        print("Model saving ended")

# if __name__ == '__main__':
#     model_creator = ModelCreator()
#     model_creator.create_and_save()

