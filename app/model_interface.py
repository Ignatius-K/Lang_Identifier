from pydantic import BaseModel


class ModelResponse(BaseModel):
    lang: str
    acc: float | None = None


class Model:

    @classmethod
    def detect_language(cls, text):
        response = Model.filter_response(
            Model.predict(text)
        )

        return response

    @classmethod
    def predict(cls, text):
        model_result = ...
        return model_result

    @classmethod
    def filter_response(cls, response):

        filtered_response = ModelResponse(lang="lug")
        return filtered_response
