from haystack.utils import print_answers
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader, TransformersReader
from haystack.pipelines import ExtractiveQAPipeline

class ContextModelClass():
    
    def __init__(self):
        self.reader = FARMReader(model_name_or_path="src/Saved Models/roberta_base_squad2", use_gpu=True, num_processes=0)
        self.document_store = FAISSDocumentStore.load("src/Saved Models/model")
        self.retriever = DensePassageRetriever.load("src/Saved Models/context_model", self.document_store)
        self.pipeline = ExtractiveQAPipeline(self.reader, self.retriever)
        
        
    def predict(self, query):
        prediction = self.pipeline.run(query=query)
        return prediction
    
        
# context_model = ContextModelClass()
# context_model.predict("Where are you from")