from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"message": "Voice Agent Backend Running"}

@app.post("/analyze")
def analyze(data: dict):

    print("========== NEW REQUEST ==========")
    print("Request Body:", data)

    transcript = data.get("transcript", "").lower()

    status = "UNKNOWN"

    if (
        "yes" in transcript
        or "taken" in transcript
        or "already" in transcript
        or "completed" in transcript
    ):
        status = "TAKEN"

    elif (
        "no" in transcript
        or "not yet" in transcript
        or "later" in transcript
        or "forgot" in transcript
    ):
        status = "PENDING"

    print("Transcript:", transcript)
    print("Status:", status)

    return {
        "transcript": transcript,
        "status": status
    } 