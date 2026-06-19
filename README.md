# AI Voice Agent

## Overview

An AI-powered voice agent that converts speech to text and enables intelligent voice interactions using modern AI technologies.

## Tech Stack

* Frontend: Next.js, TypeScript
* Backend: Python
* Speech Recognition
* AI/LLM Integration

---

## Sprint 1 ✅ Completed

### Goals

* Project planning and architecture design
* Technology stack selection
* Repository setup

### Completed

* Defined project scope
* Designed frontend/backend architecture
* Created initial project structure

---

## Sprint 2 ✅ Completed

### Goals

* Frontend development
* User interface implementation

### Completed

* Created Next.js application
* Built UI components
* Added voice interaction interface

---

## Sprint 3 ✅ Completed

### Goals

* Backend development
* Speech processing integration

### Completed

* Developed Python backend
* Implemented API endpoints
* Connected speech recognition pipeline

---

## Sprint 4 ✅ Completed

### Goal:
Make the AI Voice Agent respond naturally instead of only returning a status.

### Completed:

Added response generation in the backend
Enhanced FastAPI endpoint to return status and message
Implemented conversation flow handling
Added agent response display in the frontend
Integrated browser Text-to-Speech (TTS)
Enabled voice feedback loop

#### Example:

User: "Yes, I already took it"

Agent: "Thank you. I have recorded that you took your medication."

## Sprint 5 ✅ Completed

**Goal:**
Enable the voice agent to conduct a complete medication review session by asking about multiple medications sequentially.

**Completed:**

* Added support for multiple medications
* Implemented sequential medication questioning
* Stored medication responses during the session
* Added medication results summary view
* Automated progression to the next medication
* Enhanced voice interaction flow

### Sprint 6 ✅ Completed

**Goal:**
Introduce conversation state management to support structured medication review sessions.

**Completed:**

* Added medication session tracking
* Implemented current medication state management
* Added completed medication tracking
* Added medication results summary
* Enabled sequential medication workflow
* Improved conversation flow between medications

**Outcome:**
Successfully transformed the agent from a single-question assistant into a structured medication review assistant capable of managing complete medication sessions.

### Sprint 7 ✅ Completed

**Goal:**
Transform the voice agent from a keyword-based classifier into an AI-powered multilingual medication assistant.

**Completed:**

* Integrated Groq API with Llama 3.1 8B
* Replaced keyword matching with AI reasoning
* Added AI-powered medication intent classification
* Added multilingual speech recognition support
* Implemented language selection
* Added Telugu, Hindi, Tamil, Kannada, Malayalam, Marathi, Gujarati, and Bengali support
* Preserved multi-medication conversation workflow
* Improved natural language understanding across multiple languages

**Outcome:**
Successfully upgraded the agent from a rule-based system to an AI-powered multilingual medication assistant capable of understanding natural language responses across multiple languages.


## Future Enhancements

* Multi-language support
* Speaker identification
* Conversation memory
* Cloud deployment
* Real-time streaming audio
