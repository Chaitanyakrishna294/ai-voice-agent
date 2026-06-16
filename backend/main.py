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
    message="Sorry, i didn't understand your response"

    if (
        "yes" in transcript
        or "taken" in transcript
        or "already" in transcript
        or "completed" in transcript
    ):
        status = "TAKEN"
        message = ("Thank you  for the response "
                   "i record your medication. ")

    elif (
        "no" in transcript
        or "not yet" in transcript
        or "later" in transcript
        or "forgot" in transcript
    ):
        status = "PENDING"
        message=("Thank you for the response"
                 "i will remind you later.")

    print("Transcript:", transcript)
    print("Status:", status)
    print("message:",message)

    return {
        "transcript": transcript,
        "status": status,
        "message":message
    } 