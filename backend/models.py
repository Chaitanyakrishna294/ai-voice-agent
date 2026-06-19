from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    transcript: str


class AnalyzeResponse(BaseModel):
    transcript: str
    status: str
    message: str