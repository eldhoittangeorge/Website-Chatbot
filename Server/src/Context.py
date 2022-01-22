from haystack.utils import print_answers
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline

class ContextModelClass():
    
    def __init__(self):
        self.document_store = FAISSDocumentStore.load("Saved Models/model")
        self.retriever = DensePassageRetriever.load("Saved Models/context_model", self.document_store)
        self.reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True, num_processes=0)
        self.pipeline = ExtractiveQAPipeline(self.reader, self.retriever)
        
        
    def predict(self, query):
        prediction = self.pipeline.run(query=query)
        return prediction
    
        
context_model = ContextModelClass()
print_answers(context_model.predict("Where is MITS located?"))
# print_answers(context_model.predict("Where is MITS located?"))
