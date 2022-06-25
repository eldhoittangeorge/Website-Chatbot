import torch
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

class NonContextModel:

    def __init__(self) -> None:
        self.dataset_encoding = torch.load("../Models/Non Context Models/Data/chitchat_dataset_embedding.pt")
        self.model = SentenceTransformer('sentence-transformers/paraphrase-albert-small-v2')
        self.dataset = pd.read_csv("../Models/Non Context Models/Data/data.csv")


    def predict(self, query):
        query_encoding = self.model.encode(query)
        question_index = np.argmax(util.cos_sim(query_encoding, self.dataset_encoding)).item()
        question_data = self.dataset.iloc[question_index]
        return question_data.Answer



non_context_model = NonContextModel()
print(non_context_model.predict("Who are you"))

        
