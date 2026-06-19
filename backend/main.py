from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import (
    AnalyzeRequest,
    AnalyzeResponse,
)

from ai_classifier import (
    classify_medication_response,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Voice Agent Backend Running"
    }


@app.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(
    data: AnalyzeRequest
):

    print(
        "\n========== NEW REQUEST =========="
    )

    transcript = data.transcript

    print(
        "Transcript:",
        transcript
    )

    status, message = (
        classify_medication_response(
            transcript
        )
    )

    print("Status:", status)
    print("Message:", message)

    return AnalyzeResponse(
        transcript=transcript,
        status=status,
        message=message,
    )