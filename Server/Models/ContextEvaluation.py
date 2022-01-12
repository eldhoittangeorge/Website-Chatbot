import torch
from joblib import load
from transformers import DistilBertTokenizer, DistilBertModel


class ContextEvalutaionClass():

    def __init__(self) -> None:
        self.model_name = "distilbert-base-uncased"
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_name)
        self.model = DistilBertModel.from_pretrained(self.model_name)

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
        model = load("context_evaluation_model.joblib")
        embedding = self.create_embedding([data])
        prediction = model.predict(embedding)[0]
        return prediction


context_evaluation_model = ContextEvalutaionClass()
result = context_evaluation_model.predict("What is the name of the hod")
print(result)
    