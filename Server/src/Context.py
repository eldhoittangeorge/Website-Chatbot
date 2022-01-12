from haystack.utils import  convert_files_to_dicts, print_answers
from haystack.nodes import FARMReader
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever
from haystack.pipelines import ExtractiveQAPipeline

document_store = FAISSDocumentStore(faiss_index_factory_str="Flat")

# doc_dir = "../../Site Data/Data"
# dicts = convert_files_to_dicts(dir_path=doc_dir,split_paragraphs=True)
# document_store.write_documents(dicts)

retriever = DensePassageRetriever(document_store=document_store,
                                 query_embedding_model='facebook/dpr-question_encoder-single-nq-base',
                                 passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',
                                 max_seq_len_query=64,
                                 max_seq_len_passage=256,
                                 batch_size=16,
                                 use_gpu=True,
                                 embed_title=True,
                                 use_fast_tokenizers=True)
document_store.update_embeddings(retriever)

reader = FARMReader(model_name_or_path="deepset/roberta-large-squad2", use_gpu=True)

pipeline = ExtractiveQAPipeline(reader, retriever)

prediction = pipeline.run(query="Where is mits located?",
                         params = {"Retriever":{"top_k":10}, 
                                  "Reader":{"top_k":10}})

# print_answers(prediction,details="minimum")


