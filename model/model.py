import pickle
import joblib

PATH_TO_MODEL = "./model"


class Model:

    def __init__(self):
        self.text = None
        self.model = None
        self.predicted: str | None = None

    def load_model(self, model_name):
        model_path = f"{PATH_TO_MODEL}/{model_name}"
        
        try:
            with open(model_path, 'rb') as _model:
                self.model = pickle.load(_model)

        except pickle.UnpicklingError as e:
            self.model = joblib.load(model_path)

        finally:
            pass

    def detect_language(self, text):
        self.text = text
        self.predict()
        return self.predicted

    def preprocess_text(self):
        ...

    def predict(self):
        self.predicted = self.model.predict([self.text])[0]


if __name__ == '__main__':
    PATH_TO_MODEL = "../model"
    model = Model()
    model.load_model('n_bayes.pkl')
    print(model.detect_language('hello today'))

