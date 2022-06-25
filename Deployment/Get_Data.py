import pandas as pd
from haystack.schema import Document

class GetData:

    def __init__(self):
        self.df = pd.read_csv("Data/mits_data.csv")
        self.documents = self.get_documents()


    def get_documents(self):
        data = self.df
        docs = []

        for row in data.itertuples(index=False):
            content = row.content
            id = row._0
            source = row.source
            for para in content.split("\n\n"):
                if not para.strip():
                    continue

                tmp_doc = Document(content=para)
            tmp_doc.id = str(id)
            tmp_doc.meta = {"source":source}
            tmp_doc.content_type = "str"
            docs.append(tmp_doc)
        
        return docs

# get_data = GetData()
# print(get_data.documents)

