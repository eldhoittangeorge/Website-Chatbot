import time
from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
import numpy as np

class NonContextModelClass():

    def __init__(self) -> None:
        start = time.time()
        print(f"The non context start time is {start}")
        self.model_path = "Saved Models/paraphrase-albert-small-v2/"
        self.data = pd.read_csv("Saved Models/data.csv") 
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModel.from_pretrained(self.model_path)
        self.dataset_embedding = torch.load('Saved Models/chitchat_dataset_embedding.pt')
        end = time.time()
        print(f"The total elapsed time for constructor is {end - start}")


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
        start = time.time()
        query_encoding = self.create_embedding([query])
        cosin_sim = torch.nn.CosineSimilarity()
        qeus_index = np.argmax(cosin_sim(query_encoding, self.dataset_embedding))
        ans = self.data.iloc[qeus_index.item()].Answer
        end = time.time()
        print(f"The total elapsed time for predict is {end - start}")
        return ans



non_context_model = NonContextModelClass()
output = non_context_model.predict("Where are you from")
print(output)

