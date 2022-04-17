from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline

class ContextModelClass():
    
    def __init__(self):
        self.reader = FARMReader(model_name_or_path="../Models/Context Models/Saved Models/roberta_base_squad2", use_gpu=True, num_processes=0)
        self.document_store = FAISSDocumentStore.load("document_store")
        self.retriever = DensePassageRetriever.load("context_model_retriever", self.document_store)
        self.pipeline = ExtractiveQAPipeline(self.reader, self.retriever)
        
        
    def predict(self, query):
        query = query.lower()
        prediction = self.pipeline.run(query=query)
        answers = []
        for answer in prediction['answers']:
            tmp = dict()
            tmp["document_id"] = answer.document_id
            tmp["result"] = answer.answer
            tmp["context"] = answer.context
            answers.append(tmp)

        return {"query":prediction["query"], "answers":answers}
    
        
# context_model = ContextModelClass()
# prediction = context_model.predict("Where is MITS located?")
# print(prediction)