import os
import pickle
import numpy as np

# local
from model.text_preprocess import Preprocessor

PATH_TO_MODEL = "./model/model_1.pickle"


class Model:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Model, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.model_prediction = None
        self.preprocessor = Preprocessor()

        with open(PATH_TO_MODEL, "rb") as _model:
            self.model = pickle.load(_model)

    def detect_language(self, text):
        padded_seq_text = self.preprocessor.preprocess(text)
        self.predict(padded_seq_text)
        return self.preprocess_model_result()

    def predict(self, padded_seq_text):
        self.model_prediction = self.model.predict(padded_seq_text)

    def preprocess_model_result(self):
        return np.argmax(self.model_prediction)


