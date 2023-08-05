from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# local libraries
from app.model_interface import Model

router = APIRouter()


class RequestBody(BaseModel):
    text: str


class ResponseBody(BaseModel):
    lang: str
    acc: float | None


@router.post("/")
async def detect(req_body: RequestBody):

    model_response = Model.detect_language(text=req_body.text)

    return ResponseBody(
        lang=model_response.lang,
        acc=model_response.acc
    )


__all__ = [
    "router"
]
