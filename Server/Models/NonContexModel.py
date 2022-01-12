from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
import numpy as np

class NonContextModelClass():

    def __init__(self) -> None:
        self.model_name = "sentence-transformers/paraphrase-albert-small-v2"
        self.data = pd.read_csv("data.csv") 
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)
        self.dataset_embedding = torch.load('chitchat_dataset_embedding.pt')


    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


    def create_embedding(self, data):
        encoded_input = self.tokenizer(list(data), padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        sentence_embedding = self.mean_pooling(model_output, encoded_input['attention_mask'])
        return sentence_embedding


    def predict(self, query):
        query_encoding = self.create_embedding([query])
        cosin_sim = torch.nn.CosineSimilarity()
        qeus_index = np.argmax(cosin_sim(query_encoding, self.dataset_embedding))
        ans = self.data.iloc[qeus_index.item()].Answer
        return ans



non_context_model = NonContextModelClass()
output = non_context_model.predict("Where are you from")
print(output)

