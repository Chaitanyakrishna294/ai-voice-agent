"use client";

import { useEffect, useState } from "react";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

export default function Home() {
  const [mounted, setMounted] = useState(false);

  const [status, setStatus] = useState("");
  const [agentMessage, setAgentMessage] = useState("");

  const medications = [
    "Metformin",
    "Vitamin D",
    "Aspirin",
  ];

  const [currentMedicationIndex, setCurrentMedicationIndex] =
    useState(0);

  const [results, setResults] = useState<
    {
      medication: string;
      status: string;
    }[]
  >([]);

  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  useEffect(() => {
    setMounted(true);
  }, []);

  const speakCurrentMedication = () => {
    const medication =
      medications[currentMedicationIndex];

    const speech =
      new SpeechSynthesisUtterance(
        `Have you taken ${medication} today?`
      );

    speech.lang = "en-US";

    window.speechSynthesis.speak(speech);
  };

  const analyzeResponse = async () => {
    try {
      const response = await fetch(
        "http://localhost:5000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            transcript,
          }),
        }
      );

      const data = await response.json();

      setStatus(data.status);
      setAgentMessage(data.message);

      setResults((prev) => [
        ...prev,
        {
          medication:
            medications[currentMedicationIndex],
          status: data.status,
        },
      ]);

      const responseSpeech =
        new SpeechSynthesisUtterance(
          data.message
        );

      window.speechSynthesis.speak(
        responseSpeech
      );

      setTimeout(() => {
        if (
          currentMedicationIndex <
          medications.length - 1
        ) {
          const nextIndex =
            currentMedicationIndex + 1;

          setCurrentMedicationIndex(
            nextIndex
          );

          const nextMedication =
            medications[nextIndex];

          const nextQuestion =
            new SpeechSynthesisUtterance(
              `Have you taken ${nextMedication} today?`
            );

          window.speechSynthesis.speak(
            nextQuestion
          );
        }
      }, 2500);
    } catch (error) {
      console.error(error);
      setStatus("SERVER ERROR");
    }
  };

  if (!mounted) return null;

  if (!browserSupportsSpeechRecognition) {
    return (
      <div className="p-10">
        Speech Recognition Not Supported
      </div>
    );
  }

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        Re-MIND-eЯ Voice Agent
      </h1>

      <div className="mb-6">
        <h2 className="font-bold">
          Current Medication
        </h2>

        <p>
          {
            medications[
              currentMedicationIndex
            ]
          }
        </p>
      </div>

      <div className="space-x-2">
        <button
          onClick={speakCurrentMedication}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Ask Question
        </button>

        <button
          onClick={() =>
            SpeechRecognition.startListening({
              continuous: true,
              language: "en-US",
            })
          }
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Start Listening
        </button>

        <button
          onClick={() =>
            SpeechRecognition.stopListening()
          }
          className="bg-red-500 text-white px-4 py-2 rounded"
        >
          Stop
        </button>

        <button
          onClick={resetTranscript}
          className="bg-gray-500 text-white px-4 py-2 rounded"
        >
          Reset
        </button>

        <button
          onClick={analyzeResponse}
          className="bg-purple-500 text-white px-4 py-2 rounded"
        >
          Analyze Response
        </button>
      </div>

      <div className="mt-6 border p-4 rounded">
        <h2 className="font-bold">
          Transcript
        </h2>

        <p>{transcript}</p>
      </div>

      <div className="mt-6 border p-4 rounded">
        <h2 className="font-bold">
          Medication Status
        </h2>

        <p>{status}</p>
      </div>

      <div className="mt-6 border p-4 rounded">
        <h2 className="font-bold">
          Agent Response
        </h2>

        <p>{agentMessage}</p>
      </div>

      <div className="mt-6 border p-4 rounded">
        <h2 className="font-bold mb-2">
          Medication Results
        </h2>

        {results.length === 0 ? (
          <p>No responses yet</p>
        ) : (
          results.map((item, index) => (
            <div key={index}>
              {item.medication}
              {" → "}
              {item.status}
            </div>
          ))
        )}
      </div>
    </div>
  );
}