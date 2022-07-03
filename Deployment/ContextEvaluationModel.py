from transformers import TextClassificationPipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np


class ContextEvaluationModel:

    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
        self.model = AutoModelForSequenceClassification.from_pretrained('../Models/Context Evaluation Model/results/checkpoint-12000')
        self.pipeline = TextClassificationPipeline(model = self.model, tokenizer = self.tokenizer)


    def predict(self, query):
        result = self.pipeline(query)
        result = 0 if result == "LABEL_0" else 1
        return result


# context_evaluation_model = ContextEvaluationModel()
# print(context_evaluation_model.predict('who is the principal of mits'))