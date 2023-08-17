# Trevor's model
import joblib

# Conrad's model
import pickle
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
LANGS = [
    'ach',
    'eng',
    'lugbara',
    'lug',
    'Runyankole',
    'Ateso'
]

PATH_TO_MODEL = "./model"


class Model:

    def __init__(self):
        self.model_name: str | None = None
        self.model = None
        self.text = None
        self.predicted = None

    def load_model(self, model_name):
        model_path = f"{PATH_TO_MODEL}/{model_name}"

        try:
            with open(model_path, 'rb') as _model:
                self.model = pickle.load(_model)

        except pickle.UnpicklingError as e:
            self.model = joblib.load(model_path)

        finally:
            self.model_name = model_name.split('.')[0]

    def detect_language(self, text):
        self.text = text
        self.preprocess_text()
        self.predict()
        if self.model_name == 'n_bayes_t':
            return self.predicted

        return LANGS[self.predicted]

    def preprocess_text(self):
        if self.model_name == "n_bayes_t":
            self.text = [self.text]
            return

        with open(f"{PATH_TO_MODEL}/c_transformer.pkl", "rb") as f:
            cv = pickle.load(f)

        text = self.text.lower()
        text = text.split()
        text = word_tokenize(str(text))
        text = ' '.join(text)
        self.text = cv.transform([text]).toarray()

    def predict(self):
        self.predicted = self.model.predict(self.text)[0]


if __name__ == '__main__':
    PATH_TO_MODEL = "../model"
    model = Model()
    model.load_model('n_bayes_c.pkl')
    print(model.detect_language('hello today'))
