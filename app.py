from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form
from app.services.stt_service import transcribe_audio
from app.services.llm_service import generate_question
from app.services.essay_service import generate_essay_structure
from app.utils.memory import ConversationMemory
import uvicorn

app = FastAPI(title="AI Voice Essay Brainstormer")
memory = ConversationMemory()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Voice Essay Brainstormer! Use /voice-input/ to submit your voice and /generate-essay/ to get your essay structure."}

@app.post("/voice-input")
async def voice_input(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    # Case 1: Both missing
    if not file and not text:
        return {"error": "Either file or text input is required"}

    # Case 2: If file is provided → transcribe
    if file:
        transcribed_text = await transcribe_audio(file)
    else:
        transcribed_text = ""

    # Case 3: If text is provided → use directly
    input_text = text if text else transcribed_text

    # If both exist → combine (optional logic)
    if file and text:
        input_text = text + " " + transcribed_text

    # Memory handling
    memory.add_user_message(input_text)

    question = generate_question(input_text, memory.get_history())

    memory.add_ai_message(question)

    return {
        "user_text": input_text,
        "ai_question": question
    }


@app.get("/generate-essay")
def generate_essay():
    history = memory.get_history()
    result = generate_essay_structure(history)

    return {"essay_structure": result}


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Running on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)