import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

PATH_TO_TOKENIZER = "./model/tokenizer.pickle"
MAX_LENGTH = 150


class Preprocessor:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Preprocessor, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.text = None
        self.text_sequence = None
        self.padded_sequence = None
        with open(PATH_TO_TOKENIZER, "rb") as _tokenizer:
            self.tokenizer = pickle.load(_tokenizer)

    def preprocess(self, text):
        self.text = text
        self.tokenize()
        self.pad_sequence()
        return self.padded_sequence

    def tokenize(self):
        self.text_sequence = self.tokenizer.texts_to_sequences([self.text])

    def pad_sequence(self):
        self.padded_sequence = pad_sequences(self.text_sequence,
                                             MAX_LENGTH)


