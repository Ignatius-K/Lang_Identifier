from fastapi import APIRouter
from pydantic import BaseModel

# local libraries
from model.model import Model

from database import models
from database.db import engine, local_session

models.BASE.metadata.create_all(bind=engine)


model = Model()
model.load_model('n_bayes_c.pkl')

router = APIRouter()


class RequestBody(BaseModel):
    text: str


class ResponseBody(BaseModel):
    lang: str
    # acc: float | None


@router.post("/")
async def detect(req_body: RequestBody):
    model_response = model.detect_language(text=req_body.text)

    try:
        with local_session() as db:
            db.add(models.Log(
                text=req_body.text,
                lang=model_response
            ))
            db.commit()
    except Exception as e:
        print(e)
    finally:
        return ResponseBody(
            lang=model_response,
            # acc=model_response.acc
        )


__all__ = [
    "router"
]

"""

if __name__ == '__main__':
    with local_session() as db:
        db.add(models.Log(
            text="test text",
            lang="text"
        ))

        db.commit()
"""
