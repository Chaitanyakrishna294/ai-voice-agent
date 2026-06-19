import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def classify_medication_response(
    transcript: str
) -> tuple[str, str]:
    prompt = f"""
You are a healthcare medication adherence classifier.

The patient may respond in ANY language, dialect, script, or transliterated form.

Supported examples include:

English
Hindi
Telugu
Tamil
Kannada
Malayalam
Marathi
Gujarati
Punjabi
Bengali
Urdu

Your task:

Determine whether the patient:

1. Already took medication
2. Has not taken medication yet
3. Will take medication later
4. Gave an unclear response

Return EXACTLY one word:

TAKEN
PENDING
UNKNOWN

Examples:

English:

Yes
TAKEN

Yeah
TAKEN

I took it
TAKEN

I already took it
TAKEN

I took it after breakfast
TAKEN

No
PENDING

Not yet
PENDING

I forgot
PENDING

I will take it later
PENDING


Hindi:

मैंने दवा ले ली
TAKEN

ले लिया
TAKEN

खाने के बाद ले लिया
TAKEN

नहीं
PENDING

अभी नहीं
PENDING

बाद में लूंगा
PENDING

भूल गया
PENDING


Telugu:

నేను మందు వేసుకున్నాను
TAKEN

తీసుకున్నాను
TAKEN

వేసుకున్నాను
TAKEN

అవును
TAKEN

లేదు
PENDING

తీసుకోలేదు
PENDING

ఇంకా తీసుకోలేదు
PENDING

తర్వాత తీసుకుంటాను
PENDING

మర్చిపోయాను
PENDING


Tamil:

நான் மருந்து எடுத்துக்கொண்டேன்
TAKEN

எடுத்துக்கொண்டேன்
TAKEN

இல்லை
PENDING

இன்னும் இல்லை
PENDING

பிறகு எடுத்துக்கொள்கிறேன்
PENDING


Kannada:

ನಾನು ಔಷಧಿ ತೆಗೆದುಕೊಂಡೆ
TAKEN

ತೆಗೆದುಕೊಂಡೆ
TAKEN

ಇಲ್ಲ
PENDING

ಇನ್ನೂ ತೆಗೆದುಕೊಂಡಿಲ್ಲ
PENDING


Malayalam:

ഞാൻ മരുന്ന് കഴിച്ചു
TAKEN

കഴിച്ചു
TAKEN

ഇല്ല
PENDING

ഇനിയും കഴിച്ചിട്ടില്ല
PENDING


Marathi:

मी औषध घेतले
TAKEN

घेतले
TAKEN

नाही
PENDING

नंतर घेईन
PENDING


Gujarati:

મેં દવા લીધી
TAKEN

લીધી
TAKEN

ના
PENDING

પછી લઈશ
PENDING


Punjabi:

ਮੈਂ ਦਵਾਈ ਲੈ ਲਈ
TAKEN

ਲੈ ਲਈ
TAKEN

ਨਹੀਂ
PENDING

ਬਾਅਦ ਵਿੱਚ ਲਵਾਂਗਾ
PENDING


Bengali:

আমি ওষুধ খেয়েছি
TAKEN

খেয়েছি
TAKEN

না
PENDING

পরে খাব
PENDING


Urdu:

میں نے دوا لے لی
TAKEN

لے لی
TAKEN

نہیں
PENDING

بعد میں لوں گا
PENDING


Patient Response:
{transcript}

Return ONLY:

TAKEN
PENDING
UNKNOWN
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        raw_response = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        print("\n===== GROQ RESPONSE =====")
        print(raw_response)

        raw_upper = raw_response.upper()

        if "TAKEN" in raw_upper:
            status = "TAKEN"

        elif "PENDING" in raw_upper:
            status = "PENDING"

        else:
            status = "UNKNOWN"

    except Exception as e:

        print("\n===== GROQ ERROR =====")
        print(e)

        status = "UNKNOWN"

    if status == "TAKEN":

        message = (
            "Thank you. I have recorded "
            "that you took your medication."
        )

    elif status == "PENDING":

        message = (
            "Thank you. I will remind you "
            "again later."
        )

    else:

        message = (
            "Sorry, I did not understand "
            "your response."
        )

    return status, message