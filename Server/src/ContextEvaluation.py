import time
import torch
from joblib import load
from transformers import DistilBertTokenizer, DistilBertModel


class ContextEvalutaionClass():

    def __init__(self) -> None:
        start = time.time() 
        self.model_name = "distilbert-base-uncased"
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_name)
        self.model = DistilBertModel.from_pretrained(self.model_name)
        self.pretrained_model = load('src/Saved Models/context_evaluation_model.joblib')
        end = time.time()
        print(f"the total elapsed time in constructor is {end - start}")

    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def create_embedding(self, data):
        encoded_input = self.tokenizer(data, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            output = self.model(**encoded_input)
        embedding = self.mean_pooling(output, encoded_input["attention_mask"])
        return embedding.numpy()

    def predict(self, data):
        # start = time.time()
        # model = load("context_evaluation_model.joblib")
        embedding = self.create_embedding([data])
        prediction = self.pretrained_model.predict(embedding)[0]
        # end = time.time()
        # print(f"The total elapsed time in prediction is {end - start}")
        return prediction


# context_evaluation_model = ContextEvalutaionClass()
# result = context_evaluation_model.predict("What is the name of the hod")
# print(result)
    