from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader
from haystack.utils import print_answers
from haystack.pipelines import ExtractiveQAPipeline
from Get_Data import GetData

class ContextModelClass():
    
    def __init__(self):
        self.reader = FARMReader(model_name_or_path="Reader Models/roberta_base_squad2", use_gpu=True, num_processes=0)
        self.document_store = self._create_doc_store() 
        self.retriever = DensePassageRetriever.load("context_model_retriever", self.document_store)
        self.document_store.update_embeddings(retriever=self.retriever)
        self.pipeline = ExtractiveQAPipeline(self.reader, self.retriever)
        

    def _create_doc_store(self):
        get_data = GetData() 
        document_store = InMemoryDocumentStore()
        document_store.write_documents(get_data.documents)
        return document_store
        
    def predict(self, query):
        query = query.lower()
        prediction = self.pipeline.run(query=query)
        print_answers(prediction)
        answers = []
        for answer in prediction['answers']:
            tmp = dict()
            tmp["document_id"] = answer.document_id
            tmp["result"] = answer.answer
            tmp["context"] = answer.context
            tmp["source"] = answer.meta['source']
            answers.append(tmp)

        return {"query":prediction["query"], "answers":answers}
    
        
# context_model = ContextModelClass()
# prediction = context_model.predict("Where is MITS located?")
# print(prediction)