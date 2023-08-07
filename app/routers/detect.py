from fastapi import APIRouter
from pydantic import BaseModel

# local libraries
from model.model import Model

model = Model()
router = APIRouter()


class RequestBody(BaseModel):
    text: str


class ResponseBody(BaseModel):
    lang: str
    # acc: float | None


@router.post("/")
async def detect(req_body: RequestBody):
    model_response = str(model.detect_language(text=req_body.text))

    return ResponseBody(
        lang=model_response,
        # acc=model_response.acc
    )


__all__ = [
    "router"
]

